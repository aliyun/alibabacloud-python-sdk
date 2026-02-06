# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class WhatsappCallShrinkRequest(DaraModel):
    def __init__(
        self,
        business_number: str = None,
        call_action: str = None,
        call_id: str = None,
        cust_space_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        session_shrink: str = None,
        user_number: str = None,
    ):
        # This parameter is required.
        self.business_number = business_number
        # This parameter is required.
        self.call_action = call_action
        self.call_id = call_id
        # This parameter is required.
        self.cust_space_id = cust_space_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.session_shrink = session_shrink
        self.user_number = user_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_number is not None:
            result['BusinessNumber'] = self.business_number

        if self.call_action is not None:
            result['CallAction'] = self.call_action

        if self.call_id is not None:
            result['CallId'] = self.call_id

        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.session_shrink is not None:
            result['Session'] = self.session_shrink

        if self.user_number is not None:
            result['UserNumber'] = self.user_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessNumber') is not None:
            self.business_number = m.get('BusinessNumber')

        if m.get('CallAction') is not None:
            self.call_action = m.get('CallAction')

        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')

        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Session') is not None:
            self.session_shrink = m.get('Session')

        if m.get('UserNumber') is not None:
            self.user_number = m.get('UserNumber')

        return self

