# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePackageStateRequest(DaraModel):
    def __init__(
        self,
        product_code: str = None,
    ):
        # The specifications of the certificate resource plan. Valid values:
        # 
        # *   **digicert-free-1-free** (default): DigiCert single-domain domain validated (DV) certificate in a three-month free trial, available only on the China site (aliyun.com).
        # *   **symantec-free-1-free**: DigiCert single-domain DV certificate in a one-year free trial, available only on the China site (aliyun.com).
        # *   **symantec-dv-1-starter**: DigiCert wildcard DV certificate.
        # *   **symantec-ov-1-personal**: DigiCert single-domain organization validated (OV) certificate.
        # *   **symantec-ov-w-personal**: DigiCert wildcard OV certificate.
        # *   **geotrust-dv-1-starter**: GeoTrust single-domain DV certificate.
        # *   **geotrust-dv-w-starter**: GeoTrust wildcard DV certificate.
        # *   **geotrust-ov-1-personal**: GeoTrust single-domain OV certificate.
        # *   **geotrust-ov-w-personal**: GeoTrust wildcard OV certificate.
        # *   **globalsign-dv-1-personal**: GlobalSign single-domain DV certificate.
        # *   **globalsign-dv-w-advanced**: GlobalSign wildcard DV certificate.
        # *   **globalsign-ov-1-personal**: GlobalSign single-domain OV certificate.
        # *   **globalsign-ov-w-advanced**: GlobalSign wildcard OV certificate.
        # *   **cfca-ov-1-personal**: China Financial Certification Authority (CFCA) single-domain OV certificate, available only on the China site (aliyun.com).
        # *   **cfca-ev-w-advanced**: CFCA wildcard OV certificate, available only on the China site (aliyun.com).
        self.product_code = product_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        return self

