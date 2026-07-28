# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListVpnCertificateAssociationsRequest(DaraModel):
    def __init__(
        self,
        certificate_id: List[str] = None,
        certificate_type: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        vpn_gateway_id: List[str] = None,
    ):
        # The list of certificate IDs.
        # 
        # You can query the associations between up to 20 SSL certificates and VPN gateway instances at a time.
        self.certificate_id = certificate_id
        # The certificate type. Valid values:
        # 
        # - **Encryption**: encryption certificate.
        # 
        # - **Signature**: signing certificate.
        self.certificate_type = certificate_type
        # The number of entries per page. Valid values: **1** to **20**. Default value: **10**.
        self.max_results = max_results
        # The token for the next query. Valid values:
        # 
        # - If this is the first query or no next query exists, leave this parameter empty.
        # 
        # - If a next query exists, set this parameter to the **NextToken** value returned by the previous API call.
        self.next_token = next_token
        # The region ID of the VPN gateway.
        # 
        # You can call [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) to query the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The list of VPN gateway instance IDs.
        # 
        # You can query the associations between up to 20 VPN gateway instances and SSL certificates at a time.
        self.vpn_gateway_id = vpn_gateway_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id

        if self.certificate_type is not None:
            result['CertificateType'] = self.certificate_type

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.vpn_gateway_id is not None:
            result['VpnGatewayId'] = self.vpn_gateway_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')

        if m.get('CertificateType') is not None:
            self.certificate_type = m.get('CertificateType')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('VpnGatewayId') is not None:
            self.vpn_gateway_id = m.get('VpnGatewayId')

        return self

