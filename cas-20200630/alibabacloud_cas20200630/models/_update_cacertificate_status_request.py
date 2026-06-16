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
        # A client token used to ensure the idempotence of the request.
        # 
        # Generate a unique parameter value from your client for each request. The ClientToken parameter supports only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** of each API request is different.
        self.client_token = client_token
        # The unique identifier of the CA certificate.
        # 
        # > Call [DescribeCACertificateList](https://help.aliyun.com/document_detail/465957.html) to query the unique identifiers of all CA certificates.
        # 
        # This parameter is required.
        self.identifier = identifier
        # The operation to perform on the CA certificate. Set the value to **REVOKE**. This revokes the CA certificate and changes its status to **REVOKE**.
        # 
        # > This operation is supported only when the CA certificate is in the **ISSUE** state. Call [DescribeCACertificate](https://help.aliyun.com/document_detail/465954.html) to query the current status of the CA certificate.
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

