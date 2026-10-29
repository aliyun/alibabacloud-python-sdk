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
        # The subscribed national standard alarm methods. Valid values:
        # - 0: All.
        # - 5: Video alarm.
        # - 7: Other alarms.
        # > - An empty value indicates no subscription.
        # > - Multiple values are supported and must be separated by commas (,).
        self.alarm_method = alarm_method
        self.auto_directory = auto_directory
        # Specifies whether device position subscription is enabled.
        self.auto_pos = auto_pos
        # Specifies whether to automatically start the stream.
        self.auto_start = auto_start
        # The channel synchronization time. The time is in UTC and follows the ISO 8601 standard in the YYYY-MM-DDTHH:mm:ssZ format.
        self.channel_sync_time = channel_sync_time
        # The time when the device was created. The time is in UTC and follows the ISO 8601 standard in the YYYY-MM-DDTHH:mm:ssZ format.
        self.created_time = created_time
        # The device description.
        self.description = description
        # The directory information.
        self.directory = directory
        # The directory ID.
        self.directory_id = directory_id
        # The device serial number.
        self.dsn = dsn
        # Specifies whether the device is enabled.
        self.enabled = enabled
        # The national standard ID of the device.
        # > This parameter is applicable only to the national standard protocol.
        self.gb_id = gb_id
        # The ID of the workspace to which the device belongs.
        self.group_id = group_id
        # The device ID.
        self.id = id
        # The IP address of the device.
        self.ip = ip
        # The latitude of the device.
        self.latitude = latitude
        # The longitude of the device.
        self.longitude = longitude
        # The device name.
        self.name = name
        # Other parameters of the device.
        self.params = params
        # The ID of the parent device, such as the ID of the platform to which the camera belongs.
        self.parent_id = parent_id
        # The device password.
        self.password = password
        # The device port.
        self.port = port
        # The position subscription interval, in seconds.
        self.pos_interval = pos_interval
        # The device registration protocol.
        self.protocol = protocol
        # The time when the device was registered. The time is in UTC and follows the ISO 8601 standard in the YYYY-MM-DDTHH:mm:ssZ format.
        self.registered_time = registered_time
        # The request ID.
        self.request_id = request_id
        # The stream statistics information of the device.
        self.stats = stats
        # The device status. Valid values:
        # - on: Online.
        # - off: Offline.
        # - failed: Locked.
        # - new: Unregistered.
        self.status = status
        # The device type. Valid values:
        # - ipc: IP camera.
        # - platform: Platform.
        # - ied: Intelligent device.
        self.type = type
        # The stream URL on the device.
        self.url = url
        # The device username.
        self.username = username
        # The device vendor.
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
        # The number of channels.
        self.channel_num = channel_num
        # The number of failed streams.
        self.failed_num = failed_num
        # The number of offline streams.
        self.offline_num = offline_num
        # The number of online streams.
        self.online_num = online_num
        # The number of streams.
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
        # The time when the directory was created. The time is in UTC and follows the ISO 8601 standard in the YYYY-MM-DDTHH:mm:ssZ format.
        self.created_time = created_time
        # The directory description.
        self.description = description
        # The ID of the workspace to which the directory belongs.
        self.group_id = group_id
        # The directory ID.
        self.id = id
        # The directory name.
        self.name = name
        # The ID of the parent directory.
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

