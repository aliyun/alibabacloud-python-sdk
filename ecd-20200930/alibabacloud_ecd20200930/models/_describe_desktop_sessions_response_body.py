# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeDesktopSessionsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        sessions: List[main_models.DescribeDesktopSessionsResponseBodySessions] = None,
        total_count: int = None,
    ):
        # The request ID.
        self.request_id = request_id
        # Details of sessions.
        self.sessions = sessions
        # The total number of entries returned.
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
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.sessions = []
        if m.get('Sessions') is not None:
            for k1 in m.get('Sessions'):
                temp_model = main_models.DescribeDesktopSessionsResponseBodySessions()
                self.sessions.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDesktopSessionsResponseBodySessions(DaraModel):
    def __init__(
        self,
        account_type: str = None,
        client_ip: str = None,
        client_os: str = None,
        client_version: str = None,
        desktop_id: str = None,
        desktop_name: str = None,
        directory_type: str = None,
        end_user_apply_coordinate_time: int = None,
        end_user_id: str = None,
        latest_connection_time: int = None,
        office_site_id: str = None,
        office_site_name: str = None,
        os_session_status: str = None,
        os_type: str = None,
        protocol_type: str = None,
        resource_groups: List[main_models.DescribeDesktopSessionsResponseBodySessionsResourceGroups] = None,
        session_end_time: str = None,
        session_idle_time: int = None,
        session_start_time: str = None,
        session_status: str = None,
        sub_pay_type: str = None,
        terminal_info: main_models.DescribeDesktopSessionsResponseBodySessionsTerminalInfo = None,
        total_connection_time: int = None,
    ):
        self.account_type = account_type
        # The IP address of the client.
        self.client_ip = client_ip
        # The client OS.
        self.client_os = client_os
        # The client version.
        self.client_version = client_version
        # The ID of the cloud computer.
        self.desktop_id = desktop_id
        # The name of the cloud computer.
        self.desktop_name = desktop_name
        self.directory_type = directory_type
        # The duration of the remote assistance. Unit: seconds.
        self.end_user_apply_coordinate_time = end_user_apply_coordinate_time
        # The ID of the end user.
        self.end_user_id = end_user_id
        # The duration of the last connection to the cloud computer. Unit: seconds.
        self.latest_connection_time = latest_connection_time
        # The ID of the office network.
        self.office_site_id = office_site_id
        # The name of the office network.
        self.office_site_name = office_site_name
        # Indicates whether the switch to check session status of cloud computers is turned on.
        self.os_session_status = os_session_status
        # The OS.
        # 
        # Valid values:
        # 
        # *   Linux
        # *   Windows
        self.os_type = os_type
        # The protocol type.
        # 
        # Valid values:
        # 
        # *   HDX
        # *   ASP
        self.protocol_type = protocol_type
        self.resource_groups = resource_groups
        # The end time of the session.
        self.session_end_time = session_end_time
        # The idle duration of the session. Unit: seconds.
        self.session_idle_time = session_idle_time
        # The start time of the session.
        self.session_start_time = session_start_time
        # The state of the session.
        # 
        # Valid values:
        # 
        # *   Connected
        # *   Disconnected
        self.session_status = session_status
        # The billing method of cloud computers.
        # 
        # Valid values:
        # 
        # *   duration: hourly plan (available for users in the whitelist)
        # *   postPaid: pay-as-you-go
        # *   monthPackage: monthly subscription (120-hour computing plan and 250-hour computing plan)
        # *   prePaid: monthly subscription (Unlimited computing plan)
        self.sub_pay_type = sub_pay_type
        self.terminal_info = terminal_info
        # The total connection duration. Unit: seconds.
        self.total_connection_time = total_connection_time

    def validate(self):
        if self.resource_groups:
            for v1 in self.resource_groups:
                 if v1:
                    v1.validate()
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

        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name

        if self.directory_type is not None:
            result['DirectoryType'] = self.directory_type

        if self.end_user_apply_coordinate_time is not None:
            result['EndUserApplyCoordinateTime'] = self.end_user_apply_coordinate_time

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.latest_connection_time is not None:
            result['LatestConnectionTime'] = self.latest_connection_time

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.office_site_name is not None:
            result['OfficeSiteName'] = self.office_site_name

        if self.os_session_status is not None:
            result['OsSessionStatus'] = self.os_session_status

        if self.os_type is not None:
            result['OsType'] = self.os_type

        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type

        result['ResourceGroups'] = []
        if self.resource_groups is not None:
            for k1 in self.resource_groups:
                result['ResourceGroups'].append(k1.to_map() if k1 else None)

        if self.session_end_time is not None:
            result['SessionEndTime'] = self.session_end_time

        if self.session_idle_time is not None:
            result['SessionIdleTime'] = self.session_idle_time

        if self.session_start_time is not None:
            result['SessionStartTime'] = self.session_start_time

        if self.session_status is not None:
            result['SessionStatus'] = self.session_status

        if self.sub_pay_type is not None:
            result['SubPayType'] = self.sub_pay_type

        if self.terminal_info is not None:
            result['TerminalInfo'] = self.terminal_info.to_map()

        if self.total_connection_time is not None:
            result['TotalConnectionTime'] = self.total_connection_time

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

        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')

        if m.get('DirectoryType') is not None:
            self.directory_type = m.get('DirectoryType')

        if m.get('EndUserApplyCoordinateTime') is not None:
            self.end_user_apply_coordinate_time = m.get('EndUserApplyCoordinateTime')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('LatestConnectionTime') is not None:
            self.latest_connection_time = m.get('LatestConnectionTime')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('OfficeSiteName') is not None:
            self.office_site_name = m.get('OfficeSiteName')

        if m.get('OsSessionStatus') is not None:
            self.os_session_status = m.get('OsSessionStatus')

        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')

        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')

        self.resource_groups = []
        if m.get('ResourceGroups') is not None:
            for k1 in m.get('ResourceGroups'):
                temp_model = main_models.DescribeDesktopSessionsResponseBodySessionsResourceGroups()
                self.resource_groups.append(temp_model.from_map(k1))

        if m.get('SessionEndTime') is not None:
            self.session_end_time = m.get('SessionEndTime')

        if m.get('SessionIdleTime') is not None:
            self.session_idle_time = m.get('SessionIdleTime')

        if m.get('SessionStartTime') is not None:
            self.session_start_time = m.get('SessionStartTime')

        if m.get('SessionStatus') is not None:
            self.session_status = m.get('SessionStatus')

        if m.get('SubPayType') is not None:
            self.sub_pay_type = m.get('SubPayType')

        if m.get('TerminalInfo') is not None:
            temp_model = main_models.DescribeDesktopSessionsResponseBodySessionsTerminalInfo()
            self.terminal_info = temp_model.from_map(m.get('TerminalInfo'))

        if m.get('TotalConnectionTime') is not None:
            self.total_connection_time = m.get('TotalConnectionTime')

        return self

class DescribeDesktopSessionsResponseBodySessionsTerminalInfo(DaraModel):
    def __init__(
        self,
        model: str = None,
        product_name: str = None,
        serial_number: str = None,
        uuid: str = None,
    ):
        self.model = model
        self.product_name = product_name
        self.serial_number = serial_number
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

class DescribeDesktopSessionsResponseBodySessionsResourceGroups(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

