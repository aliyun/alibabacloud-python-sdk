# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBClusterParametersRequest(DaraModel):
    def __init__(
        self,
        clear_binlog: bool = None,
        dbcluster_id: str = None,
        from_time_service: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        parameter_group_id: str = None,
        parameters: str = None,
        planned_end_time: str = None,
        planned_start_time: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # Specifies whether to clear binlogs. This parameter takes effect only when binlog is disabled.
        self.clear_binlog = clear_binlog
        # The cluster ID.
        # > You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/98094.html) operation to query information about all clusters in the specified region, including cluster IDs.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # Specifies whether to immediately or schedule the parameter modification and cluster restart. Valid values:  
        # 
        # - false (default): Scheduled execution.
        #  
        # - true: Immediate execution.
        self.from_time_service = from_time_service
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The parameter template ID.
        # 
        # 
        # > * You can call the [DescribeParameterGroups](https://help.aliyun.com/document_detail/207178.html) operation to query the parameter template ID.
        # > * You must specify either this parameter or the `Parameters` parameter.
        # > * Only PolarDB for MySQL supports this parameter.
        self.parameter_group_id = parameter_group_id
        # A JSON string that consists of parameters and their values. Parameter values are of the STRING type. Example: `{"wait_timeout":"86","innodb_old_blocks_time":"10"}`.
        # 
        # > * You can call the [DescribeDBClusterParameters](https://help.aliyun.com/document_detail/98122.html) operation to query the parameters of a PolarDB cluster.
        # > * If the cluster runs PolarDB for PostgreSQL or PolarDB for PostgreSQL (Compatible with Oracle), this parameter is required.
        # > * If the cluster runs PolarDB for MySQL, you must specify either this parameter or the `ParameterGroupId` parameter.
        self.parameters = parameters
        # The latest time to start running the scheduled task. The time is in the `YYYY-MM-DDThh:mm:ssZ` format (UTC).
        # > * The latest time must be at least 30 minutes later than the start time.
        # > * If you specify `PlannedStartTime` but do not specify this parameter, the latest time defaults to `start time + 30 minutes`. For example, if `PlannedStartTime` is set to `2021-01-14T09:00:00Z` and this parameter is left empty, the task starts no later than `2021-01-14T09:30:00Z`.
        self.planned_end_time = planned_end_time
        # The earliest time to start running the scheduled task within the specified time range. The time is in the `YYYY-MM-DDThh:mm:ssZ` format (UTC).
        # > * The start time must be within the next 24 hours. For example, if the current time is `2021-01-14T09:00:00Z`, the start time can range from `2021-01-14T09:00:00Z` to `2021-01-15T09:00:00Z`.
        # > * If this parameter is left empty, the task is immediately executed.
        self.planned_start_time = planned_start_time
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.clear_binlog is not None:
            result['ClearBinlog'] = self.clear_binlog

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.from_time_service is not None:
            result['FromTimeService'] = self.from_time_service

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.parameter_group_id is not None:
            result['ParameterGroupId'] = self.parameter_group_id

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.planned_end_time is not None:
            result['PlannedEndTime'] = self.planned_end_time

        if self.planned_start_time is not None:
            result['PlannedStartTime'] = self.planned_start_time

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClearBinlog') is not None:
            self.clear_binlog = m.get('ClearBinlog')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('FromTimeService') is not None:
            self.from_time_service = m.get('FromTimeService')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ParameterGroupId') is not None:
            self.parameter_group_id = m.get('ParameterGroupId')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('PlannedEndTime') is not None:
            self.planned_end_time = m.get('PlannedEndTime')

        if m.get('PlannedStartTime') is not None:
            self.planned_start_time = m.get('PlannedStartTime')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

