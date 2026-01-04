# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSchedulerRuleResponseBody(DaraModel):
    def __init__(
        self,
        cname: str = None,
        request_id: str = None,
        rule_name: str = None,
    ):
        # The CNAME that is assigned by Sec-Traffic Manager for the scheduling rule.
        # 
        # > To enable the scheduling rule, you must map the domain name of the service to the CNAME.
        self.cname = cname
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The name of the rule.
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cname is not None:
            result['Cname'] = self.cname

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        return self

