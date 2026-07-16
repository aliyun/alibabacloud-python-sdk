# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Schema(DaraModel):
    def __init__(
        self,
        comment: str = None,
        create_time: int = None,
        id: str = None,
        modify_time: int = None,
        name: str = None,
        parent_meta_entity_id: str = None,
        type: str = None,
    ):
        # 注释。
        self.comment = comment
        # 创建时间（毫秒级时间戳）。
        self.create_time = create_time
        # ID，可参考[元数据实体相关概念说明](https://help.aliyun.com/document_detail/2880092.html)。
        # 
        # 格式为`${EntityType}:${实例ID或转义后的URL}:${数据目录名称}:${数据库名称}:${模式名称}`，对于不存在的层级置空。
        # 
        # > 对于MaxCompute类型，此处的实例ID即为主账号ID，数据库名称即为MaxCompute项目名称。
        self.id = id
        # 更新时间（毫秒级时间戳）。
        self.modify_time = modify_time
        # 名称。
        self.name = name
        # 父层级元数据实体ID，父层级实体类型取值参考ListCrawlerTypes接口。
        # 
        # 格式为`${EntityType}:${实例ID或转义后的URL}:${数据目录名称}:${数据库名称}`，对于不存在的层级置空。
        # 
        # > 对于MaxCompute类型，此处的实例ID即为主账号ID，数据库名称即为MaxCompute项目名称。
        self.parent_meta_entity_id = parent_meta_entity_id
        # 类型。
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

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.id is not None:
            result['Id'] = self.id

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.name is not None:
            result['Name'] = self.name

        if self.parent_meta_entity_id is not None:
            result['ParentMetaEntityId'] = self.parent_meta_entity_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ParentMetaEntityId') is not None:
            self.parent_meta_entity_id = m.get('ParentMetaEntityId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

