# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class GetSQLReviewCheckResultStatusResponseBody(DaraModel):
    def __init__(
        self,
        check_result_status: main_models.GetSQLReviewCheckResultStatusResponseBodyCheckResultStatus = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The result of the SQL review.
        self.check_result_status = check_result_status
        # The error code returned if the request failed.
        self.error_code = error_code
        # The error message returned if the request failed.
        self.error_message = error_message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.check_result_status:
            self.check_result_status.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_result_status is not None:
            result['CheckResultStatus'] = self.check_result_status.to_map()

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
        if m.get('CheckResultStatus') is not None:
            temp_model = main_models.GetSQLReviewCheckResultStatusResponseBodyCheckResultStatus()
            self.check_result_status = temp_model.from_map(m.get('CheckResultStatus'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetSQLReviewCheckResultStatusResponseBodyCheckResultStatus(DaraModel):
    def __init__(
        self,
        check_status_result: main_models.GetSQLReviewCheckResultStatusResponseBodyCheckResultStatusCheckStatusResult = None,
        checked_count: int = None,
        sqlreview_result: main_models.GetSQLReviewCheckResultStatusResponseBodyCheckResultStatusSQLReviewResult = None,
        total_sqlcount: int = None,
    ):
        # The result of the SQL status check.
        self.check_status_result = check_status_result
        # The number of SQL statements that were reviewed.
        self.checked_count = checked_count
        # The optimization suggestion for SQL statements.
        self.sqlreview_result = sqlreview_result
        # The total number of SQL statements.
        self.total_sqlcount = total_sqlcount

    def validate(self):
        if self.check_status_result:
            self.check_status_result.validate()
        if self.sqlreview_result:
            self.sqlreview_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_status_result is not None:
            result['CheckStatusResult'] = self.check_status_result.to_map()

        if self.checked_count is not None:
            result['CheckedCount'] = self.checked_count

        if self.sqlreview_result is not None:
            result['SQLReviewResult'] = self.sqlreview_result.to_map()

        if self.total_sqlcount is not None:
            result['TotalSQLCount'] = self.total_sqlcount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckStatusResult') is not None:
            temp_model = main_models.GetSQLReviewCheckResultStatusResponseBodyCheckResultStatusCheckStatusResult()
            self.check_status_result = temp_model.from_map(m.get('CheckStatusResult'))

        if m.get('CheckedCount') is not None:
            self.checked_count = m.get('CheckedCount')

        if m.get('SQLReviewResult') is not None:
            temp_model = main_models.GetSQLReviewCheckResultStatusResponseBodyCheckResultStatusSQLReviewResult()
            self.sqlreview_result = temp_model.from_map(m.get('SQLReviewResult'))

        if m.get('TotalSQLCount') is not None:
            self.total_sqlcount = m.get('TotalSQLCount')

        return self

class GetSQLReviewCheckResultStatusResponseBodyCheckResultStatusSQLReviewResult(DaraModel):
    def __init__(
        self,
        must_improve: int = None,
        potential_issue: int = None,
        suggest_improve: int = None,
        table_index_suggest: int = None,
        use_dms_dml_unlock: int = None,
        use_dms_toolkit: int = None,
    ):
        # The number of SQL statements that must be modified.
        self.must_improve = must_improve
        # The number of SQL statements that have potential issues.
        self.potential_issue = potential_issue
        # The number of SQL statements that can be modified.
        self.suggest_improve = suggest_improve
        # The number of SQL statements that can use indexes.
        self.table_index_suggest = table_index_suggest
        # The number of SQL statements that can be used for lock-free data changes.
        self.use_dms_dml_unlock = use_dms_dml_unlock
        # The number of SQL statements that can be used for lock-free schema changes.
        self.use_dms_toolkit = use_dms_toolkit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.must_improve is not None:
            result['MustImprove'] = self.must_improve

        if self.potential_issue is not None:
            result['PotentialIssue'] = self.potential_issue

        if self.suggest_improve is not None:
            result['SuggestImprove'] = self.suggest_improve

        if self.table_index_suggest is not None:
            result['TableIndexSuggest'] = self.table_index_suggest

        if self.use_dms_dml_unlock is not None:
            result['UseDmsDmlUnlock'] = self.use_dms_dml_unlock

        if self.use_dms_toolkit is not None:
            result['UseDmsToolkit'] = self.use_dms_toolkit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MustImprove') is not None:
            self.must_improve = m.get('MustImprove')

        if m.get('PotentialIssue') is not None:
            self.potential_issue = m.get('PotentialIssue')

        if m.get('SuggestImprove') is not None:
            self.suggest_improve = m.get('SuggestImprove')

        if m.get('TableIndexSuggest') is not None:
            self.table_index_suggest = m.get('TableIndexSuggest')

        if m.get('UseDmsDmlUnlock') is not None:
            self.use_dms_dml_unlock = m.get('UseDmsDmlUnlock')

        if m.get('UseDmsToolkit') is not None:
            self.use_dms_toolkit = m.get('UseDmsToolkit')

        return self

class GetSQLReviewCheckResultStatusResponseBodyCheckResultStatusCheckStatusResult(DaraModel):
    def __init__(
        self,
        check_not_pass: int = None,
        check_pass: int = None,
        force_not_pass: int = None,
        force_pass: int = None,
        new: int = None,
        unknown: int = None,
    ):
        # The number of SQL statements that failed to pass the review.
        self.check_not_pass = check_not_pass
        # The number of SQL statements that passed the review.
        self.check_pass = check_pass
        # The number of SQL statements that failed to pass the manual review.
        self.force_not_pass = force_not_pass
        # The number of SQL statements that passed the manual review.
        self.force_pass = force_pass
        # The number of SQL statements to be reviewed.
        self.new = new
        # The number of abnormal SQL statements.
        self.unknown = unknown

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_not_pass is not None:
            result['CheckNotPass'] = self.check_not_pass

        if self.check_pass is not None:
            result['CheckPass'] = self.check_pass

        if self.force_not_pass is not None:
            result['ForceNotPass'] = self.force_not_pass

        if self.force_pass is not None:
            result['ForcePass'] = self.force_pass

        if self.new is not None:
            result['New'] = self.new

        if self.unknown is not None:
            result['Unknown'] = self.unknown

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckNotPass') is not None:
            self.check_not_pass = m.get('CheckNotPass')

        if m.get('CheckPass') is not None:
            self.check_pass = m.get('CheckPass')

        if m.get('ForceNotPass') is not None:
            self.force_not_pass = m.get('ForceNotPass')

        if m.get('ForcePass') is not None:
            self.force_pass = m.get('ForcePass')

        if m.get('New') is not None:
            self.new = m.get('New')

        if m.get('Unknown') is not None:
            self.unknown = m.get('Unknown')

        return self

