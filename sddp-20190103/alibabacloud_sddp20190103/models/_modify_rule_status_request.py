# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyRuleStatusRequest(DaraModel):
    def __init__(
        self,
        id: int = None,
        ids: str = None,
        lang: str = None,
        status: int = None,
    ):
        # The unique ID of the sensitive data detection rule.
        # 
        # > To enable or disable the detection feature of a sensitive data detection rule, you must specify the unique ID of the rule. You can call the **DescribeRules** operation to obtain the ID.
        self.id = id
        # The unique IDs of the sensitive data detection rules. Separate multiple IDs with commas (,).
        # > To enable or disable the detection feature of a sensitive data detection rule, you must specify the unique ID of the rule. You can call the **DescribeRules** operation to obtain the ID.
        self.ids = ids
        # The language of the request and response. Valid values:
        # - **zh**: Chinese.
        # - **en**: English.
        self.lang = lang
        # Specifies whether to enable or disable the detection feature of the sensitive data detection rule. Valid values:
        # - **0**: disabled.  
        # - **1**: enabled.
        # 
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.ids is not None:
            result['Ids'] = self.ids

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Ids') is not None:
            self.ids = m.get('Ids')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

