# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetNormalizationRuleRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        normalization_rule_id: str = None,
        normalization_security_domain_id: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        # The language of the response. Valid values:
        # - **zh** (default): Chinese.
        # - **en**: English.
        self.lang = lang
        # The normalization rule ID.
        self.normalization_rule_id = normalization_rule_id
        self.normalization_security_domain_id = normalization_security_domain_id
        # The region where the data management center of threat analysis is located. Specify the management center based on the region of your assets. Valid values:
        # - cn-hangzhou: the asset is in the Chinese mainland.
        # - ap-southeast-1: the asset is outside the Chinese mainland.
        self.region_id = region_id
        # The user ID that the administrator uses to switch to the view of another member.
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

        if self.normalization_security_domain_id is not None:
            result['NormalizationSecurityDomainId'] = self.normalization_security_domain_id

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

        if m.get('NormalizationSecurityDomainId') is not None:
            self.normalization_security_domain_id = m.get('NormalizationSecurityDomainId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        return self

