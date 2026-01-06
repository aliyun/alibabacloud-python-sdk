# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeletePCACertRequest(DaraModel):
    def __init__(
        self,
        identifier: str = None,
    ):
        # The unique identifier of the certificate. You can call the [ListCert](https://help.aliyun.com/document_detail/452331.html) operation to query the unique identifiers of certificates.
        # 
        # This parameter is required.
        self.identifier = identifier

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.identifier is not None:
            result['Identifier'] = self.identifier

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')

        return self

