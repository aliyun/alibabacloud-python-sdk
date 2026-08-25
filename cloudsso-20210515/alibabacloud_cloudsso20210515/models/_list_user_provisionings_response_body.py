# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudsso20210515 import models as main_models
from darabonba.model import DaraModel

class ListUserProvisioningsResponseBody(DaraModel):
    def __init__(
        self,
        is_truncated: bool = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_counts: int = None,
        user_provisionings: List[main_models.ListUserProvisioningsResponseBodyUserProvisionings] = None,
    ):
        # Indicates whether the queried entries are truncated. Valid values:
        # 
        # - true
        # 
        # - false
        self.is_truncated = is_truncated
        # The maximum number of entries per page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.max_results = max_results
        # The token that is used to initiate the next request.
        # 
        # > This parameter is returned only when the `IsTruncated` parameter is set to `true`.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_counts = total_counts
        # The RAM user provisionings.
        self.user_provisionings = user_provisionings

    def validate(self):
        if self.user_provisionings:
            for v1 in self.user_provisionings:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_counts is not None:
            result['TotalCounts'] = self.total_counts

        result['UserProvisionings'] = []
        if self.user_provisionings is not None:
            for k1 in self.user_provisionings:
                result['UserProvisionings'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCounts') is not None:
            self.total_counts = m.get('TotalCounts')

        self.user_provisionings = []
        if m.get('UserProvisionings') is not None:
            for k1 in m.get('UserProvisionings'):
                temp_model = main_models.ListUserProvisioningsResponseBodyUserProvisionings()
                self.user_provisionings.append(temp_model.from_map(k1))

        return self

class ListUserProvisioningsResponseBodyUserProvisionings(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        deletion_strategy: str = None,
        description: str = None,
        directory_id: str = None,
        duplication_strategy: str = None,
        owner_pk: str = None,
        principal_id: str = None,
        principal_name: str = None,
        principal_type: str = None,
        status: str = None,
        target_id: str = None,
        target_name: str = None,
        target_path: str = None,
        target_type: str = None,
        update_time: str = None,
        user_provisioning_id: str = None,
    ):
        # The creation time.
        self.create_time = create_time
        # The deletion policy. The policy is used to manage synchronized users when you delete the RAM user provisioning. Valid values:
        # 
        # - Delete: When you delete the RAM user provisioning, the system deletes the synchronized users.
        # 
        # - Keep: When you delete the RAM user provisioning, the system retains the synchronized users.
        self.deletion_strategy = deletion_strategy
        # The description.
        self.description = description
        # The ID of the resource directory.
        self.directory_id = directory_id
        # The conflict handling policy. The policy is used when a RAM user has the same username as the CloudSSO user who is synchronized to RAM. Valid values:
        # 
        # - KeepBoth: When a CloudSSO user is synchronized to RAM, if a RAM user who has the same username as the CloudSSO user exists, the system creates a RAM user whose username is the username of the CloudSSO user plus the suffix `_sso`.
        # 
        # - TakeOver: When a CloudSSO user is synchronized to RAM, if a RAM user who has the same username as the CloudSSO user exists, the system replaces the RAM user with the CloudSSO user.
        self.duplication_strategy = duplication_strategy
        # The ID of the Alibaba Cloud account to which the resource directory belongs.
        self.owner_pk = owner_pk
        # The identity ID of the RAM user provisioning. Valid values:
        # 
        # - If `Group` is returned for the `PrincipalType` parameter, the value of this parameter is the ID of a CloudSSO user group (g-\\*\\*\\*\\*\\*\\*\\*\\*).
        # 
        # - If `User` is returned for the `PrincipalType` parameter, the value of this parameter is the ID of a CloudSSO user (u-\\*\\*\\*\\*\\*\\*\\*\\*).
        self.principal_id = principal_id
        # The identity name of the RAM user provisioning. Valid values:
        # 
        # - If `Group` is returned for the `PrincipalType` parameter, the value of this parameter is the name of a CloudSSO user group.
        # 
        # - If `User` is returned for the `PrincipalType` parameter, the value of this parameter is the name of a CloudSSO user.
        self.principal_name = principal_name
        # The identity type of the RAM user provisioning. Valid values:
        # 
        # - User: The identity of the RAM user provisioning is a CloudSSO user.
        # 
        # - Group: The identity of the RAM user provisioning is a CloudSSO user group.
        self.principal_type = principal_type
        # The status of the RAM user provisioning. Valid values:
        # 
        # - Enabled
        # 
        # - Disabled
        self.status = status
        # The ID of the object for which you create the RAM user provisioning. The value is fixed as the ID of the member in the resource directory.
        self.target_id = target_id
        # The object for which you create the RAM user provisioning. The value is fixed as `RD-Account`.
        self.target_name = target_name
        # The path of the resource directory in which you create the RAM user provisioning for the object.
        self.target_path = target_path
        # The object for which you create the RAM user provisioning. The value is fixed as `RD-Account`.
        self.target_type = target_type
        # The modification time.
        self.update_time = update_time
        # The ID of the RAM user provisioning.
        self.user_provisioning_id = user_provisioning_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.deletion_strategy is not None:
            result['DeletionStrategy'] = self.deletion_strategy

        if self.description is not None:
            result['Description'] = self.description

        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.duplication_strategy is not None:
            result['DuplicationStrategy'] = self.duplication_strategy

        if self.owner_pk is not None:
            result['OwnerPk'] = self.owner_pk

        if self.principal_id is not None:
            result['PrincipalId'] = self.principal_id

        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name

        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type

        if self.status is not None:
            result['Status'] = self.status

        if self.target_id is not None:
            result['TargetId'] = self.target_id

        if self.target_name is not None:
            result['TargetName'] = self.target_name

        if self.target_path is not None:
            result['TargetPath'] = self.target_path

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.user_provisioning_id is not None:
            result['UserProvisioningId'] = self.user_provisioning_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DeletionStrategy') is not None:
            self.deletion_strategy = m.get('DeletionStrategy')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('DuplicationStrategy') is not None:
            self.duplication_strategy = m.get('DuplicationStrategy')

        if m.get('OwnerPk') is not None:
            self.owner_pk = m.get('OwnerPk')

        if m.get('PrincipalId') is not None:
            self.principal_id = m.get('PrincipalId')

        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')

        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')

        if m.get('TargetName') is not None:
            self.target_name = m.get('TargetName')

        if m.get('TargetPath') is not None:
            self.target_path = m.get('TargetPath')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UserProvisioningId') is not None:
            self.user_provisioning_id = m.get('UserProvisioningId')

        return self

