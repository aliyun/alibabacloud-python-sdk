# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SendVerificationCodeForBindSecureMobilePhoneResponseBody(DaraModel):
    def __init__(
        self,
        expiration_date: str = None,
        request_id: str = None,
    ):
        # The time when the verification code expires.
        self.expiration_date = expiration_date
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expiration_date is not None:
            result['ExpirationDate'] = self.expiration_date

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpirationDate') is not None:
            self.expiration_date = m.get('ExpirationDate')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

