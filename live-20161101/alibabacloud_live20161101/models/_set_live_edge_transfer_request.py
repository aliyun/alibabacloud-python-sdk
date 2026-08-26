# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetLiveEdgeTransferRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        domain_name: str = None,
        http_dns: str = None,
        owner_id: int = None,
        region_id: str = None,
        stream_name: str = None,
        target_domain_list: str = None,
        transfer_args: str = None,
    ):
        # The application name to which the live stream belongs. Regular expressions are supported for configuration with exceptions. For more information, see **AppName and StreamName Parameter Configuration Instructions** below. For example: liveApp****[1,2,3] indicates that the three apps liveApp****1, liveApp****2, and liveApp****3 are allowed for stream relay.
        # 
        # > - This parameter only takes effect for the TargetDomainList in the request parameters.
        # > - When configuring the `AppName` parameter value using regular expressions, the ^ or $ characters cannot be used, otherwise stream relay will fail.
        self.app_name = app_name
        # The ingest domain name. Live stream relay is configured at the granularity of the ingest DomainName. Each domain can have only one live stream relay configuration.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The HTTPDNS interface for obtaining the stream relay target address. The request must contain one of the `TargetDomainList` and `HttpDns` parameters, and the two are mutually exclusive.
        # 
        # > If `HttpDns` is set in the request parameters, the `TargetDomainList` parameter cannot be set, and the `AppName` and `StreamName` restrictions do not take effect.
        # 
        # Live stream relay has requirements for the message structure returned by the HTTPDNS interface. For more information, see **HTTPDNS Instructions** below.
        self.http_dns = http_dns
        self.owner_id = owner_id
        # The region ID.
        self.region_id = region_id
        # The stream name. Regular expressions are supported for configuration with exceptions. For more information, see **AppName and StreamName Parameter Configuration Instructions** below. For example: liveStream****[1,2,3] indicates that the three streams liveStream****1, liveStream****2, and liveStream****3 are allowed for stream relay.
        # 
        # > - This parameter only takes effect for the TargetDomainList in the request parameters.
        # > - When configuring the `StreamName` parameter value using regular expressions, the ^ or $ characters cannot be used, otherwise stream relay will fail.
        self.stream_name = stream_name
        # The list of target domains specified by the user for stream relay. Multiple domains are separated by commas (,). The request must contain one of the `TargetDomainList` and `HttpDns` parameters, and the two are mutually exclusive.
        # 
        # > - When `TargetDomainList` is set in the request parameters, the `AppName` and `StreamName` parameters take effect.
        # > - When `TargetDomainList` is set in the request parameters, the `HttpDns` parameter cannot be set.
        self.target_domain_list = target_domain_list
        # Specifies whether to pass through ingest parameters. Valid values:
        # - **yes**: Ingest parameters are passed through.
        # - **no** (default): Ingest parameters are not passed through.
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

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

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

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        if m.get('TargetDomainList') is not None:
            self.target_domain_list = m.get('TargetDomainList')

        if m.get('TransferArgs') is not None:
            self.transfer_args = m.get('TransferArgs')

        return self

