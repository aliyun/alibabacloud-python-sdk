# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OnsInstanceCreateRequest(DaraModel):
    def __init__(
        self,
        instance_name: str = None,
        remark: str = None,
    ):
        # The name of the instance. The name must meet the following rules:
        # 
        # *   The name of the instance must be unique in the region where the instance is deployed.
        # *   The name must be 3 to 64 characters in length and can contain letters, digits, hyphens (-), and underscores (_).
        # 
        # This parameter is required.
        self.instance_name = instance_name
        # The description of the instance.
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.remark is not None:
            result['Remark'] = self.remark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        return self

