# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeAiEngineEvidenceRequestsRequest(DaraModel):
    def __init__(
        self,
        event_id: str = None,
        filter: main_models.DescribeAiEngineEvidenceRequestsRequestFilter = None,
        instance_id: str = None,
        language: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        resource_manager_resource_group_id: str = None,
        seach_value: str = None,
        search_key: str = None,
        sort_by: str = None,
        sort_order: str = None,
    ):
        # The event ID.
        # 
        # This parameter is required.
        self.event_id = event_id
        # The filter conditions. Exact match is used, and multiple conditions are connected by the AND logical operator.
        self.filter = filter
        # The ID of the WAF instance.
        # 
        # > You can call the [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) operation to query the ID of the current WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The response language.
        self.language = language
        # The number of entries to return per page. Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # The pagination token for the next page. The value is the **NextToken** parameter value returned by the previous API call. You do not need to specify this parameter for the first query.
        self.next_token = next_token
        # The region where the WAF instance resides.
        self.region_id = region_id
        # The ID of the Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        # The search value. This parameter is used together with SearchKey. The value can be up to 256 characters in length.
        self.seach_value = seach_value
        # The search key. This parameter is used together with SeachValue.
        self.search_key = search_key
        # The sort field.
        self.sort_by = sort_by
        # The sort order.
        self.sort_order = sort_order

    def validate(self):
        if self.filter:
            self.filter.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.filter is not None:
            result['Filter'] = self.filter.to_map()

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

        if self.seach_value is not None:
            result['SeachValue'] = self.seach_value

        if self.search_key is not None:
            result['SearchKey'] = self.search_key

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('Filter') is not None:
            temp_model = main_models.DescribeAiEngineEvidenceRequestsRequestFilter()
            self.filter = temp_model.from_map(m.get('Filter'))

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

        if m.get('SeachValue') is not None:
            self.seach_value = m.get('SeachValue')

        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')

        return self

class DescribeAiEngineEvidenceRequestsRequestFilter(DaraModel):
    def __init__(
        self,
        http_status: str = None,
        impact_type: str = None,
        method: str = None,
        node_id: str = None,
        source_type: str = None,
        suspected_bypass: str = None,
    ):
        # The HTTP status code.
        self.http_status = http_status
        # The evidence impact tag.
        self.impact_type = impact_type
        # The HTTP request method. Exact match is used.
        self.method = method
        # The node ID. Exact match is used. The value can be up to 64 ASCII characters in length.
        self.node_id = node_id
        # The attack source type.
        self.source_type = source_type
        # Specifies whether the request is a suspected bypass.
        self.suspected_bypass = suspected_bypass

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.http_status is not None:
            result['httpStatus'] = self.http_status

        if self.impact_type is not None:
            result['impactType'] = self.impact_type

        if self.method is not None:
            result['method'] = self.method

        if self.node_id is not None:
            result['nodeId'] = self.node_id

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        if self.suspected_bypass is not None:
            result['suspectedBypass'] = self.suspected_bypass

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('httpStatus') is not None:
            self.http_status = m.get('httpStatus')

        if m.get('impactType') is not None:
            self.impact_type = m.get('impactType')

        if m.get('method') is not None:
            self.method = m.get('method')

        if m.get('nodeId') is not None:
            self.node_id = m.get('nodeId')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        if m.get('suspectedBypass') is not None:
            self.suspected_bypass = m.get('suspectedBypass')

        return self

