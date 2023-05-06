
def createAtlasConfigString(lox,loy,hox,hoy,opacity):
#     config_string = """
#
# rect {
#   lo {
#     lat_e7: 387399950
#     lng_e7: 3386614835
#   }
#   hi {
#     lat_e7:
#     lng_e7:
#   }
# }
# radians: 0.0
# opacity: 0.457482995923
#
# """

    config_ml_string = (
        "rect {\n"
        "  lo {\n"
        f"    lat_e7: {lox}\n"
        f"    lng_e7: {loy}\n"
        "  }\n"
        "  hi {\n"
        f"    lat_e7: {hox}\n"
        f"    lng_e7: {hoy}\n"
        "  }\n"
        "{\n"
        "radians : 0.0\n"
        f"opacity: {opacity}\n"
    )

    return config_ml_string



