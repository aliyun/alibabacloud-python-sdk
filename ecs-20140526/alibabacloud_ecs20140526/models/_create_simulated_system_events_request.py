# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateSimulatedSystemEventsRequest(DaraModel):
    def __init__(
        self,
        event_type: str = None,
        instance_id: List[str] = None,
        not_before: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The type of the system event. Valid values:
        # 
        # *   SystemMaintenance.Reboot: The instance is restarted due to system maintenance.
        # *   SystemFailure.Reboot: The instance is restarted due to a system error.
        # *   InstanceFailure.Reboot: The instance is restarted due to an instance error.
        # *   SystemMaintenance.Stop: The instance is stopped due to system maintenance.
        # *   SystemMaintenance.Redeploy: The instance is redeployed due to system maintenance.
        # *   SystemFailure.Redeploy: The instance is redeployed due to a system error.
        # *   SystemFailure.Stop: The instance is stopped due to a system error.
        # 
        # This parameter is required.
        self.event_type = event_type
        # The IDs of the instances. You can specify up to 100 instance IDs.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The scheduled start time of the event. Specify the time in the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # > For events that occur due to system errors or instance errors, the simulated events of such events enter the `Executing` state when the simulated events are created. The value of `NotBefore` is the time when the simulated events enter the `Executed` state.
        # 
        # This parameter is required.
        self.not_before = not_before
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_type is not None:
            result['EventType'] = self.event_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.not_before is not None:
            result['NotBefore'] = self.not_before

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NotBefore') is not None:
            self.not_before = m.get('NotBefore')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

