# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetRulesCountResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        total_system_client_rule_count: int = None,
        total_user_define_rule_count: int = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The total number of system defense rules.
        self.total_system_client_rule_count = total_system_client_rule_count
        # The total number of custom defense rules.
        self.total_user_define_rule_count = total_user_define_rule_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_system_client_rule_count is not None:
            result['TotalSystemClientRuleCount'] = self.total_system_client_rule_count

        if self.total_user_define_rule_count is not None:
            result['TotalUserDefineRuleCount'] = self.total_user_define_rule_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalSystemClientRuleCount') is not None:
            self.total_system_client_rule_count = m.get('TotalSystemClientRuleCount')

        if m.get('TotalUserDefineRuleCount') is not None:
            self.total_user_define_rule_count = m.get('TotalUserDefineRuleCount')

        return self

