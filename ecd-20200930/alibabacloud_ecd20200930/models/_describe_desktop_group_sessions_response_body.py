# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeDesktopGroupSessionsResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        sessions: List[main_models.DescribeDesktopGroupSessionsResponseBodySessions] = None,
        total_count: int = None,
    ):
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The sessions.
        self.sessions = sessions
        # The total number of sessions.
        self.total_count = total_count

    def validate(self):
        if self.sessions:
            for v1 in self.sessions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Sessions'] = []
        if self.sessions is not None:
            for k1 in self.sessions:
                result['Sessions'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.sessions = []
        if m.get('Sessions') is not None:
            for k1 in m.get('Sessions'):
                temp_model = main_models.DescribeDesktopGroupSessionsResponseBodySessions()
                self.sessions.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDesktopGroupSessionsResponseBodySessions(DaraModel):
    def __init__(
        self,
        account_type: str = None,
        client_ip: str = None,
        client_os: str = None,
        client_version: str = None,
        desktop_group_id: str = None,
        desktop_group_name: str = None,
        desktop_id: str = None,
        directory_type: str = None,
        end_user_apply_coordinate_time: int = None,
        end_user_id: str = None,
        last_session_end_time: str = None,
        last_session_start_time: str = None,
        latest_connection_time: int = None,
        office_site_id: str = None,
        office_site_name: str = None,
        os_type: str = None,
        own_type: int = None,
        protocol_type: str = None,
        session_idle_time: int = None,
        session_status: str = None,
        terminal_info: main_models.DescribeDesktopGroupSessionsResponseBodySessionsTerminalInfo = None,
        total_connection_duration: int = None,
    ):
        # 账号类型
        self.account_type = account_type
        # The IP address of the client.
        self.client_ip = client_ip
        # The operating system of the client.
        self.client_os = client_os
        # The version of the client.
        self.client_version = client_version
        # The ID of the shared cloud computer.
        self.desktop_group_id = desktop_group_id
        # The name of the cloud computer share.
        self.desktop_group_name = desktop_group_name
        # If the session status is Connected, it indicates the ID of the cloud computer that is currently connected. If the session status is Disconnected, it indicates the ID of the cloud computer that was last connected.
        self.desktop_id = desktop_id
        # 办公网络类型
        self.directory_type = directory_type
        # The point in time when the end user applies for administrator assistance.
        self.end_user_apply_coordinate_time = end_user_apply_coordinate_time
        # The user ID of the terminal that connects to the session.
        self.end_user_id = end_user_id
        # The end time of the most recent connection.
        self.last_session_end_time = last_session_end_time
        # The start time of the most recent connection.
        self.last_session_start_time = last_session_start_time
        # The duration of the most recent session. Unit: seconds.
        self.latest_connection_time = latest_connection_time
        # The office network ID.
        self.office_site_id = office_site_id
        # The office network name.
        self.office_site_name = office_site_name
        # The operating system type of the cloud computer.
        # 
        # Valid values:
        # 
        # *   linux.
        # *   Windows.
        self.os_type = os_type
        # The type of the session.
        # 
        # Valid values:
        # 
        # *   0: single-session
        # *   1: multi-session
        self.own_type = own_type
        # The protocol type supported by the rule.
        # 
        # Valid value:
        # 
        # *   High-definition Experience (HDX).
        # *   ASP.
        self.protocol_type = protocol_type
        # The idle duration of the cloud computer. Unit: seconds.
        self.session_idle_time = session_idle_time
        # The state of the session.
        # 
        # Valid values:
        # 
        # *   Connected
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Disconnected
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.session_status = session_status
        # Terminal Info
        self.terminal_info = terminal_info
        # The total duration of the sessions. Unit: seconds.
        self.total_connection_duration = total_connection_duration

    def validate(self):
        if self.terminal_info:
            self.terminal_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_type is not None:
            result['AccountType'] = self.account_type

        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip

        if self.client_os is not None:
            result['ClientOS'] = self.client_os

        if self.client_version is not None:
            result['ClientVersion'] = self.client_version

        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id

        if self.desktop_group_name is not None:
            result['DesktopGroupName'] = self.desktop_group_name

        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.directory_type is not None:
            result['DirectoryType'] = self.directory_type

        if self.end_user_apply_coordinate_time is not None:
            result['EndUserApplyCoordinateTime'] = self.end_user_apply_coordinate_time

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.last_session_end_time is not None:
            result['LastSessionEndTime'] = self.last_session_end_time

        if self.last_session_start_time is not None:
            result['LastSessionStartTime'] = self.last_session_start_time

        if self.latest_connection_time is not None:
            result['LatestConnectionTime'] = self.latest_connection_time

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.office_site_name is not None:
            result['OfficeSiteName'] = self.office_site_name

        if self.os_type is not None:
            result['OsType'] = self.os_type

        if self.own_type is not None:
            result['OwnType'] = self.own_type

        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type

        if self.session_idle_time is not None:
            result['SessionIdleTime'] = self.session_idle_time

        if self.session_status is not None:
            result['SessionStatus'] = self.session_status

        if self.terminal_info is not None:
            result['TerminalInfo'] = self.terminal_info.to_map()

        if self.total_connection_duration is not None:
            result['TotalConnectionDuration'] = self.total_connection_duration

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')

        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')

        if m.get('ClientOS') is not None:
            self.client_os = m.get('ClientOS')

        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')

        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')

        if m.get('DesktopGroupName') is not None:
            self.desktop_group_name = m.get('DesktopGroupName')

        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('DirectoryType') is not None:
            self.directory_type = m.get('DirectoryType')

        if m.get('EndUserApplyCoordinateTime') is not None:
            self.end_user_apply_coordinate_time = m.get('EndUserApplyCoordinateTime')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('LastSessionEndTime') is not None:
            self.last_session_end_time = m.get('LastSessionEndTime')

        if m.get('LastSessionStartTime') is not None:
            self.last_session_start_time = m.get('LastSessionStartTime')

        if m.get('LatestConnectionTime') is not None:
            self.latest_connection_time = m.get('LatestConnectionTime')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('OfficeSiteName') is not None:
            self.office_site_name = m.get('OfficeSiteName')

        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')

        if m.get('OwnType') is not None:
            self.own_type = m.get('OwnType')

        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')

        if m.get('SessionIdleTime') is not None:
            self.session_idle_time = m.get('SessionIdleTime')

        if m.get('SessionStatus') is not None:
            self.session_status = m.get('SessionStatus')

        if m.get('TerminalInfo') is not None:
            temp_model = main_models.DescribeDesktopGroupSessionsResponseBodySessionsTerminalInfo()
            self.terminal_info = temp_model.from_map(m.get('TerminalInfo'))

        if m.get('TotalConnectionDuration') is not None:
            self.total_connection_duration = m.get('TotalConnectionDuration')

        return self

class DescribeDesktopGroupSessionsResponseBodySessionsTerminalInfo(DaraModel):
    def __init__(
        self,
        model: str = None,
        product_name: str = None,
        serial_number: str = None,
        uuid: str = None,
    ):
        # The type of the terminal.
        self.model = model
        # The terminal type.
        self.product_name = product_name
        # Terminal Serial Number
        self.serial_number = serial_number
        # The terminal UUID.
        self.uuid = uuid

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

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')

        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

