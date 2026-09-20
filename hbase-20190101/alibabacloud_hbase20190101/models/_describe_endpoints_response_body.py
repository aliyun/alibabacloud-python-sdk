# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hbase20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeEndpointsResponseBody(DaraModel):
    def __init__(
        self,
        conn_addrs: main_models.DescribeEndpointsResponseBodyConnAddrs = None,
        engine: str = None,
        net_type: str = None,
        request_id: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        self.conn_addrs = conn_addrs
        # The engine type of the instance. Valid values:
        # 
        # - **hbaseue**
        # - **hbase**
        # - **spark**
        # - **geomesa**.
        self.engine = engine
        # The network type of the instance. Valid values:
        # - **VPC**: virtual private cloud.
        # - **CLASSIC**: classic network.
        self.net_type = net_type
        # The request ID.
        self.request_id = request_id
        # The vSwitch ID. This parameter is returned only when NetType is set to **VPC**.
        self.v_switch_id = v_switch_id
        # The VPC ID. This parameter is returned only when NetType is set to **VPC**.
        self.vpc_id = vpc_id

    def validate(self):
        if self.conn_addrs:
            self.conn_addrs.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conn_addrs is not None:
            result['ConnAddrs'] = self.conn_addrs.to_map()

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.net_type is not None:
            result['NetType'] = self.net_type

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnAddrs') is not None:
            temp_model = main_models.DescribeEndpointsResponseBodyConnAddrs()
            self.conn_addrs = temp_model.from_map(m.get('ConnAddrs'))

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class DescribeEndpointsResponseBodyConnAddrs(DaraModel):
    def __init__(
        self,
        conn_addr_info: List[main_models.DescribeEndpointsResponseBodyConnAddrsConnAddrInfo] = None,
    ):
        self.conn_addr_info = conn_addr_info

    def validate(self):
        if self.conn_addr_info:
            for v1 in self.conn_addr_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ConnAddrInfo'] = []
        if self.conn_addr_info is not None:
            for k1 in self.conn_addr_info:
                result['ConnAddrInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conn_addr_info = []
        if m.get('ConnAddrInfo') is not None:
            for k1 in m.get('ConnAddrInfo'):
                temp_model = main_models.DescribeEndpointsResponseBodyConnAddrsConnAddrInfo()
                self.conn_addr_info.append(temp_model.from_map(k1))

        return self

class DescribeEndpointsResponseBodyConnAddrsConnAddrInfo(DaraModel):
    def __init__(
        self,
        conn_addr: str = None,
        conn_addr_port: str = None,
        conn_type: str = None,
        net_type: str = None,
    ):
        self.conn_addr = conn_addr
        self.conn_addr_port = conn_addr_port
        self.conn_type = conn_type
        self.net_type = net_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conn_addr is not None:
            result['ConnAddr'] = self.conn_addr

        if self.conn_addr_port is not None:
            result['ConnAddrPort'] = self.conn_addr_port

        if self.conn_type is not None:
            result['ConnType'] = self.conn_type

        if self.net_type is not None:
            result['NetType'] = self.net_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnAddr') is not None:
            self.conn_addr = m.get('ConnAddr')

        if m.get('ConnAddrPort') is not None:
            self.conn_addr_port = m.get('ConnAddrPort')

        if m.get('ConnType') is not None:
            self.conn_type = m.get('ConnType')

        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')

        return self

