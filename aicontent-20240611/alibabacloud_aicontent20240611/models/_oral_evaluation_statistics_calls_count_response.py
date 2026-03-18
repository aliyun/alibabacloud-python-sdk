# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aicontent20240611 import models as main_models
from darabonba.model import DaraModel

class OralEvaluationStatisticsCallsCountResponse(DaraModel):
    def __init__(
        self,
        project_data: main_models.OralEvaluationStatisticsCallsCountResponseProjectData = None,
        project_id: str = None,
    ):
        # This parameter is required.
        self.project_data = project_data
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        if self.project_data:
            self.project_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.project_data is not None:
            result['projectData'] = self.project_data.to_map()

        if self.project_id is not None:
            result['projectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('projectData') is not None:
            temp_model = main_models.OralEvaluationStatisticsCallsCountResponseProjectData()
            self.project_data = temp_model.from_map(m.get('projectData'))

        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')

        return self

class OralEvaluationStatisticsCallsCountResponseProjectData(DaraModel):
    def __init__(
        self,
        application_data: List[main_models.OralEvaluationStatisticsCallsCountResponseProjectDataApplicationData] = None,
        application_internal_id: str = None,
    ):
        self.application_data = application_data
        # This parameter is required.
        self.application_internal_id = application_internal_id

    def validate(self):
        if self.application_data:
            for v1 in self.application_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ApplicationData'] = []
        if self.application_data is not None:
            for k1 in self.application_data:
                result['ApplicationData'].append(k1.to_map() if k1 else None)

        if self.application_internal_id is not None:
            result['applicationInternalId'] = self.application_internal_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.application_data = []
        if m.get('ApplicationData') is not None:
            for k1 in m.get('ApplicationData'):
                temp_model = main_models.OralEvaluationStatisticsCallsCountResponseProjectDataApplicationData()
                self.application_data.append(temp_model.from_map(k1))

        if m.get('applicationInternalId') is not None:
            self.application_internal_id = m.get('applicationInternalId')

        return self

class OralEvaluationStatisticsCallsCountResponseProjectDataApplicationData(DaraModel):
    def __init__(
        self,
        data: List[main_models.OralEvaluationStatisticsCallsCountResponseProjectDataApplicationDataData] = None,
        application_access_id: str = None,
    ):
        self.data = data
        # appkey
        # 
        # This parameter is required.
        self.application_access_id = application_access_id

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
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.application_access_id is not None:
            result['applicationAccessId'] = self.application_access_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.OralEvaluationStatisticsCallsCountResponseProjectDataApplicationDataData()
                self.data.append(temp_model.from_map(k1))

        if m.get('applicationAccessId') is not None:
            self.application_access_id = m.get('applicationAccessId')

        return self

class OralEvaluationStatisticsCallsCountResponseProjectDataApplicationDataData(DaraModel):
    def __init__(
        self,
        count: int = None,
        name: str = None,
    ):
        # This parameter is required.
        self.count = count
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['count'] = self.count

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

