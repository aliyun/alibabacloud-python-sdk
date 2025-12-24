# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeGlobalDesktopRecordsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        sessions: List[main_models.DescribeGlobalDesktopRecordsResponseBodySessions] = None,
        total_count: int = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The session details.
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
                temp_model = main_models.DescribeGlobalDesktopRecordsResponseBodySessions()
                self.sessions.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeGlobalDesktopRecordsResponseBodySessions(DaraModel):
    def __init__(
        self,
        connection_status: str = None,
        cpu: int = None,
        desktop_group_id: str = None,
        desktop_group_name: str = None,
        desktop_id: str = None,
        desktop_name: str = None,
        desktop_status: str = None,
        end_user_id: str = None,
        end_user_ids: List[str] = None,
        gpu_spec: str = None,
        latest_connection_time: int = None,
        memory: int = None,
        office_site_id: str = None,
        office_site_name: str = None,
        office_site_type: str = None,
        os_type: str = None,
        platform: str = None,
        protocol_type: str = None,
        region_id: str = None,
        resource_groups: List[main_models.DescribeGlobalDesktopRecordsResponseBodySessionsResourceGroups] = None,
        session_idle_time: int = None,
        sessions: List[main_models.DescribeGlobalDesktopRecordsResponseBodySessionsSessions] = None,
        status_change_time: int = None,
        sub_pay_type: str = None,
        total_connection_time: int = None,
        up_time: int = None,
    ):
        # The connection status of the cloud desktop.
        self.connection_status = connection_status
        # The number of vCPUs.
        self.cpu = cpu
        # The ID of the cloud computer share.
        self.desktop_group_id = desktop_group_id
        # The name of the cloud computer share.
        self.desktop_group_name = desktop_group_name
        # The cloud computer IDs.
        self.desktop_id = desktop_id
        # The cloud computer name.
        self.desktop_name = desktop_name
        # 桌面状态
        self.desktop_status = desktop_status
        # The end user ID.
        self.end_user_id = end_user_id
        # The list of assigned terminal user IDs.
        self.end_user_ids = end_user_ids
        # The size of the GPU memory.
        self.gpu_spec = gpu_spec
        # The duration of the last connection to the cloud computer. Unit: seconds
        self.latest_connection_time = latest_connection_time
        # The memory of the cloud computer. Unit: MiB.
        self.memory = memory
        # The office network ID.
        self.office_site_id = office_site_id
        # The office network name.
        self.office_site_name = office_site_name
        self.office_site_type = office_site_type
        # The OS type. Valid values:
        # 
        # *   Windows
        # *   Linux
        self.os_type = os_type
        # The specific model of the operating system.
        self.platform = platform
        # Protocol type.
        # 
        # *   HDX
        # *   ASP
        self.protocol_type = protocol_type
        # The ID of the region where the instance resides.
        self.region_id = region_id
        # The name of the enterprise resource group.
        self.resource_groups = resource_groups
        # The idle duration of the session. Unit: minutes.
        self.session_idle_time = session_idle_time
        # The session details.
        self.sessions = sessions
        # The time when the status of the cloud computer was changed.
        self.status_change_time = status_change_time
        # The billing method of the cloud computer. Valid values:
        # 
        # *   prePaid: The monthly purchase is unlimited.
        # *   postPaid: pay-as-you-go
        # *   monthPackage: monthly duration.
        self.sub_pay_type = sub_pay_type
        # The total connection duration. Unit: seconds
        self.total_connection_time = total_connection_time
        # The startup duration of the cloud computer. Unit: seconds
        self.up_time = up_time

    def validate(self):
        if self.resource_groups:
            for v1 in self.resource_groups:
                 if v1:
                    v1.validate()
        if self.sessions:
            for v1 in self.sessions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_status is not None:
            result['ConnectionStatus'] = self.connection_status

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id

        if self.desktop_group_name is not None:
            result['DesktopGroupName'] = self.desktop_group_name

        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name

        if self.desktop_status is not None:
            result['DesktopStatus'] = self.desktop_status

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.end_user_ids is not None:
            result['EndUserIds'] = self.end_user_ids

        if self.gpu_spec is not None:
            result['GpuSpec'] = self.gpu_spec

        if self.latest_connection_time is not None:
            result['LatestConnectionTime'] = self.latest_connection_time

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.office_site_name is not None:
            result['OfficeSiteName'] = self.office_site_name

        if self.office_site_type is not None:
            result['OfficeSiteType'] = self.office_site_type

        if self.os_type is not None:
            result['OsType'] = self.os_type

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        result['ResourceGroups'] = []
        if self.resource_groups is not None:
            for k1 in self.resource_groups:
                result['ResourceGroups'].append(k1.to_map() if k1 else None)

        if self.session_idle_time is not None:
            result['SessionIdleTime'] = self.session_idle_time

        result['Sessions'] = []
        if self.sessions is not None:
            for k1 in self.sessions:
                result['Sessions'].append(k1.to_map() if k1 else None)

        if self.status_change_time is not None:
            result['StatusChangeTime'] = self.status_change_time

        if self.sub_pay_type is not None:
            result['SubPayType'] = self.sub_pay_type

        if self.total_connection_time is not None:
            result['TotalConnectionTime'] = self.total_connection_time

        if self.up_time is not None:
            result['UpTime'] = self.up_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionStatus') is not None:
            self.connection_status = m.get('ConnectionStatus')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')

        if m.get('DesktopGroupName') is not None:
            self.desktop_group_name = m.get('DesktopGroupName')

        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')

        if m.get('DesktopStatus') is not None:
            self.desktop_status = m.get('DesktopStatus')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('EndUserIds') is not None:
            self.end_user_ids = m.get('EndUserIds')

        if m.get('GpuSpec') is not None:
            self.gpu_spec = m.get('GpuSpec')

        if m.get('LatestConnectionTime') is not None:
            self.latest_connection_time = m.get('LatestConnectionTime')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('OfficeSiteName') is not None:
            self.office_site_name = m.get('OfficeSiteName')

        if m.get('OfficeSiteType') is not None:
            self.office_site_type = m.get('OfficeSiteType')

        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        self.resource_groups = []
        if m.get('ResourceGroups') is not None:
            for k1 in m.get('ResourceGroups'):
                temp_model = main_models.DescribeGlobalDesktopRecordsResponseBodySessionsResourceGroups()
                self.resource_groups.append(temp_model.from_map(k1))

        if m.get('SessionIdleTime') is not None:
            self.session_idle_time = m.get('SessionIdleTime')

        self.sessions = []
        if m.get('Sessions') is not None:
            for k1 in m.get('Sessions'):
                temp_model = main_models.DescribeGlobalDesktopRecordsResponseBodySessionsSessions()
                self.sessions.append(temp_model.from_map(k1))

        if m.get('StatusChangeTime') is not None:
            self.status_change_time = m.get('StatusChangeTime')

        if m.get('SubPayType') is not None:
            self.sub_pay_type = m.get('SubPayType')

        if m.get('TotalConnectionTime') is not None:
            self.total_connection_time = m.get('TotalConnectionTime')

        if m.get('UpTime') is not None:
            self.up_time = m.get('UpTime')

        return self

class DescribeGlobalDesktopRecordsResponseBodySessionsSessions(DaraModel):
    def __init__(
        self,
        end_user_id: str = None,
        establishment_time: str = None,
    ):
        # The end user ID.
        self.end_user_id = end_user_id
        # The time when the session was created.
        self.establishment_time = establishment_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.establishment_time is not None:
            result['EstablishmentTime'] = self.establishment_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('EstablishmentTime') is not None:
            self.establishment_time = m.get('EstablishmentTime')

        return self

class DescribeGlobalDesktopRecordsResponseBodySessionsResourceGroups(DaraModel):
    def __init__(
        self,
        resource_group_id: str = None,
        resource_group_name: str = None,
    ):
        # The ID of the enterprise resource group.
        self.resource_group_id = resource_group_id
        # The queried resource group name.
        self.resource_group_name = resource_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')

        return self

