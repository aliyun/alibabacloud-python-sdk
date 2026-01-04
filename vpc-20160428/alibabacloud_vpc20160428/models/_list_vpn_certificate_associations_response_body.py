# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class ListVpnCertificateAssociationsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
        vpn_certificate_relations: List[main_models.ListVpnCertificateAssociationsResponseBodyVpnCertificateRelations] = None,
    ):
        # The number of entries returned per page.
        self.max_results = max_results
        # The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If **NextToken** is empty, no next page exists.
        # *   If **NextToken** is not empty, the value indicates the token that is used for the next query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count
        # The association information.
        self.vpn_certificate_relations = vpn_certificate_relations

    def validate(self):
        if self.vpn_certificate_relations:
            for v1 in self.vpn_certificate_relations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['VpnCertificateRelations'] = []
        if self.vpn_certificate_relations is not None:
            for k1 in self.vpn_certificate_relations:
                result['VpnCertificateRelations'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.vpn_certificate_relations = []
        if m.get('VpnCertificateRelations') is not None:
            for k1 in m.get('VpnCertificateRelations'):
                temp_model = main_models.ListVpnCertificateAssociationsResponseBodyVpnCertificateRelations()
                self.vpn_certificate_relations.append(temp_model.from_map(k1))

        return self

class ListVpnCertificateAssociationsResponseBodyVpnCertificateRelations(DaraModel):
    def __init__(
        self,
        association_time: str = None,
        certificate_id: str = None,
        certificate_type: str = None,
        region_id: str = None,
        vpn_gateway_id: str = None,
    ):
        # The time when the Anycast EIP was associated.
        # 
        # The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC.
        self.association_time = association_time
        # The certificate ID.
        self.certificate_id = certificate_id
        # The type of the certificate.
        # 
        # *   **Encryption**
        # *   **Signature**
        self.certificate_type = certificate_type
        # The ID of the region where the VPN gateway is created.
        self.region_id = region_id
        # The ID of the VPN gateway.
        self.vpn_gateway_id = vpn_gateway_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.association_time is not None:
            result['AssociationTime'] = self.association_time

        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id

        if self.certificate_type is not None:
            result['CertificateType'] = self.certificate_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.vpn_gateway_id is not None:
            result['VpnGatewayId'] = self.vpn_gateway_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssociationTime') is not None:
            self.association_time = m.get('AssociationTime')

        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')

        if m.get('CertificateType') is not None:
            self.certificate_type = m.get('CertificateType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('VpnGatewayId') is not None:
            self.vpn_gateway_id = m.get('VpnGatewayId')

        return self

