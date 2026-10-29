# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyRenderingInstanceAttributeRequest(DaraModel):
    def __init__(
        self,
        instance_name: str = None,
        password: str = None,
        rendering_instance_id: str = None,
    ):
        # The name of the instance.
        self.instance_name = instance_name
        # The device password.
        self.password = password
        # The cloud application service instance ID.
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
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.password is not None:
            result['Password'] = self.password

        if self.rendering_instance_id is not None:
            result['RenderingInstanceId'] = self.rendering_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('RenderingInstanceId') is not None:
            self.rendering_instance_id = m.get('RenderingInstanceId')

        return self

