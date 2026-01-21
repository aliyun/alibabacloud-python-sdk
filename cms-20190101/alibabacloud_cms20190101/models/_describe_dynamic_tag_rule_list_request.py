# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDynamicTagRuleListRequest(DaraModel):
    def __init__(
        self,
        dynamic_tag_rule_id: str = None,
        page_number: str = None,
        page_size: str = None,
        tag_key: str = None,
        tag_region_id: str = None,
        tag_value: str = None,
    ):
        # The ID of the tag rule.
        self.dynamic_tag_rule_id = dynamic_tag_rule_id
        # The number of the page to return.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page.
        # 
        # Minimum value: 1. Default value: 30.
        self.page_size = page_size
        # The tag key.
        # 
        # For more information about how to obtain a tag key, see [DescribeTagKeyList](https://help.aliyun.com/document_detail/145558.html).
        self.tag_key = tag_key
        # The ID of the region to which the tags belong.
        self.tag_region_id = tag_region_id
        # The tag value.
        # 
        # For more information about how to obtain a tag value, see [DescribeTagKeyList](https://help.aliyun.com/document_detail/145557.html).
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dynamic_tag_rule_id is not None:
            result['DynamicTagRuleId'] = self.dynamic_tag_rule_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_region_id is not None:
            result['TagRegionId'] = self.tag_region_id

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DynamicTagRuleId') is not None:
            self.dynamic_tag_rule_id = m.get('DynamicTagRuleId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagRegionId') is not None:
            self.tag_region_id = m.get('TagRegionId')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

