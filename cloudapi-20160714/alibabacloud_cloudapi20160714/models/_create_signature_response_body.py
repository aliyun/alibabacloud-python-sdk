# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSignatureResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        signature_id: str = None,
        signature_name: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The ID of the back-end signature key.
        self.signature_id = signature_id
        # The name of the back-end signature key.
        self.signature_name = signature_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.signature_id is not None:
            result['SignatureId'] = self.signature_id

        if self.signature_name is not None:
            result['SignatureName'] = self.signature_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SignatureId') is not None:
            self.signature_id = m.get('SignatureId')

        if m.get('SignatureName') is not None:
            self.signature_name = m.get('SignatureName')

        return self

