# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ehpc20240730 import models as main_models
from darabonba.model import DaraModel

class CreateClusterRequest(DaraModel):
    def __init__(
        self,
        additional_packages: List[main_models.CreateClusterRequestAdditionalPackages] = None,
        addons: List[main_models.CreateClusterRequestAddons] = None,
        client_version: str = None,
        cluster_category: str = None,
        cluster_credentials: main_models.CreateClusterRequestClusterCredentials = None,
        cluster_custom_configuration: main_models.CreateClusterRequestClusterCustomConfiguration = None,
        cluster_description: str = None,
        cluster_mode: str = None,
        cluster_name: str = None,
        cluster_vswitch_id: str = None,
        cluster_vpc_id: str = None,
        deletion_protection: bool = None,
        grow_interval: int = None,
        idle_interval: int = None,
        is_enterprise_security_group: bool = None,
        manager: main_models.CreateClusterRequestManager = None,
        max_core_count: int = None,
        max_count: int = None,
        queues: List[main_models.QueueTemplate] = None,
        resource_group_id: str = None,
        security_group_id: str = None,
        shared_storages: List[main_models.SharedStorageTemplate] = None,
        tags: List[main_models.CreateClusterRequestTags] = None,
    ):
        # A list of software to install in the cluster. You can specify up to 10 packages.
        self.additional_packages = additional_packages
        # The configuration of the custom service component for the cluster. Only one component is supported.
        self.addons = addons
        # The version of the E-HPC client. By default, the latest version is used.
        self.client_version = client_version
        # The edition of the cluster. Valid values:
        # 
        # - Standard
        # 
        # - Serverless
        self.cluster_category = cluster_category
        # The security credentials for the cluster.
        self.cluster_credentials = cluster_credentials
        # The post-processing script for the cluster.
        self.cluster_custom_configuration = cluster_custom_configuration
        # The description of the cluster. The description must be 2 to 128 characters long and can contain letters, Chinese characters, digits, hyphens (-), and underscores (_).
        self.cluster_description = cluster_description
        # The cluster\\"s deployment type. Valid values:
        # 
        # - Integrated: An integrated cluster.
        # 
        # - Hybrid: A hybrid cloud cluster.
        # 
        # - Custom: A custom cluster.
        self.cluster_mode = cluster_mode
        # The name of the cluster. The name must be 2 to 128 characters long and can contain letters, Chinese characters, digits, hyphens (-), and underscores (_).
        self.cluster_name = cluster_name
        # The ID of the VSwitch for the cluster. The VSwitch must be in the VPC specified by `ClusterVpcId`.
        # 
        # Call the [DescribeVpcs](https://help.aliyun.com/document_detail/448581.html) operation to find available VPCs and VSwitches.
        self.cluster_vswitch_id = cluster_vswitch_id
        # The ID of the VPC for the cluster.
        self.cluster_vpc_id = cluster_vpc_id
        # Specifies whether to enable deletion protection for the cluster. This feature prevents the cluster from being deleted via the console or the [DeleteCluster](https://help.aliyun.com/document_detail/424406.html) operation.
        # 
        # - true: Enables deletion protection.
        # 
        # - false: Disables deletion protection.
        # 
        # Default value: false.
        self.deletion_protection = deletion_protection
        self.grow_interval = grow_interval
        self.idle_interval = idle_interval
        # Specifies whether to use an enterprise security group. Valid values:
        # 
        # - true: The system automatically creates and uses an enterprise security group.
        # 
        # - false: The system automatically creates and uses a security group.
        # 
        # For more information about how to select a security group type, see [Security groups and enterprise security groups](https://help.aliyun.com/document_detail/605897.html).
        self.is_enterprise_security_group = is_enterprise_security_group
        # Configuration for the cluster manager node.
        self.manager = manager
        # The maximum number of CPU cores that the cluster can manage across all compute nodes. Valid values: 0 to 100,000.
        self.max_core_count = max_core_count
        # The maximum number of compute nodes that the cluster can manage. Valid values: 0 to 5,000.
        self.max_count = max_count
        # Configuration for the cluster queues. You can specify up to 8 queues.
        self.queues = queues
        # The ID of the resource group.
        # 
        # Call the [ListResourceGroups](https://help.aliyun.com/document_detail/158855.html) operation to find resource group IDs.
        self.resource_group_id = resource_group_id
        # The ID of the security group for the cluster.
        # 
        # Call the [DescribeSecurityGroups](https://help.aliyun.com/document_detail/25556.html) operation to find available security groups in the current region.
        self.security_group_id = security_group_id
        # Configuration for the cluster\\"s shared storage.
        self.shared_storages = shared_storages
        # The list of tags to add to the cluster. You can add up to 20 tags.
        self.tags = tags

    def validate(self):
        if self.additional_packages:
            for v1 in self.additional_packages:
                 if v1:
                    v1.validate()
        if self.addons:
            for v1 in self.addons:
                 if v1:
                    v1.validate()
        if self.cluster_credentials:
            self.cluster_credentials.validate()
        if self.cluster_custom_configuration:
            self.cluster_custom_configuration.validate()
        if self.manager:
            self.manager.validate()
        if self.queues:
            for v1 in self.queues:
                 if v1:
                    v1.validate()
        if self.shared_storages:
            for v1 in self.shared_storages:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AdditionalPackages'] = []
        if self.additional_packages is not None:
            for k1 in self.additional_packages:
                result['AdditionalPackages'].append(k1.to_map() if k1 else None)

        result['Addons'] = []
        if self.addons is not None:
            for k1 in self.addons:
                result['Addons'].append(k1.to_map() if k1 else None)

        if self.client_version is not None:
            result['ClientVersion'] = self.client_version

        if self.cluster_category is not None:
            result['ClusterCategory'] = self.cluster_category

        if self.cluster_credentials is not None:
            result['ClusterCredentials'] = self.cluster_credentials.to_map()

        if self.cluster_custom_configuration is not None:
            result['ClusterCustomConfiguration'] = self.cluster_custom_configuration.to_map()

        if self.cluster_description is not None:
            result['ClusterDescription'] = self.cluster_description

        if self.cluster_mode is not None:
            result['ClusterMode'] = self.cluster_mode

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.cluster_vswitch_id is not None:
            result['ClusterVSwitchId'] = self.cluster_vswitch_id

        if self.cluster_vpc_id is not None:
            result['ClusterVpcId'] = self.cluster_vpc_id

        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection

        if self.grow_interval is not None:
            result['GrowInterval'] = self.grow_interval

        if self.idle_interval is not None:
            result['IdleInterval'] = self.idle_interval

        if self.is_enterprise_security_group is not None:
            result['IsEnterpriseSecurityGroup'] = self.is_enterprise_security_group

        if self.manager is not None:
            result['Manager'] = self.manager.to_map()

        if self.max_core_count is not None:
            result['MaxCoreCount'] = self.max_core_count

        if self.max_count is not None:
            result['MaxCount'] = self.max_count

        result['Queues'] = []
        if self.queues is not None:
            for k1 in self.queues:
                result['Queues'].append(k1.to_map() if k1 else None)

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        result['SharedStorages'] = []
        if self.shared_storages is not None:
            for k1 in self.shared_storages:
                result['SharedStorages'].append(k1.to_map() if k1 else None)

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.additional_packages = []
        if m.get('AdditionalPackages') is not None:
            for k1 in m.get('AdditionalPackages'):
                temp_model = main_models.CreateClusterRequestAdditionalPackages()
                self.additional_packages.append(temp_model.from_map(k1))

        self.addons = []
        if m.get('Addons') is not None:
            for k1 in m.get('Addons'):
                temp_model = main_models.CreateClusterRequestAddons()
                self.addons.append(temp_model.from_map(k1))

        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')

        if m.get('ClusterCategory') is not None:
            self.cluster_category = m.get('ClusterCategory')

        if m.get('ClusterCredentials') is not None:
            temp_model = main_models.CreateClusterRequestClusterCredentials()
            self.cluster_credentials = temp_model.from_map(m.get('ClusterCredentials'))

        if m.get('ClusterCustomConfiguration') is not None:
            temp_model = main_models.CreateClusterRequestClusterCustomConfiguration()
            self.cluster_custom_configuration = temp_model.from_map(m.get('ClusterCustomConfiguration'))

        if m.get('ClusterDescription') is not None:
            self.cluster_description = m.get('ClusterDescription')

        if m.get('ClusterMode') is not None:
            self.cluster_mode = m.get('ClusterMode')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('ClusterVSwitchId') is not None:
            self.cluster_vswitch_id = m.get('ClusterVSwitchId')

        if m.get('ClusterVpcId') is not None:
            self.cluster_vpc_id = m.get('ClusterVpcId')

        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')

        if m.get('GrowInterval') is not None:
            self.grow_interval = m.get('GrowInterval')

        if m.get('IdleInterval') is not None:
            self.idle_interval = m.get('IdleInterval')

        if m.get('IsEnterpriseSecurityGroup') is not None:
            self.is_enterprise_security_group = m.get('IsEnterpriseSecurityGroup')

        if m.get('Manager') is not None:
            temp_model = main_models.CreateClusterRequestManager()
            self.manager = temp_model.from_map(m.get('Manager'))

        if m.get('MaxCoreCount') is not None:
            self.max_core_count = m.get('MaxCoreCount')

        if m.get('MaxCount') is not None:
            self.max_count = m.get('MaxCount')

        self.queues = []
        if m.get('Queues') is not None:
            for k1 in m.get('Queues'):
                temp_model = main_models.QueueTemplate()
                self.queues.append(temp_model.from_map(k1))

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        self.shared_storages = []
        if m.get('SharedStorages') is not None:
            for k1 in m.get('SharedStorages'):
                temp_model = main_models.SharedStorageTemplate()
                self.shared_storages.append(temp_model.from_map(k1))

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.CreateClusterRequestTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class CreateClusterRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. The key cannot be an empty string. The key can be up to 128 characters in length. It cannot start with `aliyun` or `acs:` and cannot contain `http://` or `https://`.
        self.key = key
        # The tag value. The value can be an empty string. The value can be up to 128 characters in length and cannot contain `http://` or `https://`.
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

class CreateClusterRequestManager(DaraModel):
    def __init__(
        self,
        dns: main_models.CreateClusterRequestManagerDNS = None,
        directory_service: main_models.CreateClusterRequestManagerDirectoryService = None,
        manager_node: main_models.NodeTemplate = None,
        scheduler: main_models.CreateClusterRequestManagerScheduler = None,
    ):
        # Configuration for the DNS service.
        self.dns = dns
        # Configuration for the directory service.
        self.directory_service = directory_service
        # Hardware configuration for the manager node.
        self.manager_node = manager_node
        # Configuration for the scheduler.
        self.scheduler = scheduler

    def validate(self):
        if self.dns:
            self.dns.validate()
        if self.directory_service:
            self.directory_service.validate()
        if self.manager_node:
            self.manager_node.validate()
        if self.scheduler:
            self.scheduler.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dns is not None:
            result['DNS'] = self.dns.to_map()

        if self.directory_service is not None:
            result['DirectoryService'] = self.directory_service.to_map()

        if self.manager_node is not None:
            result['ManagerNode'] = self.manager_node.to_map()

        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DNS') is not None:
            temp_model = main_models.CreateClusterRequestManagerDNS()
            self.dns = temp_model.from_map(m.get('DNS'))

        if m.get('DirectoryService') is not None:
            temp_model = main_models.CreateClusterRequestManagerDirectoryService()
            self.directory_service = temp_model.from_map(m.get('DirectoryService'))

        if m.get('ManagerNode') is not None:
            temp_model = main_models.NodeTemplate()
            self.manager_node = temp_model.from_map(m.get('ManagerNode'))

        if m.get('Scheduler') is not None:
            temp_model = main_models.CreateClusterRequestManagerScheduler()
            self.scheduler = temp_model.from_map(m.get('Scheduler'))

        return self

class CreateClusterRequestManagerScheduler(DaraModel):
    def __init__(
        self,
        type: str = None,
        version: str = None,
    ):
        # The scheduler type. Valid values:
        # 
        # - SLURM
        # 
        # - PBS
        # 
        # - OPENGRIDSCHEDULER
        # 
        # - LSF_PLUGIN
        # 
        # - PBS_PLUGIN
        self.type = type
        # The scheduler version.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['Type'] = self.type

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class CreateClusterRequestManagerDirectoryService(DaraModel):
    def __init__(
        self,
        type: str = None,
        version: str = None,
    ):
        # The directory service type.
        self.type = type
        # The directory service version.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['Type'] = self.type

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class CreateClusterRequestManagerDNS(DaraModel):
    def __init__(
        self,
        type: str = None,
        version: str = None,
    ):
        # The DNS service type.
        self.type = type
        # The DNS service version.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['Type'] = self.type

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class CreateClusterRequestClusterCustomConfiguration(DaraModel):
    def __init__(
        self,
        args: str = None,
        script: str = None,
    ):
        # The execution parameters for the post-processing script.
        self.args = args
        # The download URL for the post-processing script.
        self.script = script

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.args is not None:
            result['Args'] = self.args

        if self.script is not None:
            result['Script'] = self.script

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Args') is not None:
            self.args = m.get('Args')

        if m.get('Script') is not None:
            self.script = m.get('Script')

        return self

class CreateClusterRequestClusterCredentials(DaraModel):
    def __init__(
        self,
        key_pair_name: str = None,
        password: str = None,
    ):
        # The key pair name. The name must be 2 to 128 characters long, start with a letter or a Chinese character, and not start with `http://` or `https://`. It can contain digits, colons (:), underscores (_), and hyphens (-).
        # 
        # > To use an ECS key pair, see [Create a key pair](https://help.aliyun.com/document_detail/51793.html).
        self.key_pair_name = key_pair_name
        # The root password of the login node. The password must be 8 to 20 characters long and include characters from at least three of the following categories: uppercase letters, lowercase letters, digits, and special characters. The supported special characters are: `() ~ ! @ # $ % ^ & * - = + { } [ ] : ; ‘ < > , . ? /`
        # 
        # > Use HTTPS when calling the API to prevent password exposure.
        self.password = password

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name

        if self.password is not None:
            result['Password'] = self.password

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        return self

class CreateClusterRequestAddons(DaraModel):
    def __init__(
        self,
        name: str = None,
        resources_spec: str = None,
        services_spec: str = None,
        version: str = None,
    ):
        # The name of the custom service component.
        # 
        # This parameter is required.
        self.name = name
        # The resource configuration of the custom service component.
        self.resources_spec = resources_spec
        # The service configuration of the custom service component.
        self.services_spec = services_spec
        # The version of the custom service component.
        # 
        # This parameter is required.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.resources_spec is not None:
            result['ResourcesSpec'] = self.resources_spec

        if self.services_spec is not None:
            result['ServicesSpec'] = self.services_spec

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ResourcesSpec') is not None:
            self.resources_spec = m.get('ResourcesSpec')

        if m.get('ServicesSpec') is not None:
            self.services_spec = m.get('ServicesSpec')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class CreateClusterRequestAdditionalPackages(DaraModel):
    def __init__(
        self,
        name: str = None,
        version: str = None,
    ):
        # The name of the software.
        self.name = name
        # The version of the software.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

