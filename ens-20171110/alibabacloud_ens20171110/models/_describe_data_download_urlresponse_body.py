# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeDataDownloadURLResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.DescribeDataDownloadURLResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The HTTP status code.
        self.code = code
        # The download URLs of data files.
        self.data = data
        # The response message. Success is returned for a successful request.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.DescribeDataDownloadURLResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDataDownloadURLResponseBodyData(DaraModel):
    def __init__(
        self,
        expire_time: str = None,
        server_list: List[main_models.DescribeDataDownloadURLResponseBodyDataServerList] = None,
        url: str = None,
    ):
        # The time when the data file expires. The time is displayed in UTC.
        self.expire_time = expire_time
        # The file servers.
        self.server_list = server_list
        # The download URL of the data file.
        self.url = url

    def validate(self):
        if self.server_list:
            for v1 in self.server_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        result['ServerList'] = []
        if self.server_list is not None:
            for k1 in self.server_list:
                result['ServerList'].append(k1.to_map() if k1 else None)

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        self.server_list = []
        if m.get('ServerList') is not None:
            for k1 in m.get('ServerList'):
                temp_model = main_models.DescribeDataDownloadURLResponseBodyDataServerList()
                self.server_list.append(temp_model.from_map(k1))

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class DescribeDataDownloadURLResponseBodyDataServerList(DaraModel):
    def __init__(
        self,
        host: str = None,
        region_id: str = None,
    ):
        # The host address of the file server.
        self.host = host
        # The ID of the Edge Node Service (ENS) node.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.host is not None:
            result['Host'] = self.host

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

