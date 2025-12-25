# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class ListSQLReviewOriginSQLResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        origin_sqllist: List[main_models.ListSQLReviewOriginSQLResponseBodyOriginSQLList] = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The error code that is returned.
        self.error_code = error_code
        # The error message that is returned if the request failed.
        self.error_message = error_message
        # The information about the parsed SQL statements.
        self.origin_sqllist = origin_sqllist
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values: Valid values:
        # 
        # *   true
        # *   false
        self.success = success
        # The number of SQL statements in the file.
        self.total_count = total_count

    def validate(self):
        if self.origin_sqllist:
            for v1 in self.origin_sqllist:
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

        result['OriginSQLList'] = []
        if self.origin_sqllist is not None:
            for k1 in self.origin_sqllist:
                result['OriginSQLList'].append(k1.to_map() if k1 else None)

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

        self.origin_sqllist = []
        if m.get('OriginSQLList') is not None:
            for k1 in m.get('OriginSQLList'):
                temp_model = main_models.ListSQLReviewOriginSQLResponseBodyOriginSQLList()
                self.origin_sqllist.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListSQLReviewOriginSQLResponseBodyOriginSQLList(DaraModel):
    def __init__(
        self,
        check_status: str = None,
        checked_time: str = None,
        file_id: int = None,
        file_name: str = None,
        review_summary: str = None,
        sqlcontent: str = None,
        sqlid: int = None,
        sqlname: str = None,
        sqlreview_query_key: str = None,
        sql_hash: str = None,
        status_desc: str = None,
    ):
        # The review status of the SQL statement. Valid values:
        # 
        # *   **new**: The SQL statement was waiting to be reviewed.
        # *   **unknown**: The SQL statement cannot be parsed.
        # *   **check_not_pass**: The SQL statement failed to pass the review.
        # *   **check_pass**: The SQL statement passed the review.
        # *   **force_pass**: The SQL statement passed the manual review.
        # *   **force_not_pass**: The SQL statement failed to pass the manual review.
        self.check_status = check_status
        # The time when the SQL statement was reviewed.
        self.checked_time = checked_time
        # The file ID.
        self.file_id = file_id
        # The name of the file.
        self.file_name = file_name
        # The statistics on the optimization suggestions for SQL statements. The value is a JSON string. Valid values:
        # 
        # *   **MUST_IMPROVE**: The SQL statements must be optimized.
        # *   **POTENTIAL_ISSUE**: The SQL statements contain potential issues.
        # *   **SUGGEST_IMPROVE**: We recommend that you optimize the SQL statements.
        # *   **USEDMSTOOLKIT**: We recommend that you change schemas without locking tables.
        # *   **USEDMSDML_UNLOCK**: We recommend that you change data without locking tables.
        # *   **TABLEINDEXSUGGEST**: We recommend that you optimize indexes for the SQL statements.
        self.review_summary = review_summary
        # The SQL statement in the file.
        self.sqlcontent = sqlcontent
        # The ID of the SQL statement.
        self.sqlid = sqlid
        # The name of the SQL statement.
        self.sqlname = sqlname
        # The key that is used to query the information about optimization suggestions. You can call the [GetSQLReviewOptimizeDetail](https://help.aliyun.com/document_detail/465919.html) operation to query the details based on this key.
        self.sqlreview_query_key = sqlreview_query_key
        # The MD5 hash value that is obtained after the SQL statement is calculated by using a hash algorithm.
        self.sql_hash = sql_hash
        # The description of the review status.
        self.status_desc = status_desc

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status

        if self.checked_time is not None:
            result['CheckedTime'] = self.checked_time

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.review_summary is not None:
            result['ReviewSummary'] = self.review_summary

        if self.sqlcontent is not None:
            result['SQLContent'] = self.sqlcontent

        if self.sqlid is not None:
            result['SQLId'] = self.sqlid

        if self.sqlname is not None:
            result['SQLName'] = self.sqlname

        if self.sqlreview_query_key is not None:
            result['SQLReviewQueryKey'] = self.sqlreview_query_key

        if self.sql_hash is not None:
            result['SqlHash'] = self.sql_hash

        if self.status_desc is not None:
            result['StatusDesc'] = self.status_desc

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')

        if m.get('CheckedTime') is not None:
            self.checked_time = m.get('CheckedTime')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('ReviewSummary') is not None:
            self.review_summary = m.get('ReviewSummary')

        if m.get('SQLContent') is not None:
            self.sqlcontent = m.get('SQLContent')

        if m.get('SQLId') is not None:
            self.sqlid = m.get('SQLId')

        if m.get('SQLName') is not None:
            self.sqlname = m.get('SQLName')

        if m.get('SQLReviewQueryKey') is not None:
            self.sqlreview_query_key = m.get('SQLReviewQueryKey')

        if m.get('SqlHash') is not None:
            self.sql_hash = m.get('SqlHash')

        if m.get('StatusDesc') is not None:
            self.status_desc = m.get('StatusDesc')

        return self

