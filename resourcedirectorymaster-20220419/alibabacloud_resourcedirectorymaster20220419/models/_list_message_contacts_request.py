# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListMessageContactsRequest(DaraModel):
    def __init__(
        self,
        contact_id: str = None,
        member: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The ID of the contact.
        self.contact_id = contact_id
        # The ID of the object to which the contact is bound. Valid values:
        # 
        # *   ID of the resource directory
        # *   ID of the folder
        # *   ID of the member
        self.member = member
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id

        if self.member is not None:
            result['Member'] = self.member

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')

        if m.get('Member') is not None:
            self.member = m.get('Member')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

