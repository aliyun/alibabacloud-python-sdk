# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_amqp_open20191212 import models as main_models
from darabonba.model import DaraModel

class GetMetadataAmountResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetMetadataAmountResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetMetadataAmountResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetMetadataAmountResponseBodyData(DaraModel):
    def __init__(
        self,
        current_exchanges: int = None,
        current_queues: int = None,
        current_virtual_hosts: int = None,
        max_exchanges: int = None,
        max_queues: int = None,
        max_virtual_hosts: int = None,
    ):
        # The number of created exchanges on the ApsaraMQ for RabbitMQ instance.
        self.current_exchanges = current_exchanges
        # The number of created queues on the ApsaraMQ for RabbitMQ instance.
        self.current_queues = current_queues
        # The number of created vhosts on the ApsaraMQ for RabbitMQ instance.
        self.current_virtual_hosts = current_virtual_hosts
        # The maximum number of exchanges that can be created on the ApsaraMQ for RabbitMQ instance.
        self.max_exchanges = max_exchanges
        # The maximum number of queues that can be created on the ApsaraMQ for RabbitMQ instance.
        self.max_queues = max_queues
        # The maximum number of vhosts that can be created on the ApsaraMQ for RabbitMQ instance.
        self.max_virtual_hosts = max_virtual_hosts

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_exchanges is not None:
            result['CurrentExchanges'] = self.current_exchanges

        if self.current_queues is not None:
            result['CurrentQueues'] = self.current_queues

        if self.current_virtual_hosts is not None:
            result['CurrentVirtualHosts'] = self.current_virtual_hosts

        if self.max_exchanges is not None:
            result['MaxExchanges'] = self.max_exchanges

        if self.max_queues is not None:
            result['MaxQueues'] = self.max_queues

        if self.max_virtual_hosts is not None:
            result['MaxVirtualHosts'] = self.max_virtual_hosts

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentExchanges') is not None:
            self.current_exchanges = m.get('CurrentExchanges')

        if m.get('CurrentQueues') is not None:
            self.current_queues = m.get('CurrentQueues')

        if m.get('CurrentVirtualHosts') is not None:
            self.current_virtual_hosts = m.get('CurrentVirtualHosts')

        if m.get('MaxExchanges') is not None:
            self.max_exchanges = m.get('MaxExchanges')

        if m.get('MaxQueues') is not None:
            self.max_queues = m.get('MaxQueues')

        if m.get('MaxVirtualHosts') is not None:
            self.max_virtual_hosts = m.get('MaxVirtualHosts')

        return self

