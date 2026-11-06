# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePolarClawSkillsMarketRequest(DaraModel):
    def __init__(
        self,
        order_by: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        search_by_skill_name: str = None,
        search_by_tag_name: str = None,
        source: str = None,
    ):
        # The sorting condition. DOWNLOAD_COUNT indicates sorting by download count.
        self.order_by = order_by
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Valid values:
        # * **30**
        # * **50**
        # * **100**
        # 
        # Default value: **30**.
        self.page_size = page_size
        # The region ID.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/98041.html) operation to query all available regions for the current account, including region IDs.
        self.region_id = region_id
        # The skill name to search by.
        self.search_by_skill_name = search_by_skill_name
        # The tag name to search by.
        self.search_by_tag_name = search_by_tag_name
        # The source of the skill. SELF indicates private skills of the current user, and PUBLIC indicates public skills.
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.search_by_skill_name is not None:
            result['SearchBySkillName'] = self.search_by_skill_name

        if self.search_by_tag_name is not None:
            result['SearchByTagName'] = self.search_by_tag_name

        if self.source is not None:
            result['Source'] = self.source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SearchBySkillName') is not None:
            self.search_by_skill_name = m.get('SearchBySkillName')

        if m.get('SearchByTagName') is not None:
            self.search_by_tag_name = m.get('SearchByTagName')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        return self

