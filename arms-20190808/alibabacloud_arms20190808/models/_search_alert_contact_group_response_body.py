# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class SearchAlertContactGroupResponseBody(DaraModel):
    def __init__(
        self,
        contact_groups: List[main_models.SearchAlertContactGroupResponseBodyContactGroups] = None,
        request_id: str = None,
    ):
        # The information about the alert contact groups.
        self.contact_groups = contact_groups
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.contact_groups:
            for v1 in self.contact_groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ContactGroups'] = []
        if self.contact_groups is not None:
            for k1 in self.contact_groups:
                result['ContactGroups'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.contact_groups = []
        if m.get('ContactGroups') is not None:
            for k1 in m.get('ContactGroups'):
                temp_model = main_models.SearchAlertContactGroupResponseBodyContactGroups()
                self.contact_groups.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class SearchAlertContactGroupResponseBodyContactGroups(DaraModel):
    def __init__(
        self,
        contact_group_id: int = None,
        contact_group_name: str = None,
        contacts: List[main_models.SearchAlertContactGroupResponseBodyContactGroupsContacts] = None,
        create_time: int = None,
        update_time: int = None,
        user_id: str = None,
    ):
        # The ID of the alert contact group.
        self.contact_group_id = contact_group_id
        # The name of the alert contact group.
        self.contact_group_name = contact_group_name
        # The alert contact list.
        self.contacts = contacts
        # The time when the alert contact group list was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_time = create_time
        # The time when the alert contact group was last modified. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.update_time = update_time
        # The ID of the user.
        self.user_id = user_id

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
        if self.contact_group_id is not None:
            result['ContactGroupId'] = self.contact_group_id

        if self.contact_group_name is not None:
            result['ContactGroupName'] = self.contact_group_name

        result['Contacts'] = []
        if self.contacts is not None:
            for k1 in self.contacts:
                result['Contacts'].append(k1.to_map() if k1 else None)

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactGroupId') is not None:
            self.contact_group_id = m.get('ContactGroupId')

        if m.get('ContactGroupName') is not None:
            self.contact_group_name = m.get('ContactGroupName')

        self.contacts = []
        if m.get('Contacts') is not None:
            for k1 in m.get('Contacts'):
                temp_model = main_models.SearchAlertContactGroupResponseBodyContactGroupsContacts()
                self.contacts.append(temp_model.from_map(k1))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class SearchAlertContactGroupResponseBodyContactGroupsContacts(DaraModel):
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
    ):
        # The ID of the alert contact.
        self.contact_id = contact_id
        # The name of the alert contact.
        self.contact_name = contact_name
        # The time when the alert contact group list was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_time = create_time
        # The webhook URL of the DingTalk chatbot.
        self.ding_robot = ding_robot
        # The email address of the alert contact.
        self.email = email
        # The mobile number of the alert contact.
        self.phone = phone
        # Indicates whether the alert contact receives system notifications. Valid values:
        # 
        # *   true: receives system notifications.
        # *   false: does not receive system notifications.
        self.system_noc = system_noc
        # The time when the alert contact group was last modified. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.update_time = update_time
        # The ID of the user.
        self.user_id = user_id

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

        return self

