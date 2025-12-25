# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetHttpsBasicConfigurationResponseBody(DaraModel):
    def __init__(
        self,
        ciphersuite: str = None,
        ciphersuite_group: str = None,
        config_id: int = None,
        config_type: str = None,
        http_2: str = None,
        http_3: str = None,
        https: str = None,
        ocsp_stapling: str = None,
        request_id: str = None,
        rule: str = None,
        rule_enable: str = None,
        rule_name: str = None,
        sequence: int = None,
        tls_10: str = None,
        tls_11: str = None,
        tls_12: str = None,
        tls_13: str = None,
    ):
        # Custom cipher suite, indicating the specific encryption algorithm selected when CiphersuiteGroup is set to custom.
        self.ciphersuite = ciphersuite
        # Cipher suite group, default is all cipher suites. Value range:
        # 
        # - all: All cipher suites.
        # - strict: Strong cipher suites.
        # - custom: Custom cipher suites.
        self.ciphersuite_group = ciphersuite_group
        # Configuration ID.
        self.config_id = config_id
        # Configuration type, which can be used to query global or rule configurations. Value range:
        # - global: Query global configuration;
        # - rule: Query rule configuration;
        self.config_type = config_type
        # Whether to enable HTTP2, default is enabled. Value range:
        # 
        # - on: Enable.
        # - off: Disable.
        self.http_2 = http_2
        # Whether to enable HTTP3, which is enabled by default. The value can be:
        # - on: Enabled. 
        # - off: Disabled.
        self.http_3 = http_3
        # Whether to enable HTTPS, default is enabled. Value range:
        # 
        # - on: Enable.
        # - off: Disable.
        self.https = https
        # Whether to enable OCSP, default is disabled. Value range:
        # 
        # - on: Enable.
        # - off: Disable.
        self.ocsp_stapling = ocsp_stapling
        # Request ID.
        self.request_id = request_id
        # Matching rule content.
        self.rule = rule
        # Rule switch. Value range:
        # 
        # - on: Enable.
        # - off: Disable.
        self.rule_enable = rule_enable
        # Rule name.
        self.rule_name = rule_name
        # Rule execution sequence.
        self.sequence = sequence
        # Whether to enable TLS1.0, default is disabled. Value range:
        # - on: Enable.
        # - off: Disable.
        self.tls_10 = tls_10
        # Whether to enable TLS1.1, default is disabled. Value range:
        # - on: Enable.
        # - off: Disable.
        self.tls_11 = tls_11
        # Whether to enable TLS1.2, default is disabled. Value range:
        # - on: Enable.
        # - off: Disable.
        self.tls_12 = tls_12
        # Whether to enable TLS1.3, default is disabled. Value range:
        # - on: Enable.
        # - off: Disable.
        self.tls_13 = tls_13

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ciphersuite is not None:
            result['Ciphersuite'] = self.ciphersuite

        if self.ciphersuite_group is not None:
            result['CiphersuiteGroup'] = self.ciphersuite_group

        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.config_type is not None:
            result['ConfigType'] = self.config_type

        if self.http_2 is not None:
            result['Http2'] = self.http_2

        if self.http_3 is not None:
            result['Http3'] = self.http_3

        if self.https is not None:
            result['Https'] = self.https

        if self.ocsp_stapling is not None:
            result['OcspStapling'] = self.ocsp_stapling

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.rule is not None:
            result['Rule'] = self.rule

        if self.rule_enable is not None:
            result['RuleEnable'] = self.rule_enable

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.sequence is not None:
            result['Sequence'] = self.sequence

        if self.tls_10 is not None:
            result['Tls10'] = self.tls_10

        if self.tls_11 is not None:
            result['Tls11'] = self.tls_11

        if self.tls_12 is not None:
            result['Tls12'] = self.tls_12

        if self.tls_13 is not None:
            result['Tls13'] = self.tls_13

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ciphersuite') is not None:
            self.ciphersuite = m.get('Ciphersuite')

        if m.get('CiphersuiteGroup') is not None:
            self.ciphersuite_group = m.get('CiphersuiteGroup')

        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('ConfigType') is not None:
            self.config_type = m.get('ConfigType')

        if m.get('Http2') is not None:
            self.http_2 = m.get('Http2')

        if m.get('Http3') is not None:
            self.http_3 = m.get('Http3')

        if m.get('Https') is not None:
            self.https = m.get('Https')

        if m.get('OcspStapling') is not None:
            self.ocsp_stapling = m.get('OcspStapling')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Rule') is not None:
            self.rule = m.get('Rule')

        if m.get('RuleEnable') is not None:
            self.rule_enable = m.get('RuleEnable')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('Sequence') is not None:
            self.sequence = m.get('Sequence')

        if m.get('Tls10') is not None:
            self.tls_10 = m.get('Tls10')

        if m.get('Tls11') is not None:
            self.tls_11 = m.get('Tls11')

        if m.get('Tls12') is not None:
            self.tls_12 = m.get('Tls12')

        if m.get('Tls13') is not None:
            self.tls_13 = m.get('Tls13')

        return self

