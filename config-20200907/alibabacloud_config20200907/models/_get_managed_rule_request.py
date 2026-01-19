# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetManagedRuleRequest(DaraModel):
    def __init__(
        self,
        identifier: str = None,
    ):
        # The identifier of the managed rule.
        # 
        # For more information about how to obtain the identifier of a managed rule, see [ListManagedRules](https://help.aliyun.com/document_detail/421144.html).
        # 
        # This parameter is required.
        self.identifier = identifier

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.identifier is not None:
            result['Identifier'] = self.identifier

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')

        return self

