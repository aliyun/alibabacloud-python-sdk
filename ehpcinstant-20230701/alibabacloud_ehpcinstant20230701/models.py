# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AddImageRequestContainerImageSpecRegistryCredential(TeaModel):
    def __init__(
        self,
        password: str = None,
        server: str = None,
        user_name: str = None,
    ):
        self.password = password
        self.server = server
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.password is not None:
            result['Password'] = self.password
        if self.server is not None:
            result['Server'] = self.server
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Server') is not None:
            self.server = m.get('Server')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class AddImageRequestContainerImageSpec(TeaModel):
    def __init__(
        self,
        is_acrenterprise: bool = None,
        is_acrregistry: bool = None,
        registry_credential: AddImageRequestContainerImageSpecRegistryCredential = None,
        registry_cri_id: str = None,
        registry_url: str = None,
    ):
        self.is_acrenterprise = is_acrenterprise
        self.is_acrregistry = is_acrregistry
        self.registry_credential = registry_credential
        self.registry_cri_id = registry_cri_id
        self.registry_url = registry_url

    def validate(self):
        if self.registry_credential:
            self.registry_credential.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_acrenterprise is not None:
            result['IsACREnterprise'] = self.is_acrenterprise
        if self.is_acrregistry is not None:
            result['IsACRRegistry'] = self.is_acrregistry
        if self.registry_credential is not None:
            result['RegistryCredential'] = self.registry_credential.to_map()
        if self.registry_cri_id is not None:
            result['RegistryCriId'] = self.registry_cri_id
        if self.registry_url is not None:
            result['RegistryUrl'] = self.registry_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsACREnterprise') is not None:
            self.is_acrenterprise = m.get('IsACREnterprise')
        if m.get('IsACRRegistry') is not None:
            self.is_acrregistry = m.get('IsACRRegistry')
        if m.get('RegistryCredential') is not None:
            temp_model = AddImageRequestContainerImageSpecRegistryCredential()
            self.registry_credential = temp_model.from_map(m['RegistryCredential'])
        if m.get('RegistryCriId') is not None:
            self.registry_cri_id = m.get('RegistryCriId')
        if m.get('RegistryUrl') is not None:
            self.registry_url = m.get('RegistryUrl')
        return self


class AddImageRequestVMImageSpec(TeaModel):
    def __init__(
        self,
        image_id: str = None,
    ):
        self.image_id = image_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        return self


class AddImageRequest(TeaModel):
    def __init__(
        self,
        container_image_spec: AddImageRequestContainerImageSpec = None,
        description: str = None,
        image_type: str = None,
        image_version: str = None,
        name: str = None,
        vmimage_spec: AddImageRequestVMImageSpec = None,
    ):
        self.container_image_spec = container_image_spec
        self.description = description
        self.image_type = image_type
        self.image_version = image_version
        # This parameter is required.
        self.name = name
        self.vmimage_spec = vmimage_spec

    def validate(self):
        if self.container_image_spec:
            self.container_image_spec.validate()
        if self.vmimage_spec:
            self.vmimage_spec.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_image_spec is not None:
            result['ContainerImageSpec'] = self.container_image_spec.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.image_version is not None:
            result['ImageVersion'] = self.image_version
        if self.name is not None:
            result['Name'] = self.name
        if self.vmimage_spec is not None:
            result['VMImageSpec'] = self.vmimage_spec.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerImageSpec') is not None:
            temp_model = AddImageRequestContainerImageSpec()
            self.container_image_spec = temp_model.from_map(m['ContainerImageSpec'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('ImageVersion') is not None:
            self.image_version = m.get('ImageVersion')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('VMImageSpec') is not None:
            temp_model = AddImageRequestVMImageSpec()
            self.vmimage_spec = temp_model.from_map(m['VMImageSpec'])
        return self


class AddImageShrinkRequest(TeaModel):
    def __init__(
        self,
        container_image_spec_shrink: str = None,
        description: str = None,
        image_type: str = None,
        image_version: str = None,
        name: str = None,
        vmimage_spec_shrink: str = None,
    ):
        self.container_image_spec_shrink = container_image_spec_shrink
        self.description = description
        self.image_type = image_type
        self.image_version = image_version
        # This parameter is required.
        self.name = name
        self.vmimage_spec_shrink = vmimage_spec_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_image_spec_shrink is not None:
            result['ContainerImageSpec'] = self.container_image_spec_shrink
        if self.description is not None:
            result['Description'] = self.description
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.image_version is not None:
            result['ImageVersion'] = self.image_version
        if self.name is not None:
            result['Name'] = self.name
        if self.vmimage_spec_shrink is not None:
            result['VMImageSpec'] = self.vmimage_spec_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerImageSpec') is not None:
            self.container_image_spec_shrink = m.get('ContainerImageSpec')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('ImageVersion') is not None:
            self.image_version = m.get('ImageVersion')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('VMImageSpec') is not None:
            self.vmimage_spec_shrink = m.get('VMImageSpec')
        return self


class AddImageResponseBody(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.image_id = image_id
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddImageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateJobRequestDeploymentPolicyNetwork(TeaModel):
    def __init__(
        self,
        enable_external_ip_address: bool = None,
        vswitch: List[str] = None,
    ):
        self.enable_external_ip_address = enable_external_ip_address
        self.vswitch = vswitch

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_external_ip_address is not None:
            result['EnableExternalIpAddress'] = self.enable_external_ip_address
        if self.vswitch is not None:
            result['Vswitch'] = self.vswitch
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableExternalIpAddress') is not None:
            self.enable_external_ip_address = m.get('EnableExternalIpAddress')
        if m.get('Vswitch') is not None:
            self.vswitch = m.get('Vswitch')
        return self


class CreateJobRequestDeploymentPolicyTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # This parameter is required.
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateJobRequestDeploymentPolicy(TeaModel):
    def __init__(
        self,
        allocation_spec: str = None,
        level: str = None,
        network: CreateJobRequestDeploymentPolicyNetwork = None,
        pool: str = None,
        priority: int = None,
        tag: List[CreateJobRequestDeploymentPolicyTag] = None,
    ):
        self.allocation_spec = allocation_spec
        self.level = level
        self.network = network
        self.pool = pool
        self.priority = priority
        self.tag = tag

    def validate(self):
        if self.network:
            self.network.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allocation_spec is not None:
            result['AllocationSpec'] = self.allocation_spec
        if self.level is not None:
            result['Level'] = self.level
        if self.network is not None:
            result['Network'] = self.network.to_map()
        if self.pool is not None:
            result['Pool'] = self.pool
        if self.priority is not None:
            result['Priority'] = self.priority
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationSpec') is not None:
            self.allocation_spec = m.get('AllocationSpec')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Network') is not None:
            temp_model = CreateJobRequestDeploymentPolicyNetwork()
            self.network = temp_model.from_map(m['Network'])
        if m.get('Pool') is not None:
            self.pool = m.get('Pool')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateJobRequestDeploymentPolicyTag()
                self.tag.append(temp_model.from_map(k))
        return self


class CreateJobRequestSecurityPolicySecurityGroup(TeaModel):
    def __init__(
        self,
        security_group_ids: List[str] = None,
    ):
        self.security_group_ids = security_group_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')
        return self


class CreateJobRequestSecurityPolicy(TeaModel):
    def __init__(
        self,
        security_group: CreateJobRequestSecurityPolicySecurityGroup = None,
    ):
        self.security_group = security_group

    def validate(self):
        if self.security_group:
            self.security_group.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_group is not None:
            result['SecurityGroup'] = self.security_group.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityGroup') is not None:
            temp_model = CreateJobRequestSecurityPolicySecurityGroup()
            self.security_group = temp_model.from_map(m['SecurityGroup'])
        return self


class CreateJobRequestTasksExecutorPolicyArraySpec(TeaModel):
    def __init__(
        self,
        index_end: int = None,
        index_start: int = None,
        index_step: int = None,
    ):
        self.index_end = index_end
        self.index_start = index_start
        self.index_step = index_step

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index_end is not None:
            result['IndexEnd'] = self.index_end
        if self.index_start is not None:
            result['IndexStart'] = self.index_start
        if self.index_step is not None:
            result['IndexStep'] = self.index_step
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IndexEnd') is not None:
            self.index_end = m.get('IndexEnd')
        if m.get('IndexStart') is not None:
            self.index_start = m.get('IndexStart')
        if m.get('IndexStep') is not None:
            self.index_step = m.get('IndexStep')
        return self


class CreateJobRequestTasksExecutorPolicy(TeaModel):
    def __init__(
        self,
        array_spec: CreateJobRequestTasksExecutorPolicyArraySpec = None,
        max_count: int = None,
    ):
        self.array_spec = array_spec
        self.max_count = max_count

    def validate(self):
        if self.array_spec:
            self.array_spec.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.array_spec is not None:
            result['ArraySpec'] = self.array_spec.to_map()
        if self.max_count is not None:
            result['MaxCount'] = self.max_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArraySpec') is not None:
            temp_model = CreateJobRequestTasksExecutorPolicyArraySpec()
            self.array_spec = temp_model.from_map(m['ArraySpec'])
        if m.get('MaxCount') is not None:
            self.max_count = m.get('MaxCount')
        return self


class CreateJobRequestTasksTaskSpecResourceDisks(TeaModel):
    def __init__(
        self,
        size: int = None,
        type: str = None,
    ):
        self.size = size
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.size is not None:
            result['Size'] = self.size
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateJobRequestTasksTaskSpecResource(TeaModel):
    def __init__(
        self,
        cores: float = None,
        disks: List[CreateJobRequestTasksTaskSpecResourceDisks] = None,
        instance_types: List[str] = None,
        memory: float = None,
    ):
        self.cores = cores
        self.disks = disks
        self.instance_types = instance_types
        self.memory = memory

    def validate(self):
        if self.disks:
            for k in self.disks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cores is not None:
            result['Cores'] = self.cores
        result['Disks'] = []
        if self.disks is not None:
            for k in self.disks:
                result['Disks'].append(k.to_map() if k else None)
        if self.instance_types is not None:
            result['InstanceTypes'] = self.instance_types
        if self.memory is not None:
            result['Memory'] = self.memory
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cores') is not None:
            self.cores = m.get('Cores')
        self.disks = []
        if m.get('Disks') is not None:
            for k in m.get('Disks'):
                temp_model = CreateJobRequestTasksTaskSpecResourceDisks()
                self.disks.append(temp_model.from_map(k))
        if m.get('InstanceTypes') is not None:
            self.instance_types = m.get('InstanceTypes')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        return self


class CreateJobRequestTasksTaskSpecTaskExecutorContainerEnvironmentVars(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateJobRequestTasksTaskSpecTaskExecutorContainer(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        arg: List[str] = None,
        command: List[str] = None,
        environment_vars: List[CreateJobRequestTasksTaskSpecTaskExecutorContainerEnvironmentVars] = None,
        image: str = None,
        working_dir: str = None,
    ):
        self.app_id = app_id
        self.arg = arg
        self.command = command
        self.environment_vars = environment_vars
        # This parameter is required.
        self.image = image
        self.working_dir = working_dir

    def validate(self):
        if self.environment_vars:
            for k in self.environment_vars:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.arg is not None:
            result['Arg'] = self.arg
        if self.command is not None:
            result['Command'] = self.command
        result['EnvironmentVars'] = []
        if self.environment_vars is not None:
            for k in self.environment_vars:
                result['EnvironmentVars'].append(k.to_map() if k else None)
        if self.image is not None:
            result['Image'] = self.image
        if self.working_dir is not None:
            result['WorkingDir'] = self.working_dir
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Arg') is not None:
            self.arg = m.get('Arg')
        if m.get('Command') is not None:
            self.command = m.get('Command')
        self.environment_vars = []
        if m.get('EnvironmentVars') is not None:
            for k in m.get('EnvironmentVars'):
                temp_model = CreateJobRequestTasksTaskSpecTaskExecutorContainerEnvironmentVars()
                self.environment_vars.append(temp_model.from_map(k))
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')
        return self


class CreateJobRequestTasksTaskSpecTaskExecutorVM(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        image: str = None,
        password: str = None,
        prolog_script: str = None,
        script: str = None,
    ):
        self.app_id = app_id
        # This parameter is required.
        self.image = image
        self.password = password
        self.prolog_script = prolog_script
        self.script = script

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.image is not None:
            result['Image'] = self.image
        if self.password is not None:
            result['Password'] = self.password
        if self.prolog_script is not None:
            result['PrologScript'] = self.prolog_script
        if self.script is not None:
            result['Script'] = self.script
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('PrologScript') is not None:
            self.prolog_script = m.get('PrologScript')
        if m.get('Script') is not None:
            self.script = m.get('Script')
        return self


class CreateJobRequestTasksTaskSpecTaskExecutor(TeaModel):
    def __init__(
        self,
        container: CreateJobRequestTasksTaskSpecTaskExecutorContainer = None,
        vm: CreateJobRequestTasksTaskSpecTaskExecutorVM = None,
    ):
        self.container = container
        self.vm = vm

    def validate(self):
        if self.container:
            self.container.validate()
        if self.vm:
            self.vm.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container is not None:
            result['Container'] = self.container.to_map()
        if self.vm is not None:
            result['VM'] = self.vm.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Container') is not None:
            temp_model = CreateJobRequestTasksTaskSpecTaskExecutorContainer()
            self.container = temp_model.from_map(m['Container'])
        if m.get('VM') is not None:
            temp_model = CreateJobRequestTasksTaskSpecTaskExecutorVM()
            self.vm = temp_model.from_map(m['VM'])
        return self


class CreateJobRequestTasksTaskSpecVolumeMount(TeaModel):
    def __init__(
        self,
        mount_options: str = None,
        mount_path: str = None,
        read_only: bool = None,
        volume_driver: str = None,
    ):
        self.mount_options = mount_options
        self.mount_path = mount_path
        self.read_only = read_only
        self.volume_driver = volume_driver

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mount_options is not None:
            result['MountOptions'] = self.mount_options
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        if self.read_only is not None:
            result['ReadOnly'] = self.read_only
        if self.volume_driver is not None:
            result['VolumeDriver'] = self.volume_driver
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MountOptions') is not None:
            self.mount_options = m.get('MountOptions')
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        if m.get('ReadOnly') is not None:
            self.read_only = m.get('ReadOnly')
        if m.get('VolumeDriver') is not None:
            self.volume_driver = m.get('VolumeDriver')
        return self


class CreateJobRequestTasksTaskSpec(TeaModel):
    def __init__(
        self,
        resource: CreateJobRequestTasksTaskSpecResource = None,
        task_executor: List[CreateJobRequestTasksTaskSpecTaskExecutor] = None,
        volume_mount: List[CreateJobRequestTasksTaskSpecVolumeMount] = None,
    ):
        self.resource = resource
        # This parameter is required.
        self.task_executor = task_executor
        self.volume_mount = volume_mount

    def validate(self):
        if self.resource:
            self.resource.validate()
        if self.task_executor:
            for k in self.task_executor:
                if k:
                    k.validate()
        if self.volume_mount:
            for k in self.volume_mount:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource is not None:
            result['Resource'] = self.resource.to_map()
        result['TaskExecutor'] = []
        if self.task_executor is not None:
            for k in self.task_executor:
                result['TaskExecutor'].append(k.to_map() if k else None)
        result['VolumeMount'] = []
        if self.volume_mount is not None:
            for k in self.volume_mount:
                result['VolumeMount'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Resource') is not None:
            temp_model = CreateJobRequestTasksTaskSpecResource()
            self.resource = temp_model.from_map(m['Resource'])
        self.task_executor = []
        if m.get('TaskExecutor') is not None:
            for k in m.get('TaskExecutor'):
                temp_model = CreateJobRequestTasksTaskSpecTaskExecutor()
                self.task_executor.append(temp_model.from_map(k))
        self.volume_mount = []
        if m.get('VolumeMount') is not None:
            for k in m.get('VolumeMount'):
                temp_model = CreateJobRequestTasksTaskSpecVolumeMount()
                self.volume_mount.append(temp_model.from_map(k))
        return self


class CreateJobRequestTasks(TeaModel):
    def __init__(
        self,
        executor_policy: CreateJobRequestTasksExecutorPolicy = None,
        task_name: str = None,
        task_spec: CreateJobRequestTasksTaskSpec = None,
        task_sustainable: bool = None,
    ):
        self.executor_policy = executor_policy
        self.task_name = task_name
        self.task_spec = task_spec
        self.task_sustainable = task_sustainable

    def validate(self):
        if self.executor_policy:
            self.executor_policy.validate()
        if self.task_spec:
            self.task_spec.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.executor_policy is not None:
            result['ExecutorPolicy'] = self.executor_policy.to_map()
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.task_spec is not None:
            result['TaskSpec'] = self.task_spec.to_map()
        if self.task_sustainable is not None:
            result['TaskSustainable'] = self.task_sustainable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecutorPolicy') is not None:
            temp_model = CreateJobRequestTasksExecutorPolicy()
            self.executor_policy = temp_model.from_map(m['ExecutorPolicy'])
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TaskSpec') is not None:
            temp_model = CreateJobRequestTasksTaskSpec()
            self.task_spec = temp_model.from_map(m['TaskSpec'])
        if m.get('TaskSustainable') is not None:
            self.task_sustainable = m.get('TaskSustainable')
        return self


class CreateJobRequest(TeaModel):
    def __init__(
        self,
        deployment_policy: CreateJobRequestDeploymentPolicy = None,
        job_description: str = None,
        job_name: str = None,
        job_scheduler: str = None,
        security_policy: CreateJobRequestSecurityPolicy = None,
        tasks: List[CreateJobRequestTasks] = None,
    ):
        self.deployment_policy = deployment_policy
        self.job_description = job_description
        # This parameter is required.
        self.job_name = job_name
        self.job_scheduler = job_scheduler
        self.security_policy = security_policy
        # This parameter is required.
        self.tasks = tasks

    def validate(self):
        if self.deployment_policy:
            self.deployment_policy.validate()
        if self.security_policy:
            self.security_policy.validate()
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deployment_policy is not None:
            result['DeploymentPolicy'] = self.deployment_policy.to_map()
        if self.job_description is not None:
            result['JobDescription'] = self.job_description
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.job_scheduler is not None:
            result['JobScheduler'] = self.job_scheduler
        if self.security_policy is not None:
            result['SecurityPolicy'] = self.security_policy.to_map()
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeploymentPolicy') is not None:
            temp_model = CreateJobRequestDeploymentPolicy()
            self.deployment_policy = temp_model.from_map(m['DeploymentPolicy'])
        if m.get('JobDescription') is not None:
            self.job_description = m.get('JobDescription')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('JobScheduler') is not None:
            self.job_scheduler = m.get('JobScheduler')
        if m.get('SecurityPolicy') is not None:
            temp_model = CreateJobRequestSecurityPolicy()
            self.security_policy = temp_model.from_map(m['SecurityPolicy'])
        self.tasks = []
        if m.get('Tasks') is not None:
            for k in m.get('Tasks'):
                temp_model = CreateJobRequestTasks()
                self.tasks.append(temp_model.from_map(k))
        return self


class CreateJobShrinkRequest(TeaModel):
    def __init__(
        self,
        deployment_policy_shrink: str = None,
        job_description: str = None,
        job_name: str = None,
        job_scheduler: str = None,
        security_policy_shrink: str = None,
        tasks_shrink: str = None,
    ):
        self.deployment_policy_shrink = deployment_policy_shrink
        self.job_description = job_description
        # This parameter is required.
        self.job_name = job_name
        self.job_scheduler = job_scheduler
        self.security_policy_shrink = security_policy_shrink
        # This parameter is required.
        self.tasks_shrink = tasks_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deployment_policy_shrink is not None:
            result['DeploymentPolicy'] = self.deployment_policy_shrink
        if self.job_description is not None:
            result['JobDescription'] = self.job_description
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.job_scheduler is not None:
            result['JobScheduler'] = self.job_scheduler
        if self.security_policy_shrink is not None:
            result['SecurityPolicy'] = self.security_policy_shrink
        if self.tasks_shrink is not None:
            result['Tasks'] = self.tasks_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeploymentPolicy') is not None:
            self.deployment_policy_shrink = m.get('DeploymentPolicy')
        if m.get('JobDescription') is not None:
            self.job_description = m.get('JobDescription')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('JobScheduler') is not None:
            self.job_scheduler = m.get('JobScheduler')
        if m.get('SecurityPolicy') is not None:
            self.security_policy_shrink = m.get('SecurityPolicy')
        if m.get('Tasks') is not None:
            self.tasks_shrink = m.get('Tasks')
        return self


class CreateJobResponseBodyTasks(TeaModel):
    def __init__(
        self,
        executor_ids: List[str] = None,
        task_name: str = None,
    ):
        self.executor_ids = executor_ids
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.executor_ids is not None:
            result['ExecutorIds'] = self.executor_ids
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecutorIds') is not None:
            self.executor_ids = m.get('ExecutorIds')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class CreateJobResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
        tasks: List[CreateJobResponseBodyTasks] = None,
    ):
        self.job_id = job_id
        self.request_id = request_id
        self.tasks = tasks

    def validate(self):
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tasks = []
        if m.get('Tasks') is not None:
            for k in m.get('Tasks'):
                temp_model = CreateJobResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k))
        return self


class CreateJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePoolRequestResourceLimits(TeaModel):
    def __init__(
        self,
        max_exector_num: int = None,
    ):
        self.max_exector_num = max_exector_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_exector_num is not None:
            result['MaxExectorNum'] = self.max_exector_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxExectorNum') is not None:
            self.max_exector_num = m.get('MaxExectorNum')
        return self


class CreatePoolRequest(TeaModel):
    def __init__(
        self,
        pool_name: str = None,
        priority: int = None,
        resource_limits: CreatePoolRequestResourceLimits = None,
    ):
        # This parameter is required.
        self.pool_name = pool_name
        self.priority = priority
        self.resource_limits = resource_limits

    def validate(self):
        if self.resource_limits:
            self.resource_limits.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pool_name is not None:
            result['PoolName'] = self.pool_name
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.resource_limits is not None:
            result['ResourceLimits'] = self.resource_limits.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PoolName') is not None:
            self.pool_name = m.get('PoolName')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('ResourceLimits') is not None:
            temp_model = CreatePoolRequestResourceLimits()
            self.resource_limits = temp_model.from_map(m['ResourceLimits'])
        return self


class CreatePoolShrinkRequest(TeaModel):
    def __init__(
        self,
        pool_name: str = None,
        priority: int = None,
        resource_limits_shrink: str = None,
    ):
        # This parameter is required.
        self.pool_name = pool_name
        self.priority = priority
        self.resource_limits_shrink = resource_limits_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pool_name is not None:
            result['PoolName'] = self.pool_name
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.resource_limits_shrink is not None:
            result['ResourceLimits'] = self.resource_limits_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PoolName') is not None:
            self.pool_name = m.get('PoolName')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('ResourceLimits') is not None:
            self.resource_limits_shrink = m.get('ResourceLimits')
        return self


class CreatePoolResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreatePoolResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreatePoolResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreatePoolResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteJobsRequestJobSpecTaskSpec(TeaModel):
    def __init__(
        self,
        array_index: List[int] = None,
        task_name: str = None,
    ):
        self.array_index = array_index
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.array_index is not None:
            result['ArrayIndex'] = self.array_index
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArrayIndex') is not None:
            self.array_index = m.get('ArrayIndex')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class DeleteJobsRequestJobSpec(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        task_spec: List[DeleteJobsRequestJobSpecTaskSpec] = None,
    ):
        self.job_id = job_id
        self.task_spec = task_spec

    def validate(self):
        if self.task_spec:
            for k in self.task_spec:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        result['TaskSpec'] = []
        if self.task_spec is not None:
            for k in self.task_spec:
                result['TaskSpec'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        self.task_spec = []
        if m.get('TaskSpec') is not None:
            for k in m.get('TaskSpec'):
                temp_model = DeleteJobsRequestJobSpecTaskSpec()
                self.task_spec.append(temp_model.from_map(k))
        return self


class DeleteJobsRequest(TeaModel):
    def __init__(
        self,
        executor_ids: List[str] = None,
        job_scheduler: str = None,
        job_spec: List[DeleteJobsRequestJobSpec] = None,
    ):
        self.executor_ids = executor_ids
        self.job_scheduler = job_scheduler
        self.job_spec = job_spec

    def validate(self):
        if self.job_spec:
            for k in self.job_spec:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.executor_ids is not None:
            result['ExecutorIds'] = self.executor_ids
        if self.job_scheduler is not None:
            result['JobScheduler'] = self.job_scheduler
        result['JobSpec'] = []
        if self.job_spec is not None:
            for k in self.job_spec:
                result['JobSpec'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecutorIds') is not None:
            self.executor_ids = m.get('ExecutorIds')
        if m.get('JobScheduler') is not None:
            self.job_scheduler = m.get('JobScheduler')
        self.job_spec = []
        if m.get('JobSpec') is not None:
            for k in m.get('JobSpec'):
                temp_model = DeleteJobsRequestJobSpec()
                self.job_spec.append(temp_model.from_map(k))
        return self


class DeleteJobsShrinkRequest(TeaModel):
    def __init__(
        self,
        executor_ids_shrink: str = None,
        job_scheduler: str = None,
        job_spec_shrink: str = None,
    ):
        self.executor_ids_shrink = executor_ids_shrink
        self.job_scheduler = job_scheduler
        self.job_spec_shrink = job_spec_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.executor_ids_shrink is not None:
            result['ExecutorIds'] = self.executor_ids_shrink
        if self.job_scheduler is not None:
            result['JobScheduler'] = self.job_scheduler
        if self.job_spec_shrink is not None:
            result['JobSpec'] = self.job_spec_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecutorIds') is not None:
            self.executor_ids_shrink = m.get('ExecutorIds')
        if m.get('JobScheduler') is not None:
            self.job_scheduler = m.get('JobScheduler')
        if m.get('JobSpec') is not None:
            self.job_spec_shrink = m.get('JobSpec')
        return self


class DeleteJobsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteJobsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePoolRequest(TeaModel):
    def __init__(
        self,
        pool_name: str = None,
    ):
        # This parameter is required.
        self.pool_name = pool_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pool_name is not None:
            result['PoolName'] = self.pool_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PoolName') is not None:
            self.pool_name = m.get('PoolName')
        return self


class DeletePoolResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeletePoolResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeletePoolResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeletePoolResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeJobMetricDataRequest(TeaModel):
    def __init__(
        self,
        array_index: List[int] = None,
        job_id: str = None,
        metric_name: str = None,
        task_name: str = None,
    ):
        self.array_index = array_index
        self.job_id = job_id
        self.metric_name = metric_name
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.array_index is not None:
            result['ArrayIndex'] = self.array_index
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArrayIndex') is not None:
            self.array_index = m.get('ArrayIndex')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class DescribeJobMetricDataShrinkRequest(TeaModel):
    def __init__(
        self,
        array_index_shrink: str = None,
        job_id: str = None,
        metric_name: str = None,
        task_name: str = None,
    ):
        self.array_index_shrink = array_index_shrink
        self.job_id = job_id
        self.metric_name = metric_name
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.array_index_shrink is not None:
            result['ArrayIndex'] = self.array_index_shrink
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArrayIndex') is not None:
            self.array_index_shrink = m.get('ArrayIndex')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class DescribeJobMetricDataResponseBody(TeaModel):
    def __init__(
        self,
        data_points: str = None,
        period: int = None,
        request_id: str = None,
    ):
        self.data_points = data_points
        self.period = period
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_points is not None:
            result['DataPoints'] = self.data_points
        if self.period is not None:
            result['Period'] = self.period
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataPoints') is not None:
            self.data_points = m.get('DataPoints')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeJobMetricDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeJobMetricDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeJobMetricDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeJobMetricLastRequest(TeaModel):
    def __init__(
        self,
        array_index: List[int] = None,
        job_id: str = None,
        task_name: str = None,
    ):
        self.array_index = array_index
        self.job_id = job_id
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.array_index is not None:
            result['ArrayIndex'] = self.array_index
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArrayIndex') is not None:
            self.array_index = m.get('ArrayIndex')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class DescribeJobMetricLastShrinkRequest(TeaModel):
    def __init__(
        self,
        array_index_shrink: str = None,
        job_id: str = None,
        task_name: str = None,
    ):
        self.array_index_shrink = array_index_shrink
        self.job_id = job_id
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.array_index_shrink is not None:
            result['ArrayIndex'] = self.array_index_shrink
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArrayIndex') is not None:
            self.array_index_shrink = m.get('ArrayIndex')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class DescribeJobMetricLastResponseBodyMetrics(TeaModel):
    def __init__(
        self,
        array_index: int = None,
        metric: str = None,
    ):
        self.array_index = array_index
        self.metric = metric

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.array_index is not None:
            result['ArrayIndex'] = self.array_index
        if self.metric is not None:
            result['Metric'] = self.metric
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArrayIndex') is not None:
            self.array_index = m.get('ArrayIndex')
        if m.get('Metric') is not None:
            self.metric = m.get('Metric')
        return self


class DescribeJobMetricLastResponseBody(TeaModel):
    def __init__(
        self,
        metrics: List[DescribeJobMetricLastResponseBodyMetrics] = None,
        request_id: str = None,
    ):
        self.metrics = metrics
        self.request_id = request_id

    def validate(self):
        if self.metrics:
            for k in self.metrics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Metrics'] = []
        if self.metrics is not None:
            for k in self.metrics:
                result['Metrics'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.metrics = []
        if m.get('Metrics') is not None:
            for k in m.get('Metrics'):
                temp_model = DescribeJobMetricLastResponseBodyMetrics()
                self.metrics.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeJobMetricLastResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeJobMetricLastResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeJobMetricLastResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAppVersionsRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        image_category: str = None,
        image_type: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # This parameter is required.
        self.app_name = app_name
        self.image_category = image_category
        self.image_type = image_type
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.image_category is not None:
            result['ImageCategory'] = self.image_category
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ImageCategory') is not None:
            self.image_category = m.get('ImageCategory')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class GetAppVersionsResponseBodyAppVersions(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        name: str = None,
        version: str = None,
    ):
        # This parameter is required.
        self.image_id = image_id
        self.name = name
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.name is not None:
            result['Name'] = self.name
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetAppVersionsResponseBody(TeaModel):
    def __init__(
        self,
        app_versions: List[GetAppVersionsResponseBodyAppVersions] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.app_versions = app_versions
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.app_versions:
            for k in self.app_versions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AppVersions'] = []
        if self.app_versions is not None:
            for k in self.app_versions:
                result['AppVersions'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app_versions = []
        if m.get('AppVersions') is not None:
            for k in m.get('AppVersions'):
                temp_model = GetAppVersionsResponseBodyAppVersions()
                self.app_versions.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetAppVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAppVersionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAppVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetImageRequest(TeaModel):
    def __init__(
        self,
        additional_region_ids: List[str] = None,
        image_category: str = None,
        image_id: str = None,
        image_type: str = None,
    ):
        self.additional_region_ids = additional_region_ids
        self.image_category = image_category
        self.image_id = image_id
        self.image_type = image_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.additional_region_ids is not None:
            result['AdditionalRegionIds'] = self.additional_region_ids
        if self.image_category is not None:
            result['ImageCategory'] = self.image_category
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdditionalRegionIds') is not None:
            self.additional_region_ids = m.get('AdditionalRegionIds')
        if m.get('ImageCategory') is not None:
            self.image_category = m.get('ImageCategory')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        return self


class GetImageShrinkRequest(TeaModel):
    def __init__(
        self,
        additional_region_ids_shrink: str = None,
        image_category: str = None,
        image_id: str = None,
        image_type: str = None,
    ):
        self.additional_region_ids_shrink = additional_region_ids_shrink
        self.image_category = image_category
        self.image_id = image_id
        self.image_type = image_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.additional_region_ids_shrink is not None:
            result['AdditionalRegionIds'] = self.additional_region_ids_shrink
        if self.image_category is not None:
            result['ImageCategory'] = self.image_category
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdditionalRegionIds') is not None:
            self.additional_region_ids_shrink = m.get('AdditionalRegionIds')
        if m.get('ImageCategory') is not None:
            self.image_category = m.get('ImageCategory')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        return self


class GetImageResponseBodyImageAdditionalRegionsInfo(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        region_id: str = None,
        status: str = None,
    ):
        self.image_id = image_id
        self.region_id = region_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetImageResponseBodyImageContainerImageSpecRegistryCredential(TeaModel):
    def __init__(
        self,
        password: str = None,
        server: str = None,
        user_name: str = None,
    ):
        self.password = password
        self.server = server
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.password is not None:
            result['Password'] = self.password
        if self.server is not None:
            result['Server'] = self.server
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Server') is not None:
            self.server = m.get('Server')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class GetImageResponseBodyImageContainerImageSpec(TeaModel):
    def __init__(
        self,
        architecture: str = None,
        is_acrenterprise: bool = None,
        is_acrregistry: bool = None,
        os_tag: str = None,
        platform: str = None,
        registry_credential: GetImageResponseBodyImageContainerImageSpecRegistryCredential = None,
        registry_cri_id: str = None,
        registry_url: str = None,
    ):
        self.architecture = architecture
        self.is_acrenterprise = is_acrenterprise
        self.is_acrregistry = is_acrregistry
        self.os_tag = os_tag
        self.platform = platform
        self.registry_credential = registry_credential
        self.registry_cri_id = registry_cri_id
        self.registry_url = registry_url

    def validate(self):
        if self.registry_credential:
            self.registry_credential.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture is not None:
            result['Architecture'] = self.architecture
        if self.is_acrenterprise is not None:
            result['IsACREnterprise'] = self.is_acrenterprise
        if self.is_acrregistry is not None:
            result['IsACRRegistry'] = self.is_acrregistry
        if self.os_tag is not None:
            result['OsTag'] = self.os_tag
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.registry_credential is not None:
            result['RegistryCredential'] = self.registry_credential.to_map()
        if self.registry_cri_id is not None:
            result['RegistryCriId'] = self.registry_cri_id
        if self.registry_url is not None:
            result['RegistryUrl'] = self.registry_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Architecture') is not None:
            self.architecture = m.get('Architecture')
        if m.get('IsACREnterprise') is not None:
            self.is_acrenterprise = m.get('IsACREnterprise')
        if m.get('IsACRRegistry') is not None:
            self.is_acrregistry = m.get('IsACRRegistry')
        if m.get('OsTag') is not None:
            self.os_tag = m.get('OsTag')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('RegistryCredential') is not None:
            temp_model = GetImageResponseBodyImageContainerImageSpecRegistryCredential()
            self.registry_credential = temp_model.from_map(m['RegistryCredential'])
        if m.get('RegistryCriId') is not None:
            self.registry_cri_id = m.get('RegistryCriId')
        if m.get('RegistryUrl') is not None:
            self.registry_url = m.get('RegistryUrl')
        return self


class GetImageResponseBodyImageDocumentInfo(TeaModel):
    def __init__(
        self,
        document: str = None,
        document_id: str = None,
        encoding_mode: str = None,
    ):
        self.document = document
        self.document_id = document_id
        self.encoding_mode = encoding_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.document is not None:
            result['Document'] = self.document
        if self.document_id is not None:
            result['DocumentId'] = self.document_id
        if self.encoding_mode is not None:
            result['EncodingMode'] = self.encoding_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Document') is not None:
            self.document = m.get('Document')
        if m.get('DocumentId') is not None:
            self.document_id = m.get('DocumentId')
        if m.get('EncodingMode') is not None:
            self.encoding_mode = m.get('EncodingMode')
        return self


class GetImageResponseBodyImageVMImageSpec(TeaModel):
    def __init__(
        self,
        architecture: str = None,
        image_id: str = None,
        os_tag: str = None,
        platform: str = None,
    ):
        self.architecture = architecture
        self.image_id = image_id
        self.os_tag = os_tag
        self.platform = platform

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture is not None:
            result['Architecture'] = self.architecture
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.os_tag is not None:
            result['OsTag'] = self.os_tag
        if self.platform is not None:
            result['Platform'] = self.platform
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Architecture') is not None:
            self.architecture = m.get('Architecture')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('OsTag') is not None:
            self.os_tag = m.get('OsTag')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        return self


class GetImageResponseBodyImage(TeaModel):
    def __init__(
        self,
        additional_regions_info: List[GetImageResponseBodyImageAdditionalRegionsInfo] = None,
        app_id: str = None,
        container_image_spec: GetImageResponseBodyImageContainerImageSpec = None,
        create_time: str = None,
        description: str = None,
        document_info: GetImageResponseBodyImageDocumentInfo = None,
        image_type: str = None,
        name: str = None,
        size: str = None,
        status: str = None,
        vmimage_spec: GetImageResponseBodyImageVMImageSpec = None,
        version: str = None,
    ):
        self.additional_regions_info = additional_regions_info
        self.app_id = app_id
        self.container_image_spec = container_image_spec
        self.create_time = create_time
        self.description = description
        self.document_info = document_info
        # This parameter is required.
        self.image_type = image_type
        self.name = name
        self.size = size
        self.status = status
        self.vmimage_spec = vmimage_spec
        self.version = version

    def validate(self):
        if self.additional_regions_info:
            for k in self.additional_regions_info:
                if k:
                    k.validate()
        if self.container_image_spec:
            self.container_image_spec.validate()
        if self.document_info:
            self.document_info.validate()
        if self.vmimage_spec:
            self.vmimage_spec.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AdditionalRegionsInfo'] = []
        if self.additional_regions_info is not None:
            for k in self.additional_regions_info:
                result['AdditionalRegionsInfo'].append(k.to_map() if k else None)
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.container_image_spec is not None:
            result['ContainerImageSpec'] = self.container_image_spec.to_map()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.document_info is not None:
            result['DocumentInfo'] = self.document_info.to_map()
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.name is not None:
            result['Name'] = self.name
        if self.size is not None:
            result['Size'] = self.size
        if self.status is not None:
            result['Status'] = self.status
        if self.vmimage_spec is not None:
            result['VMImageSpec'] = self.vmimage_spec.to_map()
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.additional_regions_info = []
        if m.get('AdditionalRegionsInfo') is not None:
            for k in m.get('AdditionalRegionsInfo'):
                temp_model = GetImageResponseBodyImageAdditionalRegionsInfo()
                self.additional_regions_info.append(temp_model.from_map(k))
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ContainerImageSpec') is not None:
            temp_model = GetImageResponseBodyImageContainerImageSpec()
            self.container_image_spec = temp_model.from_map(m['ContainerImageSpec'])
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DocumentInfo') is not None:
            temp_model = GetImageResponseBodyImageDocumentInfo()
            self.document_info = temp_model.from_map(m['DocumentInfo'])
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VMImageSpec') is not None:
            temp_model = GetImageResponseBodyImageVMImageSpec()
            self.vmimage_spec = temp_model.from_map(m['VMImageSpec'])
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetImageResponseBody(TeaModel):
    def __init__(
        self,
        image: GetImageResponseBodyImage = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.image = image
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.image:
            self.image.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image is not None:
            result['Image'] = self.image.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Image') is not None:
            temp_model = GetImageResponseBodyImage()
            self.image = temp_model.from_map(m['Image'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetImageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJobRequest(TeaModel):
    def __init__(
        self,
        job_id: str = None,
    ):
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class GetJobResponseBodyJobInfoDeploymentPolicyNetwork(TeaModel):
    def __init__(
        self,
        enable_enimapping: bool = None,
        enable_external_ip_address: bool = None,
        vswitch: List[str] = None,
    ):
        self.enable_enimapping = enable_enimapping
        self.enable_external_ip_address = enable_external_ip_address
        self.vswitch = vswitch

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_enimapping is not None:
            result['EnableENIMapping'] = self.enable_enimapping
        if self.enable_external_ip_address is not None:
            result['EnableExternalIpAddress'] = self.enable_external_ip_address
        if self.vswitch is not None:
            result['Vswitch'] = self.vswitch
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableENIMapping') is not None:
            self.enable_enimapping = m.get('EnableENIMapping')
        if m.get('EnableExternalIpAddress') is not None:
            self.enable_external_ip_address = m.get('EnableExternalIpAddress')
        if m.get('Vswitch') is not None:
            self.vswitch = m.get('Vswitch')
        return self


class GetJobResponseBodyJobInfoDeploymentPolicyTags(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetJobResponseBodyJobInfoDeploymentPolicy(TeaModel):
    def __init__(
        self,
        allocation_spec: str = None,
        level: str = None,
        network: GetJobResponseBodyJobInfoDeploymentPolicyNetwork = None,
        tags: List[GetJobResponseBodyJobInfoDeploymentPolicyTags] = None,
    ):
        self.allocation_spec = allocation_spec
        self.level = level
        self.network = network
        self.tags = tags

    def validate(self):
        if self.network:
            self.network.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allocation_spec is not None:
            result['AllocationSpec'] = self.allocation_spec
        if self.level is not None:
            result['Level'] = self.level
        if self.network is not None:
            result['Network'] = self.network.to_map()
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationSpec') is not None:
            self.allocation_spec = m.get('AllocationSpec')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Network') is not None:
            temp_model = GetJobResponseBodyJobInfoDeploymentPolicyNetwork()
            self.network = temp_model.from_map(m['Network'])
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = GetJobResponseBodyJobInfoDeploymentPolicyTags()
                self.tags.append(temp_model.from_map(k))
        return self


class GetJobResponseBodyJobInfoTasksExecutorPolicyArraySpec(TeaModel):
    def __init__(
        self,
        index_end: int = None,
        index_start: int = None,
        index_step: int = None,
    ):
        self.index_end = index_end
        self.index_start = index_start
        self.index_step = index_step

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index_end is not None:
            result['IndexEnd'] = self.index_end
        if self.index_start is not None:
            result['IndexStart'] = self.index_start
        if self.index_step is not None:
            result['IndexStep'] = self.index_step
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IndexEnd') is not None:
            self.index_end = m.get('IndexEnd')
        if m.get('IndexStart') is not None:
            self.index_start = m.get('IndexStart')
        if m.get('IndexStep') is not None:
            self.index_step = m.get('IndexStep')
        return self


class GetJobResponseBodyJobInfoTasksExecutorPolicy(TeaModel):
    def __init__(
        self,
        array_spec: GetJobResponseBodyJobInfoTasksExecutorPolicyArraySpec = None,
        max_count: int = None,
    ):
        self.array_spec = array_spec
        self.max_count = max_count

    def validate(self):
        if self.array_spec:
            self.array_spec.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.array_spec is not None:
            result['ArraySpec'] = self.array_spec.to_map()
        if self.max_count is not None:
            result['MaxCount'] = self.max_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArraySpec') is not None:
            temp_model = GetJobResponseBodyJobInfoTasksExecutorPolicyArraySpec()
            self.array_spec = temp_model.from_map(m['ArraySpec'])
        if m.get('MaxCount') is not None:
            self.max_count = m.get('MaxCount')
        return self


class GetJobResponseBodyJobInfoTasksExecutorStatus(TeaModel):
    def __init__(
        self,
        array_id: int = None,
        create_time: str = None,
        end_time: str = None,
        start_time: str = None,
        status: str = None,
        status_reason: str = None,
    ):
        self.array_id = array_id
        self.create_time = create_time
        self.end_time = end_time
        self.start_time = start_time
        self.status = status
        self.status_reason = status_reason

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.array_id is not None:
            result['ArrayId'] = self.array_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArrayId') is not None:
            self.array_id = m.get('ArrayId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')
        return self


class GetJobResponseBodyJobInfoTasksTaskSpecResourceDisks(TeaModel):
    def __init__(
        self,
        size: int = None,
        type: str = None,
    ):
        self.size = size
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.size is not None:
            result['Size'] = self.size
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetJobResponseBodyJobInfoTasksTaskSpecResource(TeaModel):
    def __init__(
        self,
        cores: float = None,
        disks: List[GetJobResponseBodyJobInfoTasksTaskSpecResourceDisks] = None,
        instance_types: List[str] = None,
        memory: int = None,
    ):
        self.cores = cores
        self.disks = disks
        self.instance_types = instance_types
        self.memory = memory

    def validate(self):
        if self.disks:
            for k in self.disks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cores is not None:
            result['Cores'] = self.cores
        result['Disks'] = []
        if self.disks is not None:
            for k in self.disks:
                result['Disks'].append(k.to_map() if k else None)
        if self.instance_types is not None:
            result['InstanceTypes'] = self.instance_types
        if self.memory is not None:
            result['Memory'] = self.memory
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cores') is not None:
            self.cores = m.get('Cores')
        self.disks = []
        if m.get('Disks') is not None:
            for k in m.get('Disks'):
                temp_model = GetJobResponseBodyJobInfoTasksTaskSpecResourceDisks()
                self.disks.append(temp_model.from_map(k))
        if m.get('InstanceTypes') is not None:
            self.instance_types = m.get('InstanceTypes')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        return self


class GetJobResponseBodyJobInfoTasksTaskSpecTaskExecutorVM(TeaModel):
    def __init__(
        self,
        image: str = None,
        prolog_script: str = None,
        script: str = None,
        user_name: str = None,
    ):
        self.image = image
        self.prolog_script = prolog_script
        self.script = script
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image is not None:
            result['Image'] = self.image
        if self.prolog_script is not None:
            result['PrologScript'] = self.prolog_script
        if self.script is not None:
            result['Script'] = self.script
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('PrologScript') is not None:
            self.prolog_script = m.get('PrologScript')
        if m.get('Script') is not None:
            self.script = m.get('Script')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class GetJobResponseBodyJobInfoTasksTaskSpecTaskExecutor(TeaModel):
    def __init__(
        self,
        vm: GetJobResponseBodyJobInfoTasksTaskSpecTaskExecutorVM = None,
    ):
        self.vm = vm

    def validate(self):
        if self.vm:
            self.vm.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vm is not None:
            result['VM'] = self.vm.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VM') is not None:
            temp_model = GetJobResponseBodyJobInfoTasksTaskSpecTaskExecutorVM()
            self.vm = temp_model.from_map(m['VM'])
        return self


class GetJobResponseBodyJobInfoTasksTaskSpec(TeaModel):
    def __init__(
        self,
        resource: GetJobResponseBodyJobInfoTasksTaskSpecResource = None,
        task_executor: List[GetJobResponseBodyJobInfoTasksTaskSpecTaskExecutor] = None,
    ):
        self.resource = resource
        self.task_executor = task_executor

    def validate(self):
        if self.resource:
            self.resource.validate()
        if self.task_executor:
            for k in self.task_executor:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource is not None:
            result['Resource'] = self.resource.to_map()
        result['TaskExecutor'] = []
        if self.task_executor is not None:
            for k in self.task_executor:
                result['TaskExecutor'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Resource') is not None:
            temp_model = GetJobResponseBodyJobInfoTasksTaskSpecResource()
            self.resource = temp_model.from_map(m['Resource'])
        self.task_executor = []
        if m.get('TaskExecutor') is not None:
            for k in m.get('TaskExecutor'):
                temp_model = GetJobResponseBodyJobInfoTasksTaskSpecTaskExecutor()
                self.task_executor.append(temp_model.from_map(k))
        return self


class GetJobResponseBodyJobInfoTasks(TeaModel):
    def __init__(
        self,
        executor_policy: GetJobResponseBodyJobInfoTasksExecutorPolicy = None,
        executor_status: List[GetJobResponseBodyJobInfoTasksExecutorStatus] = None,
        task_name: str = None,
        task_spec: GetJobResponseBodyJobInfoTasksTaskSpec = None,
        task_sustainable: bool = None,
    ):
        self.executor_policy = executor_policy
        self.executor_status = executor_status
        self.task_name = task_name
        self.task_spec = task_spec
        self.task_sustainable = task_sustainable

    def validate(self):
        if self.executor_policy:
            self.executor_policy.validate()
        if self.executor_status:
            for k in self.executor_status:
                if k:
                    k.validate()
        if self.task_spec:
            self.task_spec.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.executor_policy is not None:
            result['ExecutorPolicy'] = self.executor_policy.to_map()
        result['ExecutorStatus'] = []
        if self.executor_status is not None:
            for k in self.executor_status:
                result['ExecutorStatus'].append(k.to_map() if k else None)
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.task_spec is not None:
            result['TaskSpec'] = self.task_spec.to_map()
        if self.task_sustainable is not None:
            result['TaskSustainable'] = self.task_sustainable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecutorPolicy') is not None:
            temp_model = GetJobResponseBodyJobInfoTasksExecutorPolicy()
            self.executor_policy = temp_model.from_map(m['ExecutorPolicy'])
        self.executor_status = []
        if m.get('ExecutorStatus') is not None:
            for k in m.get('ExecutorStatus'):
                temp_model = GetJobResponseBodyJobInfoTasksExecutorStatus()
                self.executor_status.append(temp_model.from_map(k))
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TaskSpec') is not None:
            temp_model = GetJobResponseBodyJobInfoTasksTaskSpec()
            self.task_spec = temp_model.from_map(m['TaskSpec'])
        if m.get('TaskSustainable') is not None:
            self.task_sustainable = m.get('TaskSustainable')
        return self


class GetJobResponseBodyJobInfo(TeaModel):
    def __init__(
        self,
        app_extra_info: str = None,
        create_time: str = None,
        deployment_policy: GetJobResponseBodyJobInfoDeploymentPolicy = None,
        end_time: str = None,
        job_description: str = None,
        job_id: str = None,
        job_name: str = None,
        job_scheduler: str = None,
        start_time: str = None,
        status: str = None,
        tasks: List[GetJobResponseBodyJobInfoTasks] = None,
    ):
        self.app_extra_info = app_extra_info
        self.create_time = create_time
        self.deployment_policy = deployment_policy
        self.end_time = end_time
        self.job_description = job_description
        self.job_id = job_id
        self.job_name = job_name
        self.job_scheduler = job_scheduler
        self.start_time = start_time
        self.status = status
        self.tasks = tasks

    def validate(self):
        if self.deployment_policy:
            self.deployment_policy.validate()
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_extra_info is not None:
            result['AppExtraInfo'] = self.app_extra_info
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deployment_policy is not None:
            result['DeploymentPolicy'] = self.deployment_policy.to_map()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.job_description is not None:
            result['JobDescription'] = self.job_description
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.job_scheduler is not None:
            result['JobScheduler'] = self.job_scheduler
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppExtraInfo') is not None:
            self.app_extra_info = m.get('AppExtraInfo')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DeploymentPolicy') is not None:
            temp_model = GetJobResponseBodyJobInfoDeploymentPolicy()
            self.deployment_policy = temp_model.from_map(m['DeploymentPolicy'])
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('JobDescription') is not None:
            self.job_description = m.get('JobDescription')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('JobScheduler') is not None:
            self.job_scheduler = m.get('JobScheduler')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tasks = []
        if m.get('Tasks') is not None:
            for k in m.get('Tasks'):
                temp_model = GetJobResponseBodyJobInfoTasks()
                self.tasks.append(temp_model.from_map(k))
        return self


class GetJobResponseBody(TeaModel):
    def __init__(
        self,
        job_info: GetJobResponseBodyJobInfo = None,
        request_id: str = None,
    ):
        self.job_info = job_info
        self.request_id = request_id

    def validate(self):
        if self.job_info:
            self.job_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_info is not None:
            result['JobInfo'] = self.job_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobInfo') is not None:
            temp_model = GetJobResponseBodyJobInfo()
            self.job_info = temp_model.from_map(m['JobInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPoolRequest(TeaModel):
    def __init__(
        self,
        pool_name: str = None,
    ):
        # This parameter is required.
        self.pool_name = pool_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pool_name is not None:
            result['PoolName'] = self.pool_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PoolName') is not None:
            self.pool_name = m.get('PoolName')
        return self


class GetPoolResponseBodyPoolInfo(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        exector_usage: int = None,
        is_default: bool = None,
        max_exector_num: int = None,
        pool_name: str = None,
        priority: int = None,
        reason: str = None,
        status: str = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        self.exector_usage = exector_usage
        self.is_default = is_default
        self.max_exector_num = max_exector_num
        self.pool_name = pool_name
        self.priority = priority
        self.reason = reason
        self.status = status
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.exector_usage is not None:
            result['ExectorUsage'] = self.exector_usage
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.max_exector_num is not None:
            result['MaxExectorNum'] = self.max_exector_num
        if self.pool_name is not None:
            result['PoolName'] = self.pool_name
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExectorUsage') is not None:
            self.exector_usage = m.get('ExectorUsage')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('MaxExectorNum') is not None:
            self.max_exector_num = m.get('MaxExectorNum')
        if m.get('PoolName') is not None:
            self.pool_name = m.get('PoolName')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class GetPoolResponseBody(TeaModel):
    def __init__(
        self,
        pool_info: GetPoolResponseBodyPoolInfo = None,
        request_id: str = None,
    ):
        self.pool_info = pool_info
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.pool_info:
            self.pool_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pool_info is not None:
            result['PoolInfo'] = self.pool_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PoolInfo') is not None:
            temp_model = GetPoolResponseBodyPoolInfo()
            self.pool_info = temp_model.from_map(m['PoolInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPoolResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPoolResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetPoolResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListExecutorsRequestFilter(TeaModel):
    def __init__(
        self,
        executor_ids: List[str] = None,
        image: str = None,
        ip_addresses: List[str] = None,
        job_name: str = None,
        status: List[str] = None,
        time_created_after: int = None,
        time_created_before: int = None,
        vswitch_id: str = None,
    ):
        self.executor_ids = executor_ids
        self.image = image
        self.ip_addresses = ip_addresses
        self.job_name = job_name
        self.status = status
        self.time_created_after = time_created_after
        self.time_created_before = time_created_before
        self.vswitch_id = vswitch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.executor_ids is not None:
            result['ExecutorIds'] = self.executor_ids
        if self.image is not None:
            result['Image'] = self.image
        if self.ip_addresses is not None:
            result['IpAddresses'] = self.ip_addresses
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.status is not None:
            result['Status'] = self.status
        if self.time_created_after is not None:
            result['TimeCreatedAfter'] = self.time_created_after
        if self.time_created_before is not None:
            result['TimeCreatedBefore'] = self.time_created_before
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecutorIds') is not None:
            self.executor_ids = m.get('ExecutorIds')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('IpAddresses') is not None:
            self.ip_addresses = m.get('IpAddresses')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TimeCreatedAfter') is not None:
            self.time_created_after = m.get('TimeCreatedAfter')
        if m.get('TimeCreatedBefore') is not None:
            self.time_created_before = m.get('TimeCreatedBefore')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        return self


class ListExecutorsRequest(TeaModel):
    def __init__(
        self,
        filter: ListExecutorsRequestFilter = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.filter = filter
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        if self.filter:
            self.filter.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter is not None:
            result['Filter'] = self.filter.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Filter') is not None:
            temp_model = ListExecutorsRequestFilter()
            self.filter = temp_model.from_map(m['Filter'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListExecutorsShrinkRequest(TeaModel):
    def __init__(
        self,
        filter_shrink: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.filter_shrink = filter_shrink
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter_shrink is not None:
            result['Filter'] = self.filter_shrink
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Filter') is not None:
            self.filter_shrink = m.get('Filter')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListExecutorsResponseBodyExecutorsResourceDisks(TeaModel):
    def __init__(
        self,
        size: int = None,
        type: str = None,
    ):
        self.size = size
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.size is not None:
            result['Size'] = self.size
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListExecutorsResponseBodyExecutorsResource(TeaModel):
    def __init__(
        self,
        cores: float = None,
        disks: List[ListExecutorsResponseBodyExecutorsResourceDisks] = None,
        memory: float = None,
    ):
        self.cores = cores
        self.disks = disks
        self.memory = memory

    def validate(self):
        if self.disks:
            for k in self.disks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cores is not None:
            result['Cores'] = self.cores
        result['Disks'] = []
        if self.disks is not None:
            for k in self.disks:
                result['Disks'].append(k.to_map() if k else None)
        if self.memory is not None:
            result['Memory'] = self.memory
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cores') is not None:
            self.cores = m.get('Cores')
        self.disks = []
        if m.get('Disks') is not None:
            for k in m.get('Disks'):
                temp_model = ListExecutorsResponseBodyExecutorsResourceDisks()
                self.disks.append(temp_model.from_map(k))
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        return self


class ListExecutorsResponseBodyExecutorsTags(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListExecutorsResponseBodyExecutors(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        array_index: int = None,
        create_time: str = None,
        end_time: str = None,
        executor_id: str = None,
        expiration_time: str = None,
        external_ip_address: List[str] = None,
        host_name: List[str] = None,
        image: str = None,
        ip_address: List[str] = None,
        job_id: str = None,
        job_name: str = None,
        resource: ListExecutorsResponseBodyExecutorsResource = None,
        resource_type: str = None,
        start_time: str = None,
        status: str = None,
        status_reason: str = None,
        tags: List[ListExecutorsResponseBodyExecutorsTags] = None,
        task_name: str = None,
        task_sustainable: bool = None,
        vswitch_id: str = None,
    ):
        self.app_name = app_name
        self.array_index = array_index
        self.create_time = create_time
        self.end_time = end_time
        self.executor_id = executor_id
        self.expiration_time = expiration_time
        self.external_ip_address = external_ip_address
        self.host_name = host_name
        self.image = image
        self.ip_address = ip_address
        self.job_id = job_id
        self.job_name = job_name
        self.resource = resource
        self.resource_type = resource_type
        self.start_time = start_time
        self.status = status
        self.status_reason = status_reason
        self.tags = tags
        self.task_name = task_name
        self.task_sustainable = task_sustainable
        self.vswitch_id = vswitch_id

    def validate(self):
        if self.resource:
            self.resource.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.array_index is not None:
            result['ArrayIndex'] = self.array_index
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.executor_id is not None:
            result['ExecutorId'] = self.executor_id
        if self.expiration_time is not None:
            result['ExpirationTime'] = self.expiration_time
        if self.external_ip_address is not None:
            result['ExternalIpAddress'] = self.external_ip_address
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.image is not None:
            result['Image'] = self.image
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.resource is not None:
            result['Resource'] = self.resource.to_map()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.task_sustainable is not None:
            result['TaskSustainable'] = self.task_sustainable
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ArrayIndex') is not None:
            self.array_index = m.get('ArrayIndex')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExecutorId') is not None:
            self.executor_id = m.get('ExecutorId')
        if m.get('ExpirationTime') is not None:
            self.expiration_time = m.get('ExpirationTime')
        if m.get('ExternalIpAddress') is not None:
            self.external_ip_address = m.get('ExternalIpAddress')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('Resource') is not None:
            temp_model = ListExecutorsResponseBodyExecutorsResource()
            self.resource = temp_model.from_map(m['Resource'])
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListExecutorsResponseBodyExecutorsTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TaskSustainable') is not None:
            self.task_sustainable = m.get('TaskSustainable')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        return self


class ListExecutorsResponseBody(TeaModel):
    def __init__(
        self,
        executors: List[ListExecutorsResponseBodyExecutors] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: str = None,
    ):
        self.executors = executors
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.executors:
            for k in self.executors:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Executors'] = []
        if self.executors is not None:
            for k in self.executors:
                result['Executors'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.executors = []
        if m.get('Executors') is not None:
            for k in m.get('Executors'):
                temp_model = ListExecutorsResponseBodyExecutors()
                self.executors.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListExecutorsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListExecutorsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListExecutorsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListImagesRequest(TeaModel):
    def __init__(
        self,
        image_category: str = None,
        image_ids: List[str] = None,
        image_names: List[str] = None,
        image_type: str = None,
        mode: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.image_category = image_category
        self.image_ids = image_ids
        self.image_names = image_names
        self.image_type = image_type
        self.mode = mode
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_category is not None:
            result['ImageCategory'] = self.image_category
        if self.image_ids is not None:
            result['ImageIds'] = self.image_ids
        if self.image_names is not None:
            result['ImageNames'] = self.image_names
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageCategory') is not None:
            self.image_category = m.get('ImageCategory')
        if m.get('ImageIds') is not None:
            self.image_ids = m.get('ImageIds')
        if m.get('ImageNames') is not None:
            self.image_names = m.get('ImageNames')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListImagesShrinkRequest(TeaModel):
    def __init__(
        self,
        image_category: str = None,
        image_ids_shrink: str = None,
        image_names_shrink: str = None,
        image_type: str = None,
        mode: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.image_category = image_category
        self.image_ids_shrink = image_ids_shrink
        self.image_names_shrink = image_names_shrink
        self.image_type = image_type
        self.mode = mode
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_category is not None:
            result['ImageCategory'] = self.image_category
        if self.image_ids_shrink is not None:
            result['ImageIds'] = self.image_ids_shrink
        if self.image_names_shrink is not None:
            result['ImageNames'] = self.image_names_shrink
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageCategory') is not None:
            self.image_category = m.get('ImageCategory')
        if m.get('ImageIds') is not None:
            self.image_ids_shrink = m.get('ImageIds')
        if m.get('ImageNames') is not None:
            self.image_names_shrink = m.get('ImageNames')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListImagesResponseBodyImages(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        create_time: str = None,
        description: str = None,
        document_id: int = None,
        image_id: str = None,
        image_type: str = None,
        name: str = None,
        os_tag: str = None,
        update_time: str = None,
        version: str = None,
        weight: int = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.create_time = create_time
        self.description = description
        self.document_id = document_id
        # This parameter is required.
        self.image_id = image_id
        # This parameter is required.
        self.image_type = image_type
        self.name = name
        self.os_tag = os_tag
        self.update_time = update_time
        self.version = version
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.document_id is not None:
            result['DocumentId'] = self.document_id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.name is not None:
            result['Name'] = self.name
        if self.os_tag is not None:
            result['OsTag'] = self.os_tag
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.version is not None:
            result['Version'] = self.version
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DocumentId') is not None:
            self.document_id = m.get('DocumentId')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OsTag') is not None:
            self.os_tag = m.get('OsTag')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class ListImagesResponseBody(TeaModel):
    def __init__(
        self,
        images: List[ListImagesResponseBodyImages] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.images = images
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.images:
            for k in self.images:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Images'] = []
        if self.images is not None:
            for k in self.images:
                result['Images'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.images = []
        if m.get('Images') is not None:
            for k in m.get('Images'):
                temp_model = ListImagesResponseBodyImages()
                self.images.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListImagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListImagesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListImagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListJobExecutorsRequest(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        page_number: int = None,
        page_size: int = None,
        task_name: str = None,
    ):
        self.job_id = job_id
        self.page_number = page_number
        self.page_size = page_size
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class ListJobExecutorsResponseBodyExecutorStatus(TeaModel):
    def __init__(
        self,
        deleted: int = None,
        exception: int = None,
        failed: int = None,
        initing: int = None,
        pending: int = None,
        running: int = None,
        succeeded: int = None,
    ):
        self.deleted = deleted
        self.exception = exception
        self.failed = failed
        self.initing = initing
        self.pending = pending
        self.running = running
        self.succeeded = succeeded

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.exception is not None:
            result['Exception'] = self.exception
        if self.failed is not None:
            result['Failed'] = self.failed
        if self.initing is not None:
            result['Initing'] = self.initing
        if self.pending is not None:
            result['Pending'] = self.pending
        if self.running is not None:
            result['Running'] = self.running
        if self.succeeded is not None:
            result['Succeeded'] = self.succeeded
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('Exception') is not None:
            self.exception = m.get('Exception')
        if m.get('Failed') is not None:
            self.failed = m.get('Failed')
        if m.get('Initing') is not None:
            self.initing = m.get('Initing')
        if m.get('Pending') is not None:
            self.pending = m.get('Pending')
        if m.get('Running') is not None:
            self.running = m.get('Running')
        if m.get('Succeeded') is not None:
            self.succeeded = m.get('Succeeded')
        return self


class ListJobExecutorsResponseBodyExecutorsTags(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListJobExecutorsResponseBodyExecutors(TeaModel):
    def __init__(
        self,
        array_index: int = None,
        create_time: str = None,
        end_time: str = None,
        executor_id: str = None,
        expiration_time: str = None,
        external_ip_address: List[str] = None,
        host_name: List[str] = None,
        ip_address: List[str] = None,
        start_time: str = None,
        status: str = None,
        status_reason: str = None,
        tags: List[ListJobExecutorsResponseBodyExecutorsTags] = None,
    ):
        self.array_index = array_index
        self.create_time = create_time
        self.end_time = end_time
        self.executor_id = executor_id
        self.expiration_time = expiration_time
        self.external_ip_address = external_ip_address
        self.host_name = host_name
        self.ip_address = ip_address
        self.start_time = start_time
        self.status = status
        self.status_reason = status_reason
        self.tags = tags

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.array_index is not None:
            result['ArrayIndex'] = self.array_index
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.executor_id is not None:
            result['ExecutorId'] = self.executor_id
        if self.expiration_time is not None:
            result['ExpirationTime'] = self.expiration_time
        if self.external_ip_address is not None:
            result['ExternalIpAddress'] = self.external_ip_address
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArrayIndex') is not None:
            self.array_index = m.get('ArrayIndex')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExecutorId') is not None:
            self.executor_id = m.get('ExecutorId')
        if m.get('ExpirationTime') is not None:
            self.expiration_time = m.get('ExpirationTime')
        if m.get('ExternalIpAddress') is not None:
            self.external_ip_address = m.get('ExternalIpAddress')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListJobExecutorsResponseBodyExecutorsTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListJobExecutorsResponseBody(TeaModel):
    def __init__(
        self,
        executor_status: ListJobExecutorsResponseBodyExecutorStatus = None,
        executors: List[ListJobExecutorsResponseBodyExecutors] = None,
        job_id: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        task_name: str = None,
        total_count: str = None,
    ):
        self.executor_status = executor_status
        self.executors = executors
        self.job_id = job_id
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.task_name = task_name
        self.total_count = total_count

    def validate(self):
        if self.executor_status:
            self.executor_status.validate()
        if self.executors:
            for k in self.executors:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.executor_status is not None:
            result['ExecutorStatus'] = self.executor_status.to_map()
        result['Executors'] = []
        if self.executors is not None:
            for k in self.executors:
                result['Executors'].append(k.to_map() if k else None)
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecutorStatus') is not None:
            temp_model = ListJobExecutorsResponseBodyExecutorStatus()
            self.executor_status = temp_model.from_map(m['ExecutorStatus'])
        self.executors = []
        if m.get('Executors') is not None:
            for k in m.get('Executors'):
                temp_model = ListJobExecutorsResponseBodyExecutors()
                self.executors.append(temp_model.from_map(k))
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListJobExecutorsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListJobExecutorsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListJobExecutorsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListJobsRequestFilter(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        job_name: str = None,
        status: str = None,
        time_created_after: int = None,
        time_created_before: int = None,
    ):
        self.job_id = job_id
        self.job_name = job_name
        self.status = status
        self.time_created_after = time_created_after
        self.time_created_before = time_created_before

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.status is not None:
            result['Status'] = self.status
        if self.time_created_after is not None:
            result['TimeCreatedAfter'] = self.time_created_after
        if self.time_created_before is not None:
            result['TimeCreatedBefore'] = self.time_created_before
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TimeCreatedAfter') is not None:
            self.time_created_after = m.get('TimeCreatedAfter')
        if m.get('TimeCreatedBefore') is not None:
            self.time_created_before = m.get('TimeCreatedBefore')
        return self


class ListJobsRequestSortBy(TeaModel):
    def __init__(
        self,
        label: str = None,
        order: str = None,
    ):
        self.label = label
        self.order = order

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.order is not None:
            result['Order'] = self.order
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        return self


class ListJobsRequest(TeaModel):
    def __init__(
        self,
        filter: ListJobsRequestFilter = None,
        page_number: int = None,
        page_size: int = None,
        sort_by: ListJobsRequestSortBy = None,
    ):
        self.filter = filter
        self.page_number = page_number
        self.page_size = page_size
        self.sort_by = sort_by

    def validate(self):
        if self.filter:
            self.filter.validate()
        if self.sort_by:
            self.sort_by.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter is not None:
            result['Filter'] = self.filter.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Filter') is not None:
            temp_model = ListJobsRequestFilter()
            self.filter = temp_model.from_map(m['Filter'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            temp_model = ListJobsRequestSortBy()
            self.sort_by = temp_model.from_map(m['SortBy'])
        return self


class ListJobsShrinkRequest(TeaModel):
    def __init__(
        self,
        filter_shrink: str = None,
        page_number: int = None,
        page_size: int = None,
        sort_by_shrink: str = None,
    ):
        self.filter_shrink = filter_shrink
        self.page_number = page_number
        self.page_size = page_size
        self.sort_by_shrink = sort_by_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter_shrink is not None:
            result['Filter'] = self.filter_shrink
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by_shrink is not None:
            result['SortBy'] = self.sort_by_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Filter') is not None:
            self.filter_shrink = m.get('Filter')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by_shrink = m.get('SortBy')
        return self


class ListJobsResponseBodyJobListTags(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListJobsResponseBodyJobList(TeaModel):
    def __init__(
        self,
        app_extra_info: str = None,
        app_name: str = None,
        create_time: str = None,
        end_time: str = None,
        executor_count: int = None,
        job_description: str = None,
        job_id: str = None,
        job_name: str = None,
        owner_uid: str = None,
        start_time: str = None,
        status: str = None,
        tags: List[ListJobsResponseBodyJobListTags] = None,
        task_count: int = None,
        task_sustainable: bool = None,
    ):
        self.app_extra_info = app_extra_info
        self.app_name = app_name
        self.create_time = create_time
        self.end_time = end_time
        self.executor_count = executor_count
        self.job_description = job_description
        self.job_id = job_id
        self.job_name = job_name
        self.owner_uid = owner_uid
        self.start_time = start_time
        self.status = status
        self.tags = tags
        self.task_count = task_count
        self.task_sustainable = task_sustainable

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_extra_info is not None:
            result['AppExtraInfo'] = self.app_extra_info
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.executor_count is not None:
            result['ExecutorCount'] = self.executor_count
        if self.job_description is not None:
            result['JobDescription'] = self.job_description
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.owner_uid is not None:
            result['OwnerUid'] = self.owner_uid
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.task_count is not None:
            result['TaskCount'] = self.task_count
        if self.task_sustainable is not None:
            result['TaskSustainable'] = self.task_sustainable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppExtraInfo') is not None:
            self.app_extra_info = m.get('AppExtraInfo')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExecutorCount') is not None:
            self.executor_count = m.get('ExecutorCount')
        if m.get('JobDescription') is not None:
            self.job_description = m.get('JobDescription')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('OwnerUid') is not None:
            self.owner_uid = m.get('OwnerUid')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListJobsResponseBodyJobListTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TaskCount') is not None:
            self.task_count = m.get('TaskCount')
        if m.get('TaskSustainable') is not None:
            self.task_sustainable = m.get('TaskSustainable')
        return self


class ListJobsResponseBody(TeaModel):
    def __init__(
        self,
        job_list: List[ListJobsResponseBodyJobList] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.job_list = job_list
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.job_list:
            for k in self.job_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['JobList'] = []
        if self.job_list is not None:
            for k in self.job_list:
                result['JobList'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.job_list = []
        if m.get('JobList') is not None:
            for k in m.get('JobList'):
                temp_model = ListJobsResponseBodyJobList()
                self.job_list.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListJobsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPoolsRequestFilter(TeaModel):
    def __init__(
        self,
        pool_name: List[str] = None,
        status: List[str] = None,
        time_created_after: int = None,
        time_created_before: int = None,
    ):
        self.pool_name = pool_name
        self.status = status
        self.time_created_after = time_created_after
        self.time_created_before = time_created_before

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pool_name is not None:
            result['PoolName'] = self.pool_name
        if self.status is not None:
            result['Status'] = self.status
        if self.time_created_after is not None:
            result['TimeCreatedAfter'] = self.time_created_after
        if self.time_created_before is not None:
            result['TimeCreatedBefore'] = self.time_created_before
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PoolName') is not None:
            self.pool_name = m.get('PoolName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TimeCreatedAfter') is not None:
            self.time_created_after = m.get('TimeCreatedAfter')
        if m.get('TimeCreatedBefore') is not None:
            self.time_created_before = m.get('TimeCreatedBefore')
        return self


class ListPoolsRequest(TeaModel):
    def __init__(
        self,
        filter: ListPoolsRequestFilter = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.filter = filter
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        if self.filter:
            self.filter.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter is not None:
            result['Filter'] = self.filter.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Filter') is not None:
            temp_model = ListPoolsRequestFilter()
            self.filter = temp_model.from_map(m['Filter'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListPoolsShrinkRequest(TeaModel):
    def __init__(
        self,
        filter_shrink: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.filter_shrink = filter_shrink
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter_shrink is not None:
            result['Filter'] = self.filter_shrink
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Filter') is not None:
            self.filter_shrink = m.get('Filter')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListPoolsResponseBodyPoolList(TeaModel):
    def __init__(
        self,
        is_default: bool = None,
        max_exector_num: int = None,
        pool_name: str = None,
        priority: int = None,
        status: str = None,
    ):
        self.is_default = is_default
        self.max_exector_num = max_exector_num
        self.pool_name = pool_name
        self.priority = priority
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.max_exector_num is not None:
            result['MaxExectorNum'] = self.max_exector_num
        if self.pool_name is not None:
            result['PoolName'] = self.pool_name
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('MaxExectorNum') is not None:
            self.max_exector_num = m.get('MaxExectorNum')
        if m.get('PoolName') is not None:
            self.pool_name = m.get('PoolName')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListPoolsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        pool_list: List[ListPoolsResponseBodyPoolList] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.pool_list = pool_list
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.pool_list:
            for k in self.pool_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['PoolList'] = []
        if self.pool_list is not None:
            for k in self.pool_list:
                result['PoolList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.pool_list = []
        if m.get('PoolList') is not None:
            for k in m.get('PoolList'):
                temp_model = ListPoolsResponseBodyPoolList()
                self.pool_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListPoolsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPoolsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListPoolsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListTagResourcesRequest(TeaModel):
    def __init__(
        self,
        max_result: int = None,
        next_token: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[ListTagResourcesRequestTag] = None,
    ):
        self.max_result = max_result
        self.next_token = next_token
        self.resource_id = resource_id
        # This parameter is required.
        self.resource_type = resource_type
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_result is not None:
            result['MaxResult'] = self.max_result
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResult') is not None:
            self.max_result = m.get('MaxResult')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResourcesTagResource(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        tag_resource: List[ListTagResourcesResponseBodyTagResourcesTagResource] = None,
    ):
        self.tag_resource = tag_resource

    def validate(self):
        if self.tag_resource:
            for k in self.tag_resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TagResource'] = []
        if self.tag_resource is not None:
            for k in self.tag_resource:
                result['TagResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_resource = []
        if m.get('TagResource') is not None:
            for k in m.get('TagResource'):
                temp_model = ListTagResourcesResponseBodyTagResourcesTagResource()
                self.tag_resource.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tag_resources: ListTagResourcesResponseBodyTagResources = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            self.tag_resources.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_resources is not None:
            result['TagResources'] = self.tag_resources.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagResources') is not None:
            temp_model = ListTagResourcesResponseBodyTagResources()
            self.tag_resources = temp_model.from_map(m['TagResources'])
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveImageRequest(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        image_type: str = None,
    ):
        # This parameter is required.
        self.image_id = image_id
        self.image_type = image_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        return self


class RemoveImageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RemoveImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveImageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RemoveImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # This parameter is required.
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class TagResourcesRequest(TeaModel):
    def __init__(
        self,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[TagResourcesRequestTag] = None,
    ):
        # This parameter is required.
        self.resource_id = resource_id
        # This parameter is required.
        self.resource_type = resource_type
        # This parameter is required.
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnTagResourcesRequest(TeaModel):
    def __init__(
        self,
        all: bool = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag_key: List[str] = None,
    ):
        self.all = all
        # This parameter is required.
        self.resource_id = resource_id
        # This parameter is required.
        self.resource_type = resource_type
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UnTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UnTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UnTagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UnTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePoolRequestResourceLimits(TeaModel):
    def __init__(
        self,
        max_exector_num: int = None,
    ):
        self.max_exector_num = max_exector_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_exector_num is not None:
            result['MaxExectorNum'] = self.max_exector_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxExectorNum') is not None:
            self.max_exector_num = m.get('MaxExectorNum')
        return self


class UpdatePoolRequest(TeaModel):
    def __init__(
        self,
        pool_name: str = None,
        priority: int = None,
        resource_limits: UpdatePoolRequestResourceLimits = None,
    ):
        # This parameter is required.
        self.pool_name = pool_name
        self.priority = priority
        self.resource_limits = resource_limits

    def validate(self):
        if self.resource_limits:
            self.resource_limits.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pool_name is not None:
            result['PoolName'] = self.pool_name
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.resource_limits is not None:
            result['ResourceLimits'] = self.resource_limits.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PoolName') is not None:
            self.pool_name = m.get('PoolName')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('ResourceLimits') is not None:
            temp_model = UpdatePoolRequestResourceLimits()
            self.resource_limits = temp_model.from_map(m['ResourceLimits'])
        return self


class UpdatePoolShrinkRequest(TeaModel):
    def __init__(
        self,
        pool_name: str = None,
        priority: int = None,
        resource_limits_shrink: str = None,
    ):
        # This parameter is required.
        self.pool_name = pool_name
        self.priority = priority
        self.resource_limits_shrink = resource_limits_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pool_name is not None:
            result['PoolName'] = self.pool_name
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.resource_limits_shrink is not None:
            result['ResourceLimits'] = self.resource_limits_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PoolName') is not None:
            self.pool_name = m.get('PoolName')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('ResourceLimits') is not None:
            self.resource_limits_shrink = m.get('ResourceLimits')
        return self


class UpdatePoolResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdatePoolResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdatePoolResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdatePoolResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


