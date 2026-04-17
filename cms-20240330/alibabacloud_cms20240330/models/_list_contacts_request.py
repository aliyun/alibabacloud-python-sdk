# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListContactsRequest(DaraModel):
    def __init__(
        self,
        contact_ids: List[str] = None,
        email: str = None,
        group_id: str = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        phone: str = None,
        query_ungrouped_contacts: bool = None,
        workspace: str = None,
    ):
        self.contact_ids = contact_ids
        self.email = email
        self.group_id = group_id
        self.name = name
        self.page_number = page_number
        self.page_size = page_size
        self.phone = phone
        self.query_ungrouped_contacts = query_ungrouped_contacts
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_ids is not None:
            result['contactIds'] = self.contact_ids

        if self.email is not None:
            result['email'] = self.email

        if self.group_id is not None:
            result['groupId'] = self.group_id

        if self.name is not None:
            result['name'] = self.name

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.phone is not None:
            result['phone'] = self.phone

        if self.query_ungrouped_contacts is not None:
            result['queryUngroupedContacts'] = self.query_ungrouped_contacts

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contactIds') is not None:
            self.contact_ids = m.get('contactIds')

        if m.get('email') is not None:
            self.email = m.get('email')

        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('phone') is not None:
            self.phone = m.get('phone')

        if m.get('queryUngroupedContacts') is not None:
            self.query_ungrouped_contacts = m.get('queryUngroupedContacts')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

