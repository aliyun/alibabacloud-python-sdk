# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class ListDataImportSQLPreCheckDetailResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        pre_check_sqldetail_list: List[main_models.ListDataImportSQLPreCheckDetailResponseBodyPreCheckSQLDetailList] = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The error code returned if the request failed.
        self.error_code = error_code
        # The error message returned if the request failed.
        self.error_message = error_message
        # The precheck information of SQL statements.
        self.pre_check_sqldetail_list = pre_check_sqldetail_list
        # The request ID. You can use the ID to locate logs and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success
        # The number of SQL statements.
        self.total_count = total_count

    def validate(self):
        if self.pre_check_sqldetail_list:
            for v1 in self.pre_check_sqldetail_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        result['PreCheckSQLDetailList'] = []
        if self.pre_check_sqldetail_list is not None:
            for k1 in self.pre_check_sqldetail_list:
                result['PreCheckSQLDetailList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        self.pre_check_sqldetail_list = []
        if m.get('PreCheckSQLDetailList') is not None:
            for k1 in m.get('PreCheckSQLDetailList'):
                temp_model = main_models.ListDataImportSQLPreCheckDetailResponseBodyPreCheckSQLDetailList()
                self.pre_check_sqldetail_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListDataImportSQLPreCheckDetailResponseBodyPreCheckSQLDetailList(DaraModel):
    def __init__(
        self,
        skip: bool = None,
        sql_id: int = None,
        sql_type: str = None,
        status_code: str = None,
    ):
        # Indicates whether the precheck of the SQL statement was skipped. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.skip = skip
        # The SQL ID, which indicates the sequence number of the SQL statement. The number starts with 1.
        self.sql_id = sql_id
        # The type of the SQL statement, such as DELETE, UPDATE, or ALTER_TABLE.
        self.sql_type = sql_type
        # The state of the ticket. Valid values:
        # 
        # *   **INIT**: The ticket was being initialized.
        # *   **RUNNING**: The ticket was in progress.
        # *   **SUCCESS**: The ticket was complete.
        # *   **TIMEOUT**: The ticket was skipped due to timeout.
        # *   **FAIL**: The ticket failed.
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.skip is not None:
            result['Skip'] = self.skip

        if self.sql_id is not None:
            result['SqlId'] = self.sql_id

        if self.sql_type is not None:
            result['SqlType'] = self.sql_type

        if self.status_code is not None:
            result['StatusCode'] = self.status_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Skip') is not None:
            self.skip = m.get('Skip')

        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')

        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')

        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')

        return self

