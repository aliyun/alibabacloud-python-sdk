# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSensitiveOutboundStatisticRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        detection_result: str = None,
        end_time: int = None,
        instance_id: str = None,
        order_key: str = None,
        order_way: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_manager_resource_group_id: str = None,
        sensitive_code: str = None,
        sensitive_level: str = None,
        sensitive_type: str = None,
        start_time: int = None,
    ):
        # The ID of the hybrid cloud cluster.
        # > This parameter is only applicable to hybrid cloud scenarios. You can call the [DescribeHybridCloudClusters](https://help.aliyun.com/document_detail/2849376.html) operation to query the information about hybrid cloud clusters.
        self.cluster_id = cluster_id
        # The assessment result. Valid values:
        # - **report**: Outbound data risks exist.
        # - **none**: No outbound data risks exist.
        self.detection_result = detection_result
        # The end time of the query. The value is a UNIX timestamp in UTC. Unit: seconds.
        # > Compliance audit currently supports querying data for the last 1 month, last 3 months, last 6 months, last 12 months, and from January 1 of the previous year to the present. Make sure that the specified time range is valid.
        self.end_time = end_time
        # The ID of the WAF instance.
        # > You can call the [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) operation to query the ID of the WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the field used for sorting. Valid values:
        # - **total_count**: the total number of data records (default)
        # - **outbound_count**: the total number of outbound data records
        self.order_key = order_key
        # The sorting method. Valid values:
        # - **desc**: descending order (default)
        # - **asc**: ascending order
        self.order_way = order_way
        # The number of the page to return in a paging query. Default value: **1**, which indicates the first page.
        self.page_number = page_number
        # The number of entries to return on each page in a paging query. Default value: **10**, which indicates 10 entries per page.
        self.page_size = page_size
        # The region where the WAF instance resides. Valid values:
        # - **cn-hangzhou**: the Chinese mainland
        # - **ap-southeast-1**: outside the Chinese mainland
        self.region_id = region_id
        # The ID of the Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        # The sensitive data types. Separate multiple sensitive data types with commas (,).
        # > You can call the [DescribeApisecRules](https://help.aliyun.com/document_detail/2859155.html) operation to query the supported sensitive data types. This parameter only supports built-in sensitive data types.
        self.sensitive_code = sensitive_code
        # The sensitivity level. Valid values: 
        # - **high**: high sensitivity
        # - **medium**: medium sensitivity
        # - **low**: low sensitivity
        self.sensitive_level = sensitive_level
        # The type of information to query. Valid values: 
        # - **info**: all personal information (default)
        # - **sensitive**: only sensitive personal information
        self.sensitive_type = sensitive_type
        # The start time of the query. The value is a UNIX timestamp in UTC. Unit: seconds.
        # > Compliance audit currently supports querying data for the last 1 month, last 3 months, last 6 months, last 12 months, and from January 1 of the previous year to the present. Make sure that the specified time range is valid.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.detection_result is not None:
            result['DetectionResult'] = self.detection_result

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

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

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        if self.sensitive_code is not None:
            result['SensitiveCode'] = self.sensitive_code

        if self.sensitive_level is not None:
            result['SensitiveLevel'] = self.sensitive_level

        if self.sensitive_type is not None:
            result['SensitiveType'] = self.sensitive_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('DetectionResult') is not None:
            self.detection_result = m.get('DetectionResult')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

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

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        if m.get('SensitiveCode') is not None:
            self.sensitive_code = m.get('SensitiveCode')

        if m.get('SensitiveLevel') is not None:
            self.sensitive_level = m.get('SensitiveLevel')

        if m.get('SensitiveType') is not None:
            self.sensitive_type = m.get('SensitiveType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

