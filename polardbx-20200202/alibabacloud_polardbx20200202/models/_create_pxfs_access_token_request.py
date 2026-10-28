# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePxfsAccessTokenRequest(DaraModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        identity_name: str = None,
        label: str = None,
        region_id: str = None,
        tenant_id: str = None,
        ttl_seconds: int = None,
    ):
        # The PolarDB-X instance ID.
        # 
        # This parameter is required.
        self.dbinstance_name = dbinstance_name
        # The name of the identity.
        # 
        # This parameter is required.
        self.identity_name = identity_name
        # The label of the token.
        self.label = label
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The tenant ID.
        # 
        # This parameter is required.
        self.tenant_id = tenant_id
        # The validity period of the token.
        self.ttl_seconds = ttl_seconds

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.identity_name is not None:
            result['IdentityName'] = self.identity_name

        if self.label is not None:
            result['Label'] = self.label

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.ttl_seconds is not None:
            result['TtlSeconds'] = self.ttl_seconds

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('IdentityName') is not None:
            self.identity_name = m.get('IdentityName')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('TtlSeconds') is not None:
            self.ttl_seconds = m.get('TtlSeconds')

        return self

