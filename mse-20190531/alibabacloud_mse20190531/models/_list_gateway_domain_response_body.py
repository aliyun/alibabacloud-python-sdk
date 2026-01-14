# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class ListGatewayDomainResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: List[main_models.ListGatewayDomainResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code returned.
        self.code = code
        # The details of the data.
        self.data = data
        # The HTTP status code returned.
        self.http_status_code = http_status_code
        # The error message returned if the request failed.
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
                temp_model = main_models.ListGatewayDomainResponseBodyData()
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

class ListGatewayDomainResponseBodyData(DaraModel):
    def __init__(
        self,
        cert_before_date: str = None,
        cert_identifier: str = None,
        comment: main_models.ListGatewayDomainResponseBodyDataComment = None,
        gateway_id: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        http_2: str = None,
        id: int = None,
        is_managed: bool = None,
        must_https: bool = None,
        name: str = None,
        protocol: str = None,
        status: int = None,
        tls_cipher_suites_config: main_models.ListGatewayDomainResponseBodyDataTlsCipherSuitesConfig = None,
        tls_max: str = None,
        tls_min: str = None,
        type: str = None,
    ):
        # The time when the certificate expires.
        self.cert_before_date = cert_before_date
        # The certificate ID.
        self.cert_identifier = cert_identifier
        # The route comment. This parameter is returned only in ingress scenarios.
        self.comment = comment
        # The gateway ID.
        self.gateway_id = gateway_id
        # The time when the domain name was created.
        self.gmt_create = gmt_create
        # The time when the domain name was updated.
        self.gmt_modified = gmt_modified
        # Indicates whether `HTTP/2` is enabled.
        # 
        # *   `open`: `HTTP/2` is enabled.
        # *   `close`: `HTTP/2` is disabled.
        # *   `globalConfig`: Global configurations are used.
        self.http_2 = http_2
        # The ID of the domain name.
        self.id = id
        self.is_managed = is_managed
        # Indicates whether HTTPS is forcefully used.
        self.must_https = must_https
        # The domain name.
        self.name = name
        # The protocol.
        self.protocol = protocol
        # The state of the domain name. Valid values:
        # 
        # *   0: unpublished
        # *   2: publishing
        # *   3: published
        # *   4: editing
        # *   5: unpublishing
        # *   6: unavailable
        self.status = status
        self.tls_cipher_suites_config = tls_cipher_suites_config
        # The maximum version of Transport Layer Security (TLS).
        self.tls_max = tls_max
        # The minimum version of TLS.
        self.tls_min = tls_min
        # The type of the domain name source. Valid values:
        # 
        # *   Op: console
        # *   Ingress: MSE Ingress
        self.type = type

    def validate(self):
        if self.comment:
            self.comment.validate()
        if self.tls_cipher_suites_config:
            self.tls_cipher_suites_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_before_date is not None:
            result['CertBeforeDate'] = self.cert_before_date

        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier

        if self.comment is not None:
            result['Comment'] = self.comment.to_map()

        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id

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

        if self.must_https is not None:
            result['MustHttps'] = self.must_https

        if self.name is not None:
            result['Name'] = self.name

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.status is not None:
            result['Status'] = self.status

        if self.tls_cipher_suites_config is not None:
            result['TlsCipherSuitesConfig'] = self.tls_cipher_suites_config.to_map()

        if self.tls_max is not None:
            result['TlsMax'] = self.tls_max

        if self.tls_min is not None:
            result['TlsMin'] = self.tls_min

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertBeforeDate') is not None:
            self.cert_before_date = m.get('CertBeforeDate')

        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')

        if m.get('Comment') is not None:
            temp_model = main_models.ListGatewayDomainResponseBodyDataComment()
            self.comment = temp_model.from_map(m.get('Comment'))

        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')

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

        if m.get('MustHttps') is not None:
            self.must_https = m.get('MustHttps')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TlsCipherSuitesConfig') is not None:
            temp_model = main_models.ListGatewayDomainResponseBodyDataTlsCipherSuitesConfig()
            self.tls_cipher_suites_config = temp_model.from_map(m.get('TlsCipherSuitesConfig'))

        if m.get('TlsMax') is not None:
            self.tls_max = m.get('TlsMax')

        if m.get('TlsMin') is not None:
            self.tls_min = m.get('TlsMin')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListGatewayDomainResponseBodyDataTlsCipherSuitesConfig(DaraModel):
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

class ListGatewayDomainResponseBodyDataComment(DaraModel):
    def __init__(
        self,
        status: str = None,
    ):
        # The route status.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

