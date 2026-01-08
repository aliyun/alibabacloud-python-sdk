# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_pai_dsw20220101 import models as main_models
from darabonba.model import DaraModel

class CreateInstanceRequest(DaraModel):
    def __init__(
        self,
        accessibility: str = None,
        affinity: main_models.CreateInstanceRequestAffinity = None,
        assign_node_spec: main_models.CreateInstanceRequestAssignNodeSpec = None,
        cloud_disks: List[main_models.CreateInstanceRequestCloudDisks] = None,
        credential_config: main_models.CredentialConfig = None,
        datasets: List[main_models.CreateInstanceRequestDatasets] = None,
        driver: str = None,
        dynamic_mount: main_models.DynamicMount = None,
        ecs_spec: str = None,
        environment_variables: Dict[str, str] = None,
        image_auth: str = None,
        image_id: str = None,
        image_url: str = None,
        instance_name: str = None,
        labels: List[main_models.CreateInstanceRequestLabels] = None,
        migration_options: Dict[str, Any] = None,
        oversold_type: str = None,
        priority: int = None,
        requested_resource: main_models.CreateInstanceRequestRequestedResource = None,
        resource_id: str = None,
        spot_spec: main_models.CreateInstanceRequestSpotSpec = None,
        tag: List[main_models.CreateInstanceRequestTag] = None,
        user_command: main_models.CreateInstanceRequestUserCommand = None,
        user_id: str = None,
        user_vpc: main_models.CreateInstanceRequestUserVpc = None,
        workspace_id: str = None,
        workspace_source: str = None,
    ):
        # The instance accessibility.
        # 
        # Valid values:
        # 
        # *   PUBLIC: The instances are accessible to all members in the workspace.
        # *   PRIVATE: The instances are accessible only to you and the administrator of the workspace.
        self.accessibility = accessibility
        # The affinity configuration.
        self.affinity = affinity
        self.assign_node_spec = assign_node_spec
        # The cloud disks.
        self.cloud_disks = cloud_disks
        # The credential configuration.
        self.credential_config = credential_config
        # The datasets.
        self.datasets = datasets
        # The NVIDIA driver configuration.
        self.driver = driver
        # The dynamic mount configuration.
        self.dynamic_mount = dynamic_mount
        # The ECS instance type of the instance. You can call [ListEcsSpecs](https://help.aliyun.com/document_detail/470423.html) to obtain the ECS instance type.
        self.ecs_spec = ecs_spec
        # The environment variables.
        self.environment_variables = environment_variables
        # The Base64-encoded account and password for the user\\"s private image. The password will be hidden.
        self.image_auth = image_auth
        # The image ID. You can call [ListImages](https://help.aliyun.com/document_detail/449118.html) to obtain the image ID.
        self.image_id = image_id
        # The image address. You can call [ListImages](https://help.aliyun.com/document_detail/449118.html) to obtain the image address.
        self.image_url = image_url
        # The instance name. The name must meet the following requirements:
        # 
        # *   The name can contain only letters, digits, and underscores (_).
        # *   The name can be up to 27 characters in length.
        self.instance_name = instance_name
        # The custom labels.
        self.labels = labels
        self.migration_options = migration_options
        self.oversold_type = oversold_type
        # The priority based on which resources are allocated to instances. Valid values: 1 to 9.
        # 
        # *   1: the lowest priority.
        # *   9: the highest priority.
        self.priority = priority
        # The resource configurations.
        self.requested_resource = requested_resource
        # The ID of the resource group. This parameter is configured during prepayment. For information about how to create a dedicated resource group, see [Create a dedicated resource group and purchase general computing resources](https://help.aliyun.com/document_detail/202827.html).
        self.resource_id = resource_id
        self.spot_spec = spot_spec
        # The tags.
        self.tag = tag
        self.user_command = user_command
        # The ID of the instance owner. Valid values: Alibaba Cloud account and RAM user.
        self.user_id = user_id
        # The virtual private cloud (VPC) configurations.
        self.user_vpc = user_vpc
        # The workspace ID. You can call [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html) to obtain the workspace ID.
        self.workspace_id = workspace_id
        # The storage corresponding to the working directory. You can mount disks or datasets to /mnt/workspace at the same time. OSS datasets and dynamically mounted datasets are not supported.
        # 
        # Valid values:
        # 
        # *   rootfsCloudDisk: Mount the disk to the working directory.
        # *   Mount path of the dataset, such as /mnt/data: Datasets in URI format only support this method.
        # *   Dataset ID, such as d-vsqjvs\\*\\*\\*\\*rp5l206u: If a single dataset is mounted to multiple paths, the first path is selected. We recommend that you do not use this method, use the mount path instead.
        # 
        # If you leave this parameter empty:
        # 
        # *   If the instance uses cloud disks, cloud disks are selected by default.
        # *   if no cloud disks are available, the first NAS or CPFS dataset is selected as the working directory.
        # *   If no cloud disks, and NAS or CPFS datasets are available, the host space is used.
        self.workspace_source = workspace_source

    def validate(self):
        if self.affinity:
            self.affinity.validate()
        if self.assign_node_spec:
            self.assign_node_spec.validate()
        if self.cloud_disks:
            for v1 in self.cloud_disks:
                 if v1:
                    v1.validate()
        if self.credential_config:
            self.credential_config.validate()
        if self.datasets:
            for v1 in self.datasets:
                 if v1:
                    v1.validate()
        if self.dynamic_mount:
            self.dynamic_mount.validate()
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()
        if self.requested_resource:
            self.requested_resource.validate()
        if self.spot_spec:
            self.spot_spec.validate()
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()
        if self.user_command:
            self.user_command.validate()
        if self.user_vpc:
            self.user_vpc.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility

        if self.affinity is not None:
            result['Affinity'] = self.affinity.to_map()

        if self.assign_node_spec is not None:
            result['AssignNodeSpec'] = self.assign_node_spec.to_map()

        result['CloudDisks'] = []
        if self.cloud_disks is not None:
            for k1 in self.cloud_disks:
                result['CloudDisks'].append(k1.to_map() if k1 else None)

        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()

        result['Datasets'] = []
        if self.datasets is not None:
            for k1 in self.datasets:
                result['Datasets'].append(k1.to_map() if k1 else None)

        if self.driver is not None:
            result['Driver'] = self.driver

        if self.dynamic_mount is not None:
            result['DynamicMount'] = self.dynamic_mount.to_map()

        if self.ecs_spec is not None:
            result['EcsSpec'] = self.ecs_spec

        if self.environment_variables is not None:
            result['EnvironmentVariables'] = self.environment_variables

        if self.image_auth is not None:
            result['ImageAuth'] = self.image_auth

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        if self.migration_options is not None:
            result['MigrationOptions'] = self.migration_options

        if self.oversold_type is not None:
            result['OversoldType'] = self.oversold_type

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.requested_resource is not None:
            result['RequestedResource'] = self.requested_resource.to_map()

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.spot_spec is not None:
            result['SpotSpec'] = self.spot_spec.to_map()

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.user_command is not None:
            result['UserCommand'] = self.user_command.to_map()

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_vpc is not None:
            result['UserVpc'] = self.user_vpc.to_map()

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        if self.workspace_source is not None:
            result['WorkspaceSource'] = self.workspace_source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')

        if m.get('Affinity') is not None:
            temp_model = main_models.CreateInstanceRequestAffinity()
            self.affinity = temp_model.from_map(m.get('Affinity'))

        if m.get('AssignNodeSpec') is not None:
            temp_model = main_models.CreateInstanceRequestAssignNodeSpec()
            self.assign_node_spec = temp_model.from_map(m.get('AssignNodeSpec'))

        self.cloud_disks = []
        if m.get('CloudDisks') is not None:
            for k1 in m.get('CloudDisks'):
                temp_model = main_models.CreateInstanceRequestCloudDisks()
                self.cloud_disks.append(temp_model.from_map(k1))

        if m.get('CredentialConfig') is not None:
            temp_model = main_models.CredentialConfig()
            self.credential_config = temp_model.from_map(m.get('CredentialConfig'))

        self.datasets = []
        if m.get('Datasets') is not None:
            for k1 in m.get('Datasets'):
                temp_model = main_models.CreateInstanceRequestDatasets()
                self.datasets.append(temp_model.from_map(k1))

        if m.get('Driver') is not None:
            self.driver = m.get('Driver')

        if m.get('DynamicMount') is not None:
            temp_model = main_models.DynamicMount()
            self.dynamic_mount = temp_model.from_map(m.get('DynamicMount'))

        if m.get('EcsSpec') is not None:
            self.ecs_spec = m.get('EcsSpec')

        if m.get('EnvironmentVariables') is not None:
            self.environment_variables = m.get('EnvironmentVariables')

        if m.get('ImageAuth') is not None:
            self.image_auth = m.get('ImageAuth')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.CreateInstanceRequestLabels()
                self.labels.append(temp_model.from_map(k1))

        if m.get('MigrationOptions') is not None:
            self.migration_options = m.get('MigrationOptions')

        if m.get('OversoldType') is not None:
            self.oversold_type = m.get('OversoldType')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('RequestedResource') is not None:
            temp_model = main_models.CreateInstanceRequestRequestedResource()
            self.requested_resource = temp_model.from_map(m.get('RequestedResource'))

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('SpotSpec') is not None:
            temp_model = main_models.CreateInstanceRequestSpotSpec()
            self.spot_spec = temp_model.from_map(m.get('SpotSpec'))

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateInstanceRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('UserCommand') is not None:
            temp_model = main_models.CreateInstanceRequestUserCommand()
            self.user_command = temp_model.from_map(m.get('UserCommand'))

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserVpc') is not None:
            temp_model = main_models.CreateInstanceRequestUserVpc()
            self.user_vpc = temp_model.from_map(m.get('UserVpc'))

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        if m.get('WorkspaceSource') is not None:
            self.workspace_source = m.get('WorkspaceSource')

        return self

class CreateInstanceRequestUserVpc(DaraModel):
    def __init__(
        self,
        bandwidth_limit: main_models.BandwidthLimit = None,
        default_route: str = None,
        extended_cidrs: List[str] = None,
        forward_infos: List[main_models.ForwardInfo] = None,
        security_group_id: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        self.bandwidth_limit = bandwidth_limit
        # The default route. Valid values:
        # 
        # *   eth0: The default network interface is used to access the Internet through the public gateway.
        # *   eth1: The user\\"s elastic network interface (ENI) is used to access the Internet through the private gateway. For more information about the configuration method, see [Enable Internet access for a DSW instance by using a private Internet NAT gateway](https://help.aliyun.com/document_detail/2525343.html).
        self.default_route = default_route
        # The extended CIDR blocks.
        # 
        # *   If you leave the SwitchId and ExtendedCIDRs parameters empty, the system automatically obtains all CIDR blocks in a VPC.
        # *   If you configure the SwitchId and ExtendedCIDRs parameters, we recommend that you specify all CIDR blocks in a VPC.
        self.extended_cidrs = extended_cidrs
        # The forward information.
        self.forward_infos = forward_infos
        # The security group ID.
        self.security_group_id = security_group_id
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The VPC ID.
        self.vpc_id = vpc_id

    def validate(self):
        if self.bandwidth_limit:
            self.bandwidth_limit.validate()
        if self.forward_infos:
            for v1 in self.forward_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth_limit is not None:
            result['BandwidthLimit'] = self.bandwidth_limit.to_map()

        if self.default_route is not None:
            result['DefaultRoute'] = self.default_route

        if self.extended_cidrs is not None:
            result['ExtendedCIDRs'] = self.extended_cidrs

        result['ForwardInfos'] = []
        if self.forward_infos is not None:
            for k1 in self.forward_infos:
                result['ForwardInfos'].append(k1.to_map() if k1 else None)

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandwidthLimit') is not None:
            temp_model = main_models.BandwidthLimit()
            self.bandwidth_limit = temp_model.from_map(m.get('BandwidthLimit'))

        if m.get('DefaultRoute') is not None:
            self.default_route = m.get('DefaultRoute')

        if m.get('ExtendedCIDRs') is not None:
            self.extended_cidrs = m.get('ExtendedCIDRs')

        self.forward_infos = []
        if m.get('ForwardInfos') is not None:
            for k1 in m.get('ForwardInfos'):
                temp_model = main_models.ForwardInfo()
                self.forward_infos.append(temp_model.from_map(k1))

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class CreateInstanceRequestUserCommand(DaraModel):
    def __init__(
        self,
        on_start: main_models.CreateInstanceRequestUserCommandOnStart = None,
    ):
        self.on_start = on_start

    def validate(self):
        if self.on_start:
            self.on_start.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.on_start is not None:
            result['OnStart'] = self.on_start.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OnStart') is not None:
            temp_model = main_models.CreateInstanceRequestUserCommandOnStart()
            self.on_start = temp_model.from_map(m.get('OnStart'))

        return self

class CreateInstanceRequestUserCommandOnStart(DaraModel):
    def __init__(
        self,
        content: str = None,
    ):
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        return self

class CreateInstanceRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateInstanceRequestSpotSpec(DaraModel):
    def __init__(
        self,
        spot_discount_limit: str = None,
        spot_duration: str = None,
        spot_price_limit: str = None,
        spot_strategy: str = None,
    ):
        self.spot_discount_limit = spot_discount_limit
        self.spot_duration = spot_duration
        self.spot_price_limit = spot_price_limit
        self.spot_strategy = spot_strategy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.spot_discount_limit is not None:
            result['SpotDiscountLimit'] = self.spot_discount_limit

        if self.spot_duration is not None:
            result['SpotDuration'] = self.spot_duration

        if self.spot_price_limit is not None:
            result['SpotPriceLimit'] = self.spot_price_limit

        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpotDiscountLimit') is not None:
            self.spot_discount_limit = m.get('SpotDiscountLimit')

        if m.get('SpotDuration') is not None:
            self.spot_duration = m.get('SpotDuration')

        if m.get('SpotPriceLimit') is not None:
            self.spot_price_limit = m.get('SpotPriceLimit')

        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')

        return self

class CreateInstanceRequestRequestedResource(DaraModel):
    def __init__(
        self,
        cpu: str = None,
        gpu: str = None,
        gputype: str = None,
        memory: str = None,
        shared_memory: str = None,
    ):
        # The number of CPU cores.
        self.cpu = cpu
        # The number of GPUs.
        self.gpu = gpu
        # The GPU memory type. Valid values:
        # 
        # *   V100
        # *   A100
        # *   T4
        # *   A10
        # *   P100
        self.gputype = gputype
        # The memory size. Unit: GB.
        self.memory = memory
        # The size of the shared memory. Unit: GB.
        self.shared_memory = shared_memory

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu is not None:
            result['CPU'] = self.cpu

        if self.gpu is not None:
            result['GPU'] = self.gpu

        if self.gputype is not None:
            result['GPUType'] = self.gputype

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.shared_memory is not None:
            result['SharedMemory'] = self.shared_memory

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CPU') is not None:
            self.cpu = m.get('CPU')

        if m.get('GPU') is not None:
            self.gpu = m.get('GPU')

        if m.get('GPUType') is not None:
            self.gputype = m.get('GPUType')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('SharedMemory') is not None:
            self.shared_memory = m.get('SharedMemory')

        return self

class CreateInstanceRequestLabels(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The custom label key.
        self.key = key
        # The custom label value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateInstanceRequestDatasets(DaraModel):
    def __init__(
        self,
        dataset_id: str = None,
        dataset_version: str = None,
        dynamic: bool = None,
        mount_access: str = None,
        mount_path: str = None,
        option_type: str = None,
        options: str = None,
        uri: str = None,
    ):
        # The dataset ID. If the dataset is read-only, you cannot change the dataset permission from read-only to read and write by using MountAccess.
        # 
        # You can call [ListDatasets](https://help.aliyun.com/document_detail/457222.html) to obtain the dataset ID. If you configure the dataset ID, you cannot configure the dataset URI.
        self.dataset_id = dataset_id
        # The dataset version. You must also configure DatasetId. If you leave this parameter empty, the value v1 is used by default.
        self.dataset_version = dataset_version
        # Specifies whether to enable dynamic mounting. Default value: false.
        # 
        # *   Currently, only instances using general-purpose computing resources are supported.
        # *   Currently, only OSS datasets are supported. The mounted datasets are read-only.
        # *   The mount path of the dynamically mounted dataset must be a subpath of the root path. Example: /mnt/dynamic/data1/
        # *   A dynamically mounted dataset must be after non-dynamic datasets.
        self.dynamic = dynamic
        # The read and write permissions of the dataset. If the dataset is read-only, it cannot be changed to read and write.
        self.mount_access = mount_access
        # The mount path of the dataset.
        self.mount_path = mount_path
        # The mount type. You cannot specify Options at the same time. This is deprecated, and you can use Options instead.
        self.option_type = option_type
        # The custom dataset mount options. Only OSS is supported. You cannot specify OptionType at the same time. For more information, see [DSW mount configurations](https://www.alibabacloud.com/help/en/pai/user-guide/read-and-write-dataset-data).
        self.options = options
        # The URI of the storage service directory, which can be directly mounted. This parameter is mutually exclusive with DatasetId.
        # 
        # URI formats of different types of storage:
        # 
        # *   OSS: oss://bucket-name.oss-cn-shanghai-internal.aliyuncs.com/data/path/
        # *   NAS: nas://29\\*\\*d-b12\\*\\*\\*\\*446.cn-hangzhou.nas.aliyuncs.com/data/path/
        # *   Extreme NAS: nas://29\\*\\*\\*\\*123-y\\*\\*r.cn-hangzhou.extreme.nas.aliyuncs.com/data/path/
        # *   CPFS: cpfs://cpfs-213\\*\\*\\*\\*87.cn-wulanchabu/ptc-292\\*\\*\\*\\*\\*cbb/exp-290\\*\\*\\*\\*\\*\\*\\*\\*03e/data/path/
        # *   Lingjun CPFS: bmcpfs://cpfs-290\\*\\*\\*\\*\\*\\*foflh-vpc-x\\*\\*\\*\\*8r.cn-wulanchabu.cpfs.aliyuncs.com/data/path/
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id

        if self.dataset_version is not None:
            result['DatasetVersion'] = self.dataset_version

        if self.dynamic is not None:
            result['Dynamic'] = self.dynamic

        if self.mount_access is not None:
            result['MountAccess'] = self.mount_access

        if self.mount_path is not None:
            result['MountPath'] = self.mount_path

        if self.option_type is not None:
            result['OptionType'] = self.option_type

        if self.options is not None:
            result['Options'] = self.options

        if self.uri is not None:
            result['Uri'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')

        if m.get('DatasetVersion') is not None:
            self.dataset_version = m.get('DatasetVersion')

        if m.get('Dynamic') is not None:
            self.dynamic = m.get('Dynamic')

        if m.get('MountAccess') is not None:
            self.mount_access = m.get('MountAccess')

        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')

        if m.get('OptionType') is not None:
            self.option_type = m.get('OptionType')

        if m.get('Options') is not None:
            self.options = m.get('Options')

        if m.get('Uri') is not None:
            self.uri = m.get('Uri')

        return self

class CreateInstanceRequestCloudDisks(DaraModel):
    def __init__(
        self,
        capacity: str = None,
        mount_path: str = None,
        path: str = None,
        status: main_models.CreateInstanceRequestCloudDisksStatus = None,
        sub_type: str = None,
    ):
        # If **Resource Type** is **Public Resource** or if **Resource Quota** is subscription-based general-purpose computing resources (CPU cores ≥ 2 and memory ≥ 4 GB, or configured with GPU):
        # 
        # Each instance has a free system disk of 100 GiB for persistent storage. **If the DSW instance is stopped and not launched for more than 15 days, the disk is cleared**. The disk can be expanded. For specific pricing, refer to the console.
        # 
        # **
        # 
        # **Warning**
        # 
        # *   After the expansion, you cannot reduce the storage space. Proceed with caution.
        # 
        # *   After the expansion, the disk is not cleared if the instance is stopped for more than 15 days. However, it will continue to incur fees.
        # 
        # *   If you delete the instance, the system disk is also released and the data stored in the disk is deleted. Make sure that you have backed up your data before you delete the instance.
        # 
        # If you need persistent storage, you can **mount a dataset** or add the OSS, NAS, or CPFS path to the **storage path**.
        self.capacity = capacity
        # The mount path of the cloud disk.
        self.mount_path = mount_path
        # The subpath of the cloud disk that is mounted to the instance.
        self.path = path
        # The disk or snapshot usage.
        self.status = status
        # The cloud disk type.
        # 
        # *   rootfs: Mounts the disk as a system disk. The system environment is stored on the disk.
        self.sub_type = sub_type

    def validate(self):
        if self.status:
            self.status.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.capacity is not None:
            result['Capacity'] = self.capacity

        if self.mount_path is not None:
            result['MountPath'] = self.mount_path

        if self.path is not None:
            result['Path'] = self.path

        if self.status is not None:
            result['Status'] = self.status.to_map()

        if self.sub_type is not None:
            result['SubType'] = self.sub_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')

        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Status') is not None:
            temp_model = main_models.CreateInstanceRequestCloudDisksStatus()
            self.status = temp_model.from_map(m.get('Status'))

        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')

        return self

class CreateInstanceRequestCloudDisksStatus(DaraModel):
    def __init__(
        self,
        available: int = None,
        capacity: int = None,
        usage: int = None,
    ):
        # The available capacity. Unit: bytes.
        self.available = available
        # The capacity. Unit: bytes.
        self.capacity = capacity
        # The used capacity. Unit: bytes.
        self.usage = usage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available is not None:
            result['Available'] = self.available

        if self.capacity is not None:
            result['Capacity'] = self.capacity

        if self.usage is not None:
            result['Usage'] = self.usage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Available') is not None:
            self.available = m.get('Available')

        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')

        if m.get('Usage') is not None:
            self.usage = m.get('Usage')

        return self

class CreateInstanceRequestAssignNodeSpec(DaraModel):
    def __init__(
        self,
        anti_affinity_node_names: str = None,
        node_names: str = None,
    ):
        self.anti_affinity_node_names = anti_affinity_node_names
        self.node_names = node_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.anti_affinity_node_names is not None:
            result['AntiAffinityNodeNames'] = self.anti_affinity_node_names

        if self.node_names is not None:
            result['NodeNames'] = self.node_names

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntiAffinityNodeNames') is not None:
            self.anti_affinity_node_names = m.get('AntiAffinityNodeNames')

        if m.get('NodeNames') is not None:
            self.node_names = m.get('NodeNames')

        return self

class CreateInstanceRequestAffinity(DaraModel):
    def __init__(
        self,
        cpu: main_models.CreateInstanceRequestAffinityCPU = None,
    ):
        # The CPU affinity configuration. Only subscription instances that use general-purpose computing resources support CPU affinity configuration.
        self.cpu = cpu

    def validate(self):
        if self.cpu:
            self.cpu.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu is not None:
            result['CPU'] = self.cpu.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CPU') is not None:
            temp_model = main_models.CreateInstanceRequestAffinityCPU()
            self.cpu = temp_model.from_map(m.get('CPU'))

        return self

class CreateInstanceRequestAffinityCPU(DaraModel):
    def __init__(
        self,
        enable: bool = None,
    ):
        # Specifies whether to enable the CPU affinity feature.
        # 
        # *   false
        # *   true
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['Enable'] = self.enable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        return self

