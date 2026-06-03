# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConfigVerifySceneAppInfoRequest(DaraModel):
    def __init__(
        self,
        cm: bool = None,
        ct: bool = None,
        cu: bool = None,
        email: str = None,
        ip_whitelist: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scene_code: str = None,
    ):
        self.cm = cm
        self.ct = ct
        self.cu = cu
        # This parameter is required.
        self.email = email
        self.ip_whitelist = ip_whitelist
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # This parameter is required.
        self.scene_code = scene_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cm is not None:
            result['CM'] = self.cm

        if self.ct is not None:
            result['CT'] = self.ct

        if self.cu is not None:
            result['CU'] = self.cu

        if self.email is not None:
            result['Email'] = self.email

        if self.ip_whitelist is not None:
            result['IpWhitelist'] = self.ip_whitelist

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CM') is not None:
            self.cm = m.get('CM')

        if m.get('CT') is not None:
            self.ct = m.get('CT')

        if m.get('CU') is not None:
            self.cu = m.get('CU')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('IpWhitelist') is not None:
            self.ip_whitelist = m.get('IpWhitelist')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')

        return self

