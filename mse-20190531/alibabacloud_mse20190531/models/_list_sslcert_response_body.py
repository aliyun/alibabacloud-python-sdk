# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class ListSSLCertResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: List[main_models.ListSSLCertResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code returned. A value of 200 indicates that the request is successful.
        self.code = code
        # The returned data.
        self.data = data
        # The HTTP status code returned.
        self.http_status_code = http_status_code
        # The error message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   `true`: The request was successful.
        # *   `false`: The request failed.
        self.success = success

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
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListSSLCertResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListSSLCertResponseBodyData(DaraModel):
    def __init__(
        self,
        after_date: str = None,
        algorithm: str = None,
        before_date: str = None,
        cert_identifier: str = None,
        cert_name: str = None,
        common_name: str = None,
        gmt_after: str = None,
        gmt_before: str = None,
        issuer: str = None,
        sans: str = None,
    ):
        # The time when the certificate expires. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.after_date = after_date
        # The algorithm.
        self.algorithm = algorithm
        # The time when the certificate took effect. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.before_date = before_date
        # The ID of the certificate.
        self.cert_identifier = cert_identifier
        # The name of the certificate.
        self.cert_name = cert_name
        # The domain name with which the certificate is associated.
        self.common_name = common_name
        # The time when the certificate expires. This value is a GMT timestamp.
        self.gmt_after = gmt_after
        # The time when the certificate took effect. This value is a GMT timestamp.
        self.gmt_before = gmt_before
        # The issuer of the certificate.
        self.issuer = issuer
        # The SSL certificate.
        self.sans = sans

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.after_date is not None:
            result['AfterDate'] = self.after_date

        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm

        if self.before_date is not None:
            result['BeforeDate'] = self.before_date

        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier

        if self.cert_name is not None:
            result['CertName'] = self.cert_name

        if self.common_name is not None:
            result['CommonName'] = self.common_name

        if self.gmt_after is not None:
            result['GmtAfter'] = self.gmt_after

        if self.gmt_before is not None:
            result['GmtBefore'] = self.gmt_before

        if self.issuer is not None:
            result['Issuer'] = self.issuer

        if self.sans is not None:
            result['Sans'] = self.sans

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AfterDate') is not None:
            self.after_date = m.get('AfterDate')

        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')

        if m.get('BeforeDate') is not None:
            self.before_date = m.get('BeforeDate')

        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')

        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')

        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')

        if m.get('GmtAfter') is not None:
            self.gmt_after = m.get('GmtAfter')

        if m.get('GmtBefore') is not None:
            self.gmt_before = m.get('GmtBefore')

        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')

        if m.get('Sans') is not None:
            self.sans = m.get('Sans')

        return self

