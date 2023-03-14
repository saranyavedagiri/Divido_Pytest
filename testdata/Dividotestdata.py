from Utlilties.ExcelRead import Excel_Read


class dividotestdata():
    filepath = "C:\\Users\\SaranyaV\\PycharmProjects\\Divido_Pytest\\Inputfiles\\Divido_Test_data.xlsx"
    sheet_name = "CreateapplicationTD"
    logintestdata=[("saranyavedagiri@duologi.com","Alphabeta123#")]
    credential_excel_dic = [Excel_Read.retrundicvalue(filepath,sheet_name)]

