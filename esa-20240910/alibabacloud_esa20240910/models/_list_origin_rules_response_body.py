# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ListOriginRulesResponseBody(DaraModel):
    def __init__(
        self,
        configs: List[main_models.ListOriginRulesResponseBodyConfigs] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        total_page: int = None,
    ):
        # The configurations in the response.
        self.configs = configs
        # The current page number, same as the PageNumber request parameter.
        self.page_number = page_number
        # The page size.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of records.
        self.total_count = total_count
        # The total number of pages.
        self.total_page = total_page

    def validate(self):
        if self.configs:
            for v1 in self.configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Configs'] = []
        if self.configs is not None:
            for k1 in self.configs:
                result['Configs'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.configs = []
        if m.get('Configs') is not None:
            for k1 in m.get('Configs'):
                temp_model = main_models.ListOriginRulesResponseBodyConfigs()
                self.configs.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        return self

class ListOriginRulesResponseBodyConfigs(DaraModel):
    def __init__(
        self,
        config_id: int = None,
        config_type: str = None,
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
        site_version: int = None,
    ):
        # The configuration ID.
        self.config_id = config_id
        # The configuration type. You can query global or rule configurations based on this parameter. Valid values:
        # 
        # - global: Query global configurations.
        # - rule: Query rule configurations.
        self.config_type = config_type
        # The rewritten DNS resolution record for back-to-origin requests.
        self.dns_record = dns_record
        # The back-to-origin 302 redirect follow switch. Valid values:
        # - on: Enable.
        # - off: Disable.
        self.follow_302enable = follow_302enable
        # The maximum number of 302 redirect follows. Valid values: 1 to 5.
        self.follow_302max_tries = follow_302max_tries
        # The switch for retaining original request parameters. Valid values:
        # - on: Enable.
        # - off: Disable.
        self.follow_302retain_args = follow_302retain_args
        # The switch for retaining original request headers. Valid values:
        # - on: Enable.
        # - off: Disable.
        self.follow_302retain_header = follow_302retain_header
        # The back-to-origin host after 302 redirect modification.
        self.follow_302target_host = follow_302target_host
        # The HOST carried in the back-to-origin request.
        self.origin_host = origin_host
        # The origin server port accessed when using the HTTP protocol for back-to-origin.
        self.origin_http_port = origin_http_port
        # The origin server port accessed when using the HTTPS protocol for back-to-origin.
        self.origin_https_port = origin_https_port
        # The mTLS switch. Valid values:
        # - on: Enable.
        # - off: Disable.
        self.origin_mtls = origin_mtls
        # The origin server read timeout period, in seconds.
        self.origin_read_timeout = origin_read_timeout
        # The protocol used for back-to-origin requests. Valid values:
        # - http: Use the HTTP protocol for back-to-origin.
        # - https: Use the HTTPS protocol for back-to-origin.
        # - follow: Follow the client protocol for back-to-origin.
        self.origin_scheme = origin_scheme
        # The SNI carried in the back-to-origin request.
        self.origin_sni = origin_sni
        # The origin server certificate verification switch. Valid values:
        # - on: Enable.
        # - off: Disable.
        self.origin_verify = origin_verify
        # Use range-based slicing for back-to-origin file downloads. Valid values:
        # - on: Enable.
        # - off: Disable.
        # - force: Force enable.
        self.range = range
        # The range chunk size.
        self.range_chunk_size = range_chunk_size
        # The rule content, which uses conditional expressions to match user requests. You do not need to set this parameter when adding a global configuration. There are two usage scenarios:
        # - Match all incoming requests: Set the value to true.
        # - Match specified requests: Set the value to a custom expression, for example: (http.host eq \\"video.example.com\\")
        self.rule = rule
        # The rule switch. You do not need to set this parameter when adding a global configuration. Valid values:
        # - on: Enable.
        # - off: Disable.
        self.rule_enable = rule_enable
        # The rule name. You do not need to set this parameter when adding a global configuration.
        self.rule_name = rule_name
        # The execution order of the rule. A smaller value indicates a higher priority.
        self.sequence = sequence
        # The version number of the site configuration. For sites with configuration version management enabled, you can use this parameter to specify the site version for which the configuration takes effect. Default value: 0.
        self.site_version = site_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.config_type is not None:
            result['ConfigType'] = self.config_type

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

        if self.site_version is not None:
            result['SiteVersion'] = self.site_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('ConfigType') is not None:
            self.config_type = m.get('ConfigType')

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

        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')

        return self

