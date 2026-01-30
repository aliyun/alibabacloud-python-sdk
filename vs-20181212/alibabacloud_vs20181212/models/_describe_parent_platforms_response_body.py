# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class DescribeParentPlatformsResponseBody(DaraModel):
    def __init__(
        self,
        page_count: int = None,
        page_num: int = None,
        page_size: int = None,
        platforms: List[main_models.DescribeParentPlatformsResponseBodyPlatforms] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.page_count = page_count
        self.page_num = page_num
        self.page_size = page_size
        self.platforms = platforms
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.platforms:
            for v1 in self.platforms:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_count is not None:
            result['PageCount'] = self.page_count

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['Platforms'] = []
        if self.platforms is not None:
            for k1 in self.platforms:
                result['Platforms'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.platforms = []
        if m.get('Platforms') is not None:
            for k1 in m.get('Platforms'):
                temp_model = main_models.DescribeParentPlatformsResponseBodyPlatforms()
                self.platforms.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeParentPlatformsResponseBodyPlatforms(DaraModel):
    def __init__(
        self,
        auto_start: bool = None,
        client_auth: bool = None,
        client_gb_id: str = None,
        client_ip: str = None,
        client_password: str = None,
        client_port: int = None,
        client_username: str = None,
        created_time: str = None,
        description: str = None,
        gb_id: str = None,
        id: str = None,
        ip: str = None,
        name: str = None,
        port: int = None,
        protocol: str = None,
        status: str = None,
    ):
        self.auto_start = auto_start
        self.client_auth = client_auth
        self.client_gb_id = client_gb_id
        self.client_ip = client_ip
        self.client_password = client_password
        self.client_port = client_port
        self.client_username = client_username
        self.created_time = created_time
        self.description = description
        self.gb_id = gb_id
        self.id = id
        self.ip = ip
        self.name = name
        self.port = port
        self.protocol = protocol
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_start is not None:
            result['AutoStart'] = self.auto_start

        if self.client_auth is not None:
            result['ClientAuth'] = self.client_auth

        if self.client_gb_id is not None:
            result['ClientGbId'] = self.client_gb_id

        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip

        if self.client_password is not None:
            result['ClientPassword'] = self.client_password

        if self.client_port is not None:
            result['ClientPort'] = self.client_port

        if self.client_username is not None:
            result['ClientUsername'] = self.client_username

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.description is not None:
            result['Description'] = self.description

        if self.gb_id is not None:
            result['GbId'] = self.gb_id

        if self.id is not None:
            result['Id'] = self.id

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.name is not None:
            result['Name'] = self.name

        if self.port is not None:
            result['Port'] = self.port

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoStart') is not None:
            self.auto_start = m.get('AutoStart')

        if m.get('ClientAuth') is not None:
            self.client_auth = m.get('ClientAuth')

        if m.get('ClientGbId') is not None:
            self.client_gb_id = m.get('ClientGbId')

        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')

        if m.get('ClientPassword') is not None:
            self.client_password = m.get('ClientPassword')

        if m.get('ClientPort') is not None:
            self.client_port = m.get('ClientPort')

        if m.get('ClientUsername') is not None:
            self.client_username = m.get('ClientUsername')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

