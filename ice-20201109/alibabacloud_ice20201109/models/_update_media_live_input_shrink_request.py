# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateMediaLiveInputShrinkRequest(DaraModel):
    def __init__(
        self,
        input_id: str = None,
        input_settings_shrink: str = None,
        name: str = None,
        security_group_ids_shrink: str = None,
    ):
        # The ID of the input.
        # 
        # This parameter is required.
        self.input_id = input_id
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

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_id is not None:
            result['InputId'] = self.input_id

        if self.input_settings_shrink is not None:
            result['InputSettings'] = self.input_settings_shrink

        if self.name is not None:
            result['Name'] = self.name

        if self.security_group_ids_shrink is not None:
            result['SecurityGroupIds'] = self.security_group_ids_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputId') is not None:
            self.input_id = m.get('InputId')

        if m.get('InputSettings') is not None:
            self.input_settings_shrink = m.get('InputSettings')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids_shrink = m.get('SecurityGroupIds')

        return self

