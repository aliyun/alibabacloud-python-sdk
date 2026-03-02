# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_amqp20190901 import models as main_models
from darabonba.model import DaraModel

class GetVhostRateResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: List[main_models.GetVhostRateResponseBodyData] = None,
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
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

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

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetVhostRateResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetVhostRateResponseBodyData(DaraModel):
    def __init__(
        self,
        channel_num: int = None,
        connection_num: int = None,
        in_qps: int = None,
        out_qps: int = None,
        vhost_name: str = None,
    ):
        self.channel_num = channel_num
        self.connection_num = connection_num
        self.in_qps = in_qps
        self.out_qps = out_qps
        self.vhost_name = vhost_name

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

        if self.in_qps is not None:
            result['InQps'] = self.in_qps

        if self.out_qps is not None:
            result['OutQps'] = self.out_qps

        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelNum') is not None:
            self.channel_num = m.get('ChannelNum')

        if m.get('ConnectionNum') is not None:
            self.connection_num = m.get('ConnectionNum')

        if m.get('InQps') is not None:
            self.in_qps = m.get('InQps')

        if m.get('OutQps') is not None:
            self.out_qps = m.get('OutQps')

        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')

        return self

