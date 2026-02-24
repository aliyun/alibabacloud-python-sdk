# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class ListDigitalEmployeeSkillVersionsResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListDigitalEmployeeSkillVersionsResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.ListDigitalEmployeeSkillVersionsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListDigitalEmployeeSkillVersionsResponseBodyData(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        display_name: str = None,
        enable: bool = None,
        remark: str = None,
        skill_name: str = None,
        update_time: str = None,
        version: str = None,
    ):
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.create_time = create_time
        self.description = description
        self.display_name = display_name
        self.enable = enable
        self.remark = remark
        self.skill_name = skill_name
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.update_time = update_time
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.description is not None:
            result['description'] = self.description

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.enable is not None:
            result['enable'] = self.enable

        if self.remark is not None:
            result['remark'] = self.remark

        if self.skill_name is not None:
            result['skillName'] = self.skill_name

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('remark') is not None:
            self.remark = m.get('remark')

        if m.get('skillName') is not None:
            self.skill_name = m.get('skillName')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

