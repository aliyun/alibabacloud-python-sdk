# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms20250414 import models as main_models
from darabonba.model import DaraModel

class ListDataAgentAccuracyTestResultsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListDataAgentAccuracyTestResultsResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response struct.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message returned if the call failed.
        self.error_message = error_message
        # The maximum number of entries per page.
        self.max_results = max_results
        # The pagination token.
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # - **true**: The request was successful.
        # - **false**: The request failed.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ListDataAgentAccuracyTestResultsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListDataAgentAccuracyTestResultsResponseBodyData(DaraModel):
    def __init__(
        self,
        accuracy_rate: float = None,
        accuracy_test_task_id: str = None,
        content: List[main_models.ListDataAgentAccuracyTestResultsResponseBodyDataContent] = None,
        correct_count: int = None,
        failed_count: str = None,
        page_number: int = None,
        page_size: int = None,
        pending_count: str = None,
        total_elements: int = None,
        total_pages: int = None,
    ):
        # The accuracy rate.
        self.accuracy_rate = accuracy_rate
        # The ID of the accuracy test task.
        self.accuracy_test_task_id = accuracy_test_task_id
        # The data content.
        self.content = content
        # The number of test cases that passed evaluation.
        self.correct_count = correct_count
        self.failed_count = failed_count
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        self.pending_count = pending_count
        # The total number of results.
        self.total_elements = total_elements
        # The total number of pages.
        self.total_pages = total_pages

    def validate(self):
        if self.content:
            for v1 in self.content:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accuracy_rate is not None:
            result['AccuracyRate'] = self.accuracy_rate

        if self.accuracy_test_task_id is not None:
            result['AccuracyTestTaskId'] = self.accuracy_test_task_id

        result['Content'] = []
        if self.content is not None:
            for k1 in self.content:
                result['Content'].append(k1.to_map() if k1 else None)

        if self.correct_count is not None:
            result['CorrectCount'] = self.correct_count

        if self.failed_count is not None:
            result['FailedCount'] = self.failed_count

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.pending_count is not None:
            result['PendingCount'] = self.pending_count

        if self.total_elements is not None:
            result['TotalElements'] = self.total_elements

        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccuracyRate') is not None:
            self.accuracy_rate = m.get('AccuracyRate')

        if m.get('AccuracyTestTaskId') is not None:
            self.accuracy_test_task_id = m.get('AccuracyTestTaskId')

        self.content = []
        if m.get('Content') is not None:
            for k1 in m.get('Content'):
                temp_model = main_models.ListDataAgentAccuracyTestResultsResponseBodyDataContent()
                self.content.append(temp_model.from_map(k1))

        if m.get('CorrectCount') is not None:
            self.correct_count = m.get('CorrectCount')

        if m.get('FailedCount') is not None:
            self.failed_count = m.get('FailedCount')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PendingCount') is not None:
            self.pending_count = m.get('PendingCount')

        if m.get('TotalElements') is not None:
            self.total_elements = m.get('TotalElements')

        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')

        return self

class ListDataAgentAccuracyTestResultsResponseBodyDataContent(DaraModel):
    def __init__(
        self,
        accuracy_test_task_id: str = None,
        agent_result: str = None,
        agent_sql: str = None,
        answer_result: str = None,
        answer_sql: str = None,
        is_true: bool = None,
        question: str = None,
        reason: str = None,
        recommendation: str = None,
        result_id: str = None,
        session_id: str = None,
        subtask_id: str = None,
    ):
        # The ID of the accuracy test task.
        self.accuracy_test_task_id = accuracy_test_task_id
        # The actual answer from the agent.
        self.agent_result = agent_result
        self.agent_sql = agent_sql
        # The expected answer.
        self.answer_result = answer_result
        # The expected SQL.
        self.answer_sql = answer_sql
        # The AI evaluation result.
        self.is_true = is_true
        # The test question.
        self.question = question
        # The error reason.
        self.reason = reason
        # The improvement suggestion.
        self.recommendation = recommendation
        # The result ID.
        self.result_id = result_id
        self.session_id = session_id
        # The subtask ID.
        self.subtask_id = subtask_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accuracy_test_task_id is not None:
            result['AccuracyTestTaskId'] = self.accuracy_test_task_id

        if self.agent_result is not None:
            result['AgentResult'] = self.agent_result

        if self.agent_sql is not None:
            result['AgentSql'] = self.agent_sql

        if self.answer_result is not None:
            result['AnswerResult'] = self.answer_result

        if self.answer_sql is not None:
            result['AnswerSql'] = self.answer_sql

        if self.is_true is not None:
            result['IsTrue'] = self.is_true

        if self.question is not None:
            result['Question'] = self.question

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.recommendation is not None:
            result['Recommendation'] = self.recommendation

        if self.result_id is not None:
            result['ResultId'] = self.result_id

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.subtask_id is not None:
            result['SubtaskId'] = self.subtask_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccuracyTestTaskId') is not None:
            self.accuracy_test_task_id = m.get('AccuracyTestTaskId')

        if m.get('AgentResult') is not None:
            self.agent_result = m.get('AgentResult')

        if m.get('AgentSql') is not None:
            self.agent_sql = m.get('AgentSql')

        if m.get('AnswerResult') is not None:
            self.answer_result = m.get('AnswerResult')

        if m.get('AnswerSql') is not None:
            self.answer_sql = m.get('AnswerSql')

        if m.get('IsTrue') is not None:
            self.is_true = m.get('IsTrue')

        if m.get('Question') is not None:
            self.question = m.get('Question')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('Recommendation') is not None:
            self.recommendation = m.get('Recommendation')

        if m.get('ResultId') is not None:
            self.result_id = m.get('ResultId')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('SubtaskId') is not None:
            self.subtask_id = m.get('SubtaskId')

        return self

