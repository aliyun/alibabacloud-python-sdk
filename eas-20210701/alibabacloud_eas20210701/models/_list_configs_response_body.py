# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eas20210701 import models as main_models
from darabonba.model import DaraModel

class ListConfigsResponseBody(DaraModel):
    def __init__(
        self,
        configs: List[main_models.ListConfigsResponseBodyConfigs] = None,
        has_more: bool = None,
        name: str = None,
        page: int = None,
        page_size: int = None,
        total: int = None,
        type: str = None,
    ):
        # 配置项列表
        self.configs = configs
        # 是否有更多数据
        self.has_more = has_more
        # 服务名称
        self.name = name
        # 当前页码
        self.page = page
        # 每页数量
        self.page_size = page_size
        # 总数量
        self.total = total
        # 配置类型
        self.type = type

    def validate(self):
        if self.configs:
            for v1 in self.configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Configs'] = []
        if self.configs is not None:
            for k1 in self.configs:
                result['Configs'].append(k1.to_map() if k1 else None)

        if self.has_more is not None:
            result['HasMore'] = self.has_more

        if self.name is not None:
            result['Name'] = self.name

        if self.page is not None:
            result['Page'] = self.page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total is not None:
            result['Total'] = self.total

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.configs = []
        if m.get('Configs') is not None:
            for k1 in m.get('Configs'):
                temp_model = main_models.ListConfigsResponseBodyConfigs()
                self.configs.append(temp_model.from_map(k1))

        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListConfigsResponseBodyConfigs(DaraModel):
    def __init__(
        self,
        created_at: str = None,
        key: str = None,
        updated_at: str = None,
        value: str = None,
    ):
        # 创建时间
        self.created_at = created_at
        # 配置项键名
        self.key = key
        # 更新时间
        self.updated_at = updated_at
        # 配置值
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at

        if self.key is not None:
            result['Key'] = self.key

        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

