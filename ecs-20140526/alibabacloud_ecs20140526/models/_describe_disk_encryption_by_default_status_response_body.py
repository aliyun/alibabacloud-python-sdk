# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDiskEncryptionByDefaultStatusResponseBody(DaraModel):
    def __init__(
        self,
        encrypted: bool = None,
        request_id: str = None,
    ):
        # Indicates whether account-level default encryption of EBS resources is enabled in the region. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        self.encrypted = encrypted
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

