# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetInstanceControlConfigurationRequest(DaraModel):
    def __init__(
        self,
        element_name: str = None,
        instance_id: str = None,
    ):
        self.element_name = element_name
        # IDaaS EIAM实例的ID。
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.element_name is not None:
            result['ElementName'] = self.element_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ElementName') is not None:
            self.element_name = m.get('ElementName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

