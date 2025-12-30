# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class DetectAudioForCustomizedVoiceJobResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DetectAudioForCustomizedVoiceJobResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The data returned.
        self.data = data
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values: true false
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
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DetectAudioForCustomizedVoiceJobResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DetectAudioForCustomizedVoiceJobResponseBodyData(DaraModel):
    def __init__(
        self,
        pass_: bool = None,
        reason: str = None,
    ):
        # Indicates whether the audio file passes the check. Valid values:
        # 
        # *   true
        # *   false
        self.pass_ = pass_
        # The reason returned if the audio file failed to pass the check.
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pass_ is not None:
            result['Pass'] = self.pass_

        if self.reason is not None:
            result['Reason'] = self.reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pass') is not None:
            self.pass_ = m.get('Pass')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        return self

