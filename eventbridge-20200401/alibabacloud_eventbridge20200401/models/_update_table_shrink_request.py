# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateTableShrinkRequest(DaraModel):
    def __init__(
        self,
        add_column_shrink: str = None,
        catalog: str = None,
        client_token: str = None,
        delete_column_shrink: str = None,
        name: str = None,
        namespace: str = None,
        rename_column_shrink: str = None,
        update_column_comment_shrink: str = None,
        update_column_type_shrink: str = None,
        update_comment: str = None,
        update_retention_policy_shrink: str = None,
    ):
        # 新增列定义（JSON 对象）。包含 Name（列名，必填）、Type（数据类型，必填，如 STRING、INT32、INT64、FLOAT、DOUBLE、BOOLEAN、TIMESTAMP）、Comment（列备注，选填）。每次调用只能新增一列
        self.add_column_shrink = add_column_shrink
        # 表所属的数据目录名称。可通过 ListCatalogs 获取
        self.catalog = catalog
        # 用于保证请求幂等性的Token。建议使用 UUID
        self.client_token = client_token
        # 删除列定义（JSON 对象）。包含 Name（要删除的列名，必填）。删除后不可恢复，已有数据中该列的值将丢失。每次调用只能删除一列
        self.delete_column_shrink = delete_column_shrink
        # 要修改的事件表名称。名称本身不可修改，此处用于定位目标表。需同时指定所属 Catalog 和 Namespace。可通过 ListTables 获取
        # 
        # This parameter is required.
        self.name = name
        # 表所属的命名空间名称。可通过 ListNamespaces 获取
        self.namespace = namespace
        # 重命名列（JSON 对象）。包含 Name（原列名，必填）、NewName（新列名，必填）。每次调用只能重命名一列
        self.rename_column_shrink = rename_column_shrink
        # 修改列的备注信息（JSON 对象）。包含 Name（目标列名，必填）、Comment（新备注内容，必填，传空字符串可清除备注）。每次调用只能修改一列
        self.update_column_comment_shrink = update_column_comment_shrink
        # 修改列的数据类型（JSON 对象）。包含 Name（目标列名，必填）、Type（新数据类型，必填）。仅支持兼容类型转换，每次调用只能修改一列
        self.update_column_type_shrink = update_column_type_shrink
        # 修改表的备注描述。传入新的备注内容替换原有备注，传空字符串可清除备注
        self.update_comment = update_comment
        # 修改数据保留策略（JSON 对象）。包含 HotTTL（热数据保留天数）、ColdTTL（冷数据保留天数）。传入后会替换原有策略
        self.update_retention_policy_shrink = update_retention_policy_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_column_shrink is not None:
            result['AddColumn'] = self.add_column_shrink

        if self.catalog is not None:
            result['Catalog'] = self.catalog

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.delete_column_shrink is not None:
            result['DeleteColumn'] = self.delete_column_shrink

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.rename_column_shrink is not None:
            result['RenameColumn'] = self.rename_column_shrink

        if self.update_column_comment_shrink is not None:
            result['UpdateColumnComment'] = self.update_column_comment_shrink

        if self.update_column_type_shrink is not None:
            result['UpdateColumnType'] = self.update_column_type_shrink

        if self.update_comment is not None:
            result['UpdateComment'] = self.update_comment

        if self.update_retention_policy_shrink is not None:
            result['UpdateRetentionPolicy'] = self.update_retention_policy_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddColumn') is not None:
            self.add_column_shrink = m.get('AddColumn')

        if m.get('Catalog') is not None:
            self.catalog = m.get('Catalog')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DeleteColumn') is not None:
            self.delete_column_shrink = m.get('DeleteColumn')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('RenameColumn') is not None:
            self.rename_column_shrink = m.get('RenameColumn')

        if m.get('UpdateColumnComment') is not None:
            self.update_column_comment_shrink = m.get('UpdateColumnComment')

        if m.get('UpdateColumnType') is not None:
            self.update_column_type_shrink = m.get('UpdateColumnType')

        if m.get('UpdateComment') is not None:
            self.update_comment = m.get('UpdateComment')

        if m.get('UpdateRetentionPolicy') is not None:
            self.update_retention_policy_shrink = m.get('UpdateRetentionPolicy')

        return self

