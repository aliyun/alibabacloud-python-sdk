# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeSparkSQLDiagnosisListResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        sqldiagnosis_list: List[main_models.DescribeSparkSQLDiagnosisListResponseBodySQLDiagnosisList] = None,
        total_count: int = None,
    ):
        # The information about the request denial.
        self.access_denied_detail = access_denied_detail
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The queried diagnostic information.
        self.sqldiagnosis_list = sqldiagnosis_list
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.sqldiagnosis_list:
            for v1 in self.sqldiagnosis_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SQLDiagnosisList'] = []
        if self.sqldiagnosis_list is not None:
            for k1 in self.sqldiagnosis_list:
                result['SQLDiagnosisList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.sqldiagnosis_list = []
        if m.get('SQLDiagnosisList') is not None:
            for k1 in m.get('SQLDiagnosisList'):
                temp_model = main_models.DescribeSparkSQLDiagnosisListResponseBodySQLDiagnosisList()
                self.sqldiagnosis_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeSparkSQLDiagnosisListResponseBodySQLDiagnosisList(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        elapsed_time: int = None,
        inner_query_id: int = None,
        max_exclusive_time: int = None,
        peak_memory: int = None,
        sql: str = None,
        scan_row_count: int = None,
        start_time: str = None,
        state: str = None,
        statement_id: int = None,
    ):
        # The application ID.
        # 
        # >  You can call the [ListSparkApps](https://help.aliyun.com/document_detail/612475.html) operation to query a list of Spark application IDs.
        self.app_id = app_id
        # The execution duration of the query. Unit: milliseconds.
        self.elapsed_time = elapsed_time
        # The ID of the query executed within the Spark application.
        self.inner_query_id = inner_query_id
        # The maximum operator execution duration. Unit: milliseconds.
        self.max_exclusive_time = max_exclusive_time
        # The maximum operator memory used. Unit: bytes.
        self.peak_memory = peak_memory
        # The SQL statement.
        self.sql = sql
        # The number of entries scanned.
        self.scan_row_count = scan_row_count
        # The start time of the query. The time follows the ISO 8601 standard in the *yyyy-MM-ddTHH:mmZ* format. The time is displayed in UTC.
        self.start_time = start_time
        # The execution status of the query. Valid values:
        # 
        # *   COMPLETED
        # *   CANCELED
        # *   ABORTED
        # *   FAILED
        self.state = state
        # The unique ID of the code block in the Spark job.
        self.statement_id = statement_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.elapsed_time is not None:
            result['ElapsedTime'] = self.elapsed_time

        if self.inner_query_id is not None:
            result['InnerQueryId'] = self.inner_query_id

        if self.max_exclusive_time is not None:
            result['MaxExclusiveTime'] = self.max_exclusive_time

        if self.peak_memory is not None:
            result['PeakMemory'] = self.peak_memory

        if self.sql is not None:
            result['SQL'] = self.sql

        if self.scan_row_count is not None:
            result['ScanRowCount'] = self.scan_row_count

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.state is not None:
            result['State'] = self.state

        if self.statement_id is not None:
            result['StatementId'] = self.statement_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('ElapsedTime') is not None:
            self.elapsed_time = m.get('ElapsedTime')

        if m.get('InnerQueryId') is not None:
            self.inner_query_id = m.get('InnerQueryId')

        if m.get('MaxExclusiveTime') is not None:
            self.max_exclusive_time = m.get('MaxExclusiveTime')

        if m.get('PeakMemory') is not None:
            self.peak_memory = m.get('PeakMemory')

        if m.get('SQL') is not None:
            self.sql = m.get('SQL')

        if m.get('ScanRowCount') is not None:
            self.scan_row_count = m.get('ScanRowCount')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('StatementId') is not None:
            self.statement_id = m.get('StatementId')

        return self

