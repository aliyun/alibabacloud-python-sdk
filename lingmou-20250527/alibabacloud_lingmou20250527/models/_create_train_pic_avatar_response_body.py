# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_lingmou20250527 import models as main_models
from darabonba.model import DaraModel

class CreateTrainPicAvatarResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.CreateTrainPicAvatarResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.CreateTrainPicAvatarResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class CreateTrainPicAvatarResponseBodyData(DaraModel):
    def __init__(
        self,
        avatar_id: str = None,
        expected_completion_time: int = None,
        pass_: bool = None,
    ):
        self.avatar_id = avatar_id
        self.expected_completion_time = expected_completion_time
        self.pass_ = pass_

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avatar_id is not None:
            result['avatarId'] = self.avatar_id

        if self.expected_completion_time is not None:
            result['expectedCompletionTime'] = self.expected_completion_time

        if self.pass_ is not None:
            result['pass'] = self.pass_

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('avatarId') is not None:
            self.avatar_id = m.get('avatarId')

        if m.get('expectedCompletionTime') is not None:
            self.expected_completion_time = m.get('expectedCompletionTime')

        if m.get('pass') is not None:
            self.pass_ = m.get('pass')

        return self

