# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class CreateResourceInstancesRequest(DaraModel):
    def __init__(
        self,
        auto_renewal: bool = None,
        charge_type: str = None,
        ecs_instance_count: int = None,
        ecs_instance_type: str = None,
        labels: Dict[str, str] = None,
        system_disk_size: int = None,
        user_data: str = None,
        zone: str = None,
    ):
        # Specifies whether to enable auto-renewal. Valid values:
        # 
        # - false (default): Auto-renewal is disabled.
        # 
        # - true: Auto-renewal is enabled.
        self.auto_renewal = auto_renewal
        # The billing method. Valid values:
        # 
        # - PrePaid: subscription.
        # 
        # - PostPaid: pay-as-you-go.
        # 
        # This parameter is required.
        self.charge_type = charge_type
        # The number of new instances to create. The value must be between 1 and 100.
        # 
        # This parameter is required.
        self.ecs_instance_count = ecs_instance_count
        # The instance type. This corresponds to an ECS instance type.
        # 
        # This parameter is required.
        self.ecs_instance_type = ecs_instance_type
        # The user-defined tags.
        self.labels = labels
        # The size of the system disk, in GiB. The value must be between 200 and 2,000. If you do not configure this parameter, the default value is 200 GiB.
        self.system_disk_size = system_disk_size
        # The custom user data. This parameter is not currently used.
        self.user_data = user_data
        # The zone where the instance belongs.
        self.zone = zone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_renewal is not None:
            result['AutoRenewal'] = self.auto_renewal

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.ecs_instance_count is not None:
            result['EcsInstanceCount'] = self.ecs_instance_count

        if self.ecs_instance_type is not None:
            result['EcsInstanceType'] = self.ecs_instance_type

        if self.labels is not None:
            result['Labels'] = self.labels

        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size

        if self.user_data is not None:
            result['UserData'] = self.user_data

        if self.zone is not None:
            result['Zone'] = self.zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenewal') is not None:
            self.auto_renewal = m.get('AutoRenewal')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('EcsInstanceCount') is not None:
            self.ecs_instance_count = m.get('EcsInstanceCount')

        if m.get('EcsInstanceType') is not None:
            self.ecs_instance_type = m.get('EcsInstanceType')

        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        if m.get('Zone') is not None:
            self.zone = m.get('Zone')

        return self

