# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_airegistry20260317 import models as main_models
from darabonba.model import DaraModel

class GetSkillVersionDetailResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetSkillVersionDetailResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetSkillVersionDetailResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetSkillVersionDetailResponseBodyData(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        namespace_id: str = None,
        resource: Dict[str, main_models.DataResourceValue] = None,
        skill_md: str = None,
    ):
        self.description = description
        self.name = name
        self.namespace_id = namespace_id
        self.resource = resource
        self.skill_md = skill_md

    def validate(self):
        if self.resource:
            for v1 in self.resource.values():
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        result['Resource'] = {}
        if self.resource is not None:
            for k1, v1 in self.resource.items():
                result['Resource'][k1] = v1.to_map() if v1 else None

        if self.skill_md is not None:
            result['SkillMd'] = self.skill_md

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        self.resource = {}
        if m.get('Resource') is not None:
            for k1, v1 in m.get('Resource').items():
                temp_model = main_models.DataResourceValue()
                self.resource[k1] = temp_model.from_map(v1)

        if m.get('SkillMd') is not None:
            self.skill_md = m.get('SkillMd')

        return self

