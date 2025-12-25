# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateHttpsBasicConfigurationRequest(DaraModel):
    def __init__(
        self,
        ciphersuite: str = None,
        ciphersuite_group: str = None,
        http_2: str = None,
        http_3: str = None,
        https: str = None,
        ocsp_stapling: str = None,
        rule: str = None,
        rule_enable: str = None,
        rule_name: str = None,
        sequence: int = None,
        site_id: int = None,
        tls_10: str = None,
        tls_11: str = None,
        tls_12: str = None,
        tls_13: str = None,
    ):
        # Custom cipher suite, indicating the specific encryption algorithm selected when CiphersuiteGroup is set to custom.
        self.ciphersuite = ciphersuite
        # Cipher suite group. Default uses all cipher suites. Value range:
        # - all: All cipher suites.
        # - strict: Strong cipher suites.
        # - custom: Custom cipher suites.
        self.ciphersuite_group = ciphersuite_group
        # Whether to enable HTTP2. Default is enabled. Value range:
        # - on: Enable.
        # - off: Disable.
        self.http_2 = http_2
        # Whether to enable HTTP3. Default is enabled. Value range:
        # - on: Enable.
        # - off: Disable.
        self.http_3 = http_3
        # Whether to enable HTTPS. Default is enabled. Value range:
        # - on: Enable.
        # - off: Disable.
        self.https = https
        # Whether to enable OCSP. Default is disabled. Value range:
        # - on: Enable.
        # - off: Disable.
        self.ocsp_stapling = ocsp_stapling
        # Rule content, using conditional expressions to match user requests. This parameter is not required when adding a global configuration. There are two usage scenarios:
        # - Match all incoming requests: Set the value to true
        # - Match specific requests: Set the value to a custom expression, for example: (http.host eq \\"video.example.com\\")
        self.rule = rule
        # Rule switch. This parameter is not required when adding a global configuration. Value range:
        # - on: Enable.
        # - off: Disable.
        self.rule_enable = rule_enable
        # Rule name. This parameter is not required when adding a global configuration.
        self.rule_name = rule_name
        self.sequence = sequence
        # Site ID, which can be obtained by calling the [ListSites](~~ListSites~~) API.
        # 
        # This parameter is required.
        self.site_id = site_id
        # Whether to enable TLS1.0. Default is disabled. Value range:
        # - on: Enable.
        # - off: Disable.
        self.tls_10 = tls_10
        # Whether to enable TLS1.1. Default is enabled. Value range:
        # - on: Enable.
        # - off: Disable.
        self.tls_11 = tls_11
        # Whether to enable TLS1.2. Default is enabled. Value range:
        # - on: Enable.
        # - off: Disable.
        self.tls_12 = tls_12
        # Whether to enable TLS1.3. Default is enabled. Value range:
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

        if self.http_2 is not None:
            result['Http2'] = self.http_2

        if self.http_3 is not None:
            result['Http3'] = self.http_3

        if self.https is not None:
            result['Https'] = self.https

        if self.ocsp_stapling is not None:
            result['OcspStapling'] = self.ocsp_stapling

        if self.rule is not None:
            result['Rule'] = self.rule

        if self.rule_enable is not None:
            result['RuleEnable'] = self.rule_enable

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.sequence is not None:
            result['Sequence'] = self.sequence

        if self.site_id is not None:
            result['SiteId'] = self.site_id

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

        if m.get('Http2') is not None:
            self.http_2 = m.get('Http2')

        if m.get('Http3') is not None:
            self.http_3 = m.get('Http3')

        if m.get('Https') is not None:
            self.https = m.get('Https')

        if m.get('OcspStapling') is not None:
            self.ocsp_stapling = m.get('OcspStapling')

        if m.get('Rule') is not None:
            self.rule = m.get('Rule')

        if m.get('RuleEnable') is not None:
            self.rule_enable = m.get('RuleEnable')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('Sequence') is not None:
            self.sequence = m.get('Sequence')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('Tls10') is not None:
            self.tls_10 = m.get('Tls10')

        if m.get('Tls11') is not None:
            self.tls_11 = m.get('Tls11')

        if m.get('Tls12') is not None:
            self.tls_12 = m.get('Tls12')

        if m.get('Tls13') is not None:
            self.tls_13 = m.get('Tls13')

        return self

