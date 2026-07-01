# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class VerifyAgenticDBTenantApiKeyResponseBody(DaraModel):
    def __init__(
        self,
        api_key_id: str = None,
        dbcluster_id: str = None,
        expire_time: str = None,
        reason: str = None,
        region_id: str = None,
        request_id: str = None,
        tenant_id: str = None,
        tenant_name: str = None,
        valid: bool = None,
    ):
        self.api_key_id = api_key_id
        self.dbcluster_id = dbcluster_id
        self.expire_time = expire_time
        self.reason = reason
        self.region_id = region_id
        self.request_id = request_id
        self.tenant_id = tenant_id
        self.tenant_name = tenant_name
        self.valid = valid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key_id is not None:
            result['ApiKeyId'] = self.api_key_id

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name

        if self.valid is not None:
            result['Valid'] = self.valid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKeyId') is not None:
            self.api_key_id = m.get('ApiKeyId')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')

        if m.get('Valid') is not None:
            self.valid = m.get('Valid')

        return self

