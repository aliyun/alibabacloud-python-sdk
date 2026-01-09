# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiccs20191015 import models as main_models
from darabonba.model import DaraModel

class GetQualityProjectLogResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.GetQualityProjectLogResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

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
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetQualityProjectLogResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetQualityProjectLogResponseBodyData(DaraModel):
    def __init__(
        self,
        action_data: str = None,
        action_time: str = None,
        action_type: str = None,
        project_create_time: str = None,
        project_id: int = None,
    ):
        self.action_data = action_data
        self.action_time = action_time
        self.action_type = action_type
        self.project_create_time = project_create_time
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_data is not None:
            result['ActionData'] = self.action_data

        if self.action_time is not None:
            result['ActionTime'] = self.action_time

        if self.action_type is not None:
            result['ActionType'] = self.action_type

        if self.project_create_time is not None:
            result['ProjectCreateTime'] = self.project_create_time

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionData') is not None:
            self.action_data = m.get('ActionData')

        if m.get('ActionTime') is not None:
            self.action_time = m.get('ActionTime')

        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')

        if m.get('ProjectCreateTime') is not None:
            self.project_create_time = m.get('ProjectCreateTime')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

