# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateMailAddressResponseBody(DaraModel):
    def __init__(
        self,
        mail_address_id: str = None,
        request_id: str = None,
    ):
        # Mail address ID
        self.mail_address_id = mail_address_id
        # Request ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mail_address_id is not None:
            result['MailAddressId'] = self.mail_address_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MailAddressId') is not None:
            self.mail_address_id = m.get('MailAddressId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

