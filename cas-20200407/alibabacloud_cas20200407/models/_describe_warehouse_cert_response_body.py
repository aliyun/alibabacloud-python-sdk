# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeWarehouseCertResponseBody(DaraModel):
    def __init__(
        self,
        cert_identifier: str = None,
        cert_status: str = None,
        cert_type: str = None,
        common_name: str = None,
        content: str = None,
        fingerprint: str = None,
        issuer: str = None,
        issuer_identifier: str = None,
        private_ca_instance_id: str = None,
        private_ca_region_id: str = None,
        request_id: str = None,
        warehouse_instance_id: str = None,
    ):
        # The unique identifier of the certificate.
        self.cert_identifier = cert_identifier
        # The status of the certificate.
        self.cert_status = cert_status
        # The type of the certificate.
        self.cert_type = cert_type
        # The common name of the certificate subject. This field is empty if the certificate subject does not include a common name (CN).
        self.common_name = common_name
        # The content of the certificate, including the certificate chain.
        self.content = content
        # The fingerprint of the certificate content.
        self.fingerprint = fingerprint
        # The common name (or organization name) of the issuer.
        self.issuer = issuer
        # The unique identifier of the issuer certificate.
        self.issuer_identifier = issuer_identifier
        # The instance ID of the private CA instance associated with the certificate.
        self.private_ca_instance_id = private_ca_instance_id
        # The region ID of the private CA instance associated with the certificate.
        self.private_ca_region_id = private_ca_region_id
        # The ID of the request.
        self.request_id = request_id
        # The instance ID of the certificate warehouse.
        self.warehouse_instance_id = warehouse_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier

        if self.cert_status is not None:
            result['CertStatus'] = self.cert_status

        if self.cert_type is not None:
            result['CertType'] = self.cert_type

        if self.common_name is not None:
            result['CommonName'] = self.common_name

        if self.content is not None:
            result['Content'] = self.content

        if self.fingerprint is not None:
            result['Fingerprint'] = self.fingerprint

        if self.issuer is not None:
            result['Issuer'] = self.issuer

        if self.issuer_identifier is not None:
            result['IssuerIdentifier'] = self.issuer_identifier

        if self.private_ca_instance_id is not None:
            result['PrivateCaInstanceId'] = self.private_ca_instance_id

        if self.private_ca_region_id is not None:
            result['PrivateCaRegionId'] = self.private_ca_region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.warehouse_instance_id is not None:
            result['WarehouseInstanceId'] = self.warehouse_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')

        if m.get('CertStatus') is not None:
            self.cert_status = m.get('CertStatus')

        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')

        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Fingerprint') is not None:
            self.fingerprint = m.get('Fingerprint')

        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')

        if m.get('IssuerIdentifier') is not None:
            self.issuer_identifier = m.get('IssuerIdentifier')

        if m.get('PrivateCaInstanceId') is not None:
            self.private_ca_instance_id = m.get('PrivateCaInstanceId')

        if m.get('PrivateCaRegionId') is not None:
            self.private_ca_region_id = m.get('PrivateCaRegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('WarehouseInstanceId') is not None:
            self.warehouse_instance_id = m.get('WarehouseInstanceId')

        return self

