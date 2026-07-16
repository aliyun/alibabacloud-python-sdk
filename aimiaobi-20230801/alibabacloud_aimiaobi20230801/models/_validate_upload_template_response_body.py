# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class ValidateUploadTemplateResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ValidateUploadTemplateResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Status code.
        self.code = code
        # Template validation result.
        self.data = data
        # HTTP status code.
        self.http_status_code = http_status_code
        # Error message.
        self.message = message
        # Unique request identifier.
        self.request_id = request_id
        # Operation status. Returns true on success. Returns false on failure.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

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

        if m.get('Data') is not None:
            temp_model = main_models.ValidateUploadTemplateResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ValidateUploadTemplateResponseBodyData(DaraModel):
    def __init__(
        self,
        comment_count: int = None,
        dialogue_count: int = None,
        total_count: int = None,
    ):
        # Number of comments.
        self.comment_count = comment_count
        # Number of dialogues.
        self.dialogue_count = dialogue_count
        # Total count.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment_count is not None:
            result['CommentCount'] = self.comment_count

        if self.dialogue_count is not None:
            result['DialogueCount'] = self.dialogue_count

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommentCount') is not None:
            self.comment_count = m.get('CommentCount')

        if m.get('DialogueCount') is not None:
            self.dialogue_count = m.get('DialogueCount')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

