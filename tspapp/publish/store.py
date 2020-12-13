from abc import abstractmethod
import threading 
store_lock = threading.Lock()

class Singleton(object):
    _instance = None
    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance

class Store:
    @abstractmethod
    def add(self):
        pass
    @abstractmethod
    def get(self, vehical_id):
        pass
    @abstractmethod    
    def update(self, data):
        pass

class VehicalStore(Singleton, Store):
    def __init__(self):
        self.vehical_data = []
    
    def add(self, data):
        store_lock.acquire()
        self.vehical_data.append(data)
        store_lock.release()
    
    def get(self, vehical_id):
        for vdata in self.vehical_data:
            if vdata["id"] == vehical_id:
                return vdata
        return None

    def update(self, vehical_id ,field, data):
        store_lock.acquire()
        for vdata in self.vehical_data:
            if vdata["id"] == vehical_id:
                vdata[field] = data
        store_lock.release()