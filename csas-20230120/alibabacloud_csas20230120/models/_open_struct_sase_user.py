# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class OpenStructSaseUser(DaraModel):
    def __init__(
        self,
        create_time_unix: int = None,
        custom_fields: List[main_models.IdpCustomField] = None,
        departments: List[main_models.OpenStructSaseDepartment] = None,
        description: str = None,
        email: str = None,
        idp_config_id: str = None,
        leave_time_unix: int = None,
        login_time_unix: int = None,
        sase_user_id: str = None,
        sase_user_status: str = None,
        sync_time_unix: int = None,
        telephone: str = None,
        title: str = None,
        update_time_unix: int = None,
        user_tags: List[main_models.OpenStructSaseUserUserTags] = None,
        username: str = None,
        work_status: str = None,
    ):
        self.create_time_unix = create_time_unix
        self.custom_fields = custom_fields
        self.departments = departments
        self.description = description
        self.email = email
        self.idp_config_id = idp_config_id
        self.leave_time_unix = leave_time_unix
        self.login_time_unix = login_time_unix
        self.sase_user_id = sase_user_id
        self.sase_user_status = sase_user_status
        self.sync_time_unix = sync_time_unix
        self.telephone = telephone
        self.title = title
        self.update_time_unix = update_time_unix
        self.user_tags = user_tags
        self.username = username
        self.work_status = work_status

    def validate(self):
        if self.custom_fields:
            for v1 in self.custom_fields:
                 if v1:
                    v1.validate()
        if self.departments:
            for v1 in self.departments:
                 if v1:
                    v1.validate()
        if self.user_tags:
            for v1 in self.user_tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time_unix is not None:
            result['CreateTimeUnix'] = self.create_time_unix

        result['CustomFields'] = []
        if self.custom_fields is not None:
            for k1 in self.custom_fields:
                result['CustomFields'].append(k1.to_map() if k1 else None)

        result['Departments'] = []
        if self.departments is not None:
            for k1 in self.departments:
                result['Departments'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['Description'] = self.description

        if self.email is not None:
            result['Email'] = self.email

        if self.idp_config_id is not None:
            result['IdpConfigId'] = self.idp_config_id

        if self.leave_time_unix is not None:
            result['LeaveTimeUnix'] = self.leave_time_unix

        if self.login_time_unix is not None:
            result['LoginTimeUnix'] = self.login_time_unix

        if self.sase_user_id is not None:
            result['SaseUserId'] = self.sase_user_id

        if self.sase_user_status is not None:
            result['SaseUserStatus'] = self.sase_user_status

        if self.sync_time_unix is not None:
            result['SyncTimeUnix'] = self.sync_time_unix

        if self.telephone is not None:
            result['Telephone'] = self.telephone

        if self.title is not None:
            result['Title'] = self.title

        if self.update_time_unix is not None:
            result['UpdateTimeUnix'] = self.update_time_unix

        result['UserTags'] = []
        if self.user_tags is not None:
            for k1 in self.user_tags:
                result['UserTags'].append(k1.to_map() if k1 else None)

        if self.username is not None:
            result['Username'] = self.username

        if self.work_status is not None:
            result['WorkStatus'] = self.work_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTimeUnix') is not None:
            self.create_time_unix = m.get('CreateTimeUnix')

        self.custom_fields = []
        if m.get('CustomFields') is not None:
            for k1 in m.get('CustomFields'):
                temp_model = main_models.IdpCustomField()
                self.custom_fields.append(temp_model.from_map(k1))

        self.departments = []
        if m.get('Departments') is not None:
            for k1 in m.get('Departments'):
                temp_model = main_models.OpenStructSaseDepartment()
                self.departments.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('IdpConfigId') is not None:
            self.idp_config_id = m.get('IdpConfigId')

        if m.get('LeaveTimeUnix') is not None:
            self.leave_time_unix = m.get('LeaveTimeUnix')

        if m.get('LoginTimeUnix') is not None:
            self.login_time_unix = m.get('LoginTimeUnix')

        if m.get('SaseUserId') is not None:
            self.sase_user_id = m.get('SaseUserId')

        if m.get('SaseUserStatus') is not None:
            self.sase_user_status = m.get('SaseUserStatus')

        if m.get('SyncTimeUnix') is not None:
            self.sync_time_unix = m.get('SyncTimeUnix')

        if m.get('Telephone') is not None:
            self.telephone = m.get('Telephone')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('UpdateTimeUnix') is not None:
            self.update_time_unix = m.get('UpdateTimeUnix')

        self.user_tags = []
        if m.get('UserTags') is not None:
            for k1 in m.get('UserTags'):
                temp_model = main_models.OpenStructSaseUserUserTags()
                self.user_tags.append(temp_model.from_map(k1))

        if m.get('Username') is not None:
            self.username = m.get('Username')

        if m.get('WorkStatus') is not None:
            self.work_status = m.get('WorkStatus')

        return self

class OpenStructSaseUserUserTags(DaraModel):
    def __init__(
        self,
        aliuid: str = None,
        description: str = None,
        name: str = None,
        sase_user_id: str = None,
        tag_id: str = None,
    ):
        self.aliuid = aliuid
        self.description = description
        self.name = name
        self.sase_user_id = sase_user_id
        self.tag_id = tag_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliuid is not None:
            result['Aliuid'] = self.aliuid

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.sase_user_id is not None:
            result['SaseUserId'] = self.sase_user_id

        if self.tag_id is not None:
            result['TagId'] = self.tag_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Aliuid') is not None:
            self.aliuid = m.get('Aliuid')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SaseUserId') is not None:
            self.sase_user_id = m.get('SaseUserId')

        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')

        return self

