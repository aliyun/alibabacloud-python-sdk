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
        # The ID of the sensitive data detection rule.
        # 
        # > You can query the ID of the sensitive data detection rule by calling the **DescribeRules** operation.
        self.id = id
        # The ID of the sensitive data detection rule. Separate multiple IDs with commas (,).
        # 
        # > You can query the ID of the sensitive data detection rule by calling the **DescribeRules** operation.
        self.ids = ids
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # Specifies whether to enable or disable the sensitive data detection rule. Valid values:
        # 
        # *   **0**: disables the sensitive data detection rule.
        # *   **1**: enables the sensitive data detection rule.
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

