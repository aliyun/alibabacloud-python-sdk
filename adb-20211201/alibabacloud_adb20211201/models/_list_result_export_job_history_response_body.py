# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class ListResultExportJobHistoryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        items: List[main_models.ListResultExportJobHistoryResponseBodyItems] = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The HTTP status code.
        self.code = code
        # The response code. The status code 200 indicates that the request was successful.
        self.http_status_code = http_status_code
        # The queried result set export jobs.
        self.items = items
        # The returned message. Valid values:
        # 
        # *   If the request was successful, an **OK** message is returned.
        # *   If the request failed, an error message is returned.
        self.message = message
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.ListResultExportJobHistoryResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListResultExportJobHistoryResponseBodyItems(DaraModel):
    def __init__(
        self,
        ali_uid: str = None,
        create_time: str = None,
        dbcluster_id: str = None,
        database_user: str = None,
        end_time: str = None,
        engine: str = None,
        export_job_id: str = None,
        export_path: str = None,
        export_rows: str = None,
        export_type: str = None,
        is_expired: bool = None,
        message: str = None,
        process_id: str = None,
        progress: str = None,
        resource_group: str = None,
        schema: str = None,
        sql: str = None,
        start_time: str = None,
        status: str = None,
        time_cost: int = None,
    ):
        # The RAM user ID.
        self.ali_uid = ali_uid
        # The time when the result set export job was created. The time follows the ISO 8601 standard in the *yyyy-mm-ddThh:mm:ssZ* format. The time is displayed in UTC.
        self.create_time = create_time
        # The ID of the AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        self.dbcluster_id = dbcluster_id
        # The name of the database account that is associated with the RAM user.
        self.database_user = database_user
        # The end time of the result set export job. The time follows the ISO 8601 standard in the *yyyy-MM-ddTHH:mm:ssZ* format. The time is displayed in UTC.
        # 
        # >  The end time must be later than the start time.
        self.end_time = end_time
        # The engine that is used to execute the result set export job. Only XIHE is returned.
        self.engine = engine
        # The unique identifier of the result set export job.
        self.export_job_id = export_job_id
        # The complete URL of the path to store the exported result set.
        self.export_path = export_path
        # The number of exported rows. This parameter is returned only when the request was successful.
        self.export_rows = export_rows
        # The type of the result set export job.
        self.export_type = export_type
        # Indicates whether the result set export job has expired. Valid values:
        # 
        # *   **false**
        # *   **true**
        self.is_expired = is_expired
        # The returned message. This parameter is returned only when the request failed.
        self.message = message
        # The query ID that can be used for diagnostics.
        # 
        # >  You can call the [DescribeDiagnosisSQLInfo](https://help.aliyun.com/document_detail/612337.html) operation to query the execution information about a query.
        self.process_id = process_id
        # The progress of the result set export job. Unit: %. Valid values: 0 to 100.
        self.progress = progress
        # The name of the resource group that runs the result set export job.
        self.resource_group = resource_group
        # The name of the database.
        self.schema = schema
        # The SQL statement that is used in the result set export job.
        self.sql = sql
        # The start time of the result set export job. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.start_time = start_time
        # The execution status of the result set export job. Valid values:
        # 
        # 1.  **SUBMITTED**
        # 2.  **RUNNING**
        # 3.  **SUCCEEDED**
        # 4.  **FAILED**
        self.status = status
        # The amount of time consumed to export execution records. Unit: milliseconds.
        # 
        # >  The value is the duration between the time when the result set export job starts and the time when the result set export job ends.
        self.time_cost = time_cost

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.database_user is not None:
            result['DatabaseUser'] = self.database_user

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.export_job_id is not None:
            result['ExportJobId'] = self.export_job_id

        if self.export_path is not None:
            result['ExportPath'] = self.export_path

        if self.export_rows is not None:
            result['ExportRows'] = self.export_rows

        if self.export_type is not None:
            result['ExportType'] = self.export_type

        if self.is_expired is not None:
            result['IsExpired'] = self.is_expired

        if self.message is not None:
            result['Message'] = self.message

        if self.process_id is not None:
            result['ProcessId'] = self.process_id

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group

        if self.schema is not None:
            result['Schema'] = self.schema

        if self.sql is not None:
            result['Sql'] = self.sql

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.time_cost is not None:
            result['TimeCost'] = self.time_cost

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DatabaseUser') is not None:
            self.database_user = m.get('DatabaseUser')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('ExportJobId') is not None:
            self.export_job_id = m.get('ExportJobId')

        if m.get('ExportPath') is not None:
            self.export_path = m.get('ExportPath')

        if m.get('ExportRows') is not None:
            self.export_rows = m.get('ExportRows')

        if m.get('ExportType') is not None:
            self.export_type = m.get('ExportType')

        if m.get('IsExpired') is not None:
            self.is_expired = m.get('IsExpired')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('ProcessId') is not None:
            self.process_id = m.get('ProcessId')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('ResourceGroup') is not None:
            self.resource_group = m.get('ResourceGroup')

        if m.get('Schema') is not None:
            self.schema = m.get('Schema')

        if m.get('Sql') is not None:
            self.sql = m.get('Sql')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TimeCost') is not None:
            self.time_cost = m.get('TimeCost')

        return self

