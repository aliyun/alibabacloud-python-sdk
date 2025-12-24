# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class CancelMuteAllGroupUserResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.CancelMuteAllGroupUserResponseBodyResult = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The returned result.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.CancelMuteAllGroupUserResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class CancelMuteAllGroupUserResponseBodyResult(DaraModel):
    def __init__(
        self,
        success: bool = None,
    ):
        # Indicates whether the cancellation was successful, with values:
        # - true: Success. 
        # - false: Not successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

