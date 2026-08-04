# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aligeniessp_1_0 import models as main_models
from darabonba.model import DaraModel

class GetAligenieUserInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: main_models.GetAligenieUserInfoResponseBodyResult = None,
        success: bool = None,
    ):
        # Response code
        self.code = code
        # Response message
        self.message = message
        # Request ID
        self.request_id = request_id
        self.result = result
        # Flag indicating whether the invocation succeeded
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.GetAligenieUserInfoResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetAligenieUserInfoResponseBodyResult(DaraModel):
    def __init__(
        self,
        aligenie_nickname: str = None,
        avatar: str = None,
        deletable: bool = None,
    ):
        # Aligenie user nickname
        self.aligenie_nickname = aligenie_nickname
        # URL of the Aligenie user profile picture
        self.avatar = avatar
        # Indicates whether the account can be logged off
        self.deletable = deletable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aligenie_nickname is not None:
            result['AligenieNickname'] = self.aligenie_nickname

        if self.avatar is not None:
            result['Avatar'] = self.avatar

        if self.deletable is not None:
            result['Deletable'] = self.deletable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AligenieNickname') is not None:
            self.aligenie_nickname = m.get('AligenieNickname')

        if m.get('Avatar') is not None:
            self.avatar = m.get('Avatar')

        if m.get('Deletable') is not None:
            self.deletable = m.get('Deletable')

        return self

