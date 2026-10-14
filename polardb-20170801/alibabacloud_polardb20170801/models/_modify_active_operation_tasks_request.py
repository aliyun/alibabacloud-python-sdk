# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyActiveOperationTasksRequest(DaraModel):
    def __init__(
        self,
        immediate_start: int = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
        switch_time: str = None,
        task_ids: str = None,
    ):
        # Specifies whether to immediately start execution scheduling.
        # 
        # - 0: No (default).
        # - 1: Yes.
        # 
        # >- If the value is 0, the SwitchTime parameter is required.
        # >- If the value is 1, the SwitchTime parameter does not take effect. The event start time is set to the current time, and the switchover time is automatically calculated based on the new start time. The event immediately enters execution scheduling (not an immediate switchover) and begins pre-switchover preparations. The switchover is performed after the preparations are complete. You can call the DescribeActiveOperationTasks operation and obtain the preparation time from the PrepareInterval response parameter.
        self.immediate_start = immediate_start
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID.
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/98041.html) operation to query the region information of all clusters under the target account.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token
        # The planned switchover time to set. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format (UTC).
        # 
        # > 
        # > - The time cannot be later than the deadline.
        # > - You can call the DescribeActiveOperationTasks operation and obtain the deadline from the Deadline response parameter.
        self.switch_time = switch_time
        # The list of task IDs.
        # 
        # This parameter is required.
        self.task_ids = task_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.immediate_start is not None:
            result['ImmediateStart'] = self.immediate_start

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

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.switch_time is not None:
            result['SwitchTime'] = self.switch_time

        if self.task_ids is not None:
            result['TaskIds'] = self.task_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImmediateStart') is not None:
            self.immediate_start = m.get('ImmediateStart')

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

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('SwitchTime') is not None:
            self.switch_time = m.get('SwitchTime')

        if m.get('TaskIds') is not None:
            self.task_ids = m.get('TaskIds')

        return self

