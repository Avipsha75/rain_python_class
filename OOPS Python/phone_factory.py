class PhoneFactory:
    model: None
    color: None
    is_android: None
    
    def __init__(self, model, color, is_android):
        self.model = model
        self.color = color
        self.is_android = is_android
        print("Phone Created")

    def __str__(self):
        return f"{self.model} - {self.color}"
    
    def check_os(self):
        if self.is_android:
            print("Android")
        else:
            print("iOS")

oppo_phone_1 = PhoneFactory("A53", "black", True)
print(oppo_phone_1)