# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardbx20200202 import models as main_models
from darabonba.model import DaraModel

class DescribeSupabaseInstanceAttributeResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: main_models.DescribeSupabaseInstanceAttributeResponseBodyAccessDeniedDetail = None,
        data: main_models.DescribeSupabaseInstanceAttributeResponseBodyData = None,
        request_id: str = None,
    ):
        # The details of the access denial.
        self.access_denied_detail = access_denied_detail
        # The instance details.
        self.data = data
        # The request ID.
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
            temp_model = main_models.DescribeSupabaseInstanceAttributeResponseBodyAccessDeniedDetail()
            self.access_denied_detail = temp_model.from_map(m.get('AccessDeniedDetail'))

        if m.get('Data') is not None:
            temp_model = main_models.DescribeSupabaseInstanceAttributeResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeSupabaseInstanceAttributeResponseBodyData(DaraModel):
    def __init__(
        self,
        conn_addrs: List[main_models.DescribeSupabaseInstanceAttributeResponseBodyDataConnAddrs] = None,
        create_time: str = None,
        dbinstance_name: str = None,
        engine_version: str = None,
        expired: bool = None,
        lock_mode: str = None,
        minor_version: str = None,
        node_class: str = None,
        node_count: int = None,
        nodes: List[main_models.DescribeSupabaseInstanceAttributeResponseBodyDataNodes] = None,
        polar_dbxdbinstance_name: str = None,
        region_id: str = None,
        status: str = None,
        supabase_class_code: str = None,
        tenant_mode: bool = None,
        topology_type: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # The list of endpoints.
        self.conn_addrs = conn_addrs
        # The time when the instance was created.
        self.create_time = create_time
        # The instance name.
        self.dbinstance_name = dbinstance_name
        # The database engine version.
        self.engine_version = engine_version
        # Indicates whether the instance has expired.
        self.expired = expired
        # The lock mode.
        self.lock_mode = lock_mode
        # The minor engine version.
        self.minor_version = minor_version
        # The node specifications.
        self.node_class = node_class
        # The number of nodes.
        self.node_count = node_count
        # The list of nodes.
        self.nodes = nodes
        # The name of the associated PolarDB-X instance.
        self.polar_dbxdbinstance_name = polar_dbxdbinstance_name
        # The region ID.
        self.region_id = region_id
        # The instance status.
        self.status = status
        # The Supabase class code.
        self.supabase_class_code = supabase_class_code
        # The multi-tenant mode.
        self.tenant_mode = tenant_mode
        # The topology type.
        self.topology_type = topology_type
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # VPC ID
        self.vpc_id = vpc_id
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        if self.conn_addrs:
            for v1 in self.conn_addrs:
                 if v1:
                    v1.validate()
        if self.nodes:
            for v1 in self.nodes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ConnAddrs'] = []
        if self.conn_addrs is not None:
            for k1 in self.conn_addrs:
                result['ConnAddrs'].append(k1.to_map() if k1 else None)

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.expired is not None:
            result['Expired'] = self.expired

        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode

        if self.minor_version is not None:
            result['MinorVersion'] = self.minor_version

        if self.node_class is not None:
            result['NodeClass'] = self.node_class

        if self.node_count is not None:
            result['NodeCount'] = self.node_count

        result['Nodes'] = []
        if self.nodes is not None:
            for k1 in self.nodes:
                result['Nodes'].append(k1.to_map() if k1 else None)

        if self.polar_dbxdbinstance_name is not None:
            result['PolarDBXDBInstanceName'] = self.polar_dbxdbinstance_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        if self.supabase_class_code is not None:
            result['SupabaseClassCode'] = self.supabase_class_code

        if self.tenant_mode is not None:
            result['TenantMode'] = self.tenant_mode

        if self.topology_type is not None:
            result['TopologyType'] = self.topology_type

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conn_addrs = []
        if m.get('ConnAddrs') is not None:
            for k1 in m.get('ConnAddrs'):
                temp_model = main_models.DescribeSupabaseInstanceAttributeResponseBodyDataConnAddrs()
                self.conn_addrs.append(temp_model.from_map(k1))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('Expired') is not None:
            self.expired = m.get('Expired')

        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')

        if m.get('MinorVersion') is not None:
            self.minor_version = m.get('MinorVersion')

        if m.get('NodeClass') is not None:
            self.node_class = m.get('NodeClass')

        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')

        self.nodes = []
        if m.get('Nodes') is not None:
            for k1 in m.get('Nodes'):
                temp_model = main_models.DescribeSupabaseInstanceAttributeResponseBodyDataNodes()
                self.nodes.append(temp_model.from_map(k1))

        if m.get('PolarDBXDBInstanceName') is not None:
            self.polar_dbxdbinstance_name = m.get('PolarDBXDBInstanceName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SupabaseClassCode') is not None:
            self.supabase_class_code = m.get('SupabaseClassCode')

        if m.get('TenantMode') is not None:
            self.tenant_mode = m.get('TenantMode')

        if m.get('TopologyType') is not None:
            self.topology_type = m.get('TopologyType')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeSupabaseInstanceAttributeResponseBodyDataNodes(DaraModel):
    def __init__(
        self,
        class_code: str = None,
        id: str = None,
        name: str = None,
        zone_id: str = None,
    ):
        # The class code.
        self.class_code = class_code
        # The node ID.
        self.id = id
        # The node name.
        self.name = name
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.class_code is not None:
            result['ClassCode'] = self.class_code

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassCode') is not None:
            self.class_code = m.get('ClassCode')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeSupabaseInstanceAttributeResponseBodyDataConnAddrs(DaraModel):
    def __init__(
        self,
        connection_string: str = None,
        net_type: str = None,
        port: int = None,
        vpc_id: str = None,
    ):
        # The endpoint.
        self.connection_string = connection_string
        # The network type.
        self.net_type = net_type
        # The port.
        self.port = port
        # VPC ID
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string

        if self.net_type is not None:
            result['NetType'] = self.net_type

        if self.port is not None:
            result['Port'] = self.port

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class DescribeSupabaseInstanceAttributeResponseBodyAccessDeniedDetail(DaraModel):
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
        # The type of the authentication principal.
        self.auth_principal_type = auth_principal_type
        # The encoded diagnostic message.
        self.encoded_diagnostic_message = encoded_diagnostic_message
        # The type of the permission denial.
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

