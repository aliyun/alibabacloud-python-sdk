# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SearchAlertContactRequest(DaraModel):
    def __init__(
        self,
        contact_ids: str = None,
        contact_name: str = None,
        current_page: str = None,
        email: str = None,
        page_size: str = None,
        phone: str = None,
        region_id: str = None,
    ):
        # The ID of the alert contact.
        self.contact_ids = contact_ids
        # The name of the alert contact.
        self.contact_name = contact_name
        # The number of the page to return.
        self.current_page = current_page
        # The email address of the alert contact.
        self.email = email
        # The number of entries to return on each page.
        self.page_size = page_size
        # The mobile number of the alert contact.
        self.phone = phone
        # The ID of the region. Set the value to `cn-hangzhou`.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_ids is not None:
            result['ContactIds'] = self.contact_ids

        if self.contact_name is not None:
            result['ContactName'] = self.contact_name

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.email is not None:
            result['Email'] = self.email

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.phone is not None:
            result['Phone'] = self.phone

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactIds') is not None:
            self.contact_ids = m.get('ContactIds')

        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Phone') is not None:
            self.phone = m.get('Phone')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

