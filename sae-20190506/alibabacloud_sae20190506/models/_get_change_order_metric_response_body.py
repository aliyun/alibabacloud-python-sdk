# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class GetChangeOrderMetricResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.GetChangeOrderMetricResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code. The following limits are imposed on the ID:
        # 
        # *   **2xx**: The call was successful.
        # *   **3xx**: The call was redirected.
        # *   **4xx**: The call failed.
        # *   **5xx**: A server error occurred.
        self.code = code
        # The details of applications.
        self.data = data
        # The additional information that is returned. The following limits are imposed on the ID:
        # 
        # *   success: If the call is successful, **success** is returned.
        # *   An error code: If the call fails, an error code is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the microservice list was obtained. The following limits are imposed on the ID:
        # 
        # *   **true**: The namespaces were obtained.
        # *   **false**: no
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
                temp_model = main_models.GetChangeOrderMetricResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetChangeOrderMetricResponseBodyData(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        avg_time_cost_ms: float = None,
        error: int = None,
        error_percent: float = None,
        max_time_cost_ms: float = None,
        name: str = None,
        optimize_suggestions: str = None,
        region_id: str = None,
        task_time_cost_ms_avg: str = None,
        total: int = None,
    ):
        # The application ID.
        self.app_id = app_id
        self.avg_time_cost_ms = avg_time_cost_ms
        # The number of abnormal change orders.
        self.error = error
        # The percentage of change failures.
        self.error_percent = error_percent
        self.max_time_cost_ms = max_time_cost_ms
        # The application name.
        self.name = name
        self.optimize_suggestions = optimize_suggestions
        # The namespace ID.
        self.region_id = region_id
        self.task_time_cost_ms_avg = task_time_cost_ms_avg
        # The total number of change orders.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.avg_time_cost_ms is not None:
            result['AvgTimeCostMs'] = self.avg_time_cost_ms

        if self.error is not None:
            result['Error'] = self.error

        if self.error_percent is not None:
            result['ErrorPercent'] = self.error_percent

        if self.max_time_cost_ms is not None:
            result['MaxTimeCostMs'] = self.max_time_cost_ms

        if self.name is not None:
            result['Name'] = self.name

        if self.optimize_suggestions is not None:
            result['OptimizeSuggestions'] = self.optimize_suggestions

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.task_time_cost_ms_avg is not None:
            result['TaskTimeCostMsAvg'] = self.task_time_cost_ms_avg

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AvgTimeCostMs') is not None:
            self.avg_time_cost_ms = m.get('AvgTimeCostMs')

        if m.get('Error') is not None:
            self.error = m.get('Error')

        if m.get('ErrorPercent') is not None:
            self.error_percent = m.get('ErrorPercent')

        if m.get('MaxTimeCostMs') is not None:
            self.max_time_cost_ms = m.get('MaxTimeCostMs')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OptimizeSuggestions') is not None:
            self.optimize_suggestions = m.get('OptimizeSuggestions')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TaskTimeCostMsAvg') is not None:
            self.task_time_cost_ms_avg = m.get('TaskTimeCostMsAvg')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

