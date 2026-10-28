# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardbx20200202 import models as main_models
from darabonba.model import DaraModel

class DescribePxfsInfoResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: main_models.DescribePxfsInfoResponseBodyAccessDeniedDetail = None,
        data: main_models.DescribePxfsInfoResponseBodyData = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response data.
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
            temp_model = main_models.DescribePxfsInfoResponseBodyAccessDeniedDetail()
            self.access_denied_detail = temp_model.from_map(m.get('AccessDeniedDetail'))

        if m.get('Data') is not None:
            temp_model = main_models.DescribePxfsInfoResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribePxfsInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        instance: main_models.DescribePxfsInfoResponseBodyDataInstance = None,
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
            temp_model = main_models.DescribePxfsInfoResponseBodyDataInstance()
            self.instance = temp_model.from_map(m.get('Instance'))

        return self

class DescribePxfsInfoResponseBodyDataInstance(DaraModel):
    def __init__(
        self,
        class_code: str = None,
        conn_addrs: List[main_models.DescribePxfsInfoResponseBodyDataInstanceConnAddrs] = None,
        create_time: str = None,
        dbinstance_name: str = None,
        instance_id: str = None,
        node_count: int = None,
        pxfs_instance_id: str = None,
        region_id: str = None,
        status: str = None,
        storage_size: int = None,
        storage_type: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
        version: str = None,
        zone_id: str = None,
    ):
        # The node specification.
        self.class_code = class_code
        # The list of connection addresses.
        self.conn_addrs = conn_addrs
        # The creation time.
        self.create_time = create_time
        # The PolarDB-X instance ID.
        self.dbinstance_name = dbinstance_name
        # The associated instance ID.
        self.instance_id = instance_id
        # The number of nodes.
        self.node_count = node_count
        # The Agent file service instance ID.
        self.pxfs_instance_id = pxfs_instance_id
        # The region ID.
        self.region_id = region_id
        # The status.
        self.status = status
        # The storage size.
        self.storage_size = storage_size
        # The storage type.
        self.storage_type = storage_type
        # The virtual private cloud (VPC) ID.
        self.vpcid = vpcid
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The current version.
        self.version = version
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

        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.node_count is not None:
            result['NodeCount'] = self.node_count

        if self.pxfs_instance_id is not None:
            result['PxfsInstanceId'] = self.pxfs_instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

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
        if m.get('ClassCode') is not None:
            self.class_code = m.get('ClassCode')

        self.conn_addrs = []
        if m.get('ConnAddrs') is not None:
            for k1 in m.get('ConnAddrs'):
                temp_model = main_models.DescribePxfsInfoResponseBodyDataInstanceConnAddrs()
                self.conn_addrs.append(temp_model.from_map(k1))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')

        if m.get('PxfsInstanceId') is not None:
            self.pxfs_instance_id = m.get('PxfsInstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribePxfsInfoResponseBodyDataInstanceConnAddrs(DaraModel):
    def __init__(
        self,
        connection_string: str = None,
        endpoint: str = None,
        port: int = None,
        protocol: str = None,
        tls_enabled: bool = None,
        transport: str = None,
        type: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
    ):
        # The connection string.
        self.connection_string = connection_string
        # The endpoint.
        self.endpoint = endpoint
        # The port number.
        self.port = port
        # The access protocol.
        self.protocol = protocol
        # Indicates whether TLS is enabled.
        self.tls_enabled = tls_enabled
        # The transport protocol.
        self.transport = transport
        # The connection type.
        self.type = type
        # The virtual private cloud (VPC) ID.
        self.vpcid = vpcid
        # The vSwitch ID.
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

        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.port is not None:
            result['Port'] = self.port

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.tls_enabled is not None:
            result['TlsEnabled'] = self.tls_enabled

        if self.transport is not None:
            result['Transport'] = self.transport

        if self.type is not None:
            result['Type'] = self.type

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('TlsEnabled') is not None:
            self.tls_enabled = m.get('TlsEnabled')

        if m.get('Transport') is not None:
            self.transport = m.get('Transport')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

class DescribePxfsInfoResponseBodyAccessDeniedDetail(DaraModel):
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
        # The authorization action. Same as described above.
        self.auth_action = auth_action
        # The display name of the authentication principal.
        self.auth_principal_display_name = auth_principal_display_name
        # The owner ID of the authentication principal.
        self.auth_principal_owner_id = auth_principal_owner_id
        # The authorization action. Same as described above.
        self.auth_principal_type = auth_principal_type
        # The encoded diagnostic message.
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

