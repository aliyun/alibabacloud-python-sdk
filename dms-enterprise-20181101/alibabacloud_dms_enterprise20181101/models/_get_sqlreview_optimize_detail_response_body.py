# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class GetSQLReviewOptimizeDetailResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        optimize_detail: main_models.GetSQLReviewOptimizeDetailResponseBodyOptimizeDetail = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code returned.
        self.error_code = error_code
        # The error message returned.
        self.error_message = error_message
        # The details of optimization suggestions for SQL statements.
        self.optimize_detail = optimize_detail
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.optimize_detail:
            self.optimize_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.optimize_detail is not None:
            result['OptimizeDetail'] = self.optimize_detail.to_map()

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

        if m.get('OptimizeDetail') is not None:
            temp_model = main_models.GetSQLReviewOptimizeDetailResponseBodyOptimizeDetail()
            self.optimize_detail = temp_model.from_map(m.get('OptimizeDetail'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetSQLReviewOptimizeDetailResponseBodyOptimizeDetail(DaraModel):
    def __init__(
        self,
        db_id: int = None,
        instance_id: int = None,
        quality_result: main_models.GetSQLReviewOptimizeDetailResponseBodyOptimizeDetailQualityResult = None,
        query_key: str = None,
        sql_type: str = None,
    ):
        # The ID of the database.
        self.db_id = db_id
        # The ID of the instance to which the database belongs.
        self.instance_id = instance_id
        # The quality of the SQL statement.
        self.quality_result = quality_result
        # The key that is used to query the details of optimization suggestions.
        self.query_key = query_key
        # The type of the SQL statement. Valid values: DELETE, UPDATE, and ALTER_TABLE.
        self.sql_type = sql_type

    def validate(self):
        if self.quality_result:
            self.quality_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_id is not None:
            result['DbId'] = self.db_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.quality_result is not None:
            result['QualityResult'] = self.quality_result.to_map()

        if self.query_key is not None:
            result['QueryKey'] = self.query_key

        if self.sql_type is not None:
            result['SqlType'] = self.sql_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('QualityResult') is not None:
            temp_model = main_models.GetSQLReviewOptimizeDetailResponseBodyOptimizeDetailQualityResult()
            self.quality_result = temp_model.from_map(m.get('QualityResult'))

        if m.get('QueryKey') is not None:
            self.query_key = m.get('QueryKey')

        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')

        return self

class GetSQLReviewOptimizeDetailResponseBodyOptimizeDetailQualityResult(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        occur_error: bool = None,
        results: List[main_models.GetSQLReviewOptimizeDetailResponseBodyOptimizeDetailQualityResultResults] = None,
    ):
        # The error message returned.
        self.error_message = error_message
        # Indicates whether an error occurs. Valid values:
        # 
        # *   **true**: An error occurs.
        # *   **false**: No error occurs.
        self.occur_error = occur_error
        # The review results based on rules.
        self.results = results

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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.occur_error is not None:
            result['OccurError'] = self.occur_error

        result['Results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['Results'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('OccurError') is not None:
            self.occur_error = m.get('OccurError')

        self.results = []
        if m.get('Results') is not None:
            for k1 in m.get('Results'):
                temp_model = main_models.GetSQLReviewOptimizeDetailResponseBodyOptimizeDetailQualityResultResults()
                self.results.append(temp_model.from_map(k1))

        return self

class GetSQLReviewOptimizeDetailResponseBodyOptimizeDetailQualityResultResults(DaraModel):
    def __init__(
        self,
        comments: str = None,
        feedback: str = None,
        messages: List[str] = None,
        rule_name: str = None,
        rule_type: str = None,
        scripts: List[main_models.GetSQLReviewOptimizeDetailResponseBodyOptimizeDetailQualityResultResultsScripts] = None,
    ):
        # The comment that is specified when you create the SQL review rule. For more information, see [SQL review optimization](https://help.aliyun.com/document_detail/194114.html).
        self.comments = comments
        # The optimization suggestion for the SQL statement. Valid values:
        # 
        # *   **MUST_IMPROVE**: The SQL statement must be improved.
        # *   **POTENTIAL_ISSUE**: The SQL statement contains potential issues.
        # *   **SUGGEST_IMPROVE**: We recommend that you improve the SQL statement.
        # *   **USEDMSTOOLKIT**: We recommend that you change schemas without locking tables.
        # *   **USEDMSDML_UNLOCK**: We recommend that you change data without locking tables.
        # *   **TABLEINDEXSUGGEST**: We recommend that you use SQL statements that use indexes.
        self.feedback = feedback
        # The review results.
        self.messages = messages
        # The name of the rule. For more information, see [SQL review optimization](https://help.aliyun.com/document_detail/194114.html).
        self.rule_name = rule_name
        # The type of the SQL review rule. Valid values:
        # 
        # *   **REVIEW**: a rule that is used to review SQL statements based on standards.
        # *   **OPTIMIZE**: a rule that is used to provide optimization suggestions.
        self.rule_type = rule_type
        # The SQL script for data changes.
        self.scripts = scripts

    def validate(self):
        if self.scripts:
            for v1 in self.scripts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comments is not None:
            result['Comments'] = self.comments

        if self.feedback is not None:
            result['Feedback'] = self.feedback

        if self.messages is not None:
            result['Messages'] = self.messages

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        result['Scripts'] = []
        if self.scripts is not None:
            for k1 in self.scripts:
                result['Scripts'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')

        if m.get('Feedback') is not None:
            self.feedback = m.get('Feedback')

        if m.get('Messages') is not None:
            self.messages = m.get('Messages')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        self.scripts = []
        if m.get('Scripts') is not None:
            for k1 in m.get('Scripts'):
                temp_model = main_models.GetSQLReviewOptimizeDetailResponseBodyOptimizeDetailQualityResultResultsScripts()
                self.scripts.append(temp_model.from_map(k1))

        return self

class GetSQLReviewOptimizeDetailResponseBodyOptimizeDetailQualityResultResultsScripts(DaraModel):
    def __init__(
        self,
        content: str = None,
        op_type: str = None,
        table_name: str = None,
    ):
        # The content of the SQL script.
        self.content = content
        # The purpose of the SQL script. The value is set to AddIndex.
        self.op_type = op_type
        # The name of the table.
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.op_type is not None:
            result['OpType'] = self.op_type

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('OpType') is not None:
            self.op_type = m.get('OpType')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

