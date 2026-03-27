# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class GetDigitalEmployeeSkillResponseBody(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        display_name: str = None,
        enable: bool = None,
        files: List[main_models.GetDigitalEmployeeSkillResponseBodyFiles] = None,
        remark: str = None,
        request_id: str = None,
        skill_name: str = None,
        update_time: str = None,
        version: str = None,
    ):
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.create_time = create_time
        self.description = description
        self.display_name = display_name
        self.enable = enable
        self.files = files
        self.remark = remark
        # Id of the request
        self.request_id = request_id
        self.skill_name = skill_name
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.update_time = update_time
        self.version = version

    def validate(self):
        if self.files:
            for v1 in self.files:
                 if v1:
                    v1.validate()

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

        result['files'] = []
        if self.files is not None:
            for k1 in self.files:
                result['files'].append(k1.to_map() if k1 else None)

        if self.remark is not None:
            result['remark'] = self.remark

        if self.request_id is not None:
            result['requestId'] = self.request_id

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

        self.files = []
        if m.get('files') is not None:
            for k1 in m.get('files'):
                temp_model = main_models.GetDigitalEmployeeSkillResponseBodyFiles()
                self.files.append(temp_model.from_map(k1))

        if m.get('remark') is not None:
            self.remark = m.get('remark')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('skillName') is not None:
            self.skill_name = m.get('skillName')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

class GetDigitalEmployeeSkillResponseBodyFiles(DaraModel):
    def __init__(
        self,
        content: str = None,
        name: str = None,
    ):
        self.content = content
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

