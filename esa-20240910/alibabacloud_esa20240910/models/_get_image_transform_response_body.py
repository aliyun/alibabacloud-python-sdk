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
        self.auto_avif = auto_avif
        self.auto_webp = auto_webp
        self.config_id = config_id
        self.config_type = config_type
        self.enable = enable
        self.request_id = request_id
        self.rule = rule
        self.rule_enable = rule_enable
        self.rule_name = rule_name
        self.sequence = sequence
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

