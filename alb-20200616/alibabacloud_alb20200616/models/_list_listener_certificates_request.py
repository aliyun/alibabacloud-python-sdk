# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListListenerCertificatesRequest(DaraModel):
    def __init__(
        self,
        certificate_ids: List[str] = None,
        certificate_type: str = None,
        listener_id: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # The certificates.
        self.certificate_ids = certificate_ids
        # The type of the certificate. Valid values: **Ca** and **Server**.
        self.certificate_type = certificate_type
        # The listener ID. You must specify the ID of an HTTPS listener or a QUIC listener.
        # 
        # This parameter is required.
        self.listener_id = listener_id
        # The number of entries to return in each call. Valid values: **1 to 100**. Default value: **20**.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   You do not need to specify this parameter for the first request.
        # *   You must specify the token that is obtained from the previous query as the value of **NextToken**.
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.certificate_ids is not None:
            result['CertificateIds'] = self.certificate_ids

        if self.certificate_type is not None:
            result['CertificateType'] = self.certificate_type

        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateIds') is not None:
            self.certificate_ids = m.get('CertificateIds')

        if m.get('CertificateType') is not None:
            self.certificate_type = m.get('CertificateType')

        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

