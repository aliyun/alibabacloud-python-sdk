# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConvertPostPayOrderRequest(DaraModel):
    def __init__(
        self,
        duration: int = None,
        instance_id: str = None,
        paid_type: int = None,
        region_id: str = None,
    ):
        # The subscription duration. Unit: months. Valid values:
        # 
        # *   **1~12**
        # *   **24**
        # *   **36**
        self.duration = duration
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.paid_type = paid_type
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['Duration'] = self.duration

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.paid_type is not None:
            result['PaidType'] = self.paid_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PaidType') is not None:
            self.paid_type = m.get('PaidType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

