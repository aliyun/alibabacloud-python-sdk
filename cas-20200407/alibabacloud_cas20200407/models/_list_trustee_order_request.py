# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTrusteeOrderRequest(DaraModel):
    def __init__(
        self,
        certificate_id: int = None,
        max_results: int = None,
        next_token: str = None,
        order_id: int = None,
    ):
        # The certificate ID. You must specify either CertificateId or OrderId. Both cannot be empty at the same time.
        self.certificate_id = certificate_id
        # The maximum number of records to return in this request.
        self.max_results = max_results
        # The token for the next query. If NextToken is empty, no more results are available.
        self.next_token = next_token
        # The order ID. You must specify either CertificateId or OrderId. Both cannot be empty at the same time.
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        return self

