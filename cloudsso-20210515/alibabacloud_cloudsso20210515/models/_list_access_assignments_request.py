# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAccessAssignmentsRequest(DaraModel):
    def __init__(
        self,
        access_configuration_id: str = None,
        directory_id: str = None,
        max_results: int = None,
        next_token: str = None,
        origin_target_id: str = None,
        principal_id: str = None,
        principal_type: str = None,
        target_id: str = None,
        target_type: str = None,
    ):
        # The ID of the access configuration. This parameter is used as a filter condition for the query.
        self.access_configuration_id = access_configuration_id
        # The ID of the directory.
        self.directory_id = directory_id
        # The maximum number of entries to return on each page.
        # 
        # Valid values: 1 to 20.
        # 
        # Default value: 10.
        self.max_results = max_results
        # The token for the next page of query results. You do not need to specify `NextToken` when you call this operation for the first time.
        # 
        # When you call this operation for the first time, if the total number of returned entries exceeds the value of `MaxResults`, the returned entries are truncated. Only the number of entries specified by `MaxResults` is returned, the `IsTruncated` parameter is set to `true`, and a `NextToken` value is returned. You can use the returned `NextToken` value to call this operation again to query the truncated entries while keeping other request parameters unchanged. You can repeat this process until `IsTruncated` is set to `false`, which indicates that all entries are returned.
        self.next_token = next_token
        # The ID of the Alibaba Cloud account to which the authorization target belongs.
        self.origin_target_id = origin_target_id
        # The ID of the CloudSSO identity, which is used as a filter condition for the query. Details:
        # 
        # - If `PrincipalType` is set to User, `PrincipalId` is the ID of the CloudSSO user.
        # - If `PrincipalType` is set to Group, `PrincipalId` is the ID of the CloudSSO group.
        # 
        # > You must specify both `PrincipalId` and `PrincipalType` for the filter condition to take effect.
        self.principal_id = principal_id
        # The type of the CloudSSO identity, which is used as a filter condition for the query. Valid values:
        # 
        # - User: user.
        # - Group: group.
        # 
        # > You must specify both `PrincipalId` and `PrincipalType` for the filter condition to take effect.
        self.principal_type = principal_type
        # The ID of the task target, which is used as a filter condition for the query.
        # 
        # > You must specify both `TargetId` and `TargetType` for the filter condition to take effect.
        self.target_id = target_id
        # The type of the task target, which is used as a filter condition for the query.
        # 
        # Valid values:
        # - RD-Account: The task target is an account in a resource directory.
        # 
        # > You must specify both `TargetId` and `TargetType` for the filter condition to take effect.
        self.target_type = target_type

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

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.origin_target_id is not None:
            result['OriginTargetId'] = self.origin_target_id

        if self.principal_id is not None:
            result['PrincipalId'] = self.principal_id

        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type

        if self.target_id is not None:
            result['TargetId'] = self.target_id

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessConfigurationId') is not None:
            self.access_configuration_id = m.get('AccessConfigurationId')

        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OriginTargetId') is not None:
            self.origin_target_id = m.get('OriginTargetId')

        if m.get('PrincipalId') is not None:
            self.principal_id = m.get('PrincipalId')

        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')

        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

