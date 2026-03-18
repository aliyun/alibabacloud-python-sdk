# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aicontent20240611 import models as main_models
from darabonba.model import DaraModel

class ExecuteAITeacherExpansionDialogueResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ExecuteAITeacherExpansionDialogueResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
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
            temp_model = main_models.ExecuteAITeacherExpansionDialogueResponseBodyData()
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

class ExecuteAITeacherExpansionDialogueResponseBodyData(DaraModel):
    def __init__(
        self,
        chinese_result: str = None,
        english_result: str = None,
        is_finish: bool = None,
        is_off_topic_control: bool = None,
        is_on_topic: bool = None,
        question_index: int = None,
    ):
        self.chinese_result = chinese_result
        self.english_result = english_result
        self.is_finish = is_finish
        self.is_off_topic_control = is_off_topic_control
        self.is_on_topic = is_on_topic
        self.question_index = question_index

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

        if self.is_off_topic_control is not None:
            result['isOffTopicControl'] = self.is_off_topic_control

        if self.is_on_topic is not None:
            result['isOnTopic'] = self.is_on_topic

        if self.question_index is not None:
            result['questionIndex'] = self.question_index

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chineseResult') is not None:
            self.chinese_result = m.get('chineseResult')

        if m.get('englishResult') is not None:
            self.english_result = m.get('englishResult')

        if m.get('isFinish') is not None:
            self.is_finish = m.get('isFinish')

        if m.get('isOffTopicControl') is not None:
            self.is_off_topic_control = m.get('isOffTopicControl')

        if m.get('isOnTopic') is not None:
            self.is_on_topic = m.get('isOnTopic')

        if m.get('questionIndex') is not None:
            self.question_index = m.get('questionIndex')

        return self

