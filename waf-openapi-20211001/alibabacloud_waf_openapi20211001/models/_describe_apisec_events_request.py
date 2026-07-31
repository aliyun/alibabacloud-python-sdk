# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeApisecEventsRequest(DaraModel):
    def __init__(
        self,
        account: str = None,
        api_format: str = None,
        api_id: str = None,
        api_tag: str = None,
        attack_ip: str = None,
        cluster_id: str = None,
        end_ts: int = None,
        event_id: str = None,
        event_level: str = None,
        event_scope: str = None,
        event_tag: str = None,
        instance_id: str = None,
        matched_host: str = None,
        order_key: str = None,
        order_way: str = None,
        origin: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_manager_resource_group_id: str = None,
        start_ts: int = None,
        user_status: str = None,
    ):
        # The account information.
        self.account = account
        # The API operation.
        self.api_format = api_format
        # The ID of the API.
        self.api_id = api_id
        # The business purpose of the API.
        # > You can call [DescribeApisecRules](https://help.aliyun.com/document_detail/2859155.html) to obtain the supported business purposes.
        self.api_tag = api_tag
        # The attack IP address.
        self.attack_ip = attack_ip
        # The hybrid cloud cluster ID.
        # > This parameter applies only to hybrid cloud scenarios. You can call [DescribeHybridCloudClusters](https://help.aliyun.com/document_detail/2849376.html) to obtain hybrid cloud cluster information.
        self.cluster_id = cluster_id
        # The end time of the query, in UNIX timestamp (UTC) format. Unit: seconds.
        self.end_ts = end_ts
        # The ID of the API security event.
        self.event_id = event_id
        # The event level. Valid values:
        # - **high**: High-risk.
        # - **medium**: Medium-risk.
        # - **low**: Low-risk.
        self.event_level = event_level
        # The dimension of the security event.
        self.event_scope = event_scope
        # The event type.
        # > You can call [DescribeApisecRules](https://help.aliyun.com/document_detail/2859155.html) to obtain the supported event types.
        self.event_tag = event_tag
        # The ID of the WAF instance.
        # 
        # > You can call [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) to obtain the ID of the current WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The domain name or IP address to which the API operation belongs.
        self.matched_host = matched_host
        # The name of the field used for sorting. Valid values:
        # - **allCnt**: attack count.
        # - **startTs**: event start time.
        # - **endTs**: event end time.
        self.order_key = order_key
        # The sort order. Valid values:
        # - **desc**: Descending order (default).
        # - **asc**: Ascending order.
        self.order_way = order_way
        # The source of the event type. Valid values:
        # - **custom**: Custom.
        # - **default**: Built-in.
        self.origin = origin
        # The page number to return in a paged query. Default value: **1**, which indicates the first page.
        self.page_number = page_number
        # The number of entries per page in a paged query. Default value: **10**, which indicates 10 entries per page.
        self.page_size = page_size
        # The region where the WAF instance is deployed. Valid values:
        # 
        # - **cn-hangzhou**: the Chinese mainland.
        # 
        # - **ap-southeast-1**: outside the Chinese mainland.
        self.region_id = region_id
        # The Alibaba Cloud resource group ID.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        # The start time of the query, in UNIX timestamp (UTC) format. Unit: seconds.
        self.start_ts = start_ts
        # The event status. Valid values:
        # - **toBeConfirmed**: To be confirmed.
        # - **confirmed**: Confirmed.
        # - **actioned**: Handled.
        # - **ignored**: Ignored.
        self.user_status = user_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account is not None:
            result['Account'] = self.account

        if self.api_format is not None:
            result['ApiFormat'] = self.api_format

        if self.api_id is not None:
            result['ApiId'] = self.api_id

        if self.api_tag is not None:
            result['ApiTag'] = self.api_tag

        if self.attack_ip is not None:
            result['AttackIp'] = self.attack_ip

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.end_ts is not None:
            result['EndTs'] = self.end_ts

        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.event_level is not None:
            result['EventLevel'] = self.event_level

        if self.event_scope is not None:
            result['EventScope'] = self.event_scope

        if self.event_tag is not None:
            result['EventTag'] = self.event_tag

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

        if self.start_ts is not None:
            result['StartTs'] = self.start_ts

        if self.user_status is not None:
            result['UserStatus'] = self.user_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')

        if m.get('ApiFormat') is not None:
            self.api_format = m.get('ApiFormat')

        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')

        if m.get('ApiTag') is not None:
            self.api_tag = m.get('ApiTag')

        if m.get('AttackIp') is not None:
            self.attack_ip = m.get('AttackIp')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('EndTs') is not None:
            self.end_ts = m.get('EndTs')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('EventLevel') is not None:
            self.event_level = m.get('EventLevel')

        if m.get('EventScope') is not None:
            self.event_scope = m.get('EventScope')

        if m.get('EventTag') is not None:
            self.event_tag = m.get('EventTag')

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

        if m.get('StartTs') is not None:
            self.start_ts = m.get('StartTs')

        if m.get('UserStatus') is not None:
            self.user_status = m.get('UserStatus')

        return self

