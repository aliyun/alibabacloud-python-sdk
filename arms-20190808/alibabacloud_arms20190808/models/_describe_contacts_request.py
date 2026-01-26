# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeContactsRequest(DaraModel):
    def __init__(
        self,
        contact_ids: str = None,
        contact_name: str = None,
        email: str = None,
        page: int = None,
        phone: str = None,
        region_id: str = None,
        size: int = None,
        verbose: str = None,
    ):
        # The ID of the alert contact that you want to query. Separate multiple contact IDs with spaces.
        self.contact_ids = contact_ids
        # The name of the alert contact.
        self.contact_name = contact_name
        # The email address of the alert contact.
        self.email = email
        # The number of the page to return.
        # 
        # This parameter is required.
        self.page = page
        # The mobile number of the alert contact.
        self.phone = phone
        # The region ID.
        self.region_id = region_id
        # The number of alert contacts to return on each page.
        # 
        # This parameter is required.
        self.size = size
        # Specifies whether to return redundant information.
        self.verbose = verbose

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

        if self.email is not None:
            result['Email'] = self.email

        if self.page is not None:
            result['Page'] = self.page

        if self.phone is not None:
            result['Phone'] = self.phone

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.size is not None:
            result['Size'] = self.size

        if self.verbose is not None:
            result['Verbose'] = self.verbose

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactIds') is not None:
            self.contact_ids = m.get('ContactIds')

        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('Phone') is not None:
            self.phone = m.get('Phone')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Verbose') is not None:
            self.verbose = m.get('Verbose')

        return self

