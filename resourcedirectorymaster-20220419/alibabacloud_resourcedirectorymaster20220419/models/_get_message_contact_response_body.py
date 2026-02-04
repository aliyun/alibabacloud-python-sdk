# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcedirectorymaster20220419 import models as main_models
from darabonba.model import DaraModel

class GetMessageContactResponseBody(DaraModel):
    def __init__(
        self,
        contact: main_models.GetMessageContactResponseBodyContact = None,
        request_id: str = None,
    ):
        # The information about the contact.
        self.contact = contact
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.contact:
            self.contact.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact is not None:
            result['Contact'] = self.contact.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Contact') is not None:
            temp_model = main_models.GetMessageContactResponseBodyContact()
            self.contact = temp_model.from_map(m.get('Contact'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetMessageContactResponseBodyContact(DaraModel):
    def __init__(
        self,
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
        # The ID of the contact.
        self.contact_id = contact_id
        # The time when the contact was created.
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
        # *   Verifying
        # *   Active
        # *   Deleting
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

