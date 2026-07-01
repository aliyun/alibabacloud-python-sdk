# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAgenticDBTenantApiKeyResponseBody(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        api_key_id: str = None,
        create_time: str = None,
        expire_time: str = None,
        request_id: str = None,
        tenant_id: str = None,
        tenant_name: str = None,
    ):
        self.api_key = api_key
        self.api_key_id = api_key_id
        self.create_time = create_time
        self.expire_time = expire_time
        self.request_id = request_id
        self.tenant_id = tenant_id
        self.tenant_name = tenant_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['ApiKey'] = self.api_key

        if self.api_key_id is not None:
            result['ApiKeyId'] = self.api_key_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')

        if m.get('ApiKeyId') is not None:
            self.api_key_id = m.get('ApiKeyId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')

        return self

