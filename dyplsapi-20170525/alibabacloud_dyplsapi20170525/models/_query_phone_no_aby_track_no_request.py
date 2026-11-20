# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryPhoneNoAByTrackNoRequest(DaraModel):
    def __init__(
        self,
        cabinet_no: str = None,
        owner_id: int = None,
        phone_no_x: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        track_no: str = None,
    ):
        # The cabinet number.
        self.cabinet_no = cabinet_no
        self.owner_id = owner_id
        # Phone number X returned by the API operation for creating a binding.
        self.phone_no_x = phone_no_x
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tracking number.
        # 
        # This parameter is required.
        self.track_no = track_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cabinet_no is not None:
            result['CabinetNo'] = self.cabinet_no

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.phone_no_x is not None:
            result['PhoneNoX'] = self.phone_no_x

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.track_no is not None:
            result['trackNo'] = self.track_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CabinetNo') is not None:
            self.cabinet_no = m.get('CabinetNo')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PhoneNoX') is not None:
            self.phone_no_x = m.get('PhoneNoX')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('trackNo') is not None:
            self.track_no = m.get('trackNo')

        return self

