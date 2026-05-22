# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateOriginRuleRequest(DaraModel):
    def __init__(
        self,
        config_id: int = None,
        dns_record: str = None,
        follow_302enable: str = None,
        follow_302max_tries: str = None,
        follow_302retain_args: str = None,
        follow_302retain_header: str = None,
        follow_302target_host: str = None,
        origin_host: str = None,
        origin_http_port: str = None,
        origin_https_port: str = None,
        origin_mtls: str = None,
        origin_read_timeout: str = None,
        origin_scheme: str = None,
        origin_sni: str = None,
        origin_verify: str = None,
        range: str = None,
        range_chunk_size: str = None,
        rule: str = None,
        rule_enable: str = None,
        rule_name: str = None,
        sequence: int = None,
        site_id: int = None,
    ):
        # Configuration ID.
        # 
        # This parameter is required.
        self.config_id = config_id
        # Rewrite the DNS resolution record of the origin request.
        self.dns_record = dns_record
        self.follow_302enable = follow_302enable
        self.follow_302max_tries = follow_302max_tries
        self.follow_302retain_args = follow_302retain_args
        self.follow_302retain_header = follow_302retain_header
        self.follow_302target_host = follow_302target_host
        # The HOST carried in the origin request.
        self.origin_host = origin_host
        # Port of the origin server when using HTTP protocol for origin pull.
        self.origin_http_port = origin_http_port
        # Port of the origin server when using HTTPS protocol for origin pull.
        self.origin_https_port = origin_https_port
        # mTLS switch. Valid values:
        # - on: Enable.
        # - off: Disable.
        self.origin_mtls = origin_mtls
        self.origin_read_timeout = origin_read_timeout
        # Protocol used for the origin request. Valid values:
        # - http: Use HTTP protocol for origin pull.
        # - https: Use HTTPS protocol for origin pull.
        # - follow: Follow the client\\"s protocol for origin pull.
        self.origin_scheme = origin_scheme
        # SNI carried in the origin request.
        self.origin_sni = origin_sni
        # Origin certificate verification switch. Valid values:
        # - on: Enable.
        # - off: Disable.
        self.origin_verify = origin_verify
        # Use range chunking for origin pull file download. Valid values:
        # - on: Enable.
        # - off: Disable.
        # - force: Force.
        self.range = range
        self.range_chunk_size = range_chunk_size
        # Rule content, used to match user requests with conditional expressions. This parameter is not required when adding a global configuration. There are two usage scenarios:
        # - Match all incoming requests: Set the value to true
        # - Match specific requests: Set the value to a custom expression, for example: (http.host eq \\"video.example.com\\")
        self.rule = rule
        # Rule switch. This parameter is not required when adding a global configuration. Valid values:
        # - on: Enable.
        # - off: Disable.
        self.rule_enable = rule_enable
        # Rule name. This parameter is not required when adding a global configuration.
        self.rule_name = rule_name
        self.sequence = sequence
        # Site ID, which can be obtained by calling the [ListSites](~~ListSites~~) interface.
        # 
        # This parameter is required.
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.dns_record is not None:
            result['DnsRecord'] = self.dns_record

        if self.follow_302enable is not None:
            result['Follow302Enable'] = self.follow_302enable

        if self.follow_302max_tries is not None:
            result['Follow302MaxTries'] = self.follow_302max_tries

        if self.follow_302retain_args is not None:
            result['Follow302RetainArgs'] = self.follow_302retain_args

        if self.follow_302retain_header is not None:
            result['Follow302RetainHeader'] = self.follow_302retain_header

        if self.follow_302target_host is not None:
            result['Follow302TargetHost'] = self.follow_302target_host

        if self.origin_host is not None:
            result['OriginHost'] = self.origin_host

        if self.origin_http_port is not None:
            result['OriginHttpPort'] = self.origin_http_port

        if self.origin_https_port is not None:
            result['OriginHttpsPort'] = self.origin_https_port

        if self.origin_mtls is not None:
            result['OriginMtls'] = self.origin_mtls

        if self.origin_read_timeout is not None:
            result['OriginReadTimeout'] = self.origin_read_timeout

        if self.origin_scheme is not None:
            result['OriginScheme'] = self.origin_scheme

        if self.origin_sni is not None:
            result['OriginSni'] = self.origin_sni

        if self.origin_verify is not None:
            result['OriginVerify'] = self.origin_verify

        if self.range is not None:
            result['Range'] = self.range

        if self.range_chunk_size is not None:
            result['RangeChunkSize'] = self.range_chunk_size

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('DnsRecord') is not None:
            self.dns_record = m.get('DnsRecord')

        if m.get('Follow302Enable') is not None:
            self.follow_302enable = m.get('Follow302Enable')

        if m.get('Follow302MaxTries') is not None:
            self.follow_302max_tries = m.get('Follow302MaxTries')

        if m.get('Follow302RetainArgs') is not None:
            self.follow_302retain_args = m.get('Follow302RetainArgs')

        if m.get('Follow302RetainHeader') is not None:
            self.follow_302retain_header = m.get('Follow302RetainHeader')

        if m.get('Follow302TargetHost') is not None:
            self.follow_302target_host = m.get('Follow302TargetHost')

        if m.get('OriginHost') is not None:
            self.origin_host = m.get('OriginHost')

        if m.get('OriginHttpPort') is not None:
            self.origin_http_port = m.get('OriginHttpPort')

        if m.get('OriginHttpsPort') is not None:
            self.origin_https_port = m.get('OriginHttpsPort')

        if m.get('OriginMtls') is not None:
            self.origin_mtls = m.get('OriginMtls')

        if m.get('OriginReadTimeout') is not None:
            self.origin_read_timeout = m.get('OriginReadTimeout')

        if m.get('OriginScheme') is not None:
            self.origin_scheme = m.get('OriginScheme')

        if m.get('OriginSni') is not None:
            self.origin_sni = m.get('OriginSni')

        if m.get('OriginVerify') is not None:
            self.origin_verify = m.get('OriginVerify')

        if m.get('Range') is not None:
            self.range = m.get('Range')

        if m.get('RangeChunkSize') is not None:
            self.range_chunk_size = m.get('RangeChunkSize')

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

        return self

