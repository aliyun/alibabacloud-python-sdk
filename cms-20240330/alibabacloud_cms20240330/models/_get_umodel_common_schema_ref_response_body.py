# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class GetUmodelCommonSchemaRefResponseBody(DaraModel):
    def __init__(
        self,
        common_schema_ref: List[main_models.GetUmodelCommonSchemaRefResponseBodyCommonSchemaRef] = None,
    ):
        self.common_schema_ref = common_schema_ref

    def validate(self):
        if self.common_schema_ref:
            for v1 in self.common_schema_ref:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['commonSchemaRef'] = []
        if self.common_schema_ref is not None:
            for k1 in self.common_schema_ref:
                result['commonSchemaRef'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.common_schema_ref = []
        if m.get('commonSchemaRef') is not None:
            for k1 in m.get('commonSchemaRef'):
                temp_model = main_models.GetUmodelCommonSchemaRefResponseBodyCommonSchemaRef()
                self.common_schema_ref.append(temp_model.from_map(k1))

        return self

class GetUmodelCommonSchemaRefResponseBodyCommonSchemaRef(DaraModel):
    def __init__(
        self,
        group: str = None,
        version: str = None,
    ):
        self.group = group
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group is not None:
            result['group'] = self.group

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('group') is not None:
            self.group = m.get('group')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

