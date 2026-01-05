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
        # Specifies whether to immediately start scheduling. Valid values:
        # 
        # *   0: No. This is the default value.
        # *   1: Yes.
        # 
        # > 
        # 
        # *   If you set this parameter to 0, you must specify the SwitchTime parameter.
        # 
        # *   If you set this parameter to 1, the SwitchTime parameter does not take effect. In this case, the start time of the event is set to the current time, and the system determines the switching time based on the start time. Scheduling is started immediately, which is a prerequisite for the switchover. Then, the switchover is performed. You can call the DescribeActiveOperationTasks operation and check the return value of the PrepareInterval parameter for the preparation time.
        self.immediate_start = immediate_start
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/98041.html) operation to query the region information about all clusters within a specified account.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token
        # The scheduled switching time that you want to specify. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # > 
        # 
        # *   The time that is specified by this parameter cannot be later than the latest execution time.
        # 
        # *   You can call the DescribeActiveOperationTasks operation and check the return value of the Deadline parameter for the latest execution time.
        self.switch_time = switch_time
        # The task IDs.
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

