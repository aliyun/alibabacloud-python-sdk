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
        # This parameter is required.
        self.admin_password = admin_password
        self.agent_node_group = agent_node_group
        self.auto_pay = auto_pay
        self.auto_renew = auto_renew
        self.backend_node_groups = backend_node_groups
        self.client_token = client_token
        self.dlf_catalog_name = dlf_catalog_name
        self.dlf_catalog_type = dlf_catalog_type
        self.duration = duration
        self.encrypted = encrypted
        self.frontend_node_groups = frontend_node_groups
        self.gateway_type = gateway_type
        # This parameter is required.
        self.instance_name = instance_name
        self.kms_key_id = kms_key_id
        self.linked_ram_user_name = linked_ram_user_name
        self.observer_node_groups = observer_node_groups
        self.oss_accessing_role_name = oss_accessing_role_name
        # This parameter is required.
        self.package_type = package_type
        # This parameter is required.
        self.pay_type = pay_type
        self.pricing_cycle = pricing_cycle
        self.principal_type = principal_type
        self.promotion_option_no = promotion_option_no
        self.ram_user_id = ram_user_id
        # This parameter is required.
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        # This parameter is required.
        self.run_mode = run_mode
        self.tags = tags
        self.v_switches = v_switches
        # This parameter is required.
        self.version = version
        # VPC ID。
        # 
        # This parameter is required.
        self.vpc_id = vpc_id
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
        # This parameter is required.
        self.vsw_id = vsw_id
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
        self.key = key
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
        self.cu = cu
        self.disk_number = disk_number
        self.local_storage_instance_type = local_storage_instance_type
        self.resident_node_number = resident_node_number
        self.spec_type = spec_type
        self.storage_performance_level = storage_performance_level
        self.storage_size = storage_size
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
        self.cu = cu
        self.disk_number = disk_number
        self.local_storage_instance_type = local_storage_instance_type
        self.resident_node_number = resident_node_number
        self.spec_type = spec_type
        self.storage_performance_level = storage_performance_level
        self.storage_size = storage_size
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
        self.cu = cu
        self.disk_number = disk_number
        self.local_storage_instance_type = local_storage_instance_type
        self.resident_node_number = resident_node_number
        self.spec_type = spec_type
        self.storage_performance_level = storage_performance_level
        self.storage_size = storage_size
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

