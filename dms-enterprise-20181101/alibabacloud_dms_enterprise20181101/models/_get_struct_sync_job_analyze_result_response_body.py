# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class GetStructSyncJobAnalyzeResultResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        struct_sync_job_analyze_result: main_models.GetStructSyncJobAnalyzeResultResponseBodyStructSyncJobAnalyzeResult = None,
        success: bool = None,
    ):
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The ID of the request.
        self.request_id = request_id
        # The analysis result of the schema synchronization task.
        self.struct_sync_job_analyze_result = struct_sync_job_analyze_result
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.struct_sync_job_analyze_result:
            self.struct_sync_job_analyze_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.struct_sync_job_analyze_result is not None:
            result['StructSyncJobAnalyzeResult'] = self.struct_sync_job_analyze_result.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StructSyncJobAnalyzeResult') is not None:
            temp_model = main_models.GetStructSyncJobAnalyzeResultResponseBodyStructSyncJobAnalyzeResult()
            self.struct_sync_job_analyze_result = temp_model.from_map(m.get('StructSyncJobAnalyzeResult'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetStructSyncJobAnalyzeResultResponseBodyStructSyncJobAnalyzeResult(DaraModel):
    def __init__(
        self,
        result_list: List[main_models.GetStructSyncJobAnalyzeResultResponseBodyStructSyncJobAnalyzeResultResultList] = None,
        summary_list: List[main_models.GetStructSyncJobAnalyzeResultResponseBodyStructSyncJobAnalyzeResultSummaryList] = None,
    ):
        # The details of the analysis results.
        self.result_list = result_list
        # The statistics on the analysis results.
        self.summary_list = summary_list

    def validate(self):
        if self.result_list:
            for v1 in self.result_list:
                 if v1:
                    v1.validate()
        if self.summary_list:
            for v1 in self.summary_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ResultList'] = []
        if self.result_list is not None:
            for k1 in self.result_list:
                result['ResultList'].append(k1.to_map() if k1 else None)

        result['SummaryList'] = []
        if self.summary_list is not None:
            for k1 in self.summary_list:
                result['SummaryList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result_list = []
        if m.get('ResultList') is not None:
            for k1 in m.get('ResultList'):
                temp_model = main_models.GetStructSyncJobAnalyzeResultResponseBodyStructSyncJobAnalyzeResultResultList()
                self.result_list.append(temp_model.from_map(k1))

        self.summary_list = []
        if m.get('SummaryList') is not None:
            for k1 in m.get('SummaryList'):
                temp_model = main_models.GetStructSyncJobAnalyzeResultResponseBodyStructSyncJobAnalyzeResultSummaryList()
                self.summary_list.append(temp_model.from_map(k1))

        return self

class GetStructSyncJobAnalyzeResultResponseBodyStructSyncJobAnalyzeResultSummaryList(DaraModel):
    def __init__(
        self,
        compare_type: str = None,
        count: int = None,
    ):
        # The type of the comparison. Valid values:
        # 
        # *   **CREATE_TABLE**: compares the created tables.
        # *   **ALTER_TABLE**: compares the modified tables.
        # *   **EQUAL_TABLE**: compares the identical tables.
        # *   **PASS_TABLE**: compares the tables that are skipped during schema synchronization.
        # *   **NOT_COMPARE**: does not compare tables.
        self.compare_type = compare_type
        # The number of tables.
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compare_type is not None:
            result['CompareType'] = self.compare_type

        if self.count is not None:
            result['Count'] = self.count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompareType') is not None:
            self.compare_type = m.get('CompareType')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        return self

class GetStructSyncJobAnalyzeResultResponseBodyStructSyncJobAnalyzeResultResultList(DaraModel):
    def __init__(
        self,
        script: str = None,
        source_table_name: str = None,
        target_table_name: str = None,
    ):
        # The SQL script.
        self.script = script
        # The name of the source table.
        self.source_table_name = source_table_name
        # The name of the destination table.
        self.target_table_name = target_table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.script is not None:
            result['Script'] = self.script

        if self.source_table_name is not None:
            result['SourceTableName'] = self.source_table_name

        if self.target_table_name is not None:
            result['TargetTableName'] = self.target_table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Script') is not None:
            self.script = m.get('Script')

        if m.get('SourceTableName') is not None:
            self.source_table_name = m.get('SourceTableName')

        if m.get('TargetTableName') is not None:
            self.target_table_name = m.get('TargetTableName')

        return self

