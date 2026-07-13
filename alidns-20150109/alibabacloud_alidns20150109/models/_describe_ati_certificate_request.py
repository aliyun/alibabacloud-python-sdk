# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAtiCertificateRequest(DaraModel):
    def __init__(
        self,
        agent_certificate_id: str = None,
        client_token: str = None,
    ):
        # The ID of the certificate to query. Call the ListAtiCertificates operation to query the target certificate information and obtain the ID from the response.
        self.agent_certificate_id = agent_certificate_id
        # The client token that is used to ensure the idempotence of the request.
        # 
        # Generate a parameter value from your client to ensure that the value is unique among different requests. ClientToken supports only ASCII characters.
        # 
        # > If you do not specify this parameter, the system uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** of each API request is different.
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_certificate_id is not None:
            result['AgentCertificateId'] = self.agent_certificate_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentCertificateId') is not None:
            self.agent_certificate_id = m.get('AgentCertificateId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        return self

