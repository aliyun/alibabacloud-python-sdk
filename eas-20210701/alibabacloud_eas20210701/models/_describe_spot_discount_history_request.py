# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSpotDiscountHistoryRequest(DaraModel):
    def __init__(
        self,
        instance_type: str = None,
        is_protect: bool = None,
    ):
        # The type of the Elastic Algorithm Service (EAS) instance.
        # 
        # This parameter is required.
        self.instance_type = instance_type
        # Specifies whether the preemptible instance has a protection period. During the 1-hour protection period of the preemptible instance, the preemptible instance will not be released.
        self.is_protect = is_protect

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.is_protect is not None:
            result['IsProtect'] = self.is_protect

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('IsProtect') is not None:
            self.is_protect = m.get('IsProtect')

        return self

