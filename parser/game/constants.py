import enum

# script filenames
FIGUREN_COD = "figuren.cod"
HAEUSER_COD = "haeuser.cod"

# This section contains enums and constants referenced in the HAEUSER.COD and
# FIGUREN.COD script files.

# original game files refer to these as "Ware"
Resource = enum.IntEnum(
    "Resource",
    [
        "NOWARE",
        "ALLWARE",
        "EISENERZ",
        "GOLD",
        "WOLLE",
        "ZUCKER",
        "TABAK",
        "FLEISCH",
        "KORN",
        "MEHL",
        "EISEN",
        "SCHWERTER",
        "MUSKETEN",
        "KANONEN",
        "NAHRUNG",
        "TABAKWAREN",
        "GEWUERZE",
        "KAKAO",
        "ALKOHOL",
        "STOFFE",
        "KLEIDUNG",
        "SCHMUCK",
        "WERKZEUG",
        "HOLZ",
        "ZIEGEL",
        "GETREIDE",
        "TABAKBAUM",
        "GEWUERZBAUM",
        "ZUCKERROHR",
        "BAUMWOLLE",
        "WEINTRAUBEN",
        "KAKAOBAUM",
        "GRAS",
        "BAUM",
        "STEINE",
        "ERZE",
        "WILD",
        "FISCHE",
    ],
)

# original game files refer to these as "Bauinfra"
InfrastructureLevel = enum.IntEnum(
    "InfrastructureLevel",
    [
        "INFRA_NIX",
        "INFRA_MARKT",
        "INFRA_KAPELLE",
        "INFRA_SCHULE",
        "INFRA_WIRT",
        "INFRA_KIRCHE",
        "INFRA_BADE",
        "INFRA_THEATER",
        "INFRA_HOCHSCHULE",
        "INFRA_ARZT",
        "INFRA_GALGEN",
        "INFRA_SCHLOSS",
        "INFRA_KATHETRALE",
        "INFRA_TRIUMPH",
        "INFRA_DENKMAL",
        "INFRA_STUFE_1A",
        "INFRA_STUFE_2A",
        "INFRA_STUFE_2B",
        "INFRA_STUFE_2C",
        "INFRA_STUFE_2D",
        "INFRA_STUFE_2E",
        "INFRA_STUFE_2F",
        "INFRA_STUFE_3A",
        "INFRA_STUFE_2G",
        "INFRA_STUFE_3B",
        "INFRA_STUFE_3C",
        "INFRA_STUFE_3D",
        "INFRA_STUFE_3E",
        "INFRA_STUFE_3F",
        "INFRA_STUFE_4A",
        "INFRA_STUFE_4B",
        "INFRA_STUFE_5A",
        "INFRA_STUFE_5B",
    ],
)

# original game files refer to these as "Kind"
BuildingKind = enum.IntEnum(
    "BuildingKind",
    [
        "UNUSED",
        "BADEHAUS",
        "BERGWERK",
        "BODEN",
        "BRANDECK",
        "BRANDUNG",
        "BRUECKE",
        "BRUNNEN",
        "DENKMAL",
        "FELS",
        "FISCHEREI",
        "FLUSS",
        "FLUSSECK",
        "GALGEN",
        "GEBAEUDE",
        "HAFEN",
        "HANDWERK",
        "HANG",
        "HANGECK",
        "HANGQUELL",
        "HOCHSCHULE",
        "HQ",
        "JAGDHAUS",
        "KAPELLE",
        "KIRCHE",
        "KLINIK",
        "KONTOR",
        "MARKT",
        "MAUER",
        "MAUERSTRAND",
        "MEER",
        "MILITAR",
        "MINE",
        "MUENDUNG",
        "PIER",
        "PIRATWOHN",
        "PLANTAGE",
        "PLATZ",
        "pMAUER",
        "ROHSTERZ",
        "ROHSTOFF",
        "ROHSTWACHS",
        "RUINE",
        "SCHLOSS",
        "SCHULE",
        "STEINBRUCH",
        "STRAND",
        "STRANDECKA",
        "STRANDECKI",
        "STRANDHAUS",
        "STRANDMUND",
        "STRANDRUINE",
        "STRANDVARI",
        "STRASSE",
        "THEATER",
        "TOR",
        "TRIUMPH",
        "TURM",
        "TURMSTRAND",
        "WACHTURM",
        "WALD",
        "WEIDETIER",
        "WERFT",
        "WIRT",
        "WMUEHLE",
        "WOHNUNG",
    ],
)

# original game files refer to these as "Bausample"
AudioSample = enum.IntEnum(
    "AudioSample",
    [
        "WAV_NIX",
        "WAV_SHOTKAN1",
        "WAV_SHOTKAN2",
        "WAV_SHOTKAN3",
        "WAV_SHOTKAN4",
        "WAV_SHOTMUS",
        "WAV_HITSWORD1",
        "WAV_HITSWORD2",
        "WAV_HITSWORD3",
        "WAV_HITSWORD4",
        "WAV_HITSWORD5",
        "WAV_DEADGUY1",
        "WAV_DEADGUY2",
        "WAV_MAEHEN",
        "WAV_DONGEL",
        "WAV_HACK1",
        "WAV_HACK2",
        "WAV_STEIN1",
        "WAV_STEIN2",
        "WAV_MUH1",
        "WAV_MUH2",
        "WAV_MUEHLE",
        "WAV_WEBEREI",
        "WAV_SCHAF1",
        "WAV_SCHAF2",
        "WAV_SCHAF3",
        "WAV_BAUM",
        "WAV_VOGEL1",
        "WAV_VOGEL2",
        "WAV_VOGEL3",
        "WAV_VOGEL4",
        "WAV_VOGEL5",
        "WAV_VOGEL6",
        "WAV_WELLEN",
        "WAV_SELEC",
        "WAV_EVENT",
        "WAV_STANDARD",
        "WAV_KONTOR",
        "WAV_MARKT",
        "WAV_SCHLOSS",
        "WAV_KAPELLE",
        "WAV_KIRCHE",
        "WAV_KATHETRALE",
        "WAV_SCHULE",
        "WAV_THEATER",
        "WAV_BURG",
        "WAV_ARZT",
        "WAV_BADEHAUS",
        "WAV_BAECKER",
        "WAV_DENKMAL",
        "WAV_FISCHER",
        "WAV_FLEISCHER",
        "WAV_FOERSTER",
        "WAV_HIRSCH",
        "WAV_STEINMETZ",
        "WAV_SCHMIEDE",
        "WAV_SCHWERTBAU",
        "WAV_GIESSEREI",
        "WAV_JAGDHUETTE",
        "WAV_PLANTAGE",
        "WAV_PIRATEN",
        "WAV_PYRAMIDE",
        "WAV_RUMBRENNER",
        "WAV_BRUNNEN",
        "WAV_TRIUMPH",
        "WAV_TORE",
        "WAV_VULKAN",
        "WAV_WIRTSHAUS",
        "WAV_WOHNHAUS",
        "WAV_MINE",
        "WAV_VULKAN1",
        "WAV_VULKAN2",
        "WAV_VULKAN3",
        "WAV_VULKAN4",
        "WAV_SOLDATTK1",
        "WAV_SOLDATTK2",
        "WAV_SOLDATTK3",
        "WAV_SOLDATTK4",
        "WAV_SOLDATTK5",
        "WAV_SOLDATTK6",
        "WAV_SHIPATTK1",
        "WAV_SHIPATTK2",
        "WAV_SHIPATTK3",
        "WAV_SHIPATTK4",
        "WAV_SOLDMOVE1",
        "WAV_SOLDMOVE2",
        "WAV_SOLDMOVE3",
        "WAV_SOLDMOVE4",
        "WAV_SHIPMOVE1",
        "WAV_SHIPMOVE2",
        "WAV_SHIPMOVE3",
        "WAV_SHIPMOVE4",
    ],
)

# original game files refer to these as "Ruinenr"
Ruins = enum.IntEnum(
    "Ruins",
    [
        "NORUINE",
        "RUINE_FELD",
        "RUINE_HOLZ",
        "RUINE_KONTOR_1",
        "RUINE_KONTOR_N1",
        "RUINE_KONTOR_N2",
        "RUINE_MARKT",
        "RUINE_MINE",
        "RUINE_ROAD_FELD",
        "RUINE_ROAD_STEIN",
        "RUINE_STEIN",
    ],
)

# original game files refer to these as "Figurnr", "Rauchfignr", "Hitfignr", and more

Character = enum.IntEnum(
    "Character",
    [
        "UNUSED",
        # SOLDAT.BSH
        "SOLDAT1",
        "SOLDAT2",
        "SOLDAT3",
        "SOLDAT4",
        "KAVALERIE1",
        "KAVALERIE2",
        "KAVALERIE3",
        "KAVALERIE4",
        "KANONIER1",
        "KANONIER2",
        "KANONIER3",
        "KANONIER4",
        "MUSKETIER1",
        "MUSKETIER2",
        "MUSKETIER3",
        "MUSKETIER4",
        "KANONTURM",
        "PIRATTURM",
        "SPEER1",
        # SHIP.BSH
        "HANDEL1",
        "HANDELD1",
        "HANDEL2",
        "HANDELD2",
        "KRIEG1",
        "KRIEGD1",
        "KRIEG2",
        "KRIEGD2",
        "HANDLER",
        "HANDLERD",
        "PIRAT",
        "PIRATD",
        "BUGH",
        "FAHNE1",
        "FAHNE2",
        "FAHNE3",
        "FAHNE4",
        "FAHNEPIRAT",
        "FAHNEWEISS",
        "KANONSHOT1",
        "KANONSHOT2",
        "KANONSHOTTURM",
        "KANONSHOTTURM2",
        "FAHNEMARKT",
        "FAHNEKONTOR",  # not part of FIGUREN.COD, but referenced in HAEUSER.COD
        "FAHNEKONTOR1",
        "FAHNEKONTOR2",
        "FAHNEKONTOR3",
        "FAHNEKONTOR4",
        "FAHNETURM1",
        "FAHNETURM2",
        "FAHNETURM3",
        # GAUKLER.BSH
        "GAUKLER1",
        # TRAEGER.BSH
        "TRAEGER",
        "PACKESEL",
        "KARREN",
        "FLEISCHER",
        "ARZT",
        "TRADER1",
        "LOESCH",
        "RAEUBER",
        "TRAEGER2",
        "ADELWEIBL",
        "ADEL",
        "ALTER",
        "FRAU",
        "PASSANT",
        "VETERAN",
        "KINDREIF",
        "PILGER",
        # MAEHER.BSH
        "MAEHER",
        "STEINKLOPFER",
        "HOLZFAELLER",
        "PFLUECKER",
        "PFLUECKER2",
        "JAEGER",
        "FISCHER",
        # TIERE.BSH
        "RIND",
        "SCHAF",
        "HIRSCH",
        "ANTILOPE",
        # EFFEKTE.BSH
        "TREFFKAN1",
        "TREFFKAN2",
        "TREFFMUS",
        "UNTERGANG",
        "NOAKTIV",
        "BRANDMARKT",
        "RAUCHBAECK",
        "RAUCHSCHMELZ",
        "RAUCHWERKZEUG",
        "RAUCHGOLD",
        "RAUCHSCHWERT",
        "RAUCHMUSKET",
        "RAUCHBRENNER",
        "RAUCHKANONEN",
        "SENSENMANN",
        "VULKAN",
        "SHOWEISEN",
        "SHOWGOLD",
        "VULKANFIRE1",
        "SHIPSUNK",
        # SCHATTEN.BSH
        "SCHATTEN",
        "SCHATTENLANG",
        "SCHILD",
        # FISCHE.BSH
        "WAL",
        "KRAKE",
        "DELPHIN",
        # sound effects
        "VOGELSND",
        "STRANDSND",
    ],
)
# original game files refer to these as "Rauchfignr"
OreSize = enum.IntEnum("OreSize", ["ERZBERG_GROSS", "ERZBERG_KLEIN"])

# original game files refer to these as "Kind" (in FIGUREN.COD)
CharacterType = enum.IntEnum(
    "CharacterType",
    [
        "UNUSED",
        "FIGTYP_KANONIER",
        "FIGTYP_KANONTURM",
        "FIGTYP_KAVALERIE",
        "FIGTYP_MUSKETIER",
        "FIGTYP_PIRATSHIP",
        "FIGTYP_SCHWERT",
    ],
)

# military formations
Formation = enum.IntEnum(
    "Formation",
    ["FORM_HORI", "FORM_VERT", "FORM_QUAD", "FORM_DIA1", "FORM_DIA2", "FORM_PFEIL"],
)

# original game files refer to these as "Kind"
# "TIMENEVER" is used for the "AnimTime" property
AnimationType = enum.IntEnum(
    "AnimationType", ["TIMENEVER", "ENDLESS", "JUMPTO", "RANDOM"]
)

NOOBJEKT = "NOOBJEKT"
MAXPRODCNT = "MAXPRODCNT"
NUMMER = "Nummer"
# warehouse and marketplace radii
RADIUS_HQ = "RADIUS_HQ"
RADIUS_MARKT = "RADIUS_MARKT"

# Number of rotated perspectives available for an object. HAEUSER mostly have
# 1 or 4, FIGUREN mostly have 8.
PROPERTY_NUM_ROTATIONS = "Rotate"
