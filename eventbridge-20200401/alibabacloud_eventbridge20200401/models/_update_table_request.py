# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class UpdateTableRequest(DaraModel):
    def __init__(
        self,
        add_column: main_models.UpdateTableRequestAddColumn = None,
        catalog: str = None,
        client_token: str = None,
        delete_column: main_models.UpdateTableRequestDeleteColumn = None,
        name: str = None,
        namespace: str = None,
        rename_column: main_models.UpdateTableRequestRenameColumn = None,
        update_column_comment: main_models.UpdateTableRequestUpdateColumnComment = None,
        update_column_type: main_models.UpdateTableRequestUpdateColumnType = None,
        update_comment: str = None,
        update_retention_policy: main_models.UpdateTableRequestUpdateRetentionPolicy = None,
    ):
        # 新增列定义（JSON 对象）。包含 Name（列名，必填）、Type（数据类型，必填，如 STRING、INT32、INT64、FLOAT、DOUBLE、BOOLEAN、TIMESTAMP）、Comment（列备注，选填）。每次调用只能新增一列
        self.add_column = add_column
        # 表所属的数据目录名称。可通过 ListCatalogs 获取
        self.catalog = catalog
        # 用于保证请求幂等性的Token。建议使用 UUID
        self.client_token = client_token
        # 删除列定义（JSON 对象）。包含 Name（要删除的列名，必填）。删除后不可恢复，已有数据中该列的值将丢失。每次调用只能删除一列
        self.delete_column = delete_column
        # 要修改的事件表名称。名称本身不可修改，此处用于定位目标表。需同时指定所属 Catalog 和 Namespace。可通过 ListTables 获取
        # 
        # This parameter is required.
        self.name = name
        # 表所属的命名空间名称。可通过 ListNamespaces 获取
        self.namespace = namespace
        # 重命名列（JSON 对象）。包含 Name（原列名，必填）、NewName（新列名，必填）。每次调用只能重命名一列
        self.rename_column = rename_column
        # 修改列的备注信息（JSON 对象）。包含 Name（目标列名，必填）、Comment（新备注内容，必填，传空字符串可清除备注）。每次调用只能修改一列
        self.update_column_comment = update_column_comment
        # 修改列的数据类型（JSON 对象）。包含 Name（目标列名，必填）、Type（新数据类型，必填）。仅支持兼容类型转换，每次调用只能修改一列
        self.update_column_type = update_column_type
        # 修改表的备注描述。传入新的备注内容替换原有备注，传空字符串可清除备注
        self.update_comment = update_comment
        # 修改数据保留策略（JSON 对象）。包含 HotTTL（热数据保留天数）、ColdTTL（冷数据保留天数）。传入后会替换原有策略
        self.update_retention_policy = update_retention_policy

    def validate(self):
        if self.add_column:
            self.add_column.validate()
        if self.delete_column:
            self.delete_column.validate()
        if self.rename_column:
            self.rename_column.validate()
        if self.update_column_comment:
            self.update_column_comment.validate()
        if self.update_column_type:
            self.update_column_type.validate()
        if self.update_retention_policy:
            self.update_retention_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_column is not None:
            result['AddColumn'] = self.add_column.to_map()

        if self.catalog is not None:
            result['Catalog'] = self.catalog

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.delete_column is not None:
            result['DeleteColumn'] = self.delete_column.to_map()

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.rename_column is not None:
            result['RenameColumn'] = self.rename_column.to_map()

        if self.update_column_comment is not None:
            result['UpdateColumnComment'] = self.update_column_comment.to_map()

        if self.update_column_type is not None:
            result['UpdateColumnType'] = self.update_column_type.to_map()

        if self.update_comment is not None:
            result['UpdateComment'] = self.update_comment

        if self.update_retention_policy is not None:
            result['UpdateRetentionPolicy'] = self.update_retention_policy.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddColumn') is not None:
            temp_model = main_models.UpdateTableRequestAddColumn()
            self.add_column = temp_model.from_map(m.get('AddColumn'))

        if m.get('Catalog') is not None:
            self.catalog = m.get('Catalog')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DeleteColumn') is not None:
            temp_model = main_models.UpdateTableRequestDeleteColumn()
            self.delete_column = temp_model.from_map(m.get('DeleteColumn'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('RenameColumn') is not None:
            temp_model = main_models.UpdateTableRequestRenameColumn()
            self.rename_column = temp_model.from_map(m.get('RenameColumn'))

        if m.get('UpdateColumnComment') is not None:
            temp_model = main_models.UpdateTableRequestUpdateColumnComment()
            self.update_column_comment = temp_model.from_map(m.get('UpdateColumnComment'))

        if m.get('UpdateColumnType') is not None:
            temp_model = main_models.UpdateTableRequestUpdateColumnType()
            self.update_column_type = temp_model.from_map(m.get('UpdateColumnType'))

        if m.get('UpdateComment') is not None:
            self.update_comment = m.get('UpdateComment')

        if m.get('UpdateRetentionPolicy') is not None:
            temp_model = main_models.UpdateTableRequestUpdateRetentionPolicy()
            self.update_retention_policy = temp_model.from_map(m.get('UpdateRetentionPolicy'))

        return self

class UpdateTableRequestUpdateRetentionPolicy(DaraModel):
    def __init__(
        self,
        cold_ttl: int = None,
        hot_ttl: int = None,
    ):
        self.cold_ttl = cold_ttl
        self.hot_ttl = hot_ttl

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cold_ttl is not None:
            result['ColdTTL'] = self.cold_ttl

        if self.hot_ttl is not None:
            result['HotTTL'] = self.hot_ttl

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColdTTL') is not None:
            self.cold_ttl = m.get('ColdTTL')

        if m.get('HotTTL') is not None:
            self.hot_ttl = m.get('HotTTL')

        return self

class UpdateTableRequestUpdateColumnType(DaraModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
    ):
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class UpdateTableRequestUpdateColumnComment(DaraModel):
    def __init__(
        self,
        comment: str = None,
        name: str = None,
    ):
        self.comment = comment
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class UpdateTableRequestRenameColumn(DaraModel):
    def __init__(
        self,
        name: str = None,
        new_name: str = None,
    ):
        self.name = name
        self.new_name = new_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.new_name is not None:
            result['NewName'] = self.new_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NewName') is not None:
            self.new_name = m.get('NewName')

        return self

class UpdateTableRequestDeleteColumn(DaraModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class UpdateTableRequestAddColumn(DaraModel):
    def __init__(
        self,
        comment: str = None,
        name: str = None,
        type: str = None,
    ):
        self.comment = comment
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

