# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_outboundbot20191226 import models as main_models
from darabonba.model import DaraModel

class DialogueResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        feedback: main_models.DialogueResponseBodyFeedback = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.feedback = feedback
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.feedback:
            self.feedback.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.feedback is not None:
            result['Feedback'] = self.feedback.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Feedback') is not None:
            temp_model = main_models.DialogueResponseBodyFeedback()
            self.feedback = temp_model.from_map(m.get('Feedback'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DialogueResponseBodyFeedback(DaraModel):
    def __init__(
        self,
        action: str = None,
        action_params: str = None,
        content: str = None,
        content_params: str = None,
        interruptible: bool = None,
    ):
        self.action = action
        self.action_params = action_params
        self.content = content
        # 已废弃
        self.content_params = content_params
        self.interruptible = interruptible

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.action_params is not None:
            result['ActionParams'] = self.action_params

        if self.content is not None:
            result['Content'] = self.content

        if self.content_params is not None:
            result['ContentParams'] = self.content_params

        if self.interruptible is not None:
            result['Interruptible'] = self.interruptible

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('ActionParams') is not None:
            self.action_params = m.get('ActionParams')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('ContentParams') is not None:
            self.content_params = m.get('ContentParams')

        if m.get('Interruptible') is not None:
            self.interruptible = m.get('Interruptible')

        return self

