# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteBeebotIntentUserSayResponseBody(DaraModel):
    def __init__(
        self,
        beebot_request_id: str = None,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        user_say_id: int = None,
    ):
        self.beebot_request_id = beebot_request_id
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.user_say_id = user_say_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.beebot_request_id is not None:
            result['BeebotRequestId'] = self.beebot_request_id

        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.user_say_id is not None:
            result['UserSayId'] = self.user_say_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeebotRequestId') is not None:
            self.beebot_request_id = m.get('BeebotRequestId')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('UserSayId') is not None:
            self.user_say_id = m.get('UserSayId')

        return self

