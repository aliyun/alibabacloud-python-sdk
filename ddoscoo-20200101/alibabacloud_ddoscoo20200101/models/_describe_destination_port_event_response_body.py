# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeDestinationPortEventResponseBody(DaraModel):
    def __init__(
        self,
        port_list: List[main_models.DescribeDestinationPortEventResponseBodyPortList] = None,
        request_id: str = None,
    ):
        # The ports.
        self.port_list = port_list
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.port_list:
            for v1 in self.port_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PortList'] = []
        if self.port_list is not None:
            for k1 in self.port_list:
                result['PortList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.port_list = []
        if m.get('PortList') is not None:
            for k1 in m.get('PortList'):
                temp_model = main_models.DescribeDestinationPortEventResponseBodyPortList()
                self.port_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDestinationPortEventResponseBodyPortList(DaraModel):
    def __init__(
        self,
        dst_port: str = None,
        in_pkts: int = None,
    ):
        # The destination port.
        self.dst_port = dst_port
        # The number of request packets received by the destination port.
        self.in_pkts = in_pkts

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dst_port is not None:
            result['DstPort'] = self.dst_port

        if self.in_pkts is not None:
            result['InPkts'] = self.in_pkts

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DstPort') is not None:
            self.dst_port = m.get('DstPort')

        if m.get('InPkts') is not None:
            self.in_pkts = m.get('InPkts')

        return self

