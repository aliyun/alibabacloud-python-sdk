# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Namespace(DaraModel):
    def __init__(
        self,
        catalog: str = None,
        comment: str = None,
        name: str = None,
        properties: str = None,
    ):
        # 命名空间所属的数据目录名称
        # 
        # This parameter is required.
        self.catalog = catalog
        # 命名空间的备注描述信息
        self.comment = comment
        # 命名空间的唯一标识名称
        self.name = name
        # 命名空间的扩展属性
        self.properties = properties

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog is not None:
            result['Catalog'] = self.catalog

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.name is not None:
            result['Name'] = self.name

        if self.properties is not None:
            result['properties'] = self.properties

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Catalog') is not None:
            self.catalog = m.get('Catalog')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('properties') is not None:
            self.properties = m.get('properties')

        return self

