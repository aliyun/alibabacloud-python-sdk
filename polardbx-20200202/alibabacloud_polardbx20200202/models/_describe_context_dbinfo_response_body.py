# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardbx20200202 import models as main_models
from darabonba.model import DaraModel

class DescribeContextDBInfoResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: main_models.DescribeContextDBInfoResponseBodyAccessDeniedDetail = None,
        data: main_models.DescribeContextDBInfoResponseBodyData = None,
        request_id: str = None,
    ):
        # The details of the access denial.
        self.access_denied_detail = access_denied_detail
        # The instance data.
        self.data = data
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.access_denied_detail:
            self.access_denied_detail.validate()
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail.to_map()

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            temp_model = main_models.DescribeContextDBInfoResponseBodyAccessDeniedDetail()
            self.access_denied_detail = temp_model.from_map(m.get('AccessDeniedDetail'))

        if m.get('Data') is not None:
            temp_model = main_models.DescribeContextDBInfoResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeContextDBInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        instance: main_models.DescribeContextDBInfoResponseBodyDataInstance = None,
    ):
        # The instance information.
        self.instance = instance

    def validate(self):
        if self.instance:
            self.instance.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance is not None:
            result['Instance'] = self.instance.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Instance') is not None:
            temp_model = main_models.DescribeContextDBInfoResponseBodyDataInstance()
            self.instance = temp_model.from_map(m.get('Instance'))

        return self

class DescribeContextDBInfoResponseBodyDataInstance(DaraModel):
    def __init__(
        self,
        class_code: str = None,
        conn_addrs: List[main_models.DescribeContextDBInfoResponseBodyDataInstanceConnAddrs] = None,
        create_time: str = None,
        dbinstance_name: str = None,
        instance_id: str = None,
        node_count: int = None,
        open_search_instance_name: str = None,
        region_id: str = None,
        replica_sets: List[main_models.DescribeContextDBInfoResponseBodyDataInstanceReplicaSets] = None,
        status: str = None,
        storage_type: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        # The instance specifications.
        self.class_code = class_code
        # The list of endpoints.
        self.conn_addrs = conn_addrs
        # The creation time.
        self.create_time = create_time
        # The database instance name.
        self.dbinstance_name = dbinstance_name
        # The instance ID.
        self.instance_id = instance_id
        # The number of nodes.
        self.node_count = node_count
        # The PolarDB-X Search instance name.
        self.open_search_instance_name = open_search_instance_name
        # The region ID.
        self.region_id = region_id
        # The VPC instance ID of the replica set node.
        # > This parameter is returned only when the network type of the instance is VPC.
        self.replica_sets = replica_sets
        # The instance status.
        self.status = status
        # The storage type.
        self.storage_type = storage_type
        # VPC ID
        self.vpcid = vpcid
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        if self.conn_addrs:
            for v1 in self.conn_addrs:
                 if v1:
                    v1.validate()
        if self.replica_sets:
            for v1 in self.replica_sets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.class_code is not None:
            result['ClassCode'] = self.class_code

        result['ConnAddrs'] = []
        if self.conn_addrs is not None:
            for k1 in self.conn_addrs:
                result['ConnAddrs'].append(k1.to_map() if k1 else None)

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.node_count is not None:
            result['NodeCount'] = self.node_count

        if self.open_search_instance_name is not None:
            result['OpenSearchInstanceName'] = self.open_search_instance_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        result['ReplicaSets'] = []
        if self.replica_sets is not None:
            for k1 in self.replica_sets:
                result['ReplicaSets'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassCode') is not None:
            self.class_code = m.get('ClassCode')

        self.conn_addrs = []
        if m.get('ConnAddrs') is not None:
            for k1 in m.get('ConnAddrs'):
                temp_model = main_models.DescribeContextDBInfoResponseBodyDataInstanceConnAddrs()
                self.conn_addrs.append(temp_model.from_map(k1))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')

        if m.get('OpenSearchInstanceName') is not None:
            self.open_search_instance_name = m.get('OpenSearchInstanceName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        self.replica_sets = []
        if m.get('ReplicaSets') is not None:
            for k1 in m.get('ReplicaSets'):
                temp_model = main_models.DescribeContextDBInfoResponseBodyDataInstanceReplicaSets()
                self.replica_sets.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeContextDBInfoResponseBodyDataInstanceReplicaSets(DaraModel):
    def __init__(
        self,
        class_code: str = None,
        conn_addrs: List[main_models.DescribeContextDBInfoResponseBodyDataInstanceReplicaSetsConnAddrs] = None,
        create_time: str = None,
        instance_id: str = None,
        node_count: int = None,
        node_type: str = None,
        status: str = None,
        storage_type: str = None,
        zone_id: str = None,
    ):
        # The instance specifications.
        self.class_code = class_code
        # The endpoint type.
        self.conn_addrs = conn_addrs
        # The creation time.
        self.create_time = create_time
        # The instance ID.
        self.instance_id = instance_id
        # The number of nodes.
        self.node_count = node_count
        # The target node type: service or dashboard.
        self.node_type = node_type
        # The node status. Valid values:
        # 
        # - **0**: Running.
        # - **1**: Creating.
        # - **2**: Abnormal.
        # - **3**: Expired.
        # - **4**: Releasing.
        # - **5**: Released.
        # - **6**: Locked.
        self.status = status
        # The storage type.
        self.storage_type = storage_type
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        if self.conn_addrs:
            for v1 in self.conn_addrs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.class_code is not None:
            result['ClassCode'] = self.class_code

        result['ConnAddrs'] = []
        if self.conn_addrs is not None:
            for k1 in self.conn_addrs:
                result['ConnAddrs'].append(k1.to_map() if k1 else None)

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.node_count is not None:
            result['NodeCount'] = self.node_count

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassCode') is not None:
            self.class_code = m.get('ClassCode')

        self.conn_addrs = []
        if m.get('ConnAddrs') is not None:
            for k1 in m.get('ConnAddrs'):
                temp_model = main_models.DescribeContextDBInfoResponseBodyDataInstanceReplicaSetsConnAddrs()
                self.conn_addrs.append(temp_model.from_map(k1))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeContextDBInfoResponseBodyDataInstanceReplicaSetsConnAddrs(DaraModel):
    def __init__(
        self,
        connection_string: str = None,
        node_type: str = None,
        port: int = None,
        type: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
        vpc_instance_id: str = None,
    ):
        # The endpoint.
        self.connection_string = connection_string
        # The target node type: service or dashboard.
        self.node_type = node_type
        # The port.
        self.port = port
        # The instance type. Valid values:
        # 
        # - **ReadWrite**: primary instance.
        # - **ReadOnly**: read-only instance.
        self.type = type
        # VPC ID
        self.vpcid = vpcid
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The VPC-connected instance ID.
        self.vpc_instance_id = vpc_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.port is not None:
            result['Port'] = self.port

        if self.type is not None:
            result['Type'] = self.type

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_instance_id is not None:
            result['VpcInstanceId'] = self.vpc_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcInstanceId') is not None:
            self.vpc_instance_id = m.get('VpcInstanceId')

        return self

class DescribeContextDBInfoResponseBodyDataInstanceConnAddrs(DaraModel):
    def __init__(
        self,
        connection_string: str = None,
        node_type: str = None,
        port: int = None,
        type: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
        vpc_instance_id: str = None,
    ):
        # The endpoint.
        self.connection_string = connection_string
        # The target node type: service or dashboard.
        self.node_type = node_type
        # The port.
        self.port = port
        # The endpoint type.
        self.type = type
        # VPC ID
        self.vpcid = vpcid
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The VPC-connected instance ID.
        self.vpc_instance_id = vpc_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.port is not None:
            result['Port'] = self.port

        if self.type is not None:
            result['Type'] = self.type

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_instance_id is not None:
            result['VpcInstanceId'] = self.vpc_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcInstanceId') is not None:
            self.vpc_instance_id = m.get('VpcInstanceId')

        return self

class DescribeContextDBInfoResponseBodyAccessDeniedDetail(DaraModel):
    def __init__(
        self,
        auth_action: str = None,
        auth_principal_display_name: str = None,
        auth_principal_owner_id: str = None,
        auth_principal_type: str = None,
        encoded_diagnostic_message: str = None,
        no_permission_type: str = None,
        policy_type: str = None,
    ):
        # The authentication action.
        self.auth_action = auth_action
        # The display name of the authentication principal.
        self.auth_principal_display_name = auth_principal_display_name
        # The owner ID of the authentication principal.
        self.auth_principal_owner_id = auth_principal_owner_id
        # The authentication principal type.
        self.auth_principal_type = auth_principal_type
        # The diagnostic information.
        self.encoded_diagnostic_message = encoded_diagnostic_message
        # The type of missing permission.
        self.no_permission_type = no_permission_type
        # The policy type.
        self.policy_type = policy_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_action is not None:
            result['AuthAction'] = self.auth_action

        if self.auth_principal_display_name is not None:
            result['AuthPrincipalDisplayName'] = self.auth_principal_display_name

        if self.auth_principal_owner_id is not None:
            result['AuthPrincipalOwnerId'] = self.auth_principal_owner_id

        if self.auth_principal_type is not None:
            result['AuthPrincipalType'] = self.auth_principal_type

        if self.encoded_diagnostic_message is not None:
            result['EncodedDiagnosticMessage'] = self.encoded_diagnostic_message

        if self.no_permission_type is not None:
            result['NoPermissionType'] = self.no_permission_type

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthAction') is not None:
            self.auth_action = m.get('AuthAction')

        if m.get('AuthPrincipalDisplayName') is not None:
            self.auth_principal_display_name = m.get('AuthPrincipalDisplayName')

        if m.get('AuthPrincipalOwnerId') is not None:
            self.auth_principal_owner_id = m.get('AuthPrincipalOwnerId')

        if m.get('AuthPrincipalType') is not None:
            self.auth_principal_type = m.get('AuthPrincipalType')

        if m.get('EncodedDiagnosticMessage') is not None:
            self.encoded_diagnostic_message = m.get('EncodedDiagnosticMessage')

        if m.get('NoPermissionType') is not None:
            self.no_permission_type = m.get('NoPermissionType')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        return self

