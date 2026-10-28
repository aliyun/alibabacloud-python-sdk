# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePxfsTenantRequest(DaraModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        quota_bytes: int = None,
        quota_files: int = None,
        rate_limit_rps: int = None,
        rate_limit_wbps: int = None,
        region_id: str = None,
        tenant_id: str = None,
        tenant_name: str = None,
    ):
        # The PolarDB-X instance ID.
        # 
        # This parameter is required.
        self.dbinstance_name = dbinstance_name
        # The capacity quota.
        # 
        # This parameter is required.
        self.quota_bytes = quota_bytes
        # The file count quota.
        # 
        # This parameter is required.
        self.quota_files = quota_files
        # The request rate limit.
        self.rate_limit_rps = rate_limit_rps
        # The write bandwidth limit.
        self.rate_limit_wbps = rate_limit_wbps
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the tenant.
        # 
        # This parameter is required.
        self.tenant_id = tenant_id
        # The name of the tenant.
        # 
        # This parameter is required.
        self.tenant_name = tenant_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.quota_bytes is not None:
            result['QuotaBytes'] = self.quota_bytes

        if self.quota_files is not None:
            result['QuotaFiles'] = self.quota_files

        if self.rate_limit_rps is not None:
            result['RateLimitRps'] = self.rate_limit_rps

        if self.rate_limit_wbps is not None:
            result['RateLimitWbps'] = self.rate_limit_wbps

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('QuotaBytes') is not None:
            self.quota_bytes = m.get('QuotaBytes')

        if m.get('QuotaFiles') is not None:
            self.quota_files = m.get('QuotaFiles')

        if m.get('RateLimitRps') is not None:
            self.rate_limit_rps = m.get('RateLimitRps')

        if m.get('RateLimitWbps') is not None:
            self.rate_limit_wbps = m.get('RateLimitWbps')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')

        return self

