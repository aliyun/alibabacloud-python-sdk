# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateSharedAccountPermissionRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        permission: str = None,
        region_id: str = None,
        service_id: str = None,
        type: str = None,
        user_ali_uid: int = None,
    ):
        # Client token, used to ensure the idempotence of requests. Generate a unique value for this parameter from your client to ensure it is unique across different requests. ClientToken supports only ASCII characters.
        self.client_token = client_token
        # Permission type. Possible values:
        # - Deployable: Can be deployed.
        # - Accessible: Can be accessed.
        # - AccessibleIncludeBeta: Can access all versions, including Beta versions.
        # - DeployableIncludeBeta: Can deploy all versions, including Beta versions.
        # - Authorized: Authorized (for reselling scenarios)
        # - Unauthorized: Unauthorized (for reselling scenarios)
        # 
        # This parameter is required.
        self.permission = permission
        # Region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Service ID.
        # 
        # This parameter is required.
        self.service_id = service_id
        # Service sharing type, with a default value of SharedAccount. Available options:
        # 
        # - SharedAccount: Regular sharing type.
        # 
        # - Reseller: Reselling sharing type.
        self.type = type
        # Whitelist account for service sharing.
        # 
        # This parameter is required.
        self.user_ali_uid = user_ali_uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.permission is not None:
            result['Permission'] = self.permission

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.type is not None:
            result['Type'] = self.type

        if self.user_ali_uid is not None:
            result['UserAliUid'] = self.user_ali_uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Permission') is not None:
            self.permission = m.get('Permission')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UserAliUid') is not None:
            self.user_ali_uid = m.get('UserAliUid')

        return self

