# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetNormalizationRuleVersionRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        normalization_rule_id: str = None,
        normalization_rule_version: int = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.lang = lang
        self.normalization_rule_id = normalization_rule_id
        self.normalization_rule_version = normalization_rule_version
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.normalization_rule_id is not None:
            result['NormalizationRuleId'] = self.normalization_rule_id

        if self.normalization_rule_version is not None:
            result['NormalizationRuleVersion'] = self.normalization_rule_version

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('NormalizationRuleId') is not None:
            self.normalization_rule_id = m.get('NormalizationRuleId')

        if m.get('NormalizationRuleVersion') is not None:
            self.normalization_rule_version = m.get('NormalizationRuleVersion')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        return self

