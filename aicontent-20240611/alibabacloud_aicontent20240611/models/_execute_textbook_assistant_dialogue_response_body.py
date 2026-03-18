# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aicontent20240611 import models as main_models
from darabonba.model import DaraModel

class ExecuteTextbookAssistantDialogueResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ExecuteTextbookAssistantDialogueResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        # Id of the request
        self.request_id = request_id
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
            result['data'] = self.data.to_map()

        if self.err_code is not None:
            result['errCode'] = self.err_code

        if self.err_message is not None:
            result['errMessage'] = self.err_message

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.ExecuteTextbookAssistantDialogueResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')

        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class ExecuteTextbookAssistantDialogueResponseBodyData(DaraModel):
    def __init__(
        self,
        assistant: str = None,
        chat_id: str = None,
        result: main_models.ExecuteTextbookAssistantDialogueResponseBodyDataResult = None,
        user: str = None,
    ):
        self.assistant = assistant
        self.chat_id = chat_id
        self.result = result
        self.user = user

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assistant is not None:
            result['assistant'] = self.assistant

        if self.chat_id is not None:
            result['chatId'] = self.chat_id

        if self.result is not None:
            result['result'] = self.result.to_map()

        if self.user is not None:
            result['user'] = self.user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('assistant') is not None:
            self.assistant = m.get('assistant')

        if m.get('chatId') is not None:
            self.chat_id = m.get('chatId')

        if m.get('result') is not None:
            temp_model = main_models.ExecuteTextbookAssistantDialogueResponseBodyDataResult()
            self.result = temp_model.from_map(m.get('result'))

        if m.get('user') is not None:
            self.user = m.get('user')

        return self

class ExecuteTextbookAssistantDialogueResponseBodyDataResult(DaraModel):
    def __init__(
        self,
        chinese_result: str = None,
        english_result: str = None,
        is_finish: bool = None,
        is_task_completed: bool = None,
    ):
        self.chinese_result = chinese_result
        self.english_result = english_result
        self.is_finish = is_finish
        self.is_task_completed = is_task_completed

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chinese_result is not None:
            result['chineseResult'] = self.chinese_result

        if self.english_result is not None:
            result['englishResult'] = self.english_result

        if self.is_finish is not None:
            result['isFinish'] = self.is_finish

        if self.is_task_completed is not None:
            result['isTaskCompleted'] = self.is_task_completed

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chineseResult') is not None:
            self.chinese_result = m.get('chineseResult')

        if m.get('englishResult') is not None:
            self.english_result = m.get('englishResult')

        if m.get('isFinish') is not None:
            self.is_finish = m.get('isFinish')

        if m.get('isTaskCompleted') is not None:
            self.is_task_completed = m.get('isTaskCompleted')

        return self

