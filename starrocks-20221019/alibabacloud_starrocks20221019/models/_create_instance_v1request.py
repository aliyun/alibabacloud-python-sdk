# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_starrocks20221019 import models as main_models
from darabonba.model import DaraModel

class CreateInstanceV1Request(DaraModel):
    def __init__(
        self,
        admin_password: str = None,
        agent_node_group: main_models.CreateInstanceV1RequestAgentNodeGroup = None,
        auto_pay: bool = None,
        auto_renew: bool = None,
        backend_node_groups: List[main_models.CreateInstanceV1RequestBackendNodeGroups] = None,
        client_token: str = None,
        dlf_catalog_name: str = None,
        dlf_catalog_type: str = None,
        duration: int = None,
        enable_ai_function: bool = None,
        enable_multi_az: bool = None,
        encrypted: bool = None,
        frontend_node_groups: List[main_models.CreateInstanceV1RequestFrontendNodeGroups] = None,
        gateway_type: str = None,
        instance_name: str = None,
        kms_key_id: str = None,
        linked_ram_user_name: str = None,
        observer_node_groups: List[main_models.CreateInstanceV1RequestObserverNodeGroups] = None,
        oss_accessing_role_name: str = None,
        package_type: str = None,
        pay_type: str = None,
        pricing_cycle: str = None,
        principal_type: str = None,
        promotion_option_no: str = None,
        ram_user_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        run_mode: str = None,
        tags: List[main_models.CreateInstanceV1RequestTags] = None,
        v_switches: List[main_models.CreateInstanceV1RequestVSwitches] = None,
        version: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # The administrator password of the instance.
        # 
        # This parameter is required.
        self.admin_password = admin_password
        self.agent_node_group = agent_node_group
        self.auto_pay = auto_pay
        # Specifies whether to enable auto-renewal. This parameter takes effect only when payType is set to PrePaid. Auto-renewal is disabled by default.
        self.auto_renew = auto_renew
        # The BE or CN node group information.
        self.backend_node_groups = backend_node_groups
        # Ensures the idempotence of the request. Generate a unique parameter value from your client. The ClientToken value supports only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The name of the DLF Catalog.
        self.dlf_catalog_name = dlf_catalog_name
        # The type of the DLF Catalog. Valid values: paimon and iceberg.
        self.dlf_catalog_type = dlf_catalog_type
        # The subscription duration. This parameter takes effect only when payType is set to PrePaid.
        self.duration = duration
        self.enable_ai_function = enable_ai_function
        # Specifies whether to enable disaster recovery.
        self.enable_multi_az = enable_multi_az
        # Specifies whether to enable encryption.
        self.encrypted = encrypted
        # The FE node group information.
        self.frontend_node_groups = frontend_node_groups
        self.gateway_type = gateway_type
        # The instance name.
        # 
        # This parameter is required.
        self.instance_name = instance_name
        # The KMS key ID.
        self.kms_key_id = kms_key_id
        # The username of the associated Resource Access Management (RAM) user or the name of the associated RAM role.
        self.linked_ram_user_name = linked_ram_user_name
        # The Observer node group information. Specify this parameter only when you need to enable cross-zone disaster recovery. The Observer node group specifications must be the same as those of the FE node group.
        self.observer_node_groups = observer_node_groups
        # The name of the role used for password-free access to Object Storage Service (OSS).
        self.oss_accessing_role_name = oss_accessing_role_name
        # The instance edition. Valid values:
        # <ul>
        # <li>trial: Trial Edition.</li>
        # <li>official: Standard Edition.</li>
        # </ul>
        # 
        # This parameter is required.
        self.package_type = package_type
        # The billing method. Valid values:
        # <ol>
        # <li>prePaid: subscription.</li>
        # <li>postPaid: pay-as-you-go.</li>
        # </ol>
        # 
        # This parameter is required.
        self.pay_type = pay_type
        # The unit of the subscription duration. Valid values:
        # <ul>
        # <li>Month</li>
        # <li>Year</li>
        # </ul>
        # This parameter takes effect only when payType is set to PrePaid.
        self.pricing_cycle = pricing_cycle
        # The RAM authentication type. Valid values:
        # - RS: Resource Access Management (RAM) user.
        # - RR: RAM role.
        self.principal_type = principal_type
        # The coupon ID.
        self.promotion_option_no = promotion_option_no
        # The ID of the Resource Access Management (RAM) user or RAM role.
        self.ram_user_id = ram_user_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The running mode of the cluster. Valid values:
        # 
        # - shared_nothing: compute-storage coupled.
        # - shared_data: storage-compute disaggregation.
        # 
        # This parameter is required.
        self.run_mode = run_mode
        # The instance tags.
        self.tags = tags
        # The vSwitch and zone information.
        self.v_switches = v_switches
        # The major version of the instance.
        # 
        # This parameter is required.
        self.version = version
        # VPC ID。
        # 
        # This parameter is required.
        self.vpc_id = vpc_id
        # The primary zone ID.
        # 
        # This parameter is required.
        self.zone_id = zone_id

    def validate(self):
        if self.agent_node_group:
            self.agent_node_group.validate()
        if self.backend_node_groups:
            for v1 in self.backend_node_groups:
                 if v1:
                    v1.validate()
        if self.frontend_node_groups:
            for v1 in self.frontend_node_groups:
                 if v1:
                    v1.validate()
        if self.observer_node_groups:
            for v1 in self.observer_node_groups:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()
        if self.v_switches:
            for v1 in self.v_switches:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.admin_password is not None:
            result['AdminPassword'] = self.admin_password

        if self.agent_node_group is not None:
            result['AgentNodeGroup'] = self.agent_node_group.to_map()

        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        result['BackendNodeGroups'] = []
        if self.backend_node_groups is not None:
            for k1 in self.backend_node_groups:
                result['BackendNodeGroups'].append(k1.to_map() if k1 else None)

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dlf_catalog_name is not None:
            result['DlfCatalogName'] = self.dlf_catalog_name

        if self.dlf_catalog_type is not None:
            result['DlfCatalogType'] = self.dlf_catalog_type

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.enable_ai_function is not None:
            result['EnableAiFunction'] = self.enable_ai_function

        if self.enable_multi_az is not None:
            result['EnableMultiAz'] = self.enable_multi_az

        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted

        result['FrontendNodeGroups'] = []
        if self.frontend_node_groups is not None:
            for k1 in self.frontend_node_groups:
                result['FrontendNodeGroups'].append(k1.to_map() if k1 else None)

        if self.gateway_type is not None:
            result['GatewayType'] = self.gateway_type

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.kms_key_id is not None:
            result['KmsKeyId'] = self.kms_key_id

        if self.linked_ram_user_name is not None:
            result['LinkedRamUserName'] = self.linked_ram_user_name

        result['ObserverNodeGroups'] = []
        if self.observer_node_groups is not None:
            for k1 in self.observer_node_groups:
                result['ObserverNodeGroups'].append(k1.to_map() if k1 else None)

        if self.oss_accessing_role_name is not None:
            result['OssAccessingRoleName'] = self.oss_accessing_role_name

        if self.package_type is not None:
            result['PackageType'] = self.package_type

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle

        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type

        if self.promotion_option_no is not None:
            result['PromotionOptionNo'] = self.promotion_option_no

        if self.ram_user_id is not None:
            result['RamUserId'] = self.ram_user_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.run_mode is not None:
            result['RunMode'] = self.run_mode

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        result['VSwitches'] = []
        if self.v_switches is not None:
            for k1 in self.v_switches:
                result['VSwitches'].append(k1.to_map() if k1 else None)

        if self.version is not None:
            result['Version'] = self.version

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdminPassword') is not None:
            self.admin_password = m.get('AdminPassword')

        if m.get('AgentNodeGroup') is not None:
            temp_model = main_models.CreateInstanceV1RequestAgentNodeGroup()
            self.agent_node_group = temp_model.from_map(m.get('AgentNodeGroup'))

        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        self.backend_node_groups = []
        if m.get('BackendNodeGroups') is not None:
            for k1 in m.get('BackendNodeGroups'):
                temp_model = main_models.CreateInstanceV1RequestBackendNodeGroups()
                self.backend_node_groups.append(temp_model.from_map(k1))

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DlfCatalogName') is not None:
            self.dlf_catalog_name = m.get('DlfCatalogName')

        if m.get('DlfCatalogType') is not None:
            self.dlf_catalog_type = m.get('DlfCatalogType')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('EnableAiFunction') is not None:
            self.enable_ai_function = m.get('EnableAiFunction')

        if m.get('EnableMultiAz') is not None:
            self.enable_multi_az = m.get('EnableMultiAz')

        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')

        self.frontend_node_groups = []
        if m.get('FrontendNodeGroups') is not None:
            for k1 in m.get('FrontendNodeGroups'):
                temp_model = main_models.CreateInstanceV1RequestFrontendNodeGroups()
                self.frontend_node_groups.append(temp_model.from_map(k1))

        if m.get('GatewayType') is not None:
            self.gateway_type = m.get('GatewayType')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('KmsKeyId') is not None:
            self.kms_key_id = m.get('KmsKeyId')

        if m.get('LinkedRamUserName') is not None:
            self.linked_ram_user_name = m.get('LinkedRamUserName')

        self.observer_node_groups = []
        if m.get('ObserverNodeGroups') is not None:
            for k1 in m.get('ObserverNodeGroups'):
                temp_model = main_models.CreateInstanceV1RequestObserverNodeGroups()
                self.observer_node_groups.append(temp_model.from_map(k1))

        if m.get('OssAccessingRoleName') is not None:
            self.oss_accessing_role_name = m.get('OssAccessingRoleName')

        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')

        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')

        if m.get('PromotionOptionNo') is not None:
            self.promotion_option_no = m.get('PromotionOptionNo')

        if m.get('RamUserId') is not None:
            self.ram_user_id = m.get('RamUserId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('RunMode') is not None:
            self.run_mode = m.get('RunMode')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.CreateInstanceV1RequestTags()
                self.tags.append(temp_model.from_map(k1))

        self.v_switches = []
        if m.get('VSwitches') is not None:
            for k1 in m.get('VSwitches'):
                temp_model = main_models.CreateInstanceV1RequestVSwitches()
                self.v_switches.append(temp_model.from_map(k1))

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class CreateInstanceV1RequestVSwitches(DaraModel):
    def __init__(
        self,
        vsw_id: str = None,
        zone_id: str = None,
    ):
        # The vSwitch ID.
        # 
        # This parameter is required.
        self.vsw_id = vsw_id
        # The zone ID of the vSwitch.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.vsw_id is not None:
            result['VswId'] = self.vsw_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VswId') is not None:
            self.vsw_id = m.get('VswId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class CreateInstanceV1RequestTags(DaraModel):
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

class CreateInstanceV1RequestObserverNodeGroups(DaraModel):
    def __init__(
        self,
        cu: int = None,
        disk_number: int = None,
        local_storage_instance_type: str = None,
        resident_node_number: int = None,
        spec_type: str = None,
        storage_performance_level: str = None,
        storage_size: int = None,
        zone_id: str = None,
    ):
        # The number of CUs. A CU (Compute Unit) is the basic metering unit of the service. 1 CU = 1 CPU core + 4 GiB memory.
        self.cu = cu
        # The number of disks.
        self.disk_number = disk_number
        # The local SSD instance type. This parameter does not need to be set for the Observer node group.
        self.local_storage_instance_type = local_storage_instance_type
        # The number of nodes.
        self.resident_node_number = resident_node_number
        # The specification type of the node group. Only standard is supported.
        self.spec_type = spec_type
        # The performance level (PL) of the cloud disk. Only pl1 is supported, which provides up to 50,000 random read/write IOPS per disk.
        self.storage_performance_level = storage_performance_level
        # The storage size. Unit: GiB.
        self.storage_size = storage_size
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cu is not None:
            result['cu'] = self.cu

        if self.disk_number is not None:
            result['diskNumber'] = self.disk_number

        if self.local_storage_instance_type is not None:
            result['localStorageInstanceType'] = self.local_storage_instance_type

        if self.resident_node_number is not None:
            result['residentNodeNumber'] = self.resident_node_number

        if self.spec_type is not None:
            result['specType'] = self.spec_type

        if self.storage_performance_level is not None:
            result['storagePerformanceLevel'] = self.storage_performance_level

        if self.storage_size is not None:
            result['storageSize'] = self.storage_size

        if self.zone_id is not None:
            result['zoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cu') is not None:
            self.cu = m.get('cu')

        if m.get('diskNumber') is not None:
            self.disk_number = m.get('diskNumber')

        if m.get('localStorageInstanceType') is not None:
            self.local_storage_instance_type = m.get('localStorageInstanceType')

        if m.get('residentNodeNumber') is not None:
            self.resident_node_number = m.get('residentNodeNumber')

        if m.get('specType') is not None:
            self.spec_type = m.get('specType')

        if m.get('storagePerformanceLevel') is not None:
            self.storage_performance_level = m.get('storagePerformanceLevel')

        if m.get('storageSize') is not None:
            self.storage_size = m.get('storageSize')

        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')

        return self

class CreateInstanceV1RequestFrontendNodeGroups(DaraModel):
    def __init__(
        self,
        cu: int = None,
        disk_number: int = None,
        local_storage_instance_type: str = None,
        resident_node_number: int = None,
        spec_type: str = None,
        storage_performance_level: str = None,
        storage_size: int = None,
        zone_id: str = None,
    ):
        # The number of CUs. A CU (Compute Unit) is the basic metering unit of the service. 1 CU = 1 CPU core + 4 GiB memory.
        self.cu = cu
        # The number of disks.
        self.disk_number = disk_number
        # The local SSD instance type. This parameter does not need to be set for the FE node group.
        self.local_storage_instance_type = local_storage_instance_type
        # The number of nodes.
        self.resident_node_number = resident_node_number
        # The specification type of the node group. Only standard is supported.
        self.spec_type = spec_type
        # The performance level (PL) of the cloud disk. Only pl1 is supported, which provides up to 50,000 random read/write IOPS per disk.
        self.storage_performance_level = storage_performance_level
        # The storage size. Unit: GiB.
        self.storage_size = storage_size
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cu is not None:
            result['cu'] = self.cu

        if self.disk_number is not None:
            result['diskNumber'] = self.disk_number

        if self.local_storage_instance_type is not None:
            result['localStorageInstanceType'] = self.local_storage_instance_type

        if self.resident_node_number is not None:
            result['residentNodeNumber'] = self.resident_node_number

        if self.spec_type is not None:
            result['specType'] = self.spec_type

        if self.storage_performance_level is not None:
            result['storagePerformanceLevel'] = self.storage_performance_level

        if self.storage_size is not None:
            result['storageSize'] = self.storage_size

        if self.zone_id is not None:
            result['zoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cu') is not None:
            self.cu = m.get('cu')

        if m.get('diskNumber') is not None:
            self.disk_number = m.get('diskNumber')

        if m.get('localStorageInstanceType') is not None:
            self.local_storage_instance_type = m.get('localStorageInstanceType')

        if m.get('residentNodeNumber') is not None:
            self.resident_node_number = m.get('residentNodeNumber')

        if m.get('specType') is not None:
            self.spec_type = m.get('specType')

        if m.get('storagePerformanceLevel') is not None:
            self.storage_performance_level = m.get('storagePerformanceLevel')

        if m.get('storageSize') is not None:
            self.storage_size = m.get('storageSize')

        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')

        return self

class CreateInstanceV1RequestBackendNodeGroups(DaraModel):
    def __init__(
        self,
        cu: int = None,
        disk_number: int = None,
        local_storage_instance_type: str = None,
        resident_node_number: int = None,
        spec_type: str = None,
        storage_performance_level: str = None,
        storage_size: int = None,
        zone_id: str = None,
    ):
        # The number of CUs. A CU (Compute Unit) is the basic metering unit of the service. 1 CU = 1 CPU core + 4 GiB memory. When SpecType is set to memory-enhanced instance family, 1 CU = 1 CPU core + 8 GiB memory.
        self.cu = cu
        # The number of disks.
        self.disk_number = disk_number
        # The local SSD instance type of the node group. This parameter takes effect only when the instance is ECS-based and SpecType is set to local SSD or large-scale storage.
        self.local_storage_instance_type = local_storage_instance_type
        # The number of nodes.
        self.resident_node_number = resident_node_number
        # The specification type of the node group. Valid values:
        self.spec_type = spec_type
        # The performance level of the cloud disk. Valid values:
        # 
        # - pl0: A single disk delivers up to 10,000 random read/write IOPS.
        # - pl1: A single disk delivers up to 50,000 random read/write IOPS.
        # - pl2: A single disk delivers up to 100,000 random read/write IOPS.
        # - pl3: A single disk delivers up to 1,000,000 random read/write IOPS.
        self.storage_performance_level = storage_performance_level
        # The storage size. Unit: GiB.
        self.storage_size = storage_size
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cu is not None:
            result['cu'] = self.cu

        if self.disk_number is not None:
            result['diskNumber'] = self.disk_number

        if self.local_storage_instance_type is not None:
            result['localStorageInstanceType'] = self.local_storage_instance_type

        if self.resident_node_number is not None:
            result['residentNodeNumber'] = self.resident_node_number

        if self.spec_type is not None:
            result['specType'] = self.spec_type

        if self.storage_performance_level is not None:
            result['storagePerformanceLevel'] = self.storage_performance_level

        if self.storage_size is not None:
            result['storageSize'] = self.storage_size

        if self.zone_id is not None:
            result['zoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cu') is not None:
            self.cu = m.get('cu')

        if m.get('diskNumber') is not None:
            self.disk_number = m.get('diskNumber')

        if m.get('localStorageInstanceType') is not None:
            self.local_storage_instance_type = m.get('localStorageInstanceType')

        if m.get('residentNodeNumber') is not None:
            self.resident_node_number = m.get('residentNodeNumber')

        if m.get('specType') is not None:
            self.spec_type = m.get('specType')

        if m.get('storagePerformanceLevel') is not None:
            self.storage_performance_level = m.get('storagePerformanceLevel')

        if m.get('storageSize') is not None:
            self.storage_size = m.get('storageSize')

        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')

        return self

class CreateInstanceV1RequestAgentNodeGroup(DaraModel):
    def __init__(
        self,
        cu: int = None,
    ):
        self.cu = cu

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cu is not None:
            result['cu'] = self.cu

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cu') is not None:
            self.cu = m.get('cu')

        return self

