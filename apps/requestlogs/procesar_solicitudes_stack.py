class PilaSolicitudesLogs:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PilaSolicitudesLogs, cls).__new__(cls)
            cls._instance.stack = []  # Aquí se almacenarán los logs
        return cls._instance

    def agregar(self, log):
        self.stack.append(log)

    def obtener_ultimo(self):
        if self.stack:
            return self.stack.pop()
        return None

    def obtener_todos(self):
        return list(self.stack)
