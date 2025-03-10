import zlib

from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)


class DataSource:
    def read(self) -> bytes: ...

    def write(self, data: bytes): ...


class DataSourceDecorator(DataSource):
    def __init__(self, data_source: DataSource):
        self.data_source = data_source


class EncryptedDataSource(DataSourceDecorator):

    def write(self, data: bytes):
        return self.data_source.write(cipher.encrypt(data))

    def read(self):
        return cipher.decrypt(self.data_source.read())


class CompressedDataSource(DataSourceDecorator):
    def write(self, data: bytes):
        return self.data_source.write(zlib.compress(data))

    def read(self):
        return zlib.decompress(self.data_source.read())


class FileDataSource(DataSource):
    def __init__(self, filename):
        self.filename = filename

    def write(self, data: bytes):
        with open(self.filename, "wb") as file:
            file.write(data)

    def read(self) -> bytes:
        with open(self.filename, "rb") as file:
            return file.read()


if __name__ == "__main__":
    data_source = FileDataSource("myfile.txt")
    data_source = CompressedDataSource(data_source)
    data_source = EncryptedDataSource(data_source)
    data_source.write(b"my test data 123123 asdasd")
    print(data_source.read())
