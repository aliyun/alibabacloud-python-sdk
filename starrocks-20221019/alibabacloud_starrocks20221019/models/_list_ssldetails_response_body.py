# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_starrocks20221019 import models as main_models
from darabonba.model import DaraModel

class ListSSLDetailsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListSSLDetailsResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ListSSLDetailsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListSSLDetailsResponseBodyData(DaraModel):
    def __init__(
        self,
        aliases: str = None,
        custom_cert: bool = None,
        enable_ssl: bool = None,
        is_valid: bool = None,
        issuer_dn: str = None,
        not_after: int = None,
        not_before: int = None,
        ssl_certificate_text: str = None,
        status: str = None,
        subject_dn: str = None,
    ):
        self.aliases = aliases
        self.custom_cert = custom_cert
        self.enable_ssl = enable_ssl
        self.is_valid = is_valid
        self.issuer_dn = issuer_dn
        self.not_after = not_after
        self.not_before = not_before
        self.ssl_certificate_text = ssl_certificate_text
        self.status = status
        self.subject_dn = subject_dn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliases is not None:
            result['Aliases'] = self.aliases

        if self.custom_cert is not None:
            result['CustomCert'] = self.custom_cert

        if self.enable_ssl is not None:
            result['EnableSSL'] = self.enable_ssl

        if self.is_valid is not None:
            result['IsValid'] = self.is_valid

        if self.issuer_dn is not None:
            result['IssuerDN'] = self.issuer_dn

        if self.not_after is not None:
            result['NotAfter'] = self.not_after

        if self.not_before is not None:
            result['NotBefore'] = self.not_before

        if self.ssl_certificate_text is not None:
            result['SslCertificateText'] = self.ssl_certificate_text

        if self.status is not None:
            result['Status'] = self.status

        if self.subject_dn is not None:
            result['SubjectDN'] = self.subject_dn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Aliases') is not None:
            self.aliases = m.get('Aliases')

        if m.get('CustomCert') is not None:
            self.custom_cert = m.get('CustomCert')

        if m.get('EnableSSL') is not None:
            self.enable_ssl = m.get('EnableSSL')

        if m.get('IsValid') is not None:
            self.is_valid = m.get('IsValid')

        if m.get('IssuerDN') is not None:
            self.issuer_dn = m.get('IssuerDN')

        if m.get('NotAfter') is not None:
            self.not_after = m.get('NotAfter')

        if m.get('NotBefore') is not None:
            self.not_before = m.get('NotBefore')

        if m.get('SslCertificateText') is not None:
            self.ssl_certificate_text = m.get('SslCertificateText')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubjectDN') is not None:
            self.subject_dn = m.get('SubjectDN')

        return self

