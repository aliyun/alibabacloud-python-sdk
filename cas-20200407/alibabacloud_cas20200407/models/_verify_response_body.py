# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class VerifyResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        signature_valid: bool = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the signature is valid. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.signature_valid = signature_valid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.signature_valid is not None:
            result['SignatureValid'] = self.signature_valid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SignatureValid') is not None:
            self.signature_valid = m.get('SignatureValid')

        return self

