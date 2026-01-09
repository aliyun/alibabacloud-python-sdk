# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiccs20191015 import models as main_models
from darabonba.model import DaraModel

class EditQualityRuleTagRequest(DaraModel):
    def __init__(
        self,
        analysis_types: List[main_models.EditQualityRuleTagRequestAnalysisTypes] = None,
        instance_id: str = None,
    ):
        # This parameter is required.
        self.analysis_types = analysis_types
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        if self.analysis_types:
            for v1 in self.analysis_types:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AnalysisTypes'] = []
        if self.analysis_types is not None:
            for k1 in self.analysis_types:
                result['AnalysisTypes'].append(k1.to_map() if k1 else None)

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.analysis_types = []
        if m.get('AnalysisTypes') is not None:
            for k1 in m.get('AnalysisTypes'):
                temp_model = main_models.EditQualityRuleTagRequestAnalysisTypes()
                self.analysis_types.append(temp_model.from_map(k1))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

class EditQualityRuleTagRequestAnalysisTypes(DaraModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
    ):
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

