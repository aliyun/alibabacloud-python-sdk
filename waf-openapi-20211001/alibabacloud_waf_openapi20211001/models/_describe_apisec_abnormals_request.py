# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeApisecAbnormalsRequest(DaraModel):
    def __init__(
        self,
        abnormal_id: str = None,
        abnormal_level: str = None,
        abnormal_tag: str = None,
        api_format: str = None,
        api_id: str = None,
        api_tag: str = None,
        cluster_id: str = None,
        end_time: str = None,
        instance_id: str = None,
        matched_host: str = None,
        order_key: str = None,
        order_way: str = None,
        origin: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_manager_resource_group_id: str = None,
        start_time: str = None,
        user_status: str = None,
    ):
        # The risk ID.
        self.abnormal_id = abnormal_id
        # The risk level. Valid values:
        # - **high**: high risk.
        # - **medium**: medium risk.
        # - **low**: low risk.
        self.abnormal_level = abnormal_level
        # The risk type.
        # > You can call the [DescribeApisecRules](https://help.aliyun.com/document_detail/2859155.html) operation to query the supported risk types.
        self.abnormal_tag = abnormal_tag
        # The API operation associated with the risk.
        self.api_format = api_format
        # The ID of the API associated with the risk.
        self.api_id = api_id
        # The business purpose of the API.
        # > You can call the [DescribeApisecRules](https://help.aliyun.com/document_detail/2859155.html) operation to query the supported business purposes.
        self.api_tag = api_tag
        # The ID of the hybrid cloud cluster.
        # > This parameter applies only to hybrid cloud scenarios. You can call the [DescribeHybridCloudClusters](https://help.aliyun.com/document_detail/2849376.html) operation to query hybrid cloud cluster information.
        self.cluster_id = cluster_id
        # The end time of the query. The value is a UNIX timestamp (UTC). Unit: seconds.
        self.end_time = end_time
        # Instance ID of the WAF instance.
        # 
        # >  You can call the [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) operation to query instance ID of the WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The domain name or IP address to which the API operation belongs.
        self.matched_host = matched_host
        # The name of the field used for sorting. Valid values:
        # - **discoverTime**: the time when the risk was first detected. This is the default value.
        # - **abnormalLevel**: the risk level.
        # - **latestDiscoverTime**: the time when the risk was most recently detected.
        self.order_key = order_key
        # The sort order. Valid values:
        # - **desc**: descending order. This is the default value.
        # - **asc**: ascending order.
        self.order_way = order_way
        # The source of the risk type. Valid values:
        # - **custom**: custom.
        # - **default**: built-in.
        self.origin = origin
        # The page number to return in a paging query. Default value: **1**, which indicates the first page.
        self.page_number = page_number
        # The number of entries per page in a paging query. Default value: **10**, which indicates 10 entries per page.
        self.page_size = page_size
        # The region where the WAF instance is deployed. Valid values:
        # 
        # - **cn-hangzhou**: the Chinese mainland.
        # 
        # - **ap-southeast-1**: outside the Chinese mainland.
        self.region_id = region_id
        # The Alibaba Cloud resource group ID.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        # The start time of the query. The value is a UNIX timestamp (UTC). Unit: seconds.
        self.start_time = start_time
        # The risk status. Valid values:
        # - **toBeConfirmed**: to be confirmed.
        # - **confirmed**: confirmed.
        # - **toBeFixed**: to be fixed.
        # - **fixed**: fixed (manually verified).
        # - **ignored**: ignored.
        # - **toBeVerified**: to be verified by the system.
        # - **notFixed**: not fixed after verification.
        # - **systemFixed**: fixed (verified by the system).
        self.user_status = user_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.abnormal_id is not None:
            result['AbnormalId'] = self.abnormal_id

        if self.abnormal_level is not None:
            result['AbnormalLevel'] = self.abnormal_level

        if self.abnormal_tag is not None:
            result['AbnormalTag'] = self.abnormal_tag

        if self.api_format is not None:
            result['ApiFormat'] = self.api_format

        if self.api_id is not None:
            result['ApiId'] = self.api_id

        if self.api_tag is not None:
            result['ApiTag'] = self.api_tag

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.matched_host is not None:
            result['MatchedHost'] = self.matched_host

        if self.order_key is not None:
            result['OrderKey'] = self.order_key

        if self.order_way is not None:
            result['OrderWay'] = self.order_way

        if self.origin is not None:
            result['Origin'] = self.origin

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.user_status is not None:
            result['UserStatus'] = self.user_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AbnormalId') is not None:
            self.abnormal_id = m.get('AbnormalId')

        if m.get('AbnormalLevel') is not None:
            self.abnormal_level = m.get('AbnormalLevel')

        if m.get('AbnormalTag') is not None:
            self.abnormal_tag = m.get('AbnormalTag')

        if m.get('ApiFormat') is not None:
            self.api_format = m.get('ApiFormat')

        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')

        if m.get('ApiTag') is not None:
            self.api_tag = m.get('ApiTag')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MatchedHost') is not None:
            self.matched_host = m.get('MatchedHost')

        if m.get('OrderKey') is not None:
            self.order_key = m.get('OrderKey')

        if m.get('OrderWay') is not None:
            self.order_way = m.get('OrderWay')

        if m.get('Origin') is not None:
            self.origin = m.get('Origin')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('UserStatus') is not None:
            self.user_status = m.get('UserStatus')

        return self

