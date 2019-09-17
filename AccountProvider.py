from PyQt5.QtWidgets import *


class AccountProvider(QWizardPage):

    provider = None
    
    def __init__(self, parent=None):
        super(AccountProvider,self).__init__(parent)

