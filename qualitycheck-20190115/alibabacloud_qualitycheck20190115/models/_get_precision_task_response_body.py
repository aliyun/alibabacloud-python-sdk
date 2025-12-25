# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_qualitycheck20190115 import models as main_models
from darabonba.model import DaraModel

class GetPrecisionTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetPrecisionTaskResponseBodyData = None,
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
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

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

        if m.get('Data') is not None:
            temp_model = main_models.GetPrecisionTaskResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetPrecisionTaskResponseBodyData(DaraModel):
    def __init__(
        self,
        data_set_id: int = None,
        data_set_name: str = None,
        duration: int = None,
        incorrect_words: int = None,
        name: str = None,
        precisions: main_models.GetPrecisionTaskResponseBodyDataPrecisions = None,
        source: int = None,
        status: int = None,
        task_id: str = None,
        total_count: int = None,
        update_time: str = None,
        verified_count: int = None,
    ):
        self.data_set_id = data_set_id
        self.data_set_name = data_set_name
        self.duration = duration
        self.incorrect_words = incorrect_words
        self.name = name
        self.precisions = precisions
        self.source = source
        self.status = status
        self.task_id = task_id
        self.total_count = total_count
        self.update_time = update_time
        self.verified_count = verified_count

    def validate(self):
        if self.precisions:
            self.precisions.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_set_id is not None:
            result['DataSetId'] = self.data_set_id

        if self.data_set_name is not None:
            result['DataSetName'] = self.data_set_name

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.incorrect_words is not None:
            result['IncorrectWords'] = self.incorrect_words

        if self.name is not None:
            result['Name'] = self.name

        if self.precisions is not None:
            result['Precisions'] = self.precisions.to_map()

        if self.source is not None:
            result['Source'] = self.source

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.verified_count is not None:
            result['VerifiedCount'] = self.verified_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSetId') is not None:
            self.data_set_id = m.get('DataSetId')

        if m.get('DataSetName') is not None:
            self.data_set_name = m.get('DataSetName')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('IncorrectWords') is not None:
            self.incorrect_words = m.get('IncorrectWords')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Precisions') is not None:
            temp_model = main_models.GetPrecisionTaskResponseBodyDataPrecisions()
            self.precisions = temp_model.from_map(m.get('Precisions'))

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('VerifiedCount') is not None:
            self.verified_count = m.get('VerifiedCount')

        return self

class GetPrecisionTaskResponseBodyDataPrecisions(DaraModel):
    def __init__(
        self,
        precision: List[main_models.GetPrecisionTaskResponseBodyDataPrecisionsPrecision] = None,
    ):
        self.precision = precision

    def validate(self):
        if self.precision:
            for v1 in self.precision:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Precision'] = []
        if self.precision is not None:
            for k1 in self.precision:
                result['Precision'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.precision = []
        if m.get('Precision') is not None:
            for k1 in m.get('Precision'):
                temp_model = main_models.GetPrecisionTaskResponseBodyDataPrecisionsPrecision()
                self.precision.append(temp_model.from_map(k1))

        return self

class GetPrecisionTaskResponseBodyDataPrecisionsPrecision(DaraModel):
    def __init__(
        self,
        model_id: int = None,
        model_name: str = None,
        precision: float = None,
        status: int = None,
        task_id: str = None,
    ):
        self.model_id = model_id
        self.model_name = model_name
        self.precision = precision
        self.status = status
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_id is not None:
            result['ModelId'] = self.model_id

        if self.model_name is not None:
            result['ModelName'] = self.model_name

        if self.precision is not None:
            result['Precision'] = self.precision

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')

        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        if m.get('Precision') is not None:
            self.precision = m.get('Precision')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

