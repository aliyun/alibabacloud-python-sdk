# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_chatbot20220408 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceResponseBody(DaraModel):
    def __init__(
        self,
        avatar: str = None,
        categories: List[main_models.DescribeInstanceResponseBodyCategories] = None,
        create_time: str = None,
        edit_status: str = None,
        instance_id: str = None,
        introduction: str = None,
        language_code: str = None,
        name: str = None,
        request_id: str = None,
        robot_type: str = None,
        time_zone: str = None,
    ):
        self.avatar = avatar
        self.categories = categories
        self.create_time = create_time
        self.edit_status = edit_status
        self.instance_id = instance_id
        self.introduction = introduction
        self.language_code = language_code
        self.name = name
        self.request_id = request_id
        self.robot_type = robot_type
        self.time_zone = time_zone

    def validate(self):
        if self.categories:
            for v1 in self.categories:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avatar is not None:
            result['Avatar'] = self.avatar

        result['Categories'] = []
        if self.categories is not None:
            for k1 in self.categories:
                result['Categories'].append(k1.to_map() if k1 else None)

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.edit_status is not None:
            result['EditStatus'] = self.edit_status

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.introduction is not None:
            result['Introduction'] = self.introduction

        if self.language_code is not None:
            result['LanguageCode'] = self.language_code

        if self.name is not None:
            result['Name'] = self.name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.robot_type is not None:
            result['RobotType'] = self.robot_type

        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Avatar') is not None:
            self.avatar = m.get('Avatar')

        self.categories = []
        if m.get('Categories') is not None:
            for k1 in m.get('Categories'):
                temp_model = main_models.DescribeInstanceResponseBodyCategories()
                self.categories.append(temp_model.from_map(k1))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('EditStatus') is not None:
            self.edit_status = m.get('EditStatus')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Introduction') is not None:
            self.introduction = m.get('Introduction')

        if m.get('LanguageCode') is not None:
            self.language_code = m.get('LanguageCode')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RobotType') is not None:
            self.robot_type = m.get('RobotType')

        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')

        return self

class DescribeInstanceResponseBodyCategories(DaraModel):
    def __init__(
        self,
        ability_type: str = None,
        category_id: int = None,
        name: str = None,
        parent_category_id: int = None,
    ):
        self.ability_type = ability_type
        self.category_id = category_id
        self.name = name
        self.parent_category_id = parent_category_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ability_type is not None:
            result['AbilityType'] = self.ability_type

        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.name is not None:
            result['Name'] = self.name

        if self.parent_category_id is not None:
            result['ParentCategoryId'] = self.parent_category_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AbilityType') is not None:
            self.ability_type = m.get('AbilityType')

        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ParentCategoryId') is not None:
            self.parent_category_id = m.get('ParentCategoryId')

        return self

