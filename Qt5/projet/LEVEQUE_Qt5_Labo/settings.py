from PyQt5.QtCore       import QSettings

class Settings():

    def __init__(self, companyName, applicationName):
        self.__settings = QSettings(companyName, applicationName)

    def clear(self):
        self.__settings.clear()

    # API
    def get_selected_language(self):
        return self.__settings.value("Simply-Paint-Settings/selected_language")

    def set_selected_language(self, lang):
        self.__settings.setValue("Simply-Paint-Settings/selected_language", lang)


if __name__=='__main__':
    s = Settings("MySoft", "Simply Paint")
    s.clear()