# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateMediaLiveInputShrinkRequest(DaraModel):
    def __init__(
        self,
        input_settings_shrink: str = None,
        name: str = None,
        security_group_ids_shrink: str = None,
        type: str = None,
    ):
        # The input settings. An input can have up to two sources: primary and backup sources.
        # 
        # This parameter is required.
        self.input_settings_shrink = input_settings_shrink
        # The name of the input. Letters, digits, hyphens (-), and underscores (_) are supported. It can be up to 64 characters in length.
        # 
        # This parameter is required.
        self.name = name
        # The IDs of the security groups to be associated with the input. This parameter is required for PUSH inputs.
        self.security_group_ids_shrink = security_group_ids_shrink
        # The input type. Valid values: RTMP_PUSH, RTMP_PULL, SRT_PUSH, SRT_PULL, and MEDIA_CONNECT.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_settings_shrink is not None:
            result['InputSettings'] = self.input_settings_shrink

        if self.name is not None:
            result['Name'] = self.name

        if self.security_group_ids_shrink is not None:
            result['SecurityGroupIds'] = self.security_group_ids_shrink

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputSettings') is not None:
            self.input_settings_shrink = m.get('InputSettings')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids_shrink = m.get('SecurityGroupIds')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

