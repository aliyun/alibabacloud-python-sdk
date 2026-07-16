# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class DescribeDeviceResponseBody(DaraModel):
    def __init__(
        self,
        alarm_method: str = None,
        auto_directory: bool = None,
        auto_pos: bool = None,
        auto_start: bool = None,
        channel_sync_time: str = None,
        created_time: str = None,
        description: str = None,
        directory: main_models.DescribeDeviceResponseBodyDirectory = None,
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
        request_id: str = None,
        stats: main_models.DescribeDeviceResponseBodyStats = None,
        status: str = None,
        type: str = None,
        url: str = None,
        username: str = None,
        vendor: str = None,
    ):
        # Subscribed GB alarm method. Valid values:
        # 
        # - 0 (all)
        # 
        # - 5 (video alarm)
        # 
        # - 7 (other alarms)
        # 
        # > * An empty value means no subscription.
        # >
        # > * Multiple values are supported, separated by commas (,).
        self.alarm_method = alarm_method
        self.auto_directory = auto_directory
        # Indicates whether device location subscription is enabled.
        self.auto_pos = auto_pos
        # Automatically start the stream.
        self.auto_start = auto_start
        # Channel synchronization time.
        self.channel_sync_time = channel_sync_time
        # Device creation time.
        self.created_time = created_time
        # Device description.
        self.description = description
        # Directory information.
        self.directory = directory
        # Directory ID.
        self.directory_id = directory_id
        # Device serial number.
        self.dsn = dsn
        # Whether the device is enabled.
        self.enabled = enabled
        # GB device ID.
        # 
        # > This applies only to GB protocols.
        self.gb_id = gb_id
        # Space ID to which the device belongs.
        self.group_id = group_id
        # Device ID.
        self.id = id
        # Device IP address.
        self.ip = ip
        # Device latitude.
        self.latitude = latitude
        # Device longitude.
        self.longitude = longitude
        # Device name.
        self.name = name
        # Other device parameters.
        self.params = params
        # Parent device ID. For example, the platform ID to which a camera belongs.
        self.parent_id = parent_id
        # Device password.
        self.password = password
        # Device port.
        self.port = port
        # Position subscription interval, in seconds.
        self.pos_interval = pos_interval
        # Device registration protocol.
        self.protocol = protocol
        # Device registration time.
        self.registered_time = registered_time
        # Request ID.
        self.request_id = request_id
        # Device stream statistics.
        self.stats = stats
        # Device status. Valid values:
        # 
        # - on (online)
        # 
        # - off (offline)
        # 
        # - failed (locked)
        # 
        # - new (unregistered)
        self.status = status
        # Device type. Valid values:
        # 
        # - ipc (camera)
        # 
        # - platform (platform)
        # 
        # - ied (intelligent device)
        self.type = type
        # Stream URL on the device.
        self.url = url
        # Device username.
        self.username = username
        # Device vendor.
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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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
            temp_model = main_models.DescribeDeviceResponseBodyDirectory()
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

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Stats') is not None:
            temp_model = main_models.DescribeDeviceResponseBodyStats()
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

class DescribeDeviceResponseBodyStats(DaraModel):
    def __init__(
        self,
        channel_num: int = None,
        failed_num: int = None,
        offline_num: int = None,
        online_num: int = None,
        stream_num: int = None,
    ):
        # Number of channels.
        self.channel_num = channel_num
        # Number of failed streams.
        self.failed_num = failed_num
        # Number of offline streams.
        self.offline_num = offline_num
        # Number of online streams.
        self.online_num = online_num
        # Number of streams.
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

class DescribeDeviceResponseBodyDirectory(DaraModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        group_id: str = None,
        id: str = None,
        name: str = None,
        parent_id: str = None,
    ):
        # Directory creation time.
        self.created_time = created_time
        # Directory description.
        self.description = description
        # Space ID to which the directory belongs.
        self.group_id = group_id
        # Directory ID.
        self.id = id
        # Directory name.
        self.name = name
        # Parent directory ID.
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

