# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class DescribeContactGroupsResponseBody(DaraModel):
    def __init__(
        self,
        page_bean: main_models.DescribeContactGroupsResponseBodyPageBean = None,
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
            temp_model = main_models.DescribeContactGroupsResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m.get('PageBean'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeContactGroupsResponseBodyPageBean(DaraModel):
    def __init__(
        self,
        alert_contact_groups: List[main_models.DescribeContactGroupsResponseBodyPageBeanAlertContactGroups] = None,
        page: int = None,
        size: int = None,
        total: int = None,
    ):
        # The name of the alert contact group.
        self.alert_contact_groups = alert_contact_groups
        # The page number of the returned page.
        self.page = page
        # The number of alert contact groups displayed on each page.
        self.size = size
        # The total number of alert contact groups.
        self.total = total

    def validate(self):
        if self.alert_contact_groups:
            for v1 in self.alert_contact_groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AlertContactGroups'] = []
        if self.alert_contact_groups is not None:
            for k1 in self.alert_contact_groups:
                result['AlertContactGroups'].append(k1.to_map() if k1 else None)

        if self.page is not None:
            result['Page'] = self.page

        if self.size is not None:
            result['Size'] = self.size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alert_contact_groups = []
        if m.get('AlertContactGroups') is not None:
            for k1 in m.get('AlertContactGroups'):
                temp_model = main_models.DescribeContactGroupsResponseBodyPageBeanAlertContactGroups()
                self.alert_contact_groups.append(temp_model.from_map(k1))

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeContactGroupsResponseBodyPageBeanAlertContactGroups(DaraModel):
    def __init__(
        self,
        arms_contact_group_id: int = None,
        contact_group_id: float = None,
        contact_group_name: str = None,
        contacts: List[main_models.DescribeContactGroupsResponseBodyPageBeanAlertContactGroupsContacts] = None,
    ):
        # The ID of the alert contact group.
        self.arms_contact_group_id = arms_contact_group_id
        # The ID of the alert contact group.
        self.contact_group_id = contact_group_id
        # The name of the alert contact group.
        self.contact_group_name = contact_group_name
        # The contact information. If the **IsDetail** parameter is set to `false`, no **contact** information is displayed.
        self.contacts = contacts

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
        if self.arms_contact_group_id is not None:
            result['ArmsContactGroupId'] = self.arms_contact_group_id

        if self.contact_group_id is not None:
            result['ContactGroupId'] = self.contact_group_id

        if self.contact_group_name is not None:
            result['ContactGroupName'] = self.contact_group_name

        result['Contacts'] = []
        if self.contacts is not None:
            for k1 in self.contacts:
                result['Contacts'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArmsContactGroupId') is not None:
            self.arms_contact_group_id = m.get('ArmsContactGroupId')

        if m.get('ContactGroupId') is not None:
            self.contact_group_id = m.get('ContactGroupId')

        if m.get('ContactGroupName') is not None:
            self.contact_group_name = m.get('ContactGroupName')

        self.contacts = []
        if m.get('Contacts') is not None:
            for k1 in m.get('Contacts'):
                temp_model = main_models.DescribeContactGroupsResponseBodyPageBeanAlertContactGroupsContacts()
                self.contacts.append(temp_model.from_map(k1))

        return self

class DescribeContactGroupsResponseBodyPageBeanAlertContactGroupsContacts(DaraModel):
    def __init__(
        self,
        arms_contact_id: int = None,
        contact_id: float = None,
        contact_name: str = None,
        email: str = None,
        phone: str = None,
    ):
        # The ID of the alert contact.
        self.arms_contact_id = arms_contact_id
        # The ID of the alert contact.
        self.contact_id = contact_id
        # The name of the alert contact.
        self.contact_name = contact_name
        # The email address of the alert contact.
        self.email = email
        # The mobile number of the alert contact.
        self.phone = phone

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

        if self.phone is not None:
            result['Phone'] = self.phone

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

        if m.get('Phone') is not None:
            self.phone = m.get('Phone')

        return self

