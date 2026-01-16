# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChangeDomainDkimRecordResponseBody(DaraModel):
    def __init__(
        self,
        changed: bool = None,
        dkim_public_key: str = None,
        dkim_rsa_length: int = None,
        hostname: str = None,
        request_id: str = None,
    ):
        self.changed = changed
        self.dkim_public_key = dkim_public_key
        self.dkim_rsa_length = dkim_rsa_length
        self.hostname = hostname
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.changed is not None:
            result['Changed'] = self.changed

        if self.dkim_public_key is not None:
            result['DkimPublicKey'] = self.dkim_public_key

        if self.dkim_rsa_length is not None:
            result['DkimRsaLength'] = self.dkim_rsa_length

        if self.hostname is not None:
            result['Hostname'] = self.hostname

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Changed') is not None:
            self.changed = m.get('Changed')

        if m.get('DkimPublicKey') is not None:
            self.dkim_public_key = m.get('DkimPublicKey')

        if m.get('DkimRsaLength') is not None:
            self.dkim_rsa_length = m.get('DkimRsaLength')

        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

