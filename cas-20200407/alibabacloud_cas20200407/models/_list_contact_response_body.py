# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cas20200407 import models as main_models
from darabonba.model import DaraModel

class ListContactResponseBody(DaraModel):
    def __init__(
        self,
        contact_list: List[main_models.ListContactResponseBodyContactList] = None,
        current_page: int = None,
        keyword: str = None,
        request_id: str = None,
        show_size: int = None,
        total_count: int = None,
    ):
        # The contacts.
        self.contact_list = contact_list
        # The page number. Default value: **1**.
        self.current_page = current_page
        # The keyword used in the fuzzy search.
        self.keyword = keyword
        # The request ID.
        self.request_id = request_id
        # The number of certificates per page. Default value: **20**.
        self.show_size = show_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.contact_list:
            for v1 in self.contact_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ContactList'] = []
        if self.contact_list is not None:
            for k1 in self.contact_list:
                result['ContactList'].append(k1.to_map() if k1 else None)

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.show_size is not None:
            result['ShowSize'] = self.show_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.contact_list = []
        if m.get('ContactList') is not None:
            for k1 in m.get('ContactList'):
                temp_model = main_models.ListContactResponseBodyContactList()
                self.contact_list.append(temp_model.from_map(k1))

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListContactResponseBodyContactList(DaraModel):
    def __init__(
        self,
        contact_id: int = None,
        email: str = None,
        email_status: int = None,
        mobile: str = None,
        mobile_status: int = None,
        name: str = None,
        webhooks: str = None,
    ):
        # The ID of the contact.
        self.contact_id = contact_id
        # The email address of the contact.
        self.email = email
        # Indicates whether the email address passed the verification.
        self.email_status = email_status
        # The phone number.
        self.mobile = mobile
        # Indicates whether the phone number was verified.
        self.mobile_status = mobile_status
        # The name of the contact.
        self.name = name
        # The webhook URL of the chatbot.
        self.webhooks = webhooks

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id

        if self.email is not None:
            result['Email'] = self.email

        if self.email_status is not None:
            result['EmailStatus'] = self.email_status

        if self.mobile is not None:
            result['Mobile'] = self.mobile

        if self.mobile_status is not None:
            result['MobileStatus'] = self.mobile_status

        if self.name is not None:
            result['Name'] = self.name

        if self.webhooks is not None:
            result['Webhooks'] = self.webhooks

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('EmailStatus') is not None:
            self.email_status = m.get('EmailStatus')

        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')

        if m.get('MobileStatus') is not None:
            self.mobile_status = m.get('MobileStatus')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Webhooks') is not None:
            self.webhooks = m.get('Webhooks')

        return self

