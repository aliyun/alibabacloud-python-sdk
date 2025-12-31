# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCACertificateListRequest(DaraModel):
    def __init__(
        self,
        ca_status: str = None,
        cert_type: str = None,
        current_page: int = None,
        identifier: str = None,
        issuer_type: str = None,
        resource_group_id: str = None,
        show_size: int = None,
        valid_status: str = None,
    ):
        # Ca status.
        # 
        # - issue: inUse.
        # - forbidden: forbidden.
        # - revoke: revoked.
        self.ca_status = ca_status
        # The type of the certificate. Valid values:
        # 
        # - root: rootCA.
        # - subRoot: subCA.
        # - externalCa: import.
        self.cert_type = cert_type
        # The page number. Default value: **1**.
        self.current_page = current_page
        # The unique identifier of the CA certificate.
        # 
        # >  You can call the [DescribeCACertificateList](https://help.aliyun.com/document_detail/328095.html) operation to query the unique identifiers of all CA certificates.
        self.identifier = identifier
        # The CA Issuer Type.
        # 
        # - local: Private certificate.
        # - iTrusChina: Compliance CA.
        # - external: External Import.
        self.issuer_type = issuer_type
        self.resource_group_id = resource_group_id
        # The number of CA certificates per page. Default value: **20**.
        self.show_size = show_size
        # valid time.
        # 
        # - valid: means in the valid period.
        # - notValid: means expired.
        self.valid_status = valid_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ca_status is not None:
            result['CaStatus'] = self.ca_status

        if self.cert_type is not None:
            result['CertType'] = self.cert_type

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.identifier is not None:
            result['Identifier'] = self.identifier

        if self.issuer_type is not None:
            result['IssuerType'] = self.issuer_type

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.show_size is not None:
            result['ShowSize'] = self.show_size

        if self.valid_status is not None:
            result['ValidStatus'] = self.valid_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaStatus') is not None:
            self.ca_status = m.get('CaStatus')

        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')

        if m.get('IssuerType') is not None:
            self.issuer_type = m.get('IssuerType')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')

        if m.get('ValidStatus') is not None:
            self.valid_status = m.get('ValidStatus')

        return self

