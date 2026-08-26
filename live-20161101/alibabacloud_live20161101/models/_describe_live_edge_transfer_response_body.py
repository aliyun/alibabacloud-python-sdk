# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLiveEdgeTransferResponseBody(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        domain_name: str = None,
        http_dns: str = None,
        request_id: str = None,
        stream_name: str = None,
        target_domain_list: str = None,
        transfer_args: str = None,
    ):
        # The name of the application to which the live stream belongs.
        self.app_name = app_name
        # The ingest domain.
        self.domain_name = domain_name
        # The URL of the HTTPDNS service used to resolve the addresses of the target domains.
        self.http_dns = http_dns
        # The request ID.
        self.request_id = request_id
        # The name of the ingested live stream.
        self.stream_name = stream_name
        # A comma-separated list of the target domains where the stream is forwarded.
        self.target_domain_list = target_domain_list
        # Indicates whether the query parameters from the original ingest URL are passed through to the target URL.
        # 
        # - **yes**: The parameters are passed through.
        # 
        # - **no**: The parameters are not passed through.
        self.transfer_args = transfer_args

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.http_dns is not None:
            result['HttpDns'] = self.http_dns

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        if self.target_domain_list is not None:
            result['TargetDomainList'] = self.target_domain_list

        if self.transfer_args is not None:
            result['TransferArgs'] = self.transfer_args

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('HttpDns') is not None:
            self.http_dns = m.get('HttpDns')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        if m.get('TargetDomainList') is not None:
            self.target_domain_list = m.get('TargetDomainList')

        if m.get('TransferArgs') is not None:
            self.transfer_args = m.get('TransferArgs')

        return self

