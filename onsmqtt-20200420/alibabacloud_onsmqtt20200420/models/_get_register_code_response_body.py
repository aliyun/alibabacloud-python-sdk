# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetRegisterCodeResponseBody(DaraModel):
    def __init__(
        self,
        register_code: str = None,
        request_id: str = None,
    ):
        # The registration code of the CA certificate.
        self.register_code = register_code
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.register_code is not None:
            result['RegisterCode'] = self.register_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegisterCode') is not None:
            self.register_code = m.get('RegisterCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

