# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class DescribeDevicesResponseBody(DaraModel):
    def __init__(
        self,
        devices: List[main_models.DescribeDevicesResponseBodyDevices] = None,
        page_count: int = None,
        page_num: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.devices = devices
        self.page_count = page_count
        self.page_num = page_num
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.devices:
            for v1 in self.devices:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Devices'] = []
        if self.devices is not None:
            for k1 in self.devices:
                result['Devices'].append(k1.to_map() if k1 else None)

        if self.page_count is not None:
            result['PageCount'] = self.page_count

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.devices = []
        if m.get('Devices') is not None:
            for k1 in m.get('Devices'):
                temp_model = main_models.DescribeDevicesResponseBodyDevices()
                self.devices.append(temp_model.from_map(k1))

        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDevicesResponseBodyDevices(DaraModel):
    def __init__(
        self,
        alarm_method: str = None,
        auto_directory: bool = None,
        auto_pos: bool = None,
        auto_start: bool = None,
        channel_sync_time: str = None,
        created_time: str = None,
        description: str = None,
        directory: main_models.DescribeDevicesResponseBodyDevicesDirectory = None,
        directory_id: str = None,
        dsn: str = None,
        enabled: bool = None,
        gb_id: str = None,
        group_id: str = None,
        id: str = None,
        ip: str = None,
        latitude: str = None,
        longitude: str = None,
        name: str = None,
        params: str = None,
        parent_id: str = None,
        password: str = None,
        port: int = None,
        pos_interval: int = None,
        protocol: str = None,
        registered_time: str = None,
        stats: main_models.DescribeDevicesResponseBodyDevicesStats = None,
        status: str = None,
        type: str = None,
        url: str = None,
        username: str = None,
        vendor: str = None,
    ):
        self.alarm_method = alarm_method
        self.auto_directory = auto_directory
        self.auto_pos = auto_pos
        self.auto_start = auto_start
        self.channel_sync_time = channel_sync_time
        self.created_time = created_time
        self.description = description
        self.directory = directory
        self.directory_id = directory_id
        self.dsn = dsn
        self.enabled = enabled
        self.gb_id = gb_id
        self.group_id = group_id
        self.id = id
        self.ip = ip
        self.latitude = latitude
        self.longitude = longitude
        self.name = name
        self.params = params
        self.parent_id = parent_id
        self.password = password
        self.port = port
        self.pos_interval = pos_interval
        self.protocol = protocol
        self.registered_time = registered_time
        self.stats = stats
        self.status = status
        self.type = type
        self.url = url
        self.username = username
        self.vendor = vendor

    def validate(self):
        if self.directory:
            self.directory.validate()
        if self.stats:
            self.stats.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_method is not None:
            result['AlarmMethod'] = self.alarm_method

        if self.auto_directory is not None:
            result['AutoDirectory'] = self.auto_directory

        if self.auto_pos is not None:
            result['AutoPos'] = self.auto_pos

        if self.auto_start is not None:
            result['AutoStart'] = self.auto_start

        if self.channel_sync_time is not None:
            result['ChannelSyncTime'] = self.channel_sync_time

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.description is not None:
            result['Description'] = self.description

        if self.directory is not None:
            result['Directory'] = self.directory.to_map()

        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.dsn is not None:
            result['Dsn'] = self.dsn

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.gb_id is not None:
            result['GbId'] = self.gb_id

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.id is not None:
            result['Id'] = self.id

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.latitude is not None:
            result['Latitude'] = self.latitude

        if self.longitude is not None:
            result['Longitude'] = self.longitude

        if self.name is not None:
            result['Name'] = self.name

        if self.params is not None:
            result['Params'] = self.params

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        if self.password is not None:
            result['Password'] = self.password

        if self.port is not None:
            result['Port'] = self.port

        if self.pos_interval is not None:
            result['PosInterval'] = self.pos_interval

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.registered_time is not None:
            result['RegisteredTime'] = self.registered_time

        if self.stats is not None:
            result['Stats'] = self.stats.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        if self.url is not None:
            result['Url'] = self.url

        if self.username is not None:
            result['Username'] = self.username

        if self.vendor is not None:
            result['Vendor'] = self.vendor

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmMethod') is not None:
            self.alarm_method = m.get('AlarmMethod')

        if m.get('AutoDirectory') is not None:
            self.auto_directory = m.get('AutoDirectory')

        if m.get('AutoPos') is not None:
            self.auto_pos = m.get('AutoPos')

        if m.get('AutoStart') is not None:
            self.auto_start = m.get('AutoStart')

        if m.get('ChannelSyncTime') is not None:
            self.channel_sync_time = m.get('ChannelSyncTime')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Directory') is not None:
            temp_model = main_models.DescribeDevicesResponseBodyDevicesDirectory()
            self.directory = temp_model.from_map(m.get('Directory'))

        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('Dsn') is not None:
            self.dsn = m.get('Dsn')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('Latitude') is not None:
            self.latitude = m.get('Latitude')

        if m.get('Longitude') is not None:
            self.longitude = m.get('Longitude')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('PosInterval') is not None:
            self.pos_interval = m.get('PosInterval')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('RegisteredTime') is not None:
            self.registered_time = m.get('RegisteredTime')

        if m.get('Stats') is not None:
            temp_model = main_models.DescribeDevicesResponseBodyDevicesStats()
            self.stats = temp_model.from_map(m.get('Stats'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        return self

class DescribeDevicesResponseBodyDevicesStats(DaraModel):
    def __init__(
        self,
        channel_num: int = None,
        failed_num: int = None,
        offline_num: int = None,
        online_num: int = None,
        stream_num: int = None,
    ):
        self.channel_num = channel_num
        self.failed_num = failed_num
        self.offline_num = offline_num
        self.online_num = online_num
        self.stream_num = stream_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_num is not None:
            result['ChannelNum'] = self.channel_num

        if self.failed_num is not None:
            result['FailedNum'] = self.failed_num

        if self.offline_num is not None:
            result['OfflineNum'] = self.offline_num

        if self.online_num is not None:
            result['OnlineNum'] = self.online_num

        if self.stream_num is not None:
            result['StreamNum'] = self.stream_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelNum') is not None:
            self.channel_num = m.get('ChannelNum')

        if m.get('FailedNum') is not None:
            self.failed_num = m.get('FailedNum')

        if m.get('OfflineNum') is not None:
            self.offline_num = m.get('OfflineNum')

        if m.get('OnlineNum') is not None:
            self.online_num = m.get('OnlineNum')

        if m.get('StreamNum') is not None:
            self.stream_num = m.get('StreamNum')

        return self

class DescribeDevicesResponseBodyDevicesDirectory(DaraModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        group_id: str = None,
        id: str = None,
        name: str = None,
        parent_id: str = None,
    ):
        self.created_time = created_time
        self.description = description
        self.group_id = group_id
        self.id = id
        self.name = name
        self.parent_id = parent_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.description is not None:
            result['Description'] = self.description

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        return self

