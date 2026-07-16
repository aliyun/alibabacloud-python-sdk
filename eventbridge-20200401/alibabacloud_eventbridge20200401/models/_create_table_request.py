# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class CreateTableRequest(DaraModel):
    def __init__(
        self,
        catalog: str = None,
        client_token: str = None,
        columns: List[main_models.CreateTableRequestColumns] = None,
        comment: str = None,
        name: str = None,
        namespace: str = None,
        retention_policy: main_models.CreateTableRequestRetentionPolicy = None,
    ):
        # 表所属的数据目录名称。可通过 ListCatalogs 获取已有目录列表
        self.catalog = catalog
        # 用于保证请求幂等性的Token，防止因网络重试导致重复创建。建议使用 UUID
        self.client_token = client_token
        # 表的列定义（JSON 数组）。每列包含 Name（列名，必填）、Type（数据类型，必填，如 STRING、INT32、INT64、FLOAT、DOUBLE、BOOLEAN、TIMESTAMP）、Comment（列备注，选填）
        self.columns = columns
        # 表的备注描述信息，无格式限制
        self.comment = comment
        # 事件表名称。以字母或数字开头，支持字母、数字、下划线和短横线，长度1~127。在同一命名空间下唯一
        # 
        # This parameter is required.
        self.name = name
        # 表所属的命名空间名称。可通过 ListNamespaces 获取已有命名空间列表
        self.namespace = namespace
        # 数据保留策略（JSON 对象）。包含 HotTTL（热数据保留天数，高性能查询）和 ColdTTL（冷数据保留天数，低成本存储）。不传则使用系统默认值
        self.retention_policy = retention_policy

    def validate(self):
        if self.columns:
            for v1 in self.columns:
                 if v1:
                    v1.validate()
        if self.retention_policy:
            self.retention_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog is not None:
            result['Catalog'] = self.catalog

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        result['Columns'] = []
        if self.columns is not None:
            for k1 in self.columns:
                result['Columns'].append(k1.to_map() if k1 else None)

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.retention_policy is not None:
            result['RetentionPolicy'] = self.retention_policy.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Catalog') is not None:
            self.catalog = m.get('Catalog')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        self.columns = []
        if m.get('Columns') is not None:
            for k1 in m.get('Columns'):
                temp_model = main_models.CreateTableRequestColumns()
                self.columns.append(temp_model.from_map(k1))

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('RetentionPolicy') is not None:
            temp_model = main_models.CreateTableRequestRetentionPolicy()
            self.retention_policy = temp_model.from_map(m.get('RetentionPolicy'))

        return self

class CreateTableRequestRetentionPolicy(DaraModel):
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

class CreateTableRequestColumns(DaraModel):
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

