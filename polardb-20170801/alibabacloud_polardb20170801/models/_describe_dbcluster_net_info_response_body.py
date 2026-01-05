# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeDBClusterNetInfoResponseBody(DaraModel):
    def __init__(
        self,
        cluster_network_type: str = None,
        dbcluster_net_infos: main_models.DescribeDBClusterNetInfoResponseBodyDBClusterNetInfos = None,
        dbnode_net_infos: main_models.DescribeDBClusterNetInfoResponseBodyDBNodeNetInfos = None,
        request_id: str = None,
    ):
        self.cluster_network_type = cluster_network_type
        self.dbcluster_net_infos = dbcluster_net_infos
        self.dbnode_net_infos = dbnode_net_infos
        self.request_id = request_id

    def validate(self):
        if self.dbcluster_net_infos:
            self.dbcluster_net_infos.validate()
        if self.dbnode_net_infos:
            self.dbnode_net_infos.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_network_type is not None:
            result['ClusterNetworkType'] = self.cluster_network_type

        if self.dbcluster_net_infos is not None:
            result['DBClusterNetInfos'] = self.dbcluster_net_infos.to_map()

        if self.dbnode_net_infos is not None:
            result['DBNodeNetInfos'] = self.dbnode_net_infos.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterNetworkType') is not None:
            self.cluster_network_type = m.get('ClusterNetworkType')

        if m.get('DBClusterNetInfos') is not None:
            temp_model = main_models.DescribeDBClusterNetInfoResponseBodyDBClusterNetInfos()
            self.dbcluster_net_infos = temp_model.from_map(m.get('DBClusterNetInfos'))

        if m.get('DBNodeNetInfos') is not None:
            temp_model = main_models.DescribeDBClusterNetInfoResponseBodyDBNodeNetInfos()
            self.dbnode_net_infos = temp_model.from_map(m.get('DBNodeNetInfos'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDBClusterNetInfoResponseBodyDBNodeNetInfos(DaraModel):
    def __init__(
        self,
        dbnode_net_info: List[main_models.DescribeDBClusterNetInfoResponseBodyDBNodeNetInfosDBNodeNetInfo] = None,
    ):
        self.dbnode_net_info = dbnode_net_info

    def validate(self):
        if self.dbnode_net_info:
            for v1 in self.dbnode_net_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DBNodeNetInfo'] = []
        if self.dbnode_net_info is not None:
            for k1 in self.dbnode_net_info:
                result['DBNodeNetInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbnode_net_info = []
        if m.get('DBNodeNetInfo') is not None:
            for k1 in m.get('DBNodeNetInfo'):
                temp_model = main_models.DescribeDBClusterNetInfoResponseBodyDBNodeNetInfosDBNodeNetInfo()
                self.dbnode_net_info.append(temp_model.from_map(k1))

        return self

class DescribeDBClusterNetInfoResponseBodyDBNodeNetInfosDBNodeNetInfo(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        dbnode_role: str = None,
        net_infos: main_models.DescribeDBClusterNetInfoResponseBodyDBNodeNetInfosDBNodeNetInfoNetInfos = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.dbnode_role = dbnode_role
        self.net_infos = net_infos

    def validate(self):
        if self.net_infos:
            self.net_infos.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dbnode_role is not None:
            result['DBNodeRole'] = self.dbnode_role

        if self.net_infos is not None:
            result['NetInfos'] = self.net_infos.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DBNodeRole') is not None:
            self.dbnode_role = m.get('DBNodeRole')

        if m.get('NetInfos') is not None:
            temp_model = main_models.DescribeDBClusterNetInfoResponseBodyDBNodeNetInfosDBNodeNetInfoNetInfos()
            self.net_infos = temp_model.from_map(m.get('NetInfos'))

        return self

class DescribeDBClusterNetInfoResponseBodyDBNodeNetInfosDBNodeNetInfoNetInfos(DaraModel):
    def __init__(
        self,
        net_info: List[main_models.DescribeDBClusterNetInfoResponseBodyDBNodeNetInfosDBNodeNetInfoNetInfosNetInfo] = None,
    ):
        self.net_info = net_info

    def validate(self):
        if self.net_info:
            for v1 in self.net_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NetInfo'] = []
        if self.net_info is not None:
            for k1 in self.net_info:
                result['NetInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.net_info = []
        if m.get('NetInfo') is not None:
            for k1 in m.get('NetInfo'):
                temp_model = main_models.DescribeDBClusterNetInfoResponseBodyDBNodeNetInfosDBNodeNetInfoNetInfosNetInfo()
                self.net_info.append(temp_model.from_map(k1))

        return self

class DescribeDBClusterNetInfoResponseBodyDBNodeNetInfosDBNodeNetInfoNetInfosNetInfo(DaraModel):
    def __init__(
        self,
        connection_string: str = None,
        ipaddress: str = None,
        iptype: str = None,
        port: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
    ):
        self.connection_string = connection_string
        self.ipaddress = ipaddress
        self.iptype = iptype
        self.port = port
        self.vpcid = vpcid
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string

        if self.ipaddress is not None:
            result['IPAddress'] = self.ipaddress

        if self.iptype is not None:
            result['IPType'] = self.iptype

        if self.port is not None:
            result['Port'] = self.port

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('IPAddress') is not None:
            self.ipaddress = m.get('IPAddress')

        if m.get('IPType') is not None:
            self.iptype = m.get('IPType')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

class DescribeDBClusterNetInfoResponseBodyDBClusterNetInfos(DaraModel):
    def __init__(
        self,
        dbcluster_net_info: List[main_models.DescribeDBClusterNetInfoResponseBodyDBClusterNetInfosDBClusterNetInfo] = None,
    ):
        self.dbcluster_net_info = dbcluster_net_info

    def validate(self):
        if self.dbcluster_net_info:
            for v1 in self.dbcluster_net_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DBClusterNetInfo'] = []
        if self.dbcluster_net_info is not None:
            for k1 in self.dbcluster_net_info:
                result['DBClusterNetInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbcluster_net_info = []
        if m.get('DBClusterNetInfo') is not None:
            for k1 in m.get('DBClusterNetInfo'):
                temp_model = main_models.DescribeDBClusterNetInfoResponseBodyDBClusterNetInfosDBClusterNetInfo()
                self.dbcluster_net_info.append(temp_model.from_map(k1))

        return self

class DescribeDBClusterNetInfoResponseBodyDBClusterNetInfosDBClusterNetInfo(DaraModel):
    def __init__(
        self,
        connection_string: str = None,
        connection_string_type: str = None,
        ipaddress: str = None,
        iptype: str = None,
        port: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
    ):
        self.connection_string = connection_string
        self.connection_string_type = connection_string_type
        self.ipaddress = ipaddress
        self.iptype = iptype
        self.port = port
        self.vpcid = vpcid
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string

        if self.connection_string_type is not None:
            result['ConnectionStringType'] = self.connection_string_type

        if self.ipaddress is not None:
            result['IPAddress'] = self.ipaddress

        if self.iptype is not None:
            result['IPType'] = self.iptype

        if self.port is not None:
            result['Port'] = self.port

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('ConnectionStringType') is not None:
            self.connection_string_type = m.get('ConnectionStringType')

        if m.get('IPAddress') is not None:
            self.ipaddress = m.get('IPAddress')

        if m.get('IPType') is not None:
            self.iptype = m.get('IPType')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

