# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class GetServerIdeInstanceResponseBody(DaraModel):
    def __init__(
        self,
        instance: main_models.GetServerIdeInstanceResponseBodyInstance = None,
        request_id: str = None,
    ):
        # The details of the personal development environment instance.
        self.instance = instance
        # The request ID.
        self.request_id = request_id

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Instance') is not None:
            temp_model = main_models.GetServerIdeInstanceResponseBodyInstance()
            self.instance = temp_model.from_map(m.get('Instance'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetServerIdeInstanceResponseBodyInstance(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        credential_config: main_models.GetServerIdeInstanceResponseBodyInstanceCredentialConfig = None,
        cu: int = None,
        datasets: List[main_models.GetServerIdeInstanceResponseBodyInstanceDatasets] = None,
        fail_reason: str = None,
        image_id: str = None,
        image_name: str = None,
        image_url: str = None,
        instance_id: str = None,
        instance_name: str = None,
        owner_id: str = None,
        project_id: int = None,
        project_name: str = None,
        resource_group_id: int = None,
        resource_group_name: str = None,
        status: str = None,
        update_time: int = None,
        user_vpc: main_models.GetServerIdeInstanceResponseBodyInstanceUserVpc = None,
    ):
        # The time when the instance was created. This value is a UNIX timestamp in milliseconds.
        self.create_time = create_time
        # The credential injection configuration of the instance. After this feature is enabled, you can use the default RAM role chain or specify a custom RAM role.
        self.credential_config = credential_config
        # The number of CUs used by the instance.
        self.cu = cu
        # The list of datasets mounted to the instance.
        self.datasets = datasets
        # The reason why the instance entered the failed state.
        self.fail_reason = fail_reason
        # The ID of the image used by the instance.
        self.image_id = image_id
        # The image name.
        self.image_name = image_name
        # The image URL.
        self.image_url = image_url
        # The personal development environment instance ID.
        self.instance_id = instance_id
        # The name of the personal development environment instance.
        self.instance_name = instance_name
        # The account ID of the user who owns the instance.
        self.owner_id = owner_id
        # The DataWorks workspace ID.
        self.project_id = project_id
        # The DataWorks workspace name.
        self.project_name = project_name
        # The internal numeric ID of the resource group.
        self.resource_group_id = resource_group_id
        # The resource group name.
        self.resource_group_name = resource_group_name
        # The instance status. Valid values: Creating, Starting, Running, Stopping, Stopped, Updating, Deleting, DELETED, Failed, Arrearage, Saving, SaveFailed, and Saved.
        self.status = status
        # The time when the instance was last updated. This value is a UNIX timestamp in milliseconds.
        self.update_time = update_time
        # The VPC configuration used by the instance.
        self.user_vpc = user_vpc

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()
        if self.datasets:
            for v1 in self.datasets:
                 if v1:
                    v1.validate()
        if self.user_vpc:
            self.user_vpc.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()

        if self.cu is not None:
            result['Cu'] = self.cu

        result['Datasets'] = []
        if self.datasets is not None:
            for k1 in self.datasets:
                result['Datasets'].append(k1.to_map() if k1 else None)

        if self.fail_reason is not None:
            result['FailReason'] = self.fail_reason

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

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.user_vpc is not None:
            result['UserVpc'] = self.user_vpc.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CredentialConfig') is not None:
            temp_model = main_models.GetServerIdeInstanceResponseBodyInstanceCredentialConfig()
            self.credential_config = temp_model.from_map(m.get('CredentialConfig'))

        if m.get('Cu') is not None:
            self.cu = m.get('Cu')

        self.datasets = []
        if m.get('Datasets') is not None:
            for k1 in m.get('Datasets'):
                temp_model = main_models.GetServerIdeInstanceResponseBodyInstanceDatasets()
                self.datasets.append(temp_model.from_map(k1))

        if m.get('FailReason') is not None:
            self.fail_reason = m.get('FailReason')

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

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UserVpc') is not None:
            temp_model = main_models.GetServerIdeInstanceResponseBodyInstanceUserVpc()
            self.user_vpc = temp_model.from_map(m.get('UserVpc'))

        return self

class GetServerIdeInstanceResponseBodyInstanceUserVpc(DaraModel):
    def __init__(
        self,
        forward_infos: List[main_models.GetServerIdeInstanceResponseBodyInstanceUserVpcForwardInfos] = None,
        security_group_id: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The list of port forwarding configurations.
        self.forward_infos = forward_infos
        # The security group ID.
        self.security_group_id = security_group_id
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The VPC ID.
        self.vpc_id = vpc_id

    def validate(self):
        if self.forward_infos:
            for v1 in self.forward_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
        self.forward_infos = []
        if m.get('ForwardInfos') is not None:
            for k1 in m.get('ForwardInfos'):
                temp_model = main_models.GetServerIdeInstanceResponseBodyInstanceUserVpcForwardInfos()
                self.forward_infos.append(temp_model.from_map(k1))

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class GetServerIdeInstanceResponseBodyInstanceUserVpcForwardInfos(DaraModel):
    def __init__(
        self,
        access_type: List[str] = None,
        container_name: str = None,
        eip_allocation_id: str = None,
        enable: bool = None,
        external_port: str = None,
        forward_port: str = None,
        name: str = None,
        nat_gateway_id: str = None,
        sshpublic_key: str = None,
    ):
        # The list of access types.
        self.access_type = access_type
        # The name of the target container.
        self.container_name = container_name
        # The instance ID of the public Elastic IP Address (EIP).
        self.eip_allocation_id = eip_allocation_id
        # Indicates whether this port forwarding configuration is enabled.
        self.enable = enable
        # The mapped public port.
        self.external_port = external_port
        # The target port inside the instance container.
        self.forward_port = forward_port
        # The name of the port forwarding configuration.
        self.name = name
        # The NAT gateway ID.
        self.nat_gateway_id = nat_gateway_id
        # The public key used for SSH access.
        self.sshpublic_key = sshpublic_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_type is not None:
            result['AccessType'] = self.access_type

        if self.container_name is not None:
            result['ContainerName'] = self.container_name

        if self.eip_allocation_id is not None:
            result['EipAllocationId'] = self.eip_allocation_id

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.external_port is not None:
            result['ExternalPort'] = self.external_port

        if self.forward_port is not None:
            result['ForwardPort'] = self.forward_port

        if self.name is not None:
            result['Name'] = self.name

        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

        if self.sshpublic_key is not None:
            result['SSHPublicKey'] = self.sshpublic_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')

        if m.get('ContainerName') is not None:
            self.container_name = m.get('ContainerName')

        if m.get('EipAllocationId') is not None:
            self.eip_allocation_id = m.get('EipAllocationId')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('ExternalPort') is not None:
            self.external_port = m.get('ExternalPort')

        if m.get('ForwardPort') is not None:
            self.forward_port = m.get('ForwardPort')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

        if m.get('SSHPublicKey') is not None:
            self.sshpublic_key = m.get('SSHPublicKey')

        return self

class GetServerIdeInstanceResponseBodyInstanceDatasets(DaraModel):
    def __init__(
        self,
        ext_options: str = None,
        identifier: str = None,
        mount_path: str = None,
        read_only: bool = None,
        uri: str = None,
        version: int = None,
    ):
        # The custom mount properties of the dataset. The content is passed as mount options.
        self.ext_options = ext_options
        # The dataset identifier.
        self.identifier = identifier
        # The mount path of the dataset in the instance.
        self.mount_path = mount_path
        # Indicates whether the dataset is mounted in read-only mode.
        self.read_only = read_only
        # The URI of the storage service directory used for direct mounting.
        self.uri = uri
        # The dataset version number.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ext_options is not None:
            result['ExtOptions'] = self.ext_options

        if self.identifier is not None:
            result['Identifier'] = self.identifier

        if self.mount_path is not None:
            result['MountPath'] = self.mount_path

        if self.read_only is not None:
            result['ReadOnly'] = self.read_only

        if self.uri is not None:
            result['Uri'] = self.uri

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtOptions') is not None:
            self.ext_options = m.get('ExtOptions')

        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')

        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')

        if m.get('ReadOnly') is not None:
            self.read_only = m.get('ReadOnly')

        if m.get('Uri') is not None:
            self.uri = m.get('Uri')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class GetServerIdeInstanceResponseBodyInstanceCredentialConfig(DaraModel):
    def __init__(
        self,
        aliyun_env_role_key: str = None,
        configs: List[main_models.GetServerIdeInstanceResponseBodyInstanceCredentialConfigConfigs] = None,
        enable: bool = None,
    ):
        # The environment variable role key.
        self.aliyun_env_role_key = aliyun_env_role_key
        # The list of credential configurations.
        self.configs = configs
        # Indicates whether credential injection is enabled.
        self.enable = enable

    def validate(self):
        if self.configs:
            for v1 in self.configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_env_role_key is not None:
            result['AliyunEnvRoleKey'] = self.aliyun_env_role_key

        result['Configs'] = []
        if self.configs is not None:
            for k1 in self.configs:
                result['Configs'].append(k1.to_map() if k1 else None)

        if self.enable is not None:
            result['Enable'] = self.enable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunEnvRoleKey') is not None:
            self.aliyun_env_role_key = m.get('AliyunEnvRoleKey')

        self.configs = []
        if m.get('Configs') is not None:
            for k1 in m.get('Configs'):
                temp_model = main_models.GetServerIdeInstanceResponseBodyInstanceCredentialConfigConfigs()
                self.configs.append(temp_model.from_map(k1))

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        return self

class GetServerIdeInstanceResponseBodyInstanceCredentialConfigConfigs(DaraModel):
    def __init__(
        self,
        key: str = None,
        roles: List[main_models.GetServerIdeInstanceResponseBodyInstanceCredentialConfigConfigsRoles] = None,
        type: str = None,
    ):
        # The identifier key of the credential configuration.
        self.key = key
        # The list of roles in the credential configuration.
        self.roles = roles
        # The credential configuration type. Valid values: Role (single role assumption) and RoleChain (role chain assumption).
        self.type = type

    def validate(self):
        if self.roles:
            for v1 in self.roles:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        result['Roles'] = []
        if self.roles is not None:
            for k1 in self.roles:
                result['Roles'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        self.roles = []
        if m.get('Roles') is not None:
            for k1 in m.get('Roles'):
                temp_model = main_models.GetServerIdeInstanceResponseBodyInstanceCredentialConfigConfigsRoles()
                self.roles.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetServerIdeInstanceResponseBodyInstanceCredentialConfigConfigsRoles(DaraModel):
    def __init__(
        self,
        assume_role_for: str = None,
        policy: str = None,
        role_arn: str = None,
        role_type: str = None,
        user_info: main_models.GetServerIdeInstanceResponseBodyInstanceCredentialConfigConfigsRolesUserInfo = None,
    ):
        # The Alibaba Cloud account ID of the principal that owns the assumed role.
        self.assume_role_for = assume_role_for
        # The policy used to further restrict the permissions of the role.
        self.policy = policy
        # The ARN of the RAM role.
        self.role_arn = role_arn
        # The role assumption type. Valid values: service (assumed by a service) and user (assumed by a user).
        self.role_type = role_type
        # The information of the proxied user.
        self.user_info = user_info

    def validate(self):
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assume_role_for is not None:
            result['AssumeRoleFor'] = self.assume_role_for

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn

        if self.role_type is not None:
            result['RoleType'] = self.role_type

        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssumeRoleFor') is not None:
            self.assume_role_for = m.get('AssumeRoleFor')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')

        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')

        if m.get('UserInfo') is not None:
            temp_model = main_models.GetServerIdeInstanceResponseBodyInstanceCredentialConfigConfigsRolesUserInfo()
            self.user_info = temp_model.from_map(m.get('UserInfo'))

        return self

class GetServerIdeInstanceResponseBodyInstanceCredentialConfigConfigsRolesUserInfo(DaraModel):
    def __init__(
        self,
        access_key_id: str = None,
        id: str = None,
        security_token: str = None,
        type: str = None,
    ):
        # The temporary AccessKey ID used for credential injection.
        self.access_key_id = access_key_id
        # The account ID of the proxied user.
        self.id = id
        # The temporary security token used for credential injection.
        self.security_token = security_token
        # The user type. Valid values: customer (Alibaba Cloud account), sub (RAM user), and AssumedRoleUser (RAM role).
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id

        if self.id is not None:
            result['Id'] = self.id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

