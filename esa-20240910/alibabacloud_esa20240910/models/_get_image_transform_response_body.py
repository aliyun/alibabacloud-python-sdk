# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetImageTransformResponseBody(DaraModel):
    def __init__(
        self,
        auto_avif: str = None,
        auto_webp: str = None,
        config_id: int = None,
        config_type: str = None,
        enable: str = None,
        request_id: str = None,
        rule: str = None,
        rule_enable: str = None,
        rule_name: str = None,
        sequence: int = None,
        site_version: int = None,
    ):
        # Specifies whether adaptive AVIF is enabled. Valid values:
        # - on: enabled
        # - off: disabled
        self.auto_avif = auto_avif
        # Specifies whether adaptive WebP is enabled. Valid values:
        # - on: enabled
        # - off: disabled
        self.auto_webp = auto_webp
        # The ID of the configuration.
        self.config_id = config_id
        # The type of the configuration. Valid values:
        # - global: global configuration
        # - rule: rule configuration
        self.config_type = config_type
        # Specifies whether image transform is enabled. Valid values:
        # - on: enabled
        # - off: disabled
        self.enable = enable
        # The ID of the request.
        self.request_id = request_id
        # The rule content, which uses a conditional expression to match user requests. You do not need to set this parameter when adding a global configuration. Two scenarios are supported:
        # - Match all incoming requests: Set the value to true.
        # - Match specific requests: Set the value to a custom expression, such as (http.host eq "video.example.com").
        self.rule = rule
        # The rule switch. You do not need to set this parameter when adding a global configuration. Valid values:
        # - on: enabled
        # - off: disabled
        self.rule_enable = rule_enable
        # The name of the rule. You do not need to set this parameter when adding a global configuration.
        self.rule_name = rule_name
        # The execution sequence of the rule. A smaller value indicates a higher execution priority.
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
        if self.auto_avif is not None:
            result['AutoAvif'] = self.auto_avif

        if self.auto_webp is not None:
            result['AutoWebp'] = self.auto_webp

        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.config_type is not None:
            result['ConfigType'] = self.config_type

        if self.enable is not None:
            result['Enable'] = self.enable

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoAvif') is not None:
            self.auto_avif = m.get('AutoAvif')

        if m.get('AutoWebp') is not None:
            self.auto_webp = m.get('AutoWebp')

        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('ConfigType') is not None:
            self.config_type = m.get('ConfigType')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

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

        return self

