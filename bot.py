import discord
from discord import app_commands, ui
import os

# Wstaw tutaj swój token bota
TOKEN = "TWÓJ_TOKEN_TUTAJ"

# ID ról i kanałów
ROLE_PASZPORT_ID = 1138467540201394322
ROLE_ZARZAD_MIASTA_ID = 1414310002390470730
ROLE_POLICJA_ID = 1415073475265167482
ROLE_PING_ID = 1138467540201394326

# Definicja klas Modali
class WdowodModal(ui.Modal, title='Formularz paszportowy'):
    imie_nazwisko = ui.TextInput(label='1. Imię i Nazwisko', style=discord.TextStyle.short, required=True, min_length=3)
    data_urodzenia = ui.TextInput(label='2. Data urodzenia', style=discord.TextStyle.short, required=True, min_length=3)
    obywatelstwo = ui.TextInput(label='3. Obywatelstwo', style=discord.TextStyle.short, required=True, min_length=3)
    ktora_postac = ui.TextInput(label='4. Która Postać', style=discord.TextStyle.short, required=True, min_length=3)

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            f"**Wniosek o dowód dla {interaction.user.mention}**\n\n"
            f"**1. Imię i Nazwisko:** {self.imie_nazwisko}\n"
            f"**2. Data urodzenia:** {self.data_urodzenia}\n"
            f"**3. Obywatelstwo:** {self.obywatelstwo}\n"
            f"**4. Która Postać:** {self.ktora_postac}",
            ephemeral=False
        )
        # Nadanie roli po wypełnieniu formularza
        member = interaction.user
        role = interaction.guild.get_role(ROLE_PASZPORT_ID)
        if role:
            await member.add_roles(role)

class WystawWyrokModal(ui.Modal, title='Wystawianie wyroku'):
    obywatel_nick = ui.TextInput(label='Nick Discord obywatela', required=True)
    obywatel_imie = ui.TextInput(label='Imię i Nazwisko obywatela', required=True)
    obywatel_data = ui.TextInput(label='Data urodzenia IC obywatela', required=True)
    funkcjonariusz_imie = ui.TextInput(label='Imie i Nazwisko Funkcjonariusza', required=True)
    funkcjonariusz_odznaka = ui.TextInput(label='Numer odznaki funkcjonariusza', required=True)
    funkcjonariusz_podpis = ui.TextInput(label='Podpis funkcjonariusza', required=True)
    powod = ui.TextInput(label='Powód', style=discord.TextStyle.long, required=True)
    dlugosc = ui.TextInput(label='Długość', required=True)
    dodatkowe = ui.TextInput(label='Dodatkowe', style=discord.TextStyle.long, required=False)

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            f"**Wystawienie wyroku**\n\n"
            f"**Nick Discord obywatela:** {self.obywatel_nick}\n"
            f"**Imię i Nazwisko obywatela:** {self.obywatel_imie}\n"
            f"**Data urodzenia IC obywatela:** {self.obywatel_data}\n"
            f"**Imię i Nazwisko Funkcjonariusza:** {self.funkcjonariusz_imie}\n"
            f"**Numer odznaki funkcjonariusza:** {self.funkcjonariusz_odznaka}\n"
            f"**Podpis funkcjonariusza:** {self.funkcjonariusz_podpis}\n"
            f"**Powód:** {self.powod}\n"
            f"**Długość:** {self.dlugosc}\n"
            f"**Dodatkowe:** {self.dodatkowe}"
        )

class WystawMandatModal(ui.Modal, title='Wystawianie mandatu'):
    powod = ui.TextInput(label='Powód', style=discord.TextStyle.long, required=True)
    kwota = ui.TextInput(label='Kwota', required=True)
    obywatel_nick = ui.TextInput(label='Nick discord Obywatela', required=True)
    obywatel_imie = ui.TextInput(label='Imię i Nazwisko Obywatela', required=True)
    funkcjonariusz_imie = ui.TextInput(label='Imie i Nazwisko Funkcjonariusza', required=True)
    funkcjonariusz_odznaka = ui.TextInput(label='Numer odznaki Funkcjonariusza', required=True)

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            f"**Wystawienie mandatu**\n\n"
            f"**Powód:** {self.powod}\n"
            f"**Kwota:** {self.kwota}\n"
            f"**Nick discord Obywatela:** {self.obywatel_nick}\n"
            f"**Imię i Nazwisko Obywatela:** {self.obywatel_imie}\n"
            f"**Imie i Nazwisko Funkcjonariusza:** {self.funkcjonariusz_imie}\n"
            f"**Numer odznaki Funkcjonariusza:** {self.funkcjonariusz_odznaka}"
        )

class AwansDegradModal(ui.Modal, title='Awans/Degradacja'):
    kto_dostaje = ui.TextInput(label='Kto dostaje', required=True)
    kto_nadaje = ui.TextInput(label='Kto nadaje', required=True)
    z_jakiej_rangi = ui.TextInput(label='Z jakiej rangi', required=True)
    na_jaka_range = ui.TextInput(label='Na jaką rangę', required=True)
    powod = ui.TextInput(label='Powód', style=discord.TextStyle.long, required=True)
    data = ui.TextInput(label='Data', required=True)

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            f"**Awans/Degradacja dla: {self.kto_dostaje}**\n\n"
            f"**Kto nadaje:** {self.kto_nadaje}\n"
            f"**Z jakiej rangi:** {self.z_jakiej_rangi}\n"
            f"**Na jaką rangę:** {self.na_jaka_range}\n"
            f"**Powód:** {self.powod}\n"
            f"**Data:** {self.data}"
        )

class AktywnoscModal(ui.Modal, title='Aktywność'):
    ktora_aktywnosc = ui.TextInput(label='1. Która aktywność', required=True)
    dopiska = ui.TextInput(label='2. Dopiska', style=discord.TextStyle.long, required=False)

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            f"**Raport aktywności**\n\n"
            f"**1. Która aktywność:** {self.ktora_aktywnosc}\n"
            f"**2. Dopiska:** {self.dopiska}\n"
            f"**Ping:** <@&{ROLE_PING_ID}>"
        )

# Definicja bota
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    await tree.sync()
    print(f'Zalogowano jako {client.user}')

@tree.command(name="wdowod", description="Formularz do wyrobienia dowodu osobistego.")
async def wdowod_command(interaction: discord.Interaction):
    await interaction.response.send_modal(WdowodModal())

@tree.command(name="wystaw-wyrok", description="Wystaw wyrok dla obywatela.")
async def wystaw_wyrok_command(interaction: discord.Interaction):
    if any(role.id == ROLE_POLICJA_ID for role in interaction.user.roles):
        await interaction.response.send_modal(WystawWyrokModal())
    else:
        await interaction.response.send_message("Nie masz uprawnień do użycia tej komendy.", ephemeral=True)

@tree.command(name="wystaw-mandat", description="Wystaw mandat dla obywatela.")
async def wystaw_mandat_command(interaction: discord.Interaction):
    if any(role.id == ROLE_POLICJA_ID for role in interaction.user.roles):
        await interaction.response.send_modal(WystawMandatModal())
    else:
        await interaction.response.send_message("Nie masz uprawnień do użycia tej komendy.", ephemeral=True)

@tree.command(name="rpstart", description="Ogłoszenie rozpoczęcia RolePlay.")
async def rpstart_command(interaction: discord.Interaction):
    if any(role.id == ROLE_ZARZAD_MIASTA_ID for role in interaction.user.roles):
        role_to_ping = interaction.guild.get_role(ROLE_PING_ID)
        await interaction.response.send_message(
            f"**RolePlay rozpoczęty** zapraszamy wszystkich graczy.\n"
            f"Kod do gry: PLDRP\n"
            f"Ping: {role_to_ping.mention}"
        )
    else:
        await interaction.response.send_message("Nie masz uprawnień do użycia tej komendy.", ephemeral=True)

@tree.command(name="rpkoniec", description="Ogłoszenie zakończenia RolePlay.")
async def rpkoniec_command(interaction: discord.Interaction):
    if any(role.id == ROLE_ZARZAD_MIASTA_ID for role in interaction.user.roles):
        await interaction.response.send_message(
            "**RolePlay Zakończony** dziękujemy za dzisiaj, miłego dnia! <3"
        )
    else:
        await interaction.response.send_message("Nie masz uprawnień do użycia tej komendy.", ephemeral=True)

@tree.command(name="awans-degrad", description="Wypełnij formularz awansu/degradacji.")
async def awans_degrad_command(interaction: discord.Interaction):
    if any(role.id == ROLE_ZARZAD_MIASTA_ID for role in interaction.user.roles):
        await interaction.response.send_modal(AwansDegradModal())
    else:
        await interaction.response.send_message("Nie masz uprawnień do użycia tej komendy.", ephemeral=True)

@tree.command(name="aktywnosc", description="Wypełnij formularz aktywności.")
async def aktywnosc_command(interaction: discord.Interaction):
    if any(role.id == ROLE_ZARZAD_MIASTA_ID for role in interaction.user.roles):
        await interaction.response.send_modal(AktywnoscModal())
    else:
        await interaction.response.send_message("Nie masz uprawnień do użycia tej komendy.", ephemeral=True)

# Uruchomienie bota
client.run(TOKEN)
