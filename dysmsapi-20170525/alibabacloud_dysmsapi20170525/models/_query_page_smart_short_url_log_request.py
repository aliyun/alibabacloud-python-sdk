# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryPageSmartShortUrlLogRequest(DaraModel):
    def __init__(
        self,
        create_date_end: int = None,
        create_date_start: int = None,
        owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        phone_number: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        short_url: str = None,
    ):
        # This parameter is required.
        self.create_date_end = create_date_end
        # This parameter is required.
        self.create_date_start = create_date_start
        self.owner_id = owner_id
        # This parameter is required.
        self.page_no = page_no
        # This parameter is required.
        self.page_size = page_size
        self.phone_number = phone_number
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.short_url = short_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_date_end is not None:
            result['CreateDateEnd'] = self.create_date_end

        if self.create_date_start is not None:
            result['CreateDateStart'] = self.create_date_start

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.short_url is not None:
            result['ShortUrl'] = self.short_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateDateEnd') is not None:
            self.create_date_end = m.get('CreateDateEnd')

        if m.get('CreateDateStart') is not None:
            self.create_date_start = m.get('CreateDateStart')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ShortUrl') is not None:
            self.short_url = m.get('ShortUrl')

        return self

