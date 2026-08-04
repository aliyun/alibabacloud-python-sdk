# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aligeniessp_1_0 import models as main_models
from darabonba.model import DaraModel

class ThirdImmediateMsgPushResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        model: main_models.ThirdImmediateMsgPushResponseBodyModel = None,
        success: bool = None,
    ):
        # error code
        self.error_code = error_code
        # error message
        self.error_msg = error_msg
        # push result
        self.model = model
        # whether the invocation succeeded
        self.success = success

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.model is not None:
            result['Model'] = self.model.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('Model') is not None:
            temp_model = main_models.ThirdImmediateMsgPushResponseBodyModel()
            self.model = temp_model.from_map(m.get('Model'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ThirdImmediateMsgPushResponseBodyModel(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        # request ID
        self.request_id = request_id
        # whether the push succeeded
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

