# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBClusterPrimaryZoneRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        from_time_service: bool = None,
        is_switch_over_for_disaster: str = None,
        owner_account: str = None,
        owner_id: int = None,
        planned_end_time: str = None,
        planned_start_time: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        vpcid: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
        zone_type: str = None,
    ):
        # The cluster ID.
        # 
        # > Call the [DescribeDBClusters](https://help.aliyun.com/document_detail/173433.html) operation to query the details of all clusters in a destination region, including their cluster IDs.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # Specifies whether to perform the zone change immediately or at a scheduled time. Valid values:
        # 
        # - false (default): The zone change is performed at the scheduled time.
        # 
        # - true: The zone change is performed immediately.
        self.from_time_service = from_time_service
        # Specifies whether to fail back to the original zone. Valid values:
        # 
        # - true: Fails back to the original zone.
        # 
        # - false: Does not fail back to the original zone.
        self.is_switch_over_for_disaster = is_switch_over_for_disaster
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The latest time to start the scheduled task. Specify the time in the `YYYY-MM-DDThh:mm:ssZ` format. The time must be in UTC.
        # 
        # > - The latest start time must be at least 30 minutes later than the earliest start time.
        # >
        # > - If you specify `PlannedStartTime` but not this parameter, the latest start time of the task is the value of `PlannedStartTime` plus 30 minutes by default. For example, if you set `PlannedStartTime` to `2021-01-14T09:00:00Z` and leave this parameter empty, the task starts no later than `2021-01-14T09:30:00Z`.
        self.planned_end_time = planned_end_time
        # The earliest time to start the scheduled task to change the zone. Specify the time in the `YYYY-MM-DDThh:mm:ssZ` format. The time must be in UTC.
        # 
        # > - The start time must be a point in time within the next 24 hours. For example, if the current time is `2021-01-14T09:00:00Z`, you can set the start time to a value from `2021-01-14T09:00:00Z` to `2021-01-15T09:00:00Z`.
        # >
        # > - If you do not specify this parameter, the zone change task is performed immediately.
        self.planned_start_time = planned_start_time
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the virtual private cloud (VPC).
        self.vpcid = vpcid
        # The ID of the vSwitch in the destination zone.
        # 
        # > - This parameter is required for PolarDB for Oracle and PolarDB for PostgreSQL clusters.
        # >
        # > - For PolarDB for MySQL clusters, this parameter is required if a vSwitch is created in the destination zone. If no vSwitch is created, the default vSwitch is used and this parameter is optional.
        self.v_switch_id = v_switch_id
        # The ID of the new zone.
        # 
        # > Call the [DescribeRegions](https://help.aliyun.com/document_detail/98041.html) operation to query available zones.
        # 
        # This parameter is required.
        self.zone_id = zone_id
        # The type of the zone. Valid values:
        # 
        # - **Primary**: The primary zone.
        # 
        # - **Standby**: The secondary zone.
        self.zone_type = zone_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.from_time_service is not None:
            result['FromTimeService'] = self.from_time_service

        if self.is_switch_over_for_disaster is not None:
            result['IsSwitchOverForDisaster'] = self.is_switch_over_for_disaster

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.planned_end_time is not None:
            result['PlannedEndTime'] = self.planned_end_time

        if self.planned_start_time is not None:
            result['PlannedStartTime'] = self.planned_start_time

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        if self.zone_type is not None:
            result['ZoneType'] = self.zone_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('FromTimeService') is not None:
            self.from_time_service = m.get('FromTimeService')

        if m.get('IsSwitchOverForDisaster') is not None:
            self.is_switch_over_for_disaster = m.get('IsSwitchOverForDisaster')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PlannedEndTime') is not None:
            self.planned_end_time = m.get('PlannedEndTime')

        if m.get('PlannedStartTime') is not None:
            self.planned_start_time = m.get('PlannedStartTime')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        if m.get('ZoneType') is not None:
            self.zone_type = m.get('ZoneType')

        return self

