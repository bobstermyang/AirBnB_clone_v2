#!/usr/bin/python3
import json
from datetime import datetime
from models import *


class FileStorage:
    __file_path = "file.json"
    __objects = {}
    valid_classes = ["State", "City", "Amenity", "Place", "BaseModel",
                     "Review", "User"]

    def __init__(self):
        self.reload()

    def all(self, cls=None):
        if cls in self.valid_classes:
            cls_obj = eval(cls)()
            return_cls = {}
            for obj_id, obj_obj in FileStorage.__objects.items():
                if type(obj_obj) == type(cls_obj):
                    return_cls[obj_id] = obj_obj
            return return_cls
        elif cls is None:
            return FileStorage.__objects
        else:
            pass

    def new(self, obj):
        if obj is not None:
            FileStorage.__objects[obj.id] = obj

    def save(self):
        store = {}
        for k in FileStorage.__objects.keys():
            store[k] = FileStorage.__objects[k].to_json()

        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as fd:
            fd.write(json.dumps(store))

    def reload(self):
        try:
            with open(FileStorage.__file_path,
                      mode="r+", encoding="utf-8") as fd:
                FileStorage.__objects = {}
                temp = json.load(fd)
                for k in temp.keys():
                    cls = temp[k].pop("__class__", None)
                    cr_at = temp[k]["created_at"]
                    cr_at = datetime.strptime(cr_at, "%Y-%m-%d %H:%M:%S.%f")
                    if hasattr(temp[k], "updated_at"):
                        up_at = temp[k]["updated_at"]
                        up_at = datetime.strptime(up_at,
                                                  "%Y-%m-%d %H:%M:%S.%f")
                    FileStorage.__objects[k] = eval(cls)(temp[k])
        except Exception as e:
            pass

    def close(self):
        self.reload()

    def delete(self, obj=None):
        if hasattr(obj, '__object'):
            del obj
