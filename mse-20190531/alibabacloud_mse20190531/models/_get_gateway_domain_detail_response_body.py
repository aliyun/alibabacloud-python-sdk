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
        # The status code.
        self.code = code
        # The data.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # - `true`: The request is successful.
        # - `false`: The request fails.
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
        ca_cert_identifier: str = None,
        cert_identifier: str = None,
        cert_name: str = None,
        common_name: str = None,
        enable_waf: bool = None,
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
        mtls_enabled: bool = None,
        must_https: bool = None,
        name: str = None,
        protocol: str = None,
        sans: str = None,
        support_waf: bool = None,
        tls_cipher_suites_config: main_models.GetGatewayDomainDetailResponseBodyDataTlsCipherSuitesConfig = None,
        tls_max: str = None,
        tls_min: str = None,
    ):
        # The certificate expiration time.
        self.after_date = after_date
        # The algorithm.
        self.algorithm = algorithm
        # The certificate issuance time.
        self.before_date = before_date
        # The CA certificate content.
        self.ca_cert_identifier = ca_cert_identifier
        # The certificate identifier.
        self.cert_identifier = cert_identifier
        # The certificate name.
        self.cert_name = cert_name
        # The public domain name.
        self.common_name = common_name
        # Indicates whether WAF protection is enabled for the domain name.
        self.enable_waf = enable_waf
        # The gateway ID.
        self.gateway_id = gateway_id
        # The unique ID of the gateway.
        self.gateway_unique_id = gateway_unique_id
        # The certificate expiration time in GMT.
        self.gmt_after = gmt_after
        # The certificate issuance time in GMT.
        self.gmt_before = gmt_before
        # The creation time.
        self.gmt_create = gmt_create
        # The update time.
        self.gmt_modified = gmt_modified
        # Indicates whether HTTP/2 is enabled. Valid values:
        # - `open`: HTTP/2 is enabled.
        # - `close`: HTTP/2 is disabled.
        # - `globalConfig`: The global configuration is used.
        self.http_2 = http_2
        # The ID.
        self.id = id
        # Indicates whether the domain name is managed.
        self.is_managed = is_managed
        # The issuer.
        self.issuer = issuer
        # Indicates whether mTLS is enabled.
        self.mtls_enabled = mtls_enabled
        # Indicates whether HTTPS is forced.
        self.must_https = must_https
        # The name.
        self.name = name
        # The gateway protocol.
        self.protocol = protocol
        # The subject alternative names.
        self.sans = sans
        # Indicates whether the gateway supports WAF protection.
        self.support_waf = support_waf
        # The TLS cipher suite configuration, including the configuration type and the list of cipher suite names.
        self.tls_cipher_suites_config = tls_cipher_suites_config
        # The maximum TLS version.
        self.tls_max = tls_max
        # The minimum TLS version.
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

        if self.ca_cert_identifier is not None:
            result['CaCertIdentifier'] = self.ca_cert_identifier

        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier

        if self.cert_name is not None:
            result['CertName'] = self.cert_name

        if self.common_name is not None:
            result['CommonName'] = self.common_name

        if self.enable_waf is not None:
            result['EnableWaf'] = self.enable_waf

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

        if self.mtls_enabled is not None:
            result['MtlsEnabled'] = self.mtls_enabled

        if self.must_https is not None:
            result['MustHttps'] = self.must_https

        if self.name is not None:
            result['Name'] = self.name

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.sans is not None:
            result['Sans'] = self.sans

        if self.support_waf is not None:
            result['SupportWaf'] = self.support_waf

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

        if m.get('CaCertIdentifier') is not None:
            self.ca_cert_identifier = m.get('CaCertIdentifier')

        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')

        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')

        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')

        if m.get('EnableWaf') is not None:
            self.enable_waf = m.get('EnableWaf')

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

        if m.get('MtlsEnabled') is not None:
            self.mtls_enabled = m.get('MtlsEnabled')

        if m.get('MustHttps') is not None:
            self.must_https = m.get('MustHttps')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('Sans') is not None:
            self.sans = m.get('Sans')

        if m.get('SupportWaf') is not None:
            self.support_waf = m.get('SupportWaf')

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
        # The TLS cipher suite configuration type. DEFAULT indicates the default configuration, and CUSTOM indicates the custom configuration.
        self.config_type = config_type
        # The list of TLS cipher suite names.
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

