# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTableShrinkRequest(DaraModel):
    def __init__(
        self,
        catalog: str = None,
        client_token: str = None,
        columns_shrink: str = None,
        comment: str = None,
        name: str = None,
        namespace: str = None,
        retention_policy_shrink: str = None,
    ):
        # 表所属的数据目录名称。可通过 ListCatalogs 获取已有目录列表
        self.catalog = catalog
        # 用于保证请求幂等性的Token，防止因网络重试导致重复创建。建议使用 UUID
        self.client_token = client_token
        # 表的列定义（JSON 数组）。每列包含 Name（列名，必填）、Type（数据类型，必填，如 STRING、INT32、INT64、FLOAT、DOUBLE、BOOLEAN、TIMESTAMP）、Comment（列备注，选填）
        self.columns_shrink = columns_shrink
        # 表的备注描述信息，无格式限制
        self.comment = comment
        # 事件表名称。以字母或数字开头，支持字母、数字、下划线和短横线，长度1~127。在同一命名空间下唯一
        # 
        # This parameter is required.
        self.name = name
        # 表所属的命名空间名称。可通过 ListNamespaces 获取已有命名空间列表
        self.namespace = namespace
        # 数据保留策略（JSON 对象）。包含 HotTTL（热数据保留天数，高性能查询）和 ColdTTL（冷数据保留天数，低成本存储）。不传则使用系统默认值
        self.retention_policy_shrink = retention_policy_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog is not None:
            result['Catalog'] = self.catalog

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.columns_shrink is not None:
            result['Columns'] = self.columns_shrink

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.retention_policy_shrink is not None:
            result['RetentionPolicy'] = self.retention_policy_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Catalog') is not None:
            self.catalog = m.get('Catalog')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Columns') is not None:
            self.columns_shrink = m.get('Columns')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('RetentionPolicy') is not None:
            self.retention_policy_shrink = m.get('RetentionPolicy')

        return self

