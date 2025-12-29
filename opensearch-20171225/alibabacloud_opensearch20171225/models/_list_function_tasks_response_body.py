# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_opensearch20171225 import models as main_models
from darabonba.model import DaraModel

class ListFunctionTasksResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_code: int = None,
        latency: int = None,
        message: str = None,
        request_id: str = None,
        result: List[main_models.ListFunctionTasksResponseBodyResult] = None,
        status: str = None,
        total_count: int = None,
    ):
        # The error code.
        self.code = code
        # The HTTP status code.
        self.http_code = http_code
        # The time consumed for the request, in milliseconds.
        self.latency = latency
        # The error message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # The returned result.
        self.result = result
        # The status of the request.
        self.status = status
        # The total number of records that meet the requirements.
        self.total_count = total_count

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_code is not None:
            result['HttpCode'] = self.http_code

        if self.latency is not None:
            result['Latency'] = self.latency

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')

        if m.get('Latency') is not None:
            self.latency = m.get('Latency')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListFunctionTasksResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListFunctionTasksResponseBodyResult(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        extend_info: str = None,
        function_name: str = None,
        generation: str = None,
        progress: int = None,
        run_id: str = None,
        start_time: int = None,
        status: str = None,
    ):
        # The timestamp that indicates the end time. Unit: milliseconds. 0 indicates that the task has not ended.
        self.end_time = end_time
        # The value is a JSON string. It includes model evaluation information and training error information.
        self.extend_info = extend_info
        # The name of the feature.
        self.function_name = function_name
        # The number of iterations.
        self.generation = generation
        # The progress. 90 indicates 90%.
        self.progress = progress
        # The ID of the task.
        self.run_id = run_id
        # The timestamp that indicates the start time. Unit: milliseconds.
        self.start_time = start_time
        # The status of the task. Valid values:
        # 
        # *   success
        # *   failed
        # *   running
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info

        if self.function_name is not None:
            result['FunctionName'] = self.function_name

        if self.generation is not None:
            result['Generation'] = self.generation

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.run_id is not None:
            result['RunId'] = self.run_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')

        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')

        if m.get('Generation') is not None:
            self.generation = m.get('Generation')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('RunId') is not None:
            self.run_id = m.get('RunId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

