# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeClientCertificateStatusRequest(DaraModel):
    def __init__(
        self,
        identifier: str = None,
    ):
        # The unique identifiers of the client certificates or server certificates that you want to query. Separate multiple unique identifiers with commas (,).
        # 
        # >  You can call the [ListClientCertificate](https://help.aliyun.com/document_detail/330884.html) operation to query the unique identifiers of all client certificates and server certificates.
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

