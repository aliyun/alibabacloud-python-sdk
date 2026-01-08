# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_pai_dsw20220101 import models as main_models
from darabonba.model import DaraModel

class GetUserCommandResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        on_start: main_models.GetUserCommandResponseBodyOnStart = None,
        request_id: str = None,
        success: bool = None,
        user_command_id: str = None,
        access_denied_detail: Dict[str, Any] = None,
    ):
        self.code = code
        self.message = message
        self.on_start = on_start
        self.request_id = request_id
        self.success = success
        self.user_command_id = user_command_id
        self.access_denied_detail = access_denied_detail

    def validate(self):
        if self.on_start:
            self.on_start.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.on_start is not None:
            result['OnStart'] = self.on_start.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.user_command_id is not None:
            result['UserCommandId'] = self.user_command_id

        if self.access_denied_detail is not None:
            result['accessDeniedDetail'] = self.access_denied_detail

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('OnStart') is not None:
            temp_model = main_models.GetUserCommandResponseBodyOnStart()
            self.on_start = temp_model.from_map(m.get('OnStart'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('UserCommandId') is not None:
            self.user_command_id = m.get('UserCommandId')

        if m.get('accessDeniedDetail') is not None:
            self.access_denied_detail = m.get('accessDeniedDetail')

        return self

class GetUserCommandResponseBodyOnStart(DaraModel):
    def __init__(
        self,
        content: str = None,
    ):
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        return self

