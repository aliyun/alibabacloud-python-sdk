# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCompressionRuleRequest(DaraModel):
    def __init__(
        self,
        brotli: str = None,
        gzip: str = None,
        rule: str = None,
        rule_enable: str = None,
        rule_name: str = None,
        sequence: int = None,
        site_id: int = None,
        site_version: int = None,
        zstd: str = None,
    ):
        # Brotli compression. Valid values:
        # 
        # - on: Enabled.
        # - off: Disabled.
        self.brotli = brotli
        # Gzip compression. Valid values:
        # 
        # - on: Enabled.
        # - off: Disabled.
        self.gzip = gzip
        # The rule content, which uses a conditional expression to match user requests. You do not need to set this parameter when adding a global configuration. Two scenarios are supported:
        # - Match all incoming requests: Set the value to true.
        # - Match specified requests: Set the value to a custom expression, for example, (http.host eq \\"video.example.com\\").
        self.rule = rule
        # The rule switch. You do not need to set this parameter when adding a global configuration. Valid values:
        # - on: Enabled.
        # - off: Disabled.
        self.rule_enable = rule_enable
        # The rule name. You do not need to set this parameter when adding a global configuration.
        self.rule_name = rule_name
        # The rule execution order. A smaller value indicates a higher priority.
        self.sequence = sequence
        # The site ID, which can be obtained by calling the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation.
        # 
        # This parameter is required.
        self.site_id = site_id
        # The version number of the site configuration. For sites with configuration version management enabled, you can use this parameter to specify the site version on which the configuration takes effect. The default value is version 0.
        self.site_version = site_version
        # Zstd compression. Valid values:
        # 
        # - on: Enabled.
        # - off: Disabled.
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

        if self.gzip is not None:
            result['Gzip'] = self.gzip

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

        if self.site_version is not None:
            result['SiteVersion'] = self.site_version

        if self.zstd is not None:
            result['Zstd'] = self.zstd

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Brotli') is not None:
            self.brotli = m.get('Brotli')

        if m.get('Gzip') is not None:
            self.gzip = m.get('Gzip')

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

        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')

        if m.get('Zstd') is not None:
            self.zstd = m.get('Zstd')

        return self

