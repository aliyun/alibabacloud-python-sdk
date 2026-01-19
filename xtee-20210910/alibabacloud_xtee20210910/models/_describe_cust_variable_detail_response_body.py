# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeCustVariableDetailResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_object: List[main_models.DescribeCustVariableDetailResponseBodyResultObject] = None,
    ):
        # Request ID
        self.request_id = request_id
        # Return object
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            for v1 in self.result_object:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['resultObject'] = []
        if self.result_object is not None:
            for k1 in self.result_object:
                result['resultObject'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result_object = []
        if m.get('resultObject') is not None:
            for k1 in m.get('resultObject'):
                temp_model = main_models.DescribeCustVariableDetailResponseBodyResultObject()
                self.result_object.append(temp_model.from_map(k1))

        return self

class DescribeCustVariableDetailResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        condition: str = None,
        data_version: int = None,
        description: str = None,
        event_codes: str = None,
        history_value_type: str = None,
        id: int = None,
        object: str = None,
        outputs: str = None,
        subject: str = None,
        time_type: str = None,
        title: str = None,
        tw_count: str = None,
        velocity_fc: str = None,
        velocity_tw: str = None,
    ):
        # Condition value.
        self.condition = condition
        # Data version.
        self.data_version = data_version
        # Description information.
        self.description = description
        # Event code.
        self.event_codes = event_codes
        # Value type
        self.history_value_type = history_value_type
        # Primary key ID of the cumulative variable
        self.id = id
        # Cumulative object
        self.object = object
        # Variable return type
        self.outputs = outputs
        # Main object
        self.subject = subject
        # Time slice type
        self.time_type = time_type
        # Title.
        self.title = title
        # Time count
        self.tw_count = tw_count
        # Variable type
        self.velocity_fc = velocity_fc
        # Time slice unit
        self.velocity_tw = velocity_tw

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.condition is not None:
            result['condition'] = self.condition

        if self.data_version is not None:
            result['dataVersion'] = self.data_version

        if self.description is not None:
            result['description'] = self.description

        if self.event_codes is not None:
            result['eventCodes'] = self.event_codes

        if self.history_value_type is not None:
            result['historyValueType'] = self.history_value_type

        if self.id is not None:
            result['id'] = self.id

        if self.object is not None:
            result['object'] = self.object

        if self.outputs is not None:
            result['outputs'] = self.outputs

        if self.subject is not None:
            result['subject'] = self.subject

        if self.time_type is not None:
            result['timeType'] = self.time_type

        if self.title is not None:
            result['title'] = self.title

        if self.tw_count is not None:
            result['twCount'] = self.tw_count

        if self.velocity_fc is not None:
            result['velocityFC'] = self.velocity_fc

        if self.velocity_tw is not None:
            result['velocityTW'] = self.velocity_tw

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('condition') is not None:
            self.condition = m.get('condition')

        if m.get('dataVersion') is not None:
            self.data_version = m.get('dataVersion')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('eventCodes') is not None:
            self.event_codes = m.get('eventCodes')

        if m.get('historyValueType') is not None:
            self.history_value_type = m.get('historyValueType')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('object') is not None:
            self.object = m.get('object')

        if m.get('outputs') is not None:
            self.outputs = m.get('outputs')

        if m.get('subject') is not None:
            self.subject = m.get('subject')

        if m.get('timeType') is not None:
            self.time_type = m.get('timeType')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('twCount') is not None:
            self.tw_count = m.get('twCount')

        if m.get('velocityFC') is not None:
            self.velocity_fc = m.get('velocityFC')

        if m.get('velocityTW') is not None:
            self.velocity_tw = m.get('velocityTW')

        return self

