# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeSparkSQLDiagnosisAttributeResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        app_id: str = None,
        diagnosis_infos: List[main_models.Adb4MysqlSparkDiagnosisInfo] = None,
        elapsed_time: int = None,
        inner_query_id: int = None,
        operator_list_sorted_by_metrics: main_models.DescribeSparkSQLDiagnosisAttributeResponseBodyOperatorListSortedByMetrics = None,
        request_id: str = None,
        root: main_models.OperatorNode = None,
    ):
        # The information about the request denial.
        self.access_denied_detail = access_denied_detail
        # The application ID.
        # 
        # >  You can call the [ListSparkApps](https://help.aliyun.com/document_detail/612475.html) operation to query a list of Spark application IDs.
        self.app_id = app_id
        # The queried diagnostic information.
        self.diagnosis_infos = diagnosis_infos
        # The execution duration of the query. Unit: milliseconds.
        self.elapsed_time = elapsed_time
        # The ID of the query executed within the Spark application.
        self.inner_query_id = inner_query_id
        # The operators sorted by metrics.
        self.operator_list_sorted_by_metrics = operator_list_sorted_by_metrics
        # The request ID.
        self.request_id = request_id
        # The Spark execution plan tree.
        self.root = root

    def validate(self):
        if self.diagnosis_infos:
            for v1 in self.diagnosis_infos:
                 if v1:
                    v1.validate()
        if self.operator_list_sorted_by_metrics:
            self.operator_list_sorted_by_metrics.validate()
        if self.root:
            self.root.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.app_id is not None:
            result['AppId'] = self.app_id

        result['DiagnosisInfos'] = []
        if self.diagnosis_infos is not None:
            for k1 in self.diagnosis_infos:
                result['DiagnosisInfos'].append(k1.to_map() if k1 else None)

        if self.elapsed_time is not None:
            result['ElapsedTime'] = self.elapsed_time

        if self.inner_query_id is not None:
            result['InnerQueryId'] = self.inner_query_id

        if self.operator_list_sorted_by_metrics is not None:
            result['OperatorListSortedByMetrics'] = self.operator_list_sorted_by_metrics.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.root is not None:
            result['Root'] = self.root.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        self.diagnosis_infos = []
        if m.get('DiagnosisInfos') is not None:
            for k1 in m.get('DiagnosisInfos'):
                temp_model = main_models.Adb4MysqlSparkDiagnosisInfo()
                self.diagnosis_infos.append(temp_model.from_map(k1))

        if m.get('ElapsedTime') is not None:
            self.elapsed_time = m.get('ElapsedTime')

        if m.get('InnerQueryId') is not None:
            self.inner_query_id = m.get('InnerQueryId')

        if m.get('OperatorListSortedByMetrics') is not None:
            temp_model = main_models.DescribeSparkSQLDiagnosisAttributeResponseBodyOperatorListSortedByMetrics()
            self.operator_list_sorted_by_metrics = temp_model.from_map(m.get('OperatorListSortedByMetrics'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Root') is not None:
            temp_model = main_models.OperatorNode()
            self.root = temp_model.from_map(m.get('Root'))

        return self

class DescribeSparkSQLDiagnosisAttributeResponseBodyOperatorListSortedByMetrics(DaraModel):
    def __init__(
        self,
        operator_list_sorted_by_exclusive_time: List[main_models.SparkOperatorInfo] = None,
        operator_list_sorted_by_max_memory: List[main_models.SparkOperatorInfo] = None,
    ):
        # The operators sorted by the execution duration.
        self.operator_list_sorted_by_exclusive_time = operator_list_sorted_by_exclusive_time
        # The operators sorted by the maximum memory used.
        self.operator_list_sorted_by_max_memory = operator_list_sorted_by_max_memory

    def validate(self):
        if self.operator_list_sorted_by_exclusive_time:
            for v1 in self.operator_list_sorted_by_exclusive_time:
                 if v1:
                    v1.validate()
        if self.operator_list_sorted_by_max_memory:
            for v1 in self.operator_list_sorted_by_max_memory:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['OperatorListSortedByExclusiveTime'] = []
        if self.operator_list_sorted_by_exclusive_time is not None:
            for k1 in self.operator_list_sorted_by_exclusive_time:
                result['OperatorListSortedByExclusiveTime'].append(k1.to_map() if k1 else None)

        result['OperatorListSortedByMaxMemory'] = []
        if self.operator_list_sorted_by_max_memory is not None:
            for k1 in self.operator_list_sorted_by_max_memory:
                result['OperatorListSortedByMaxMemory'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.operator_list_sorted_by_exclusive_time = []
        if m.get('OperatorListSortedByExclusiveTime') is not None:
            for k1 in m.get('OperatorListSortedByExclusiveTime'):
                temp_model = main_models.SparkOperatorInfo()
                self.operator_list_sorted_by_exclusive_time.append(temp_model.from_map(k1))

        self.operator_list_sorted_by_max_memory = []
        if m.get('OperatorListSortedByMaxMemory') is not None:
            for k1 in m.get('OperatorListSortedByMaxMemory'):
                temp_model = main_models.SparkOperatorInfo()
                self.operator_list_sorted_by_max_memory.append(temp_model.from_map(k1))

        return self

