# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetCompressionRuleResponseBody(DaraModel):
    def __init__(
        self,
        brotli: str = None,
        config_id: int = None,
        config_type: str = None,
        gzip: str = None,
        request_id: str = None,
        rule: str = None,
        rule_enable: str = None,
        rule_name: str = None,
        sequence: int = None,
        site_version: int = None,
        zstd: str = None,
    ):
        # Brotli compression. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.brotli = brotli
        # The ID of the configuration.
        self.config_id = config_id
        # The type of the configuration. Valid values:
        # - global: global configuration.
        # - rule: rule configuration.
        self.config_type = config_type
        # Gzip compression. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.gzip = gzip
        # The ID of the request.
        self.request_id = request_id
        # The rule content, which uses a conditional expression to match user requests. You do not need to set this parameter when adding a global configuration. Two scenarios are supported:
        # - Match all incoming requests: set the value to true.
        # - Match specific requests: set the value to a custom expression, such as (http.host eq "video.example.com").
        self.rule = rule
        # The rule switch. You do not need to set this parameter when adding a global configuration. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.rule_enable = rule_enable
        # The name of the rule. You do not need to set this parameter when adding a global configuration.
        self.rule_name = rule_name
        # The execution sequence of the rule. A smaller value indicates a higher priority.
        self.sequence = sequence
        # The version number of the site configuration. For sites with configuration version management enabled, you can use this parameter to specify the site version for which the configuration takes effect. The default value is version 0.
        self.site_version = site_version
        # Zstd compression. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.zstd = zstd

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.brotli is not None:
            result['Brotli'] = self.brotli

        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.config_type is not None:
            result['ConfigType'] = self.config_type

        if self.gzip is not None:
            result['Gzip'] = self.gzip

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

        if self.site_version is not None:
            result['SiteVersion'] = self.site_version

        if self.zstd is not None:
            result['Zstd'] = self.zstd

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Brotli') is not None:
            self.brotli = m.get('Brotli')

        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('ConfigType') is not None:
            self.config_type = m.get('ConfigType')

        if m.get('Gzip') is not None:
            self.gzip = m.get('Gzip')

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

        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')

        if m.get('Zstd') is not None:
            self.zstd = m.get('Zstd')

        return self

