# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rdsai20250507 import models as main_models
from darabonba.model import DaraModel

class ListContextDatabaseMembersResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        members: List[main_models.ListContextDatabaseMembersResponseBodyMembers] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The maximum number of entries per page. This field is empty.
        self.max_results = max_results
        # The list of members.
        self.members = members
        # The pagination token for the next page. This field is empty.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.members:
            for v1 in self.members:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        result['Members'] = []
        if self.members is not None:
            for k1 in self.members:
                result['Members'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        self.members = []
        if m.get('Members') is not None:
            for k1 in m.get('Members'):
                temp_model = main_models.ListContextDatabaseMembersResponseBodyMembers()
                self.members.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListContextDatabaseMembersResponseBodyMembers(DaraModel):
    def __init__(
        self,
        created_at: str = None,
        keys: List[main_models.ListContextDatabaseMembersResponseBodyMembersKeys] = None,
        member_id: str = None,
        member_name: str = None,
        role: str = None,
        status: str = None,
    ):
        # The time when the member was created.
        self.created_at = created_at
        # The list of API keys.
        self.keys = keys
        # The member ID.
        self.member_id = member_id
        # The member name.
        self.member_name = member_name
        # The member role.
        self.role = role
        # The member status.
        self.status = status

    def validate(self):
        if self.keys:
            for v1 in self.keys:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at

        result['Keys'] = []
        if self.keys is not None:
            for k1 in self.keys:
                result['Keys'].append(k1.to_map() if k1 else None)

        if self.member_id is not None:
            result['MemberId'] = self.member_id

        if self.member_name is not None:
            result['MemberName'] = self.member_name

        if self.role is not None:
            result['Role'] = self.role

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')

        self.keys = []
        if m.get('Keys') is not None:
            for k1 in m.get('Keys'):
                temp_model = main_models.ListContextDatabaseMembersResponseBodyMembersKeys()
                self.keys.append(temp_model.from_map(k1))

        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')

        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class ListContextDatabaseMembersResponseBodyMembersKeys(DaraModel):
    def __init__(
        self,
        created_at: str = None,
        description: str = None,
        expires_at: str = None,
        key_display_suffix: str = None,
        key_id: int = None,
        key_prefix: str = None,
        last_used_at: str = None,
        name: str = None,
        revoked_at: str = None,
        status: str = None,
    ):
        # The time when the member was created.
        self.created_at = created_at
        # The API key description.
        self.description = description
        # This field is empty.
        self.expires_at = expires_at
        # The suffix of the API key.
        self.key_display_suffix = key_display_suffix
        # The key ID.
        self.key_id = key_id
        # The prefix of the API key.
        self.key_prefix = key_prefix
        # The time when the key was last used. This field is populated after the key has been authenticated and used. This field is empty for keys that have never been used.
        self.last_used_at = last_used_at
        # The API key name.
        self.name = name
        # This field is empty.
        self.revoked_at = revoked_at
        # The API key status.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at

        if self.description is not None:
            result['Description'] = self.description

        if self.expires_at is not None:
            result['ExpiresAt'] = self.expires_at

        if self.key_display_suffix is not None:
            result['KeyDisplaySuffix'] = self.key_display_suffix

        if self.key_id is not None:
            result['KeyId'] = self.key_id

        if self.key_prefix is not None:
            result['KeyPrefix'] = self.key_prefix

        if self.last_used_at is not None:
            result['LastUsedAt'] = self.last_used_at

        if self.name is not None:
            result['Name'] = self.name

        if self.revoked_at is not None:
            result['RevokedAt'] = self.revoked_at

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExpiresAt') is not None:
            self.expires_at = m.get('ExpiresAt')

        if m.get('KeyDisplaySuffix') is not None:
            self.key_display_suffix = m.get('KeyDisplaySuffix')

        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')

        if m.get('KeyPrefix') is not None:
            self.key_prefix = m.get('KeyPrefix')

        if m.get('LastUsedAt') is not None:
            self.last_used_at = m.get('LastUsedAt')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RevokedAt') is not None:
            self.revoked_at = m.get('RevokedAt')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

