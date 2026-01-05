# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBNodesParametersRequest(DaraModel):
    def __init__(
        self,
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
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The ID of the node. You can specify multiple node IDs. Separate multiple node IDs with commas (,).
        # 
        # This parameter is required.
        self.dbnode_ids = dbnode_ids
        # Specifies whether to immediately run the task to modify parameters and restart the cluster. Valid values: false: runs the task on schedule. true: runs the task immediately. Default value: false.
        self.from_time_service = from_time_service
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the parameter template that is used for the cluster.
        self.parameter_group_id = parameter_group_id
        # The JSON string that specifies the parameter and its value.
        self.parameters = parameters
        # The latest start time to run the task. Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time must be in UTC.
        self.planned_end_time = planned_end_time
        # The earliest start time to run the task to upgrade the kernel version of the cluster. The task runs within a specified period of time. Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time must be in UTC.
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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        return self

