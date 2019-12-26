class BaseEntity:
    def __init__(self, id_, table_name):
        self.id_ = id_
        self.table_name = table_name

    def get_table_variable_names(self):
        entity_dict = self.__dict__
        entity_dict.pop('table_name')
        return ','.join(map(str, list(entity_dict.keys())))

    def get_table_variables(self):
        entity_dict = self.__dict__
        entity_dict.pop('table_name')
        return ','.join(map(str, list(entity_dict.values())))
