# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyPortAutoCcStatusRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        mode: str = None,
        switch: str = None,
    ):
        # The ID of the instance.
        # 
        # > You can call the [DescribeInstanceIds](https://help.aliyun.com/document_detail/157459.html) operation to query the IDs of all instances.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The mode of the Intelligent Protection policy. Valid values:
        # 
        # *   **normal**
        # *   **loose**
        # *   **strict**
        # 
        # This parameter is required.
        self.mode = mode
        # Specifies the status of the Intelligent Protection policy. Valid values:
        # 
        # *   **on**: enables the policy.
        # *   **off**: disables the policy.
        # 
        # This parameter is required.
        self.switch = switch

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.switch is not None:
            result['Switch'] = self.switch

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('Switch') is not None:
            self.switch = m.get('Switch')

        return self

