# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ManageLoginRequest(DaraModel):
    def __init__(
        self,
        action_name: str = None,
        key_group: str = None,
        key_name: str = None,
        rendering_instance_id: str = None,
    ):
        # Name of the management action. Valid values:
        # 
        # 1. open — Activate the public key. This is the default value.
        # 
        # 2. close — Deactivate the public key.
        self.action_name = action_name
        # Name of the public key group. If you do not specify KeyName, all public keys in this group are applied.
        self.key_group = key_group
        # Name of the public key. You must specify either KeyName or KeyGroup.
        self.key_name = key_name
        # ID of the Cloud Application Service instance.
        # 
        # This parameter is required.
        self.rendering_instance_id = rendering_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_name is not None:
            result['ActionName'] = self.action_name

        if self.key_group is not None:
            result['KeyGroup'] = self.key_group

        if self.key_name is not None:
            result['KeyName'] = self.key_name

        if self.rendering_instance_id is not None:
            result['RenderingInstanceId'] = self.rendering_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionName') is not None:
            self.action_name = m.get('ActionName')

        if m.get('KeyGroup') is not None:
            self.key_group = m.get('KeyGroup')

        if m.get('KeyName') is not None:
            self.key_name = m.get('KeyName')

        if m.get('RenderingInstanceId') is not None:
            self.rendering_instance_id = m.get('RenderingInstanceId')

        return self

