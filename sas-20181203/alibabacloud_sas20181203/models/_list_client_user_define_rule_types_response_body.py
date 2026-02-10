# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListClientUserDefineRuleTypesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        user_define_rule_types: List[str] = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # An array consisting of the rule types that are supported.
        self.user_define_rule_types = user_define_rule_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.user_define_rule_types is not None:
            result['UserDefineRuleTypes'] = self.user_define_rule_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UserDefineRuleTypes') is not None:
            self.user_define_rule_types = m.get('UserDefineRuleTypes')

        return self

