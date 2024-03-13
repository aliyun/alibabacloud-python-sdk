# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class AddonNodeTemplateDataDisks(TeaModel):
    def __init__(
        self,
        category: str = None,
        delete_with_instance: bool = None,
        level: str = None,
        size: int = None,
    ):
        self.category = category
        self.delete_with_instance = delete_with_instance
        self.level = level
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.delete_with_instance is not None:
            result['DeleteWithInstance'] = self.delete_with_instance
        if self.level is not None:
            result['Level'] = self.level
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('DeleteWithInstance') is not None:
            self.delete_with_instance = m.get('DeleteWithInstance')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class AddonNodeTemplateSystemDisk(TeaModel):
    def __init__(
        self,
        category: str = None,
        level: str = None,
        size: int = None,
    ):
        self.category = category
        self.level = level
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.level is not None:
            result['Level'] = self.level
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class AddonNodeTemplate(TeaModel):
    def __init__(
        self,
        auto_renew: bool = None,
        auto_renew_period: int = None,
        data_disks: List[AddonNodeTemplateDataDisks] = None,
        duration: int = None,
        enable_ht: bool = None,
        image_id: str = None,
        instance_charge_type: str = None,
        instance_type: str = None,
        os_name: str = None,
        os_name_en: str = None,
        period: int = None,
        period_unit: str = None,
        spot_price_limit: float = None,
        spot_strategy: str = None,
        system_disk: AddonNodeTemplateSystemDisk = None,
    ):
        self.auto_renew = auto_renew
        self.auto_renew_period = auto_renew_period
        self.data_disks = data_disks
        self.duration = duration
        self.enable_ht = enable_ht
        self.image_id = image_id
        self.instance_charge_type = instance_charge_type
        self.instance_type = instance_type
        self.os_name = os_name
        self.os_name_en = os_name_en
        self.period = period
        self.period_unit = period_unit
        self.spot_price_limit = spot_price_limit
        self.spot_strategy = spot_strategy
        self.system_disk = system_disk

    def validate(self):
        if self.data_disks:
            for k in self.data_disks:
                if k:
                    k.validate()
        if self.system_disk:
            self.system_disk.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period
        result['DataDisks'] = []
        if self.data_disks is not None:
            for k in self.data_disks:
                result['DataDisks'].append(k.to_map() if k else None)
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.enable_ht is not None:
            result['EnableHT'] = self.enable_ht
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.os_name is not None:
            result['OsName'] = self.os_name
        if self.os_name_en is not None:
            result['OsNameEN'] = self.os_name_en
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.spot_price_limit is not None:
            result['SpotPriceLimit'] = self.spot_price_limit
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')
        self.data_disks = []
        if m.get('DataDisks') is not None:
            for k in m.get('DataDisks'):
                temp_model = AddonNodeTemplateDataDisks()
                self.data_disks.append(temp_model.from_map(k))
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('EnableHT') is not None:
            self.enable_ht = m.get('EnableHT')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('OsName') is not None:
            self.os_name = m.get('OsName')
        if m.get('OsNameEN') is not None:
            self.os_name_en = m.get('OsNameEN')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('SpotPriceLimit') is not None:
            self.spot_price_limit = m.get('SpotPriceLimit')
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        if m.get('SystemDisk') is not None:
            temp_model = AddonNodeTemplateSystemDisk()
            self.system_disk = temp_model.from_map(m['SystemDisk'])
        return self


class NodeTemplateDataDisks(TeaModel):
    def __init__(
        self,
        category: str = None,
        delete_with_instance: bool = None,
        level: str = None,
        size: int = None,
    ):
        self.category = category
        self.delete_with_instance = delete_with_instance
        self.level = level
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.delete_with_instance is not None:
            result['DeleteWithInstance'] = self.delete_with_instance
        if self.level is not None:
            result['Level'] = self.level
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('DeleteWithInstance') is not None:
            self.delete_with_instance = m.get('DeleteWithInstance')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class NodeTemplateSystemDisk(TeaModel):
    def __init__(
        self,
        category: str = None,
        level: str = None,
        size: int = None,
    ):
        self.category = category
        self.level = level
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.level is not None:
            result['Level'] = self.level
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class NodeTemplate(TeaModel):
    def __init__(
        self,
        auto_renew: bool = None,
        auto_renew_period: int = None,
        data_disks: List[NodeTemplateDataDisks] = None,
        duration: int = None,
        enable_ht: bool = None,
        image_id: str = None,
        instance_charge_type: str = None,
        instance_type: str = None,
        period: int = None,
        period_unit: str = None,
        spot_price_limit: float = None,
        spot_strategy: str = None,
        system_disk: NodeTemplateSystemDisk = None,
    ):
        self.auto_renew = auto_renew
        self.auto_renew_period = auto_renew_period
        self.data_disks = data_disks
        self.duration = duration
        self.enable_ht = enable_ht
        self.image_id = image_id
        self.instance_charge_type = instance_charge_type
        self.instance_type = instance_type
        self.period = period
        self.period_unit = period_unit
        self.spot_price_limit = spot_price_limit
        self.spot_strategy = spot_strategy
        self.system_disk = system_disk

    def validate(self):
        if self.data_disks:
            for k in self.data_disks:
                if k:
                    k.validate()
        if self.system_disk:
            self.system_disk.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period
        result['DataDisks'] = []
        if self.data_disks is not None:
            for k in self.data_disks:
                result['DataDisks'].append(k.to_map() if k else None)
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.enable_ht is not None:
            result['EnableHT'] = self.enable_ht
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.spot_price_limit is not None:
            result['SpotPriceLimit'] = self.spot_price_limit
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')
        self.data_disks = []
        if m.get('DataDisks') is not None:
            for k in m.get('DataDisks'):
                temp_model = NodeTemplateDataDisks()
                self.data_disks.append(temp_model.from_map(k))
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('EnableHT') is not None:
            self.enable_ht = m.get('EnableHT')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('SpotPriceLimit') is not None:
            self.spot_price_limit = m.get('SpotPriceLimit')
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        if m.get('SystemDisk') is not None:
            temp_model = NodeTemplateSystemDisk()
            self.system_disk = temp_model.from_map(m['SystemDisk'])
        return self


class QueueTemplate(TeaModel):
    def __init__(
        self,
        allocation_strategy: str = None,
        compute_nodes: List[NodeTemplate] = None,
        enable_scale_in: bool = None,
        enable_scale_out: bool = None,
        hostname_prefix: str = None,
        hostname_suffix: str = None,
        initial_count: int = None,
        inter_connect: str = None,
        keep_alive_nodes: List[str] = None,
        max_count: int = None,
        max_count_per_cycle: int = None,
        min_count: int = None,
        name: str = None,
        ram_role: str = None,
        v_switch_ids: List[str] = None,
    ):
        self.allocation_strategy = allocation_strategy
        self.compute_nodes = compute_nodes
        self.enable_scale_in = enable_scale_in
        self.enable_scale_out = enable_scale_out
        self.hostname_prefix = hostname_prefix
        self.hostname_suffix = hostname_suffix
        self.initial_count = initial_count
        self.inter_connect = inter_connect
        self.keep_alive_nodes = keep_alive_nodes
        self.max_count = max_count
        self.max_count_per_cycle = max_count_per_cycle
        self.min_count = min_count
        self.name = name
        self.ram_role = ram_role
        self.v_switch_ids = v_switch_ids

    def validate(self):
        if self.compute_nodes:
            for k in self.compute_nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allocation_strategy is not None:
            result['AllocationStrategy'] = self.allocation_strategy
        result['ComputeNodes'] = []
        if self.compute_nodes is not None:
            for k in self.compute_nodes:
                result['ComputeNodes'].append(k.to_map() if k else None)
        if self.enable_scale_in is not None:
            result['EnableScaleIn'] = self.enable_scale_in
        if self.enable_scale_out is not None:
            result['EnableScaleOut'] = self.enable_scale_out
        if self.hostname_prefix is not None:
            result['HostnamePrefix'] = self.hostname_prefix
        if self.hostname_suffix is not None:
            result['HostnameSuffix'] = self.hostname_suffix
        if self.initial_count is not None:
            result['InitialCount'] = self.initial_count
        if self.inter_connect is not None:
            result['InterConnect'] = self.inter_connect
        if self.keep_alive_nodes is not None:
            result['KeepAliveNodes'] = self.keep_alive_nodes
        if self.max_count is not None:
            result['MaxCount'] = self.max_count
        if self.max_count_per_cycle is not None:
            result['MaxCountPerCycle'] = self.max_count_per_cycle
        if self.min_count is not None:
            result['MinCount'] = self.min_count
        if self.name is not None:
            result['Name'] = self.name
        if self.ram_role is not None:
            result['RamRole'] = self.ram_role
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationStrategy') is not None:
            self.allocation_strategy = m.get('AllocationStrategy')
        self.compute_nodes = []
        if m.get('ComputeNodes') is not None:
            for k in m.get('ComputeNodes'):
                temp_model = NodeTemplate()
                self.compute_nodes.append(temp_model.from_map(k))
        if m.get('EnableScaleIn') is not None:
            self.enable_scale_in = m.get('EnableScaleIn')
        if m.get('EnableScaleOut') is not None:
            self.enable_scale_out = m.get('EnableScaleOut')
        if m.get('HostnamePrefix') is not None:
            self.hostname_prefix = m.get('HostnamePrefix')
        if m.get('HostnameSuffix') is not None:
            self.hostname_suffix = m.get('HostnameSuffix')
        if m.get('InitialCount') is not None:
            self.initial_count = m.get('InitialCount')
        if m.get('InterConnect') is not None:
            self.inter_connect = m.get('InterConnect')
        if m.get('KeepAliveNodes') is not None:
            self.keep_alive_nodes = m.get('KeepAliveNodes')
        if m.get('MaxCount') is not None:
            self.max_count = m.get('MaxCount')
        if m.get('MaxCountPerCycle') is not None:
            self.max_count_per_cycle = m.get('MaxCountPerCycle')
        if m.get('MinCount') is not None:
            self.min_count = m.get('MinCount')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RamRole') is not None:
            self.ram_role = m.get('RamRole')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        return self


class SharedStorageTemplate(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        mount_directory: str = None,
        mount_options: str = None,
        mount_target_domain: str = None,
        nasdirectory: str = None,
        protocol_type: str = None,
    ):
        self.file_system_id = file_system_id
        self.mount_directory = mount_directory
        self.mount_options = mount_options
        self.mount_target_domain = mount_target_domain
        self.nasdirectory = nasdirectory
        self.protocol_type = protocol_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.mount_directory is not None:
            result['MountDirectory'] = self.mount_directory
        if self.mount_options is not None:
            result['MountOptions'] = self.mount_options
        if self.mount_target_domain is not None:
            result['MountTargetDomain'] = self.mount_target_domain
        if self.nasdirectory is not None:
            result['NASDirectory'] = self.nasdirectory
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('MountDirectory') is not None:
            self.mount_directory = m.get('MountDirectory')
        if m.get('MountOptions') is not None:
            self.mount_options = m.get('MountOptions')
        if m.get('MountTargetDomain') is not None:
            self.mount_target_domain = m.get('MountTargetDomain')
        if m.get('NASDirectory') is not None:
            self.nasdirectory = m.get('NASDirectory')
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        return self


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
        name: str = None,
        vmimage_spec: AddImageRequestVMImageSpec = None,
        version: str = None,
    ):
        self.container_image_spec = container_image_spec
        self.description = description
        self.name = name
        self.vmimage_spec = vmimage_spec
        self.version = version

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
        if self.name is not None:
            result['Name'] = self.name
        if self.vmimage_spec is not None:
            result['VMImageSpec'] = self.vmimage_spec.to_map()
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerImageSpec') is not None:
            temp_model = AddImageRequestContainerImageSpec()
            self.container_image_spec = temp_model.from_map(m['ContainerImageSpec'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('VMImageSpec') is not None:
            temp_model = AddImageRequestVMImageSpec()
            self.vmimage_spec = temp_model.from_map(m['VMImageSpec'])
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class AddImageShrinkRequest(TeaModel):
    def __init__(
        self,
        container_image_spec_shrink: str = None,
        description: str = None,
        name: str = None,
        vmimage_spec_shrink: str = None,
        version: str = None,
    ):
        self.container_image_spec_shrink = container_image_spec_shrink
        self.description = description
        self.name = name
        self.vmimage_spec_shrink = vmimage_spec_shrink
        self.version = version

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
        if self.name is not None:
            result['Name'] = self.name
        if self.vmimage_spec_shrink is not None:
            result['VMImageSpec'] = self.vmimage_spec_shrink
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerImageSpec') is not None:
            self.container_image_spec_shrink = m.get('ContainerImageSpec')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('VMImageSpec') is not None:
            self.vmimage_spec_shrink = m.get('VMImageSpec')
        if m.get('Version') is not None:
            self.version = m.get('Version')
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
        vswitch: List[str] = None,
    ):
        self.vswitch = vswitch

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vswitch is not None:
            result['Vswitch'] = self.vswitch
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Vswitch') is not None:
            self.vswitch = m.get('Vswitch')
        return self


class CreateJobRequestDeploymentPolicy(TeaModel):
    def __init__(
        self,
        allocation_spec: str = None,
        network: CreateJobRequestDeploymentPolicyNetwork = None,
    ):
        self.allocation_spec = allocation_spec
        self.network = network

    def validate(self):
        if self.network:
            self.network.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allocation_spec is not None:
            result['AllocationSpec'] = self.allocation_spec
        if self.network is not None:
            result['Network'] = self.network.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationSpec') is not None:
            self.allocation_spec = m.get('AllocationSpec')
        if m.get('Network') is not None:
            temp_model = CreateJobRequestDeploymentPolicyNetwork()
            self.network = temp_model.from_map(m['Network'])
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
                temp_model = CreateJobRequestTasksTaskSpecResourceDisks()
                self.disks.append(temp_model.from_map(k))
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        return self


class CreateJobRequestTasksTaskSpecTaskExecutorVM(TeaModel):
    def __init__(
        self,
        image: str = None,
        prolog_script: str = None,
        script: str = None,
    ):
        self.image = image
        self.prolog_script = prolog_script
        self.script = script

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('PrologScript') is not None:
            self.prolog_script = m.get('PrologScript')
        if m.get('Script') is not None:
            self.script = m.get('Script')
        return self


class CreateJobRequestTasksTaskSpecTaskExecutor(TeaModel):
    def __init__(
        self,
        vm: CreateJobRequestTasksTaskSpecTaskExecutorVM = None,
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
            temp_model = CreateJobRequestTasksTaskSpecTaskExecutorVM()
            self.vm = temp_model.from_map(m['VM'])
        return self


class CreateJobRequestTasksTaskSpec(TeaModel):
    def __init__(
        self,
        resource: CreateJobRequestTasksTaskSpecResource = None,
        task_executor: List[CreateJobRequestTasksTaskSpecTaskExecutor] = None,
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
            temp_model = CreateJobRequestTasksTaskSpecResource()
            self.resource = temp_model.from_map(m['Resource'])
        self.task_executor = []
        if m.get('TaskExecutor') is not None:
            for k in m.get('TaskExecutor'):
                temp_model = CreateJobRequestTasksTaskSpecTaskExecutor()
                self.task_executor.append(temp_model.from_map(k))
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
        tasks: List[CreateJobRequestTasks] = None,
    ):
        self.deployment_policy = deployment_policy
        self.job_description = job_description
        self.job_name = job_name
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
        if self.deployment_policy is not None:
            result['DeploymentPolicy'] = self.deployment_policy.to_map()
        if self.job_description is not None:
            result['JobDescription'] = self.job_description
        if self.job_name is not None:
            result['JobName'] = self.job_name
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
        tasks_shrink: str = None,
    ):
        self.deployment_policy_shrink = deployment_policy_shrink
        self.job_description = job_description
        self.job_name = job_name
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
        if m.get('Tasks') is not None:
            self.tasks_shrink = m.get('Tasks')
        return self


class CreateJobResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        self.job_id = job_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
        job_spec: List[DeleteJobsRequestJobSpec] = None,
    ):
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
        result['JobSpec'] = []
        if self.job_spec is not None:
            for k in self.job_spec:
                result['JobSpec'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.job_spec = []
        if m.get('JobSpec') is not None:
            for k in m.get('JobSpec'):
                temp_model = DeleteJobsRequestJobSpec()
                self.job_spec.append(temp_model.from_map(k))
        return self


class DeleteJobsShrinkRequest(TeaModel):
    def __init__(
        self,
        job_spec_shrink: str = None,
    ):
        self.job_spec_shrink = job_spec_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_spec_shrink is not None:
            result['JobSpec'] = self.job_spec_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobSpec') is not None:
            self.job_spec_shrink = m.get('JobSpec')
        return self


class DeleteJobsResponseBody(TeaModel):
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


class GetImageRequest(TeaModel):
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
        is_acrenterprise: bool = None,
        is_acrregistry: bool = None,
        registry_credential: GetImageResponseBodyImageContainerImageSpecRegistryCredential = None,
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
            temp_model = GetImageResponseBodyImageContainerImageSpecRegistryCredential()
            self.registry_credential = temp_model.from_map(m['RegistryCredential'])
        if m.get('RegistryCriId') is not None:
            self.registry_cri_id = m.get('RegistryCriId')
        if m.get('RegistryUrl') is not None:
            self.registry_url = m.get('RegistryUrl')
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
        container_image_spec: GetImageResponseBodyImageContainerImageSpec = None,
        create_time: str = None,
        description: str = None,
        image_type: str = None,
        name: str = None,
        size: str = None,
        vmimage_spec: GetImageResponseBodyImageVMImageSpec = None,
        version: str = None,
    ):
        self.container_image_spec = container_image_spec
        self.create_time = create_time
        self.description = description
        self.image_type = image_type
        self.name = name
        self.size = size
        self.vmimage_spec = vmimage_spec
        self.version = version

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
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.name is not None:
            result['Name'] = self.name
        if self.size is not None:
            result['Size'] = self.size
        if self.vmimage_spec is not None:
            result['VMImageSpec'] = self.vmimage_spec.to_map()
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerImageSpec') is not None:
            temp_model = GetImageResponseBodyImageContainerImageSpec()
            self.container_image_spec = temp_model.from_map(m['ContainerImageSpec'])
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Size') is not None:
            self.size = m.get('Size')
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
        vswitch: List[str] = None,
    ):
        self.vswitch = vswitch

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vswitch is not None:
            result['Vswitch'] = self.vswitch
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Vswitch') is not None:
            self.vswitch = m.get('Vswitch')
        return self


class GetJobResponseBodyJobInfoDeploymentPolicy(TeaModel):
    def __init__(
        self,
        allocation_spec: str = None,
        network: GetJobResponseBodyJobInfoDeploymentPolicyNetwork = None,
    ):
        self.allocation_spec = allocation_spec
        self.network = network

    def validate(self):
        if self.network:
            self.network.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allocation_spec is not None:
            result['AllocationSpec'] = self.allocation_spec
        if self.network is not None:
            result['Network'] = self.network.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationSpec') is not None:
            self.allocation_spec = m.get('AllocationSpec')
        if m.get('Network') is not None:
            temp_model = GetJobResponseBodyJobInfoDeploymentPolicyNetwork()
            self.network = temp_model.from_map(m['Network'])
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
        memory: int = None,
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
                temp_model = GetJobResponseBodyJobInfoTasksTaskSpecResourceDisks()
                self.disks.append(temp_model.from_map(k))
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        return self


class GetJobResponseBodyJobInfoTasksTaskSpecTaskExecutorVM(TeaModel):
    def __init__(
        self,
        image: str = None,
        prolog_script: str = None,
        script: str = None,
    ):
        self.image = image
        self.prolog_script = prolog_script
        self.script = script

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('PrologScript') is not None:
            self.prolog_script = m.get('PrologScript')
        if m.get('Script') is not None:
            self.script = m.get('Script')
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
        create_time: str = None,
        deployment_policy: GetJobResponseBodyJobInfoDeploymentPolicy = None,
        end_time: str = None,
        job_description: str = None,
        job_id: str = None,
        job_name: str = None,
        start_time: str = None,
        status: str = None,
        tasks: List[GetJobResponseBodyJobInfoTasks] = None,
    ):
        self.create_time = create_time
        self.deployment_policy = deployment_policy
        self.end_time = end_time
        self.job_description = job_description
        self.job_id = job_id
        self.job_name = job_name
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
        # Id of the request
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


class ListImagesRequest(TeaModel):
    def __init__(
        self,
        image_ids: List[str] = None,
        image_names: List[str] = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.image_ids = image_ids
        self.image_names = image_names
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_ids is not None:
            result['ImageIds'] = self.image_ids
        if self.image_names is not None:
            result['ImageNames'] = self.image_names
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageIds') is not None:
            self.image_ids = m.get('ImageIds')
        if m.get('ImageNames') is not None:
            self.image_names = m.get('ImageNames')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListImagesShrinkRequest(TeaModel):
    def __init__(
        self,
        image_ids_shrink: str = None,
        image_names_shrink: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.image_ids_shrink = image_ids_shrink
        self.image_names_shrink = image_names_shrink
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_ids_shrink is not None:
            result['ImageIds'] = self.image_ids_shrink
        if self.image_names_shrink is not None:
            result['ImageNames'] = self.image_names_shrink
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageIds') is not None:
            self.image_ids_shrink = m.get('ImageIds')
        if m.get('ImageNames') is not None:
            self.image_names_shrink = m.get('ImageNames')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListImagesResponseBodyImages(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        image_id: str = None,
        image_type: str = None,
        name: str = None,
        version: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.image_id = image_id
        self.image_type = image_type
        self.name = name
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.name is not None:
            result['Name'] = self.name
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Version') is not None:
            self.version = m.get('Version')
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
        page_number: str = None,
        page_size: str = None,
        task_name: str = None,
    ):
        self.job_id = job_id
        self.page_number = page_number
        self.page_size = page_size
        # Task ID
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


class ListJobExecutorsResponseBodyExecutors(TeaModel):
    def __init__(
        self,
        array_index: int = None,
        create_time: str = None,
        end_time: str = None,
        host_name: List[str] = None,
        ip_address: List[str] = None,
        status: str = None,
        status_reason: str = None,
    ):
        self.array_index = array_index
        self.create_time = create_time
        self.end_time = end_time
        self.host_name = host_name
        self.ip_address = ip_address
        self.status = status
        self.status_reason = status_reason

    def validate(self):
        pass

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
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address
        if self.status is not None:
            result['Status'] = self.status
        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArrayIndex') is not None:
            self.array_index = m.get('ArrayIndex')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')
        return self


class ListJobExecutorsResponseBody(TeaModel):
    def __init__(
        self,
        executors: List[ListJobExecutorsResponseBodyExecutors] = None,
        job_id: str = None,
        page_number: str = None,
        page_size: str = None,
        request_id: str = None,
        task_name: str = None,
        total_count: str = None,
    ):
        self.executors = executors
        self.job_id = job_id
        self.page_number = page_number
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        self.task_name = task_name
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
        page_number: str = None,
        page_size: str = None,
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
        page_number: str = None,
        page_size: str = None,
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


class ListJobsResponseBodyJobList(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        end_time: str = None,
        executor_count: int = None,
        job_description: str = None,
        job_id: str = None,
        job_name: str = None,
        owner_uid: str = None,
        start_time: str = None,
        status: str = None,
        task_count: int = None,
        task_sustainable: bool = None,
    ):
        self.create_time = create_time
        self.end_time = end_time
        self.executor_count = executor_count
        self.job_description = job_description
        self.job_id = job_id
        self.job_name = job_name
        self.owner_uid = owner_uid
        self.start_time = start_time
        self.status = status
        self.task_count = task_count
        self.task_sustainable = task_sustainable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.task_count is not None:
            result['TaskCount'] = self.task_count
        if self.task_sustainable is not None:
            result['TaskSustainable'] = self.task_sustainable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
        # Id of the request
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


class RemoveImageRequest(TeaModel):
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


