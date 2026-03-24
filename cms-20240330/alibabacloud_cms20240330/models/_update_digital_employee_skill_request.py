# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class UpdateDigitalEmployeeSkillRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        display_name: str = None,
        enable: bool = None,
        files: List[main_models.UpdateDigitalEmployeeSkillRequestFiles] = None,
        remark: str = None,
    ):
        # Description
        self.description = description
        # Display name
        self.display_name = display_name
        # Is enabled
        # 
        # This parameter is required.
        self.enable = enable
        # List of skill files
        # 
        # This parameter is required.
        self.files = files
        # Remark
        self.remark = remark

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('enable') is not None:
            self.enable = m.get('enable')

        self.files = []
        if m.get('files') is not None:
            for k1 in m.get('files'):
                temp_model = main_models.UpdateDigitalEmployeeSkillRequestFiles()
                self.files.append(temp_model.from_map(k1))

        if m.get('remark') is not None:
            self.remark = m.get('remark')

        return self

class UpdateDigitalEmployeeSkillRequestFiles(DaraModel):
    def __init__(
        self,
        content: str = None,
        name: str = None,
    ):
        # File content
        self.content = content
        # File name
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

