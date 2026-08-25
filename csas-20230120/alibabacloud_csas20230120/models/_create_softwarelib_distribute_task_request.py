# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateSoftwarelibDistributeTaskRequest(DaraModel):
    def __init__(
        self,
        dev_tags: List[str] = None,
        device_group_ids: List[str] = None,
        execute_mode: str = None,
        execute_parameters: str = None,
        execute_period: str = None,
        expire_mode: str = None,
        gmt_expired: str = None,
        match_mode: str = None,
        name: str = None,
        retry_times: str = None,
        run_as_account: str = None,
        software_id: str = None,
        software_name: str = None,
        support_os: str = None,
        task_type: str = None,
        timeout: str = None,
        user_group_ids: List[str] = None,
        version_id: str = None,
    ):
        # The collection of terminal device IDs. Duplicate values are not allowed. Each ID must not exceed 1000 characters in length. This parameter is required when MatchMode is set to DevTagNormal. This parameter is not allowed when MatchMode is set to other values. Otherwise, the request is rejected.
        self.dev_tags = dev_tags
        # The collection of device group IDs. Duplicate values are not allowed. This parameter is required when MatchMode is set to DeviceGroupNormal. This parameter is not allowed when MatchMode is set to other values. Otherwise, the request is rejected. You can call [ListDeviceGroups](~~ListDeviceGroups~~) to obtain the values.
        self.device_group_ids = device_group_ids
        # The execution mode. Valid values:
        # - **Once**: immediate execution.
        # - **Schedule**: scheduled execution.
        self.execute_mode = execute_mode
        # The scheduling execution parameters in JSON format.
        self.execute_parameters = execute_parameters
        # The task execution cycle in JSON format. The validType field specifies the cycle type. Valid values:
        # - **Once**: one-time execution.
        # - **Interval**: execution at intervals.
        # - **Weekly**: weekly execution.
        self.execute_period = execute_period
        # The expiration type. Valid values:
        # - **Expire**: expires at the time specified by GmtExpired.
        # - **Never**: never expires.
        self.expire_mode = expire_mode
        # The task expiration time as a millisecond-level UNIX timestamp. This parameter takes effect only when ExpireMode is set to Expire.
        self.gmt_expired = gmt_expired
        # The policy matching target type. Valid values:
        # - **UserGroupAll**: all users.
        # - **UserGroupNormal**: specified user groups.
        # - **DevTagNormal**: specified devices.
        # - **DeviceGroupNormal**: specified device groups.
        # - **DevTagAll**: all devices.
        # - **None**: not configured.
        self.match_mode = match_mode
        # The task name. The name must be 1 to 64 characters in length.
        # 
        # This parameter is required.
        self.name = name
        # The number of retries after a task failure.
        self.retry_times = retry_times
        # The administrator account name used to run the task on Windows. The name must not exceed 128 characters in length.
        self.run_as_account = run_as_account
        # The software ID in the software library. You can call [ListSoftwarelibSoftware](~~ListSoftwarelibSoftware~~) to obtain the value.
        self.software_id = software_id
        # The software name. The name must not exceed 128 characters in length.
        self.software_name = software_name
        # The operating system to which the task applies. Only a single value is supported. Valid values:
        # - **Windows**: Windows.
        # - **Mac(Apple)**: macOS with Apple silicon.
        # - **Mac(Intel)**: macOS with Intel processors.
        self.support_os = support_os
        # The task type. Valid values:
        # - **server**: a task delivered from the console.
        # - **client**: a task initiated from the client.
        self.task_type = task_type
        # The task execution timeout period. Unit: seconds. For example, a value of 3600 indicates 1 hour.
        self.timeout = timeout
        # The collection of user group IDs. Duplicate values are not allowed. This parameter is required and must contain at least one value when MatchMode is set to UserGroupNormal. This parameter is not allowed when MatchMode is set to other values. Otherwise, the request is rejected. You can call [ListUserGroups](~~ListUserGroups~~) to obtain the values.
        self.user_group_ids = user_group_ids
        # The ID of the software version to distribute. You can call [ListSoftwarelibVersion](~~ListSoftwarelibVersion~~) to obtain the value.
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dev_tags is not None:
            result['DevTags'] = self.dev_tags

        if self.device_group_ids is not None:
            result['DeviceGroupIds'] = self.device_group_ids

        if self.execute_mode is not None:
            result['ExecuteMode'] = self.execute_mode

        if self.execute_parameters is not None:
            result['ExecuteParameters'] = self.execute_parameters

        if self.execute_period is not None:
            result['ExecutePeriod'] = self.execute_period

        if self.expire_mode is not None:
            result['ExpireMode'] = self.expire_mode

        if self.gmt_expired is not None:
            result['GmtExpired'] = self.gmt_expired

        if self.match_mode is not None:
            result['MatchMode'] = self.match_mode

        if self.name is not None:
            result['Name'] = self.name

        if self.retry_times is not None:
            result['RetryTimes'] = self.retry_times

        if self.run_as_account is not None:
            result['RunAsAccount'] = self.run_as_account

        if self.software_id is not None:
            result['SoftwareId'] = self.software_id

        if self.software_name is not None:
            result['SoftwareName'] = self.software_name

        if self.support_os is not None:
            result['SupportOs'] = self.support_os

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DevTags') is not None:
            self.dev_tags = m.get('DevTags')

        if m.get('DeviceGroupIds') is not None:
            self.device_group_ids = m.get('DeviceGroupIds')

        if m.get('ExecuteMode') is not None:
            self.execute_mode = m.get('ExecuteMode')

        if m.get('ExecuteParameters') is not None:
            self.execute_parameters = m.get('ExecuteParameters')

        if m.get('ExecutePeriod') is not None:
            self.execute_period = m.get('ExecutePeriod')

        if m.get('ExpireMode') is not None:
            self.expire_mode = m.get('ExpireMode')

        if m.get('GmtExpired') is not None:
            self.gmt_expired = m.get('GmtExpired')

        if m.get('MatchMode') is not None:
            self.match_mode = m.get('MatchMode')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RetryTimes') is not None:
            self.retry_times = m.get('RetryTimes')

        if m.get('RunAsAccount') is not None:
            self.run_as_account = m.get('RunAsAccount')

        if m.get('SoftwareId') is not None:
            self.software_id = m.get('SoftwareId')

        if m.get('SoftwareName') is not None:
            self.software_name = m.get('SoftwareName')

        if m.get('SupportOs') is not None:
            self.support_os = m.get('SupportOs')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        return self

