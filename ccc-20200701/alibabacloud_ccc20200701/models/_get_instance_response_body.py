# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ccc20200701 import models as main_models
from darabonba.model import DaraModel

class GetInstanceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetInstanceResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
            temp_model = main_models.GetInstanceResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetInstanceResponseBodyData(DaraModel):
    def __init__(
        self,
        admin_list: List[main_models.GetInstanceResponseBodyDataAdminList] = None,
        agent_type: str = None,
        aliyun_uid: str = None,
        chatbot_business_unit: main_models.GetInstanceResponseBodyDataChatbotBusinessUnit = None,
        console_url: str = None,
        description: str = None,
        domain_name: str = None,
        id: str = None,
        name: str = None,
        number_list: List[main_models.GetInstanceResponseBodyDataNumberList] = None,
        status: str = None,
    ):
        self.admin_list = admin_list
        self.agent_type = agent_type
        self.aliyun_uid = aliyun_uid
        self.chatbot_business_unit = chatbot_business_unit
        self.console_url = console_url
        self.description = description
        self.domain_name = domain_name
        self.id = id
        self.name = name
        self.number_list = number_list
        self.status = status

    def validate(self):
        if self.admin_list:
            for v1 in self.admin_list:
                 if v1:
                    v1.validate()
        if self.chatbot_business_unit:
            self.chatbot_business_unit.validate()
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

        if self.agent_type is not None:
            result['AgentType'] = self.agent_type

        if self.aliyun_uid is not None:
            result['AliyunUid'] = self.aliyun_uid

        if self.chatbot_business_unit is not None:
            result['ChatbotBusinessUnit'] = self.chatbot_business_unit.to_map()

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
                temp_model = main_models.GetInstanceResponseBodyDataAdminList()
                self.admin_list.append(temp_model.from_map(k1))

        if m.get('AgentType') is not None:
            self.agent_type = m.get('AgentType')

        if m.get('AliyunUid') is not None:
            self.aliyun_uid = m.get('AliyunUid')

        if m.get('ChatbotBusinessUnit') is not None:
            temp_model = main_models.GetInstanceResponseBodyDataChatbotBusinessUnit()
            self.chatbot_business_unit = temp_model.from_map(m.get('ChatbotBusinessUnit'))

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
                temp_model = main_models.GetInstanceResponseBodyDataNumberList()
                self.number_list.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetInstanceResponseBodyDataNumberList(DaraModel):
    def __init__(
        self,
        active: bool = None,
        city: str = None,
        contact_flow_id: str = None,
        instance_id: str = None,
        number: str = None,
        province: str = None,
        skill_groups: List[main_models.GetInstanceResponseBodyDataNumberListSkillGroups] = None,
        usage: str = None,
        user_id: str = None,
    ):
        self.active = active
        self.city = city
        self.contact_flow_id = contact_flow_id
        self.instance_id = instance_id
        self.number = number
        self.province = province
        self.skill_groups = skill_groups
        self.usage = usage
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
                temp_model = main_models.GetInstanceResponseBodyDataNumberListSkillGroups()
                self.skill_groups.append(temp_model.from_map(k1))

        if m.get('Usage') is not None:
            self.usage = m.get('Usage')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class GetInstanceResponseBodyDataNumberListSkillGroups(DaraModel):
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
        self.description = description
        self.display_name = display_name
        self.instance_id = instance_id
        self.name = name
        self.phone_number_count = phone_number_count
        self.skill_group_id = skill_group_id
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

class GetInstanceResponseBodyDataChatbotBusinessUnit(DaraModel):
    def __init__(
        self,
        unit_id: int = None,
        unit_key: str = None,
    ):
        self.unit_id = unit_id
        self.unit_key = unit_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.unit_id is not None:
            result['UnitId'] = self.unit_id

        if self.unit_key is not None:
            result['UnitKey'] = self.unit_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UnitId') is not None:
            self.unit_id = m.get('UnitId')

        if m.get('UnitKey') is not None:
            self.unit_key = m.get('UnitKey')

        return self

class GetInstanceResponseBodyDataAdminList(DaraModel):
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
        self.display_name = display_name
        self.email = email
        self.extension = extension
        self.instance_id = instance_id
        self.login_name = login_name
        self.mobile = mobile
        self.role_id = role_id
        self.role_name = role_name
        self.user_id = user_id
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

