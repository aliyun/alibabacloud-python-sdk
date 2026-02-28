# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ccc20200701 import models as main_models
from darabonba.model import DaraModel

class ListPhoneNumbersResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListPhoneNumbersResponseBodyData = None,
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
            temp_model = main_models.ListPhoneNumbersResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListPhoneNumbersResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.ListPhoneNumbersResponseBodyDataList] = None,
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
                temp_model = main_models.ListPhoneNumbersResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListPhoneNumbersResponseBodyDataList(DaraModel):
    def __init__(
        self,
        active: bool = None,
        city: str = None,
        contact_flow_id: str = None,
        contact_flow_name: str = None,
        create_time: str = None,
        instance_id: str = None,
        number: str = None,
        provider: str = None,
        province: str = None,
        skill_groups: List[main_models.ListPhoneNumbersResponseBodyDataListSkillGroups] = None,
        tags: str = None,
        usage: str = None,
        user_id: str = None,
    ):
        self.active = active
        self.city = city
        self.contact_flow_id = contact_flow_id
        self.contact_flow_name = contact_flow_name
        self.create_time = create_time
        self.instance_id = instance_id
        self.number = number
        self.provider = provider
        self.province = province
        self.skill_groups = skill_groups
        self.tags = tags
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

        if self.contact_flow_name is not None:
            result['ContactFlowName'] = self.contact_flow_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.number is not None:
            result['Number'] = self.number

        if self.provider is not None:
            result['Provider'] = self.provider

        if self.province is not None:
            result['Province'] = self.province

        result['SkillGroups'] = []
        if self.skill_groups is not None:
            for k1 in self.skill_groups:
                result['SkillGroups'].append(k1.to_map() if k1 else None)

        if self.tags is not None:
            result['Tags'] = self.tags

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

        if m.get('ContactFlowName') is not None:
            self.contact_flow_name = m.get('ContactFlowName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Number') is not None:
            self.number = m.get('Number')

        if m.get('Provider') is not None:
            self.provider = m.get('Provider')

        if m.get('Province') is not None:
            self.province = m.get('Province')

        self.skill_groups = []
        if m.get('SkillGroups') is not None:
            for k1 in m.get('SkillGroups'):
                temp_model = main_models.ListPhoneNumbersResponseBodyDataListSkillGroups()
                self.skill_groups.append(temp_model.from_map(k1))

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('Usage') is not None:
            self.usage = m.get('Usage')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class ListPhoneNumbersResponseBodyDataListSkillGroups(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        instance_id: str = None,
        name: str = None,
        skill_group_id: str = None,
    ):
        self.display_name = display_name
        self.instance_id = instance_id
        self.name = name
        self.skill_group_id = skill_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')

        return self

