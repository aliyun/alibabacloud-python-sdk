# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateCACertificateStatusRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        identifier: str = None,
        status: str = None,
    ):
        self.client_token = client_token
        # The unique identifier of the CA certificate whose status you want to change.
        # 
        # >  You can call the [DescribeCACertificateList](https://help.aliyun.com/document_detail/328095.html) operation to query the unique identifiers of all CA certificates.
        # 
        # This parameter is required.
        self.identifier = identifier
        # The state to which you want to change the CA certificate. Set to the value to **REVOKE**. After this operation is called, the status of the CA certificate is changed to **REVOKE**.
        # 
        # >  You can call this operation only if the status of a CA certificate is **ISSUE**. You can call the [DescribeCACertificate](https://help.aliyun.com/document_detail/328096.html) operation to query the status of a CA certificate.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.identifier is not None:
            result['Identifier'] = self.identifier

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

