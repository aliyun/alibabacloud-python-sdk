# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteDynamicTagGroupRequest(DaraModel):
    def __init__(
        self,
        dynamic_tag_rule_id: str = None,
        region_id: str = None,
    ):
        # The ID of the tag rule.
        # 
        # For information about how to obtain the ID of a tag rule, see [DescribeDynamicTagRuleList](https://help.aliyun.com/document_detail/150126.html).
        # 
        # This parameter is required.
        self.dynamic_tag_rule_id = dynamic_tag_rule_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dynamic_tag_rule_id is not None:
            result['DynamicTagRuleId'] = self.dynamic_tag_rule_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DynamicTagRuleId') is not None:
            self.dynamic_tag_rule_id = m.get('DynamicTagRuleId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

