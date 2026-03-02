# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_amqp20190901 import models as main_models
from darabonba.model import DaraModel

class GetStatisticsByVhostResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetStatisticsByVhostResponseBodyData = None,
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
            temp_model = main_models.GetStatisticsByVhostResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetStatisticsByVhostResponseBodyData(DaraModel):
    def __init__(
        self,
        connection_statistics: List[main_models.GetStatisticsByVhostResponseBodyDataConnectionStatistics] = None,
    ):
        self.connection_statistics = connection_statistics

    def validate(self):
        if self.connection_statistics:
            for v1 in self.connection_statistics:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ConnectionStatistics'] = []
        if self.connection_statistics is not None:
            for k1 in self.connection_statistics:
                result['ConnectionStatistics'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.connection_statistics = []
        if m.get('ConnectionStatistics') is not None:
            for k1 in m.get('ConnectionStatistics'):
                temp_model = main_models.GetStatisticsByVhostResponseBodyDataConnectionStatistics()
                self.connection_statistics.append(temp_model.from_map(k1))

        return self

class GetStatisticsByVhostResponseBodyDataConnectionStatistics(DaraModel):
    def __init__(
        self,
        access_key: str = None,
        channel_num: int = None,
        channel_statistics_list: main_models.GetStatisticsByVhostResponseBodyDataConnectionStatisticsChannelStatisticsList = None,
        connection_name: str = None,
        deliver_qps: float = None,
        protocol: str = None,
        publish_qps: float = None,
        remote_address: str = None,
        security_transport: bool = None,
        state: int = None,
    ):
        self.access_key = access_key
        self.channel_num = channel_num
        self.channel_statistics_list = channel_statistics_list
        self.connection_name = connection_name
        self.deliver_qps = deliver_qps
        self.protocol = protocol
        self.publish_qps = publish_qps
        self.remote_address = remote_address
        self.security_transport = security_transport
        self.state = state

    def validate(self):
        if self.channel_statistics_list:
            self.channel_statistics_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_key is not None:
            result['AccessKey'] = self.access_key

        if self.channel_num is not None:
            result['ChannelNum'] = self.channel_num

        if self.channel_statistics_list is not None:
            result['ChannelStatisticsList'] = self.channel_statistics_list.to_map()

        if self.connection_name is not None:
            result['ConnectionName'] = self.connection_name

        if self.deliver_qps is not None:
            result['DeliverQps'] = self.deliver_qps

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.publish_qps is not None:
            result['PublishQps'] = self.publish_qps

        if self.remote_address is not None:
            result['RemoteAddress'] = self.remote_address

        if self.security_transport is not None:
            result['SecurityTransport'] = self.security_transport

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')

        if m.get('ChannelNum') is not None:
            self.channel_num = m.get('ChannelNum')

        if m.get('ChannelStatisticsList') is not None:
            temp_model = main_models.GetStatisticsByVhostResponseBodyDataConnectionStatisticsChannelStatisticsList()
            self.channel_statistics_list = temp_model.from_map(m.get('ChannelStatisticsList'))

        if m.get('ConnectionName') is not None:
            self.connection_name = m.get('ConnectionName')

        if m.get('DeliverQps') is not None:
            self.deliver_qps = m.get('DeliverQps')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('PublishQps') is not None:
            self.publish_qps = m.get('PublishQps')

        if m.get('RemoteAddress') is not None:
            self.remote_address = m.get('RemoteAddress')

        if m.get('SecurityTransport') is not None:
            self.security_transport = m.get('SecurityTransport')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

class GetStatisticsByVhostResponseBodyDataConnectionStatisticsChannelStatisticsList(DaraModel):
    def __init__(
        self,
        channel_statistics: List[main_models.GetStatisticsByVhostResponseBodyDataConnectionStatisticsChannelStatisticsListChannelStatistics] = None,
    ):
        self.channel_statistics = channel_statistics

    def validate(self):
        if self.channel_statistics:
            for v1 in self.channel_statistics:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ChannelStatistics'] = []
        if self.channel_statistics is not None:
            for k1 in self.channel_statistics:
                result['ChannelStatistics'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.channel_statistics = []
        if m.get('ChannelStatistics') is not None:
            for k1 in m.get('ChannelStatistics'):
                temp_model = main_models.GetStatisticsByVhostResponseBodyDataConnectionStatisticsChannelStatisticsListChannelStatistics()
                self.channel_statistics.append(temp_model.from_map(k1))

        return self

class GetStatisticsByVhostResponseBodyDataConnectionStatisticsChannelStatisticsListChannelStatistics(DaraModel):
    def __init__(
        self,
        ack_qps: float = None,
        confirm_qps: float = None,
        deliver_qps: float = None,
        get_qps: float = None,
        prefetch: int = None,
        publish_qps: float = None,
        state: int = None,
        unacked: int = None,
        unconfirmed: int = None,
    ):
        self.ack_qps = ack_qps
        self.confirm_qps = confirm_qps
        self.deliver_qps = deliver_qps
        self.get_qps = get_qps
        self.prefetch = prefetch
        self.publish_qps = publish_qps
        self.state = state
        self.unacked = unacked
        self.unconfirmed = unconfirmed

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ack_qps is not None:
            result['AckQps'] = self.ack_qps

        if self.confirm_qps is not None:
            result['ConfirmQps'] = self.confirm_qps

        if self.deliver_qps is not None:
            result['DeliverQps'] = self.deliver_qps

        if self.get_qps is not None:
            result['GetQps'] = self.get_qps

        if self.prefetch is not None:
            result['Prefetch'] = self.prefetch

        if self.publish_qps is not None:
            result['PublishQps'] = self.publish_qps

        if self.state is not None:
            result['State'] = self.state

        if self.unacked is not None:
            result['Unacked'] = self.unacked

        if self.unconfirmed is not None:
            result['Unconfirmed'] = self.unconfirmed

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AckQps') is not None:
            self.ack_qps = m.get('AckQps')

        if m.get('ConfirmQps') is not None:
            self.confirm_qps = m.get('ConfirmQps')

        if m.get('DeliverQps') is not None:
            self.deliver_qps = m.get('DeliverQps')

        if m.get('GetQps') is not None:
            self.get_qps = m.get('GetQps')

        if m.get('Prefetch') is not None:
            self.prefetch = m.get('Prefetch')

        if m.get('PublishQps') is not None:
            self.publish_qps = m.get('PublishQps')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Unacked') is not None:
            self.unacked = m.get('Unacked')

        if m.get('Unconfirmed') is not None:
            self.unconfirmed = m.get('Unconfirmed')

        return self

