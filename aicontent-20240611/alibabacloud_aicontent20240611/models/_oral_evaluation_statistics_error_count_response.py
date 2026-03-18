# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aicontent20240611 import models as main_models
from darabonba.model import DaraModel

class OralEvaluationStatisticsErrorCountResponse(DaraModel):
    def __init__(
        self,
        project_data: main_models.OralEvaluationStatisticsErrorCountResponseProjectData = None,
        project_id: str = None,
    ):
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
            result['ProjectData'] = self.project_data.to_map()

        if self.project_id is not None:
            result['projectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectData') is not None:
            temp_model = main_models.OralEvaluationStatisticsErrorCountResponseProjectData()
            self.project_data = temp_model.from_map(m.get('ProjectData'))

        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')

        return self

class OralEvaluationStatisticsErrorCountResponseProjectData(DaraModel):
    def __init__(
        self,
        application_data: List[main_models.OralEvaluationStatisticsErrorCountResponseProjectDataApplicationData] = None,
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
                temp_model = main_models.OralEvaluationStatisticsErrorCountResponseProjectDataApplicationData()
                self.application_data.append(temp_model.from_map(k1))

        if m.get('applicationInternalId') is not None:
            self.application_internal_id = m.get('applicationInternalId')

        return self

class OralEvaluationStatisticsErrorCountResponseProjectDataApplicationData(DaraModel):
    def __init__(
        self,
        data: List[main_models.OralEvaluationStatisticsErrorCountResponseProjectDataApplicationDataData] = None,
        application_access_id: str = None,
    ):
        self.data = data
        # appId,appkey
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
                temp_model = main_models.OralEvaluationStatisticsErrorCountResponseProjectDataApplicationDataData()
                self.data.append(temp_model.from_map(k1))

        if m.get('applicationAccessId') is not None:
            self.application_access_id = m.get('applicationAccessId')

        return self

class OralEvaluationStatisticsErrorCountResponseProjectDataApplicationDataData(DaraModel):
    def __init__(
        self,
        data: List[main_models.OralEvaluationStatisticsErrorCountResponseProjectDataApplicationDataDataData] = None,
        error_code: str = None,
        error_message: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message

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

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.OralEvaluationStatisticsErrorCountResponseProjectDataApplicationDataDataData()
                self.data.append(temp_model.from_map(k1))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        return self

class OralEvaluationStatisticsErrorCountResponseProjectDataApplicationDataDataData(DaraModel):
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

