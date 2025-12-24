# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeClientEventsResponseBody(DaraModel):
    def __init__(
        self,
        events: List[main_models.DescribeClientEventsResponseBodyEvents] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The user events.
        self.events = events
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.events:
            for v1 in self.events:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Events'] = []
        if self.events is not None:
            for k1 in self.events:
                result['Events'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.events = []
        if m.get('Events') is not None:
            for k1 in m.get('Events'):
                temp_model = main_models.DescribeClientEventsResponseBodyEvents()
                self.events.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeClientEventsResponseBodyEvents(DaraModel):
    def __init__(
        self,
        ali_uid: str = None,
        bytes_received: str = None,
        bytes_send: str = None,
        client_ip: str = None,
        client_os: str = None,
        client_version: str = None,
        description: str = None,
        desktop_group_id: str = None,
        desktop_group_name: str = None,
        desktop_id: str = None,
        desktop_ip: str = None,
        desktop_name: str = None,
        directory_id: str = None,
        directory_type: str = None,
        end_user_id: str = None,
        event_id: str = None,
        event_time: str = None,
        event_type: str = None,
        office_site_id: str = None,
        office_site_name: str = None,
        office_site_type: str = None,
        region_id: str = None,
        status: str = None,
        terminal_info: main_models.DescribeClientEventsResponseBodyEventsTerminalInfo = None,
    ):
        # The ID of the Alibaba Cloud account with which the event is associated.
        self.ali_uid = ali_uid
        # The number of bytes that are received.
        self.bytes_received = bytes_received
        # The number of bytes that are sent.
        self.bytes_send = bytes_send
        # The IP address of the client.
        self.client_ip = client_ip
        # The OS that the client runs.
        self.client_os = client_os
        # The client version.
        self.client_version = client_version
        # The description.
        self.description = description
        # The desktop group ID.
        self.desktop_group_id = desktop_group_id
        # The desktop group name.
        self.desktop_group_name = desktop_group_name
        # The cloud desktop ID.
        self.desktop_id = desktop_id
        # The IP address of the cloud desktop.
        self.desktop_ip = desktop_ip
        # The cloud desktop name.
        self.desktop_name = desktop_name
        # The ID of the directory to which the cloud desktop belongs.
        self.directory_id = directory_id
        # The directory type.
        self.directory_type = directory_type
        # The information about the end user that connects to the cloud desktop from the EDS client. The information can be a RAM user ID or an AD username.
        self.end_user_id = end_user_id
        # The event ID.
        self.event_id = event_id
        # The time when the event occurred.
        self.event_time = event_time
        # The event type. Valid values:
        self.event_type = event_type
        # The ID of the workspace to which the cloud desktop belongs.
        self.office_site_id = office_site_id
        # The workspace name.
        self.office_site_name = office_site_name
        # The account type of the workspace.
        # 
        # Valid values:
        # 
        # *   SIMPLE: convenience account
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   AD_CONNECTOR: enterprise AD account
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.office_site_type = office_site_type
        # The region ID.
        self.region_id = region_id
        # The status of the event. If you set the EventType parameter to `DESKTOP_DISCONNECT` or `GET_CONNECTION_TICKET`, this parameter is returned. Valid values:
        # 
        # *   200\\. The value indicates that the request is successful.
        # *   An error message. The value indicates that the request failed. Example: FailedToGetConnectionTicket.
        self.status = status
        self.terminal_info = terminal_info

    def validate(self):
        if self.terminal_info:
            self.terminal_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.bytes_received is not None:
            result['BytesReceived'] = self.bytes_received

        if self.bytes_send is not None:
            result['BytesSend'] = self.bytes_send

        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip

        if self.client_os is not None:
            result['ClientOS'] = self.client_os

        if self.client_version is not None:
            result['ClientVersion'] = self.client_version

        if self.description is not None:
            result['Description'] = self.description

        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id

        if self.desktop_group_name is not None:
            result['DesktopGroupName'] = self.desktop_group_name

        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.desktop_ip is not None:
            result['DesktopIp'] = self.desktop_ip

        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name

        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.directory_type is not None:
            result['DirectoryType'] = self.directory_type

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.event_time is not None:
            result['EventTime'] = self.event_time

        if self.event_type is not None:
            result['EventType'] = self.event_type

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.office_site_name is not None:
            result['OfficeSiteName'] = self.office_site_name

        if self.office_site_type is not None:
            result['OfficeSiteType'] = self.office_site_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        if self.terminal_info is not None:
            result['TerminalInfo'] = self.terminal_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('BytesReceived') is not None:
            self.bytes_received = m.get('BytesReceived')

        if m.get('BytesSend') is not None:
            self.bytes_send = m.get('BytesSend')

        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')

        if m.get('ClientOS') is not None:
            self.client_os = m.get('ClientOS')

        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')

        if m.get('DesktopGroupName') is not None:
            self.desktop_group_name = m.get('DesktopGroupName')

        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('DesktopIp') is not None:
            self.desktop_ip = m.get('DesktopIp')

        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')

        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('DirectoryType') is not None:
            self.directory_type = m.get('DirectoryType')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')

        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('OfficeSiteName') is not None:
            self.office_site_name = m.get('OfficeSiteName')

        if m.get('OfficeSiteType') is not None:
            self.office_site_type = m.get('OfficeSiteType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TerminalInfo') is not None:
            temp_model = main_models.DescribeClientEventsResponseBodyEventsTerminalInfo()
            self.terminal_info = temp_model.from_map(m.get('TerminalInfo'))

        return self

class DescribeClientEventsResponseBodyEventsTerminalInfo(DaraModel):
    def __init__(
        self,
        model: str = None,
        product_name: str = None,
        serial_number: str = None,
    ):
        self.model = model
        self.product_name = product_name
        self.serial_number = serial_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model is not None:
            result['Model'] = self.model

        if self.product_name is not None:
            result['ProductName'] = self.product_name

        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')

        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')

        return self

