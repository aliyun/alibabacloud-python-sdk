# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class DescribeStreamsResponseBody(DaraModel):
    def __init__(
        self,
        page_count: int = None,
        page_num: int = None,
        page_size: int = None,
        request_id: str = None,
        streams: List[main_models.DescribeStreamsResponseBodyStreams] = None,
        total_count: int = None,
    ):
        self.page_count = page_count
        self.page_num = page_num
        self.page_size = page_size
        self.request_id = request_id
        self.streams = streams
        self.total_count = total_count

    def validate(self):
        if self.streams:
            for v1 in self.streams:
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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Streams'] = []
        if self.streams is not None:
            for k1 in self.streams:
                result['Streams'].append(k1.to_map() if k1 else None)

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

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.streams = []
        if m.get('Streams') is not None:
            for k1 in m.get('Streams'):
                temp_model = main_models.DescribeStreamsResponseBodyStreams()
                self.streams.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeStreamsResponseBodyStreams(DaraModel):
    def __init__(
        self,
        app: str = None,
        created_time: str = None,
        device_id: str = None,
        enabled: bool = None,
        group_id: str = None,
        height: int = None,
        id: str = None,
        name: str = None,
        play_domain: str = None,
        protocol: str = None,
        push_domain: str = None,
        status: str = None,
        width: int = None,
    ):
        self.app = app
        self.created_time = created_time
        self.device_id = device_id
        self.enabled = enabled
        self.group_id = group_id
        self.height = height
        self.id = id
        self.name = name
        self.play_domain = play_domain
        self.protocol = protocol
        self.push_domain = push_domain
        self.status = status
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app is not None:
            result['App'] = self.app

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.height is not None:
            result['Height'] = self.height

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.play_domain is not None:
            result['PlayDomain'] = self.play_domain

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.push_domain is not None:
            result['PushDomain'] = self.push_domain

        if self.status is not None:
            result['Status'] = self.status

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            self.app = m.get('App')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PlayDomain') is not None:
            self.play_domain = m.get('PlayDomain')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('PushDomain') is not None:
            self.push_domain = m.get('PushDomain')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

