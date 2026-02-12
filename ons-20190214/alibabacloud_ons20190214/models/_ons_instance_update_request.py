# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OnsInstanceUpdateRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_name: str = None,
        remark: str = None,
    ):
        # The ID of the instance whose name or description you want to update.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The new name of the instance. The name must meet the following rules:
        # 
        # *   The name of the instance must be unique in the region where the instance is deployed.
        # *   The name must be 3 to 64 characters in length and can contain letters, digits, hyphens (-), underscores (_), and Chinese characters.
        # *   If you do not configure this parameter, the instance name remains unchanged.
        self.instance_name = instance_name
        # The updated description of the instance. If you do not configure this parameter, the instance description remains unchanged.
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.remark is not None:
            result['Remark'] = self.remark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        return self

