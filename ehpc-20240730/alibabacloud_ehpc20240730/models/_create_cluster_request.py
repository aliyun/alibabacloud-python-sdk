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
        # The list of software that you want to install in the cluster. Valid values of N: 0 to 10.
        self.additional_packages = additional_packages
        # The configurations of the custom addons in the cluster. Only one addon is supported.
        self.addons = addons
        # The client version. By default, the latest version is used.
        self.client_version = client_version
        # The cluster type. Valid values:
        # 
        # *   Standard
        # *   Serverless
        self.cluster_category = cluster_category
        # The access credentials of the cluster.
        self.cluster_credentials = cluster_credentials
        # The post-processing script of the cluster.
        self.cluster_custom_configuration = cluster_custom_configuration
        # The cluster description. The description must be 1 to 128 characters in length and can contain letters, digits, hyphens (-), and underscores (_).
        self.cluster_description = cluster_description
        # The deployment mode of the cluster. Valid values:
        # 
        # *   Integrated
        # *   Hybrid
        # *   Custom
        self.cluster_mode = cluster_mode
        # The cluster name. The name must be 1 to 128 characters in length and can contain letters, digits, hyphens (-), and underscores (_).
        self.cluster_name = cluster_name
        # The ID of the vSwitch that you want the cluster to use. The vSwitch must reside in the VPC that is specified by the `ClusterVpcId` parameter.
        # 
        # You can call the [DescribeVpcs](https://help.aliyun.com/document_detail/448581.html) operation to query information about the created VPCs and vSwitches.
        self.cluster_vswitch_id = cluster_vswitch_id
        # The ID of the virtual private cloud (VPC) in which the cluster resides.
        self.cluster_vpc_id = cluster_vpc_id
        # Specifies whether to enable deletion protection for the cluster. Deletion protection decides whether the cluster can be deleted in the console or by calling the [DeleteCluster](https://help.aliyun.com/document_detail/424406.html) operation. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        self.deletion_protection = deletion_protection
        # Specifies whether to use an advanced security group. Valid values:
        # 
        # *   true: automatically creates and uses an advanced security group.
        # *   false: automatically creates and uses a basic security group.
        # 
        # For more information, see [Basic security groups and advanced security groups](https://help.aliyun.com/document_detail/605897.html).
        self.is_enterprise_security_group = is_enterprise_security_group
        # The configurations of the cluster management node.
        self.manager = manager
        # The maximum number of vCPUs that can be used by compute nodes in the cluster. Valid values: 0 to 100,000.
        self.max_core_count = max_core_count
        # The maximum number of compute nodes that the cluster can manage. Valid values: 0 to 5,000.
        self.max_count = max_count
        # The queues in the cluster. The number of queues can be 0 to 8.
        self.queues = queues
        # The ID of the resource group to which the cluster belongs.
        # 
        # You can call the [ListResourceGroups](https://help.aliyun.com/document_detail/158855.html) operation to obtain the IDs of the resource groups.
        self.resource_group_id = resource_group_id
        # The ID of the security group to which the cluster belongs.
        # 
        # You can call the [DescribeSecurityGroups](https://help.aliyun.com/document_detail/25556.html) operation to query available security groups in the current region.
        self.security_group_id = security_group_id
        # The shared storage resources of the cluster.
        self.shared_storages = shared_storages
        # The tags of the cluster.
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
        # The tag key. Valid values of N: 1 to 20. The tag key cannot be an empty string. The tag key can be up to 128 characters in length and cannot start with `acs:` or `aliyun`. The tag key cannot contain `http://` or `https://`.
        self.key = key
        # The tag value. Valid values of N: 1 to 20. The tag value can be an empty string. The tag value can be up to 128 characters in length and cannot contain `http://` or `https://`.
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
        # The configurations of the domain name resolution service.
        self.dns = dns
        # The configurations of the domain account service.
        self.directory_service = directory_service
        # The hardware configurations of the management node.
        self.manager_node = manager_node
        # The configurations of the scheduler service.
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
        # *   SLURM
        # *   PBS
        # *   OPENGRIDSCHEDULER
        # *   LSF_PLUGIN
        # *   PBS_PLUGIN
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
        # The type of the domain account.
        # 
        # Valid values:
        # 
        # *   NIS
        self.type = type
        # The version of the domain account service.
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
        # The domain name resolution type.
        # 
        # Valid values:
        # 
        # *   NIS
        self.type = type
        # The version of the domain name resolution service.
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
        # The runtime parameters of the script after the cluster is created.
        self.args = args
        # The URL that is used to download the post-processing script.
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
        # The name of the key pair. The name must be 2 to 128 characters in length. The name must start with a letter but cannot start with `http://` or `https://`. The name can contain digits, letters, colons (:), underscores (_), and hyphens (-).
        # 
        # >  For more information, see [Create a key pair](https://help.aliyun.com/document_detail/51793.html).
        self.key_pair_name = key_pair_name
        # The password for the root user to log on to the node. The password must be 8 to 20 characters in length, and must contain at least 3 of the following character types: uppercase letters, lowercase letters, digits, and special characters. The following special characters are supported: `() ~ ! @ # $ % ^ & * - = + { } [ ] : ; \\" < > , . ? /`
        # 
        # >  We recommend that you use HTTPS to call the API operation to prevent password leakage.
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
        # The addon name.
        # 
        # This parameter is required.
        self.name = name
        # The resource configurations of the addon.
        self.resources_spec = resources_spec
        # The service configurations of the addon.
        self.services_spec = services_spec
        # The addon version.
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
        # The name of the software that you want to install in the cluster.
        self.name = name
        # The version of the software that you want to install in the cluster.
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

