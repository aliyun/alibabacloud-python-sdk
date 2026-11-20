# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTotalPublicUrlRequest(DaraModel):
    def __init__(
        self,
        call_id: str = None,
        call_time: str = None,
        check_subs: bool = None,
        owner_id: int = None,
        partner_key: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the call record.
        # 
        # Log on to the [Phone Number Protection console](https://dypls.console.aliyun.com/dypls.htm#/account) and view **Call Record ID** on the **Call Record Query** page.
        # 
        # This parameter is required.
        self.call_id = call_id
        # The call initiation time in the call record.
        # 
        # Log on to the [Phone Number Protection console](https://dypls.console.aliyun.com/dypls.htm#/account). View **Call Initiated At** on the **Call Record Query** page, or view the call_time field in the Call Detail Record (CDR) receipt.
        # 
        # This parameter is required.
        self.call_time = call_time
        # Specifies whether the verification on the binding ID is required.
        # 
        # This parameter is required.
        self.check_subs = check_subs
        self.owner_id = owner_id
        # The key of the phone number pool. Log on to the [Phone Number Protection console](https://dypls.console.aliyun.com/dypls.htm#/account) and view the key of the phone number pool on the **Number Pool Management** page.
        # 
        # This parameter is required.
        self.partner_key = partner_key
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_id is not None:
            result['CallId'] = self.call_id

        if self.call_time is not None:
            result['CallTime'] = self.call_time

        if self.check_subs is not None:
            result['CheckSubs'] = self.check_subs

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.partner_key is not None:
            result['PartnerKey'] = self.partner_key

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')

        if m.get('CallTime') is not None:
            self.call_time = m.get('CallTime')

        if m.get('CheckSubs') is not None:
            self.check_subs = m.get('CheckSubs')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PartnerKey') is not None:
            self.partner_key = m.get('PartnerKey')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

