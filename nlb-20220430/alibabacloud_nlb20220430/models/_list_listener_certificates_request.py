# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListListenerCertificatesRequest(DaraModel):
    def __init__(
        self,
        cert_type: str = None,
        certificate_ids: List[str] = None,
        listener_id: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
    ):
        # The certificate type. Valid values:
        # 
        # - **Ca**: CA certificate.
        # - **Server**: Server certificate.
        self.cert_type = cert_type
        # The server certificates. You can add only one server certificate.
        # 
        # > This parameter takes effect only for TCPSSL listeners.
        self.certificate_ids = certificate_ids
        # The listener ID. This parameter is valid only for TCPSSL listeners.
        # 
        # This parameter is required.
        self.listener_id = listener_id
        # The number of entries to return per page. Valid values: **1** to **50**. Default value: **20**.
        self.max_results = max_results
        # The pagination token for the next query.
        # - Leave this parameter empty for the first query or when no subsequent query is required.
        # - For subsequent queries, set this parameter to the NextToken value returned by the previous API call.
        self.next_token = next_token
        # The region ID of the Network Load Balancer (NLB) instance.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/443657.html) operation to query region IDs.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_type is not None:
            result['CertType'] = self.cert_type

        if self.certificate_ids is not None:
            result['CertificateIds'] = self.certificate_ids

        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')

        if m.get('CertificateIds') is not None:
            self.certificate_ids = m.get('CertificateIds')

        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

