# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateResourceRuleItemResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        resource_rule_item_id: str = None,
    ):
        self.request_id = request_id
        self.resource_rule_item_id = resource_rule_item_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_rule_item_id is not None:
            result['ResourceRuleItemId'] = self.resource_rule_item_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceRuleItemId') is not None:
            self.resource_rule_item_id = m.get('ResourceRuleItemId')

        return self

