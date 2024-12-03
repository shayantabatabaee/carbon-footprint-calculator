labels = {
    'WINDOW_TITLE': 'Carbon Footprint Calculator',
    'PDF_VIEWER_WINDOW_TITLE': 'PDF Report',
    'COMPANY_NAME_TITLE': 'Company Name',
    'COMPANY_NAME_QUESTION': 'Enter company name',
    'ENERGY_USAGE_TITLE': 'Energy Usage',
    'ENERGY_USAGE_QUESTION_1': 'What is your average monthly electricity bill in euros?',
    'ENERGY_USAGE_QUESTION_2': 'What is your average monthly natural gas bill in euros?',
    'ENERGY_USAGE_QUESTION_3': 'What is your average monthly fuel bill for transportation in euros?',
    'WASTE_TITLE': 'Waste',
    'WASTE_QUESTION_1': 'How much waste do you generate per months in kilograms?',
    'WASTE_QUESTION_2': 'How much of that waste is recycled or composted (in percentage)?',
    'BUSINESS_TRAVEL_TITLE': 'Business Travel',
    'BUSINESS_TRAVEL_QUESTION_1': 'How many kilometers do your employees travel per year for business purposes? ',
    'BUSINESS_TRAVEL_QUESTION_2': 'What is the average fuel efficiency of the vehicles used for business travel in liters per 100 kilometers?',
    'CLEAR_BUTTON': 'Clear',
    'SUBMIT_BUTTON': 'Submit Company',
    'FULL_REPORT_BUTTON': 'Full Report',
    'EMPTY_INPUT_TITLE': 'Empty Input',
    'EMPTY_INPUT_TEXT': 'Input should not be empty, make sure the input is correct!',
    'UNKNOWN_ERROR': 'Unknown error',
    'UNKNOWN_ERROR_TEXT': 'Unknown error occurred, please refer to log for further information!',
    'NETWORK_ERROR': 'Network error',
    'EMPTY_COMPANY_TITLE': 'Empty Company',
    'EMPTY_COMPANY_TEXT': 'The number of companies must be greater than one',
}

full_report = ("# **Carbon Footprint Report Across Companies**\n\n"
               "In this report, the companies are compared in detail regarding their carbon footprints."
               "To have a better insight about the usages of companies, the following table and bar chart are provided."
               "The companies have been sorted by their total usage during one year. The most carbon footprints "
               "usage belongs to {0} company.\n")

full_report += "## Table\n"
full_report += "{1}"
full_report += "## Chart\n"
full_report += '![Bar Chart]({2})'
