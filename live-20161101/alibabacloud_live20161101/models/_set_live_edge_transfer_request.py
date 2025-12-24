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
        # The name of the application to which the live stream belongs. Regular expressions are supported, with a few limits. For more information, see the **Description about the AppName and StreamName parameters** section. For example, a value of **liveApp\\*\\*\\*\\*[1,2,3]** specifies that stream relay is configured for three applications: liveApp\\*\\*\\*\\*1, liveApp\\*\\*\\*\\*2, and liveApp\\*\\*\\*\\*3.****
        # 
        # > 
        # 
        # *   This parameter takes effect for only destination domain names that are specified by the TargetDomainList parameter.
        # 
        # *   You cannot use a caret (^) or a dollar sign ($) in a regular expression to configure the `AppName` parameter. Otherwise, stream relay fails.
        self.app_name = app_name
        # The ingest domain. Stream relay is configured based on the ingest domain. Only one stream relay configuration can be set for an ingest domain.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The HTTPDNS API that is used to obtain the destination URLs. The request must contain the `TargetDomainList` parameter or the `HttpDns` parameter. The two parameters are mutually exclusive.
        # 
        # >  If the `HttpDns` parameter is configured, you cannot configure the `TargetDomainList` parameter, and the `AppName` and `StreamName` parameters do not take effect.
        # 
        # For information about the requirements on the structure of messages that are returned by the HTTPDNS API, see the **Description about the HTTPDNS API** section.
        self.http_dns = http_dns
        self.owner_id = owner_id
        self.region_id = region_id
        # The name of the ingested stream. Regular expressions are supported, with a few limits. For more information, see the **Description about the AppName and StreamName parameters** section. For example, a value of **liveStream\\*\\*\\*\\*[1,2,3]** specifies that stream relay is configured for three streams: liveStream\\*\\*\\*\\*1, liveStream\\*\\*\\*\\*2, and liveStream\\*\\*\\*\\*3.****
        # 
        # > 
        # 
        # *   This parameter takes effect for only destination domain names that are specified by the TargetDomainList parameter.
        # 
        # *   You cannot use a caret (^) or a dollar sign ($) in a regular expression to configure the `StreamName` parameter. Otherwise, stream relay fails.
        self.stream_name = stream_name
        # The destination domain names to which you want to relay the ingested stream. Separate multiple domain names with commas (,). The request must contain the `TargetDomainList` parameter or the `HttpDns` parameter. The two parameters are mutually exclusive.
        # 
        # > 
        # 
        # *   The `AppName` and `StreamName` parameters take effect only when the `TargetDomainList` parameter is configured.
        # 
        # *   If the `TargetDomainList` parameter is configured, you cannot configure the `HttpDns` parameter.
        self.target_domain_list = target_domain_list
        # Specifies whether to pass through stream ingest parameters. Valid values:
        # 
        # *   **yes**: passes through stream ingest parameters.
        # *   **no**: does not pass through stream ingest parameters.
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

