# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTasksRequest(DaraModel):
    def __init__(
        self,
        access_configuration_id: str = None,
        directory_id: str = None,
        filter: str = None,
        max_results: int = None,
        next_token: str = None,
        principal_id: str = None,
        principal_type: str = None,
        status: str = None,
        target_id: str = None,
        target_type: str = None,
        task_type: str = None,
    ):
        # The ID of the access configuration. The ID can be used to filter access permissions.
        self.access_configuration_id = access_configuration_id
        # The ID of the directory.
        self.directory_id = directory_id
        # The filter condition.
        # 
        # The condition is not case-sensitive. The condition must be in the StartTime ge YYYY-MM-DDTHH:mm:SSZ format. You must set YYYY-MM-DDTHH:mm:SSZ to a value that is no more than 7 days from the current time. ge indicates Greater Than or Equals.
        # 
        # For example, if you set the Filter parameter to StartTime ge 2021-03-15T01:12:23Z, the operation queries the tasks from 2021-03-15T01:12:23 GMT.
        # 
        # > If you do not specify this parameter, the operation queries the tasks within the previous 24 hours by default.
        self.filter = filter
        # The maximum number of entries per page.
        # 
        # Valid values: 1 to 20.
        # 
        # Default value: 10.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. If this is your first time to call this operation, you do not need to specify the `NextToken` parameter.
        # 
        # When you call this operation for the first time, if the total number of entries to return exceeds the value of `MaxResults`, the entries are truncated. Only the entries that match the value of `MaxResults` are returned, and the excess entries are not returned. In this case, the value of the response parameter `IsTruncated` is `true`, and `NextToken` is returned. In the next call, you can use the value of `NextToken` and maintain the settings of the other request parameters to query the excess entries. You can repeat the call until the value of `IsTruncated` becomes `false`. This way, all entries are returned.
        self.next_token = next_token
        # The ID of the CloudSSO identity. The ID can be used to filter access permissions.
        # 
        # - If you set `PrincipalType` to `User`, set `PrincipalId` to the ID of the CloudSSO user.
        # 
        # - If you set `PrincipalType` to `Group`, set `PrincipalId` to the ID of the CloudSSO group.
        # 
        # > You can use the type to filter access permissions only if you specify both `PrincipalId` and `PrincipalType`.
        self.principal_id = principal_id
        # The type of the CloudSSO identity. The type can be used to filter access permissions. Valid values:
        # 
        # - User
        # 
        # - Group
        # 
        # > You can use the type to filter access permissions only if you specify both `PrincipalId` and `PrincipalType`.
        self.principal_type = principal_type
        # The ID of the task. The ID can be used to filter tasks. Valid values:
        # 
        # - InProgress: The task is running.
        # 
        # - Success: The task is successful.
        # 
        # - Failed: The task failed.
        self.status = status
        # The ID of the task object. The ID can be used to filter access permissions.
        # 
        # > You can use the type to filter access permissions only if you specify both `TargetId` and `TargetType`.
        self.target_id = target_id
        # The type of the task object. The type can be used to filter access permissions.
        # 
        # Set the value to RD-Account, which specifies the accounts in the resource directory.
        # 
        # > You can use the type to filter access permissions only if you specify both `TargetId` and `TargetType`.
        self.target_type = target_type
        # The type of the task. The type can be used to filter tasks. Valid values:
        # 
        # - ProvisionAccessConfiguration: An access configuration is provisioned.
        # 
        # - DeprovisionAccessConfiguration: An access configuration is de-provisioned.
        # 
        # - CreateAccessAssignment: Access permissions on an account in the resource directory are assigned.
        # 
        # - DeleteAccessAssignment: Access permissions on an account in the resource directory are removed.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_configuration_id is not None:
            result['AccessConfigurationId'] = self.access_configuration_id

        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.filter is not None:
            result['Filter'] = self.filter

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.principal_id is not None:
            result['PrincipalId'] = self.principal_id

        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type

        if self.status is not None:
            result['Status'] = self.status

        if self.target_id is not None:
            result['TargetId'] = self.target_id

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessConfigurationId') is not None:
            self.access_configuration_id = m.get('AccessConfigurationId')

        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('Filter') is not None:
            self.filter = m.get('Filter')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PrincipalId') is not None:
            self.principal_id = m.get('PrincipalId')

        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

