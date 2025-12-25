# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BatchDeleteConsumerAuthorizationRuleRequest(DaraModel):
    def __init__(
        self,
        consumer_authorization_rule_ids: str = None,
    ):
        # The rule IDs.
        self.consumer_authorization_rule_ids = consumer_authorization_rule_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consumer_authorization_rule_ids is not None:
            result['consumerAuthorizationRuleIds'] = self.consumer_authorization_rule_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consumerAuthorizationRuleIds') is not None:
            self.consumer_authorization_rule_ids = m.get('consumerAuthorizationRuleIds')

        return self

