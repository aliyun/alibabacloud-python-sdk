# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cas20200407 import models as main_models
from darabonba.model import DaraModel

class ListDeploymentJobCertResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListDeploymentJobCertResponseBodyData] = None,
        request_id: str = None,
    ):
        # The response parameters.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListDeploymentJobCertResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListDeploymentJobCertResponseBodyData(DaraModel):
    def __init__(
        self,
        algorithm: str = None,
        cert_id: int = None,
        cert_instance_id: str = None,
        cert_name: str = None,
        cert_order_type: str = None,
        cert_type: str = None,
        common_name: str = None,
        is_trustee: bool = None,
        month: int = None,
        not_after_time: int = None,
        not_before_time: int = None,
        order_id: int = None,
        sans: List[str] = None,
        status_code: str = None,
    ):
        # The algorithm of the certificate public key.
        self.algorithm = algorithm
        # The ID of the certificate.
        self.cert_id = cert_id
        # The instance ID of the certificate.
        self.cert_instance_id = cert_instance_id
        # The name of the certificate.
        self.cert_name = cert_name
        # The type of the certificate order. Valid values:
        # 
        # *   **upload**: uploaded certificate.
        # *   **buy**: purchased certificate.
        # *   **free**: free certificate. This value is available only on the China site (aliyun.com).
        self.cert_order_type = cert_order_type
        # The type of the certificate.
        self.cert_type = cert_type
        # The common name of the certificate.
        self.common_name = common_name
        # Indicates whether the certificate is hosted. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.is_trustee = is_trustee
        # The month in which the certificate is applied for.
        self.month = month
        # The end time of the validity period of the certificate. The value is a timestamp in seconds.
        self.not_after_time = not_after_time
        # The start time of the validity period of the certificate. The value is a timestamp in seconds.
        self.not_before_time = not_before_time
        # The ID of the certificate order.
        # 
        # >  If CertId is returned, this parameter is not returned.
        self.order_id = order_id
        # The subject alternative name (SAN) extensions of the certificate.
        self.sans = sans
        # The status code of the certificate. Valid values:
        # 
        # *   **payed**: paid and pending application
        # *   **checking**: being validated
        # *   **checkedFail**: validation failed
        # *   **revoked**: revoked
        # *   **revokeChecking**: revocation request being validated
        # *   **issued**: issued (excluding hosted certificates that are issued, certificates that are about to expire, expired certificates, and uploaded certificates)
        # *   **trustee**: hosted and issued
        # *   **upload**: uploaded (excluding certificates that are about to expire and expired certificates)
        # *   **willExpired**: about to expire (including certificates issued by using the Certificate Management Service console and uploaded certificates)
        # *   **expired**: expired (including certificates issued by using the Certificate Management Service console and uploaded certificates)
        # *   **validity**: valid (including certificates that are not expired or revoked)
        # *   **refund**: refunded
        # *   **closed**: closed
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm

        if self.cert_id is not None:
            result['CertId'] = self.cert_id

        if self.cert_instance_id is not None:
            result['CertInstanceId'] = self.cert_instance_id

        if self.cert_name is not None:
            result['CertName'] = self.cert_name

        if self.cert_order_type is not None:
            result['CertOrderType'] = self.cert_order_type

        if self.cert_type is not None:
            result['CertType'] = self.cert_type

        if self.common_name is not None:
            result['CommonName'] = self.common_name

        if self.is_trustee is not None:
            result['IsTrustee'] = self.is_trustee

        if self.month is not None:
            result['Month'] = self.month

        if self.not_after_time is not None:
            result['NotAfterTime'] = self.not_after_time

        if self.not_before_time is not None:
            result['NotBeforeTime'] = self.not_before_time

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.sans is not None:
            result['Sans'] = self.sans

        if self.status_code is not None:
            result['StatusCode'] = self.status_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')

        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')

        if m.get('CertInstanceId') is not None:
            self.cert_instance_id = m.get('CertInstanceId')

        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')

        if m.get('CertOrderType') is not None:
            self.cert_order_type = m.get('CertOrderType')

        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')

        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')

        if m.get('IsTrustee') is not None:
            self.is_trustee = m.get('IsTrustee')

        if m.get('Month') is not None:
            self.month = m.get('Month')

        if m.get('NotAfterTime') is not None:
            self.not_after_time = m.get('NotAfterTime')

        if m.get('NotBeforeTime') is not None:
            self.not_before_time = m.get('NotBeforeTime')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('Sans') is not None:
            self.sans = m.get('Sans')

        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')

        return self

