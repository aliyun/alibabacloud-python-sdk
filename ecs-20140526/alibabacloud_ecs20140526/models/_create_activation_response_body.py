# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateActivationResponseBody(DaraModel):
    def __init__(
        self,
        activation_code: str = None,
        activation_id: str = None,
        request_id: str = None,
    ):
        # The value of the activation code. The code is returned only once when you call this operation and cannot be queried afterward. Store the return value properly.
        self.activation_code = activation_code
        # The activation code ID.
        self.activation_id = activation_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activation_code is not None:
            result['ActivationCode'] = self.activation_code

        if self.activation_id is not None:
            result['ActivationId'] = self.activation_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivationCode') is not None:
            self.activation_code = m.get('ActivationCode')

        if m.get('ActivationId') is not None:
            self.activation_id = m.get('ActivationId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

