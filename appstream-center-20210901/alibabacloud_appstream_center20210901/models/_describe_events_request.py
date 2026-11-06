# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeEventsRequest(DaraModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        app_instance_group_name: str = None,
        app_instance_id: str = None,
        biz_region_id: str = None,
        end_time: str = None,
        event_id: str = None,
        event_type: str = None,
        max_results: int = None,
        member_eni_ip: str = None,
        next_token: str = None,
        office_site_id: str = None,
        page_number: int = None,
        page_size: int = None,
        product_type: str = None,
        start_time: str = None,
        user_id: str = None,
    ):
        # The delivery group ID, used to filter events of a specific delivery group. If you do not specify this parameter, events are not filtered by delivery group. You can call the [ListAppInstanceGroup](~~ListAppInstanceGroup~~) operation to obtain the ID.
        self.app_instance_group_id = app_instance_group_id
        # The delivery group name. If the name contains only letters, digits, underscores, or hyphens, events are filtered by name prefix. If the name contains spaces or other special characters, events are filtered by the exact name. If you do not specify this parameter, events are not filtered by name.
        self.app_instance_group_name = app_instance_group_name
        # The application instance ID, used to filter events associated with a specific instance. If you do not specify this parameter, events are not filtered by application instance. To obtain this value, first call the [ListAppInstanceGroup](~~ListAppInstanceGroup~~) operation to obtain the delivery group ID, and then use the ID as `AppInstanceGroupId` to call the [ListAppInstances](~~ListAppInstances~~) operation.
        self.app_instance_id = app_instance_id
        # The business region ID of the event, used for exact filtering. If you do not specify this parameter, events are not filtered by business region. You can call the [ListRegions](~~ListRegions~~) operation to obtain the ID.
        self.biz_region_id = biz_region_id
        # The end time of the query. **Required**. The format is the same as that of `StartTime`. We recommend that you always include the time zone offset. The query includes this time, and the end time cannot be earlier than the `StartTime`. A time range later than the call time does not generate future events.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The event ID, used to query a specific event. If you do not specify this parameter, events are not filtered by event ID.
        self.event_id = event_id
        # The event type identifier, used to filter events. Different products may generate different event types. This operation does not restrict the value to a fixed enumeration. You should use the EventType values retrieved from EventList as filter values.
        self.event_type = event_type
        # A compatibility field. The current version does not read this parameter. Use `PageSize` to control the number of records on each page.
        self.max_results = max_results
        # The private IP address of the member elastic network interface (ENI) of the cloud resource, used to filter related events. If you do not specify this parameter, events are not filtered by IP address.
        self.member_eni_ip = member_eni_ip
        # A compatibility field. The current version does not read this parameter and does not support token-based pagination. Use `PageNumber`.
        self.next_token = next_token
        # The office network ID, used to filter events generated within a specific office network. If you do not specify this parameter, events are not filtered by office network.
        self.office_site_id = office_site_id
        # The page number to query. Pages start from 1. Default value: 1. This parameter is used together with `PageSize`.
        self.page_number = page_number
        # The number of events to return on each page. Default value: 10. This operation does not declare a fixed upper limit. We recommend that you set this parameter to a reasonable positive integer based on your actual needs.
        self.page_size = page_size
        # The product type. The value is case-insensitive. If you specify an invalid value, the request fails. If you do not specify this parameter, events are not filtered by product type. Only the following public product values are supported:
        # 
        # - `CloudApp`: Wuying Cloud Application.
        # - `CloudBrowser`: Cloud Browser.
        # - `WuyingServer`: Enterprise Edition Workstation.
        # - `WuyingWorkstation`: Personal Edition Linggou Container Workstation.
        # - `WuyingWorkstationTeam`: Linggou Team Edition Container Workstation.
        # - `WuyingWorkstationBusiness`: Linggou Dedicated Edition Container Workstation.
        # - `AndroidCloud`: Cloud Phone.
        # - `AIAgent`: AgentBay (AI agent).
        self.product_type = product_type
        # The start time of the query. **Required**. Use the ISO 8601 format: `yyyy-MM-dd\\"T\\"HH:mm:ss`. You can include three-digit milliseconds and use `Z` or `±HH:mm` to specify the time zone. We recommend that you always include the time zone offset. The query includes this time, and the start time must be earlier than or equal to the `EndTime`. The service only retains and retrieves events that occurred within 30 days before the call time.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The end user ID, used to filter events generated by a specific user. If you do not specify this parameter, events are not filtered by user.
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

        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id

        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.event_type is not None:
            result['EventType'] = self.event_type

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.member_eni_ip is not None:
            result['MemberEniIp'] = self.member_eni_ip

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')

        if m.get('AppInstanceGroupName') is not None:
            self.app_instance_group_name = m.get('AppInstanceGroupName')

        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')

        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('MemberEniIp') is not None:
            self.member_eni_ip = m.get('MemberEniIp')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

