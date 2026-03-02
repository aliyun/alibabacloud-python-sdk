# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_amqp20190901 import models as main_models
from darabonba.model import DaraModel

class ListVhostResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.ListVhostResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

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

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ListVhostResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListVhostResponseBodyData(DaraModel):
    def __init__(
        self,
        vhosts: List[main_models.ListVhostResponseBodyDataVhosts] = None,
    ):
        self.vhosts = vhosts

    def validate(self):
        if self.vhosts:
            for v1 in self.vhosts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Vhosts'] = []
        if self.vhosts is not None:
            for k1 in self.vhosts:
                result['Vhosts'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.vhosts = []
        if m.get('Vhosts') is not None:
            for k1 in m.get('Vhosts'):
                temp_model = main_models.ListVhostResponseBodyDataVhosts()
                self.vhosts.append(temp_model.from_map(k1))

        return self

class ListVhostResponseBodyDataVhosts(DaraModel):
    def __init__(
        self,
        channel_num: int = None,
        connection_num: int = None,
        name: str = None,
    ):
        self.channel_num = channel_num
        self.connection_num = connection_num
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_num is not None:
            result['ChannelNum'] = self.channel_num

        if self.connection_num is not None:
            result['ConnectionNum'] = self.connection_num

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelNum') is not None:
            self.channel_num = m.get('ChannelNum')

        if m.get('ConnectionNum') is not None:
            self.connection_num = m.get('ConnectionNum')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

