# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeExecutorDetectionResponseBody(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        detection_items: List[main_models.DescribeExecutorDetectionResponseBodyDetectionItems] = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition cluster.
        self.dbcluster_id = dbcluster_id
        # The queried detection items and detection results.
        self.detection_items = detection_items
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.detection_items:
            for v1 in self.detection_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        result['DetectionItems'] = []
        if self.detection_items is not None:
            for k1 in self.detection_items:
                result['DetectionItems'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        self.detection_items = []
        if m.get('DetectionItems') is not None:
            for k1 in m.get('DetectionItems'):
                temp_model = main_models.DescribeExecutorDetectionResponseBodyDetectionItems()
                self.detection_items.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeExecutorDetectionResponseBodyDetectionItems(DaraModel):
    def __init__(
        self,
        message: str = None,
        name: str = None,
        results: main_models.DescribeExecutorDetectionResponseBodyDetectionItemsResults = None,
        status: str = None,
    ):
        # The information about the detection result.
        self.message = message
        # The name of the detection item.
        self.name = name
        # The detection result items.
        self.results = results
        # The severity level of the detection result. Valid values:
        # 
        # *   NORMAL
        # *   WARNING
        # *   CRITICAL
        self.status = status

    def validate(self):
        if self.results:
            self.results.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['Message'] = self.message

        if self.name is not None:
            result['Name'] = self.name

        if self.results is not None:
            result['Results'] = self.results.to_map()

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Results') is not None:
            temp_model = main_models.DescribeExecutorDetectionResponseBodyDetectionItemsResults()
            self.results = temp_model.from_map(m.get('Results'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeExecutorDetectionResponseBodyDetectionItemsResults(DaraModel):
    def __init__(
        self,
        operator_agg: List[main_models.DescribeExecutorDetectionResponseBodyDetectionItemsResultsOperatorAgg] = None,
        operator_details: List[main_models.DescribeExecutorDetectionResponseBodyDetectionItemsResultsOperatorDetails] = None,
    ):
        # The detection result items of operator metric aggregation.
        self.operator_agg = operator_agg
        # The detection result items of abnormal operators.
        self.operator_details = operator_details

    def validate(self):
        if self.operator_agg:
            for v1 in self.operator_agg:
                 if v1:
                    v1.validate()
        if self.operator_details:
            for v1 in self.operator_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['OperatorAgg'] = []
        if self.operator_agg is not None:
            for k1 in self.operator_agg:
                result['OperatorAgg'].append(k1.to_map() if k1 else None)

        result['OperatorDetails'] = []
        if self.operator_details is not None:
            for k1 in self.operator_details:
                result['OperatorDetails'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.operator_agg = []
        if m.get('OperatorAgg') is not None:
            for k1 in m.get('OperatorAgg'):
                temp_model = main_models.DescribeExecutorDetectionResponseBodyDetectionItemsResultsOperatorAgg()
                self.operator_agg.append(temp_model.from_map(k1))

        self.operator_details = []
        if m.get('OperatorDetails') is not None:
            for k1 in m.get('OperatorDetails'):
                temp_model = main_models.DescribeExecutorDetectionResponseBodyDetectionItemsResultsOperatorDetails()
                self.operator_details.append(temp_model.from_map(k1))

        return self

class DescribeExecutorDetectionResponseBodyDetectionItemsResultsOperatorDetails(DaraModel):
    def __init__(
        self,
        metric_name: str = None,
        search_results: List[main_models.DescribeExecutorDetectionResponseBodyDetectionItemsResultsOperatorDetailsSearchResults] = None,
    ):
        # The name of the detection metric.
        self.metric_name = metric_name
        # The detection result items of abnormal operators.
        self.search_results = search_results

    def validate(self):
        if self.search_results:
            for v1 in self.search_results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        result['SearchResults'] = []
        if self.search_results is not None:
            for k1 in self.search_results:
                result['SearchResults'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        self.search_results = []
        if m.get('SearchResults') is not None:
            for k1 in m.get('SearchResults'):
                temp_model = main_models.DescribeExecutorDetectionResponseBodyDetectionItemsResultsOperatorDetailsSearchResults()
                self.search_results.append(temp_model.from_map(k1))

        return self

class DescribeExecutorDetectionResponseBodyDetectionItemsResultsOperatorDetailsSearchResults(DaraModel):
    def __init__(
        self,
        input_rows: int = None,
        input_size: int = None,
        operator_cost: float = None,
        operator_info: str = None,
        operator_name: str = None,
        output_rows: int = None,
        output_size: int = None,
        peak_memory: int = None,
        process_id: str = None,
        stage_id: str = None,
    ):
        # The number of rows input by the operator.
        self.input_rows = input_rows
        # The amount of data input by the operator. Unit: bytes.
        self.input_size = input_size
        # The total CPU time consumed by all operators in the stage, which is equivalent to the total CPU time of the stage. You can use this parameter to determine which parts of the stage consume a large amount of computing resources. Unit: milliseconds.
        self.operator_cost = operator_cost
        # The property information about the operator.
        self.operator_info = operator_info
        # The name of the operator.
        self.operator_name = operator_name
        # The number of rows output by the operator.
        self.output_rows = output_rows
        # The amount of data output by the operator. Unit: bytes.
        self.output_size = output_size
        # The peak memory. Unit: bytes.
        self.peak_memory = peak_memory
        # The query ID.
        self.process_id = process_id
        # The stage ID.
        self.stage_id = stage_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_rows is not None:
            result['InputRows'] = self.input_rows

        if self.input_size is not None:
            result['InputSize'] = self.input_size

        if self.operator_cost is not None:
            result['OperatorCost'] = self.operator_cost

        if self.operator_info is not None:
            result['OperatorInfo'] = self.operator_info

        if self.operator_name is not None:
            result['OperatorName'] = self.operator_name

        if self.output_rows is not None:
            result['OutputRows'] = self.output_rows

        if self.output_size is not None:
            result['OutputSize'] = self.output_size

        if self.peak_memory is not None:
            result['PeakMemory'] = self.peak_memory

        if self.process_id is not None:
            result['ProcessId'] = self.process_id

        if self.stage_id is not None:
            result['StageId'] = self.stage_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputRows') is not None:
            self.input_rows = m.get('InputRows')

        if m.get('InputSize') is not None:
            self.input_size = m.get('InputSize')

        if m.get('OperatorCost') is not None:
            self.operator_cost = m.get('OperatorCost')

        if m.get('OperatorInfo') is not None:
            self.operator_info = m.get('OperatorInfo')

        if m.get('OperatorName') is not None:
            self.operator_name = m.get('OperatorName')

        if m.get('OutputRows') is not None:
            self.output_rows = m.get('OutputRows')

        if m.get('OutputSize') is not None:
            self.output_size = m.get('OutputSize')

        if m.get('PeakMemory') is not None:
            self.peak_memory = m.get('PeakMemory')

        if m.get('ProcessId') is not None:
            self.process_id = m.get('ProcessId')

        if m.get('StageId') is not None:
            self.stage_id = m.get('StageId')

        return self

class DescribeExecutorDetectionResponseBodyDetectionItemsResultsOperatorAgg(DaraModel):
    def __init__(
        self,
        metric_name: str = None,
        search_results: List[main_models.DescribeExecutorDetectionResponseBodyDetectionItemsResultsOperatorAggSearchResults] = None,
    ):
        # The name of the detection metric.
        self.metric_name = metric_name
        # The detection result items of operator metric aggregation.
        self.search_results = search_results

    def validate(self):
        if self.search_results:
            for v1 in self.search_results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        result['SearchResults'] = []
        if self.search_results is not None:
            for k1 in self.search_results:
                result['SearchResults'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        self.search_results = []
        if m.get('SearchResults') is not None:
            for k1 in m.get('SearchResults'):
                temp_model = main_models.DescribeExecutorDetectionResponseBodyDetectionItemsResultsOperatorAggSearchResults()
                self.search_results.append(temp_model.from_map(k1))

        return self

class DescribeExecutorDetectionResponseBodyDetectionItemsResultsOperatorAggSearchResults(DaraModel):
    def __init__(
        self,
        avg_value: float = None,
        max_value: int = None,
        operator_count: int = None,
        operator_name: str = None,
        total_value: int = None,
    ):
        # The average value of the operator metric.
        self.avg_value = avg_value
        # The maximum value of the operator metric.
        self.max_value = max_value
        # The number of occurrences of the operator.
        self.operator_count = operator_count
        # The name of the operator.
        self.operator_name = operator_name
        # The cumulative value of the operator metric.
        self.total_value = total_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avg_value is not None:
            result['AvgValue'] = self.avg_value

        if self.max_value is not None:
            result['MaxValue'] = self.max_value

        if self.operator_count is not None:
            result['OperatorCount'] = self.operator_count

        if self.operator_name is not None:
            result['OperatorName'] = self.operator_name

        if self.total_value is not None:
            result['TotalValue'] = self.total_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvgValue') is not None:
            self.avg_value = m.get('AvgValue')

        if m.get('MaxValue') is not None:
            self.max_value = m.get('MaxValue')

        if m.get('OperatorCount') is not None:
            self.operator_count = m.get('OperatorCount')

        if m.get('OperatorName') is not None:
            self.operator_name = m.get('OperatorName')

        if m.get('TotalValue') is not None:
            self.total_value = m.get('TotalValue')

        return self

