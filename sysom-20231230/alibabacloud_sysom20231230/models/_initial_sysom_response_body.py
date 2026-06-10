# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sysom20231230 import models as main_models
from darabonba.model import DaraModel

class InitialSysomResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: main_models.InitialSysomResponseBodyData = None,
        message: str = None,
    ):
        # Request ID, which can be used for end-to-end diagnosis
        self.request_id = request_id
        # Status code  
        # - If `code == Success`, authorization succeeded.  
        # - Any other status code indicates a failed authorization. In such cases, view the `message` field for detailed error information.
        self.code = code
        # Return Result.
        self.data = data
        # Error message  
        # - If `code == Success`, this field is empty.  
        # - Otherwise, this field contains the error message.
        self.message = message

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.InitialSysomResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        return self

class InitialSysomResponseBodyData(DaraModel):
    def __init__(
        self,
        role_exist: bool = None,
    ):
        # Indicates whether the service role exists
        self.role_exist = role_exist

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.role_exist is not None:
            result['role_exist'] = self.role_exist

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('role_exist') is not None:
            self.role_exist = m.get('role_exist')

        return self

