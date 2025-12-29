# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeApplicationScalingRuleRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        scaling_rule_name: str = None,
    ):
        # a0d2e04c-159d-40a8-b240-d2f2c263\\*\\*\\*\\*
        # 
        # This parameter is required.
        self.app_id = app_id
        # test
        # 
        # This parameter is required.
        self.scaling_rule_name = scaling_rule_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.scaling_rule_name is not None:
            result['ScalingRuleName'] = self.scaling_rule_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('ScalingRuleName') is not None:
            self.scaling_rule_name = m.get('ScalingRuleName')

        return self

