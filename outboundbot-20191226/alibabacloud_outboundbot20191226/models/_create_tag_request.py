# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTagRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        script_id: str = None,
        tag_group: str = None,
        tag_name: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.script_id = script_id
        # This parameter is required.
        self.tag_group = tag_group
        # This parameter is required.
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        if self.tag_group is not None:
            result['TagGroup'] = self.tag_group

        if self.tag_name is not None:
            result['TagName'] = self.tag_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        if m.get('TagGroup') is not None:
            self.tag_group = m.get('TagGroup')

        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')

        return self

