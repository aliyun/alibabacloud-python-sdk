# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pvtz20180101 import models as main_models
from darabonba.model import DaraModel

class DescribeZonesRequest(DaraModel):
    def __init__(
        self,
        keyword: str = None,
        lang: str = None,
        page_number: int = None,
        page_size: int = None,
        query_region_id: str = None,
        query_vpc_id: str = None,
        resource_group_id: str = None,
        resource_tag: List[main_models.DescribeZonesRequestResourceTag] = None,
        search_mode: str = None,
        zone_tag: List[str] = None,
        zone_type: str = None,
    ):
        # The keyword of the zone name. The value is not case-sensitive. You can set SearchMode to LIKE or EXACT. The default value of SearchMode is LIKE.
        self.keyword = keyword
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        # 
        # Default value: en.
        self.lang = lang
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: **1 to 100**. Default value: **20**.
        self.page_size = page_size
        # The region ID of the virtual private cloud (VPC) associated with the zone.
        self.query_region_id = query_region_id
        # The ID of the VPC associated with the zone.
        self.query_vpc_id = query_vpc_id
        # The ID of the resource group to which the zone belongs.
        self.resource_group_id = resource_group_id
        # The tags added to the zone.
        self.resource_tag = resource_tag
        # The search mode. The value of Keyword is the search scope. Valid values:
        # 
        # *   **LIKE** (default): fuzzy search
        # *   **EXACT**: exact search
        # 
        # Default value: **LIKE**.
        self.search_mode = search_mode
        # The types of cloud services.
        self.zone_tag = zone_tag
        # The zone type. Valid values:
        # 
        # *   **AUTH_ZONE**: authoritative zone
        # *   **CLOUD_PRODUCT_ZONE**: authoritative zone for cloud services
        # 
        # Default value: **AUTH_ZONE**.
        self.zone_type = zone_type

    def validate(self):
        if self.resource_tag:
            for v1 in self.resource_tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.query_region_id is not None:
            result['QueryRegionId'] = self.query_region_id

        if self.query_vpc_id is not None:
            result['QueryVpcId'] = self.query_vpc_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['ResourceTag'] = []
        if self.resource_tag is not None:
            for k1 in self.resource_tag:
                result['ResourceTag'].append(k1.to_map() if k1 else None)

        if self.search_mode is not None:
            result['SearchMode'] = self.search_mode

        if self.zone_tag is not None:
            result['ZoneTag'] = self.zone_tag

        if self.zone_type is not None:
            result['ZoneType'] = self.zone_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('QueryRegionId') is not None:
            self.query_region_id = m.get('QueryRegionId')

        if m.get('QueryVpcId') is not None:
            self.query_vpc_id = m.get('QueryVpcId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.resource_tag = []
        if m.get('ResourceTag') is not None:
            for k1 in m.get('ResourceTag'):
                temp_model = main_models.DescribeZonesRequestResourceTag()
                self.resource_tag.append(temp_model.from_map(k1))

        if m.get('SearchMode') is not None:
            self.search_mode = m.get('SearchMode')

        if m.get('ZoneTag') is not None:
            self.zone_tag = m.get('ZoneTag')

        if m.get('ZoneType') is not None:
            self.zone_type = m.get('ZoneType')

        return self

class DescribeZonesRequestResourceTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N added to the zone.
        self.key = key
        # The value of tag N added to the zone.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

