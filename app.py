class Phone:
  def __init__(self, phone_number):
    self.number = phone_number

  def call(self, other_number):
    print(f"Calling {other_number}.")

  def text(self, other_number, msg):
    print(f"Sending text from {self.number} to {other_number}: {msg}")

class iPhone(Phone):
  def __init__(self, phone_number):
    super().__init__(phone_number)
    self.fingerprint = None

    def set_fingerprint(self, fingerprint):
      self.fingerprint = fingerprint
    
    def unlock(self, fingerprint=None):
      if (fingerprint == self.fingerprint):
        print("Phone unlocked. Fingerprint matches.")
      else:
        print("Phone locked. ACCESS DENIED")

class Android(Phone):
  def __init__(self, phone_number):
    super().__init__(phone_number)
    self.keyboard = "Default"

    def set_keyboard(self, keyboard):
      self.keyboard