# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class GetGatewayDomainDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetGatewayDomainDetailResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code returned.
        self.code = code
        # The returned data.
        self.data = data
        # The HTTP status code returned.
        self.http_status_code = http_status_code
        # The message returned.
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
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

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

        if m.get('Data') is not None:
            temp_model = main_models.GetGatewayDomainDetailResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetGatewayDomainDetailResponseBodyData(DaraModel):
    def __init__(
        self,
        after_date: int = None,
        algorithm: str = None,
        before_date: int = None,
        cert_identifier: str = None,
        cert_name: str = None,
        common_name: str = None,
        gateway_id: int = None,
        gateway_unique_id: str = None,
        gmt_after: str = None,
        gmt_before: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        http_2: str = None,
        id: int = None,
        is_managed: bool = None,
        issuer: str = None,
        must_https: bool = None,
        name: str = None,
        protocol: str = None,
        sans: str = None,
        tls_cipher_suites_config: main_models.GetGatewayDomainDetailResponseBodyDataTlsCipherSuitesConfig = None,
        tls_max: str = None,
        tls_min: str = None,
    ):
        # The start time.
        self.after_date = after_date
        # The algorithm.
        self.algorithm = algorithm
        # The expiration time.
        self.before_date = before_date
        # The ID of the certificate.
        self.cert_identifier = cert_identifier
        # The name of the certificate.
        self.cert_name = cert_name
        # The public domain name.
        self.common_name = common_name
        # The ID of the gateway.
        self.gateway_id = gateway_id
        # The unique ID of the gateway.
        self.gateway_unique_id = gateway_unique_id
        # The start time.
        self.gmt_after = gmt_after
        # The expiration time.
        self.gmt_before = gmt_before
        # The creation time.
        self.gmt_create = gmt_create
        # The update time.
        self.gmt_modified = gmt_modified
        # Indicates whether `HTTP/2` is enabled.
        # 
        # *   `open`: `HTTP/2` is enabled.
        # *   `close`: `HTTP/2` is disabled.
        # *   `globalConfig`: Global configurations are used.
        self.http_2 = http_2
        # The ID.
        self.id = id
        self.is_managed = is_managed
        # The issuer.
        self.issuer = issuer
        # Indicates whether HTTPS is forcibly used.
        self.must_https = must_https
        # The domain name.
        self.name = name
        # The protocol of the gateway.
        self.protocol = protocol
        # The name of the extended field.
        self.sans = sans
        self.tls_cipher_suites_config = tls_cipher_suites_config
        # The maximum version of Transport Layer Security (TLS).
        self.tls_max = tls_max
        # The minimum version of TLS.
        self.tls_min = tls_min

    def validate(self):
        if self.tls_cipher_suites_config:
            self.tls_cipher_suites_config.validate()

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

        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id

        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id

        if self.gmt_after is not None:
            result['GmtAfter'] = self.gmt_after

        if self.gmt_before is not None:
            result['GmtBefore'] = self.gmt_before

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.http_2 is not None:
            result['Http2'] = self.http_2

        if self.id is not None:
            result['Id'] = self.id

        if self.is_managed is not None:
            result['IsManaged'] = self.is_managed

        if self.issuer is not None:
            result['Issuer'] = self.issuer

        if self.must_https is not None:
            result['MustHttps'] = self.must_https

        if self.name is not None:
            result['Name'] = self.name

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.sans is not None:
            result['Sans'] = self.sans

        if self.tls_cipher_suites_config is not None:
            result['TlsCipherSuitesConfig'] = self.tls_cipher_suites_config.to_map()

        if self.tls_max is not None:
            result['TlsMax'] = self.tls_max

        if self.tls_min is not None:
            result['TlsMin'] = self.tls_min

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

        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')

        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')

        if m.get('GmtAfter') is not None:
            self.gmt_after = m.get('GmtAfter')

        if m.get('GmtBefore') is not None:
            self.gmt_before = m.get('GmtBefore')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Http2') is not None:
            self.http_2 = m.get('Http2')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IsManaged') is not None:
            self.is_managed = m.get('IsManaged')

        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')

        if m.get('MustHttps') is not None:
            self.must_https = m.get('MustHttps')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('Sans') is not None:
            self.sans = m.get('Sans')

        if m.get('TlsCipherSuitesConfig') is not None:
            temp_model = main_models.GetGatewayDomainDetailResponseBodyDataTlsCipherSuitesConfig()
            self.tls_cipher_suites_config = temp_model.from_map(m.get('TlsCipherSuitesConfig'))

        if m.get('TlsMax') is not None:
            self.tls_max = m.get('TlsMax')

        if m.get('TlsMin') is not None:
            self.tls_min = m.get('TlsMin')

        return self

class GetGatewayDomainDetailResponseBodyDataTlsCipherSuitesConfig(DaraModel):
    def __init__(
        self,
        config_type: str = None,
        tls_cipher_suites: List[str] = None,
    ):
        self.config_type = config_type
        self.tls_cipher_suites = tls_cipher_suites

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_type is not None:
            result['ConfigType'] = self.config_type

        if self.tls_cipher_suites is not None:
            result['TlsCipherSuites'] = self.tls_cipher_suites

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigType') is not None:
            self.config_type = m.get('ConfigType')

        if m.get('TlsCipherSuites') is not None:
            self.tls_cipher_suites = m.get('TlsCipherSuites')

        return self

