# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_rdsai20250507 import models as main_models
from darabonba.model import DaraModel

class CreateContextDatabaseApiKeyResponseBody(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        key: main_models.CreateContextDatabaseApiKeyResponseBodyKey = None,
        request_id: str = None,
    ):
        self.api_key = api_key
        self.key = key
        self.request_id = request_id

    def validate(self):
        if self.key:
            self.key.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['ApiKey'] = self.api_key

        if self.key is not None:
            result['Key'] = self.key.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')

        if m.get('Key') is not None:
            temp_model = main_models.CreateContextDatabaseApiKeyResponseBodyKey()
            self.key = temp_model.from_map(m.get('Key'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateContextDatabaseApiKeyResponseBodyKey(DaraModel):
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
        self.created_at = created_at
        self.description = description
        self.expires_at = expires_at
        self.key_display_suffix = key_display_suffix
        self.key_id = key_id
        self.key_prefix = key_prefix
        self.last_used_at = last_used_at
        self.name = name
        self.revoked_at = revoked_at
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

