# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListUserProvisioningsRequest(DaraModel):
    def __init__(
        self,
        directory_id: str = None,
        max_results: int = None,
        next_token: str = None,
        principal_id: str = None,
        principal_type: str = None,
        target_id: str = None,
        target_type: str = None,
    ):
        # The ID of the resource directory.
        self.directory_id = directory_id
        # The maximum number of entries per page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.max_results = max_results
        # The token that is used to initiate the next request. If this is your first time to call this operation, you do not need to specify the `NextToken` parameter.
        # 
        # When you call this operation for the first time, if the total number of entries to return is larger than the value of `MaxResults`, the entries are truncated. The system returns entries based on the value of `MaxResults`, and does not return the excess entries. In this case, the value of the response parameter `IsTruncated` is `true`, and `NextToken` is returned. In the next call, you can use the value of `NextToken` and maintain the settings of the other request parameters to query the excess entries. You can repeat the call until the value of `IsTruncated` becomes `false`. This way, all entries are returned.
        self.next_token = next_token
        # The identity ID of the RAM user provisioning. Valid values:
        # 
        # - If `Group` is returned for the `PrincipalType` parameter, the value of this parameter is the ID of a CloudSSO user group (g-\\*\\*\\*\\*\\*\\*\\*\\*).
        # 
        # - If `User` is returned for the `PrincipalType` parameter, the value of this parameter is the ID of a CloudSSO user (u-\\*\\*\\*\\*\\*\\*\\*\\*).
        self.principal_id = principal_id
        # The identity type of the RAM user provisioning. Valid values:
        # 
        # - User: The identity of the RAM user provisioning is a CloudSSO user.
        # 
        # - Group: The identity of the RAM user provisioning is a CloudSSO user group.
        self.principal_type = principal_type
        # The ID of the object for which you create the RAM user provisioning. The value is fixed as the ID of the member in the resource directory.
        self.target_id = target_id
        # The object for which you create the RAM user provisioning. The value is fixed as `RD-Account`.
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

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
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PrincipalId') is not None:
            self.principal_id = m.get('PrincipalId')

        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')

        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

