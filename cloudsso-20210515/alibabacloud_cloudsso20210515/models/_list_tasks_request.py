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
        # The ID of the access configuration. This parameter is used as a filter condition for the query.
        self.access_configuration_id = access_configuration_id
        # The ID of the directory.
        self.directory_id = directory_id
        # The filter condition.
        # 
        # Format: <Attribute> <Operator> <Value>. The format is not case-sensitive. <Attribute> only supports StartTime. <Operator> only supports ge (greater than or equal to). <Value> must be in the YYYY-MM-DDTHH:mm:ssZ format and can only be a time within the last 7 days.
        # 
        # Example: Filter = "StartTime ge 2021-03-15T01:12:23Z". This example queries the list of tasks starting from 2021-03-15T01:12:23Z.
        # 
        # > If you do not specify this parameter, the list of tasks created within the last 24 hours is returned by default.
        self.filter = filter
        # The maximum number of entries to return on each page.
        # 
        # Valid values: 1 to 20.
        # 
        # Default value: 10.
        self.max_results = max_results
        # The token used to return the next page of the query results. You do not need to specify NextToken when you call this operation for the first time.
        # 
        # When you call this operation for the first time, if the total number of returned entries exceeds the value of MaxResults, the returned data is truncated. Only the number of entries specified by MaxResults is returned, the IsTruncated response parameter is set to true, and a NextToken value is returned. You can use the returned NextToken value to call this operation again while keeping other request parameters unchanged to query the truncated data. You can repeat this process until IsTruncated is set to false, which indicates that all data is returned.
        self.next_token = next_token
        # The ID of the CloudSSO identity. This parameter is used as a filter condition for the query. Details:
        # 
        # - If PrincipalType is set to User, PrincipalId is the ID of the CloudSSO user.
        # - If PrincipalType is set to Group, PrincipalId is the ID of the CloudSSO group.
        # 
        # > PrincipalId and PrincipalType must be specified at the same time to serve as a valid filter condition.
        self.principal_id = principal_id
        # The type of the CloudSSO identity. This parameter is used as a filter condition for the query. Valid values:
        # 
        # - User: The CloudSSO user.
        # - Group: The CloudSSO group.
        # 
        # > PrincipalId and PrincipalType must be specified at the same time to serve as a valid filter condition.
        self.principal_type = principal_type
        # The status of the task. This parameter is used as a filter condition for the query. Valid values:
        # 
        # - InProgress: The task is running.
        # - Success: The task succeeded.
        # - Failed: The task failed.
        self.status = status
        # The ID of the task target. This parameter is used as a filter condition for the query.
        # 
        # > TargetId and TargetType must be specified at the same time to serve as a valid filter condition.
        self.target_id = target_id
        # The type of the task target. This parameter is used as a filter condition for the query. Valid values:
        # 
        # - RD-Account: The task target is an account in a resource directory.
        # 
        # > TargetId and TargetType must be specified at the same time to serve as a valid filter condition.
        self.target_type = target_type
        # The type of the node. This parameter is used as a filter condition for the query. Valid values:
        # 
        # - ProvisionAccessConfiguration: Access configuration deployment.
        # - DeprovisionAccessConfiguration: Removes access configuration provisioning.
        # - CreateAccessAssignment: Grants authorization to an account in a resource directory.
        # - DeleteAccessAssignment: Removes authorization from an account in a resource directory.
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

