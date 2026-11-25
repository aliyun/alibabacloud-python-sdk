# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeAiEngineEventsRequest(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        filter: main_models.DescribeAiEngineEventsRequestFilter = None,
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
        start_time: int = None,
    ):
        # The end time. The time is a UNIX timestamp in UTC. Unit: seconds. The data is filtered based on the time when the event was last detected. The end time must be later than the start time.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The filter conditions. Exact match is used, and multiple conditions are connected by the AND logical operator.
        self.filter = filter
        # The ID of the WAF instance.
        # 
        # > You can call the [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) operation to query the ID of the current WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The language of the response.
        self.language = language
        # The number of entries to return on each page in a paging query. Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # The pagination token. The value is the **NextToken** parameter value returned by the previous API call. You do not need to specify this parameter for the first query.
        self.next_token = next_token
        # The region ID of the WAF instance.
        self.region_id = region_id
        # The ID of the Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        # The search value. This parameter is used together with SearchKey. Maximum length: 256 characters.
        self.seach_value = seach_value
        # The search field. This parameter is used together with SeachValue.
        self.search_key = search_key
        # The field by which to sort the results.
        self.sort_by = sort_by
        # The sort order.
        self.sort_order = sort_order
        # The start time. The time is a UNIX timestamp in UTC. Unit: seconds. The data is filtered based on the time when the event was last detected. You can query data within the last 30 days.
        # 
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        if self.filter:
            self.filter.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

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

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Filter') is not None:
            temp_model = main_models.DescribeAiEngineEventsRequestFilter()
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

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class DescribeAiEngineEventsRequestFilter(DaraModel):
    def __init__(
        self,
        domain: str = None,
        event_id: str = None,
        event_node_count: int = None,
        handle_status: str = None,
        resource: str = None,
        risk_level: str = None,
        source_account: str = None,
        source_fingerprint: str = None,
        source_ip: str = None,
    ):
        # The domain name.
        self.domain = domain
        # The event ID.
        self.event_id = event_id
        # The number of nodes included in the event.
        self.event_node_count = event_node_count
        # The event handling status.
        self.handle_status = handle_status
        # The protected object.
        self.resource = resource
        # The risk level.
        self.risk_level = risk_level
        # The source account of the attack.
        self.source_account = source_account
        # The source fingerprint of the attack.
        self.source_fingerprint = source_fingerprint
        # The source IP address of the attack.
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['domain'] = self.domain

        if self.event_id is not None:
            result['eventId'] = self.event_id

        if self.event_node_count is not None:
            result['eventNodeCount'] = self.event_node_count

        if self.handle_status is not None:
            result['handleStatus'] = self.handle_status

        if self.resource is not None:
            result['resource'] = self.resource

        if self.risk_level is not None:
            result['riskLevel'] = self.risk_level

        if self.source_account is not None:
            result['sourceAccount'] = self.source_account

        if self.source_fingerprint is not None:
            result['sourceFingerprint'] = self.source_fingerprint

        if self.source_ip is not None:
            result['sourceIp'] = self.source_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')

        if m.get('eventId') is not None:
            self.event_id = m.get('eventId')

        if m.get('eventNodeCount') is not None:
            self.event_node_count = m.get('eventNodeCount')

        if m.get('handleStatus') is not None:
            self.handle_status = m.get('handleStatus')

        if m.get('resource') is not None:
            self.resource = m.get('resource')

        if m.get('riskLevel') is not None:
            self.risk_level = m.get('riskLevel')

        if m.get('sourceAccount') is not None:
            self.source_account = m.get('sourceAccount')

        if m.get('sourceFingerprint') is not None:
            self.source_fingerprint = m.get('sourceFingerprint')

        if m.get('sourceIp') is not None:
            self.source_ip = m.get('sourceIp')

        return self

