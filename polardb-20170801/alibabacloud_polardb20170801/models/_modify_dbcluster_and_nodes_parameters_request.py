# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBClusterAndNodesParametersRequest(DaraModel):
    def __init__(
        self,
        clear_binlog: bool = None,
        dbcluster_id: str = None,
        dbnode_ids: str = None,
        from_time_service: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        parameter_group_id: str = None,
        parameters: str = None,
        planned_end_time: str = None,
        planned_start_time: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        standby_cluster_id_list_need_to_sync: str = None,
    ):
        # Specifies whether to clear binlog. This parameter is valid only when binlog is disabled.
        self.clear_binlog = clear_binlog
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The IDs of the nodes. By setting this parameter, you can modify the parameters of the cluster and specified nodes. Separate multiple node IDs with commas (,).
        # 
        # > If this parameter is not specified, only the cluster parameters are modified.
        self.dbnode_ids = dbnode_ids
        # Specifies whether to immediately or scheduledly modify parameters and restart the cluster. Valid values:
        # 
        # - **false** (default): scheduled execution
        # 
        # - **true**: immediate execution
        self.from_time_service = from_time_service
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the parameter template.
        self.parameter_group_id = parameter_group_id
        # The JSON string that consists of parameters and their values.
        self.parameters = parameters
        # The latest time to start the scheduled task. Specify the time in the `YYYY-MM-DDThh:mm:ssZ` format. The time must be in UTC.
        # 
        # > - The latest start time must be 30 minutes or more later than the earliest start time.
        # >
        # > - If you specify `PlannedStartTime` but not this parameter, the latest start time of the task is `the earliest start time + 30 minutes` by default. For example, if you set `PlannedStartTime` to `2021-01-14T09:00:00Z` and leave this parameter empty, the task will start no later than `2021-01-14T09:30:00Z`.
        self.planned_end_time = planned_end_time
        # The earliest time to start the scheduled task. Specify the time in the `YYYY-MM-DDThh:mm:ssZ` format. The time must be in UTC.
        # 
        # > - The start time can be any time within the next 24 hours. For example, if the current time is `2021-01-14T09:00:00Z`, you can specify a time that ranges from `2021-01-14T09:00:00Z` to `2021-01-15T09:00:00Z`.
        # >
        # > - If you leave this parameter empty, the task is immediately executed.
        self.planned_start_time = planned_start_time
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The list of GDN standby clusters to which you want to synchronize the parameter settings.
        self.standby_cluster_id_list_need_to_sync = standby_cluster_id_list_need_to_sync

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

        if self.dbnode_ids is not None:
            result['DBNodeIds'] = self.dbnode_ids

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

        if self.standby_cluster_id_list_need_to_sync is not None:
            result['StandbyClusterIdListNeedToSync'] = self.standby_cluster_id_list_need_to_sync

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClearBinlog') is not None:
            self.clear_binlog = m.get('ClearBinlog')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DBNodeIds') is not None:
            self.dbnode_ids = m.get('DBNodeIds')

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

        if m.get('StandbyClusterIdListNeedToSync') is not None:
            self.standby_cluster_id_list_need_to_sync = m.get('StandbyClusterIdListNeedToSync')

        return self

