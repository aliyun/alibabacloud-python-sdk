# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeApplicationAttributeResponseBody(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        application_type: str = None,
        architecture: str = None,
        components: List[main_models.DescribeApplicationAttributeResponseBodyComponents] = None,
        creation_time: str = None,
        dbcluster_id: str = None,
        description: str = None,
        endpoints: List[main_models.DescribeApplicationAttributeResponseBodyEndpoints] = None,
        expire_time: str = None,
        expired: bool = None,
        lock_mode: str = None,
        maintain_end_time: str = None,
        maintain_start_time: str = None,
        mem_application_attribute: main_models.DescribeApplicationAttributeResponseBodyMemApplicationAttribute = None,
        pay_type: str = None,
        polar_fsinstance_id: str = None,
        region_id: str = None,
        request_id: str = None,
        security_groups: List[main_models.DescribeApplicationAttributeResponseBodySecurityGroups] = None,
        security_iparrays: List[main_models.DescribeApplicationAttributeResponseBodySecurityIPArrays] = None,
        serverless_type: str = None,
        status: str = None,
        upgrade_available: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
        version: str = None,
        zone_id: str = None,
    ):
        self.application_id = application_id
        self.application_type = application_type
        self.architecture = architecture
        self.components = components
        self.creation_time = creation_time
        self.dbcluster_id = dbcluster_id
        self.description = description
        self.endpoints = endpoints
        self.expire_time = expire_time
        self.expired = expired
        self.lock_mode = lock_mode
        self.maintain_end_time = maintain_end_time
        self.maintain_start_time = maintain_start_time
        self.mem_application_attribute = mem_application_attribute
        self.pay_type = pay_type
        self.polar_fsinstance_id = polar_fsinstance_id
        self.region_id = region_id
        self.request_id = request_id
        self.security_groups = security_groups
        self.security_iparrays = security_iparrays
        self.serverless_type = serverless_type
        self.status = status
        self.upgrade_available = upgrade_available
        # VPC ID
        self.vpcid = vpcid
        # VSwitch ID
        self.v_switch_id = v_switch_id
        self.version = version
        self.zone_id = zone_id

    def validate(self):
        if self.components:
            for v1 in self.components:
                 if v1:
                    v1.validate()
        if self.endpoints:
            for v1 in self.endpoints:
                 if v1:
                    v1.validate()
        if self.mem_application_attribute:
            self.mem_application_attribute.validate()
        if self.security_groups:
            for v1 in self.security_groups:
                 if v1:
                    v1.validate()
        if self.security_iparrays:
            for v1 in self.security_iparrays:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.application_type is not None:
            result['ApplicationType'] = self.application_type

        if self.architecture is not None:
            result['Architecture'] = self.architecture

        result['Components'] = []
        if self.components is not None:
            for k1 in self.components:
                result['Components'].append(k1.to_map() if k1 else None)

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.description is not None:
            result['Description'] = self.description

        result['Endpoints'] = []
        if self.endpoints is not None:
            for k1 in self.endpoints:
                result['Endpoints'].append(k1.to_map() if k1 else None)

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.expired is not None:
            result['Expired'] = self.expired

        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode

        if self.maintain_end_time is not None:
            result['MaintainEndTime'] = self.maintain_end_time

        if self.maintain_start_time is not None:
            result['MaintainStartTime'] = self.maintain_start_time

        if self.mem_application_attribute is not None:
            result['MemApplicationAttribute'] = self.mem_application_attribute.to_map()

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.polar_fsinstance_id is not None:
            result['PolarFSInstanceId'] = self.polar_fsinstance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SecurityGroups'] = []
        if self.security_groups is not None:
            for k1 in self.security_groups:
                result['SecurityGroups'].append(k1.to_map() if k1 else None)

        result['SecurityIPArrays'] = []
        if self.security_iparrays is not None:
            for k1 in self.security_iparrays:
                result['SecurityIPArrays'].append(k1.to_map() if k1 else None)

        if self.serverless_type is not None:
            result['ServerlessType'] = self.serverless_type

        if self.status is not None:
            result['Status'] = self.status

        if self.upgrade_available is not None:
            result['UpgradeAvailable'] = self.upgrade_available

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.version is not None:
            result['Version'] = self.version

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')

        if m.get('Architecture') is not None:
            self.architecture = m.get('Architecture')

        self.components = []
        if m.get('Components') is not None:
            for k1 in m.get('Components'):
                temp_model = main_models.DescribeApplicationAttributeResponseBodyComponents()
                self.components.append(temp_model.from_map(k1))

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.endpoints = []
        if m.get('Endpoints') is not None:
            for k1 in m.get('Endpoints'):
                temp_model = main_models.DescribeApplicationAttributeResponseBodyEndpoints()
                self.endpoints.append(temp_model.from_map(k1))

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('Expired') is not None:
            self.expired = m.get('Expired')

        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')

        if m.get('MaintainEndTime') is not None:
            self.maintain_end_time = m.get('MaintainEndTime')

        if m.get('MaintainStartTime') is not None:
            self.maintain_start_time = m.get('MaintainStartTime')

        if m.get('MemApplicationAttribute') is not None:
            temp_model = main_models.DescribeApplicationAttributeResponseBodyMemApplicationAttribute()
            self.mem_application_attribute = temp_model.from_map(m.get('MemApplicationAttribute'))

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('PolarFSInstanceId') is not None:
            self.polar_fsinstance_id = m.get('PolarFSInstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.security_groups = []
        if m.get('SecurityGroups') is not None:
            for k1 in m.get('SecurityGroups'):
                temp_model = main_models.DescribeApplicationAttributeResponseBodySecurityGroups()
                self.security_groups.append(temp_model.from_map(k1))

        self.security_iparrays = []
        if m.get('SecurityIPArrays') is not None:
            for k1 in m.get('SecurityIPArrays'):
                temp_model = main_models.DescribeApplicationAttributeResponseBodySecurityIPArrays()
                self.security_iparrays.append(temp_model.from_map(k1))

        if m.get('ServerlessType') is not None:
            self.serverless_type = m.get('ServerlessType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpgradeAvailable') is not None:
            self.upgrade_available = m.get('UpgradeAvailable')

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeApplicationAttributeResponseBodySecurityIPArrays(DaraModel):
    def __init__(
        self,
        security_iparray_name: str = None,
        security_iparray_tag: str = None,
        security_iplist: str = None,
        security_ipnet_type: str = None,
        security_iptype: str = None,
    ):
        self.security_iparray_name = security_iparray_name
        self.security_iparray_tag = security_iparray_tag
        self.security_iplist = security_iplist
        self.security_ipnet_type = security_ipnet_type
        self.security_iptype = security_iptype

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.security_iparray_name is not None:
            result['SecurityIPArrayName'] = self.security_iparray_name

        if self.security_iparray_tag is not None:
            result['SecurityIPArrayTag'] = self.security_iparray_tag

        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist

        if self.security_ipnet_type is not None:
            result['SecurityIPNetType'] = self.security_ipnet_type

        if self.security_iptype is not None:
            result['SecurityIPType'] = self.security_iptype

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityIPArrayName') is not None:
            self.security_iparray_name = m.get('SecurityIPArrayName')

        if m.get('SecurityIPArrayTag') is not None:
            self.security_iparray_tag = m.get('SecurityIPArrayTag')

        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')

        if m.get('SecurityIPNetType') is not None:
            self.security_ipnet_type = m.get('SecurityIPNetType')

        if m.get('SecurityIPType') is not None:
            self.security_iptype = m.get('SecurityIPType')

        return self

class DescribeApplicationAttributeResponseBodySecurityGroups(DaraModel):
    def __init__(
        self,
        net_type: str = None,
        region_id: str = None,
        security_group_id: str = None,
        security_group_name: str = None,
    ):
        self.net_type = net_type
        self.region_id = region_id
        self.security_group_id = security_group_id
        self.security_group_name = security_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.net_type is not None:
            result['NetType'] = self.net_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.security_group_name is not None:
            result['SecurityGroupName'] = self.security_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('SecurityGroupName') is not None:
            self.security_group_name = m.get('SecurityGroupName')

        return self

class DescribeApplicationAttributeResponseBodyMemApplicationAttribute(DaraModel):
    def __init__(
        self,
        db_name: str = None,
        embedder_model_name: str = None,
        llm_model_name: str = None,
        project_name: str = None,
        reranker_model_name: str = None,
        user_name: str = None,
    ):
        self.db_name = db_name
        self.embedder_model_name = embedder_model_name
        self.llm_model_name = llm_model_name
        self.project_name = project_name
        self.reranker_model_name = reranker_model_name
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_name is not None:
            result['DbName'] = self.db_name

        if self.embedder_model_name is not None:
            result['EmbedderModelName'] = self.embedder_model_name

        if self.llm_model_name is not None:
            result['LlmModelName'] = self.llm_model_name

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.reranker_model_name is not None:
            result['RerankerModelName'] = self.reranker_model_name

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

        if m.get('EmbedderModelName') is not None:
            self.embedder_model_name = m.get('EmbedderModelName')

        if m.get('LlmModelName') is not None:
            self.llm_model_name = m.get('LlmModelName')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('RerankerModelName') is not None:
            self.reranker_model_name = m.get('RerankerModelName')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

class DescribeApplicationAttributeResponseBodyEndpoints(DaraModel):
    def __init__(
        self,
        description: str = None,
        endpoint_id: str = None,
        ip: str = None,
        net_type: str = None,
        port: str = None,
        port_description: str = None,
    ):
        self.description = description
        self.endpoint_id = endpoint_id
        self.ip = ip
        self.net_type = net_type
        self.port = port
        self.port_description = port_description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id

        if self.ip is not None:
            result['IP'] = self.ip

        if self.net_type is not None:
            result['NetType'] = self.net_type

        if self.port is not None:
            result['Port'] = self.port

        if self.port_description is not None:
            result['PortDescription'] = self.port_description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')

        if m.get('IP') is not None:
            self.ip = m.get('IP')

        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('PortDescription') is not None:
            self.port_description = m.get('PortDescription')

        return self

class DescribeApplicationAttributeResponseBodyComponents(DaraModel):
    def __init__(
        self,
        component_class: str = None,
        component_class_description: str = None,
        component_id: str = None,
        component_max_replica: int = None,
        component_replica: int = None,
        component_replica_group_name: str = None,
        component_type: str = None,
        security_groups: List[main_models.DescribeApplicationAttributeResponseBodyComponentsSecurityGroups] = None,
        security_iparrays: List[main_models.DescribeApplicationAttributeResponseBodyComponentsSecurityIPArrays] = None,
        status: str = None,
        topology: main_models.DescribeApplicationAttributeResponseBodyComponentsTopology = None,
    ):
        self.component_class = component_class
        self.component_class_description = component_class_description
        self.component_id = component_id
        self.component_max_replica = component_max_replica
        self.component_replica = component_replica
        self.component_replica_group_name = component_replica_group_name
        self.component_type = component_type
        self.security_groups = security_groups
        self.security_iparrays = security_iparrays
        self.status = status
        self.topology = topology

    def validate(self):
        if self.security_groups:
            for v1 in self.security_groups:
                 if v1:
                    v1.validate()
        if self.security_iparrays:
            for v1 in self.security_iparrays:
                 if v1:
                    v1.validate()
        if self.topology:
            self.topology.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_class is not None:
            result['ComponentClass'] = self.component_class

        if self.component_class_description is not None:
            result['ComponentClassDescription'] = self.component_class_description

        if self.component_id is not None:
            result['ComponentId'] = self.component_id

        if self.component_max_replica is not None:
            result['ComponentMaxReplica'] = self.component_max_replica

        if self.component_replica is not None:
            result['ComponentReplica'] = self.component_replica

        if self.component_replica_group_name is not None:
            result['ComponentReplicaGroupName'] = self.component_replica_group_name

        if self.component_type is not None:
            result['ComponentType'] = self.component_type

        result['SecurityGroups'] = []
        if self.security_groups is not None:
            for k1 in self.security_groups:
                result['SecurityGroups'].append(k1.to_map() if k1 else None)

        result['SecurityIPArrays'] = []
        if self.security_iparrays is not None:
            for k1 in self.security_iparrays:
                result['SecurityIPArrays'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        if self.topology is not None:
            result['Topology'] = self.topology.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentClass') is not None:
            self.component_class = m.get('ComponentClass')

        if m.get('ComponentClassDescription') is not None:
            self.component_class_description = m.get('ComponentClassDescription')

        if m.get('ComponentId') is not None:
            self.component_id = m.get('ComponentId')

        if m.get('ComponentMaxReplica') is not None:
            self.component_max_replica = m.get('ComponentMaxReplica')

        if m.get('ComponentReplica') is not None:
            self.component_replica = m.get('ComponentReplica')

        if m.get('ComponentReplicaGroupName') is not None:
            self.component_replica_group_name = m.get('ComponentReplicaGroupName')

        if m.get('ComponentType') is not None:
            self.component_type = m.get('ComponentType')

        self.security_groups = []
        if m.get('SecurityGroups') is not None:
            for k1 in m.get('SecurityGroups'):
                temp_model = main_models.DescribeApplicationAttributeResponseBodyComponentsSecurityGroups()
                self.security_groups.append(temp_model.from_map(k1))

        self.security_iparrays = []
        if m.get('SecurityIPArrays') is not None:
            for k1 in m.get('SecurityIPArrays'):
                temp_model = main_models.DescribeApplicationAttributeResponseBodyComponentsSecurityIPArrays()
                self.security_iparrays.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Topology') is not None:
            temp_model = main_models.DescribeApplicationAttributeResponseBodyComponentsTopology()
            self.topology = temp_model.from_map(m.get('Topology'))

        return self

class DescribeApplicationAttributeResponseBodyComponentsTopology(DaraModel):
    def __init__(
        self,
        children: List[str] = None,
        layer: str = None,
        parents: List[str] = None,
    ):
        self.children = children
        self.layer = layer
        self.parents = parents

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.children is not None:
            result['Children'] = self.children

        if self.layer is not None:
            result['Layer'] = self.layer

        if self.parents is not None:
            result['Parents'] = self.parents

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Children') is not None:
            self.children = m.get('Children')

        if m.get('Layer') is not None:
            self.layer = m.get('Layer')

        if m.get('Parents') is not None:
            self.parents = m.get('Parents')

        return self

class DescribeApplicationAttributeResponseBodyComponentsSecurityIPArrays(DaraModel):
    def __init__(
        self,
        security_iparray_name: str = None,
        security_iparray_tag: str = None,
        security_iplist: str = None,
        security_ipnet_type: str = None,
        security_iptype: str = None,
    ):
        self.security_iparray_name = security_iparray_name
        self.security_iparray_tag = security_iparray_tag
        self.security_iplist = security_iplist
        self.security_ipnet_type = security_ipnet_type
        self.security_iptype = security_iptype

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.security_iparray_name is not None:
            result['SecurityIPArrayName'] = self.security_iparray_name

        if self.security_iparray_tag is not None:
            result['SecurityIPArrayTag'] = self.security_iparray_tag

        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist

        if self.security_ipnet_type is not None:
            result['SecurityIPNetType'] = self.security_ipnet_type

        if self.security_iptype is not None:
            result['SecurityIPType'] = self.security_iptype

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityIPArrayName') is not None:
            self.security_iparray_name = m.get('SecurityIPArrayName')

        if m.get('SecurityIPArrayTag') is not None:
            self.security_iparray_tag = m.get('SecurityIPArrayTag')

        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')

        if m.get('SecurityIPNetType') is not None:
            self.security_ipnet_type = m.get('SecurityIPNetType')

        if m.get('SecurityIPType') is not None:
            self.security_iptype = m.get('SecurityIPType')

        return self

class DescribeApplicationAttributeResponseBodyComponentsSecurityGroups(DaraModel):
    def __init__(
        self,
        net_type: str = None,
        region_id: str = None,
        security_group_id: str = None,
        security_group_name: str = None,
    ):
        self.net_type = net_type
        self.region_id = region_id
        self.security_group_id = security_group_id
        self.security_group_name = security_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.net_type is not None:
            result['NetType'] = self.net_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.security_group_name is not None:
            result['SecurityGroupName'] = self.security_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('SecurityGroupName') is not None:
            self.security_group_name = m.get('SecurityGroupName')

        return self

