# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentteams20260605 import models as main_models
from darabonba.model import DaraModel

class GetInstanceAsyncTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        items: List[main_models.GetInstanceAsyncTaskResponseBodyItems] = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.items = items
        self.max_results = max_results
        self.message = message
        self.next_token = next_token
        self.request_id = request_id
        self.success = success
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

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.message is not None:
            result['Message'] = self.message

        if self.next_token is not None:
            result['NextToken'] = self.next_token

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
                temp_model = main_models.GetInstanceAsyncTaskResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class GetInstanceAsyncTaskResponseBodyItems(DaraModel):
    def __init__(
        self,
        current_step: str = None,
        recovery_message: main_models.GetInstanceAsyncTaskResponseBodyItemsRecoveryMessage = None,
        task_code: str = None,
        task_id: str = None,
        task_status: str = None,
        waiting_for_user_action: bool = None,
    ):
        self.current_step = current_step
        self.recovery_message = recovery_message
        self.task_code = task_code
        self.task_id = task_id
        self.task_status = task_status
        self.waiting_for_user_action = waiting_for_user_action

    def validate(self):
        if self.recovery_message:
            self.recovery_message.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_step is not None:
            result['CurrentStep'] = self.current_step

        if self.recovery_message is not None:
            result['RecoveryMessage'] = self.recovery_message.to_map()

        if self.task_code is not None:
            result['TaskCode'] = self.task_code

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        if self.waiting_for_user_action is not None:
            result['WaitingForUserAction'] = self.waiting_for_user_action

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentStep') is not None:
            self.current_step = m.get('CurrentStep')

        if m.get('RecoveryMessage') is not None:
            temp_model = main_models.GetInstanceAsyncTaskResponseBodyItemsRecoveryMessage()
            self.recovery_message = temp_model.from_map(m.get('RecoveryMessage'))

        if m.get('TaskCode') is not None:
            self.task_code = m.get('TaskCode')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('WaitingForUserAction') is not None:
            self.waiting_for_user_action = m.get('WaitingForUserAction')

        return self

class GetInstanceAsyncTaskResponseBodyItemsRecoveryMessage(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        occurred_at: str = None,
        recovery_suggestion: str = None,
        retryable: bool = None,
        source: str = None,
        type: str = None,
    ):
        self.code = code
        self.message = message
        self.occurred_at = occurred_at
        self.recovery_suggestion = recovery_suggestion
        self.retryable = retryable
        self.source = source
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.occurred_at is not None:
            result['OccurredAt'] = self.occurred_at

        if self.recovery_suggestion is not None:
            result['RecoverySuggestion'] = self.recovery_suggestion

        if self.retryable is not None:
            result['Retryable'] = self.retryable

        if self.source is not None:
            result['Source'] = self.source

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('OccurredAt') is not None:
            self.occurred_at = m.get('OccurredAt')

        if m.get('RecoverySuggestion') is not None:
            self.recovery_suggestion = m.get('RecoverySuggestion')

        if m.get('Retryable') is not None:
            self.retryable = m.get('Retryable')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

