# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcedirectorymaster20220419 import models as main_models
from darabonba.model import DaraModel

class ListMessageContactsResponseBody(DaraModel):
    def __init__(
        self,
        contacts: List[main_models.ListMessageContactsResponseBodyContacts] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The time when the contact was bound to the objects.
        self.contacts = contacts
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.contacts:
            for v1 in self.contacts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Contacts'] = []
        if self.contacts is not None:
            for k1 in self.contacts:
                result['Contacts'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.contacts = []
        if m.get('Contacts') is not None:
            for k1 in m.get('Contacts'):
                temp_model = main_models.ListMessageContactsResponseBodyContacts()
                self.contacts.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListMessageContactsResponseBodyContacts(DaraModel):
    def __init__(
        self,
        associated_date: str = None,
        contact_id: str = None,
        create_date: str = None,
        email_address: str = None,
        members: List[str] = None,
        message_types: List[str] = None,
        name: str = None,
        phone_number: str = None,
        status: str = None,
        title: str = None,
    ):
        # The time when the contact was bound to the objects.
        self.associated_date = associated_date
        # The ID of the contact.
        self.contact_id = contact_id
        # The time when the contact was added.
        self.create_date = create_date
        # The email address of the contact.
        self.email_address = email_address
        # The IDs of objects to which the contact is bound.
        self.members = members
        # The types of messages received by the contact.
        self.message_types = message_types
        # The name of the contact.
        self.name = name
        # The mobile phone number of the contact.
        self.phone_number = phone_number
        # The status of the contact. Valid values:
        # 
        # - Verifying
        # - Active
        # - Deleting
        self.status = status
        # The job title of the contact.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.associated_date is not None:
            result['AssociatedDate'] = self.associated_date

        if self.contact_id is not None:
            result['ContactId'] = self.contact_id

        if self.create_date is not None:
            result['CreateDate'] = self.create_date

        if self.email_address is not None:
            result['EmailAddress'] = self.email_address

        if self.members is not None:
            result['Members'] = self.members

        if self.message_types is not None:
            result['MessageTypes'] = self.message_types

        if self.name is not None:
            result['Name'] = self.name

        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number

        if self.status is not None:
            result['Status'] = self.status

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssociatedDate') is not None:
            self.associated_date = m.get('AssociatedDate')

        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')

        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')

        if m.get('EmailAddress') is not None:
            self.email_address = m.get('EmailAddress')

        if m.get('Members') is not None:
            self.members = m.get('Members')

        if m.get('MessageTypes') is not None:
            self.message_types = m.get('MessageTypes')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

