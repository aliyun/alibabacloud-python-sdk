# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SetAdbSecureRequest(DaraModel):
    def __init__(
        self,
        instance_ids: List[str] = None,
        status: int = None,
    ):
        # The IDs of the cloud phone instances. You can specify a maximum of 50 cloud phone instances.
        self.instance_ids = instance_ids
        # The status of the ADB authentication feature.
        # 
        # Valid values:
        # 
        # *   0: The ADB authentication feature is disabled.
        # *   1: The ADB authentication feature is enabled.
        # 
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

