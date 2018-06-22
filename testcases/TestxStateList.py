import json
import unittest
import test_utils as tu


class TestxStateList(unittest.TestCase):

    def setUp(self):
        tu.log_out()
        return

    def tearDown(self):
        return

    def test_state_list_id(self):
        expected_state_list = {
            "echo_req": {
                "states_list": "id"
            },
            "msg_type": "states_list",
            "states_list": [
                {
                    "text": "Aceh",
                    "value": "AC"
                },
                {
                    "text": "Bali",
                    "value": "BA"
                },
                {
                    "text": "Bangka Belitung",
                    "value": "BB"
                },
                {
                    "text": "Banten",
                    "value": "BT"
                },
                {
                    "text": "Bengkulu",
                    "value": "BE"
                },
                {
                    "text": "Gorontalo",
                    "value": "GO"
                },
                {
                    "text": "Jakarta Raya",
                    "value": "JK"
                },
                {
                    "text": "Jambi",
                    "value": "JA"
                },
                {
                    "text": "Jawa Barat",
                    "value": "JB"
                },
                {
                    "text": "Jawa Tengah",
                    "value": "JT"
                },
                {
                    "text": "Jawa Timur",
                    "value": "JI"
                },
                {
                    "text": "Kalimantan Barat",
                    "value": "KB"
                },
                {
                    "text": "Kalimantan Selatan",
                    "value": "KS"
                },
                {
                    "text": "Kalimantan Tengah",
                    "value": "KT"
                },
                {
                    "text": "Kalimantan Timur",
                    "value": "KI"
                },
                {
                    "text": "Kepulauan Riau",
                    "value": "KR"
                },
                {
                    "text": "Lampung",
                    "value": "LA"
                },
                {
                    "text": "Maluku",
                    "value": "MA"
                },
                {
                    "text": "Maluku Utara",
                    "value": "MU"
                },
                {
                    "text": "Nusa Tenggara Barat",
                    "value": "NB"
                },
                {
                    "text": "Nusa Tenggara Timur",
                    "value": "NT"
                },
                {
                    "text": "Papua",
                    "value": "PA"
                },
                {
                    "text": "Papua Barat",
                    "value": "PB"
                },
                {
                    "text": "Riau",
                    "value": "RI"
                },
                {
                    "text": "Sulawesi Barat",
                    "value": "SR"
                },
                {
                    "text": "Sulawesi Selatan",
                    "value": "SN"
                },
                {
                    "text": "Sulawesi Tengah",
                    "value": "ST"
                },
                {
                    "text": "Sulawesi Tenggara",
                    "value": "SG"
                },
                {
                    "text": "Sulawesi Utara",
                    "value": "SA"
                },
                {
                    "text": "Sumatera Barat",
                    "value": "SB"
                },
                {
                    "text": "Sumatera Selatan",
                    "value": "SS"
                },
                {
                    "text": "Sumatera Utara",
                    "value": "SU"
                },
                {
                    "text": "Yogyakarta",
                    "value": "YO"
                }
            ]
        }

        # to convert python structure same as json output
        expected_state_list_id = tu.convert_py_json_output(expected_state_list)

        state_list = json.dumps({
            "states_list": "id"

        })

        state_list_id = tu.send_and_receive_ws_x_authorize(state_list)

        self.assertTrue(tu.compare_data(state_list_id, expected_state_list_id))
        self.assertTrue('error' not in state_list_id)

    def test_state_list_gb(self):
        expected_state_list = {
            "echo_req": {
                "states_list": "gb"
            },
            "msg_type": "states_list",
            "states_list": [
                {
                    "text": "Aberdeen City",
                    "value": "ABE"
                },
                {
                    "text": "Aberdeenshire",
                    "value": "ABD"
                },
                {
                    "text": "Angus",
                    "value": "ANS"
                },
                {
                    "text": "Antrim",
                    "value": "ANT"
                },
                {
                    "text": "Ards",
                    "value": "ARD"
                },
                {
                    "text": "Argyll and Bute",
                    "value": "AGB"
                },
                {
                    "text": "Armagh",
                    "value": "ARM"
                },
                {
                    "text": "Ballymena",
                    "value": "BLA"
                },
                {
                    "text": "Ballymoney",
                    "value": "BLY"
                },
                {
                    "text": "Banbridge",
                    "value": "BNB"
                },
                {
                    "text": "Barking and Dagenham",
                    "value": "BDG"
                },
                {
                    "text": "Barnet",
                    "value": "BNE"
                },
                {
                    "text": "Barnsley",
                    "value": "BNS"
                },
                {
                    "text": "Bath and North East Somerset",
                    "value": "BAS"
                },
                {
                    "text": "Bedfordshire",
                    "value": "BDF"
                },
                {
                    "text": "Belfast",
                    "value": "BFS"
                },
                {
                    "text": "Bexley",
                    "value": "BEX"
                },
                {
                    "text": "Birmingham",
                    "value": "BIR"
                },
                {
                    "text": "Blackburn with Darwen",
                    "value": "BBD"
                },
                {
                    "text": "Blackpool",
                    "value": "BPL"
                },
                {
                    "text": "Blaenau Gwent",
                    "value": "BGW"
                },
                {
                    "text": "Bolton",
                    "value": "BOL"
                },
                {
                    "text": "Bournemouth",
                    "value": "BMH"
                },
                {
                    "text": "Bracknell Forest",
                    "value": "BRC"
                },
                {
                    "text": "Bradford",
                    "value": "BRD"
                },
                {
                    "text": "Brent",
                    "value": "BEN"
                },
                {
                    "text": "Bridgend",
                    "value": "BGE"
                },
                {
                    "text": "Brighton and Hove",
                    "value": "BNH"
                },
                {
                    "text": "Bristol, City of",
                    "value": "BST"
                },
                {
                    "text": "Bromley",
                    "value": "BRY"
                },
                {
                    "text": "Buckinghamshire",
                    "value": "BKM"
                },
                {
                    "text": "Bury",
                    "value": "BUR"
                },
                {
                    "text": "Caerphilly",
                    "value": "CAY"
                },
                {
                    "text": "Calderdale",
                    "value": "CLD"
                },
                {
                    "text": "Cambridgeshire",
                    "value": "CAM"
                },
                {
                    "text": "Camden",
                    "value": "CMD"
                },
                {
                    "text": "Cardiff",
                    "value": "CRF"
                },
                {
                    "text": "Carmarthenshire",
                    "value": "CMN"
                },
                {
                    "text": "Carrickfergus",
                    "value": "CKF"
                },
                {
                    "text": "Castlereagh",
                    "value": "CSR"
                },
                {
                    "text": "Ceredigion",
                    "value": "CGN"
                },
                {
                    "text": "Cheshire",
                    "value": "CHS"
                },
                {
                    "text": "Clackmannanshire",
                    "value": "CLK"
                },
                {
                    "text": "Coleraine",
                    "value": "CLR"
                },
                {
                    "text": "Conwy",
                    "value": "CWY"
                },
                {
                    "text": "Cookstown",
                    "value": "CKT"
                },
                {
                    "text": "Cornwall",
                    "value": "CON"
                },
                {
                    "text": "Coventry",
                    "value": "COV"
                },
                {
                    "text": "Craigavon",
                    "value": "CGV"
                },
                {
                    "text": "Croydon",
                    "value": "CRY"
                },
                {
                    "text": "Cumbria",
                    "value": "CMA"
                },
                {
                    "text": "Darlington",
                    "value": "DAL"
                },
                {
                    "text": "Denbighshire",
                    "value": "DEN"
                },
                {
                    "text": "Derby",
                    "value": "DER"
                },
                {
                    "text": "Derbyshire",
                    "value": "DBY"
                },
                {
                    "text": "Derry",
                    "value": "DRY"
                },
                {
                    "text": "Devon",
                    "value": "DEV"
                },
                {
                    "text": "Doncaster",
                    "value": "DNC"
                },
                {
                    "text": "Dorset",
                    "value": "DOR"
                },
                {
                    "text": "Down",
                    "value": "DOW"
                },
                {
                    "text": "Dudley",
                    "value": "DUD"
                },
                {
                    "text": "Dumfries and Galloway",
                    "value": "DGY"
                },
                {
                    "text": "Dundee City",
                    "value": "DND"
                },
                {
                    "text": "Dungannon",
                    "value": "DGN"
                },
                {
                    "text": "Durham",
                    "value": "DUR"
                },
                {
                    "text": "Ealing",
                    "value": "EAL"
                },
                {
                    "text": "East Ayrshire",
                    "value": "EAY"
                },
                {
                    "text": "East Dunbartonshire",
                    "value": "EDU"
                },
                {
                    "text": "East Lothian",
                    "value": "ELN"
                },
                {
                    "text": "East Renfrewshire",
                    "value": "ERW"
                },
                {
                    "text": "East Riding of Yorkshire",
                    "value": "ERY"
                },
                {
                    "text": "East Sussex",
                    "value": "ESX"
                },
                {
                    "text": "Edinburgh, City of",
                    "value": "EDH"
                },
                {
                    "text": "Eilean Siar",
                    "value": "ELS"
                },
                {
                    "text": "Enfield",
                    "value": "ENF"
                },
                {
                    "text": "Essex",
                    "value": "ESS"
                },
                {
                    "text": "Falkirk",
                    "value": "FAL"
                },
                {
                    "text": "Fermanagh",
                    "value": "FER"
                },
                {
                    "text": "Fife",
                    "value": "FIF"
                },
                {
                    "text": "Flintshire",
                    "value": "FLN"
                },
                {
                    "text": "Gateshead",
                    "value": "GAT"
                },
                {
                    "text": "Glasgow City",
                    "value": "GLG"
                },
                {
                    "text": "Gloucestershire",
                    "value": "GLS"
                },
                {
                    "text": "Greenwich",
                    "value": "GRE"
                },
                {
                    "text": "Guernsey",
                    "value": "GSY"
                },
                {
                    "text": "Gwynedd",
                    "value": "GWN"
                },
                {
                    "text": "Hackney",
                    "value": "HCK"
                },
                {
                    "text": "Halton",
                    "value": "HAL"
                },
                {
                    "text": "Hammersmith and Fulham",
                    "value": "HMF"
                },
                {
                    "text": "Hampshire",
                    "value": "HAM"
                },
                {
                    "text": "Haringey",
                    "value": "HRY"
                },
                {
                    "text": "Harrow",
                    "value": "HRW"
                },
                {
                    "text": "Hartlepool",
                    "value": "HPL"
                },
                {
                    "text": "Havering",
                    "value": "HAV"
                },
                {
                    "text": "Herefordshire, County of",
                    "value": "HEF"
                },
                {
                    "text": "Hertfordshire",
                    "value": "HRT"
                },
                {
                    "text": "Highland",
                    "value": "HLD"
                },
                {
                    "text": "Hillingdon",
                    "value": "HIL"
                },
                {
                    "text": "Hounslow",
                    "value": "HNS"
                },
                {
                    "text": "Inverclyde",
                    "value": "IVC"
                },
                {
                    "text": "Isle of Anglesey",
                    "value": "AGY"
                },
                {
                    "text": "Isle of Wight",
                    "value": "IOW"
                },
                {
                    "text": "Isles of Scilly",
                    "value": "IOS"
                },
                {
                    "text": "Islington",
                    "value": "ISL"
                },
                {
                    "text": "Jersey",
                    "value": "JSY"
                },
                {
                    "text": "Kensington and Chelsea",
                    "value": "KEC"
                },
                {
                    "text": "Kent",
                    "value": "KEN"
                },
                {
                    "text": "Kingston upon Hull, City of",
                    "value": "KHL"
                },
                {
                    "text": "Kingston upon Thames",
                    "value": "KTT"
                },
                {
                    "text": "Kirklees",
                    "value": "KIR"
                },
                {
                    "text": "Knowsley",
                    "value": "KWL"
                },
                {
                    "text": "Lambeth",
                    "value": "LBH"
                },
                {
                    "text": "Lancashire",
                    "value": "LAN"
                },
                {
                    "text": "Larne",
                    "value": "LRN"
                },
                {
                    "text": "Leeds",
                    "value": "LDS"
                },
                {
                    "text": "Leicester",
                    "value": "LCE"
                },
                {
                    "text": "Leicestershire",
                    "value": "LEC"
                },
                {
                    "text": "Lewisham",
                    "value": "LEW"
                },
                {
                    "text": "Limavady",
                    "value": "LMV"
                },
                {
                    "text": "Lincolnshire",
                    "value": "LIN"
                },
                {
                    "text": "Lisburn",
                    "value": "LSB"
                },
                {
                    "text": "Liverpool",
                    "value": "LIV"
                },
                {
                    "text": "London, City of",
                    "value": "LND"
                },
                {
                    "text": "Luton",
                    "value": "LUT"
                },
                {
                    "text": "Magherafelt",
                    "value": "MFT"
                },
                {
                    "text": "Manchester",
                    "value": "MAN"
                },
                {
                    "text": "Medway",
                    "value": "MDW"
                },
                {
                    "text": "Merthyr Tydfil",
                    "value": "MTY"
                },
                {
                    "text": "Merton",
                    "value": "MRT"
                },
                {
                    "text": "Middlesbrough",
                    "value": "MDB"
                },
                {
                    "text": "Midlothian",
                    "value": "MLN"
                },
                {
                    "text": "Milton Keynes",
                    "value": "MIK"
                },
                {
                    "text": "Monmouthshire [Sir Fynwy GB-FYN]",
                    "value": "MON"
                },
                {
                    "text": "Moray",
                    "value": "MRY"
                },
                {
                    "text": "Moyle",
                    "value": "MYL"
                },
                {
                    "text": "Neath Port Talbot",
                    "value": "NTL"
                },
                {
                    "text": "Newcastle upon Tyne",
                    "value": "NET"
                },
                {
                    "text": "Newham",
                    "value": "NWM"
                },
                {
                    "text": "Newport",
                    "value": "NWP"
                },
                {
                    "text": "Newry and Mourne",
                    "value": "NYM"
                },
                {
                    "text": "Newtownabbey",
                    "value": "NTA"
                },
                {
                    "text": "Norfolk",
                    "value": "NFK"
                },
                {
                    "text": "North Ayrshire",
                    "value": "NAY"
                },
                {
                    "text": "North Down",
                    "value": "NDN"
                },
                {
                    "text": "North East Lincolnshire",
                    "value": "NEL"
                },
                {
                    "text": "North Lanarkshire",
                    "value": "NLK"
                },
                {
                    "text": "North Lincolnshire",
                    "value": "NLN"
                },
                {
                    "text": "North Somerset",
                    "value": "NSM"
                },
                {
                    "text": "North Tyneside",
                    "value": "NTY"
                },
                {
                    "text": "North Yorkshire",
                    "value": "NYK"
                },
                {
                    "text": "Northamptonshire",
                    "value": "NTH"
                },
                {
                    "text": "Northumberland",
                    "value": "NBL"
                },
                {
                    "text": "Nottingham",
                    "value": "NGM"
                },
                {
                    "text": "Nottinghamshire",
                    "value": "NTT"
                },
                {
                    "text": "Oldham",
                    "value": "OLD"
                },
                {
                    "text": "Omagh",
                    "value": "OMH"
                },
                {
                    "text": "Orkney Islands",
                    "value": "ORK"
                },
                {
                    "text": "Oxfordshire",
                    "value": "OXF"
                },
                {
                    "text": "Pembrokeshire",
                    "value": "PEM"
                },
                {
                    "text": "Perth and Kinross",
                    "value": "PKN"
                },
                {
                    "text": "Peterborough",
                    "value": "PTE"
                },
                {
                    "text": "Plymouth",
                    "value": "PLY"
                },
                {
                    "text": "Poole",
                    "value": "POL"
                },
                {
                    "text": "Portsmouth",
                    "value": "POR"
                },
                {
                    "text": "Powys",
                    "value": "POW"
                },
                {
                    "text": "Reading",
                    "value": "RDG"
                },
                {
                    "text": "Redbridge",
                    "value": "RDB"
                },
                {
                    "text": "Redcar and Cleveland",
                    "value": "RCC"
                },
                {
                    "text": "Renfrewshire",
                    "value": "RFW"
                },
                {
                    "text": "Rhondda, Cynon, Taff",
                    "value": "RCT"
                },
                {
                    "text": "Richmond upon Thames",
                    "value": "RIC"
                },
                {
                    "text": "Rochdale",
                    "value": "RCH"
                },
                {
                    "text": "Rotherham",
                    "value": "ROT"
                },
                {
                    "text": "Rutland",
                    "value": "RUT"
                },
                {
                    "text": "Saint Helens",
                    "value": "SHN"
                },
                {
                    "text": "Salford",
                    "value": "SLF"
                },
                {
                    "text": "Sandwell",
                    "value": "SAW"
                },
                {
                    "text": "Scottish Borders, The",
                    "value": "SCB"
                },
                {
                    "text": "Sefton",
                    "value": "SFT"
                },
                {
                    "text": "Sheffield",
                    "value": "SHF"
                },
                {
                    "text": "Shetland Islands",
                    "value": "ZET"
                },
                {
                    "text": "Shropshire",
                    "value": "SHR"
                },
                {
                    "text": "Slough",
                    "value": "SLG"
                },
                {
                    "text": "Solihull",
                    "value": "SOL"
                },
                {
                    "text": "Somerset",
                    "value": "SOM"
                },
                {
                    "text": "South Ayrshire",
                    "value": "SAY"
                },
                {
                    "text": "South Gloucestershire",
                    "value": "SGC"
                },
                {
                    "text": "South Lanarkshire",
                    "value": "SLK"
                },
                {
                    "text": "South Tyneside",
                    "value": "STY"
                },
                {
                    "text": "Southampton",
                    "value": "STH"
                },
                {
                    "text": "Southend-on-Sea",
                    "value": "SOS"
                },
                {
                    "text": "Southwark",
                    "value": "SWK"
                },
                {
                    "text": "Staffordshire",
                    "value": "STS"
                },
                {
                    "text": "Stirling",
                    "value": "STG"
                },
                {
                    "text": "Stockport",
                    "value": "SKP"
                },
                {
                    "text": "Stockton-on-Tees",
                    "value": "STT"
                },
                {
                    "text": "Stoke-on-Trent",
                    "value": "STE"
                },
                {
                    "text": "Strabane",
                    "value": "STB"
                },
                {
                    "text": "Suffolk",
                    "value": "SFK"
                },
                {
                    "text": "Sunderland",
                    "value": "SND"
                },
                {
                    "text": "Surrey",
                    "value": "SRY"
                },
                {
                    "text": "Sutton",
                    "value": "STN"
                },
                {
                    "text": "Swansea",
                    "value": "SWA"
                },
                {
                    "text": "Swindon",
                    "value": "SWD"
                },
                {
                    "text": "Tameside",
                    "value": "TAM"
                },
                {
                    "text": "Telford and Wrekin",
                    "value": "TFW"
                },
                {
                    "text": "Thurrock",
                    "value": "THR"
                },
                {
                    "text": "Torbay",
                    "value": "TOB"
                },
                {
                    "text": "Torfaen",
                    "value": "TOF"
                },
                {
                    "text": "Tower Hamlets",
                    "value": "TWH"
                },
                {
                    "text": "Trafford",
                    "value": "TRF"
                },
                {
                    "text": "Vale of Glamorgan",
                    "value": "VGL"
                },
                {
                    "text": "Wakefield",
                    "value": "WKF"
                },
                {
                    "text": "Walsall",
                    "value": "WLL"
                },
                {
                    "text": "Waltham Forest",
                    "value": "WFT"
                },
                {
                    "text": "Wandsworth",
                    "value": "WND"
                },
                {
                    "text": "Warrington",
                    "value": "WRT"
                },
                {
                    "text": "Warwickshire",
                    "value": "WAR"
                },
                {
                    "text": "West Berkshire",
                    "value": "WBK"
                },
                {
                    "text": "West Dunbartonshire",
                    "value": "WDU"
                },
                {
                    "text": "West Lothian",
                    "value": "WLN"
                },
                {
                    "text": "West Sussex",
                    "value": "WSX"
                },
                {
                    "text": "Westminster",
                    "value": "WSM"
                },
                {
                    "text": "Wigan",
                    "value": "WGN"
                },
                {
                    "text": "Wiltshire",
                    "value": "WIL"
                },
                {
                    "text": "Windsor and Maidenhead",
                    "value": "WNM"
                },
                {
                    "text": "Wirral",
                    "value": "WRL"
                },
                {
                    "text": "Wokingham",
                    "value": "WOK"
                },
                {
                    "text": "Wolverhampton",
                    "value": "WLV"
                },
                {
                    "text": "Worcestershire",
                    "value": "WOR"
                },
                {
                    "text": "Wrexham",
                    "value": "WRX"
                },
                {
                    "text": "York",
                    "value": "YOR"
                }
            ]
        }

        # to convert python structure same as json output
        expected_state_list_gb = tu.convert_py_json_output(expected_state_list)

        state_list = json.dumps({
            "states_list": "gb"

        })

        state_list_id = tu.send_and_receive_ws_x_authorize(state_list)

        self.assertTrue(tu.compare_data(state_list_id, expected_state_list_gb))
        self.assertTrue('error' not in state_list_id)
