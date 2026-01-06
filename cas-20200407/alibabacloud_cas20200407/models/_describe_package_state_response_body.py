# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePackageStateResponseBody(DaraModel):
    def __init__(
        self,
        issued_count: int = None,
        product_code: str = None,
        request_id: str = None,
        total_count: int = None,
        used_count: int = None,
    ):
        # The number of issued certificates of the specified specifications.
        self.issued_count = issued_count
        # The specifications of the certificate resource plan. Valid values:
        # 
        # *   **digicert-free-1-free**: DigiCert single-domain DV certificate in a three-month free trial, available only on the China site (aliyun.com).
        # *   **symantec-free-1-free**: DigiCert single-domain DV certificate in a one-year free trial, available only on the China site (aliyun.com).
        # *   **symantec-dv-1-starter**: DigiCert wildcard DV certificate.
        # *   **symantec-ov-1-personal**: DigiCert single-domain OV certificate.
        # *   **symantec-ov-w-personal**: DigiCert wildcard OV certificate.
        # *   **geotrust-dv-1-starter**: GeoTrust single-domain DV certificate.
        # *   **geotrust-dv-w-starter**: GeoTrust wildcard DV certificate.
        # *   **geotrust-ov-1-personal**: GeoTrust single-domain OV certificate.
        # *   **geotrust-ov-w-personal**: GeoTrust wildcard OV certificate.
        # *   **globalsign-dv-1-personal**: GlobalSign single-domain DV certificate.
        # *   **globalsign-dv-w-advanced**: GlobalSign wildcard DV certificate.
        # *   **globalsign-ov-1-personal**: GlobalSign single-domain OV certificate.
        # *   **globalsign-ov-w-advanced**: GlobalSign wildcard OV certificate.
        # *   **cfca-ov-1-personal**: CFCA single-domain OV certificate, available only on the China site (aliyun.com).
        # *   **cfca-ev-w-advanced**: CFCA wildcard OV certificate, available only on the China site (aliyun.com).
        self.product_code = product_code
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The total number of purchased certificate resource plans of the specified specifications.
        self.total_count = total_count
        # The number of certificate applications that you submitted for certificates of the specified specifications.
        # 
        # > : A successful call of the [CreateCertificateForPackageRequest](https://help.aliyun.com/document_detail/204087.html), [CreateCertificateRequest](https://help.aliyun.com/document_detail/164105.html), or [CreateCertificateWithCsrRequest](https://help.aliyun.com/document_detail/178732.html) operation is counted as one a certificate application, regardless of whether the certificate is issued.
        self.used_count = used_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.issued_count is not None:
            result['IssuedCount'] = self.issued_count

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.used_count is not None:
            result['UsedCount'] = self.used_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IssuedCount') is not None:
            self.issued_count = m.get('IssuedCount')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('UsedCount') is not None:
            self.used_count = m.get('UsedCount')

        return self

