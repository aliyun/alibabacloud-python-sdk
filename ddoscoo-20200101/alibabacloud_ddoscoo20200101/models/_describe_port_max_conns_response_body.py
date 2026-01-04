# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribePortMaxConnsResponseBody(DaraModel):
    def __init__(
        self,
        port_max_conns: List[main_models.DescribePortMaxConnsResponseBodyPortMaxConns] = None,
        request_id: str = None,
    ):
        # The details of the maximum number of connections that can be established over a port of the instance.
        self.port_max_conns = port_max_conns
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.port_max_conns:
            for v1 in self.port_max_conns:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PortMaxConns'] = []
        if self.port_max_conns is not None:
            for k1 in self.port_max_conns:
                result['PortMaxConns'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.port_max_conns = []
        if m.get('PortMaxConns') is not None:
            for k1 in m.get('PortMaxConns'):
                temp_model = main_models.DescribePortMaxConnsResponseBodyPortMaxConns()
                self.port_max_conns.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribePortMaxConnsResponseBodyPortMaxConns(DaraModel):
    def __init__(
        self,
        cps: int = None,
        ip: str = None,
        port: str = None,
    ):
        # The maximum number of connections per second (CPS).
        self.cps = cps
        # The IP address of the instance.
        self.ip = ip
        # The port of the instance.
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cps is not None:
            result['Cps'] = self.cps

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.port is not None:
            result['Port'] = self.port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cps') is not None:
            self.cps = m.get('Cps')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        return self

