# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateConfigRulesReportRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        config_rule_ids: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The ID of the rule. Separate multiple rule IDs with commas (,).
        # 
        # For more information about how to query the ID of a rule, see [ListConfigRules](https://help.aliyun.com/document_detail/169607.html).
        self.config_rule_ids = config_rule_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.config_rule_ids is not None:
            result['ConfigRuleIds'] = self.config_rule_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ConfigRuleIds') is not None:
            self.config_rule_ids = m.get('ConfigRuleIds')

        return self

