# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from alibabacloud_appflow20230904 import models as main_models
from darabonba.model import DaraModel

class InvokeActionResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.InvokeActionResponseBodyResult = None,
    ):
        # Id of the request
        self.request_id = request_id
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
            temp_model = main_models.InvokeActionResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class InvokeActionResponseBodyResult(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        output: Any = None,
        status: str = None,
    ):
        self.error_message = error_message
        self.output = output
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.output is not None:
            result['Output'] = self.output

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('Output') is not None:
            self.output = m.get('Output')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

