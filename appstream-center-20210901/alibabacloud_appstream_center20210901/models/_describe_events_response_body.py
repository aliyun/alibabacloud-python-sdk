# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class DescribeEventsResponseBody(DaraModel):
    def __init__(
        self,
        event_list: List[main_models.DescribeEventsResponseBodyEventList] = None,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of events on the current page, returned in descending order of the event log time.
        self.event_list = event_list
        # A compatibility field. The current version does not set this field. Do not rely on its value.
        self.max_results = max_results
        # A compatibility field. The current version does not generate a next page token. Do not use this field for pagination.
        self.next_token = next_token
        # The page number corresponding to the current response.
        self.page_number = page_number
        # The number of events per page used in the current response.
        self.page_size = page_size
        # The unique identifier of the request, which can be used to troubleshoot request issues.
        self.request_id = request_id
        # The total number of events that meet all filter conditions within the 30-day retrievable window. Unit: entries.
        self.total_count = total_count

    def validate(self):
        if self.event_list:
            for v1 in self.event_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EventList'] = []
        if self.event_list is not None:
            for k1 in self.event_list:
                result['EventList'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.event_list = []
        if m.get('EventList') is not None:
            for k1 in m.get('EventList'):
                temp_model = main_models.DescribeEventsResponseBodyEventList()
                self.event_list.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeEventsResponseBodyEventList(DaraModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        app_instance_group_name: str = None,
        detail_info: str = None,
        event_id: str = None,
        event_type: str = None,
        member_eni_ip: str = None,
        occurred_time: str = None,
        office_site_id: str = None,
        product_type: str = None,
        user_id: str = None,
    ):
        # The ID of the delivery group associated with the event. This field may be empty if the event is not associated with a delivery group.
        self.app_instance_group_id = app_instance_group_id
        # The name of the delivery group associated with the event. This field may be empty if the event is not associated with a delivery group.
        self.app_instance_group_name = app_instance_group_name
        # The event detail text. The content varies based on the `EventType` and may be empty. For example, a session release event may return a JSON text that describes the release cause.
        self.detail_info = detail_info
        # The unique identifier of the event.
        self.event_id = event_id
        # The event type identifier. Different products may return different values. You can use this value for subsequent exact filtering.
        self.event_type = event_type
        # The private IP address of the member ENI of the cloud resource associated with the event. This field may be empty if it is not applicable.
        self.member_eni_ip = member_eni_ip
        # The time when the event occurred. Format: `yyyy-MM-dd HH:mm:ss`. Time zone: UTC+8 (Asia/Shanghai).
        self.occurred_time = occurred_time
        # The ID of the office network associated with the event. This field may be empty if it is not applicable.
        self.office_site_id = office_site_id
        # The product type to which the event belongs. This field is an open string and may be extended as supported event sources expand. Callers should not restrict the value to the products currently listed in the `ProductType` request parameter.
        self.product_type = product_type
        # The ID of the end user who generated the event. This field may be empty if the event is not associated with an end user.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id

        if self.app_instance_group_name is not None:
            result['AppInstanceGroupName'] = self.app_instance_group_name

        if self.detail_info is not None:
            result['DetailInfo'] = self.detail_info

        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.event_type is not None:
            result['EventType'] = self.event_type

        if self.member_eni_ip is not None:
            result['MemberEniIp'] = self.member_eni_ip

        if self.occurred_time is not None:
            result['OccurredTime'] = self.occurred_time

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')

        if m.get('AppInstanceGroupName') is not None:
            self.app_instance_group_name = m.get('AppInstanceGroupName')

        if m.get('DetailInfo') is not None:
            self.detail_info = m.get('DetailInfo')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        if m.get('MemberEniIp') is not None:
            self.member_eni_ip = m.get('MemberEniIp')

        if m.get('OccurredTime') is not None:
            self.occurred_time = m.get('OccurredTime')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

