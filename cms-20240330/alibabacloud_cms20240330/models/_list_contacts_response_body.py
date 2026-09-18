# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class ListContactsResponseBody(DaraModel):
    def __init__(
        self,
        contacts: List[main_models.ListContactsResponseBodyContacts] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
    ):
        # The list of alert contacts.
        self.contacts = contacts
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 100.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of records.
        self.total = total

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
        result['contacts'] = []
        if self.contacts is not None:
            for k1 in self.contacts:
                result['contacts'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.contacts = []
        if m.get('contacts') is not None:
            for k1 in m.get('contacts'):
                temp_model = main_models.ListContactsResponseBodyContacts()
                self.contacts.append(temp_model.from_map(k1))

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListContactsResponseBodyContacts(DaraModel):
    def __init__(
        self,
        contact_id: str = None,
        email: str = None,
        email_verify: bool = None,
        group_list: List[str] = None,
        im_user_ids: Dict[str, str] = None,
        lang: str = None,
        name: str = None,
        phone: str = None,
        phone_verify: bool = None,
        update_time: str = None,
        workspace: str = None,
    ):
        # The ID of the alert contact.
        self.contact_id = contact_id
        # The email address of the alert contact.
        self.email = email
        # Indicates whether the email address is verified.
        self.email_verify = email_verify
        # The contact groups to which the alert contact belongs.
        self.group_list = group_list
        # The mapping of instant messaging user IDs. Multiple instant messaging tools are supported.
        self.im_user_ids = im_user_ids
        # The language.
        self.lang = lang
        # The name of the alert contact.
        self.name = name
        # The phone number of the alert contact.
        self.phone = phone
        # Indicates whether the phone number of the alert contact is verified.
        self.phone_verify = phone_verify
        # The time when the alert contact was last updated. Format: yyyy-MM-dd HH:mm:ss.
        self.update_time = update_time
        # The workspace name.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_id is not None:
            result['contactId'] = self.contact_id

        if self.email is not None:
            result['email'] = self.email

        if self.email_verify is not None:
            result['emailVerify'] = self.email_verify

        if self.group_list is not None:
            result['groupList'] = self.group_list

        if self.im_user_ids is not None:
            result['imUserIds'] = self.im_user_ids

        if self.lang is not None:
            result['lang'] = self.lang

        if self.name is not None:
            result['name'] = self.name

        if self.phone is not None:
            result['phone'] = self.phone

        if self.phone_verify is not None:
            result['phoneVerify'] = self.phone_verify

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contactId') is not None:
            self.contact_id = m.get('contactId')

        if m.get('email') is not None:
            self.email = m.get('email')

        if m.get('emailVerify') is not None:
            self.email_verify = m.get('emailVerify')

        if m.get('groupList') is not None:
            self.group_list = m.get('groupList')

        if m.get('imUserIds') is not None:
            self.im_user_ids = m.get('imUserIds')

        if m.get('lang') is not None:
            self.lang = m.get('lang')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('phone') is not None:
            self.phone = m.get('phone')

        if m.get('phoneVerify') is not None:
            self.phone_verify = m.get('phoneVerify')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

