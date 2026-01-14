# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ValidateModuleResponseBody(DaraModel):
    def __init__(
        self,
        message: str = None,
        module_validation_id: str = None,
        request_id: str = None,
        status: str = None,
    ):
        self.message = message
        self.module_validation_id = module_validation_id
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['message'] = self.message

        if self.module_validation_id is not None:
            result['moduleValidationId'] = self.module_validation_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('moduleValidationId') is not None:
            self.module_validation_id = m.get('moduleValidationId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

