# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateSystemConfigsShrinkRequest(DaraModel):
    def __init__(
        self,
        configs_shrink: str = None,
        object_id: str = None,
        object_type: str = None,
    ):
        # 配置列表
        self.configs_shrink = configs_shrink
        # 对象ID
        self.object_id = object_id
        # 外呼开发时补充参数限制
        self.object_type = object_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.configs_shrink is not None:
            result['Configs'] = self.configs_shrink

        if self.object_id is not None:
            result['ObjectId'] = self.object_id

        if self.object_type is not None:
            result['ObjectType'] = self.object_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Configs') is not None:
            self.configs_shrink = m.get('Configs')

        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')

        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')

        return self

