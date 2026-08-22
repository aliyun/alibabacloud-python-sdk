# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_polardbx20200202 import models as main_models
from darabonba.model import DaraModel

class DescribeOpenSearchInfoResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: main_models.DescribeOpenSearchInfoResponseBodyAccessDeniedDetail = None,
        data: main_models.DescribeOpenSearchInfoResponseBodyData = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The returned result set.
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
            temp_model = main_models.DescribeOpenSearchInfoResponseBodyAccessDeniedDetail()
            self.access_denied_detail = temp_model.from_map(m.get('AccessDeniedDetail'))

        if m.get('Data') is not None:
            temp_model = main_models.DescribeOpenSearchInfoResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeOpenSearchInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        instance: main_models.DescribeOpenSearchInfoResponseBodyDataInstance = None,
        spec: main_models.DescribeOpenSearchInfoResponseBodyDataSpec = None,
    ):
        # The instance information.
        self.instance = instance
        # The specifications.
        self.spec = spec

    def validate(self):
        if self.instance:
            self.instance.validate()
        if self.spec:
            self.spec.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance is not None:
            result['Instance'] = self.instance.to_map()

        if self.spec is not None:
            result['Spec'] = self.spec.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Instance') is not None:
            temp_model = main_models.DescribeOpenSearchInfoResponseBodyDataInstance()
            self.instance = temp_model.from_map(m.get('Instance'))

        if m.get('Spec') is not None:
            temp_model = main_models.DescribeOpenSearchInfoResponseBodyDataSpec()
            self.spec = temp_model.from_map(m.get('Spec'))

        return self

class DescribeOpenSearchInfoResponseBodyDataSpec(DaraModel):
    def __init__(
        self,
        coordinator_node_count: int = None,
        coordinator_node_cpu: int = None,
        coordinator_node_enabled: bool = None,
        coordinator_node_memory_gb: int = None,
        data_node_count: int = None,
        data_node_cpu: int = None,
        data_node_memory_gb: int = None,
        master_node_count: int = None,
        master_node_cpu: int = None,
        master_node_enabled: bool = None,
        master_node_memory_gb: int = None,
        replica_count: int = None,
        storage_size_gb: int = None,
        storage_type: str = None,
    ):
        # The number of coordinator nodes.
        self.coordinator_node_count = coordinator_node_count
        # The number of CPU cores of a single coordinator node.
        self.coordinator_node_cpu = coordinator_node_cpu
        # Indicates whether coordinator nodes are enabled.
        self.coordinator_node_enabled = coordinator_node_enabled
        # The memory size of a single coordinator node. Unit: GB.
        self.coordinator_node_memory_gb = coordinator_node_memory_gb
        # The number of data nodes.
        self.data_node_count = data_node_count
        # The number of CPU cores of a single data node.
        self.data_node_cpu = data_node_cpu
        # The memory size of a single data node. Unit: GB.
        self.data_node_memory_gb = data_node_memory_gb
        # The master node type. Valid values:
        # - **0**: The master node is a single node.
        # - **2**: The master node is in Cluster Edition.
        self.master_node_count = master_node_count
        # The number of CPU cores of a single dedicated master node.
        self.master_node_cpu = master_node_cpu
        # Indicates whether dedicated master nodes are enabled.
        self.master_node_enabled = master_node_enabled
        # The memory size of a single dedicated master node. Unit: GB.
        self.master_node_memory_gb = master_node_memory_gb
        # The number of replica nodes in the primary zone.
        # > The **ReplicaCount** and **SlaveReplicaCount** parameters apply only to cloud-native instances. If the instance uses a cluster architecture, these parameters indicate the number of replica nodes of a **single shard** in the primary and secondary zones.
        self.replica_count = replica_count
        # The storage size of a single data node. Unit: GB.
        self.storage_size_gb = storage_size_gb
        # The storage type.
        self.storage_type = storage_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.coordinator_node_count is not None:
            result['CoordinatorNodeCount'] = self.coordinator_node_count

        if self.coordinator_node_cpu is not None:
            result['CoordinatorNodeCpu'] = self.coordinator_node_cpu

        if self.coordinator_node_enabled is not None:
            result['CoordinatorNodeEnabled'] = self.coordinator_node_enabled

        if self.coordinator_node_memory_gb is not None:
            result['CoordinatorNodeMemoryGB'] = self.coordinator_node_memory_gb

        if self.data_node_count is not None:
            result['DataNodeCount'] = self.data_node_count

        if self.data_node_cpu is not None:
            result['DataNodeCpu'] = self.data_node_cpu

        if self.data_node_memory_gb is not None:
            result['DataNodeMemoryGB'] = self.data_node_memory_gb

        if self.master_node_count is not None:
            result['MasterNodeCount'] = self.master_node_count

        if self.master_node_cpu is not None:
            result['MasterNodeCpu'] = self.master_node_cpu

        if self.master_node_enabled is not None:
            result['MasterNodeEnabled'] = self.master_node_enabled

        if self.master_node_memory_gb is not None:
            result['MasterNodeMemoryGB'] = self.master_node_memory_gb

        if self.replica_count is not None:
            result['ReplicaCount'] = self.replica_count

        if self.storage_size_gb is not None:
            result['StorageSizeGB'] = self.storage_size_gb

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoordinatorNodeCount') is not None:
            self.coordinator_node_count = m.get('CoordinatorNodeCount')

        if m.get('CoordinatorNodeCpu') is not None:
            self.coordinator_node_cpu = m.get('CoordinatorNodeCpu')

        if m.get('CoordinatorNodeEnabled') is not None:
            self.coordinator_node_enabled = m.get('CoordinatorNodeEnabled')

        if m.get('CoordinatorNodeMemoryGB') is not None:
            self.coordinator_node_memory_gb = m.get('CoordinatorNodeMemoryGB')

        if m.get('DataNodeCount') is not None:
            self.data_node_count = m.get('DataNodeCount')

        if m.get('DataNodeCpu') is not None:
            self.data_node_cpu = m.get('DataNodeCpu')

        if m.get('DataNodeMemoryGB') is not None:
            self.data_node_memory_gb = m.get('DataNodeMemoryGB')

        if m.get('MasterNodeCount') is not None:
            self.master_node_count = m.get('MasterNodeCount')

        if m.get('MasterNodeCpu') is not None:
            self.master_node_cpu = m.get('MasterNodeCpu')

        if m.get('MasterNodeEnabled') is not None:
            self.master_node_enabled = m.get('MasterNodeEnabled')

        if m.get('MasterNodeMemoryGB') is not None:
            self.master_node_memory_gb = m.get('MasterNodeMemoryGB')

        if m.get('ReplicaCount') is not None:
            self.replica_count = m.get('ReplicaCount')

        if m.get('StorageSizeGB') is not None:
            self.storage_size_gb = m.get('StorageSizeGB')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        return self

class DescribeOpenSearchInfoResponseBodyDataInstance(DaraModel):
    def __init__(
        self,
        charge_type: str = None,
        compatible_version: str = None,
        create_time: str = None,
        deploy_mode: str = None,
        engine_version: str = None,
        expire_time: str = None,
        instance_id: str = None,
        instance_name: str = None,
        net_type: str = None,
        region_id: str = None,
        status: str = None,
        update_time: str = None,
        vpc_id: str = None,
        vswitch_id: str = None,
    ):
        # The billing method. Valid values:
        # - **POSTPAY**: pay-as-you-go.
        # - **PREPAY**: subscription.
        self.charge_type = charge_type
        # The OpenSearch-compatible version.
        self.compatible_version = compatible_version
        # The creation time.
        self.create_time = create_time
        # The deployment mode. Valid values:
        # - multiple: multi-zone deployment.
        # - single: single-zone deployment.
        self.deploy_mode = deploy_mode
        # The DPI engine version. Default value: 2.0.
        self.engine_version = engine_version
        # The expiration time.
        self.expire_time = expire_time
        # The instance ID.
        self.instance_id = instance_id
        # The instance name.
        self.instance_name = instance_name
        # The network type of the connection string. Valid values:
        # * **Public**: public endpoint.
        # * **Private**: private endpoint.
        # * **Inner**: private endpoint (classic network).
        self.net_type = net_type
        # The region ID.
        self.region_id = region_id
        # The instance status.
        self.status = status
        # The time when the last task was updated (in timestamp format).
        self.update_time = update_time
        # The ID of the virtual private cloud (VPC) in which the access endpoint resides.
        self.vpc_id = vpc_id
        # The vSwitch ID. This parameter is required when you create a DRDS instance of the VPC network type.
        self.vswitch_id = vswitch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.compatible_version is not None:
            result['CompatibleVersion'] = self.compatible_version

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.deploy_mode is not None:
            result['DeployMode'] = self.deploy_mode

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.net_type is not None:
            result['NetType'] = self.net_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('CompatibleVersion') is not None:
            self.compatible_version = m.get('CompatibleVersion')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DeployMode') is not None:
            self.deploy_mode = m.get('DeployMode')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')

        return self

class DescribeOpenSearchInfoResponseBodyAccessDeniedDetail(DaraModel):
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
        # The identity used for authentication in the request.
        self.auth_principal_display_name = auth_principal_display_name
        # The owner ID of the authentication principal.
        self.auth_principal_owner_id = auth_principal_owner_id
        # The authentication principal type.
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

