# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ccc20200701 import models as main_models
from darabonba.model import DaraModel

class ListUsersResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListUsersResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        params: List[str] = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.params = params
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.params is not None:
            result['Params'] = self.params

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ListUsersResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListUsersResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.ListUsersResponseBodyDataList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.list = list
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.ListUsersResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListUsersResponseBodyDataList(DaraModel):
    def __init__(
        self,
        device_ext: str = None,
        device_id: str = None,
        device_state: str = None,
        display_id: str = None,
        display_name: str = None,
        email: str = None,
        extension: str = None,
        login_name: str = None,
        mobile: str = None,
        personal_outbound_number_list: List[main_models.ListUsersResponseBodyDataListPersonalOutboundNumberList] = None,
        primary: bool = None,
        primary_account: bool = None,
        ram_id: int = None,
        role_id: str = None,
        role_name: str = None,
        skill_level_list: List[main_models.ListUsersResponseBodyDataListSkillLevelList] = None,
        user_id: str = None,
        work_mode: str = None,
    ):
        self.device_ext = device_ext
        self.device_id = device_id
        self.device_state = device_state
        self.display_id = display_id
        self.display_name = display_name
        self.email = email
        self.extension = extension
        self.login_name = login_name
        self.mobile = mobile
        self.personal_outbound_number_list = personal_outbound_number_list
        self.primary = primary
        self.primary_account = primary_account
        self.ram_id = ram_id
        self.role_id = role_id
        self.role_name = role_name
        self.skill_level_list = skill_level_list
        self.user_id = user_id
        self.work_mode = work_mode

    def validate(self):
        if self.personal_outbound_number_list:
            for v1 in self.personal_outbound_number_list:
                 if v1:
                    v1.validate()
        if self.skill_level_list:
            for v1 in self.skill_level_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_ext is not None:
            result['DeviceExt'] = self.device_ext

        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        if self.device_state is not None:
            result['DeviceState'] = self.device_state

        if self.display_id is not None:
            result['DisplayId'] = self.display_id

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.email is not None:
            result['Email'] = self.email

        if self.extension is not None:
            result['Extension'] = self.extension

        if self.login_name is not None:
            result['LoginName'] = self.login_name

        if self.mobile is not None:
            result['Mobile'] = self.mobile

        result['PersonalOutboundNumberList'] = []
        if self.personal_outbound_number_list is not None:
            for k1 in self.personal_outbound_number_list:
                result['PersonalOutboundNumberList'].append(k1.to_map() if k1 else None)

        if self.primary is not None:
            result['Primary'] = self.primary

        if self.primary_account is not None:
            result['PrimaryAccount'] = self.primary_account

        if self.ram_id is not None:
            result['RamId'] = self.ram_id

        if self.role_id is not None:
            result['RoleId'] = self.role_id

        if self.role_name is not None:
            result['RoleName'] = self.role_name

        result['SkillLevelList'] = []
        if self.skill_level_list is not None:
            for k1 in self.skill_level_list:
                result['SkillLevelList'].append(k1.to_map() if k1 else None)

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.work_mode is not None:
            result['WorkMode'] = self.work_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceExt') is not None:
            self.device_ext = m.get('DeviceExt')

        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        if m.get('DeviceState') is not None:
            self.device_state = m.get('DeviceState')

        if m.get('DisplayId') is not None:
            self.display_id = m.get('DisplayId')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('Extension') is not None:
            self.extension = m.get('Extension')

        if m.get('LoginName') is not None:
            self.login_name = m.get('LoginName')

        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')

        self.personal_outbound_number_list = []
        if m.get('PersonalOutboundNumberList') is not None:
            for k1 in m.get('PersonalOutboundNumberList'):
                temp_model = main_models.ListUsersResponseBodyDataListPersonalOutboundNumberList()
                self.personal_outbound_number_list.append(temp_model.from_map(k1))

        if m.get('Primary') is not None:
            self.primary = m.get('Primary')

        if m.get('PrimaryAccount') is not None:
            self.primary_account = m.get('PrimaryAccount')

        if m.get('RamId') is not None:
            self.ram_id = m.get('RamId')

        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')

        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')

        self.skill_level_list = []
        if m.get('SkillLevelList') is not None:
            for k1 in m.get('SkillLevelList'):
                temp_model = main_models.ListUsersResponseBodyDataListSkillLevelList()
                self.skill_level_list.append(temp_model.from_map(k1))

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('WorkMode') is not None:
            self.work_mode = m.get('WorkMode')

        return self

class ListUsersResponseBodyDataListSkillLevelList(DaraModel):
    def __init__(
        self,
        skill_group_id: str = None,
        skill_group_name: str = None,
        skill_level: int = None,
    ):
        self.skill_group_id = skill_group_id
        self.skill_group_name = skill_group_name
        self.skill_level = skill_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id

        if self.skill_group_name is not None:
            result['SkillGroupName'] = self.skill_group_name

        if self.skill_level is not None:
            result['SkillLevel'] = self.skill_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')

        if m.get('SkillGroupName') is not None:
            self.skill_group_name = m.get('SkillGroupName')

        if m.get('SkillLevel') is not None:
            self.skill_level = m.get('SkillLevel')

        return self

class ListUsersResponseBodyDataListPersonalOutboundNumberList(DaraModel):
    def __init__(
        self,
        active: bool = None,
        city: str = None,
        number: str = None,
        province: str = None,
        usage: str = None,
    ):
        self.active = active
        self.city = city
        self.number = number
        self.province = province
        self.usage = usage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active is not None:
            result['Active'] = self.active

        if self.city is not None:
            result['City'] = self.city

        if self.number is not None:
            result['Number'] = self.number

        if self.province is not None:
            result['Province'] = self.province

        if self.usage is not None:
            result['Usage'] = self.usage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')

        if m.get('City') is not None:
            self.city = m.get('City')

        if m.get('Number') is not None:
            self.number = m.get('Number')

        if m.get('Province') is not None:
            self.province = m.get('Province')

        if m.get('Usage') is not None:
            self.usage = m.get('Usage')

        return self

