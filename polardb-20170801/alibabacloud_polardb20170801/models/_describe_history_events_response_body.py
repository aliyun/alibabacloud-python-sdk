# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeHistoryEventsResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeHistoryEventsResponseBodyItems] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of events.
        self.items = items
        # The page number of the returned page. The default value is 1.
        self.page_number = page_number
        # The number of entries returned per page. Valid values:
        # 
        # - **30**
        # 
        # - **50**
        # 
        # - **100**
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries in the list.
        self.total_count = total_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

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
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeHistoryEventsResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeHistoryEventsResponseBodyItems(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeHistoryEventsResponseBodyItemsData = None,
        id: str = None,
        region: str = None,
        source: str = None,
        specversion: str = None,
        subject: str = None,
        time: str = None,
        type: str = None,
    ):
        # The data overview.
        self.data = data
        # The task ID.
        self.id = id
        # The ID of the region where the task is located.
        self.region = region
        # The event source.
        self.source = source
        # The database version.
        self.specversion = specversion
        # The name of the pending event.
        self.subject = subject
        # The runtime of the query task. Unit: seconds (s).
        self.time = time
        # The event type.
        self.type = type

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.id is not None:
            result['Id'] = self.id

        if self.region is not None:
            result['Region'] = self.region

        if self.source is not None:
            result['Source'] = self.source

        if self.specversion is not None:
            result['Specversion'] = self.specversion

        if self.subject is not None:
            result['Subject'] = self.subject

        if self.time is not None:
            result['Time'] = self.time

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeHistoryEventsResponseBodyItemsData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Specversion') is not None:
            self.specversion = m.get('Specversion')

        if m.get('Subject') is not None:
            self.subject = m.get('Subject')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeHistoryEventsResponseBodyItemsData(DaraModel):
    def __init__(
        self,
        cms_product: str = None,
        db_type: str = None,
        detail_impact: str = None,
        detail_reason: str = None,
        end_time: str = None,
        event_category: str = None,
        event_code: str = None,
        event_detail: str = None,
        event_id: str = None,
        event_impact: str = None,
        event_level: str = None,
        event_reason: str = None,
        event_status: str = None,
        event_type: str = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        handle_status: str = None,
        has_life_cycle: int = None,
        instance_id: str = None,
        instance_name: str = None,
        is_closed: int = None,
        product: str = None,
        region_id: str = None,
        resource_type: str = None,
        source_type: str = None,
        start_time: str = None,
        uid: str = None,
    ):
        # The type of the Alibaba Cloud service for the application group. Valid values:
        # 
        # - **web**: web application.
        # 
        # - **native**: native application.
        self.cms_product = cms_product
        # The database type.
        self.db_type = db_type
        # This parameter is used for pagination.
        self.detail_impact = detail_impact
        # The details of the instance operation.
        self.detail_reason = detail_reason
        # The end of the query time range. The end time must be later than the start time. The interval between the start time and the end time must be within 24 hours. The time is in the `YYYY-MM-DDThh:mmZ` format and is displayed in UTC.
        self.end_time = end_time
        # The category of the system event. Valid values:
        # 
        # - **Exception**: anomalous activity
        # 
        # - **Optimize**: optimization events
        # 
        # - **Notification**: notification events
        # 
        # - **Maintenance**: scheduled O\\&M events
        self.event_category = event_category
        # The event code.
        self.event_code = event_code
        # The event details.
        self.event_detail = event_detail
        # The event ID.
        self.event_id = event_id
        # An overview of the event\\"s impact.
        self.event_impact = event_impact
        # The event level. Valid values:
        # 
        # - **INFO**: notification
        # 
        # - **WARN**: warning
        # 
        # - **CRITICAL**: urgent
        self.event_level = event_level
        # The source of the event operation.
        self.event_reason = event_reason
        # The event status. Valid values:
        # 
        # - **Inquiring**: The event is being inquired.
        # 
        # - **Scheduled**: The event is scheduled.
        # 
        # - **Running**: The event is in progress.
        # 
        # - **Succeed**: The event is successful.
        # 
        # - **Failed**: The event failed.
        # 
        # - **Canceled**: The event is canceled.
        self.event_status = event_status
        # The type of the system event. Valid values:
        # 
        # - **SystemMaintenance.Reboot**: The instance is restarted due to system maintenance.
        # 
        # - **SystemMaintenance.Redeploy**: The instance is redeployed due to system maintenance.
        # 
        # - **SystemFailure.Reboot**: The instance is restarted due to a system fault.
        # 
        # - **SystemFailure.Redeploy**: The instance is redeployed due to a system fault.
        # 
        # - **SystemFailure.Delete**: The instance is released because it failed to be created.
        # 
        # - **InstanceFailure.Reboot**: The instance is restarted due to an instance fault.
        # 
        # - **InstanceExpiration.Stop**: The subscription instance is stopped because its subscription expires.
        # 
        # - **InstanceExpiration.Delete**: The subscription instance is released because its subscription expires.
        # 
        # - **AccountUnbalanced.Stop**: The pay-as-you-go instance is stopped due to an overdue payment.
        # 
        # - **AccountUnbalanced.Delete**: The pay-as-you-go instance is released due to an overdue payment.
        self.event_type = event_type
        # The creation time.
        self.gmt_created = gmt_created
        # The update time.
        self.gmt_modified = gmt_modified
        # The processing status.
        self.handle_status = handle_status
        # Indicates whether a lifecycle exists.
        self.has_life_cycle = has_life_cycle
        # The instance ID.
        self.instance_id = instance_id
        # The instance name.
        self.instance_name = instance_name
        # Indicates whether the event is successfully closed. Valid values:
        # 
        # - **0**: closed
        # 
        # - **1**: open
        self.is_closed = is_closed
        # The product name.
        self.product = product
        # The region ID.
        self.region_id = region_id
        # The resource type. Valid values:
        # 
        # - **Instance**: instance resource
        # 
        # - **Host**: host resource
        # 
        # - **User**: user resource
        self.resource_type = resource_type
        # The type of the source data.
        self.source_type = source_type
        # The start of the query time range. The time is in the `yyyy-MM-ddTHH:mm:ssZ` format and is displayed in UTC.
        self.start_time = start_time
        # The ID of the user to whom the resource belongs.
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cms_product is not None:
            result['CmsProduct'] = self.cms_product

        if self.db_type is not None:
            result['DbType'] = self.db_type

        if self.detail_impact is not None:
            result['DetailImpact'] = self.detail_impact

        if self.detail_reason is not None:
            result['DetailReason'] = self.detail_reason

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.event_category is not None:
            result['EventCategory'] = self.event_category

        if self.event_code is not None:
            result['EventCode'] = self.event_code

        if self.event_detail is not None:
            result['EventDetail'] = self.event_detail

        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.event_impact is not None:
            result['EventImpact'] = self.event_impact

        if self.event_level is not None:
            result['EventLevel'] = self.event_level

        if self.event_reason is not None:
            result['EventReason'] = self.event_reason

        if self.event_status is not None:
            result['EventStatus'] = self.event_status

        if self.event_type is not None:
            result['EventType'] = self.event_type

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.handle_status is not None:
            result['HandleStatus'] = self.handle_status

        if self.has_life_cycle is not None:
            result['HasLifeCycle'] = self.has_life_cycle

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.is_closed is not None:
            result['IsClosed'] = self.is_closed

        if self.product is not None:
            result['Product'] = self.product

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.uid is not None:
            result['Uid'] = self.uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CmsProduct') is not None:
            self.cms_product = m.get('CmsProduct')

        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

        if m.get('DetailImpact') is not None:
            self.detail_impact = m.get('DetailImpact')

        if m.get('DetailReason') is not None:
            self.detail_reason = m.get('DetailReason')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EventCategory') is not None:
            self.event_category = m.get('EventCategory')

        if m.get('EventCode') is not None:
            self.event_code = m.get('EventCode')

        if m.get('EventDetail') is not None:
            self.event_detail = m.get('EventDetail')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('EventImpact') is not None:
            self.event_impact = m.get('EventImpact')

        if m.get('EventLevel') is not None:
            self.event_level = m.get('EventLevel')

        if m.get('EventReason') is not None:
            self.event_reason = m.get('EventReason')

        if m.get('EventStatus') is not None:
            self.event_status = m.get('EventStatus')

        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('HandleStatus') is not None:
            self.handle_status = m.get('HandleStatus')

        if m.get('HasLifeCycle') is not None:
            self.has_life_cycle = m.get('HasLifeCycle')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('IsClosed') is not None:
            self.is_closed = m.get('IsClosed')

        if m.get('Product') is not None:
            self.product = m.get('Product')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        return self

