# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeAIDBClusterTaskMetricsResponseBody(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        end_time: str = None,
        items: main_models.DescribeAIDBClusterTaskMetricsResponseBodyItems = None,
        metric_type: str = None,
        page_number: int = None,
        page_record_count: int = None,
        page_size: int = None,
        relative_db_cluster_id: str = None,
        request_id: str = None,
        start_time: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.end_time = end_time
        self.items = items
        self.metric_type = metric_type
        self.page_number = page_number
        self.page_record_count = page_record_count
        self.page_size = page_size
        self.relative_db_cluster_id = relative_db_cluster_id
        # Id of the request
        self.request_id = request_id
        self.start_time = start_time

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.items is not None:
            result['Items'] = self.items.to_map()

        if self.metric_type is not None:
            result['MetricType'] = self.metric_type

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.relative_db_cluster_id is not None:
            result['RelativeDbClusterId'] = self.relative_db_cluster_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Items') is not None:
            temp_model = main_models.DescribeAIDBClusterTaskMetricsResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RelativeDbClusterId') is not None:
            self.relative_db_cluster_id = m.get('RelativeDbClusterId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class DescribeAIDBClusterTaskMetricsResponseBodyItems(DaraModel):
    def __init__(
        self,
        sls_metrics_items: List[main_models.DescribeAIDBClusterTaskMetricsResponseBodyItemsSlsMetricsItems] = None,
    ):
        self.sls_metrics_items = sls_metrics_items

    def validate(self):
        if self.sls_metrics_items:
            for v1 in self.sls_metrics_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SlsMetricsItems'] = []
        if self.sls_metrics_items is not None:
            for k1 in self.sls_metrics_items:
                result['SlsMetricsItems'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sls_metrics_items = []
        if m.get('SlsMetricsItems') is not None:
            for k1 in m.get('SlsMetricsItems'):
                temp_model = main_models.DescribeAIDBClusterTaskMetricsResponseBodyItemsSlsMetricsItems()
                self.sls_metrics_items.append(temp_model.from_map(k1))

        return self

class DescribeAIDBClusterTaskMetricsResponseBodyItemsSlsMetricsItems(DaraModel):
    def __init__(
        self,
        current_step: int = None,
        epoch: float = None,
        global_step: int = None,
        log_time: str = None,
        metric: Dict[str, Any] = None,
        metric_type: str = None,
        timestamp: str = None,
    ):
        self.current_step = current_step
        self.epoch = epoch
        self.global_step = global_step
        self.log_time = log_time
        self.metric = metric
        self.metric_type = metric_type
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_step is not None:
            result['CurrentStep'] = self.current_step

        if self.epoch is not None:
            result['Epoch'] = self.epoch

        if self.global_step is not None:
            result['GlobalStep'] = self.global_step

        if self.log_time is not None:
            result['LogTime'] = self.log_time

        if self.metric is not None:
            result['Metric'] = self.metric

        if self.metric_type is not None:
            result['MetricType'] = self.metric_type

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentStep') is not None:
            self.current_step = m.get('CurrentStep')

        if m.get('Epoch') is not None:
            self.epoch = m.get('Epoch')

        if m.get('GlobalStep') is not None:
            self.global_step = m.get('GlobalStep')

        if m.get('LogTime') is not None:
            self.log_time = m.get('LogTime')

        if m.get('Metric') is not None:
            self.metric = m.get('Metric')

        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

