# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryCallInTransferRecordRequest(DaraModel):
    def __init__(
        self,
        call_in_caller: str = None,
        owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        phone_number: str = None,
        query_date: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The calling number of the inbound call.
        self.call_in_caller = call_in_caller
        self.owner_id = owner_id
        # The page number. Default value: **1**.
        # 
        # This parameter is required.
        self.page_no = page_no
        # The number of entries per page. Valid values: 1 to 10.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The phone number to which a call is transferred.
        # 
        # This parameter is required.
        self.phone_number = phone_number
        # The time at which call transfer records are queried, in the YYYY-MM-DD hh:mm:ss format.
        # 
        # > The query result is all the call transfer records of the specified day.
        # 
        # This parameter is required.
        self.query_date = query_date
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_in_caller is not None:
            result['CallInCaller'] = self.call_in_caller

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number

        if self.query_date is not None:
            result['QueryDate'] = self.query_date

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallInCaller') is not None:
            self.call_in_caller = m.get('CallInCaller')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        if m.get('QueryDate') is not None:
            self.query_date = m.get('QueryDate')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

