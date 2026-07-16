# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDeviceRequest(DaraModel):
    def __init__(
        self,
        alarm_method: str = None,
        auto_directory: bool = None,
        auto_pos: bool = None,
        auto_start: bool = None,
        description: str = None,
        directory_id: str = None,
        dsn: str = None,
        gb_id: str = None,
        group_id: str = None,
        ip: str = None,
        latitude: str = None,
        longitude: str = None,
        name: str = None,
        owner_id: int = None,
        params: str = None,
        parent_id: str = None,
        password: str = None,
        port: int = None,
        pos_interval: int = None,
        type: str = None,
        url: str = None,
        username: str = None,
        vendor: str = None,
    ):
        # GB-compliant alarm method to subscribe to. Valid values:
        # 
        # - 0 (all)
        # 
        # - 5 (video alarm)
        # 
        # - 7 (other alarms)
        # 
        # > * An empty value means no subscription.
        # >
        # > * You can specify multiple values, separated by commas (,).
        self.alarm_method = alarm_method
        self.auto_directory = auto_directory
        # Whether to enable location subscription for the device. Default value: false.
        self.auto_pos = auto_pos
        # Whether to automatically start the stream. Default value: false.
        self.auto_start = auto_start
        # Device description.
        self.description = description
        # ID of the folder that contains the device.
        self.directory_id = directory_id
        # Device serial number.
        self.dsn = dsn
        # GB-compliant device ID.
        # 
        # > This parameter applies only to GB-compliant protocols.
        self.gb_id = gb_id
        # ID of the space that contains the device.
        # 
        # This parameter is required.
        self.group_id = group_id
        # Device IP address.
        self.ip = ip
        # The dimension of the device.
        self.latitude = latitude
        # Device longitude.
        self.longitude = longitude
        # Device name.
        self.name = name
        self.owner_id = owner_id
        # Additional device parameters, formatted as a JSON string.
        self.params = params
        # ID of the parent device. For example, the ID of the platform that hosts the camera.
        self.parent_id = parent_id
        # Device password.
        self.password = password
        # Device port.
        self.port = port
        # Location subscription interval, in seconds.
        self.pos_interval = pos_interval
        # Device type. Valid values:
        # 
        # - ipc (camera)
        # 
        # - platform (platform)
        # 
        # - ied (intelligent device)
        # 
        # This parameter is required.
        self.type = type
        # Stream URL on the device.
        self.url = url
        # Device username.
        self.username = username
        # Device vendor.
        self.vendor = vendor

    def validate(self):
        pass

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

        if self.description is not None:
            result['Description'] = self.description

        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.dsn is not None:
            result['Dsn'] = self.dsn

        if self.gb_id is not None:
            result['GbId'] = self.gb_id

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.latitude is not None:
            result['Latitude'] = self.latitude

        if self.longitude is not None:
            result['Longitude'] = self.longitude

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

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

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('Dsn') is not None:
            self.dsn = m.get('Dsn')

        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('Latitude') is not None:
            self.latitude = m.get('Latitude')

        if m.get('Longitude') is not None:
            self.longitude = m.get('Longitude')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

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

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        return self

