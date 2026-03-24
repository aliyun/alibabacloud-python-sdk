# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeApisecApiResourcesRequest(DaraModel):
    def __init__(
        self,
        api_format: str = None,
        api_id: str = None,
        api_method: str = None,
        api_status: str = None,
        api_tag: str = None,
        api_type: str = None,
        auth_flag: str = None,
        cluster_id: str = None,
        end_time: str = None,
        follow: int = None,
        instance_id: str = None,
        matched_host: str = None,
        note: str = None,
        order_key: str = None,
        order_way: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        request_sensitive_type: str = None,
        resource_manager_resource_group_id: str = None,
        sensitive_level: str = None,
        sensitive_type: str = None,
        start_time: str = None,
    ):
        # The API endpoint path used to filter the query results.
        self.api_format = api_format
        # The ID of the API.
        self.api_id = api_id
        # The HTTP request method of the API. Valid values: **GET**, **POST**, **HEAD**, **PUT**, **DELETE**, **CONNECT**, **PATCH**, and **OPTIONS**.
        self.api_method = api_method
        # The lifecycle status of the API. Valid values:
        # 
        # - **NewbornInterface**: newly discovered.
        # 
        # - **OfflineInterface**: inactive.
        # 
        # - **normal**: active.
        self.api_status = api_status
        # The business purpose of the API.
        # 
        # > Call the [DescribeApisecRules](https://help.aliyun.com/document_detail/2859155.html) operation to obtain the supported business purposes.
        self.api_tag = api_tag
        # The type of service that the API serves. Valid values:
        # 
        # - **PublicAPI**: public-facing service.
        # 
        # - **ThirdpartAPI**: third-party service.
        # 
        # - **InternalAPI**: internal service.
        self.api_type = api_type
        # Indicates whether the API requires authentication. Valid values:
        # 
        # - **0**: The API requires authentication.
        # 
        # - **1**: The API does not require authentication.
        self.auth_flag = auth_flag
        # The ID of the Hybrid Cloud WAF cluster.
        # 
        # > This parameter is available only for hybrid cloud scenarios. Call the [DescribeHybridCloudClusters](https://help.aliyun.com/document_detail/2849376.html) operation to obtain information about Hybrid Cloud WAF clusters.
        self.cluster_id = cluster_id
        # The end of the time range to query. Specify a UNIX timestamp in seconds.
        self.end_time = end_time
        # Indicates whether the API is followed. Valid values:
        # 
        # - **1**: The API is followed.
        # 
        # - **0**: The API is not followed.
        self.follow = follow
        # The ID of the WAF instance.
        # 
        # > Call the [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) operation to obtain the ID of the WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The domain name or IP address of the API used to filter the query results.
        self.matched_host = matched_host
        # The remarks of the API asset used to filter the query results.
        self.note = note
        # The field by which to sort the results. Valid values:
        # 
        # - **allCnt**: sorts by the total number of requests in the last 30 days.
        # 
        # - **botCnt**: sorts by the number of bot requests in the last 30 days.
        # 
        # - **crossBorderCnt**: sorts by the number of cross-border requests in the last 30 days.
        # 
        # - **abnormalNum**: sorts by the number of threats associated with the API.
        # 
        # - **eventNum**: sorts by the number of security events associated with the API.
        # 
        # - **farthestTs**: sorts by the time when the API was first discovered.
        # 
        # - **lastestTs**: sorts by the time of the most recent access.
        self.order_key = order_key
        # The sort order. Valid values:
        # 
        # - **desc**: descending order (default).
        # 
        # - **asc**: ascending order.
        self.order_way = order_way
        # The page number. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Default value: **10**.
        self.page_size = page_size
        # The region ID of the WAF instance. Valid values:
        # 
        # - **cn-hangzhou**: the Chinese mainland.
        # 
        # - **ap-southeast-1**: outside the Chinese mainland.
        self.region_id = region_id
        # The type of sensitive data in the request.
        # 
        # > Call the [DescribeApisecRules](https://help.aliyun.com/document_detail/2859155.html) operation to obtain the supported sensitive data types.
        self.request_sensitive_type = request_sensitive_type
        # The ID of the Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        # The sensitivity level of the API. Valid values:
        # 
        # - **L1**: High.
        # 
        # - **L2**: Medium.
        # 
        # - **L3**: Low.
        # 
        # - **N**: Non-sensitive.
        self.sensitive_level = sensitive_level
        # The type of sensitive data in the response.
        # 
        # > Call the [DescribeApisecRules](https://help.aliyun.com/document_detail/2859155.html) operation to obtain the supported sensitive data types.
        self.sensitive_type = sensitive_type
        # The beginning of the time range to query. Specify a UNIX timestamp in seconds.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_format is not None:
            result['ApiFormat'] = self.api_format

        if self.api_id is not None:
            result['ApiId'] = self.api_id

        if self.api_method is not None:
            result['ApiMethod'] = self.api_method

        if self.api_status is not None:
            result['ApiStatus'] = self.api_status

        if self.api_tag is not None:
            result['ApiTag'] = self.api_tag

        if self.api_type is not None:
            result['ApiType'] = self.api_type

        if self.auth_flag is not None:
            result['AuthFlag'] = self.auth_flag

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.follow is not None:
            result['Follow'] = self.follow

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.matched_host is not None:
            result['MatchedHost'] = self.matched_host

        if self.note is not None:
            result['Note'] = self.note

        if self.order_key is not None:
            result['OrderKey'] = self.order_key

        if self.order_way is not None:
            result['OrderWay'] = self.order_way

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_sensitive_type is not None:
            result['RequestSensitiveType'] = self.request_sensitive_type

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        if self.sensitive_level is not None:
            result['SensitiveLevel'] = self.sensitive_level

        if self.sensitive_type is not None:
            result['SensitiveType'] = self.sensitive_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiFormat') is not None:
            self.api_format = m.get('ApiFormat')

        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')

        if m.get('ApiMethod') is not None:
            self.api_method = m.get('ApiMethod')

        if m.get('ApiStatus') is not None:
            self.api_status = m.get('ApiStatus')

        if m.get('ApiTag') is not None:
            self.api_tag = m.get('ApiTag')

        if m.get('ApiType') is not None:
            self.api_type = m.get('ApiType')

        if m.get('AuthFlag') is not None:
            self.auth_flag = m.get('AuthFlag')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Follow') is not None:
            self.follow = m.get('Follow')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MatchedHost') is not None:
            self.matched_host = m.get('MatchedHost')

        if m.get('Note') is not None:
            self.note = m.get('Note')

        if m.get('OrderKey') is not None:
            self.order_key = m.get('OrderKey')

        if m.get('OrderWay') is not None:
            self.order_way = m.get('OrderWay')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestSensitiveType') is not None:
            self.request_sensitive_type = m.get('RequestSensitiveType')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        if m.get('SensitiveLevel') is not None:
            self.sensitive_level = m.get('SensitiveLevel')

        if m.get('SensitiveType') is not None:
            self.sensitive_type = m.get('SensitiveType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

