# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListScriptsShrinkRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        publish_only: bool = None,
        script_ids_shrink: str = None,
    ):
        # 实例ID
        self.instance_id = instance_id
        # 搜索关键词
        self.name = name
        # 页码，从1开始
        self.page_number = page_number
        # 每页记录数
        self.page_size = page_size
        # 是否仅返回已发布的场景
        self.publish_only = publish_only
        # 场景ID列表
        self.script_ids_shrink = script_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.publish_only is not None:
            result['PublishOnly'] = self.publish_only

        if self.script_ids_shrink is not None:
            result['ScriptIds'] = self.script_ids_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PublishOnly') is not None:
            self.publish_only = m.get('PublishOnly')

        if m.get('ScriptIds') is not None:
            self.script_ids_shrink = m.get('ScriptIds')

        return self

