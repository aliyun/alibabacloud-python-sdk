# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hbase20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeClusterConnectionResponseBody(DaraModel):
    def __init__(
        self,
        db_type: str = None,
        is_multimod: str = None,
        net_type: str = None,
        request_id: str = None,
        service_conn_addrs: main_models.DescribeClusterConnectionResponseBodyServiceConnAddrs = None,
        slb_conn_addrs: main_models.DescribeClusterConnectionResponseBodySlbConnAddrs = None,
        thrift_conn: main_models.DescribeClusterConnectionResponseBodyThriftConn = None,
        ui_proxy_conn_addr_info: main_models.DescribeClusterConnectionResponseBodyUiProxyConnAddrInfo = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zk_conn_addrs: main_models.DescribeClusterConnectionResponseBodyZkConnAddrs = None,
    ):
        # The database engine type. Valid values:
        # 
        # - **hbaseue**: ApsaraDB for HBase Performance-enhanced Edition.
        # - **hbase**: ApsaraDB for HBase Standard Edition or ApsaraDB for HBase single-node edition.
        # - **bds**: a BDS instance.
        self.db_type = db_type
        # Indicates whether multi-model management is enabled. Valid values:
        # 
        # - **true**: Multi-model management is enabled.
        # - **false**: Multi-model management is not enabled.
        self.is_multimod = is_multimod
        # The network type of the instance. Valid values:
        # 
        # - **VPC**: Virtual Private Cloud (VPC).
        # - **CLASSIC**: classic network.
        self.net_type = net_type
        # The request ID.
        self.request_id = request_id
        self.service_conn_addrs = service_conn_addrs
        self.slb_conn_addrs = slb_conn_addrs
        # The Thrift endpoint information list.
        # 
        # > This parameter list is returned only when the database DPI engine type is **hbase**.
        self.thrift_conn = thrift_conn
        # The WebUI connection information list.
        self.ui_proxy_conn_addr_info = ui_proxy_conn_addr_info
        # The vSwitch ID in the VPC.
        self.v_switch_id = v_switch_id
        # The VPC ID.
        self.vpc_id = vpc_id
        self.zk_conn_addrs = zk_conn_addrs

    def validate(self):
        if self.service_conn_addrs:
            self.service_conn_addrs.validate()
        if self.slb_conn_addrs:
            self.slb_conn_addrs.validate()
        if self.thrift_conn:
            self.thrift_conn.validate()
        if self.ui_proxy_conn_addr_info:
            self.ui_proxy_conn_addr_info.validate()
        if self.zk_conn_addrs:
            self.zk_conn_addrs.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_type is not None:
            result['DbType'] = self.db_type

        if self.is_multimod is not None:
            result['IsMultimod'] = self.is_multimod

        if self.net_type is not None:
            result['NetType'] = self.net_type

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.service_conn_addrs is not None:
            result['ServiceConnAddrs'] = self.service_conn_addrs.to_map()

        if self.slb_conn_addrs is not None:
            result['SlbConnAddrs'] = self.slb_conn_addrs.to_map()

        if self.thrift_conn is not None:
            result['ThriftConn'] = self.thrift_conn.to_map()

        if self.ui_proxy_conn_addr_info is not None:
            result['UiProxyConnAddrInfo'] = self.ui_proxy_conn_addr_info.to_map()

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zk_conn_addrs is not None:
            result['ZkConnAddrs'] = self.zk_conn_addrs.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

        if m.get('IsMultimod') is not None:
            self.is_multimod = m.get('IsMultimod')

        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ServiceConnAddrs') is not None:
            temp_model = main_models.DescribeClusterConnectionResponseBodyServiceConnAddrs()
            self.service_conn_addrs = temp_model.from_map(m.get('ServiceConnAddrs'))

        if m.get('SlbConnAddrs') is not None:
            temp_model = main_models.DescribeClusterConnectionResponseBodySlbConnAddrs()
            self.slb_conn_addrs = temp_model.from_map(m.get('SlbConnAddrs'))

        if m.get('ThriftConn') is not None:
            temp_model = main_models.DescribeClusterConnectionResponseBodyThriftConn()
            self.thrift_conn = temp_model.from_map(m.get('ThriftConn'))

        if m.get('UiProxyConnAddrInfo') is not None:
            temp_model = main_models.DescribeClusterConnectionResponseBodyUiProxyConnAddrInfo()
            self.ui_proxy_conn_addr_info = temp_model.from_map(m.get('UiProxyConnAddrInfo'))

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZkConnAddrs') is not None:
            temp_model = main_models.DescribeClusterConnectionResponseBodyZkConnAddrs()
            self.zk_conn_addrs = temp_model.from_map(m.get('ZkConnAddrs'))

        return self

class DescribeClusterConnectionResponseBodyZkConnAddrs(DaraModel):
    def __init__(
        self,
        zk_conn_addr: List[main_models.DescribeClusterConnectionResponseBodyZkConnAddrsZkConnAddr] = None,
    ):
        self.zk_conn_addr = zk_conn_addr

    def validate(self):
        if self.zk_conn_addr:
            for v1 in self.zk_conn_addr:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ZkConnAddr'] = []
        if self.zk_conn_addr is not None:
            for k1 in self.zk_conn_addr:
                result['ZkConnAddr'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.zk_conn_addr = []
        if m.get('ZkConnAddr') is not None:
            for k1 in m.get('ZkConnAddr'):
                temp_model = main_models.DescribeClusterConnectionResponseBodyZkConnAddrsZkConnAddr()
                self.zk_conn_addr.append(temp_model.from_map(k1))

        return self

class DescribeClusterConnectionResponseBodyZkConnAddrsZkConnAddr(DaraModel):
    def __init__(
        self,
        conn_addr: str = None,
        conn_addr_port: str = None,
        net_type: str = None,
    ):
        self.conn_addr = conn_addr
        self.conn_addr_port = conn_addr_port
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

        if self.net_type is not None:
            result['NetType'] = self.net_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnAddr') is not None:
            self.conn_addr = m.get('ConnAddr')

        if m.get('ConnAddrPort') is not None:
            self.conn_addr_port = m.get('ConnAddrPort')

        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')

        return self

class DescribeClusterConnectionResponseBodyUiProxyConnAddrInfo(DaraModel):
    def __init__(
        self,
        conn_addr: str = None,
        conn_addr_port: str = None,
        net_type: str = None,
    ):
        # The endpoint.
        self.conn_addr = conn_addr
        # The connection port.
        self.conn_addr_port = conn_addr_port
        # The access type of the endpoint, which is public network access.
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

        if self.net_type is not None:
            result['NetType'] = self.net_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnAddr') is not None:
            self.conn_addr = m.get('ConnAddr')

        if m.get('ConnAddrPort') is not None:
            self.conn_addr_port = m.get('ConnAddrPort')

        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')

        return self

class DescribeClusterConnectionResponseBodyThriftConn(DaraModel):
    def __init__(
        self,
        conn_addr: str = None,
        conn_addr_port: str = None,
        net_type: str = None,
    ):
        # The endpoint.
        self.conn_addr = conn_addr
        # The connection port.
        self.conn_addr_port = conn_addr_port
        # The access type of the endpoint. Valid values:
        # 
        # - **2**: internal network access.
        # - **0**: public network access.
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

        if self.net_type is not None:
            result['NetType'] = self.net_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnAddr') is not None:
            self.conn_addr = m.get('ConnAddr')

        if m.get('ConnAddrPort') is not None:
            self.conn_addr_port = m.get('ConnAddrPort')

        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')

        return self

class DescribeClusterConnectionResponseBodySlbConnAddrs(DaraModel):
    def __init__(
        self,
        slb_conn_addr: List[main_models.DescribeClusterConnectionResponseBodySlbConnAddrsSlbConnAddr] = None,
    ):
        self.slb_conn_addr = slb_conn_addr

    def validate(self):
        if self.slb_conn_addr:
            for v1 in self.slb_conn_addr:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SlbConnAddr'] = []
        if self.slb_conn_addr is not None:
            for k1 in self.slb_conn_addr:
                result['SlbConnAddr'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.slb_conn_addr = []
        if m.get('SlbConnAddr') is not None:
            for k1 in m.get('SlbConnAddr'):
                temp_model = main_models.DescribeClusterConnectionResponseBodySlbConnAddrsSlbConnAddr()
                self.slb_conn_addr.append(temp_model.from_map(k1))

        return self

class DescribeClusterConnectionResponseBodySlbConnAddrsSlbConnAddr(DaraModel):
    def __init__(
        self,
        conn_addr_info: main_models.DescribeClusterConnectionResponseBodySlbConnAddrsSlbConnAddrConnAddrInfo = None,
        slb_type: str = None,
    ):
        self.conn_addr_info = conn_addr_info
        self.slb_type = slb_type

    def validate(self):
        if self.conn_addr_info:
            self.conn_addr_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conn_addr_info is not None:
            result['ConnAddrInfo'] = self.conn_addr_info.to_map()

        if self.slb_type is not None:
            result['SlbType'] = self.slb_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnAddrInfo') is not None:
            temp_model = main_models.DescribeClusterConnectionResponseBodySlbConnAddrsSlbConnAddrConnAddrInfo()
            self.conn_addr_info = temp_model.from_map(m.get('ConnAddrInfo'))

        if m.get('SlbType') is not None:
            self.slb_type = m.get('SlbType')

        return self

class DescribeClusterConnectionResponseBodySlbConnAddrsSlbConnAddrConnAddrInfo(DaraModel):
    def __init__(
        self,
        conn_addr: str = None,
        conn_addr_port: str = None,
        net_type: str = None,
    ):
        self.conn_addr = conn_addr
        self.conn_addr_port = conn_addr_port
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

        if self.net_type is not None:
            result['NetType'] = self.net_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnAddr') is not None:
            self.conn_addr = m.get('ConnAddr')

        if m.get('ConnAddrPort') is not None:
            self.conn_addr_port = m.get('ConnAddrPort')

        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')

        return self

class DescribeClusterConnectionResponseBodyServiceConnAddrs(DaraModel):
    def __init__(
        self,
        service_conn_addr: List[main_models.DescribeClusterConnectionResponseBodyServiceConnAddrsServiceConnAddr] = None,
    ):
        self.service_conn_addr = service_conn_addr

    def validate(self):
        if self.service_conn_addr:
            for v1 in self.service_conn_addr:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ServiceConnAddr'] = []
        if self.service_conn_addr is not None:
            for k1 in self.service_conn_addr:
                result['ServiceConnAddr'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.service_conn_addr = []
        if m.get('ServiceConnAddr') is not None:
            for k1 in m.get('ServiceConnAddr'):
                temp_model = main_models.DescribeClusterConnectionResponseBodyServiceConnAddrsServiceConnAddr()
                self.service_conn_addr.append(temp_model.from_map(k1))

        return self

class DescribeClusterConnectionResponseBodyServiceConnAddrsServiceConnAddr(DaraModel):
    def __init__(
        self,
        conn_addr_info: main_models.DescribeClusterConnectionResponseBodyServiceConnAddrsServiceConnAddrConnAddrInfo = None,
        conn_type: str = None,
    ):
        self.conn_addr_info = conn_addr_info
        self.conn_type = conn_type

    def validate(self):
        if self.conn_addr_info:
            self.conn_addr_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conn_addr_info is not None:
            result['ConnAddrInfo'] = self.conn_addr_info.to_map()

        if self.conn_type is not None:
            result['ConnType'] = self.conn_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnAddrInfo') is not None:
            temp_model = main_models.DescribeClusterConnectionResponseBodyServiceConnAddrsServiceConnAddrConnAddrInfo()
            self.conn_addr_info = temp_model.from_map(m.get('ConnAddrInfo'))

        if m.get('ConnType') is not None:
            self.conn_type = m.get('ConnType')

        return self

class DescribeClusterConnectionResponseBodyServiceConnAddrsServiceConnAddrConnAddrInfo(DaraModel):
    def __init__(
        self,
        conn_addr: str = None,
        conn_addr_port: str = None,
        net_type: str = None,
    ):
        self.conn_addr = conn_addr
        self.conn_addr_port = conn_addr_port
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

        if self.net_type is not None:
            result['NetType'] = self.net_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnAddr') is not None:
            self.conn_addr = m.get('ConnAddr')

        if m.get('ConnAddrPort') is not None:
            self.conn_addr_port = m.get('ConnAddrPort')

        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')

        return self

