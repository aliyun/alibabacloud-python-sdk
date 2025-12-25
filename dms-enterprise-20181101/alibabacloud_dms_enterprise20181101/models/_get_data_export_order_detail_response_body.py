# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class GetDataExportOrderDetailResponseBody(DaraModel):
    def __init__(
        self,
        data_export_order_detail: main_models.GetDataExportOrderDetailResponseBodyDataExportOrderDetail = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The information about the data export ticket.
        self.data_export_order_detail = data_export_order_detail
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values: Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success

    def validate(self):
        if self.data_export_order_detail:
            self.data_export_order_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_export_order_detail is not None:
            result['DataExportOrderDetail'] = self.data_export_order_detail.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataExportOrderDetail') is not None:
            temp_model = main_models.GetDataExportOrderDetailResponseBodyDataExportOrderDetail()
            self.data_export_order_detail = temp_model.from_map(m.get('DataExportOrderDetail'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetDataExportOrderDetailResponseBodyDataExportOrderDetail(DaraModel):
    def __init__(
        self,
        key_info: main_models.GetDataExportOrderDetailResponseBodyDataExportOrderDetailKeyInfo = None,
        order_detail: main_models.GetDataExportOrderDetailResponseBodyDataExportOrderDetailOrderDetail = None,
    ):
        # The status information.
        self.key_info = key_info
        # The details of the ticket.
        self.order_detail = order_detail

    def validate(self):
        if self.key_info:
            self.key_info.validate()
        if self.order_detail:
            self.order_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key_info is not None:
            result['KeyInfo'] = self.key_info.to_map()

        if self.order_detail is not None:
            result['OrderDetail'] = self.order_detail.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyInfo') is not None:
            temp_model = main_models.GetDataExportOrderDetailResponseBodyDataExportOrderDetailKeyInfo()
            self.key_info = temp_model.from_map(m.get('KeyInfo'))

        if m.get('OrderDetail') is not None:
            temp_model = main_models.GetDataExportOrderDetailResponseBodyDataExportOrderDetailOrderDetail()
            self.order_detail = temp_model.from_map(m.get('OrderDetail'))

        return self

class GetDataExportOrderDetailResponseBodyDataExportOrderDetailOrderDetail(DaraModel):
    def __init__(
        self,
        actual_affect_rows: int = None,
        classify: str = None,
        database: str = None,
        db_id: int = None,
        env_type: str = None,
        exe_sql: str = None,
        ignore_affect_rows: bool = None,
        ignore_affect_rows_reason: str = None,
        logic: bool = None,
    ):
        # The number of rows that were affected by the SQL statement.
        self.actual_affect_rows = actual_affect_rows
        # The category of the reason for the data export.
        self.classify = classify
        # The name of the database from which data was exported.
        self.database = database
        # The ID of the database from which data was exported.
        self.db_id = db_id
        # The type of the environment to which the database belongs.
        self.env_type = env_type
        # The SQL statement that was executed to export data.
        self.exe_sql = exe_sql
        # Indicates whether the affected rows are skipped.
        self.ignore_affect_rows = ignore_affect_rows
        # The reason why the affected rows are skipped.
        self.ignore_affect_rows_reason = ignore_affect_rows_reason
        # Indicates whether the database is a logical database.
        self.logic = logic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actual_affect_rows is not None:
            result['ActualAffectRows'] = self.actual_affect_rows

        if self.classify is not None:
            result['Classify'] = self.classify

        if self.database is not None:
            result['Database'] = self.database

        if self.db_id is not None:
            result['DbId'] = self.db_id

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.exe_sql is not None:
            result['ExeSQL'] = self.exe_sql

        if self.ignore_affect_rows is not None:
            result['IgnoreAffectRows'] = self.ignore_affect_rows

        if self.ignore_affect_rows_reason is not None:
            result['IgnoreAffectRowsReason'] = self.ignore_affect_rows_reason

        if self.logic is not None:
            result['Logic'] = self.logic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActualAffectRows') is not None:
            self.actual_affect_rows = m.get('ActualAffectRows')

        if m.get('Classify') is not None:
            self.classify = m.get('Classify')

        if m.get('Database') is not None:
            self.database = m.get('Database')

        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('ExeSQL') is not None:
            self.exe_sql = m.get('ExeSQL')

        if m.get('IgnoreAffectRows') is not None:
            self.ignore_affect_rows = m.get('IgnoreAffectRows')

        if m.get('IgnoreAffectRowsReason') is not None:
            self.ignore_affect_rows_reason = m.get('IgnoreAffectRowsReason')

        if m.get('Logic') is not None:
            self.logic = m.get('Logic')

        return self

class GetDataExportOrderDetailResponseBodyDataExportOrderDetailKeyInfo(DaraModel):
    def __init__(
        self,
        job_id: int = None,
        job_status: str = None,
        pre_check_id: int = None,
    ):
        # Export task ID.
        self.job_id = job_id
        # The state of the data export ticket. Valid values:
        # 
        # *   **PRE_CHECKING**: The ticket was being prechecked.
        # *   **PRE_CHECK_SUCCESS**: The ticket passed the precheck.
        # *   **PRE_CHECK_FAIL**: The ticket failed to pass the prechecked.
        # *   **WAITING_APPLY_AUDIT**: The ticket was to be submitted for approval.
        # *   **APPLY_AUDIT_SUCCESS**: The ticket was submitted for approval.
        # *   **ENABLE_EXPORT**: The ticket was approved. Data can be exported.
        # *   **WAITING_EXPORT**: Data was to be scheduled for export.
        # *   **DOING_EXPORT**: Data was being exported.
        # *   **EXPORT_FAIL**: Data failed to be exported.
        # *   **EXPORT_SUCCESS**: Data was exported.
        self.job_status = job_status
        # The precheck ID.
        self.pre_check_id = pre_check_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.job_status is not None:
            result['JobStatus'] = self.job_status

        if self.pre_check_id is not None:
            result['PreCheckId'] = self.pre_check_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('JobStatus') is not None:
            self.job_status = m.get('JobStatus')

        if m.get('PreCheckId') is not None:
            self.pre_check_id = m.get('PreCheckId')

        return self

