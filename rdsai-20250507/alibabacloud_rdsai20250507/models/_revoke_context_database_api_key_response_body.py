# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RevokeContextDatabaseApiKeyResponseBody(DaraModel):
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
        request_id: str = None,
        revoked_at: str = None,
        status: str = None,
    ):
        # The time when the API key was created.
        self.created_at = created_at
        # The description of the API key.
        self.description = description
        # A reserved field. This field is currently empty.
        self.expires_at = expires_at
        # The suffix of the API key.
        self.key_display_suffix = key_display_suffix
        # The key ID.
        self.key_id = key_id
        # The prefix of the API key.
        self.key_prefix = key_prefix
        # The time when the API key was last used.
        self.last_used_at = last_used_at
        # The name of the API key.
        self.name = name
        # The request ID.
        self.request_id = request_id
        # The time when the API key was revoked.
        self.revoked_at = revoked_at
        # The status of the API key. After revocation, the value is revoked.
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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RevokedAt') is not None:
            self.revoked_at = m.get('RevokedAt')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

