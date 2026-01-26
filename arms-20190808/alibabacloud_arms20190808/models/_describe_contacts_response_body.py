# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class DescribeContactsResponseBody(DaraModel):
    def __init__(
        self,
        page_bean: main_models.DescribeContactsResponseBodyPageBean = None,
        request_id: str = None,
    ):
        # The objects that were returned.
        self.page_bean = page_bean
        # The ID of the request.
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
            temp_model = main_models.DescribeContactsResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m.get('PageBean'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeContactsResponseBodyPageBean(DaraModel):
    def __init__(
        self,
        alert_contacts: List[main_models.DescribeContactsResponseBodyPageBeanAlertContacts] = None,
        page: int = None,
        size: int = None,
        total: int = None,
    ):
        # The alert contacts.
        self.alert_contacts = alert_contacts
        # The page number of the returned page.
        self.page = page
        # The number of alert contacts returned per page.
        self.size = size
        # The total number of alert contacts.
        self.total = total

    def validate(self):
        if self.alert_contacts:
            for v1 in self.alert_contacts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AlertContacts'] = []
        if self.alert_contacts is not None:
            for k1 in self.alert_contacts:
                result['AlertContacts'].append(k1.to_map() if k1 else None)

        if self.page is not None:
            result['Page'] = self.page

        if self.size is not None:
            result['Size'] = self.size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alert_contacts = []
        if m.get('AlertContacts') is not None:
            for k1 in m.get('AlertContacts'):
                temp_model = main_models.DescribeContactsResponseBodyPageBeanAlertContacts()
                self.alert_contacts.append(temp_model.from_map(k1))

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeContactsResponseBodyPageBeanAlertContacts(DaraModel):
    def __init__(
        self,
        arms_contact_id: int = None,
        contact_id: float = None,
        contact_name: str = None,
        email: str = None,
        is_email_verify: bool = None,
        is_verify: bool = None,
        phone: str = None,
        reissue_send_notice: int = None,
    ):
        # The ID of the alert contact.
        self.arms_contact_id = arms_contact_id
        # The ID of the alert contact.
        self.contact_id = contact_id
        # The name of the alert contact.
        self.contact_name = contact_name
        # The email address of the alert contact.
        self.email = email
        # Indicates whether the email address was verified.
        self.is_email_verify = is_email_verify
        # Indicates whether the mobile number was verified. Valid values:
        # 
        # *   `false`: no
        # *   `true`: yes
        self.is_verify = is_verify
        # The mobile number of the alert contact.
        self.phone = phone
        # The operation that you want to perform if phone calls fail to be answered. Valid values:
        # 
        # *   0: No operation is performed.
        # *   1: A phone call is made again.
        # *   2: A text message is sent.
        # *   3 (default value): The global default value is used.
        self.reissue_send_notice = reissue_send_notice

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arms_contact_id is not None:
            result['ArmsContactId'] = self.arms_contact_id

        if self.contact_id is not None:
            result['ContactId'] = self.contact_id

        if self.contact_name is not None:
            result['ContactName'] = self.contact_name

        if self.email is not None:
            result['Email'] = self.email

        if self.is_email_verify is not None:
            result['IsEmailVerify'] = self.is_email_verify

        if self.is_verify is not None:
            result['IsVerify'] = self.is_verify

        if self.phone is not None:
            result['Phone'] = self.phone

        if self.reissue_send_notice is not None:
            result['ReissueSendNotice'] = self.reissue_send_notice

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArmsContactId') is not None:
            self.arms_contact_id = m.get('ArmsContactId')

        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')

        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('IsEmailVerify') is not None:
            self.is_email_verify = m.get('IsEmailVerify')

        if m.get('IsVerify') is not None:
            self.is_verify = m.get('IsVerify')

        if m.get('Phone') is not None:
            self.phone = m.get('Phone')

        if m.get('ReissueSendNotice') is not None:
            self.reissue_send_notice = m.get('ReissueSendNotice')

        return self

