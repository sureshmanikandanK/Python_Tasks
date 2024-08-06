class Mobile:
    def __init__(self,brand,RAM):
        self.brand = brand
        self.RAM = RAM
    def Display(self):
        print(f'{self.brand} {self.RAM}')

Mobile_phone=Mobile('Vivo','8Gb')
Mobile_phone1=Mobile('Realme','8Gb')
Mobile_phone2=Mobile('oppo','8Gb')
Mobile_phone.Display()
Mobile_phone1.Display()
Mobile_phone2.Display()