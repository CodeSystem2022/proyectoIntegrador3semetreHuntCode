import Capas_log.Logger as log

class individuos:
    def __init__(self, idIndividuos=None, nombre=None, apellido=None, contraseña=None, email=None):
        self._idIndividuos = idIndividuos
        self._nombre = nombre
        self._apellido = apellido
        self._contraseña = contraseña
        self._email = email

    def __str__(self):
        return f'''
            Id: {self._idIndividuos},
            Nombre: {self._nombre},
            Apellido: {self._apellido},
            contraseña: {self._contraseña},
            Email: {self._email}
        '''

    # Metodos Getters and Setters
    @property
    def idIndividuos(self):
        return self.idIndividuos

    @idIndividuos.setter
    def idIndividuos(self, idIndividuos):
        self._idIndividuos

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido

    @property
    def contraseña(self):
        return self._contraseña

    @contraseña.setter
    def apellido(self, contraseña):
        self._contraseña

    @property
    def email(self):
        return self._email

    @email.setter
    def nombre(self, email):
        self._email

'''
if __name__ == '__main__':
    individuo1 = individuos(1, 'Juan', 'Perez', 'jperez@mail.com')
    log.debug(individuo1)
    individuo2 = individuos(nombre='Jose', apellido='Lepez', email='jlepez@mail.com')
    log.debug(individuo2)
    individuo1 = individuos(id_persona=1)
    log.debug(individuo1)
'''