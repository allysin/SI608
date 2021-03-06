import networkx as nx
import matplotlib.pyplot as plt
goarn_network= nx.Graph()

goarn_network.add_edge("Epicentre France", "National Institute of Virology (NIV-South Africa)",weight=2)
goarn_network.add_edge("National Institute of Virology (NIV-South Africa)", "WHO HQ",weight=2)
goarn_network.add_edge("National Institute of Virology (NIV-South Africa)", "WHO Collaborating Centre",weight=2)
goarn_network.add_edge("Epicentre France", "WHO HQ",weight=2)
goarn_network.add_edge("Epicentre France", "WHO Collaborating Centre",weight=2)
goarn_network.add_edge("WHO Collaborating Centre", "WHO HQ",weight=2)
goarn_network.add_edge("CDC Atlanta", "WHO HQ",weight=2)
goarn_network.add_edge("FAO", "WHO HQ",weight=1)
goarn_network.add_edge("NAMRU-3 Egypt", "WHO HQ",weight=1)
goarn_network.add_edge("National Health Laboratory Service (NHLS)", "WHO HQ",weight=1)
goarn_network.add_edge("CDC Atlanta", "FAO",weight=2)
goarn_network.add_edge("CDC Atlanta", "NAMRU-3 Egypt",weight=2)
goarn_network.add_edge("CDC Atlanta", "National Health Laboratory Service (NHLS)",weight=2)
goarn_network.add_edge("FAO", "NAMRU-3 Egypt",weight=2)
goarn_network.add_edge("FAO", "National Health Laboratory Service (NHLS)",weight=2)
goarn_network.add_edge("NAMRU-3 Egypt", "National Health Laboratory Service (NHLS)",weight=2)
goarn_network.add_edge("CDC Atlanta", "National Institute of Virology (NIV-South Africa)",weight=2)
goarn_network.add_edge("CDC Atlanta", "Ministry of Health Saudi Arabia",weight=1)
goarn_network.add_edge("FAO", "National Institute of Virology (NIV-South Africa)",weight=1)
goarn_network.add_edge("FAO", "Ministry of Health Saudi Arabia",weight=1)
goarn_network.add_edge("NAMRU-3 Egypt", "National Institute of Virology (NIV-South Africa)",weight=1)
goarn_network.add_edge("Ministry of Health Saudi Arabia", "NAMRU-3 Egypt",weight=1)
goarn_network.add_edge("National Health Laboratory Service (NHLS)", "National Institute of Virology (NIV-South Africa)",weight=1)
goarn_network.add_edge("Ministry of Health Saudi Arabia", "National Health Laboratory Service (NHLS)",weight=1)
goarn_network.add_edge("Ministry of Health Saudi Arabia", "National Institute of Virology (NIV-South Africa)",weight=1)
goarn_network.add_edge("WHO HQ", "WHO Uganda",weight=1)
goarn_network.add_edge("Ministry of Health of Uganda", "WHO HQ",weight=1)
goarn_network.add_edge("National Task Force Uganda", "WHO HQ",weight=1)
goarn_network.add_edge("MSF International", "WHO HQ",weight=1)
goarn_network.add_edge("ISS Italy", "WHO HQ",weight=1)
goarn_network.add_edge("Sendai Quarantine Station", "WHO HQ",weight=1)
goarn_network.add_edge("National Institute for Infectious Diseases Japan", "WHO HQ",weight=1)
goarn_network.add_edge("WHO HQ", "WHO_AFRO",weight=1)
goarn_network.add_edge("Action Contre la Faim", "WHO HQ",weight=1)
goarn_network.add_edge("African Medical and Research Foundation", "WHO HQ",weight=1)
goarn_network.add_edge("ACORD-UK", "WHO HQ",weight=1)
goarn_network.add_edge("Catholic Relief Services", "WHO HQ",weight=1)
goarn_network.add_edge("Lacor Hospital", "WHO HQ",weight=1)
goarn_network.add_edge("Red Crescent societies", "WHO HQ",weight=1)
goarn_network.add_edge("ICRC", "WHO HQ",weight=1)
goarn_network.add_edge("Save the Children-Denmark", "WHO HQ",weight=1)
goarn_network.add_edge("WHO HQ", "World Food Programme",weight=1)
goarn_network.add_edge("WHO HQ", "World Vision",weight=1)
goarn_network.add_edge("UNICEF", "WHO HQ",weight=1)
goarn_network.add_edge("United Kingdom Department for International Development (DFID)", "WHO HQ",weight=1)
goarn_network.add_edge("USAID", "WHO HQ",weight=1)
goarn_network.add_edge("National Institute of Virology (NIV-South Africa)", "WHO Uganda",weight=1)
goarn_network.add_edge("Ministry of Health of Uganda", "National Institute of Virology (NIV-South Africa)",weight=1)
goarn_network.add_edge("National Institute of Virology (NIV-South Africa)", "National Task Force Uganda",weight=1)
goarn_network.add_edge("MSF International", "National Institute of Virology (NIV-South Africa)",weight=1)
goarn_network.add_edge("ISS Italy", "National Institute of Virology (NIV-South Africa)",weight=1)
goarn_network.add_edge("National Institute of Virology (NIV-South Africa)", "Sendai Quarantine Station",weight=1)
goarn_network.add_edge("National Institute for Infectious Diseases Japan", "National Institute of Virology (NIV-South Africa)",weight=1)
goarn_network.add_edge("National Institute of Virology (NIV-South Africa)", "WHO_AFRO",weight=1)
goarn_network.add_edge("Action Contre la Faim", "National Institute of Virology (NIV-South Africa)",weight=1)
goarn_network.add_edge("African Medical and Research Foundation", "National Institute of Virology (NIV-South Africa)",weight=1)
goarn_network.add_edge("ACORD-UK", "National Institute of Virology (NIV-South Africa)",weight=1)
goarn_network.add_edge("Catholic Relief Services", "National Institute of Virology (NIV-South Africa)",weight=1)
goarn_network.add_edge("Lacor Hospital", "National Institute of Virology (NIV-South Africa)",weight=1)
goarn_network.add_edge("National Institute of Virology (NIV-South Africa)", "Red Crescent societies",weight=1)
goarn_network.add_edge("ICRC", "National Institute of Virology (NIV-South Africa)",weight=1)
goarn_network.add_edge("National Institute of Virology (NIV-South Africa)", "Save the Children-Denmark",weight=1)
goarn_network.add_edge("National Institute of Virology (NIV-South Africa)", "World Food Programme",weight=1)
goarn_network.add_edge("National Institute of Virology (NIV-South Africa)", "World Vision",weight=1)
goarn_network.add_edge("National Institute of Virology (NIV-South Africa)", "UNICEF",weight=1)
goarn_network.add_edge("National Institute of Virology (NIV-South Africa)", "United Kingdom Department for International Development (DFID)",weight=1)
goarn_network.add_edge("National Institute of Virology (NIV-South Africa)", "USAID",weight=1)
goarn_network.add_edge("Ministry of Health of Uganda", "WHO Uganda",weight=1)
goarn_network.add_edge("National Task Force Uganda", "WHO Uganda",weight=1)
goarn_network.add_edge("MSF International", "WHO Uganda",weight=1)
goarn_network.add_edge("Epicentre France", "WHO Uganda",weight=1)
goarn_network.add_edge("WHO Collaborating Centre", "WHO Uganda",weight=1)
goarn_network.add_edge("CDC Atlanta", "WHO Uganda",weight=1)
goarn_network.add_edge("ISS Italy", "WHO Uganda",weight=1)
goarn_network.add_edge("Sendai Quarantine Station", "WHO Uganda",weight=1)
goarn_network.add_edge("National Institute for Infectious Diseases Japan", "WHO Uganda",weight=1)
goarn_network.add_edge("WHO Uganda", "WHO_AFRO",weight=1)
goarn_network.add_edge("Action Contre la Faim", "WHO Uganda",weight=1)
goarn_network.add_edge("African Medical and Research Foundation", "WHO Uganda",weight=1)
goarn_network.add_edge("ACORD-UK", "WHO Uganda",weight=1)
goarn_network.add_edge("Catholic Relief Services", "WHO Uganda",weight=1)
goarn_network.add_edge("Lacor Hospital", "WHO Uganda",weight=1)
goarn_network.add_edge("Red Crescent societies", "WHO Uganda",weight=1)
goarn_network.add_edge("ICRC", "WHO Uganda",weight=1)
goarn_network.add_edge("Save the Children-Denmark", "WHO Uganda",weight=1)
goarn_network.add_edge("WHO Uganda", "World Food Programme",weight=1)
goarn_network.add_edge("WHO Uganda", "World Vision",weight=1)
goarn_network.add_edge("UNICEF", "WHO Uganda",weight=1)
goarn_network.add_edge("United Kingdom Department for International Development (DFID)", "WHO Uganda",weight=1)
goarn_network.add_edge("USAID", "WHO Uganda",weight=1)
goarn_network.add_edge("Ministry of Health of Uganda", "National Task Force Uganda",weight=1)
goarn_network.add_edge("MSF International", "Ministry of Health of Uganda",weight=1)
goarn_network.add_edge("Epicentre France", "Ministry of Health of Uganda",weight=1)
goarn_network.add_edge("Ministry of Health of Uganda", "WHO Collaborating Centre",weight=1)
goarn_network.add_edge("CDC Atlanta", "Ministry of Health of Uganda",weight=1)
goarn_network.add_edge("ISS Italy", "Ministry of Health of Uganda",weight=1)
goarn_network.add_edge("Ministry of Health of Uganda", "Sendai Quarantine Station",weight=1)
goarn_network.add_edge("Ministry of Health of Uganda", "National Institute for Infectious Diseases Japan",weight=1)
goarn_network.add_edge("Ministry of Health of Uganda", "WHO_AFRO",weight=1)
goarn_network.add_edge("Action Contre la Faim", "Ministry of Health of Uganda",weight=1)
goarn_network.add_edge("African Medical and Research Foundation", "Ministry of Health of Uganda",weight=1)
goarn_network.add_edge("ACORD-UK", "Ministry of Health of Uganda",weight=1)
goarn_network.add_edge("Catholic Relief Services", "Ministry of Health of Uganda",weight=1)
goarn_network.add_edge("Lacor Hospital", "Ministry of Health of Uganda",weight=1)
goarn_network.add_edge("Ministry of Health of Uganda", "Red Crescent societies",weight=1)
goarn_network.add_edge("ICRC", "Ministry of Health of Uganda",weight=1)
goarn_network.add_edge("Ministry of Health of Uganda", "Save the Children-Denmark",weight=1)
goarn_network.add_edge("Ministry of Health of Uganda", "World Food Programme",weight=1)
goarn_network.add_edge("Ministry of Health of Uganda", "World Vision",weight=1)
goarn_network.add_edge("Ministry of Health of Uganda", "UNICEF",weight=1)
goarn_network.add_edge("Ministry of Health of Uganda", "United Kingdom Department for International Development (DFID)",weight=1)
goarn_network.add_edge("Ministry of Health of Uganda", "USAID",weight=1)
goarn_network.add_edge("MSF International", "National Task Force Uganda",weight=1)
goarn_network.add_edge("Epicentre France", "National Task Force Uganda",weight=1)
goarn_network.add_edge("National Task Force Uganda", "WHO Collaborating Centre",weight=1)
goarn_network.add_edge("CDC Atlanta", "National Task Force Uganda",weight=1)
goarn_network.add_edge("ISS Italy", "National Task Force Uganda",weight=1)
goarn_network.add_edge("National Task Force Uganda", "Sendai Quarantine Station",weight=1)
goarn_network.add_edge("National Institute for Infectious Diseases Japan", "National Task Force Uganda",weight=1)
goarn_network.add_edge("National Task Force Uganda", "WHO_AFRO",weight=1)
goarn_network.add_edge("Action Contre la Faim", "National Task Force Uganda",weight=1)
goarn_network.add_edge("African Medical and Research Foundation", "National Task Force Uganda",weight=1)
goarn_network.add_edge("ACORD-UK", "National Task Force Uganda",weight=1)
goarn_network.add_edge("Catholic Relief Services", "National Task Force Uganda",weight=1)
goarn_network.add_edge("Lacor Hospital", "National Task Force Uganda",weight=1)
goarn_network.add_edge("National Task Force Uganda", "Red Crescent societies",weight=1)
goarn_network.add_edge("ICRC", "National Task Force Uganda",weight=1)
goarn_network.add_edge("National Task Force Uganda", "Save the Children-Denmark",weight=1)
goarn_network.add_edge("National Task Force Uganda", "World Food Programme",weight=1)
goarn_network.add_edge("National Task Force Uganda", "World Vision",weight=1)
goarn_network.add_edge("National Task Force Uganda", "UNICEF",weight=1)
goarn_network.add_edge("National Task Force Uganda", "United Kingdom Department for International Development (DFID)",weight=1)
goarn_network.add_edge("National Task Force Uganda", "USAID",weight=1)
goarn_network.add_edge("Epicentre France", "MSF International",weight=1)
goarn_network.add_edge("MSF International", "WHO Collaborating Centre",weight=1)
goarn_network.add_edge("CDC Atlanta", "MSF International",weight=1)
goarn_network.add_edge("ISS Italy", "MSF International",weight=1)
goarn_network.add_edge("MSF International", "Sendai Quarantine Station",weight=1)
goarn_network.add_edge("MSF International", "National Institute for Infectious Diseases Japan",weight=1)
goarn_network.add_edge("MSF International", "WHO_AFRO",weight=1)
goarn_network.add_edge("Action Contre la Faim", "MSF International",weight=1)
goarn_network.add_edge("African Medical and Research Foundation", "MSF International",weight=1)
goarn_network.add_edge("ACORD-UK", "MSF International",weight=1)
goarn_network.add_edge("Catholic Relief Services", "MSF International",weight=1)
goarn_network.add_edge("Lacor Hospital", "MSF International",weight=1)
goarn_network.add_edge("MSF International", "Red Crescent societies",weight=1)
goarn_network.add_edge("ICRC", "MSF International",weight=1)
goarn_network.add_edge("MSF International", "Save the Children-Denmark",weight=1)
goarn_network.add_edge("MSF International", "World Food Programme",weight=1)
goarn_network.add_edge("MSF International", "World Vision",weight=1)
goarn_network.add_edge("MSF International", "UNICEF",weight=1)
goarn_network.add_edge("MSF International", "United Kingdom Department for International Development (DFID)",weight=1)
goarn_network.add_edge("MSF International", "USAID",weight=1)
goarn_network.add_edge("CDC Atlanta", "Epicentre France",weight=1)
goarn_network.add_edge("Epicentre France", "ISS Italy",weight=1)
goarn_network.add_edge("Epicentre France", "Sendai Quarantine Station",weight=1)
goarn_network.add_edge("Epicentre France", "National Institute for Infectious Diseases Japan",weight=1)
goarn_network.add_edge("Epicentre France", "WHO_AFRO",weight=1)
goarn_network.add_edge("Action Contre la Faim", "Epicentre France",weight=1)
goarn_network.add_edge("African Medical and Research Foundation", "Epicentre France",weight=1)
goarn_network.add_edge("ACORD-UK", "Epicentre France",weight=1)
goarn_network.add_edge("Catholic Relief Services", "Epicentre France",weight=1)
goarn_network.add_edge("Epicentre France", "Lacor Hospital",weight=1)
goarn_network.add_edge("Epicentre France", "Red Crescent societies",weight=1)
goarn_network.add_edge("Epicentre France", "ICRC",weight=1)
goarn_network.add_edge("Epicentre France", "Save the Children-Denmark",weight=1)
goarn_network.add_edge("Epicentre France", "World Food Programme",weight=1)
goarn_network.add_edge("Epicentre France", "World Vision",weight=1)
goarn_network.add_edge("Epicentre France", "UNICEF",weight=1)
goarn_network.add_edge("Epicentre France", "United Kingdom Department for International Development (DFID)",weight=1)
goarn_network.add_edge("Epicentre France", "USAID",weight=1)
goarn_network.add_edge("CDC Atlanta", "WHO Collaborating Centre",weight=1)
goarn_network.add_edge("ISS Italy", "WHO Collaborating Centre",weight=1)
goarn_network.add_edge("Sendai Quarantine Station", "WHO Collaborating Centre",weight=1)
goarn_network.add_edge("National Institute for Infectious Diseases Japan", "WHO Collaborating Centre",weight=1)
goarn_network.add_edge("WHO Collaborating Centre", "WHO_AFRO",weight=1)
goarn_network.add_edge("Action Contre la Faim", "WHO Collaborating Centre",weight=1)
goarn_network.add_edge("African Medical and Research Foundation", "WHO Collaborating Centre",weight=1)
goarn_network.add_edge("ACORD-UK", "WHO Collaborating Centre",weight=1)
goarn_network.add_edge("Catholic Relief Services", "WHO Collaborating Centre",weight=1)
goarn_network.add_edge("Lacor Hospital", "WHO Collaborating Centre",weight=1)
goarn_network.add_edge("Red Crescent societies", "WHO Collaborating Centre",weight=1)
goarn_network.add_edge("ICRC", "WHO Collaborating Centre",weight=1)
goarn_network.add_edge("Save the Children-Denmark", "WHO Collaborating Centre",weight=1)
goarn_network.add_edge("WHO Collaborating Centre", "World Food Programme",weight=1)
goarn_network.add_edge("WHO Collaborating Centre", "World Vision",weight=1)
goarn_network.add_edge("UNICEF", "WHO Collaborating Centre",weight=1)
goarn_network.add_edge("United Kingdom Department for International Development (DFID)", "WHO Collaborating Centre",weight=1)
goarn_network.add_edge("USAID", "WHO Collaborating Centre",weight=1)
goarn_network.add_edge("CDC Atlanta", "ISS Italy",weight=1)
goarn_network.add_edge("CDC Atlanta", "Sendai Quarantine Station",weight=1)
goarn_network.add_edge("CDC Atlanta", "National Institute for Infectious Diseases Japan",weight=1)
goarn_network.add_edge("CDC Atlanta", "WHO_AFRO",weight=1)
goarn_network.add_edge("Action Contre la Faim", "CDC Atlanta",weight=1)
goarn_network.add_edge("African Medical and Research Foundation", "CDC Atlanta",weight=1)
goarn_network.add_edge("ACORD-UK", "CDC Atlanta",weight=1)
goarn_network.add_edge("CDC Atlanta", "Catholic Relief Services",weight=1)
goarn_network.add_edge("CDC Atlanta", "Lacor Hospital",weight=1)
goarn_network.add_edge("CDC Atlanta", "Red Crescent societies",weight=1)
goarn_network.add_edge("CDC Atlanta", "ICRC",weight=1)
goarn_network.add_edge("CDC Atlanta", "Save the Children-Denmark",weight=1)
goarn_network.add_edge("CDC Atlanta", "World Food Programme",weight=1)
goarn_network.add_edge("CDC Atlanta", "World Vision",weight=1)
goarn_network.add_edge("CDC Atlanta", "UNICEF",weight=1)
goarn_network.add_edge("CDC Atlanta", "United Kingdom Department for International Development (DFID)",weight=1)
goarn_network.add_edge("CDC Atlanta", "USAID",weight=1)
goarn_network.add_edge("ISS Italy", "Sendai Quarantine Station",weight=1)
goarn_network.add_edge("ISS Italy", "National Institute for Infectious Diseases Japan",weight=1)
goarn_network.add_edge("ISS Italy", "WHO_AFRO",weight=1)
goarn_network.add_edge("Action Contre la Faim", "ISS Italy",weight=1)
goarn_network.add_edge("African Medical and Research Foundation", "ISS Italy",weight=1)
goarn_network.add_edge("ACORD-UK", "ISS Italy",weight=1)
goarn_network.add_edge("Catholic Relief Services", "ISS Italy",weight=1)
goarn_network.add_edge("ISS Italy", "Lacor Hospital",weight=1)
goarn_network.add_edge("ISS Italy", "Red Crescent societies",weight=1)
goarn_network.add_edge("ICRC", "ISS Italy",weight=1)
goarn_network.add_edge("ISS Italy", "Save the Children-Denmark",weight=1)
goarn_network.add_edge("ISS Italy", "World Food Programme",weight=1)
goarn_network.add_edge("ISS Italy", "World Vision",weight=1)
goarn_network.add_edge("ISS Italy", "UNICEF",weight=1)
goarn_network.add_edge("ISS Italy", "United Kingdom Department for International Development (DFID)",weight=1)
goarn_network.add_edge("ISS Italy", "USAID",weight=1)
goarn_network.add_edge("National Institute for Infectious Diseases Japan", "Sendai Quarantine Station",weight=1)
goarn_network.add_edge("Sendai Quarantine Station", "WHO_AFRO",weight=1)
goarn_network.add_edge("Action Contre la Faim", "Sendai Quarantine Station",weight=1)
goarn_network.add_edge("African Medical and Research Foundation", "Sendai Quarantine Station",weight=1)
goarn_network.add_edge("ACORD-UK", "Sendai Quarantine Station",weight=1)
goarn_network.add_edge("Catholic Relief Services", "Sendai Quarantine Station",weight=1)
goarn_network.add_edge("Lacor Hospital", "Sendai Quarantine Station",weight=1)
goarn_network.add_edge("Red Crescent societies", "Sendai Quarantine Station",weight=1)
goarn_network.add_edge("ICRC", "Sendai Quarantine Station",weight=1)
goarn_network.add_edge("Save the Children-Denmark", "Sendai Quarantine Station",weight=1)
goarn_network.add_edge("Sendai Quarantine Station", "World Food Programme",weight=1)
goarn_network.add_edge("Sendai Quarantine Station", "World Vision",weight=1)
goarn_network.add_edge("Sendai Quarantine Station", "UNICEF",weight=1)
goarn_network.add_edge("Sendai Quarantine Station", "United Kingdom Department for International Development (DFID)",weight=1)
goarn_network.add_edge("Sendai Quarantine Station", "USAID",weight=1)
goarn_network.add_edge("National Institute for Infectious Diseases Japan", "WHO_AFRO",weight=1)
goarn_network.add_edge("Action Contre la Faim", "National Institute for Infectious Diseases Japan",weight=1)
goarn_network.add_edge("African Medical and Research Foundation", "National Institute for Infectious Diseases Japan",weight=1)
goarn_network.add_edge("ACORD-UK", "National Institute for Infectious Diseases Japan",weight=1)
goarn_network.add_edge("Catholic Relief Services", "National Institute for Infectious Diseases Japan",weight=1)
goarn_network.add_edge("Lacor Hospital", "National Institute for Infectious Diseases Japan",weight=1)
goarn_network.add_edge("National Institute for Infectious Diseases Japan", "Red Crescent societies",weight=1)
goarn_network.add_edge("ICRC", "National Institute for Infectious Diseases Japan",weight=1)
goarn_network.add_edge("National Institute for Infectious Diseases Japan", "Save the Children-Denmark",weight=1)
goarn_network.add_edge("National Institute for Infectious Diseases Japan", "World Food Programme",weight=1)
goarn_network.add_edge("National Institute for Infectious Diseases Japan", "World Vision",weight=1)
goarn_network.add_edge("National Institute for Infectious Diseases Japan", "UNICEF",weight=1)
goarn_network.add_edge("National Institute for Infectious Diseases Japan", "United Kingdom Department for International Development (DFID)",weight=1)
goarn_network.add_edge("National Institute for Infectious Diseases Japan", "USAID",weight=1)
goarn_network.add_edge("Action Contre la Faim", "WHO_AFRO",weight=1)
goarn_network.add_edge("African Medical and Research Foundation", "WHO_AFRO",weight=1)
goarn_network.add_edge("ACORD-UK", "WHO_AFRO",weight=1)
goarn_network.add_edge("Catholic Relief Services", "WHO_AFRO",weight=1)
goarn_network.add_edge("Lacor Hospital", "WHO_AFRO",weight=1)
goarn_network.add_edge("Red Crescent societies", "WHO_AFRO",weight=1)
goarn_network.add_edge("ICRC", "WHO_AFRO",weight=1)
goarn_network.add_edge("Save the Children-Denmark", "WHO_AFRO",weight=1)
goarn_network.add_edge("WHO_AFRO", "World Food Programme",weight=1)
goarn_network.add_edge("WHO_AFRO", "World Vision",weight=1)
goarn_network.add_edge("UNICEF", "WHO_AFRO",weight=1)
goarn_network.add_edge("United Kingdom Department for International Development (DFID)", "WHO_AFRO",weight=1)
goarn_network.add_edge("USAID", "WHO_AFRO",weight=1)
goarn_network.add_edge("Action Contre la Faim", "African Medical and Research Foundation",weight=1)
goarn_network.add_edge("ACORD-UK", "Action Contre la Faim",weight=1)
goarn_network.add_edge("Action Contre la Faim", "Catholic Relief Services",weight=1)
goarn_network.add_edge("Action Contre la Faim", "Lacor Hospital",weight=1)
goarn_network.add_edge("Action Contre la Faim", "Red Crescent societies",weight=1)
goarn_network.add_edge("Action Contre la Faim", "ICRC",weight=1)
goarn_network.add_edge("Action Contre la Faim", "Save the Children-Denmark",weight=1)
goarn_network.add_edge("Action Contre la Faim", "World Food Programme",weight=1)
goarn_network.add_edge("Action Contre la Faim", "World Vision",weight=1)
goarn_network.add_edge("Action Contre la Faim", "UNICEF",weight=1)
goarn_network.add_edge("Action Contre la Faim", "United Kingdom Department for International Development (DFID)",weight=1)
goarn_network.add_edge("Action Contre la Faim", "USAID",weight=1)
goarn_network.add_edge("ACORD-UK", "African Medical and Research Foundation",weight=1)
goarn_network.add_edge("African Medical and Research Foundation", "Catholic Relief Services",weight=1)
goarn_network.add_edge("African Medical and Research Foundation", "Lacor Hospital",weight=1)
goarn_network.add_edge("African Medical and Research Foundation", "Red Crescent societies",weight=1)
goarn_network.add_edge("African Medical and Research Foundation", "ICRC",weight=1)
goarn_network.add_edge("African Medical and Research Foundation", "Save the Children-Denmark",weight=1)
goarn_network.add_edge("African Medical and Research Foundation", "World Food Programme",weight=1)
goarn_network.add_edge("African Medical and Research Foundation", "World Vision",weight=1)
goarn_network.add_edge("African Medical and Research Foundation", "UNICEF",weight=1)
goarn_network.add_edge("African Medical and Research Foundation", "United Kingdom Department for International Development (DFID)",weight=1)
goarn_network.add_edge("African Medical and Research Foundation", "USAID",weight=1)
goarn_network.add_edge("ACORD-UK", "Catholic Relief Services",weight=1)
goarn_network.add_edge("ACORD-UK", "Lacor Hospital",weight=1)
goarn_network.add_edge("ACORD-UK", "Red Crescent societies",weight=1)
goarn_network.add_edge("ACORD-UK", "ICRC",weight=1)
goarn_network.add_edge("ACORD-UK", "Save the Children-Denmark",weight=1)
goarn_network.add_edge("ACORD-UK", "World Food Programme",weight=1)
goarn_network.add_edge("ACORD-UK", "World Vision",weight=1)
goarn_network.add_edge("ACORD-UK", "UNICEF",weight=1)
goarn_network.add_edge("ACORD-UK", "United Kingdom Department for International Development (DFID)",weight=1)
goarn_network.add_edge("ACORD-UK", "USAID",weight=1)
goarn_network.add_edge("Catholic Relief Services", "Lacor Hospital",weight=1)
goarn_network.add_edge("Catholic Relief Services", "Red Crescent societies",weight=1)
goarn_network.add_edge("Catholic Relief Services", "ICRC",weight=1)
goarn_network.add_edge("Catholic Relief Services", "Save the Children-Denmark",weight=1)
goarn_network.add_edge("Catholic Relief Services", "World Food Programme",weight=1)
goarn_network.add_edge("Catholic Relief Services", "World Vision",weight=1)
goarn_network.add_edge("Catholic Relief Services", "UNICEF",weight=1)
goarn_network.add_edge("Catholic Relief Services", "United Kingdom Department for International Development (DFID)",weight=1)
goarn_network.add_edge("Catholic Relief Services", "USAID",weight=1)
goarn_network.add_edge("Lacor Hospital", "Red Crescent societies",weight=1)
goarn_network.add_edge("ICRC", "Lacor Hospital",weight=1)
goarn_network.add_edge("Lacor Hospital", "Save the Children-Denmark",weight=1)
goarn_network.add_edge("Lacor Hospital", "World Food Programme",weight=1)
goarn_network.add_edge("Lacor Hospital", "World Vision",weight=1)
goarn_network.add_edge("Lacor Hospital", "UNICEF",weight=1)
goarn_network.add_edge("Lacor Hospital", "United Kingdom Department for International Development (DFID)",weight=1)
goarn_network.add_edge("Lacor Hospital", "USAID",weight=1)
goarn_network.add_edge("ICRC", "Red Crescent societies",weight=1)
goarn_network.add_edge("Red Crescent societies", "Save the Children-Denmark",weight=1)
goarn_network.add_edge("Red Crescent societies", "World Food Programme",weight=1)
goarn_network.add_edge("Red Crescent societies", "World Vision",weight=1)
goarn_network.add_edge("Red Crescent societies", "UNICEF",weight=1)
goarn_network.add_edge("Red Crescent societies", "United Kingdom Department for International Development (DFID)",weight=1)
goarn_network.add_edge("Red Crescent societies", "USAID",weight=1)
goarn_network.add_edge("ICRC", "Save the Children-Denmark",weight=1)
goarn_network.add_edge("ICRC", "World Food Programme",weight=1)
goarn_network.add_edge("ICRC", "World Vision",weight=1)
goarn_network.add_edge("ICRC", "UNICEF",weight=1)
goarn_network.add_edge("ICRC", "United Kingdom Department for International Development (DFID)",weight=1)
goarn_network.add_edge("ICRC", "USAID",weight=1)
goarn_network.add_edge("Save the Children-Denmark", "World Food Programme",weight=1)
goarn_network.add_edge("Save the Children-Denmark", "World Vision",weight=1)
goarn_network.add_edge("Save the Children-Denmark", "UNICEF",weight=1)
goarn_network.add_edge("Save the Children-Denmark", "United Kingdom Department for International Development (DFID)",weight=1)
goarn_network.add_edge("Save the Children-Denmark", "USAID",weight=1)
goarn_network.add_edge("World Food Programme", "World Vision",weight=1)
goarn_network.add_edge("UNICEF", "World Food Programme",weight=1)
goarn_network.add_edge("United Kingdom Department for International Development (DFID)", "World Food Programme",weight=1)
goarn_network.add_edge("USAID", "World Food Programme",weight=1)
goarn_network.add_edge("UNICEF", "World Vision",weight=1)
goarn_network.add_edge("United Kingdom Department for International Development (DFID)", "World Vision",weight=1)
goarn_network.add_edge("USAID", "World Vision",weight=1)
goarn_network.add_edge("UNICEF", "United Kingdom Department for International Development (DFID)",weight=1)
goarn_network.add_edge("UNICEF", "USAID",weight=1)
goarn_network.add_edge("USAID", "United Kingdom Department for International Development (DFID)",weight=1)

#import csv
#with open("/Users/grizzlemuff/Documents/SI608/GOARN/2000.csv", 'wb') as csvfile:
#    spamwriter = csv.writer(csvfile)
#    spamwriter.writerow('D')
#    centrality=  nx.degree_centrality(goarn_network)
#    for each in centrality.items():
#        print 'Degree Centrality: ', each[0], each[1]
#        print each
#        spamwriter.writerow([each[0], each[1]])
#    
#    spamwriter.writerow('C')
#    close=nx.closeness_centrality(goarn_network)    
#    for each in close.items():
#        print 'Closeness Centrality: ', each[0], '\t', each[1]
#        spamwriter.writerow([each[0], each[1]])
#
#    spamwriter.writerow('B')
#    btwn=nx.betweenness_centrality(goarn_network, weight='weight')
#    for each in btwn.items():
#        print 'Betweeness Centrality: ', each[0], each[1]
#        spamwriter.writerow([each[0], each[1]])
#
#    avg_clust= nx.average_clustering(goarn_network)
#    print 'Average Clustering: ', avg_clust
#    
#
#
#
#    clustering = nx.clustering(goarn_network)
#
#    spamwriter.writerow('L')
#    for each in clustering.items():
#        print 'Clustering Coefficient per Node: ', each[0], each[1]
#        spamwriter.writerow([each[0], each[1]])
#    csvfile.close()
#
#nx.draw_spring(goarn_network,  k=0.95,iterations=20 )
#plt.show()


#
#def most_important(G):
# """ returns a copy of G with
#     the most important nodes
#     according to the pagerank """ 
# ranking = nx.betweenness_centrality(G).items()
# print ranking
# r = [x[1] for x in ranking]
# m = sum(r)/len(r) # mean centrality
# t = m*3 # threshold, we keep only the nodes with 3 times the mean
# Gt = G.copy()
# for k, v in ranking:
#  if v < t:
#   Gt.remove_node(k)
# return Gt
#
#Gt = most_important(goarn_network) # trimming
#
#from pylab import show
## create the layout
#pos = nx.spring_layout(goarn_network)
## draw the nodes and the edges (all)
#nx.draw_networkx_nodes(goarn_network,pos,node_color='b',alpha=0.2,node_size=8)
#nx.draw_networkx_edges(goarn_network,pos,alpha=0.1)
#
## draw the most important nodes with a different style
#nx.draw_networkx_nodes(Gt,pos,node_color='r',alpha=0.4,node_size=254)
## also the labels this time
#nx.draw_networkx_labels(Gt,pos,font_size=12,font_color='b')
#show()








#from networkx.algorithms import bipartite
#print bipartite.is_bipartite(goarn_network)

from networkx import find_cliques
cliques = list(find_cliques(goarn_network))
bigg= max(cliques, key=lambda l: len(l))
print bigg
print nx.graph_number_of_cliques(goarn_network, cliques)

#
#print nx.eigenvector_centrality(goarn_network)

H=nx.connected_component_subgraphs(goarn_network)[0]
print(nx.average_shortest_path_length(H))

#
#def trim_nodes(goarn_network,d):
# """ returns a copy of G without 
#     the nodes with a degree less than d """
# Gt = goarn_network.copy()
# dn = nx.degree(Gt)
# for n in Gt.nodes():
#  if dn[n] <= d:
#   Gt.remove_node(n)
# return Gt
#
##drawing the network without nodes with degree less than 10
#
#
#Gt = trim_nodes(goarn_network,10)
#plt.figure(1)
#plt.title("2000 Network of nodes with at least degree of 10")
#nx.draw(Gt,node_size=0,node_color='w',edge_color='b',alpha=.2, with_labels=False)
#plt.show()

print len(list(nx.k_clique_communities(goarn_network, 5)))
print len(goarn_network.nodes())