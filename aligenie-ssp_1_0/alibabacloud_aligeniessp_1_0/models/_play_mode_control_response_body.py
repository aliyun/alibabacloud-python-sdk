# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aligeniessp_1_0 import models as main_models
from darabonba.model import DaraModel

class PlayModeControlResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: main_models.PlayModeControlResponseBodyResult = None,
        success: str = None,
    ):
        # Return code of the invocation
        self.code = code
        # Additional information, typically used to briefly describe a failed invocation to help the caller troubleshoot the issue.
        self.message = message
        # Request ID
        self.request_id = request_id
        # Actual return result of the service
        self.result = result
        # Indicates whether the invocation succeeded. true indicates success, and false indicates failure. When the value is false, check the Message field for details.
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
            temp_model = main_models.PlayModeControlResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class PlayModeControlResponseBodyResult(DaraModel):
    def __init__(
        self,
        open_play_mode: str = None,
    ):
        # Playback mode
        # 
        # List loop: Repeat; Shuffle: Shuffle; Single-track loop: RepeatOne; NAT mode: Normal;
        self.open_play_mode = open_play_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.open_play_mode is not None:
            result['OpenPlayMode'] = self.open_play_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpenPlayMode') is not None:
            self.open_play_mode = m.get('OpenPlayMode')

        return self

