# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeDBInstanceNetInfoResponseBody(DaraModel):
    def __init__(
        self,
        dbinstance_net_infos: main_models.DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfos = None,
        instance_network_type: str = None,
        request_id: str = None,
        security_ipmode: str = None,
    ):
        # The information about the endpoints of the instance.
        self.dbinstance_net_infos = dbinstance_net_infos
        # The network type of the instance. Valid values:
        # 
        # *   **Classic**: classic network
        # *   **VPC**: virtual private cloud (VPC)
        self.instance_network_type = instance_network_type
        # The ID of the request.
        self.request_id = request_id
        # The whitelist mode of the instance. Valid values:
        # 
        # *   **normal**: standard whitelist mode
        # *   **safety**: enhanced whitelist mode
        self.security_ipmode = security_ipmode

    def validate(self):
        if self.dbinstance_net_infos:
            self.dbinstance_net_infos.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_net_infos is not None:
            result['DBInstanceNetInfos'] = self.dbinstance_net_infos.to_map()

        if self.instance_network_type is not None:
            result['InstanceNetworkType'] = self.instance_network_type

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.security_ipmode is not None:
            result['SecurityIPMode'] = self.security_ipmode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceNetInfos') is not None:
            temp_model = main_models.DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfos()
            self.dbinstance_net_infos = temp_model.from_map(m.get('DBInstanceNetInfos'))

        if m.get('InstanceNetworkType') is not None:
            self.instance_network_type = m.get('InstanceNetworkType')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SecurityIPMode') is not None:
            self.security_ipmode = m.get('SecurityIPMode')

        return self

class DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfos(DaraModel):
    def __init__(
        self,
        dbinstance_net_info: List[main_models.DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfosDBInstanceNetInfo] = None,
    ):
        self.dbinstance_net_info = dbinstance_net_info

    def validate(self):
        if self.dbinstance_net_info:
            for v1 in self.dbinstance_net_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DBInstanceNetInfo'] = []
        if self.dbinstance_net_info is not None:
            for k1 in self.dbinstance_net_info:
                result['DBInstanceNetInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbinstance_net_info = []
        if m.get('DBInstanceNetInfo') is not None:
            for k1 in m.get('DBInstanceNetInfo'):
                temp_model = main_models.DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfosDBInstanceNetInfo()
                self.dbinstance_net_info.append(temp_model.from_map(k1))

        return self

class DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfosDBInstanceNetInfo(DaraModel):
    def __init__(
        self,
        babelfish_port: str = None,
        connection_string: str = None,
        connection_string_type: str = None,
        dbinstance_weights: main_models.DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfosDBInstanceNetInfoDBInstanceWeights = None,
        distribution_type: str = None,
        expired_time: str = None,
        ipaddress: str = None,
        iptype: str = None,
        max_delay_time: str = None,
        pgbouncer_port: str = None,
        port: str = None,
        security_ipgroups: main_models.DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfosDBInstanceNetInfoSecurityIPGroups = None,
        upgradeable: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
    ):
        # The Tabular Data Stream (TDS) port of the instance for which Babelfish is enabled.
        # 
        # >  This parameter applies only to ApsaraDB RDS for PostgreSQL instances. For more information about Babelfish for ApsaraDB RDS for PostgreSQL, see [Introduction to Babelfish](https://help.aliyun.com/document_detail/428613.html).
        self.babelfish_port = babelfish_port
        # The endpoint of the instance.
        self.connection_string = connection_string
        # The type of the endpoint. Valid values:
        # 
        # *   **Normal**: a regular endpoint
        # *   **ReadWriteSplitting**: a read/write splitting endpoint
        self.connection_string_type = connection_string_type
        # The information about the instance weight.
        # 
        # >  This parameter is returned only when the read/write splitting feature is enabled for the instance.
        self.dbinstance_weights = dbinstance_weights
        # The policy that is used to assign read weights. This parameter is returned only for a read/write splitting endpoint. Valid values:
        # 
        # *   **Standard**: The system automatically allocates read weights to the instance and its read-only instances based on the specifications of the instances.
        # *   **Custom**: You must manually allocate read weights to the instance and its read-only instances.
        self.distribution_type = distribution_type
        # The remaining validity period of the instance in the classic network in hybrid access mode. Unit: seconds.
        self.expired_time = expired_time
        # The IP address.
        self.ipaddress = ipaddress
        # The network type.
        # 
        # *   Valid values when the instance resides in the classic network:
        # 
        #     *   **Inner**
        #     *   **Public**
        # 
        # *   Valid values when the instance resides in a virtual private cloud (VPC):
        # 
        #     *   **Private**
        #     *   **Public**
        self.iptype = iptype
        # The latency threshold. This parameter is returned only for a read/write splitting endpoint. Unit: seconds.
        # 
        # >  If the latency on a read-only instance exceeds the specified threshold, ApsaraDB RDS no longer forwards read requests to the read-only instance.
        self.max_delay_time = max_delay_time
        # The PgBouncer port.
        # 
        # >  This parameter is returned only when PgBouncer is enabled for the instance that runs PostgreSQL.
        self.pgbouncer_port = pgbouncer_port
        # The port that is used to connect to the instance.
        self.port = port
        # The IP addresses in the whitelist for the instance.
        self.security_ipgroups = security_ipgroups
        # Indicates whether the IP version can be updated. Valid values:
        # 
        # *   **Enable**
        # *   **Disabled**
        # 
        # >  The IP version can be updated from IPv4 to IPv6.
        self.upgradeable = upgradeable
        # The VPC ID of the instance.
        self.vpcid = vpcid
        # The vSwitch ID.
        self.v_switch_id = v_switch_id

    def validate(self):
        if self.dbinstance_weights:
            self.dbinstance_weights.validate()
        if self.security_ipgroups:
            self.security_ipgroups.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.babelfish_port is not None:
            result['BabelfishPort'] = self.babelfish_port

        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string

        if self.connection_string_type is not None:
            result['ConnectionStringType'] = self.connection_string_type

        if self.dbinstance_weights is not None:
            result['DBInstanceWeights'] = self.dbinstance_weights.to_map()

        if self.distribution_type is not None:
            result['DistributionType'] = self.distribution_type

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.ipaddress is not None:
            result['IPAddress'] = self.ipaddress

        if self.iptype is not None:
            result['IPType'] = self.iptype

        if self.max_delay_time is not None:
            result['MaxDelayTime'] = self.max_delay_time

        if self.pgbouncer_port is not None:
            result['PGBouncerPort'] = self.pgbouncer_port

        if self.port is not None:
            result['Port'] = self.port

        if self.security_ipgroups is not None:
            result['SecurityIPGroups'] = self.security_ipgroups.to_map()

        if self.upgradeable is not None:
            result['Upgradeable'] = self.upgradeable

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BabelfishPort') is not None:
            self.babelfish_port = m.get('BabelfishPort')

        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('ConnectionStringType') is not None:
            self.connection_string_type = m.get('ConnectionStringType')

        if m.get('DBInstanceWeights') is not None:
            temp_model = main_models.DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfosDBInstanceNetInfoDBInstanceWeights()
            self.dbinstance_weights = temp_model.from_map(m.get('DBInstanceWeights'))

        if m.get('DistributionType') is not None:
            self.distribution_type = m.get('DistributionType')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('IPAddress') is not None:
            self.ipaddress = m.get('IPAddress')

        if m.get('IPType') is not None:
            self.iptype = m.get('IPType')

        if m.get('MaxDelayTime') is not None:
            self.max_delay_time = m.get('MaxDelayTime')

        if m.get('PGBouncerPort') is not None:
            self.pgbouncer_port = m.get('PGBouncerPort')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('SecurityIPGroups') is not None:
            temp_model = main_models.DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfosDBInstanceNetInfoSecurityIPGroups()
            self.security_ipgroups = temp_model.from_map(m.get('SecurityIPGroups'))

        if m.get('Upgradeable') is not None:
            self.upgradeable = m.get('Upgradeable')

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

class DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfosDBInstanceNetInfoSecurityIPGroups(DaraModel):
    def __init__(
        self,
        security_ipgroup: List[main_models.DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfosDBInstanceNetInfoSecurityIPGroupsSecurityIPGroup] = None,
    ):
        self.security_ipgroup = security_ipgroup

    def validate(self):
        if self.security_ipgroup:
            for v1 in self.security_ipgroup:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['securityIPGroup'] = []
        if self.security_ipgroup is not None:
            for k1 in self.security_ipgroup:
                result['securityIPGroup'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.security_ipgroup = []
        if m.get('securityIPGroup') is not None:
            for k1 in m.get('securityIPGroup'):
                temp_model = main_models.DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfosDBInstanceNetInfoSecurityIPGroupsSecurityIPGroup()
                self.security_ipgroup.append(temp_model.from_map(k1))

        return self

class DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfosDBInstanceNetInfoSecurityIPGroupsSecurityIPGroup(DaraModel):
    def __init__(
        self,
        security_ipgroup_name: str = None,
        security_ips: str = None,
    ):
        # The name of the IP address whitelist.
        self.security_ipgroup_name = security_ipgroup_name
        # The IP address in the whitelist.
        self.security_ips = security_ips

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.security_ipgroup_name is not None:
            result['SecurityIPGroupName'] = self.security_ipgroup_name

        if self.security_ips is not None:
            result['SecurityIPs'] = self.security_ips

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityIPGroupName') is not None:
            self.security_ipgroup_name = m.get('SecurityIPGroupName')

        if m.get('SecurityIPs') is not None:
            self.security_ips = m.get('SecurityIPs')

        return self

class DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfosDBInstanceNetInfoDBInstanceWeights(DaraModel):
    def __init__(
        self,
        dbinstance_weight: List[main_models.DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfosDBInstanceNetInfoDBInstanceWeightsDBInstanceWeight] = None,
    ):
        self.dbinstance_weight = dbinstance_weight

    def validate(self):
        if self.dbinstance_weight:
            for v1 in self.dbinstance_weight:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DBInstanceWeight'] = []
        if self.dbinstance_weight is not None:
            for k1 in self.dbinstance_weight:
                result['DBInstanceWeight'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbinstance_weight = []
        if m.get('DBInstanceWeight') is not None:
            for k1 in m.get('DBInstanceWeight'):
                temp_model = main_models.DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfosDBInstanceNetInfoDBInstanceWeightsDBInstanceWeight()
                self.dbinstance_weight.append(temp_model.from_map(k1))

        return self

class DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfosDBInstanceNetInfoDBInstanceWeightsDBInstanceWeight(DaraModel):
    def __init__(
        self,
        availability: str = None,
        dbinstance_id: str = None,
        dbinstance_type: str = None,
        role: str = None,
        weight: str = None,
    ):
        # The availability of the instance. Valid values:
        # 
        # *   **Unavailable**
        # *   **Available**
        self.availability = availability
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        # The type of the instance. Valid values:
        # 
        # *   **Master**: primary instance
        # *   **Readonly**: read-only instance
        self.dbinstance_type = dbinstance_type
        # A deprecated parameter.
        self.role = role
        # The weight of the instance.
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.availability is not None:
            result['Availability'] = self.availability

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dbinstance_type is not None:
            result['DBInstanceType'] = self.dbinstance_type

        if self.role is not None:
            result['Role'] = self.role

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Availability') is not None:
            self.availability = m.get('Availability')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DBInstanceType') is not None:
            self.dbinstance_type = m.get('DBInstanceType')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

