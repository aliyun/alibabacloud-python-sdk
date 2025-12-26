# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_lingmou20250527 import models as main_models
from darabonba.model import DaraModel

class BroadcastTemplate(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        id: str = None,
        modified_time: str = None,
        name: str = None,
        variables: List[main_models.TemplateVariable] = None,
    ):
        self.create_time = create_time
        self.id = id
        self.modified_time = modified_time
        self.name = name
        self.variables = variables

    def validate(self):
        if self.variables:
            for v1 in self.variables:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.id is not None:
            result['id'] = self.id

        if self.modified_time is not None:
            result['modifiedTime'] = self.modified_time

        if self.name is not None:
            result['name'] = self.name

        result['variables'] = []
        if self.variables is not None:
            for k1 in self.variables:
                result['variables'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('modifiedTime') is not None:
            self.modified_time = m.get('modifiedTime')

        if m.get('name') is not None:
            self.name = m.get('name')

        self.variables = []
        if m.get('variables') is not None:
            for k1 in m.get('variables'):
                temp_model = main_models.TemplateVariable()
                self.variables.append(temp_model.from_map(k1))

        return self

