# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudsso20210515 import models as main_models
from darabonba.model import DaraModel

class ListUsersResponseBody(DaraModel):
    def __init__(
        self,
        is_truncated: bool = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_counts: int = None,
        users: List[main_models.ListUsersResponseBodyUsers] = None,
    ):
        # Indicates whether the results are truncated. Valid values:
        # 
        # - true: The results are truncated.
        # - false: The results are not truncated.
        self.is_truncated = is_truncated
        # The maximum number of entries per page.
        self.max_results = max_results
        # The token for the next page of results. 
        # 
        # > This parameter is returned only when `IsTruncated` is `true`.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries that match the request parameters.
        self.total_counts = total_counts
        # The user list.
        self.users = users

    def validate(self):
        if self.users:
            for v1 in self.users:
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

        result['Users'] = []
        if self.users is not None:
            for k1 in self.users:
                result['Users'].append(k1.to_map() if k1 else None)

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

        self.users = []
        if m.get('Users') is not None:
            for k1 in m.get('Users'):
                temp_model = main_models.ListUsersResponseBodyUsers()
                self.users.append(temp_model.from_map(k1))

        return self

class ListUsersResponseBodyUsers(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        display_name: str = None,
        email: str = None,
        external_id: main_models.ListUsersResponseBodyUsersExternalId = None,
        first_name: str = None,
        last_name: str = None,
        provision_type: str = None,
        status: str = None,
        tags: List[main_models.ListUsersResponseBodyUsersTags] = None,
        update_time: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        # The time when the user was created (UTC).
        self.create_time = create_time
        # The description of the user.
        self.description = description
        # The display name of the user.
        self.display_name = display_name
        # The email address of the user.
        self.email = email
        # The identifier information of the user from the external identity provider.
        self.external_id = external_id
        # The first name of the user.
        self.first_name = first_name
        # The last name of the user.
        self.last_name = last_name
        # The type of the user. Valid values:
        # 
        # - Manual: The user is manually created.
        # - Synchronized: The user is synchronized from an external identity provider.
        self.provision_type = provision_type
        # The status of the user. Valid values:
        # 
        # - Enabled: The user is enabled.
        # - Disabled: The user is disabled.
        self.status = status
        # The tag list.
        self.tags = tags
        # The time when the user was last modified (UTC).
        self.update_time = update_time
        # The user ID.
        self.user_id = user_id
        # The username.
        self.user_name = user_name

    def validate(self):
        if self.external_id:
            self.external_id.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.email is not None:
            result['Email'] = self.email

        if self.external_id is not None:
            result['ExternalId'] = self.external_id.to_map()

        if self.first_name is not None:
            result['FirstName'] = self.first_name

        if self.last_name is not None:
            result['LastName'] = self.last_name

        if self.provision_type is not None:
            result['ProvisionType'] = self.provision_type

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('ExternalId') is not None:
            temp_model = main_models.ListUsersResponseBodyUsersExternalId()
            self.external_id = temp_model.from_map(m.get('ExternalId'))

        if m.get('FirstName') is not None:
            self.first_name = m.get('FirstName')

        if m.get('LastName') is not None:
            self.last_name = m.get('LastName')

        if m.get('ProvisionType') is not None:
            self.provision_type = m.get('ProvisionType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListUsersResponseBodyUsersTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

class ListUsersResponseBodyUsersTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListUsersResponseBodyUsersExternalId(DaraModel):
    def __init__(
        self,
        id: str = None,
        issuer: str = None,
    ):
        # The user identifier from the external identity provider.
        self.id = id
        # The external identity synchronization channel. Currently, only SCIM-based user synchronization is supported.
        self.issuer = issuer

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.issuer is not None:
            result['Issuer'] = self.issuer

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')

        return self

