# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ccc20200701 import models as main_models
from darabonba.model import DaraModel

class ListInstancesOfUserResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListInstancesOfUserResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        # Response code.
        self.code = code
        # Data.
        self.data = data
        # HTTP status code.
        self.http_status_code = http_status_code
        # Response message.
        self.message = message
        # Request ID.
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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ListInstancesOfUserResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListInstancesOfUserResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.ListInstancesOfUserResponseBodyDataList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # List.
        self.list = list
        # Page number, ranging from 1 to 100.
        self.page_number = page_number
        # Page size, ranging from 1 to 100.
        self.page_size = page_size
        # Total count.
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
                temp_model = main_models.ListInstancesOfUserResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListInstancesOfUserResponseBodyDataList(DaraModel):
    def __init__(
        self,
        admin_list: List[main_models.ListInstancesOfUserResponseBodyDataListAdminList] = None,
        aliyun_uid: str = None,
        console_url: str = None,
        description: str = None,
        domain_name: str = None,
        id: str = None,
        name: str = None,
        number_list: List[main_models.ListInstancesOfUserResponseBodyDataListNumberList] = None,
        status: str = None,
    ):
        # Administrator list.
        self.admin_list = admin_list
        # The Alibaba Cloud Account ID to which the instance belongs.
        self.aliyun_uid = aliyun_uid
        # The URL of the Cloud Contact Center instance, used to access the homepage of the Cloud Contact Center instance. It consists of the specific Cloud Contact Center URL followed by the instance ID.
        self.console_url = console_url
        # The instance description.
        self.description = description
        # The domain name of the instance, which is globally unique.
        self.domain_name = domain_name
        # The instance ID.
        self.id = id
        # The instance name.
        self.name = name
        # List of numbers.
        self.number_list = number_list
        # Instance status.
        self.status = status

    def validate(self):
        if self.admin_list:
            for v1 in self.admin_list:
                 if v1:
                    v1.validate()
        if self.number_list:
            for v1 in self.number_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AdminList'] = []
        if self.admin_list is not None:
            for k1 in self.admin_list:
                result['AdminList'].append(k1.to_map() if k1 else None)

        if self.aliyun_uid is not None:
            result['AliyunUid'] = self.aliyun_uid

        if self.console_url is not None:
            result['ConsoleUrl'] = self.console_url

        if self.description is not None:
            result['Description'] = self.description

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        result['NumberList'] = []
        if self.number_list is not None:
            for k1 in self.number_list:
                result['NumberList'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.admin_list = []
        if m.get('AdminList') is not None:
            for k1 in m.get('AdminList'):
                temp_model = main_models.ListInstancesOfUserResponseBodyDataListAdminList()
                self.admin_list.append(temp_model.from_map(k1))

        if m.get('AliyunUid') is not None:
            self.aliyun_uid = m.get('AliyunUid')

        if m.get('ConsoleUrl') is not None:
            self.console_url = m.get('ConsoleUrl')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.number_list = []
        if m.get('NumberList') is not None:
            for k1 in m.get('NumberList'):
                temp_model = main_models.ListInstancesOfUserResponseBodyDataListNumberList()
                self.number_list.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class ListInstancesOfUserResponseBodyDataListNumberList(DaraModel):
    def __init__(
        self,
        active: bool = None,
        city: str = None,
        contact_flow_id: str = None,
        instance_id: str = None,
        number: str = None,
        province: str = None,
        skill_groups: List[main_models.ListInstancesOfUserResponseBodyDataListNumberListSkillGroups] = None,
        usage: str = None,
        user_id: str = None,
    ):
        # Indicates whether the number is active.
        self.active = active
        # The city of the phone number\\"s registration location.
        self.city = city
        # The contact flow ID (IVR) associated with this phone number.
        self.contact_flow_id = contact_flow_id
        # Instance ID.
        self.instance_id = instance_id
        # The number.
        self.number = number
        # The province of the phone number\\"s registration location.
        self.province = province
        # List of skill groups associated with the phone number.
        self.skill_groups = skill_groups
        # The usage of the number.
        self.usage = usage
        # Agent ID. If this parameter is not empty, the number is a personal outbound number assigned to the agent.
        self.user_id = user_id

    def validate(self):
        if self.skill_groups:
            for v1 in self.skill_groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active is not None:
            result['Active'] = self.active

        if self.city is not None:
            result['City'] = self.city

        if self.contact_flow_id is not None:
            result['ContactFlowId'] = self.contact_flow_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.number is not None:
            result['Number'] = self.number

        if self.province is not None:
            result['Province'] = self.province

        result['SkillGroups'] = []
        if self.skill_groups is not None:
            for k1 in self.skill_groups:
                result['SkillGroups'].append(k1.to_map() if k1 else None)

        if self.usage is not None:
            result['Usage'] = self.usage

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')

        if m.get('City') is not None:
            self.city = m.get('City')

        if m.get('ContactFlowId') is not None:
            self.contact_flow_id = m.get('ContactFlowId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Number') is not None:
            self.number = m.get('Number')

        if m.get('Province') is not None:
            self.province = m.get('Province')

        self.skill_groups = []
        if m.get('SkillGroups') is not None:
            for k1 in m.get('SkillGroups'):
                temp_model = main_models.ListInstancesOfUserResponseBodyDataListNumberListSkillGroups()
                self.skill_groups.append(temp_model.from_map(k1))

        if m.get('Usage') is not None:
            self.usage = m.get('Usage')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class ListInstancesOfUserResponseBodyDataListNumberListSkillGroups(DaraModel):
    def __init__(
        self,
        description: str = None,
        display_name: str = None,
        instance_id: str = None,
        name: str = None,
        phone_number_count: int = None,
        skill_group_id: str = None,
        user_count: int = None,
    ):
        # Skill group description.
        self.description = description
        # The display name of the skill group.
        self.display_name = display_name
        # Instance ID.
        self.instance_id = instance_id
        # The name of the skill group.
        self.name = name
        # Number of phone numbers associated with the skill group.
        self.phone_number_count = phone_number_count
        # The skill group ID.
        self.skill_group_id = skill_group_id
        # The number of agents associated with the skill group.
        self.user_count = user_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.phone_number_count is not None:
            result['PhoneNumberCount'] = self.phone_number_count

        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id

        if self.user_count is not None:
            result['UserCount'] = self.user_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PhoneNumberCount') is not None:
            self.phone_number_count = m.get('PhoneNumberCount')

        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')

        if m.get('UserCount') is not None:
            self.user_count = m.get('UserCount')

        return self

class ListInstancesOfUserResponseBodyDataListAdminList(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        email: str = None,
        extension: str = None,
        instance_id: str = None,
        login_name: str = None,
        mobile: str = None,
        role_id: str = None,
        role_name: str = None,
        user_id: str = None,
        work_mode: str = None,
    ):
        # The administrator\\"s name.
        self.display_name = display_name
        # Mailbox.
        self.email = email
        # Agent extension number.
        self.extension = extension
        # Instance ID.
        self.instance_id = instance_id
        # Agent logon name.
        self.login_name = login_name
        # The agent\\"s personal phone number.
        self.mobile = mobile
        # The role ID, in the format: role\\@instance ID.
        self.role_id = role_id
        # Role name.
        self.role_name = role_name
        # Agent ID.
        self.user_id = user_id
        # Work mode.
        self.work_mode = work_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.email is not None:
            result['Email'] = self.email

        if self.extension is not None:
            result['Extension'] = self.extension

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.login_name is not None:
            result['LoginName'] = self.login_name

        if self.mobile is not None:
            result['Mobile'] = self.mobile

        if self.role_id is not None:
            result['RoleId'] = self.role_id

        if self.role_name is not None:
            result['RoleName'] = self.role_name

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.work_mode is not None:
            result['WorkMode'] = self.work_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('Extension') is not None:
            self.extension = m.get('Extension')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LoginName') is not None:
            self.login_name = m.get('LoginName')

        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')

        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')

        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('WorkMode') is not None:
            self.work_mode = m.get('WorkMode')

        return self

