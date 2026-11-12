# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RestartDBNodeRequest(DaraModel):
    def __init__(
        self,
        dbnode_id: str = None,
        from_time_service: str = None,
        owner_account: str = None,
        owner_id: int = None,
        planned_end_time: str = None,
        planned_start_time: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the cluster node.
        # > You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/185342.html) operation to view the details of all clusters under your account, including the node ID.
        # 
        # > Nodes in Serverless (AgileServerless) clusters are not supported. Operation description: This operation does not support nodes in Serverless (AgileServerless) clusters. You can check the ServerlessType field in the DescribeDBClusters response to determine the cluster type. For Serverless clusters, use the alternative management operations.
        # 
        # This parameter is required.
        self.dbnode_id = dbnode_id
        # Specifies whether to execute the node restart task immediately or at a scheduled time. Valid values:
        # 
        # - **false** (default): Executes the task at a scheduled time.
        # 
        # - **true**: Executes the task immediately.
        self.from_time_service = from_time_service
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The latest time to start the scheduled task. The time must be in the `YYYY-MM-DDThh:mm:ssZ` format (UTC).
        # > * The end time must be at least 30 minutes later than the start time.
        # > * If `PlannedStartTime` is specified but this parameter is not, the latest time to start the task defaults to the start time plus 30 minutes. For example, if `PlannedStartTime` is set to `2021-01-14T09:00:00Z` and this parameter is left empty, the task will start no later than `2021-01-14T09:30:00Z`.
        self.planned_end_time = planned_end_time
        # The earliest time to start the scheduled node restart task. The time must be in the `YYYY-MM-DDThh:mm:ssZ` format (UTC).
        # > * The start time must be within the next 72 hours. For example, if the current time is `2021-01-14T09:00:00Z`, the allowed start time ranges from `2021-01-14T09:00:00Z` to `2021-01-17T09:00:00Z`.
        # > * If this parameter is left empty, the node restart task is executed immediately by default.
        self.planned_start_time = planned_start_time
        # The region ID.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/98041.html) operation to view the available regions.
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
        if self.dbnode_id is not None:
            result['DBNodeId'] = self.dbnode_id

        if self.from_time_service is not None:
            result['FromTimeService'] = self.from_time_service

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.planned_end_time is not None:
            result['PlannedEndTime'] = self.planned_end_time

        if self.planned_start_time is not None:
            result['PlannedStartTime'] = self.planned_start_time

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBNodeId') is not None:
            self.dbnode_id = m.get('DBNodeId')

        if m.get('FromTimeService') is not None:
            self.from_time_service = m.get('FromTimeService')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PlannedEndTime') is not None:
            self.planned_end_time = m.get('PlannedEndTime')

        if m.get('PlannedStartTime') is not None:
            self.planned_start_time = m.get('PlannedStartTime')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

