# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeIpAbroadCountryInfosRequest(DaraModel):
    def __init__(
        self,
        abroad_region: str = None,
        country: str = None,
        instance_id: str = None,
        language: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        resource_manager_resource_group_id: str = None,
    ):
        # The region outside China to query. Supports fuzzy query by region ID or region name in Chinese or English.
        self.abroad_region = abroad_region
        # The country outside China to query. Supports fuzzy query by country ID or country name in Chinese or English.
        self.country = country
        # The ID of the WAF instance.
        # 
        # > Call the [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) operation to query the current WAF instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The language used for country and region names in the response. Valid values:
        # 
        # - **en** (**default**): English.
        # 
        # - **cn**: Simplified Chinese.
        self.language = language
        # The number of entries per page in a paged query. Valid values: 1 to 500. Default value: 20.
        self.max_results = max_results
        # The token for the next page. Set this parameter to the value of the **NextToken** parameter returned from the previous API call. You do not need to specify this parameter for the first page query.
        self.next_token = next_token
        # The region in which the WAF instance is deployed. Valid values:
        # 
        # - **cn-hangzhou**: The Chinese mainland.
        # 
        # - **ap-southeast-1**: Outside the Chinese mainland.
        self.region_id = region_id
        # The ID of the Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.abroad_region is not None:
            result['AbroadRegion'] = self.abroad_region

        if self.country is not None:
            result['Country'] = self.country

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.language is not None:
            result['Language'] = self.language

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AbroadRegion') is not None:
            self.abroad_region = m.get('AbroadRegion')

        if m.get('Country') is not None:
            self.country = m.get('Country')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        return self

