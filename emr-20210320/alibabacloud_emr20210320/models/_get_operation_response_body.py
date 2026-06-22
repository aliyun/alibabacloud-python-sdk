# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class GetOperationResponseBody(DaraModel):
    def __init__(
        self,
        operation: main_models.Operation = None,
        request_id: str = None,
    ):
        # The operation that was performed.
        self.operation = operation
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.operation:
            self.operation.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.operation is not None:
            result['Operation'] = self.operation.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Operation') is not None:
            temp_model = main_models.Operation()
            self.operation = temp_model.from_map(m.get('Operation'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

