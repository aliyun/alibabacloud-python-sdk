# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class ListDataCorrectPreCheckSQLResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        pre_check_sqllist: List[main_models.ListDataCorrectPreCheckSQLResponseBodyPreCheckSQLList] = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code returned.
        self.error_code = error_code
        # The error message returned.
        self.error_message = error_message
        # The precheck information about SQL statements.
        self.pre_check_sqllist = pre_check_sqllist
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # *   **true**: The request is successful.
        # *   **false**: The request fails.
        self.success = success

    def validate(self):
        if self.pre_check_sqllist:
            for v1 in self.pre_check_sqllist:
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

        result['PreCheckSQLList'] = []
        if self.pre_check_sqllist is not None:
            for k1 in self.pre_check_sqllist:
                result['PreCheckSQLList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        self.pre_check_sqllist = []
        if m.get('PreCheckSQLList') is not None:
            for k1 in m.get('PreCheckSQLList'):
                temp_model = main_models.ListDataCorrectPreCheckSQLResponseBodyPreCheckSQLList()
                self.pre_check_sqllist.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListDataCorrectPreCheckSQLResponseBodyPreCheckSQLList(DaraModel):
    def __init__(
        self,
        affect_rows: int = None,
        check_sql: str = None,
        db_id: int = None,
        sqlreview_query_key: str = None,
        sql_review_status: str = None,
        sql_type: str = None,
        table_names: str = None,
    ):
        # The estimated number of affected rows.
        self.affect_rows = affect_rows
        # The SQL statement.
        self.check_sql = check_sql
        # The ID of the database.
        self.db_id = db_id
        # The key that is used to query the details of optimization suggestions. You can call the [GetSQLReviewOptimizeDetail](https://help.aliyun.com/document_detail/265977.html) operation to query the details of optimization suggestions based on the key.
        self.sqlreview_query_key = sqlreview_query_key
        # The review status of the SQL statement. Valid values:
        # 
        # *   **WAITING**: The SQL statement is pending for review.
        # *   **RUNNING**: The SQL statement is being reviewed.
        # *   **IGNORE**: The SQL statement review is skipped.
        # *   **PASS**: The SQL statement passed the review.
        # *   **BLOCK**: The SQL statement failed the review.
        self.sql_review_status = sql_review_status
        # The type of the SQL statement, such as DELETE, UPDATE, or ALTER_TABLE.
        self.sql_type = sql_type
        # The name of the table whose data is changed.
        self.table_names = table_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.affect_rows is not None:
            result['AffectRows'] = self.affect_rows

        if self.check_sql is not None:
            result['CheckSQL'] = self.check_sql

        if self.db_id is not None:
            result['DbId'] = self.db_id

        if self.sqlreview_query_key is not None:
            result['SQLReviewQueryKey'] = self.sqlreview_query_key

        if self.sql_review_status is not None:
            result['SqlReviewStatus'] = self.sql_review_status

        if self.sql_type is not None:
            result['SqlType'] = self.sql_type

        if self.table_names is not None:
            result['TableNames'] = self.table_names

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AffectRows') is not None:
            self.affect_rows = m.get('AffectRows')

        if m.get('CheckSQL') is not None:
            self.check_sql = m.get('CheckSQL')

        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('SQLReviewQueryKey') is not None:
            self.sqlreview_query_key = m.get('SQLReviewQueryKey')

        if m.get('SqlReviewStatus') is not None:
            self.sql_review_status = m.get('SqlReviewStatus')

        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')

        if m.get('TableNames') is not None:
            self.table_names = m.get('TableNames')

        return self

