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
        # The ID of the cluster.
        # 
        # > You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/173433.html) operation to query information about all clusters that are deployed in a specified region, such as the cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # Specifies whether to change the primary zone immediately. Valid values:
        # 
        # *   false (default): changes the primary zone as scheduled.
        # *   true: changes the primary zone immediately.
        self.from_time_service = from_time_service
        # Specifies whether to switch back to the original primary zone.
        # 
        # *   true: switches back to the original primary zone.
        # *   false: does not switch back to the original primary zone.
        self.is_switch_over_for_disaster = is_switch_over_for_disaster
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The latest start time to switch the primary zone within the scheduled time period. Specify the time in the ISO 8601 standard in the `YYYY-MM-DDThh:mm:ssZ` format. The time must be in UTC.
        # 
        # > *   The latest start time must be at least 30 minutes later than the earliest start time.
        # >*   If you specify the `PlannedStartTime` parameter but do not specify the PlannedEndTime parameter, the latest start time of the task is set to a value that is calculated by `the value of the PlannedEndTime parameter + 30 minutes` by default. For example, if you set the `PlannedStartTime` parameter to `2021-01-14T09:00:00Z` and you do not specify the PlannedEndTime parameter, the latest start time of the task is set to `2021-01-14T09:30:00Z`.
        self.planned_end_time = planned_end_time
        # The start time to change the primary zone within the scheduled time period. Specify the time in the ISO 8601 standard in the `YYYY-MM-DDThh:mm:ssZ` format. The time must be in UTC.
        # 
        # > *   The start time of the task can be a point in time within the next 24 hours. For example, if the current time is `2021-01-14T09:00:00Z`, you can specify a point in time from `2021-01-14T09:00:00Z` to `2021-01-15T09:00:00Z`.
        # >*   If you leave this parameter empty, the primary zone is immediately changed.
        self.planned_start_time = planned_start_time
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The virtual private cloud (VPC) ID of the destination primary zone.
        self.vpcid = vpcid
        # The ID of the vSwitch in the destination primary zone.
        # 
        # > *   For a PolarDB for PostgreSQL (Compatible with Oracle) cluster or a PolarDB for PostgreSQL cluster, this parameter is required.
        # >*   For a PolarDB for MySQL cluster, the default vSwitch is used if no vSwitches are created in the destination zone. If a vSwitch is in the destination zone, this parameter is required.
        self.v_switch_id = v_switch_id
        # The ID of the destination primary zone.
        # 
        # >  You can call the DescribeRegions operation to query available zones.[](~~98041~~)
        # 
        # This parameter is required.
        self.zone_id = zone_id
        # The zone type. Valid values:
        # 
        # *   **Primary**: primary zone
        # *   **Standby**: secondary zone
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

