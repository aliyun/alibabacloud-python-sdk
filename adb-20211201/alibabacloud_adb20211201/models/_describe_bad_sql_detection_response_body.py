# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeBadSqlDetectionResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        dbcluster_id: str = None,
        detection_items: List[main_models.DescribeBadSqlDetectionResponseBodyDetectionItems] = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # The information about the request denial.
        self.access_denied_detail = access_denied_detail
        # The cluster ID.
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

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
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        self.detection_items = []
        if m.get('DetectionItems') is not None:
            for k1 in m.get('DetectionItems'):
                temp_model = main_models.DescribeBadSqlDetectionResponseBodyDetectionItems()
                self.detection_items.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeBadSqlDetectionResponseBodyDetectionItems(DaraModel):
    def __init__(
        self,
        message: str = None,
        name: str = None,
        results: List[main_models.DescribeBadSqlDetectionResponseBodyDetectionItemsResults] = None,
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
            for v1 in self.results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['Message'] = self.message

        if self.name is not None:
            result['Name'] = self.name

        result['Results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['Results'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.results = []
        if m.get('Results') is not None:
            for k1 in m.get('Results'):
                temp_model = main_models.DescribeBadSqlDetectionResponseBodyDetectionItemsResults()
                self.results.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeBadSqlDetectionResponseBodyDetectionItemsResults(DaraModel):
    def __init__(
        self,
        cost: int = None,
        diagnosis_results: List[main_models.DescribeBadSqlDetectionResponseBodyDetectionItemsResultsDiagnosisResults] = None,
        operator_cost: int = None,
        output_data_size: int = None,
        pattern_id: str = None,
        peak_memory: int = None,
        process_id: str = None,
        sql: str = None,
        scan_size: int = None,
        start_time: str = None,
        total_stages: int = None,
    ):
        # The total execution duration. Unit: milliseconds.
        # 
        # >  This value is the cumulative value of the `QueuedTime`, `TotalPlanningTime`, and `ExecutionTime` parameters.
        self.cost = cost
        # The diagnostic result items.
        self.diagnosis_results = diagnosis_results
        # The total CPU time consumed by all operators in the stage, which is equivalent to the total CPU time of the stage. You can use this parameter to determine which parts of the stage consume a large amount of computing resources. Unit: milliseconds.
        self.operator_cost = operator_cost
        # The amount of returned data. Unit: bytes.
        self.output_data_size = output_data_size
        # The SQL pattern ID.
        self.pattern_id = pattern_id
        # The peak memory. Unit: bytes.
        self.peak_memory = peak_memory
        # The query ID.
        self.process_id = process_id
        # The SQL statement.
        # 
        # >  For performance considerations, an SQL statement cannot exceed 5,120 characters in length. Otherwise, the SQL statement is truncated. You can call the [DownloadDiagnosisRecords](https://help.aliyun.com/document_detail/308212.html) operation to download the information about SQL statements that meet a query condition for an AnalyticDB for MySQL cluster, including the complete SQL statements.
        self.sql = sql
        # The amount of scanned data. Unit: bytes.
        self.scan_size = scan_size
        # The start time of the query. The time follows the ISO 8601 standard in the *yyyy-MM-ddTHH:mm:ssZ* format. The time is displayed in UTC.
        self.start_time = start_time
        # The total number of stages generated.
        self.total_stages = total_stages

    def validate(self):
        if self.diagnosis_results:
            for v1 in self.diagnosis_results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cost is not None:
            result['Cost'] = self.cost

        result['DiagnosisResults'] = []
        if self.diagnosis_results is not None:
            for k1 in self.diagnosis_results:
                result['DiagnosisResults'].append(k1.to_map() if k1 else None)

        if self.operator_cost is not None:
            result['OperatorCost'] = self.operator_cost

        if self.output_data_size is not None:
            result['OutputDataSize'] = self.output_data_size

        if self.pattern_id is not None:
            result['PatternId'] = self.pattern_id

        if self.peak_memory is not None:
            result['PeakMemory'] = self.peak_memory

        if self.process_id is not None:
            result['ProcessId'] = self.process_id

        if self.sql is not None:
            result['SQL'] = self.sql

        if self.scan_size is not None:
            result['ScanSize'] = self.scan_size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.total_stages is not None:
            result['TotalStages'] = self.total_stages

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cost') is not None:
            self.cost = m.get('Cost')

        self.diagnosis_results = []
        if m.get('DiagnosisResults') is not None:
            for k1 in m.get('DiagnosisResults'):
                temp_model = main_models.DescribeBadSqlDetectionResponseBodyDetectionItemsResultsDiagnosisResults()
                self.diagnosis_results.append(temp_model.from_map(k1))

        if m.get('OperatorCost') is not None:
            self.operator_cost = m.get('OperatorCost')

        if m.get('OutputDataSize') is not None:
            self.output_data_size = m.get('OutputDataSize')

        if m.get('PatternId') is not None:
            self.pattern_id = m.get('PatternId')

        if m.get('PeakMemory') is not None:
            self.peak_memory = m.get('PeakMemory')

        if m.get('ProcessId') is not None:
            self.process_id = m.get('ProcessId')

        if m.get('SQL') is not None:
            self.sql = m.get('SQL')

        if m.get('ScanSize') is not None:
            self.scan_size = m.get('ScanSize')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TotalStages') is not None:
            self.total_stages = m.get('TotalStages')

        return self

class DescribeBadSqlDetectionResponseBodyDetectionItemsResultsDiagnosisResults(DaraModel):
    def __init__(
        self,
        code: str = None,
        detail: str = None,
        operator_id: str = None,
        stage_id: str = None,
    ):
        # The diagnostic code.
        self.code = code
        # The information about the diagnostic result.
        self.detail = detail
        # The operator ID.
        self.operator_id = operator_id
        # The stage ID.
        self.stage_id = stage_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.detail is not None:
            result['Detail'] = self.detail

        if self.operator_id is not None:
            result['OperatorId'] = self.operator_id

        if self.stage_id is not None:
            result['StageId'] = self.stage_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Detail') is not None:
            self.detail = m.get('Detail')

        if m.get('OperatorId') is not None:
            self.operator_id = m.get('OperatorId')

        if m.get('StageId') is not None:
            self.stage_id = m.get('StageId')

        return self

