# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_pai_dsw20220101 import models as main_models
from darabonba.model import DaraModel

class ListInstancesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        instances: List[main_models.ListInstancesResponseBodyInstances] = None,
        message: str = None,
        migration_options: Dict[str, Any] = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The status code. Valid values:
        # 
        # *   InternalError: an internal error. All errors, except for parameter validation errors, are classified as internal errors.
        # *   ValidationError: a parameter validation error.
        self.code = code
        # The HTTP status code. Valid values:
        # 
        # *   400
        # *   404
        self.http_status_code = http_status_code
        # The instances returned on this page.
        self.instances = instances
        # The response message.
        self.message = message
        self.migration_options = migration_options
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        # 
        # *   true
        # *   false
        self.success = success
        # The total number of instances.
        self.total_count = total_count

    def validate(self):
        if self.instances:
            for v1 in self.instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        result['Instances'] = []
        if self.instances is not None:
            for k1 in self.instances:
                result['Instances'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.migration_options is not None:
            result['MigrationOptions'] = self.migration_options

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        self.instances = []
        if m.get('Instances') is not None:
            for k1 in m.get('Instances'):
                temp_model = main_models.ListInstancesResponseBodyInstances()
                self.instances.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('MigrationOptions') is not None:
            self.migration_options = m.get('MigrationOptions')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListInstancesResponseBodyInstances(DaraModel):
    def __init__(
        self,
        accelerator_type: str = None,
        accessibility: str = None,
        accumulated_running_time_in_ms: int = None,
        affinity: main_models.ListInstancesResponseBodyInstancesAffinity = None,
        cloud_disks: List[main_models.ListInstancesResponseBodyInstancesCloudDisks] = None,
        credential_config: main_models.CredentialConfig = None,
        datasets: List[main_models.ListInstancesResponseBodyInstancesDatasets] = None,
        driver: str = None,
        dynamic_mount: main_models.DynamicMount = None,
        ecs_spec: str = None,
        environment_variables: Dict[str, str] = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        idle_instance_culler: main_models.ListInstancesResponseBodyInstancesIdleInstanceCuller = None,
        image_auth: str = None,
        image_id: str = None,
        image_name: str = None,
        image_url: str = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_shutdown_timer: main_models.ListInstancesResponseBodyInstancesInstanceShutdownTimer = None,
        instance_snapshot_list: List[main_models.ListInstancesResponseBodyInstancesInstanceSnapshotList] = None,
        instance_url: str = None,
        jupyterlab_url: str = None,
        labels: List[main_models.ListInstancesResponseBodyInstancesLabels] = None,
        latest_snapshot: main_models.ListInstancesResponseBodyInstancesLatestSnapshot = None,
        oversold_info: str = None,
        oversold_type: str = None,
        payment_type: str = None,
        priority: int = None,
        reason_code: str = None,
        reason_message: str = None,
        requested_resource: main_models.ListInstancesResponseBodyInstancesRequestedResource = None,
        resource_id: str = None,
        resource_name: str = None,
        service_config: main_models.ServiceConfig = None,
        status: str = None,
        tags: List[main_models.ListInstancesResponseBodyInstancesTags] = None,
        terminal_url: str = None,
        user_id: str = None,
        user_name: str = None,
        user_vpc: main_models.ListInstancesResponseBodyInstancesUserVpc = None,
        web_ideurl: str = None,
        workspace_id: str = None,
        workspace_name: str = None,
        workspace_source: str = None,
    ):
        # The accelerator type of the instance. Valid values:
        # 
        # *   CPU
        # *   GPU
        self.accelerator_type = accelerator_type
        # The accessibility. Valid values:
        # 
        # *   PRIVATE (default): The instances are accessible only to you and the administrator of the workspace.
        # *   PUBLIC: The instances are accessible only to all members in the workspace.
        self.accessibility = accessibility
        # The accumulated running duration. Unit: milliseconds.
        self.accumulated_running_time_in_ms = accumulated_running_time_in_ms
        # The affinity configuration.
        self.affinity = affinity
        # The cloud disks of the instance.
        self.cloud_disks = cloud_disks
        # The credential configuration.
        self.credential_config = credential_config
        # The datasets.
        self.datasets = datasets
        # The NVIDIA driver configuration.
        self.driver = driver
        # The dynamic mount configurations.
        self.dynamic_mount = dynamic_mount
        # The ECS instance type of the instance.
        self.ecs_spec = ecs_spec
        # The environment variables.
        self.environment_variables = environment_variables
        # The time when the instance was created.
        self.gmt_create_time = gmt_create_time
        # The time when the instance was modified.
        self.gmt_modified_time = gmt_modified_time
        # The rule for stopping idle instances.
        self.idle_instance_culler = idle_instance_culler
        # The Base64-encoded account and password for the user\\"s private image. The password will be hidden.
        self.image_auth = image_auth
        # The image ID.
        self.image_id = image_id
        # The image name.
        self.image_name = image_name
        # The image address.
        self.image_url = image_url
        # The instance ID.
        self.instance_id = instance_id
        # The instance name.
        self.instance_name = instance_name
        # The scheduled stop task.
        self.instance_shutdown_timer = instance_shutdown_timer
        # The instance snapshots.
        self.instance_snapshot_list = instance_snapshot_list
        # The instance URL.
        self.instance_url = instance_url
        # The JupyterLab URL.
        self.jupyterlab_url = jupyterlab_url
        # The custom labels.
        self.labels = labels
        # The user image that was latest saved.
        self.latest_snapshot = latest_snapshot
        self.oversold_info = oversold_info
        self.oversold_type = oversold_type
        # The billing method. Valid values:
        # 
        # *   PayAsYouGo
        # *   Subscription
        self.payment_type = payment_type
        # The priority based on which resources are allocated to instances. Resources are preferentially allocated to instances with higher priorities.
        self.priority = priority
        # The error code of the instance.
        self.reason_code = reason_code
        # The cause of the instance error.
        self.reason_message = reason_message
        # The resource configurations.
        self.requested_resource = requested_resource
        # The resource ID. This parameter is valid only if you set PaymentType to Subscription.
        self.resource_id = resource_id
        # The specifications.
        # 
        # *   In pay-as-you-go scenarios, the value is the specifications of the purchased ECS instance type.
        # *   In subscription scenarios, the value is the requested number of CPU cores and memory size.
        self.resource_name = resource_name
        self.service_config = service_config
        # The instance status.
        self.status = status
        # The tags.
        self.tags = tags
        # The terminal URL.
        self.terminal_url = terminal_url
        # The user ID.
        self.user_id = user_id
        # The username.
        self.user_name = user_name
        # The virtual private cloud (VPC) configurations.
        self.user_vpc = user_vpc
        # The Web IDE URL.
        self.web_ideurl = web_ideurl
        # The workspace ID.
        self.workspace_id = workspace_id
        # The workspace name.
        self.workspace_name = workspace_name
        # The storage for the workspace. If you leave this parameter empty, the workspace uses File Storage NAS (NAS) storage, cloud disks, or local disks in sequence.
        self.workspace_source = workspace_source

    def validate(self):
        if self.affinity:
            self.affinity.validate()
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
        if self.idle_instance_culler:
            self.idle_instance_culler.validate()
        if self.instance_shutdown_timer:
            self.instance_shutdown_timer.validate()
        if self.instance_snapshot_list:
            for v1 in self.instance_snapshot_list:
                 if v1:
                    v1.validate()
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()
        if self.latest_snapshot:
            self.latest_snapshot.validate()
        if self.requested_resource:
            self.requested_resource.validate()
        if self.service_config:
            self.service_config.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()
        if self.user_vpc:
            self.user_vpc.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerator_type is not None:
            result['AcceleratorType'] = self.accelerator_type

        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility

        if self.accumulated_running_time_in_ms is not None:
            result['AccumulatedRunningTimeInMs'] = self.accumulated_running_time_in_ms

        if self.affinity is not None:
            result['Affinity'] = self.affinity.to_map()

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

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.idle_instance_culler is not None:
            result['IdleInstanceCuller'] = self.idle_instance_culler.to_map()

        if self.image_auth is not None:
            result['ImageAuth'] = self.image_auth

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_name is not None:
            result['ImageName'] = self.image_name

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_shutdown_timer is not None:
            result['InstanceShutdownTimer'] = self.instance_shutdown_timer.to_map()

        result['InstanceSnapshotList'] = []
        if self.instance_snapshot_list is not None:
            for k1 in self.instance_snapshot_list:
                result['InstanceSnapshotList'].append(k1.to_map() if k1 else None)

        if self.instance_url is not None:
            result['InstanceUrl'] = self.instance_url

        if self.jupyterlab_url is not None:
            result['JupyterlabUrl'] = self.jupyterlab_url

        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        if self.latest_snapshot is not None:
            result['LatestSnapshot'] = self.latest_snapshot.to_map()

        if self.oversold_info is not None:
            result['OversoldInfo'] = self.oversold_info

        if self.oversold_type is not None:
            result['OversoldType'] = self.oversold_type

        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code

        if self.reason_message is not None:
            result['ReasonMessage'] = self.reason_message

        if self.requested_resource is not None:
            result['RequestedResource'] = self.requested_resource.to_map()

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name

        if self.service_config is not None:
            result['ServiceConfig'] = self.service_config.to_map()

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.terminal_url is not None:
            result['TerminalUrl'] = self.terminal_url

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_name is not None:
            result['UserName'] = self.user_name

        if self.user_vpc is not None:
            result['UserVpc'] = self.user_vpc.to_map()

        if self.web_ideurl is not None:
            result['WebIDEUrl'] = self.web_ideurl

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name

        if self.workspace_source is not None:
            result['WorkspaceSource'] = self.workspace_source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorType') is not None:
            self.accelerator_type = m.get('AcceleratorType')

        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')

        if m.get('AccumulatedRunningTimeInMs') is not None:
            self.accumulated_running_time_in_ms = m.get('AccumulatedRunningTimeInMs')

        if m.get('Affinity') is not None:
            temp_model = main_models.ListInstancesResponseBodyInstancesAffinity()
            self.affinity = temp_model.from_map(m.get('Affinity'))

        self.cloud_disks = []
        if m.get('CloudDisks') is not None:
            for k1 in m.get('CloudDisks'):
                temp_model = main_models.ListInstancesResponseBodyInstancesCloudDisks()
                self.cloud_disks.append(temp_model.from_map(k1))

        if m.get('CredentialConfig') is not None:
            temp_model = main_models.CredentialConfig()
            self.credential_config = temp_model.from_map(m.get('CredentialConfig'))

        self.datasets = []
        if m.get('Datasets') is not None:
            for k1 in m.get('Datasets'):
                temp_model = main_models.ListInstancesResponseBodyInstancesDatasets()
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

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('IdleInstanceCuller') is not None:
            temp_model = main_models.ListInstancesResponseBodyInstancesIdleInstanceCuller()
            self.idle_instance_culler = temp_model.from_map(m.get('IdleInstanceCuller'))

        if m.get('ImageAuth') is not None:
            self.image_auth = m.get('ImageAuth')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstanceShutdownTimer') is not None:
            temp_model = main_models.ListInstancesResponseBodyInstancesInstanceShutdownTimer()
            self.instance_shutdown_timer = temp_model.from_map(m.get('InstanceShutdownTimer'))

        self.instance_snapshot_list = []
        if m.get('InstanceSnapshotList') is not None:
            for k1 in m.get('InstanceSnapshotList'):
                temp_model = main_models.ListInstancesResponseBodyInstancesInstanceSnapshotList()
                self.instance_snapshot_list.append(temp_model.from_map(k1))

        if m.get('InstanceUrl') is not None:
            self.instance_url = m.get('InstanceUrl')

        if m.get('JupyterlabUrl') is not None:
            self.jupyterlab_url = m.get('JupyterlabUrl')

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.ListInstancesResponseBodyInstancesLabels()
                self.labels.append(temp_model.from_map(k1))

        if m.get('LatestSnapshot') is not None:
            temp_model = main_models.ListInstancesResponseBodyInstancesLatestSnapshot()
            self.latest_snapshot = temp_model.from_map(m.get('LatestSnapshot'))

        if m.get('OversoldInfo') is not None:
            self.oversold_info = m.get('OversoldInfo')

        if m.get('OversoldType') is not None:
            self.oversold_type = m.get('OversoldType')

        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')

        if m.get('ReasonMessage') is not None:
            self.reason_message = m.get('ReasonMessage')

        if m.get('RequestedResource') is not None:
            temp_model = main_models.ListInstancesResponseBodyInstancesRequestedResource()
            self.requested_resource = temp_model.from_map(m.get('RequestedResource'))

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')

        if m.get('ServiceConfig') is not None:
            temp_model = main_models.ServiceConfig()
            self.service_config = temp_model.from_map(m.get('ServiceConfig'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListInstancesResponseBodyInstancesTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TerminalUrl') is not None:
            self.terminal_url = m.get('TerminalUrl')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        if m.get('UserVpc') is not None:
            temp_model = main_models.ListInstancesResponseBodyInstancesUserVpc()
            self.user_vpc = temp_model.from_map(m.get('UserVpc'))

        if m.get('WebIDEUrl') is not None:
            self.web_ideurl = m.get('WebIDEUrl')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')

        if m.get('WorkspaceSource') is not None:
            self.workspace_source = m.get('WorkspaceSource')

        return self

class ListInstancesResponseBodyInstancesUserVpc(DaraModel):
    def __init__(
        self,
        bandwidth_limit: main_models.BandwidthLimit = None,
        default_route: str = None,
        extended_cidrs: List[str] = None,
        forward_infos: List[main_models.ForwardInfoResponse] = None,
        ip: str = None,
        security_group_id: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        self.bandwidth_limit = bandwidth_limit
        # The default route.
        self.default_route = default_route
        # The extended CIDR blocks.
        self.extended_cidrs = extended_cidrs
        # The forward information.
        self.forward_infos = forward_infos
        self.ip = ip
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

        if self.ip is not None:
            result['Ip'] = self.ip

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
                temp_model = main_models.ForwardInfoResponse()
                self.forward_infos.append(temp_model.from_map(k1))

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class ListInstancesResponseBodyInstancesTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

class ListInstancesResponseBodyInstancesRequestedResource(DaraModel):
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
        # The GPU memory type.
        self.gputype = gputype
        # The memory size.
        self.memory = memory
        # The size of the shared memory.
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

class ListInstancesResponseBodyInstancesLatestSnapshot(DaraModel):
    def __init__(
        self,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        image_id: str = None,
        image_name: str = None,
        image_url: str = None,
        reason_code: str = None,
        reason_message: str = None,
        repository_url: str = None,
        status: str = None,
    ):
        # The time when the snapshot was created.
        self.gmt_create_time = gmt_create_time
        # The time when the snapshot was modified.
        self.gmt_modified_time = gmt_modified_time
        # The image ID.
        self.image_id = image_id
        # The image name.
        self.image_name = image_name
        # The image URL.
        self.image_url = image_url
        # The error code of the instance snapshot.
        self.reason_code = reason_code
        # The error message of the instance snapshot.
        self.reason_message = reason_message
        # The URL of the image repository.
        self.repository_url = repository_url
        # The status of the instance snapshot.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_name is not None:
            result['ImageName'] = self.image_name

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code

        if self.reason_message is not None:
            result['ReasonMessage'] = self.reason_message

        if self.repository_url is not None:
            result['RepositoryUrl'] = self.repository_url

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')

        if m.get('ReasonMessage') is not None:
            self.reason_message = m.get('ReasonMessage')

        if m.get('RepositoryUrl') is not None:
            self.repository_url = m.get('RepositoryUrl')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class ListInstancesResponseBodyInstancesLabels(DaraModel):
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

class ListInstancesResponseBodyInstancesInstanceSnapshotList(DaraModel):
    def __init__(
        self,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        image_id: str = None,
        image_name: str = None,
        image_url: str = None,
        reason_code: str = None,
        reason_message: str = None,
        repository_url: str = None,
        status: str = None,
    ):
        # The time when the snapshot was created.
        self.gmt_create_time = gmt_create_time
        # The time when the snapshot was modified.
        self.gmt_modified_time = gmt_modified_time
        # The image ID.
        self.image_id = image_id
        # The image name.
        self.image_name = image_name
        # The image URL.
        self.image_url = image_url
        # The error code of the instance snapshot.
        self.reason_code = reason_code
        # The error message of the instance snapshot.
        self.reason_message = reason_message
        # The URL of the image repository.
        self.repository_url = repository_url
        # The status of the instance snapshot.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_name is not None:
            result['ImageName'] = self.image_name

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code

        if self.reason_message is not None:
            result['ReasonMessage'] = self.reason_message

        if self.repository_url is not None:
            result['RepositoryUrl'] = self.repository_url

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')

        if m.get('ReasonMessage') is not None:
            self.reason_message = m.get('ReasonMessage')

        if m.get('RepositoryUrl') is not None:
            self.repository_url = m.get('RepositoryUrl')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class ListInstancesResponseBodyInstancesInstanceShutdownTimer(DaraModel):
    def __init__(
        self,
        due_time: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        instance_id: str = None,
        remaining_time_in_ms: int = None,
    ):
        # The scheduled stop time.
        self.due_time = due_time
        # The time when the instance was created.
        self.gmt_create_time = gmt_create_time
        # The time when the instance was modified.
        self.gmt_modified_time = gmt_modified_time
        # The instance ID.
        self.instance_id = instance_id
        # The remaining time before the instance is stopped.
        self.remaining_time_in_ms = remaining_time_in_ms

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.due_time is not None:
            result['DueTime'] = self.due_time

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.remaining_time_in_ms is not None:
            result['RemainingTimeInMs'] = self.remaining_time_in_ms

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DueTime') is not None:
            self.due_time = m.get('DueTime')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RemainingTimeInMs') is not None:
            self.remaining_time_in_ms = m.get('RemainingTimeInMs')

        return self

class ListInstancesResponseBodyInstancesIdleInstanceCuller(DaraModel):
    def __init__(
        self,
        cpu_percent_threshold: int = None,
        gpu_percent_threshold: int = None,
        idle_time_in_minutes: int = None,
        instance_id: str = None,
        max_idle_time_in_minutes: int = None,
    ):
        # The CPU utilization threshold. Unit: percentage. Valid values: 1 to 100. If the CPU utilization of the instance is lower than this threshold, the instance is considered idle.
        self.cpu_percent_threshold = cpu_percent_threshold
        # The GPU utilization threshold. Unit: percentage. Valid values: 1 to 100. This parameter takes effect only if the instance is of the GPU instance type. If both CPU and GPU utilization is lower than the thresholds, the instance is considered idle.
        self.gpu_percent_threshold = gpu_percent_threshold
        # The time duration for which the instance is idle. Unit: minutes.
        self.idle_time_in_minutes = idle_time_in_minutes
        # The instance ID.
        self.instance_id = instance_id
        # The maximum time duration for which the instance is idle. Unit: minutes. If the time duration for which the instance is idle exceeds this value, the system automatically stops the instance.
        self.max_idle_time_in_minutes = max_idle_time_in_minutes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu_percent_threshold is not None:
            result['CpuPercentThreshold'] = self.cpu_percent_threshold

        if self.gpu_percent_threshold is not None:
            result['GpuPercentThreshold'] = self.gpu_percent_threshold

        if self.idle_time_in_minutes is not None:
            result['IdleTimeInMinutes'] = self.idle_time_in_minutes

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.max_idle_time_in_minutes is not None:
            result['MaxIdleTimeInMinutes'] = self.max_idle_time_in_minutes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuPercentThreshold') is not None:
            self.cpu_percent_threshold = m.get('CpuPercentThreshold')

        if m.get('GpuPercentThreshold') is not None:
            self.gpu_percent_threshold = m.get('GpuPercentThreshold')

        if m.get('IdleTimeInMinutes') is not None:
            self.idle_time_in_minutes = m.get('IdleTimeInMinutes')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MaxIdleTimeInMinutes') is not None:
            self.max_idle_time_in_minutes = m.get('MaxIdleTimeInMinutes')

        return self

class ListInstancesResponseBodyInstancesDatasets(DaraModel):
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
        # The dataset ID.
        self.dataset_id = dataset_id
        # The dataset version.
        self.dataset_version = dataset_version
        # Indicates whether dynamic mounting was enabled. Default value: false.
        self.dynamic = dynamic
        # The read and write permissions. Valid values: RW and RO.
        self.mount_access = mount_access
        # The mount path in the container.
        self.mount_path = mount_path
        # The type of the mount option.
        self.option_type = option_type
        # The mount type of the dataset.
        self.options = options
        # The dataset URI.
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

class ListInstancesResponseBodyInstancesCloudDisks(DaraModel):
    def __init__(
        self,
        capacity: str = None,
        mount_path: str = None,
        path: str = None,
        sub_type: str = None,
    ):
        # The cloud disk capacity.
        self.capacity = capacity
        # The mount path of the cloud disk in the container.
        self.mount_path = mount_path
        # The directory on the cloud disk that is mounted to the container.
        self.path = path
        # The cloud disk type. The value rootfs indicates that the cloud disk is used as the root file system (rootfs).
        self.sub_type = sub_type

    def validate(self):
        pass

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

        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')

        return self

class ListInstancesResponseBodyInstancesAffinity(DaraModel):
    def __init__(
        self,
        cpu: main_models.ListInstancesResponseBodyInstancesAffinityCPU = None,
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
            temp_model = main_models.ListInstancesResponseBodyInstancesAffinityCPU()
            self.cpu = temp_model.from_map(m.get('CPU'))

        return self

class ListInstancesResponseBodyInstancesAffinityCPU(DaraModel):
    def __init__(
        self,
        enable: bool = None,
    ):
        # Indicates whether the CPU affinity feature was enabled.
        # 
        # true false
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

