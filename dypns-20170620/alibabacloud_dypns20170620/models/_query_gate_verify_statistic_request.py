# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryGateVerifyStatisticRequest(DaraModel):
    def __init__(
        self,
        authentication_type: int = None,
        end_date: str = None,
        os_type: str = None,
        owner_id: int = None,
        prod_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scene_code: str = None,
        start_date: str = None,
    ):
        # This parameter is required.
        self.authentication_type = authentication_type
        # This parameter is required.
        self.end_date = end_date
        self.os_type = os_type
        self.owner_id = owner_id
        self.prod_code = prod_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.scene_code = scene_code
        # This parameter is required.
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authentication_type is not None:
            result['AuthenticationType'] = self.authentication_type

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.os_type is not None:
            result['OsType'] = self.os_type

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthenticationType') is not None:
            self.authentication_type = m.get('AuthenticationType')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        return self

