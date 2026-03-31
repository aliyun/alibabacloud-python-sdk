# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StopConfigurationRecorderResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        stop_configuration_recorder_result: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.stop_configuration_recorder_result = stop_configuration_recorder_result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.stop_configuration_recorder_result is not None:
            result['StopConfigurationRecorderResult'] = self.stop_configuration_recorder_result

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StopConfigurationRecorderResult') is not None:
            self.stop_configuration_recorder_result = m.get('StopConfigurationRecorderResult')

        return self

