# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20210422 import models as main_models
from darabonba.model import DaraModel

class SearchAlertContactResponseBody(DaraModel):
    def __init__(
        self,
        page_bean: main_models.SearchAlertContactResponseBodyPageBean = None,
        request_id: str = None,
    ):
        self.page_bean = page_bean
        self.request_id = request_id

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageBean') is not None:
            temp_model = main_models.SearchAlertContactResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m.get('PageBean'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class SearchAlertContactResponseBodyPageBean(DaraModel):
    def __init__(
        self,
        contacts: List[main_models.SearchAlertContactResponseBodyPageBeanContacts] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.contacts = contacts
        self.page_number = page_number
        self.page_size = page_size
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

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.contacts = []
        if m.get('Contacts') is not None:
            for k1 in m.get('Contacts'):
                temp_model = main_models.SearchAlertContactResponseBodyPageBeanContacts()
                self.contacts.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class SearchAlertContactResponseBodyPageBeanContacts(DaraModel):
    def __init__(
        self,
        contact_id: int = None,
        contact_name: str = None,
        create_time: int = None,
        ding_robot: str = None,
        email: str = None,
        phone: str = None,
        system_noc: bool = None,
        update_time: int = None,
        user_id: str = None,
        webhook: str = None,
    ):
        self.contact_id = contact_id
        self.contact_name = contact_name
        self.create_time = create_time
        self.ding_robot = ding_robot
        self.email = email
        self.phone = phone
        self.system_noc = system_noc
        self.update_time = update_time
        self.user_id = user_id
        self.webhook = webhook

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id

        if self.contact_name is not None:
            result['ContactName'] = self.contact_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.ding_robot is not None:
            result['DingRobot'] = self.ding_robot

        if self.email is not None:
            result['Email'] = self.email

        if self.phone is not None:
            result['Phone'] = self.phone

        if self.system_noc is not None:
            result['SystemNoc'] = self.system_noc

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.webhook is not None:
            result['Webhook'] = self.webhook

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')

        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DingRobot') is not None:
            self.ding_robot = m.get('DingRobot')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('Phone') is not None:
            self.phone = m.get('Phone')

        if m.get('SystemNoc') is not None:
            self.system_noc = m.get('SystemNoc')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('Webhook') is not None:
            self.webhook = m.get('Webhook')

        return self

