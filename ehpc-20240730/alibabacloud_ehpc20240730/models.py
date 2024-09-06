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
        instance_id: str = None,
        instance_type: str = None,
        os_name: str = None,
        os_name_en: str = None,
        period: int = None,
        period_unit: str = None,
        private_ip_address: str = None,
        spot_price_limit: float = None,
        spot_strategy: str = None,
        system_disk: AddonNodeTemplateSystemDisk = None,
    ):
        self.auto_renew = auto_renew
        self.auto_renew_period = auto_renew_period
        self.data_disks = data_disks
        self.duration = duration
        self.enable_ht = enable_ht
        # This parameter is required.
        self.image_id = image_id
        self.instance_charge_type = instance_charge_type
        self.instance_id = instance_id
        # This parameter is required.
        self.instance_type = instance_type
        # This parameter is required.
        self.os_name = os_name
        # This parameter is required.
        self.os_name_en = os_name_en
        self.period = period
        self.period_unit = period_unit
        self.private_ip_address = private_ip_address
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
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
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
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
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
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
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
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')
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
        queue_name: str = None,
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
        # This parameter is required.
        self.queue_name = queue_name
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
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
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
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
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


class AttachSharedStoragesRequestSharedStorages(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        location: str = None,
        mount_directory: str = None,
        mount_options: str = None,
        mount_target: str = None,
        protocol_type: str = None,
        storage_directory: str = None,
        volume_type: str = None,
    ):
        # This parameter is required.
        self.file_system_id = file_system_id
        self.location = location
        # This parameter is required.
        self.mount_directory = mount_directory
        self.mount_options = mount_options
        # This parameter is required.
        self.mount_target = mount_target
        # This parameter is required.
        self.protocol_type = protocol_type
        # This parameter is required.
        self.storage_directory = storage_directory
        # This parameter is required.
        self.volume_type = volume_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.location is not None:
            result['Location'] = self.location
        if self.mount_directory is not None:
            result['MountDirectory'] = self.mount_directory
        if self.mount_options is not None:
            result['MountOptions'] = self.mount_options
        if self.mount_target is not None:
            result['MountTarget'] = self.mount_target
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.storage_directory is not None:
            result['StorageDirectory'] = self.storage_directory
        if self.volume_type is not None:
            result['VolumeType'] = self.volume_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('MountDirectory') is not None:
            self.mount_directory = m.get('MountDirectory')
        if m.get('MountOptions') is not None:
            self.mount_options = m.get('MountOptions')
        if m.get('MountTarget') is not None:
            self.mount_target = m.get('MountTarget')
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('StorageDirectory') is not None:
            self.storage_directory = m.get('StorageDirectory')
        if m.get('VolumeType') is not None:
            self.volume_type = m.get('VolumeType')
        return self


class AttachSharedStoragesRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        shared_storages: List[AttachSharedStoragesRequestSharedStorages] = None,
    ):
        # This parameter is required.
        self.cluster_id = cluster_id
        # This parameter is required.
        self.shared_storages = shared_storages

    def validate(self):
        if self.shared_storages:
            for k in self.shared_storages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        result['SharedStorages'] = []
        if self.shared_storages is not None:
            for k in self.shared_storages:
                result['SharedStorages'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        self.shared_storages = []
        if m.get('SharedStorages') is not None:
            for k in m.get('SharedStorages'):
                temp_model = AttachSharedStoragesRequestSharedStorages()
                self.shared_storages.append(temp_model.from_map(k))
        return self


class AttachSharedStoragesShrinkRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        shared_storages_shrink: str = None,
    ):
        # This parameter is required.
        self.cluster_id = cluster_id
        # This parameter is required.
        self.shared_storages_shrink = shared_storages_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.shared_storages_shrink is not None:
            result['SharedStorages'] = self.shared_storages_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('SharedStorages') is not None:
            self.shared_storages_shrink = m.get('SharedStorages')
        return self


class AttachSharedStoragesResponseBody(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.cluster_id = cluster_id
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AttachSharedStoragesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AttachSharedStoragesResponseBody = None,
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
            temp_model = AttachSharedStoragesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateClusterRequestAdditionalPackages(TeaModel):
    def __init__(
        self,
        name: str = None,
        version: str = None,
    ):
        self.name = name
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateClusterRequestAddons(TeaModel):
    def __init__(
        self,
        name: str = None,
        resources_spec: str = None,
        services_spec: str = None,
        version: str = None,
    ):
        # This parameter is required.
        self.name = name
        self.resources_spec = resources_spec
        self.services_spec = services_spec
        # This parameter is required.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateClusterRequestClusterCredentials(TeaModel):
    def __init__(
        self,
        key_pair_name: str = None,
        password: str = None,
    ):
        self.key_pair_name = key_pair_name
        self.password = password

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateClusterRequestClusterCustomConfiguration(TeaModel):
    def __init__(
        self,
        args: str = None,
        script: str = None,
    ):
        self.args = args
        self.script = script

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateClusterRequestManagerDNS(TeaModel):
    def __init__(
        self,
        type: str = None,
        version: str = None,
    ):
        self.type = type
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateClusterRequestManagerDirectoryService(TeaModel):
    def __init__(
        self,
        type: str = None,
        version: str = None,
    ):
        self.type = type
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateClusterRequestManagerScheduler(TeaModel):
    def __init__(
        self,
        type: str = None,
        version: str = None,
    ):
        self.type = type
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateClusterRequestManager(TeaModel):
    def __init__(
        self,
        dns: CreateClusterRequestManagerDNS = None,
        directory_service: CreateClusterRequestManagerDirectoryService = None,
        manager_node: NodeTemplate = None,
        scheduler: CreateClusterRequestManagerScheduler = None,
    ):
        self.dns = dns
        self.directory_service = directory_service
        self.manager_node = manager_node
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = CreateClusterRequestManagerDNS()
            self.dns = temp_model.from_map(m['DNS'])
        if m.get('DirectoryService') is not None:
            temp_model = CreateClusterRequestManagerDirectoryService()
            self.directory_service = temp_model.from_map(m['DirectoryService'])
        if m.get('ManagerNode') is not None:
            temp_model = NodeTemplate()
            self.manager_node = temp_model.from_map(m['ManagerNode'])
        if m.get('Scheduler') is not None:
            temp_model = CreateClusterRequestManagerScheduler()
            self.scheduler = temp_model.from_map(m['Scheduler'])
        return self


class CreateClusterRequestTags(TeaModel):
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


class CreateClusterRequest(TeaModel):
    def __init__(
        self,
        additional_packages: List[CreateClusterRequestAdditionalPackages] = None,
        addons: List[CreateClusterRequestAddons] = None,
        client_version: str = None,
        cluster_category: str = None,
        cluster_credentials: CreateClusterRequestClusterCredentials = None,
        cluster_custom_configuration: CreateClusterRequestClusterCustomConfiguration = None,
        cluster_description: str = None,
        cluster_mode: str = None,
        cluster_name: str = None,
        cluster_vswitch_id: str = None,
        cluster_vpc_id: str = None,
        deletion_protection: bool = None,
        is_enterprise_security_group: bool = None,
        manager: CreateClusterRequestManager = None,
        max_core_count: int = None,
        max_count: int = None,
        queues: List[QueueTemplate] = None,
        resource_group_id: str = None,
        security_group_id: str = None,
        shared_storages: List[SharedStorageTemplate] = None,
        tags: List[CreateClusterRequestTags] = None,
    ):
        self.additional_packages = additional_packages
        self.addons = addons
        self.client_version = client_version
        self.cluster_category = cluster_category
        self.cluster_credentials = cluster_credentials
        self.cluster_custom_configuration = cluster_custom_configuration
        self.cluster_description = cluster_description
        self.cluster_mode = cluster_mode
        self.cluster_name = cluster_name
        self.cluster_vswitch_id = cluster_vswitch_id
        self.cluster_vpc_id = cluster_vpc_id
        self.deletion_protection = deletion_protection
        self.is_enterprise_security_group = is_enterprise_security_group
        self.manager = manager
        self.max_core_count = max_core_count
        self.max_count = max_count
        self.queues = queues
        self.resource_group_id = resource_group_id
        self.security_group_id = security_group_id
        self.shared_storages = shared_storages
        self.tags = tags

    def validate(self):
        if self.additional_packages:
            for k in self.additional_packages:
                if k:
                    k.validate()
        if self.addons:
            for k in self.addons:
                if k:
                    k.validate()
        if self.cluster_credentials:
            self.cluster_credentials.validate()
        if self.cluster_custom_configuration:
            self.cluster_custom_configuration.validate()
        if self.manager:
            self.manager.validate()
        if self.queues:
            for k in self.queues:
                if k:
                    k.validate()
        if self.shared_storages:
            for k in self.shared_storages:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AdditionalPackages'] = []
        if self.additional_packages is not None:
            for k in self.additional_packages:
                result['AdditionalPackages'].append(k.to_map() if k else None)
        result['Addons'] = []
        if self.addons is not None:
            for k in self.addons:
                result['Addons'].append(k.to_map() if k else None)
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
            for k in self.queues:
                result['Queues'].append(k.to_map() if k else None)
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        result['SharedStorages'] = []
        if self.shared_storages is not None:
            for k in self.shared_storages:
                result['SharedStorages'].append(k.to_map() if k else None)
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.additional_packages = []
        if m.get('AdditionalPackages') is not None:
            for k in m.get('AdditionalPackages'):
                temp_model = CreateClusterRequestAdditionalPackages()
                self.additional_packages.append(temp_model.from_map(k))
        self.addons = []
        if m.get('Addons') is not None:
            for k in m.get('Addons'):
                temp_model = CreateClusterRequestAddons()
                self.addons.append(temp_model.from_map(k))
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('ClusterCategory') is not None:
            self.cluster_category = m.get('ClusterCategory')
        if m.get('ClusterCredentials') is not None:
            temp_model = CreateClusterRequestClusterCredentials()
            self.cluster_credentials = temp_model.from_map(m['ClusterCredentials'])
        if m.get('ClusterCustomConfiguration') is not None:
            temp_model = CreateClusterRequestClusterCustomConfiguration()
            self.cluster_custom_configuration = temp_model.from_map(m['ClusterCustomConfiguration'])
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
            temp_model = CreateClusterRequestManager()
            self.manager = temp_model.from_map(m['Manager'])
        if m.get('MaxCoreCount') is not None:
            self.max_core_count = m.get('MaxCoreCount')
        if m.get('MaxCount') is not None:
            self.max_count = m.get('MaxCount')
        self.queues = []
        if m.get('Queues') is not None:
            for k in m.get('Queues'):
                temp_model = QueueTemplate()
                self.queues.append(temp_model.from_map(k))
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        self.shared_storages = []
        if m.get('SharedStorages') is not None:
            for k in m.get('SharedStorages'):
                temp_model = SharedStorageTemplate()
                self.shared_storages.append(temp_model.from_map(k))
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = CreateClusterRequestTags()
                self.tags.append(temp_model.from_map(k))
        return self


class CreateClusterShrinkRequest(TeaModel):
    def __init__(
        self,
        additional_packages_shrink: str = None,
        addons_shrink: str = None,
        client_version: str = None,
        cluster_category: str = None,
        cluster_credentials_shrink: str = None,
        cluster_custom_configuration_shrink: str = None,
        cluster_description: str = None,
        cluster_mode: str = None,
        cluster_name: str = None,
        cluster_vswitch_id: str = None,
        cluster_vpc_id: str = None,
        deletion_protection: bool = None,
        is_enterprise_security_group: bool = None,
        manager_shrink: str = None,
        max_core_count: int = None,
        max_count: int = None,
        queues_shrink: str = None,
        resource_group_id: str = None,
        security_group_id: str = None,
        shared_storages_shrink: str = None,
        tags_shrink: str = None,
    ):
        self.additional_packages_shrink = additional_packages_shrink
        self.addons_shrink = addons_shrink
        self.client_version = client_version
        self.cluster_category = cluster_category
        self.cluster_credentials_shrink = cluster_credentials_shrink
        self.cluster_custom_configuration_shrink = cluster_custom_configuration_shrink
        self.cluster_description = cluster_description
        self.cluster_mode = cluster_mode
        self.cluster_name = cluster_name
        self.cluster_vswitch_id = cluster_vswitch_id
        self.cluster_vpc_id = cluster_vpc_id
        self.deletion_protection = deletion_protection
        self.is_enterprise_security_group = is_enterprise_security_group
        self.manager_shrink = manager_shrink
        self.max_core_count = max_core_count
        self.max_count = max_count
        self.queues_shrink = queues_shrink
        self.resource_group_id = resource_group_id
        self.security_group_id = security_group_id
        self.shared_storages_shrink = shared_storages_shrink
        self.tags_shrink = tags_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.additional_packages_shrink is not None:
            result['AdditionalPackages'] = self.additional_packages_shrink
        if self.addons_shrink is not None:
            result['Addons'] = self.addons_shrink
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.cluster_category is not None:
            result['ClusterCategory'] = self.cluster_category
        if self.cluster_credentials_shrink is not None:
            result['ClusterCredentials'] = self.cluster_credentials_shrink
        if self.cluster_custom_configuration_shrink is not None:
            result['ClusterCustomConfiguration'] = self.cluster_custom_configuration_shrink
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
        if self.manager_shrink is not None:
            result['Manager'] = self.manager_shrink
        if self.max_core_count is not None:
            result['MaxCoreCount'] = self.max_core_count
        if self.max_count is not None:
            result['MaxCount'] = self.max_count
        if self.queues_shrink is not None:
            result['Queues'] = self.queues_shrink
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.shared_storages_shrink is not None:
            result['SharedStorages'] = self.shared_storages_shrink
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdditionalPackages') is not None:
            self.additional_packages_shrink = m.get('AdditionalPackages')
        if m.get('Addons') is not None:
            self.addons_shrink = m.get('Addons')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('ClusterCategory') is not None:
            self.cluster_category = m.get('ClusterCategory')
        if m.get('ClusterCredentials') is not None:
            self.cluster_credentials_shrink = m.get('ClusterCredentials')
        if m.get('ClusterCustomConfiguration') is not None:
            self.cluster_custom_configuration_shrink = m.get('ClusterCustomConfiguration')
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
            self.manager_shrink = m.get('Manager')
        if m.get('MaxCoreCount') is not None:
            self.max_core_count = m.get('MaxCoreCount')
        if m.get('MaxCount') is not None:
            self.max_count = m.get('MaxCount')
        if m.get('Queues') is not None:
            self.queues_shrink = m.get('Queues')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('SharedStorages') is not None:
            self.shared_storages_shrink = m.get('SharedStorages')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        return self


class CreateClusterResponseBody(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateClusterResponseBody = None,
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
            temp_model = CreateClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateNodesRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        compute_node: NodeTemplate = None,
        count: int = None,
        hpcinter_connect: str = None,
        hostname_prefix: str = None,
        hostname_suffix: str = None,
        keep_alive: str = None,
        queue_name: str = None,
        ram_role: str = None,
        v_switch_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.compute_node = compute_node
        self.count = count
        self.hpcinter_connect = hpcinter_connect
        self.hostname_prefix = hostname_prefix
        self.hostname_suffix = hostname_suffix
        self.keep_alive = keep_alive
        self.queue_name = queue_name
        self.ram_role = ram_role
        self.v_switch_id = v_switch_id

    def validate(self):
        if self.compute_node:
            self.compute_node.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.compute_node is not None:
            result['ComputeNode'] = self.compute_node.to_map()
        if self.count is not None:
            result['Count'] = self.count
        if self.hpcinter_connect is not None:
            result['HPCInterConnect'] = self.hpcinter_connect
        if self.hostname_prefix is not None:
            result['HostnamePrefix'] = self.hostname_prefix
        if self.hostname_suffix is not None:
            result['HostnameSuffix'] = self.hostname_suffix
        if self.keep_alive is not None:
            result['KeepAlive'] = self.keep_alive
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.ram_role is not None:
            result['RamRole'] = self.ram_role
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ComputeNode') is not None:
            temp_model = NodeTemplate()
            self.compute_node = temp_model.from_map(m['ComputeNode'])
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('HPCInterConnect') is not None:
            self.hpcinter_connect = m.get('HPCInterConnect')
        if m.get('HostnamePrefix') is not None:
            self.hostname_prefix = m.get('HostnamePrefix')
        if m.get('HostnameSuffix') is not None:
            self.hostname_suffix = m.get('HostnameSuffix')
        if m.get('KeepAlive') is not None:
            self.keep_alive = m.get('KeepAlive')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('RamRole') is not None:
            self.ram_role = m.get('RamRole')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class CreateNodesShrinkRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        compute_node_shrink: str = None,
        count: int = None,
        hpcinter_connect: str = None,
        hostname_prefix: str = None,
        hostname_suffix: str = None,
        keep_alive: str = None,
        queue_name: str = None,
        ram_role: str = None,
        v_switch_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.compute_node_shrink = compute_node_shrink
        self.count = count
        self.hpcinter_connect = hpcinter_connect
        self.hostname_prefix = hostname_prefix
        self.hostname_suffix = hostname_suffix
        self.keep_alive = keep_alive
        self.queue_name = queue_name
        self.ram_role = ram_role
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.compute_node_shrink is not None:
            result['ComputeNode'] = self.compute_node_shrink
        if self.count is not None:
            result['Count'] = self.count
        if self.hpcinter_connect is not None:
            result['HPCInterConnect'] = self.hpcinter_connect
        if self.hostname_prefix is not None:
            result['HostnamePrefix'] = self.hostname_prefix
        if self.hostname_suffix is not None:
            result['HostnameSuffix'] = self.hostname_suffix
        if self.keep_alive is not None:
            result['KeepAlive'] = self.keep_alive
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.ram_role is not None:
            result['RamRole'] = self.ram_role
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ComputeNode') is not None:
            self.compute_node_shrink = m.get('ComputeNode')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('HPCInterConnect') is not None:
            self.hpcinter_connect = m.get('HPCInterConnect')
        if m.get('HostnamePrefix') is not None:
            self.hostname_prefix = m.get('HostnamePrefix')
        if m.get('HostnameSuffix') is not None:
            self.hostname_suffix = m.get('HostnameSuffix')
        if m.get('KeepAlive') is not None:
            self.keep_alive = m.get('KeepAlive')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('RamRole') is not None:
            self.ram_role = m.get('RamRole')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class CreateNodesResponseBody(TeaModel):
    def __init__(
        self,
        instance_ids: List[str] = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.instance_ids = instance_ids
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateNodesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateNodesResponseBody = None,
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
            temp_model = CreateNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateQueueRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        queue: QueueTemplate = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # The configurations of the queue to be created.
        self.queue = queue

    def validate(self):
        if self.queue:
            self.queue.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.queue is not None:
            result['Queue'] = self.queue.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Queue') is not None:
            temp_model = QueueTemplate()
            self.queue = temp_model.from_map(m['Queue'])
        return self


class CreateQueueShrinkRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        queue_shrink: str = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # The configurations of the queue to be created.
        self.queue_shrink = queue_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.queue_shrink is not None:
            result['Queue'] = self.queue_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Queue') is not None:
            self.queue_shrink = m.get('Queue')
        return self


class CreateQueueResponseBody(TeaModel):
    def __init__(
        self,
        name: str = None,
        request_id: str = None,
    ):
        # The name of the created queue.
        self.name = name
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateQueueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateQueueResponseBody = None,
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
            temp_model = CreateQueueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUsersRequestUser(TeaModel):
    def __init__(
        self,
        auth_key: str = None,
        group: str = None,
        password: str = None,
        user_name: str = None,
    ):
        self.auth_key = auth_key
        self.group = group
        self.password = password
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key
        if self.group is not None:
            result['Group'] = self.group
        if self.password is not None:
            result['Password'] = self.password
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class CreateUsersRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        user: List[CreateUsersRequestUser] = None,
    ):
        # This parameter is required.
        self.cluster_id = cluster_id
        self.user = user

    def validate(self):
        if self.user:
            for k in self.user:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        result['User'] = []
        if self.user is not None:
            for k in self.user:
                result['User'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        self.user = []
        if m.get('User') is not None:
            for k in m.get('User'):
                temp_model = CreateUsersRequestUser()
                self.user.append(temp_model.from_map(k))
        return self


class CreateUsersShrinkRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        user_shrink: str = None,
    ):
        # This parameter is required.
        self.cluster_id = cluster_id
        self.user_shrink = user_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.user_shrink is not None:
            result['User'] = self.user_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('User') is not None:
            self.user_shrink = m.get('User')
        return self


class CreateUsersResponseBody(TeaModel):
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


class CreateUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateUsersResponseBody = None,
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
            temp_model = CreateUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteClusterRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DeleteClusterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The request result. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success
        # The task ID.
        self.task_id = task_id

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
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DeleteClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteClusterResponseBody = None,
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
            temp_model = DeleteClusterResponseBody()
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


class DeleteNodesRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        instance_ids: List[str] = None,
    ):
        # The cluster ID. You can call the [listclusters](https://help.aliyun.com/document_detail/87116.html) operation to query the cluster ID.
        self.cluster_id = cluster_id
        # The instance IDs of the compute nodes that you want to delete.
        self.instance_ids = instance_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class DeleteNodesShrinkRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        instance_ids_shrink: str = None,
    ):
        # The cluster ID. You can call the [listclusters](https://help.aliyun.com/document_detail/87116.html) operation to query the cluster ID.
        self.cluster_id = cluster_id
        # The instance IDs of the compute nodes that you want to delete.
        self.instance_ids_shrink = instance_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.instance_ids_shrink is not None:
            result['InstanceIds'] = self.instance_ids_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('InstanceIds') is not None:
            self.instance_ids_shrink = m.get('InstanceIds')
        return self


class DeleteNodesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success
        # The task ID.
        self.task_id = task_id

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
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DeleteNodesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteNodesResponseBody = None,
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
            temp_model = DeleteNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteQueuesRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        queue_names: List[str] = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # The queues that you want to delete.
        self.queue_names = queue_names

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.queue_names is not None:
            result['QueueNames'] = self.queue_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('QueueNames') is not None:
            self.queue_names = m.get('QueueNames')
        return self


class DeleteQueuesShrinkRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        queue_names_shrink: str = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # The queues that you want to delete.
        self.queue_names_shrink = queue_names_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.queue_names_shrink is not None:
            result['QueueNames'] = self.queue_names_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('QueueNames') is not None:
            self.queue_names_shrink = m.get('QueueNames')
        return self


class DeleteQueuesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
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


class DeleteQueuesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteQueuesResponseBody = None,
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
            temp_model = DeleteQueuesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUsersRequestUser(TeaModel):
    def __init__(
        self,
        user_name: str = None,
    ):
        # The name of user N that you want to delete.
        # 
        # Valid values of N: 1 to 100.
        # 
        # This parameter is required.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DeleteUsersRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        user: List[DeleteUsersRequestUser] = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The users that you want to delete.
        # 
        # This parameter is required.
        self.user = user

    def validate(self):
        if self.user:
            for k in self.user:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        result['User'] = []
        if self.user is not None:
            for k in self.user:
                result['User'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        self.user = []
        if m.get('User') is not None:
            for k in m.get('User'):
                temp_model = DeleteUsersRequestUser()
                self.user.append(temp_model.from_map(k))
        return self


class DeleteUsersShrinkRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        user_shrink: str = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The users that you want to delete.
        # 
        # This parameter is required.
        self.user_shrink = user_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.user_shrink is not None:
            result['User'] = self.user_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('User') is not None:
            self.user_shrink = m.get('User')
        return self


class DeleteUsersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class DeleteUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteUsersResponseBody = None,
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
            temp_model = DeleteUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAddonTemplateRequest(TeaModel):
    def __init__(
        self,
        addon_name: str = None,
        addon_version: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        zone_id: str = None,
    ):
        # This parameter is required.
        self.addon_name = addon_name
        # This parameter is required.
        self.addon_version = addon_version
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.addon_name is not None:
            result['AddonName'] = self.addon_name
        if self.addon_version is not None:
            result['AddonVersion'] = self.addon_version
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddonName') is not None:
            self.addon_name = m.get('AddonName')
        if m.get('AddonVersion') is not None:
            self.addon_version = m.get('AddonVersion')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeAddonTemplateResponseBodyAddonResourcesSpecEipResource(TeaModel):
    def __init__(
        self,
        auto_create: bool = None,
        bandwidth: str = None,
        eip_instance_id: str = None,
        instance_charge_type: str = None,
        internet_charge_type: str = None,
    ):
        self.auto_create = auto_create
        self.bandwidth = bandwidth
        self.eip_instance_id = eip_instance_id
        self.instance_charge_type = instance_charge_type
        self.internet_charge_type = internet_charge_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_create is not None:
            result['AutoCreate'] = self.auto_create
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.eip_instance_id is not None:
            result['EipInstanceId'] = self.eip_instance_id
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoCreate') is not None:
            self.auto_create = m.get('AutoCreate')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('EipInstanceId') is not None:
            self.eip_instance_id = m.get('EipInstanceId')
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        return self


class DescribeAddonTemplateResponseBodyAddonResourcesSpec(TeaModel):
    def __init__(
        self,
        ecs_resources: List[AddonNodeTemplate] = None,
        eip_resource: DescribeAddonTemplateResponseBodyAddonResourcesSpecEipResource = None,
    ):
        self.ecs_resources = ecs_resources
        self.eip_resource = eip_resource

    def validate(self):
        if self.ecs_resources:
            for k in self.ecs_resources:
                if k:
                    k.validate()
        if self.eip_resource:
            self.eip_resource.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EcsResources'] = []
        if self.ecs_resources is not None:
            for k in self.ecs_resources:
                result['EcsResources'].append(k.to_map() if k else None)
        if self.eip_resource is not None:
            result['EipResource'] = self.eip_resource.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ecs_resources = []
        if m.get('EcsResources') is not None:
            for k in m.get('EcsResources'):
                temp_model = AddonNodeTemplate()
                self.ecs_resources.append(temp_model.from_map(k))
        if m.get('EipResource') is not None:
            temp_model = DescribeAddonTemplateResponseBodyAddonResourcesSpecEipResource()
            self.eip_resource = temp_model.from_map(m['EipResource'])
        return self


class DescribeAddonTemplateResponseBodyAddonServicesSpecInputParams(TeaModel):
    def __init__(
        self,
        help_text: str = None,
        label: str = None,
        name: str = None,
        type: str = None,
        value: str = None,
    ):
        self.help_text = help_text
        self.label = label
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.type = type
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.help_text is not None:
            result['HelpText'] = self.help_text
        if self.label is not None:
            result['Label'] = self.label
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HelpText') is not None:
            self.help_text = m.get('HelpText')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeAddonTemplateResponseBodyAddonServicesSpecNetworkACL(TeaModel):
    def __init__(
        self,
        ip_protocol: str = None,
        port: float = None,
        source_cidr_ip: str = None,
    ):
        # This parameter is required.
        self.ip_protocol = ip_protocol
        # This parameter is required.
        self.port = port
        # This parameter is required.
        self.source_cidr_ip = source_cidr_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol
        if self.port is not None:
            result['Port'] = self.port
        if self.source_cidr_ip is not None:
            result['SourceCidrIp'] = self.source_cidr_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('SourceCidrIp') is not None:
            self.source_cidr_ip = m.get('SourceCidrIp')
        return self


class DescribeAddonTemplateResponseBodyAddonServicesSpec(TeaModel):
    def __init__(
        self,
        input_params: List[DescribeAddonTemplateResponseBodyAddonServicesSpecInputParams] = None,
        network_acl: List[DescribeAddonTemplateResponseBodyAddonServicesSpecNetworkACL] = None,
        service_access_type: str = None,
        service_access_url: str = None,
        service_name: str = None,
    ):
        self.input_params = input_params
        self.network_acl = network_acl
        self.service_access_type = service_access_type
        self.service_access_url = service_access_url
        # This parameter is required.
        self.service_name = service_name

    def validate(self):
        if self.input_params:
            for k in self.input_params:
                if k:
                    k.validate()
        if self.network_acl:
            for k in self.network_acl:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InputParams'] = []
        if self.input_params is not None:
            for k in self.input_params:
                result['InputParams'].append(k.to_map() if k else None)
        result['NetworkACL'] = []
        if self.network_acl is not None:
            for k in self.network_acl:
                result['NetworkACL'].append(k.to_map() if k else None)
        if self.service_access_type is not None:
            result['ServiceAccessType'] = self.service_access_type
        if self.service_access_url is not None:
            result['ServiceAccessUrl'] = self.service_access_url
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.input_params = []
        if m.get('InputParams') is not None:
            for k in m.get('InputParams'):
                temp_model = DescribeAddonTemplateResponseBodyAddonServicesSpecInputParams()
                self.input_params.append(temp_model.from_map(k))
        self.network_acl = []
        if m.get('NetworkACL') is not None:
            for k in m.get('NetworkACL'):
                temp_model = DescribeAddonTemplateResponseBodyAddonServicesSpecNetworkACL()
                self.network_acl.append(temp_model.from_map(k))
        if m.get('ServiceAccessType') is not None:
            self.service_access_type = m.get('ServiceAccessType')
        if m.get('ServiceAccessUrl') is not None:
            self.service_access_url = m.get('ServiceAccessUrl')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class DescribeAddonTemplateResponseBodyAddon(TeaModel):
    def __init__(
        self,
        description: str = None,
        icon: str = None,
        label: str = None,
        last_update: str = None,
        name: str = None,
        resources_spec: DescribeAddonTemplateResponseBodyAddonResourcesSpec = None,
        services_spec: List[DescribeAddonTemplateResponseBodyAddonServicesSpec] = None,
        version: str = None,
    ):
        self.description = description
        self.icon = icon
        self.label = label
        self.last_update = last_update
        # This parameter is required.
        self.name = name
        self.resources_spec = resources_spec
        self.services_spec = services_spec
        # This parameter is required.
        self.version = version

    def validate(self):
        if self.resources_spec:
            self.resources_spec.validate()
        if self.services_spec:
            for k in self.services_spec:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.label is not None:
            result['Label'] = self.label
        if self.last_update is not None:
            result['LastUpdate'] = self.last_update
        if self.name is not None:
            result['Name'] = self.name
        if self.resources_spec is not None:
            result['ResourcesSpec'] = self.resources_spec.to_map()
        result['ServicesSpec'] = []
        if self.services_spec is not None:
            for k in self.services_spec:
                result['ServicesSpec'].append(k.to_map() if k else None)
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('LastUpdate') is not None:
            self.last_update = m.get('LastUpdate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ResourcesSpec') is not None:
            temp_model = DescribeAddonTemplateResponseBodyAddonResourcesSpec()
            self.resources_spec = temp_model.from_map(m['ResourcesSpec'])
        self.services_spec = []
        if m.get('ServicesSpec') is not None:
            for k in m.get('ServicesSpec'):
                temp_model = DescribeAddonTemplateResponseBodyAddonServicesSpec()
                self.services_spec.append(temp_model.from_map(k))
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeAddonTemplateResponseBody(TeaModel):
    def __init__(
        self,
        addon: DescribeAddonTemplateResponseBodyAddon = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.addon = addon
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.addon:
            self.addon.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.addon is not None:
            result['Addon'] = self.addon.to_map()
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
        if m.get('Addon') is not None:
            temp_model = DescribeAddonTemplateResponseBodyAddon()
            self.addon = temp_model.from_map(m['Addon'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAddonTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAddonTemplateResponseBody = None,
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
            temp_model = DescribeAddonTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachSharedStoragesRequestSharedStorages(TeaModel):
    def __init__(
        self,
        mount_directory: str = None,
    ):
        # The local mount directory of the mounted file system.
        # 
        # This parameter is required.
        self.mount_directory = mount_directory

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mount_directory is not None:
            result['MountDirectory'] = self.mount_directory
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MountDirectory') is not None:
            self.mount_directory = m.get('MountDirectory')
        return self


class DetachSharedStoragesRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        shared_storages: List[DetachSharedStoragesRequestSharedStorages] = None,
    ):
        # The cluster ID.
        # 
        # You can call the [ListClusters](https://help.aliyun.com/document_detail/87116.html) operation to query the cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The information about mounted shared storage resources.
        # 
        # This parameter is required.
        self.shared_storages = shared_storages

    def validate(self):
        if self.shared_storages:
            for k in self.shared_storages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        result['SharedStorages'] = []
        if self.shared_storages is not None:
            for k in self.shared_storages:
                result['SharedStorages'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        self.shared_storages = []
        if m.get('SharedStorages') is not None:
            for k in m.get('SharedStorages'):
                temp_model = DetachSharedStoragesRequestSharedStorages()
                self.shared_storages.append(temp_model.from_map(k))
        return self


class DetachSharedStoragesShrinkRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        shared_storages_shrink: str = None,
    ):
        # The cluster ID.
        # 
        # You can call the [ListClusters](https://help.aliyun.com/document_detail/87116.html) operation to query the cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The information about mounted shared storage resources.
        # 
        # This parameter is required.
        self.shared_storages_shrink = shared_storages_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.shared_storages_shrink is not None:
            result['SharedStorages'] = self.shared_storages_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('SharedStorages') is not None:
            self.shared_storages_shrink = m.get('SharedStorages')
        return self


class DetachSharedStoragesResponseBody(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The cluster ID.
        # 
        # You can call the [ListClusters](https://help.aliyun.com/document_detail/87116.html) operation to query the cluster ID.
        self.cluster_id = cluster_id
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DetachSharedStoragesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetachSharedStoragesResponseBody = None,
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
            temp_model = DetachSharedStoragesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAddonRequest(TeaModel):
    def __init__(
        self,
        addon_id: str = None,
        cluster_id: str = None,
    ):
        # This parameter is required.
        self.addon_id = addon_id
        # This parameter is required.
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.addon_id is not None:
            result['AddonId'] = self.addon_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddonId') is not None:
            self.addon_id = m.get('AddonId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class GetAddonResponseBodyAddonResourcesSpecEipResource(TeaModel):
    def __init__(
        self,
        auto_create: bool = None,
        bandwidth: str = None,
        eip_address: str = None,
        eip_instance_id: str = None,
        instance_charge_type: str = None,
        internet_charge_type: str = None,
    ):
        self.auto_create = auto_create
        self.bandwidth = bandwidth
        self.eip_address = eip_address
        self.eip_instance_id = eip_instance_id
        self.instance_charge_type = instance_charge_type
        self.internet_charge_type = internet_charge_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_create is not None:
            result['AutoCreate'] = self.auto_create
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.eip_address is not None:
            result['EipAddress'] = self.eip_address
        if self.eip_instance_id is not None:
            result['EipInstanceId'] = self.eip_instance_id
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoCreate') is not None:
            self.auto_create = m.get('AutoCreate')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('EipAddress') is not None:
            self.eip_address = m.get('EipAddress')
        if m.get('EipInstanceId') is not None:
            self.eip_instance_id = m.get('EipInstanceId')
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        return self


class GetAddonResponseBodyAddonResourcesSpec(TeaModel):
    def __init__(
        self,
        ecs_resources: List[AddonNodeTemplate] = None,
        eip_resource: GetAddonResponseBodyAddonResourcesSpecEipResource = None,
    ):
        self.ecs_resources = ecs_resources
        self.eip_resource = eip_resource

    def validate(self):
        if self.ecs_resources:
            for k in self.ecs_resources:
                if k:
                    k.validate()
        if self.eip_resource:
            self.eip_resource.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EcsResources'] = []
        if self.ecs_resources is not None:
            for k in self.ecs_resources:
                result['EcsResources'].append(k.to_map() if k else None)
        if self.eip_resource is not None:
            result['EipResource'] = self.eip_resource.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ecs_resources = []
        if m.get('EcsResources') is not None:
            for k in m.get('EcsResources'):
                temp_model = AddonNodeTemplate()
                self.ecs_resources.append(temp_model.from_map(k))
        if m.get('EipResource') is not None:
            temp_model = GetAddonResponseBodyAddonResourcesSpecEipResource()
            self.eip_resource = temp_model.from_map(m['EipResource'])
        return self


class GetAddonResponseBodyAddonServicesSpecInputParams(TeaModel):
    def __init__(
        self,
        help_text: str = None,
        label: str = None,
        name: str = None,
        type: str = None,
        value: str = None,
    ):
        self.help_text = help_text
        self.label = label
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.type = type
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.help_text is not None:
            result['HelpText'] = self.help_text
        if self.label is not None:
            result['Label'] = self.label
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HelpText') is not None:
            self.help_text = m.get('HelpText')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetAddonResponseBodyAddonServicesSpecNetworkACL(TeaModel):
    def __init__(
        self,
        ip_protocol: str = None,
        port: float = None,
        source_cidr_ip: str = None,
    ):
        # This parameter is required.
        self.ip_protocol = ip_protocol
        # This parameter is required.
        self.port = port
        # This parameter is required.
        self.source_cidr_ip = source_cidr_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol
        if self.port is not None:
            result['Port'] = self.port
        if self.source_cidr_ip is not None:
            result['SourceCidrIp'] = self.source_cidr_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('SourceCidrIp') is not None:
            self.source_cidr_ip = m.get('SourceCidrIp')
        return self


class GetAddonResponseBodyAddonServicesSpec(TeaModel):
    def __init__(
        self,
        input_params: List[GetAddonResponseBodyAddonServicesSpecInputParams] = None,
        network_acl: List[GetAddonResponseBodyAddonServicesSpecNetworkACL] = None,
        service_access_type: str = None,
        service_access_url: str = None,
        service_name: str = None,
    ):
        self.input_params = input_params
        self.network_acl = network_acl
        self.service_access_type = service_access_type
        self.service_access_url = service_access_url
        # This parameter is required.
        self.service_name = service_name

    def validate(self):
        if self.input_params:
            for k in self.input_params:
                if k:
                    k.validate()
        if self.network_acl:
            for k in self.network_acl:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InputParams'] = []
        if self.input_params is not None:
            for k in self.input_params:
                result['InputParams'].append(k.to_map() if k else None)
        result['NetworkACL'] = []
        if self.network_acl is not None:
            for k in self.network_acl:
                result['NetworkACL'].append(k.to_map() if k else None)
        if self.service_access_type is not None:
            result['ServiceAccessType'] = self.service_access_type
        if self.service_access_url is not None:
            result['ServiceAccessUrl'] = self.service_access_url
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.input_params = []
        if m.get('InputParams') is not None:
            for k in m.get('InputParams'):
                temp_model = GetAddonResponseBodyAddonServicesSpecInputParams()
                self.input_params.append(temp_model.from_map(k))
        self.network_acl = []
        if m.get('NetworkACL') is not None:
            for k in m.get('NetworkACL'):
                temp_model = GetAddonResponseBodyAddonServicesSpecNetworkACL()
                self.network_acl.append(temp_model.from_map(k))
        if m.get('ServiceAccessType') is not None:
            self.service_access_type = m.get('ServiceAccessType')
        if m.get('ServiceAccessUrl') is not None:
            self.service_access_url = m.get('ServiceAccessUrl')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class GetAddonResponseBodyAddon(TeaModel):
    def __init__(
        self,
        addon_id: str = None,
        description: str = None,
        icon: str = None,
        install_time: str = None,
        label: str = None,
        name: str = None,
        resources_spec: GetAddonResponseBodyAddonResourcesSpec = None,
        services_spec: List[GetAddonResponseBodyAddonServicesSpec] = None,
        status: str = None,
        version: str = None,
    ):
        # This parameter is required.
        self.addon_id = addon_id
        self.description = description
        self.icon = icon
        self.install_time = install_time
        self.label = label
        # This parameter is required.
        self.name = name
        self.resources_spec = resources_spec
        self.services_spec = services_spec
        self.status = status
        # This parameter is required.
        self.version = version

    def validate(self):
        if self.resources_spec:
            self.resources_spec.validate()
        if self.services_spec:
            for k in self.services_spec:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.addon_id is not None:
            result['AddonId'] = self.addon_id
        if self.description is not None:
            result['Description'] = self.description
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.install_time is not None:
            result['InstallTime'] = self.install_time
        if self.label is not None:
            result['Label'] = self.label
        if self.name is not None:
            result['Name'] = self.name
        if self.resources_spec is not None:
            result['ResourcesSpec'] = self.resources_spec.to_map()
        result['ServicesSpec'] = []
        if self.services_spec is not None:
            for k in self.services_spec:
                result['ServicesSpec'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddonId') is not None:
            self.addon_id = m.get('AddonId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('InstallTime') is not None:
            self.install_time = m.get('InstallTime')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ResourcesSpec') is not None:
            temp_model = GetAddonResponseBodyAddonResourcesSpec()
            self.resources_spec = temp_model.from_map(m['ResourcesSpec'])
        self.services_spec = []
        if m.get('ServicesSpec') is not None:
            for k in m.get('ServicesSpec'):
                temp_model = GetAddonResponseBodyAddonServicesSpec()
                self.services_spec.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetAddonResponseBody(TeaModel):
    def __init__(
        self,
        addon: GetAddonResponseBodyAddon = None,
        request_id: str = None,
    ):
        self.addon = addon
        self.request_id = request_id

    def validate(self):
        if self.addon:
            self.addon.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.addon is not None:
            result['Addon'] = self.addon.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Addon') is not None:
            temp_model = GetAddonResponseBodyAddon()
            self.addon = temp_model.from_map(m['Addon'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAddonResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAddonResponseBody = None,
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
            temp_model = GetAddonResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetClusterRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
    ):
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class GetClusterResponseBodyClusterCustomConfiguration(TeaModel):
    def __init__(
        self,
        args: str = None,
        script: str = None,
    ):
        self.args = args
        self.script = script

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetClusterResponseBodyManagerDNS(TeaModel):
    def __init__(
        self,
        status: str = None,
        type: str = None,
        version: str = None,
    ):
        self.status = status
        self.type = type
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetClusterResponseBodyManagerDirectoryService(TeaModel):
    def __init__(
        self,
        status: str = None,
        type: str = None,
        version: str = None,
    ):
        self.status = status
        self.type = type
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetClusterResponseBodyManagerManagerNode(TeaModel):
    def __init__(
        self,
        expired_time: str = None,
        instance_charge_type: str = None,
        instance_id: str = None,
        instance_type: str = None,
    ):
        self.expired_time = expired_time
        self.instance_charge_type = instance_charge_type
        self.instance_id = instance_id
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class GetClusterResponseBodyManagerScheduler(TeaModel):
    def __init__(
        self,
        status: str = None,
        type: str = None,
        version: str = None,
    ):
        self.status = status
        self.type = type
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetClusterResponseBodyManager(TeaModel):
    def __init__(
        self,
        dns: GetClusterResponseBodyManagerDNS = None,
        directory_service: GetClusterResponseBodyManagerDirectoryService = None,
        manager_node: GetClusterResponseBodyManagerManagerNode = None,
        scheduler: GetClusterResponseBodyManagerScheduler = None,
    ):
        self.dns = dns
        self.directory_service = directory_service
        self.manager_node = manager_node
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetClusterResponseBodyManagerDNS()
            self.dns = temp_model.from_map(m['DNS'])
        if m.get('DirectoryService') is not None:
            temp_model = GetClusterResponseBodyManagerDirectoryService()
            self.directory_service = temp_model.from_map(m['DirectoryService'])
        if m.get('ManagerNode') is not None:
            temp_model = GetClusterResponseBodyManagerManagerNode()
            self.manager_node = temp_model.from_map(m['ManagerNode'])
        if m.get('Scheduler') is not None:
            temp_model = GetClusterResponseBodyManagerScheduler()
            self.scheduler = temp_model.from_map(m['Scheduler'])
        return self


class GetClusterResponseBody(TeaModel):
    def __init__(
        self,
        client_version: str = None,
        cluster_category: str = None,
        cluster_create_time: str = None,
        cluster_custom_configuration: GetClusterResponseBodyClusterCustomConfiguration = None,
        cluster_id: str = None,
        cluster_mode: str = None,
        cluster_modify_time: str = None,
        cluster_name: str = None,
        cluster_status: str = None,
        cluster_vswitch_id: str = None,
        cluster_vpc_id: str = None,
        delete_protection: str = None,
        ehpc_version: str = None,
        enable_scale_in: bool = None,
        enable_scale_out: bool = None,
        grow_interval: int = None,
        idle_interval: int = None,
        manager: GetClusterResponseBodyManager = None,
        max_core_count: str = None,
        max_count: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        security_group_id: str = None,
    ):
        self.client_version = client_version
        self.cluster_category = cluster_category
        self.cluster_create_time = cluster_create_time
        self.cluster_custom_configuration = cluster_custom_configuration
        self.cluster_id = cluster_id
        self.cluster_mode = cluster_mode
        self.cluster_modify_time = cluster_modify_time
        self.cluster_name = cluster_name
        self.cluster_status = cluster_status
        self.cluster_vswitch_id = cluster_vswitch_id
        self.cluster_vpc_id = cluster_vpc_id
        self.delete_protection = delete_protection
        self.ehpc_version = ehpc_version
        self.enable_scale_in = enable_scale_in
        self.enable_scale_out = enable_scale_out
        self.grow_interval = grow_interval
        self.idle_interval = idle_interval
        self.manager = manager
        self.max_core_count = max_core_count
        self.max_count = max_count
        self.request_id = request_id
        self.resource_group_id = resource_group_id
        self.security_group_id = security_group_id

    def validate(self):
        if self.cluster_custom_configuration:
            self.cluster_custom_configuration.validate()
        if self.manager:
            self.manager.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.cluster_category is not None:
            result['ClusterCategory'] = self.cluster_category
        if self.cluster_create_time is not None:
            result['ClusterCreateTime'] = self.cluster_create_time
        if self.cluster_custom_configuration is not None:
            result['ClusterCustomConfiguration'] = self.cluster_custom_configuration.to_map()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_mode is not None:
            result['ClusterMode'] = self.cluster_mode
        if self.cluster_modify_time is not None:
            result['ClusterModifyTime'] = self.cluster_modify_time
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.cluster_status is not None:
            result['ClusterStatus'] = self.cluster_status
        if self.cluster_vswitch_id is not None:
            result['ClusterVSwitchId'] = self.cluster_vswitch_id
        if self.cluster_vpc_id is not None:
            result['ClusterVpcId'] = self.cluster_vpc_id
        if self.delete_protection is not None:
            result['DeleteProtection'] = self.delete_protection
        if self.ehpc_version is not None:
            result['EhpcVersion'] = self.ehpc_version
        if self.enable_scale_in is not None:
            result['EnableScaleIn'] = self.enable_scale_in
        if self.enable_scale_out is not None:
            result['EnableScaleOut'] = self.enable_scale_out
        if self.grow_interval is not None:
            result['GrowInterval'] = self.grow_interval
        if self.idle_interval is not None:
            result['IdleInterval'] = self.idle_interval
        if self.manager is not None:
            result['Manager'] = self.manager.to_map()
        if self.max_core_count is not None:
            result['MaxCoreCount'] = self.max_core_count
        if self.max_count is not None:
            result['MaxCount'] = self.max_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('ClusterCategory') is not None:
            self.cluster_category = m.get('ClusterCategory')
        if m.get('ClusterCreateTime') is not None:
            self.cluster_create_time = m.get('ClusterCreateTime')
        if m.get('ClusterCustomConfiguration') is not None:
            temp_model = GetClusterResponseBodyClusterCustomConfiguration()
            self.cluster_custom_configuration = temp_model.from_map(m['ClusterCustomConfiguration'])
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterMode') is not None:
            self.cluster_mode = m.get('ClusterMode')
        if m.get('ClusterModifyTime') is not None:
            self.cluster_modify_time = m.get('ClusterModifyTime')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('ClusterStatus') is not None:
            self.cluster_status = m.get('ClusterStatus')
        if m.get('ClusterVSwitchId') is not None:
            self.cluster_vswitch_id = m.get('ClusterVSwitchId')
        if m.get('ClusterVpcId') is not None:
            self.cluster_vpc_id = m.get('ClusterVpcId')
        if m.get('DeleteProtection') is not None:
            self.delete_protection = m.get('DeleteProtection')
        if m.get('EhpcVersion') is not None:
            self.ehpc_version = m.get('EhpcVersion')
        if m.get('EnableScaleIn') is not None:
            self.enable_scale_in = m.get('EnableScaleIn')
        if m.get('EnableScaleOut') is not None:
            self.enable_scale_out = m.get('EnableScaleOut')
        if m.get('GrowInterval') is not None:
            self.grow_interval = m.get('GrowInterval')
        if m.get('IdleInterval') is not None:
            self.idle_interval = m.get('IdleInterval')
        if m.get('Manager') is not None:
            temp_model = GetClusterResponseBodyManager()
            self.manager = temp_model.from_map(m['Manager'])
        if m.get('MaxCoreCount') is not None:
            self.max_core_count = m.get('MaxCoreCount')
        if m.get('MaxCount') is not None:
            self.max_count = m.get('MaxCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        return self


class GetClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetClusterResponseBody = None,
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
            temp_model = GetClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCommonLogDetailRequest(TeaModel):
    def __init__(
        self,
        from_: int = None,
        hidden_process: bool = None,
        log_request_id: str = None,
        to: int = None,
    ):
        # This parameter is required.
        self.from_ = from_
        self.hidden_process = hidden_process
        # This parameter is required.
        self.log_request_id = log_request_id
        # This parameter is required.
        self.to = to

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_ is not None:
            result['From'] = self.from_
        if self.hidden_process is not None:
            result['HiddenProcess'] = self.hidden_process
        if self.log_request_id is not None:
            result['LogRequestId'] = self.log_request_id
        if self.to is not None:
            result['To'] = self.to
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('HiddenProcess') is not None:
            self.hidden_process = m.get('HiddenProcess')
        if m.get('LogRequestId') is not None:
            self.log_request_id = m.get('LogRequestId')
        if m.get('To') is not None:
            self.to = m.get('To')
        return self


class GetCommonLogDetailResponseBodyLogDetailStages(TeaModel):
    def __init__(
        self,
        log_level: str = None,
        message: str = None,
        method: str = None,
        request_id: str = None,
        status: str = None,
        target: str = None,
        time: str = None,
    ):
        self.log_level = log_level
        self.message = message
        self.method = method
        self.request_id = request_id
        self.status = status
        self.target = target
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_level is not None:
            result['LogLevel'] = self.log_level
        if self.message is not None:
            result['Message'] = self.message
        if self.method is not None:
            result['Method'] = self.method
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.target is not None:
            result['Target'] = self.target
        if self.time is not None:
            result['Time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogLevel') is not None:
            self.log_level = m.get('LogLevel')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        return self


class GetCommonLogDetailResponseBodyLogDetail(TeaModel):
    def __init__(
        self,
        stage_name: str = None,
        stages: List[GetCommonLogDetailResponseBodyLogDetailStages] = None,
    ):
        self.stage_name = stage_name
        self.stages = stages

    def validate(self):
        if self.stages:
            for k in self.stages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        result['Stages'] = []
        if self.stages is not None:
            for k in self.stages:
                result['Stages'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        self.stages = []
        if m.get('Stages') is not None:
            for k in m.get('Stages'):
                temp_model = GetCommonLogDetailResponseBodyLogDetailStages()
                self.stages.append(temp_model.from_map(k))
        return self


class GetCommonLogDetailResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        cluster_id: str = None,
        log_detail: List[GetCommonLogDetailResponseBodyLogDetail] = None,
        log_type: str = None,
        operator_uid: str = None,
        request_id: str = None,
        uid: str = None,
    ):
        self.action = action
        self.cluster_id = cluster_id
        self.log_detail = log_detail
        self.log_type = log_type
        self.operator_uid = operator_uid
        self.request_id = request_id
        self.uid = uid

    def validate(self):
        if self.log_detail:
            for k in self.log_detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        result['LogDetail'] = []
        if self.log_detail is not None:
            for k in self.log_detail:
                result['LogDetail'].append(k.to_map() if k else None)
        if self.log_type is not None:
            result['LogType'] = self.log_type
        if self.operator_uid is not None:
            result['OperatorUid'] = self.operator_uid
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        self.log_detail = []
        if m.get('LogDetail') is not None:
            for k in m.get('LogDetail'):
                temp_model = GetCommonLogDetailResponseBodyLogDetail()
                self.log_detail.append(temp_model.from_map(k))
        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')
        if m.get('OperatorUid') is not None:
            self.operator_uid = m.get('OperatorUid')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class GetCommonLogDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCommonLogDetailResponseBody = None,
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
            temp_model = GetCommonLogDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQueueRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        queue_name: str = None,
    ):
        self.cluster_id = cluster_id
        self.queue_name = queue_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        return self


class GetQueueResponseBodyQueue(TeaModel):
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
        queue_name: str = None,
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
        # This parameter is required.
        self.queue_name = queue_name
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
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
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
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('RamRole') is not None:
            self.ram_role = m.get('RamRole')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        return self


class GetQueueResponseBody(TeaModel):
    def __init__(
        self,
        queue: GetQueueResponseBodyQueue = None,
        request_id: str = None,
    ):
        self.queue = queue
        self.request_id = request_id

    def validate(self):
        if self.queue:
            self.queue.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.queue is not None:
            result['Queue'] = self.queue.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Queue') is not None:
            temp_model = GetQueueResponseBodyQueue()
            self.queue = temp_model.from_map(m['Queue'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetQueueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetQueueResponseBody = None,
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
            temp_model = GetQueueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InstallAddonRequest(TeaModel):
    def __init__(
        self,
        addon_name: str = None,
        addon_version: str = None,
        cluster_id: str = None,
        resources_spec: str = None,
        services_spec: str = None,
    ):
        # The addon name.
        # 
        # This parameter is required.
        self.addon_name = addon_name
        # The addon version.
        # 
        # This parameter is required.
        self.addon_version = addon_version
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The resource configurations of the addon.
        # 
        # This parameter is required.
        self.resources_spec = resources_spec
        # The service configurations of the addon.
        # 
        # This parameter is required.
        self.services_spec = services_spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.addon_name is not None:
            result['AddonName'] = self.addon_name
        if self.addon_version is not None:
            result['AddonVersion'] = self.addon_version
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.resources_spec is not None:
            result['ResourcesSpec'] = self.resources_spec
        if self.services_spec is not None:
            result['ServicesSpec'] = self.services_spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddonName') is not None:
            self.addon_name = m.get('AddonName')
        if m.get('AddonVersion') is not None:
            self.addon_version = m.get('AddonVersion')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ResourcesSpec') is not None:
            self.resources_spec = m.get('ResourcesSpec')
        if m.get('ServicesSpec') is not None:
            self.services_spec = m.get('ServicesSpec')
        return self


class InstallAddonResponseBody(TeaModel):
    def __init__(
        self,
        addon_id: str = None,
        cluster_id: str = None,
        request_id: str = None,
    ):
        # The addon ID.
        # 
        # This parameter is required.
        self.addon_id = addon_id
        # The cluster ID.
        self.cluster_id = cluster_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.addon_id is not None:
            result['AddonId'] = self.addon_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddonId') is not None:
            self.addon_id = m.get('AddonId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class InstallAddonResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InstallAddonResponseBody = None,
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
            temp_model = InstallAddonResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InstallSoftwaresRequestAdditionalPackages(TeaModel):
    def __init__(
        self,
        name: str = None,
        version: str = None,
    ):
        # The software name.
        self.name = name
        # The software version.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class InstallSoftwaresRequest(TeaModel):
    def __init__(
        self,
        additional_packages: List[InstallSoftwaresRequestAdditionalPackages] = None,
        cluster_id: str = None,
    ):
        # The information about the software systems that you want to install.
        self.additional_packages = additional_packages
        # The cluster ID.
        self.cluster_id = cluster_id

    def validate(self):
        if self.additional_packages:
            for k in self.additional_packages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AdditionalPackages'] = []
        if self.additional_packages is not None:
            for k in self.additional_packages:
                result['AdditionalPackages'].append(k.to_map() if k else None)
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.additional_packages = []
        if m.get('AdditionalPackages') is not None:
            for k in m.get('AdditionalPackages'):
                temp_model = InstallSoftwaresRequestAdditionalPackages()
                self.additional_packages.append(temp_model.from_map(k))
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class InstallSoftwaresShrinkRequest(TeaModel):
    def __init__(
        self,
        additional_packages_shrink: str = None,
        cluster_id: str = None,
    ):
        # The information about the software systems that you want to install.
        self.additional_packages_shrink = additional_packages_shrink
        # The cluster ID.
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.additional_packages_shrink is not None:
            result['AdditionalPackages'] = self.additional_packages_shrink
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdditionalPackages') is not None:
            self.additional_packages_shrink = m.get('AdditionalPackages')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class InstallSoftwaresResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class InstallSoftwaresResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InstallSoftwaresResponseBody = None,
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
            temp_model = InstallSoftwaresResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAddonTemplatesRequest(TeaModel):
    def __init__(
        self,
        addon_names: List[str] = None,
        cluster_category: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
    ):
        self.addon_names = addon_names
        self.cluster_category = cluster_category
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.addon_names is not None:
            result['AddonNames'] = self.addon_names
        if self.cluster_category is not None:
            result['ClusterCategory'] = self.cluster_category
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddonNames') is not None:
            self.addon_names = m.get('AddonNames')
        if m.get('ClusterCategory') is not None:
            self.cluster_category = m.get('ClusterCategory')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListAddonTemplatesResponseBodyAddons(TeaModel):
    def __init__(
        self,
        description: str = None,
        label: str = None,
        name: str = None,
        version: str = None,
    ):
        self.description = description
        self.label = label
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.label is not None:
            result['Label'] = self.label
        if self.name is not None:
            result['Name'] = self.name
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListAddonTemplatesResponseBody(TeaModel):
    def __init__(
        self,
        addons: List[ListAddonTemplatesResponseBodyAddons] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.addons = addons
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.addons:
            for k in self.addons:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Addons'] = []
        if self.addons is not None:
            for k in self.addons:
                result['Addons'].append(k.to_map() if k else None)
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
        self.addons = []
        if m.get('Addons') is not None:
            for k in m.get('Addons'):
                temp_model = ListAddonTemplatesResponseBodyAddons()
                self.addons.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAddonTemplatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAddonTemplatesResponseBody = None,
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
            temp_model = ListAddonTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAddonsRequest(TeaModel):
    def __init__(
        self,
        addon_ids: List[str] = None,
        cluster_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.addon_ids = addon_ids
        # This parameter is required.
        self.cluster_id = cluster_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.addon_ids is not None:
            result['AddonIds'] = self.addon_ids
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddonIds') is not None:
            self.addon_ids = m.get('AddonIds')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListAddonsShrinkRequest(TeaModel):
    def __init__(
        self,
        addon_ids_shrink: str = None,
        cluster_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.addon_ids_shrink = addon_ids_shrink
        # This parameter is required.
        self.cluster_id = cluster_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.addon_ids_shrink is not None:
            result['AddonIds'] = self.addon_ids_shrink
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddonIds') is not None:
            self.addon_ids_shrink = m.get('AddonIds')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListAddonsResponseBodyAddons(TeaModel):
    def __init__(
        self,
        addon_id: str = None,
        description: str = None,
        install_time: str = None,
        label: str = None,
        name: str = None,
        status: str = None,
        version: str = None,
    ):
        # This parameter is required.
        self.addon_id = addon_id
        self.description = description
        self.install_time = install_time
        self.label = label
        # This parameter is required.
        self.name = name
        self.status = status
        # This parameter is required.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.addon_id is not None:
            result['AddonId'] = self.addon_id
        if self.description is not None:
            result['Description'] = self.description
        if self.install_time is not None:
            result['InstallTime'] = self.install_time
        if self.label is not None:
            result['Label'] = self.label
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddonId') is not None:
            self.addon_id = m.get('AddonId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstallTime') is not None:
            self.install_time = m.get('InstallTime')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListAddonsResponseBody(TeaModel):
    def __init__(
        self,
        addons: List[ListAddonsResponseBodyAddons] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.addons = addons
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.addons:
            for k in self.addons:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Addons'] = []
        if self.addons is not None:
            for k in self.addons:
                result['Addons'].append(k.to_map() if k else None)
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
        self.addons = []
        if m.get('Addons') is not None:
            for k in m.get('Addons'):
                temp_model = ListAddonsResponseBodyAddons()
                self.addons.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAddonsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAddonsResponseBody = None,
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
            temp_model = ListAddonsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAvailableFileSystemsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListAvailableFileSystemsResponseBodyFileSystemListMountTargetList(TeaModel):
    def __init__(
        self,
        mount_target_domain: str = None,
        network_type: str = None,
        status: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        self.mount_target_domain = mount_target_domain
        self.network_type = network_type
        self.status = status
        self.v_switch_id = v_switch_id
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mount_target_domain is not None:
            result['MountTargetDomain'] = self.mount_target_domain
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.status is not None:
            result['Status'] = self.status
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MountTargetDomain') is not None:
            self.mount_target_domain = m.get('MountTargetDomain')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ListAvailableFileSystemsResponseBodyFileSystemList(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        file_system_id: str = None,
        file_system_type: str = None,
        mount_target_list: List[ListAvailableFileSystemsResponseBodyFileSystemListMountTargetList] = None,
        protocol_type: str = None,
        status: str = None,
        storage_type: str = None,
        vpc_id: str = None,
    ):
        self.create_time = create_time
        self.file_system_id = file_system_id
        self.file_system_type = file_system_type
        self.mount_target_list = mount_target_list
        self.protocol_type = protocol_type
        self.status = status
        self.storage_type = storage_type
        self.vpc_id = vpc_id

    def validate(self):
        if self.mount_target_list:
            for k in self.mount_target_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        result['MountTargetList'] = []
        if self.mount_target_list is not None:
            for k in self.mount_target_list:
                result['MountTargetList'].append(k.to_map() if k else None)
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.status is not None:
            result['Status'] = self.status
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        self.mount_target_list = []
        if m.get('MountTargetList') is not None:
            for k in m.get('MountTargetList'):
                temp_model = ListAvailableFileSystemsResponseBodyFileSystemListMountTargetList()
                self.mount_target_list.append(temp_model.from_map(k))
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ListAvailableFileSystemsResponseBody(TeaModel):
    def __init__(
        self,
        file_system_list: List[ListAvailableFileSystemsResponseBodyFileSystemList] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.file_system_list = file_system_list
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.file_system_list:
            for k in self.file_system_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FileSystemList'] = []
        if self.file_system_list is not None:
            for k in self.file_system_list:
                result['FileSystemList'].append(k.to_map() if k else None)
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
        self.file_system_list = []
        if m.get('FileSystemList') is not None:
            for k in m.get('FileSystemList'):
                temp_model = ListAvailableFileSystemsResponseBodyFileSystemList()
                self.file_system_list.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAvailableFileSystemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAvailableFileSystemsResponseBody = None,
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
            temp_model = ListAvailableFileSystemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAvailableImagesRequestDirectoryService(TeaModel):
    def __init__(
        self,
        type: str = None,
        version: str = None,
    ):
        self.type = type
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListAvailableImagesRequestScheduler(TeaModel):
    def __init__(
        self,
        type: str = None,
        version: str = None,
    ):
        self.type = type
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListAvailableImagesRequest(TeaModel):
    def __init__(
        self,
        directory_service: ListAvailableImagesRequestDirectoryService = None,
        enable_ht: bool = None,
        hpcinter_connect: str = None,
        image_owner_alias: str = None,
        instance_type: str = None,
        is_public: bool = None,
        page_number: int = None,
        page_size: int = None,
        scheduler: ListAvailableImagesRequestScheduler = None,
    ):
        self.directory_service = directory_service
        self.enable_ht = enable_ht
        self.hpcinter_connect = hpcinter_connect
        self.image_owner_alias = image_owner_alias
        self.instance_type = instance_type
        self.is_public = is_public
        self.page_number = page_number
        self.page_size = page_size
        self.scheduler = scheduler

    def validate(self):
        if self.directory_service:
            self.directory_service.validate()
        if self.scheduler:
            self.scheduler.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_service is not None:
            result['DirectoryService'] = self.directory_service.to_map()
        if self.enable_ht is not None:
            result['EnableHT'] = self.enable_ht
        if self.hpcinter_connect is not None:
            result['HPCInterConnect'] = self.hpcinter_connect
        if self.image_owner_alias is not None:
            result['ImageOwnerAlias'] = self.image_owner_alias
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.is_public is not None:
            result['IsPublic'] = self.is_public
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryService') is not None:
            temp_model = ListAvailableImagesRequestDirectoryService()
            self.directory_service = temp_model.from_map(m['DirectoryService'])
        if m.get('EnableHT') is not None:
            self.enable_ht = m.get('EnableHT')
        if m.get('HPCInterConnect') is not None:
            self.hpcinter_connect = m.get('HPCInterConnect')
        if m.get('ImageOwnerAlias') is not None:
            self.image_owner_alias = m.get('ImageOwnerAlias')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('IsPublic') is not None:
            self.is_public = m.get('IsPublic')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Scheduler') is not None:
            temp_model = ListAvailableImagesRequestScheduler()
            self.scheduler = temp_model.from_map(m['Scheduler'])
        return self


class ListAvailableImagesShrinkRequest(TeaModel):
    def __init__(
        self,
        directory_service_shrink: str = None,
        enable_ht: bool = None,
        hpcinter_connect: str = None,
        image_owner_alias: str = None,
        instance_type: str = None,
        is_public: bool = None,
        page_number: int = None,
        page_size: int = None,
        scheduler_shrink: str = None,
    ):
        self.directory_service_shrink = directory_service_shrink
        self.enable_ht = enable_ht
        self.hpcinter_connect = hpcinter_connect
        self.image_owner_alias = image_owner_alias
        self.instance_type = instance_type
        self.is_public = is_public
        self.page_number = page_number
        self.page_size = page_size
        self.scheduler_shrink = scheduler_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_service_shrink is not None:
            result['DirectoryService'] = self.directory_service_shrink
        if self.enable_ht is not None:
            result['EnableHT'] = self.enable_ht
        if self.hpcinter_connect is not None:
            result['HPCInterConnect'] = self.hpcinter_connect
        if self.image_owner_alias is not None:
            result['ImageOwnerAlias'] = self.image_owner_alias
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.is_public is not None:
            result['IsPublic'] = self.is_public
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.scheduler_shrink is not None:
            result['Scheduler'] = self.scheduler_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryService') is not None:
            self.directory_service_shrink = m.get('DirectoryService')
        if m.get('EnableHT') is not None:
            self.enable_ht = m.get('EnableHT')
        if m.get('HPCInterConnect') is not None:
            self.hpcinter_connect = m.get('HPCInterConnect')
        if m.get('ImageOwnerAlias') is not None:
            self.image_owner_alias = m.get('ImageOwnerAlias')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('IsPublic') is not None:
            self.is_public = m.get('IsPublic')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Scheduler') is not None:
            self.scheduler_shrink = m.get('Scheduler')
        return self


class ListAvailableImagesResponseBodyImages(TeaModel):
    def __init__(
        self,
        architecture: str = None,
        boot_mode: str = None,
        description: str = None,
        image_id: str = None,
        image_name: str = None,
        image_owner_alias: str = None,
        osname: str = None,
        osname_en: str = None,
        platform: str = None,
        size: str = None,
    ):
        self.architecture = architecture
        self.boot_mode = boot_mode
        self.description = description
        self.image_id = image_id
        self.image_name = image_name
        self.image_owner_alias = image_owner_alias
        self.osname = osname
        self.osname_en = osname_en
        self.platform = platform
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture is not None:
            result['Architecture'] = self.architecture
        if self.boot_mode is not None:
            result['BootMode'] = self.boot_mode
        if self.description is not None:
            result['Description'] = self.description
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.image_owner_alias is not None:
            result['ImageOwnerAlias'] = self.image_owner_alias
        if self.osname is not None:
            result['OSName'] = self.osname
        if self.osname_en is not None:
            result['OSNameEn'] = self.osname_en
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Architecture') is not None:
            self.architecture = m.get('Architecture')
        if m.get('BootMode') is not None:
            self.boot_mode = m.get('BootMode')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('ImageOwnerAlias') is not None:
            self.image_owner_alias = m.get('ImageOwnerAlias')
        if m.get('OSName') is not None:
            self.osname = m.get('OSName')
        if m.get('OSNameEn') is not None:
            self.osname_en = m.get('OSNameEn')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class ListAvailableImagesResponseBody(TeaModel):
    def __init__(
        self,
        images: List[ListAvailableImagesResponseBodyImages] = None,
        page_number: str = None,
        page_size: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: str = None,
    ):
        self.images = images
        # Id of the request
        self.page_number = page_number
        # Id of the request
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        # Id of the request
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
                temp_model = ListAvailableImagesResponseBodyImages()
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


class ListAvailableImagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAvailableImagesResponseBody = None,
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
            temp_model = ListAvailableImagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClustersRequest(TeaModel):
    def __init__(
        self,
        cluster_ids: List[str] = None,
        cluster_names: List[str] = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.cluster_ids = cluster_ids
        self.cluster_names = cluster_names
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_ids is not None:
            result['ClusterIds'] = self.cluster_ids
        if self.cluster_names is not None:
            result['ClusterNames'] = self.cluster_names
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterIds') is not None:
            self.cluster_ids = m.get('ClusterIds')
        if m.get('ClusterNames') is not None:
            self.cluster_names = m.get('ClusterNames')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListClustersShrinkRequest(TeaModel):
    def __init__(
        self,
        cluster_ids_shrink: str = None,
        cluster_names_shrink: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.cluster_ids_shrink = cluster_ids_shrink
        self.cluster_names_shrink = cluster_names_shrink
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_ids_shrink is not None:
            result['ClusterIds'] = self.cluster_ids_shrink
        if self.cluster_names_shrink is not None:
            result['ClusterNames'] = self.cluster_names_shrink
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterIds') is not None:
            self.cluster_ids_shrink = m.get('ClusterIds')
        if m.get('ClusterNames') is not None:
            self.cluster_names_shrink = m.get('ClusterNames')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListClustersResponseBodyClustersAdditionalPackages(TeaModel):
    def __init__(
        self,
        name: str = None,
        version: str = None,
    ):
        self.name = name
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListClustersResponseBodyClustersAddonsResourcesSpec(TeaModel):
    def __init__(
        self,
        ecs_instance_id: str = None,
        eip_instance_id: str = None,
    ):
        self.ecs_instance_id = ecs_instance_id
        self.eip_instance_id = eip_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ecs_instance_id is not None:
            result['EcsInstanceId'] = self.ecs_instance_id
        if self.eip_instance_id is not None:
            result['EipInstanceId'] = self.eip_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EcsInstanceId') is not None:
            self.ecs_instance_id = m.get('EcsInstanceId')
        if m.get('EipInstanceId') is not None:
            self.eip_instance_id = m.get('EipInstanceId')
        return self


class ListClustersResponseBodyClustersAddonsServicesSpec(TeaModel):
    def __init__(
        self,
        service_access_type: str = None,
        service_access_url: str = None,
        service_name: str = None,
    ):
        self.service_access_type = service_access_type
        self.service_access_url = service_access_url
        # This parameter is required.
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_access_type is not None:
            result['ServiceAccessType'] = self.service_access_type
        if self.service_access_url is not None:
            result['ServiceAccessUrl'] = self.service_access_url
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceAccessType') is not None:
            self.service_access_type = m.get('ServiceAccessType')
        if m.get('ServiceAccessUrl') is not None:
            self.service_access_url = m.get('ServiceAccessUrl')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class ListClustersResponseBodyClustersAddons(TeaModel):
    def __init__(
        self,
        addon_id: str = None,
        description: str = None,
        label: str = None,
        name: str = None,
        resources_spec: ListClustersResponseBodyClustersAddonsResourcesSpec = None,
        services_spec: List[ListClustersResponseBodyClustersAddonsServicesSpec] = None,
        status: str = None,
        version: str = None,
    ):
        self.addon_id = addon_id
        self.description = description
        self.label = label
        # This parameter is required.
        self.name = name
        self.resources_spec = resources_spec
        self.services_spec = services_spec
        self.status = status
        # This parameter is required.
        self.version = version

    def validate(self):
        if self.resources_spec:
            self.resources_spec.validate()
        if self.services_spec:
            for k in self.services_spec:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.addon_id is not None:
            result['AddonId'] = self.addon_id
        if self.description is not None:
            result['Description'] = self.description
        if self.label is not None:
            result['Label'] = self.label
        if self.name is not None:
            result['Name'] = self.name
        if self.resources_spec is not None:
            result['ResourcesSpec'] = self.resources_spec.to_map()
        result['ServicesSpec'] = []
        if self.services_spec is not None:
            for k in self.services_spec:
                result['ServicesSpec'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddonId') is not None:
            self.addon_id = m.get('AddonId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ResourcesSpec') is not None:
            temp_model = ListClustersResponseBodyClustersAddonsResourcesSpec()
            self.resources_spec = temp_model.from_map(m['ResourcesSpec'])
        self.services_spec = []
        if m.get('ServicesSpec') is not None:
            for k in m.get('ServicesSpec'):
                temp_model = ListClustersResponseBodyClustersAddonsServicesSpec()
                self.services_spec.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListClustersResponseBodyClustersClusterCustomConfiguration(TeaModel):
    def __init__(
        self,
        args: str = None,
        script: str = None,
    ):
        self.args = args
        self.script = script

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListClustersResponseBodyClustersManagerDNS(TeaModel):
    def __init__(
        self,
        type: str = None,
        version: str = None,
    ):
        self.type = type
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListClustersResponseBodyClustersManagerDirectoryService(TeaModel):
    def __init__(
        self,
        type: str = None,
        version: str = None,
    ):
        self.type = type
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListClustersResponseBodyClustersManagerScheduler(TeaModel):
    def __init__(
        self,
        type: str = None,
        version: str = None,
    ):
        self.type = type
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListClustersResponseBodyClustersManager(TeaModel):
    def __init__(
        self,
        dns: ListClustersResponseBodyClustersManagerDNS = None,
        directory_service: ListClustersResponseBodyClustersManagerDirectoryService = None,
        scheduler: ListClustersResponseBodyClustersManagerScheduler = None,
    ):
        self.dns = dns
        self.directory_service = directory_service
        self.scheduler = scheduler

    def validate(self):
        if self.dns:
            self.dns.validate()
        if self.directory_service:
            self.directory_service.validate()
        if self.scheduler:
            self.scheduler.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dns is not None:
            result['DNS'] = self.dns.to_map()
        if self.directory_service is not None:
            result['DirectoryService'] = self.directory_service.to_map()
        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DNS') is not None:
            temp_model = ListClustersResponseBodyClustersManagerDNS()
            self.dns = temp_model.from_map(m['DNS'])
        if m.get('DirectoryService') is not None:
            temp_model = ListClustersResponseBodyClustersManagerDirectoryService()
            self.directory_service = temp_model.from_map(m['DirectoryService'])
        if m.get('Scheduler') is not None:
            temp_model = ListClustersResponseBodyClustersManagerScheduler()
            self.scheduler = temp_model.from_map(m['Scheduler'])
        return self


class ListClustersResponseBodyClustersNodes(TeaModel):
    def __init__(
        self,
        abnormal_counts: int = None,
        creating_counts: int = None,
        running_counts: int = None,
    ):
        self.abnormal_counts = abnormal_counts
        self.creating_counts = creating_counts
        self.running_counts = running_counts

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.abnormal_counts is not None:
            result['AbnormalCounts'] = self.abnormal_counts
        if self.creating_counts is not None:
            result['CreatingCounts'] = self.creating_counts
        if self.running_counts is not None:
            result['RunningCounts'] = self.running_counts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AbnormalCounts') is not None:
            self.abnormal_counts = m.get('AbnormalCounts')
        if m.get('CreatingCounts') is not None:
            self.creating_counts = m.get('CreatingCounts')
        if m.get('RunningCounts') is not None:
            self.running_counts = m.get('RunningCounts')
        return self


class ListClustersResponseBodyClustersUsers(TeaModel):
    def __init__(
        self,
        normal_counts: int = None,
        sudo_counts: int = None,
    ):
        self.normal_counts = normal_counts
        self.sudo_counts = sudo_counts

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.normal_counts is not None:
            result['NormalCounts'] = self.normal_counts
        if self.sudo_counts is not None:
            result['SudoCounts'] = self.sudo_counts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NormalCounts') is not None:
            self.normal_counts = m.get('NormalCounts')
        if m.get('SudoCounts') is not None:
            self.sudo_counts = m.get('SudoCounts')
        return self


class ListClustersResponseBodyClusters(TeaModel):
    def __init__(
        self,
        additional_packages: List[ListClustersResponseBodyClustersAdditionalPackages] = None,
        addons: List[ListClustersResponseBodyClustersAddons] = None,
        cluster_category: str = None,
        cluster_create_time: str = None,
        cluster_credentials: List[str] = None,
        cluster_custom_configuration: ListClustersResponseBodyClustersClusterCustomConfiguration = None,
        cluster_description: str = None,
        cluster_id: str = None,
        cluster_mode: str = None,
        cluster_modify_time: str = None,
        cluster_name: str = None,
        cluster_status: str = None,
        cluster_used_core_time: float = None,
        cluster_vswitch_id: str = None,
        cluster_vpc_id: str = None,
        deletion_protection: bool = None,
        ehpc_version: str = None,
        manager: ListClustersResponseBodyClustersManager = None,
        max_core_count: int = None,
        max_count: int = None,
        nodes: ListClustersResponseBodyClustersNodes = None,
        resource_group_id: str = None,
        security_group_id: str = None,
        users: ListClustersResponseBodyClustersUsers = None,
    ):
        self.additional_packages = additional_packages
        self.addons = addons
        self.cluster_category = cluster_category
        self.cluster_create_time = cluster_create_time
        self.cluster_credentials = cluster_credentials
        self.cluster_custom_configuration = cluster_custom_configuration
        self.cluster_description = cluster_description
        self.cluster_id = cluster_id
        self.cluster_mode = cluster_mode
        self.cluster_modify_time = cluster_modify_time
        self.cluster_name = cluster_name
        self.cluster_status = cluster_status
        self.cluster_used_core_time = cluster_used_core_time
        self.cluster_vswitch_id = cluster_vswitch_id
        self.cluster_vpc_id = cluster_vpc_id
        self.deletion_protection = deletion_protection
        self.ehpc_version = ehpc_version
        self.manager = manager
        self.max_core_count = max_core_count
        self.max_count = max_count
        self.nodes = nodes
        self.resource_group_id = resource_group_id
        self.security_group_id = security_group_id
        self.users = users

    def validate(self):
        if self.additional_packages:
            for k in self.additional_packages:
                if k:
                    k.validate()
        if self.addons:
            for k in self.addons:
                if k:
                    k.validate()
        if self.cluster_custom_configuration:
            self.cluster_custom_configuration.validate()
        if self.manager:
            self.manager.validate()
        if self.nodes:
            self.nodes.validate()
        if self.users:
            self.users.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AdditionalPackages'] = []
        if self.additional_packages is not None:
            for k in self.additional_packages:
                result['AdditionalPackages'].append(k.to_map() if k else None)
        result['Addons'] = []
        if self.addons is not None:
            for k in self.addons:
                result['Addons'].append(k.to_map() if k else None)
        if self.cluster_category is not None:
            result['ClusterCategory'] = self.cluster_category
        if self.cluster_create_time is not None:
            result['ClusterCreateTime'] = self.cluster_create_time
        if self.cluster_credentials is not None:
            result['ClusterCredentials'] = self.cluster_credentials
        if self.cluster_custom_configuration is not None:
            result['ClusterCustomConfiguration'] = self.cluster_custom_configuration.to_map()
        if self.cluster_description is not None:
            result['ClusterDescription'] = self.cluster_description
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_mode is not None:
            result['ClusterMode'] = self.cluster_mode
        if self.cluster_modify_time is not None:
            result['ClusterModifyTime'] = self.cluster_modify_time
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.cluster_status is not None:
            result['ClusterStatus'] = self.cluster_status
        if self.cluster_used_core_time is not None:
            result['ClusterUsedCoreTime'] = self.cluster_used_core_time
        if self.cluster_vswitch_id is not None:
            result['ClusterVSwitchId'] = self.cluster_vswitch_id
        if self.cluster_vpc_id is not None:
            result['ClusterVpcId'] = self.cluster_vpc_id
        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection
        if self.ehpc_version is not None:
            result['EhpcVersion'] = self.ehpc_version
        if self.manager is not None:
            result['Manager'] = self.manager.to_map()
        if self.max_core_count is not None:
            result['MaxCoreCount'] = self.max_core_count
        if self.max_count is not None:
            result['MaxCount'] = self.max_count
        if self.nodes is not None:
            result['Nodes'] = self.nodes.to_map()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.users is not None:
            result['Users'] = self.users.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.additional_packages = []
        if m.get('AdditionalPackages') is not None:
            for k in m.get('AdditionalPackages'):
                temp_model = ListClustersResponseBodyClustersAdditionalPackages()
                self.additional_packages.append(temp_model.from_map(k))
        self.addons = []
        if m.get('Addons') is not None:
            for k in m.get('Addons'):
                temp_model = ListClustersResponseBodyClustersAddons()
                self.addons.append(temp_model.from_map(k))
        if m.get('ClusterCategory') is not None:
            self.cluster_category = m.get('ClusterCategory')
        if m.get('ClusterCreateTime') is not None:
            self.cluster_create_time = m.get('ClusterCreateTime')
        if m.get('ClusterCredentials') is not None:
            self.cluster_credentials = m.get('ClusterCredentials')
        if m.get('ClusterCustomConfiguration') is not None:
            temp_model = ListClustersResponseBodyClustersClusterCustomConfiguration()
            self.cluster_custom_configuration = temp_model.from_map(m['ClusterCustomConfiguration'])
        if m.get('ClusterDescription') is not None:
            self.cluster_description = m.get('ClusterDescription')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterMode') is not None:
            self.cluster_mode = m.get('ClusterMode')
        if m.get('ClusterModifyTime') is not None:
            self.cluster_modify_time = m.get('ClusterModifyTime')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('ClusterStatus') is not None:
            self.cluster_status = m.get('ClusterStatus')
        if m.get('ClusterUsedCoreTime') is not None:
            self.cluster_used_core_time = m.get('ClusterUsedCoreTime')
        if m.get('ClusterVSwitchId') is not None:
            self.cluster_vswitch_id = m.get('ClusterVSwitchId')
        if m.get('ClusterVpcId') is not None:
            self.cluster_vpc_id = m.get('ClusterVpcId')
        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')
        if m.get('EhpcVersion') is not None:
            self.ehpc_version = m.get('EhpcVersion')
        if m.get('Manager') is not None:
            temp_model = ListClustersResponseBodyClustersManager()
            self.manager = temp_model.from_map(m['Manager'])
        if m.get('MaxCoreCount') is not None:
            self.max_core_count = m.get('MaxCoreCount')
        if m.get('MaxCount') is not None:
            self.max_count = m.get('MaxCount')
        if m.get('Nodes') is not None:
            temp_model = ListClustersResponseBodyClustersNodes()
            self.nodes = temp_model.from_map(m['Nodes'])
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('Users') is not None:
            temp_model = ListClustersResponseBodyClustersUsers()
            self.users = temp_model.from_map(m['Users'])
        return self


class ListClustersResponseBody(TeaModel):
    def __init__(
        self,
        clusters: List[ListClustersResponseBodyClusters] = None,
        page_number: str = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.clusters = clusters
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.clusters:
            for k in self.clusters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Clusters'] = []
        if self.clusters is not None:
            for k in self.clusters:
                result['Clusters'].append(k.to_map() if k else None)
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
        self.clusters = []
        if m.get('Clusters') is not None:
            for k in m.get('Clusters'):
                temp_model = ListClustersResponseBodyClusters()
                self.clusters.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListClustersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListClustersResponseBody = None,
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
            temp_model = ListClustersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCommonLogsRequest(TeaModel):
    def __init__(
        self,
        action_name: List[str] = None,
        action_status: str = None,
        cluster_id: str = None,
        from_: int = None,
        is_reverse: bool = None,
        log_request_id: str = None,
        log_type: str = None,
        operator_uid: str = None,
        page_number: int = None,
        page_size: int = None,
        resource: str = None,
        to: int = None,
    ):
        self.action_name = action_name
        self.action_status = action_status
        self.cluster_id = cluster_id
        # This parameter is required.
        self.from_ = from_
        self.is_reverse = is_reverse
        self.log_request_id = log_request_id
        self.log_type = log_type
        self.operator_uid = operator_uid
        self.page_number = page_number
        self.page_size = page_size
        self.resource = resource
        # This parameter is required.
        self.to = to

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_name is not None:
            result['ActionName'] = self.action_name
        if self.action_status is not None:
            result['ActionStatus'] = self.action_status
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.from_ is not None:
            result['From'] = self.from_
        if self.is_reverse is not None:
            result['IsReverse'] = self.is_reverse
        if self.log_request_id is not None:
            result['LogRequestId'] = self.log_request_id
        if self.log_type is not None:
            result['LogType'] = self.log_type
        if self.operator_uid is not None:
            result['OperatorUid'] = self.operator_uid
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.to is not None:
            result['To'] = self.to
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionName') is not None:
            self.action_name = m.get('ActionName')
        if m.get('ActionStatus') is not None:
            self.action_status = m.get('ActionStatus')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('IsReverse') is not None:
            self.is_reverse = m.get('IsReverse')
        if m.get('LogRequestId') is not None:
            self.log_request_id = m.get('LogRequestId')
        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')
        if m.get('OperatorUid') is not None:
            self.operator_uid = m.get('OperatorUid')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('To') is not None:
            self.to = m.get('To')
        return self


class ListCommonLogsShrinkRequest(TeaModel):
    def __init__(
        self,
        action_name_shrink: str = None,
        action_status: str = None,
        cluster_id: str = None,
        from_: int = None,
        is_reverse: bool = None,
        log_request_id: str = None,
        log_type: str = None,
        operator_uid: str = None,
        page_number: int = None,
        page_size: int = None,
        resource: str = None,
        to: int = None,
    ):
        self.action_name_shrink = action_name_shrink
        self.action_status = action_status
        self.cluster_id = cluster_id
        # This parameter is required.
        self.from_ = from_
        self.is_reverse = is_reverse
        self.log_request_id = log_request_id
        self.log_type = log_type
        self.operator_uid = operator_uid
        self.page_number = page_number
        self.page_size = page_size
        self.resource = resource
        # This parameter is required.
        self.to = to

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_name_shrink is not None:
            result['ActionName'] = self.action_name_shrink
        if self.action_status is not None:
            result['ActionStatus'] = self.action_status
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.from_ is not None:
            result['From'] = self.from_
        if self.is_reverse is not None:
            result['IsReverse'] = self.is_reverse
        if self.log_request_id is not None:
            result['LogRequestId'] = self.log_request_id
        if self.log_type is not None:
            result['LogType'] = self.log_type
        if self.operator_uid is not None:
            result['OperatorUid'] = self.operator_uid
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.to is not None:
            result['To'] = self.to
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionName') is not None:
            self.action_name_shrink = m.get('ActionName')
        if m.get('ActionStatus') is not None:
            self.action_status = m.get('ActionStatus')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('IsReverse') is not None:
            self.is_reverse = m.get('IsReverse')
        if m.get('LogRequestId') is not None:
            self.log_request_id = m.get('LogRequestId')
        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')
        if m.get('OperatorUid') is not None:
            self.operator_uid = m.get('OperatorUid')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('To') is not None:
            self.to = m.get('To')
        return self


class ListCommonLogsResponseBodyLogs(TeaModel):
    def __init__(
        self,
        action: str = None,
        cluster_id: str = None,
        log_type: str = None,
        message: str = None,
        operator_uid: str = None,
        request_id: str = None,
        status: str = None,
        target: str = None,
        time: str = None,
    ):
        self.action = action
        self.cluster_id = cluster_id
        self.log_type = log_type
        self.message = message
        self.operator_uid = operator_uid
        self.request_id = request_id
        self.status = status
        self.target = target
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.log_type is not None:
            result['LogType'] = self.log_type
        if self.message is not None:
            result['Message'] = self.message
        if self.operator_uid is not None:
            result['OperatorUid'] = self.operator_uid
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.target is not None:
            result['Target'] = self.target
        if self.time is not None:
            result['Time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OperatorUid') is not None:
            self.operator_uid = m.get('OperatorUid')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        return self


class ListCommonLogsResponseBody(TeaModel):
    def __init__(
        self,
        logs: List[ListCommonLogsResponseBodyLogs] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        uid: str = None,
    ):
        self.logs = logs
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count
        self.uid = uid

    def validate(self):
        if self.logs:
            for k in self.logs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Logs'] = []
        if self.logs is not None:
            for k in self.logs:
                result['Logs'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.logs = []
        if m.get('Logs') is not None:
            for k in m.get('Logs'):
                temp_model = ListCommonLogsResponseBodyLogs()
                self.logs.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class ListCommonLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCommonLogsResponseBody = None,
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
            temp_model = ListCommonLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstalledSoftwaresRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        page_number: str = None,
        page_size: str = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListInstalledSoftwaresResponseBodyAdditionalPackagesAdditionalPackageInfos(TeaModel):
    def __init__(
        self,
        category: str = None,
        create_time: str = None,
        description: str = None,
        icon: str = None,
        name: str = None,
        status: str = None,
        version: str = None,
    ):
        # The category into which the software falls.
        self.category = category
        # The time when the software was installed.
        self.create_time = create_time
        # The software description.
        self.description = description
        # The URL of the software icon.
        self.icon = icon
        # The software name.
        self.name = name
        # The installation status of the software.
        # 
        # Valid values:
        # 
        # *   Installed
        # *   Uninstalled
        # *   Installing
        # *   Exception
        self.status = status
        # The software version.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListInstalledSoftwaresResponseBodyAdditionalPackages(TeaModel):
    def __init__(
        self,
        additional_package_infos: List[ListInstalledSoftwaresResponseBodyAdditionalPackagesAdditionalPackageInfos] = None,
    ):
        self.additional_package_infos = additional_package_infos

    def validate(self):
        if self.additional_package_infos:
            for k in self.additional_package_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AdditionalPackageInfos'] = []
        if self.additional_package_infos is not None:
            for k in self.additional_package_infos:
                result['AdditionalPackageInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.additional_package_infos = []
        if m.get('AdditionalPackageInfos') is not None:
            for k in m.get('AdditionalPackageInfos'):
                temp_model = ListInstalledSoftwaresResponseBodyAdditionalPackagesAdditionalPackageInfos()
                self.additional_package_infos.append(temp_model.from_map(k))
        return self


class ListInstalledSoftwaresResponseBody(TeaModel):
    def __init__(
        self,
        additional_packages: ListInstalledSoftwaresResponseBodyAdditionalPackages = None,
        page_number: str = None,
        page_size: str = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # The list of installed software.
        self.additional_packages = additional_packages
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.additional_packages:
            self.additional_packages.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.additional_packages is not None:
            result['AdditionalPackages'] = self.additional_packages.to_map()
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
        if m.get('AdditionalPackages') is not None:
            temp_model = ListInstalledSoftwaresResponseBodyAdditionalPackages()
            self.additional_packages = temp_model.from_map(m['AdditionalPackages'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListInstalledSoftwaresResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInstalledSoftwaresResponseBody = None,
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
            temp_model = ListInstalledSoftwaresResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNodesRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        hostnames: List[str] = None,
        page_number: int = None,
        page_size: int = None,
        private_ip_address: List[str] = None,
        queue_names: List[str] = None,
        sequence: str = None,
        sort_by: str = None,
        status: List[str] = None,
    ):
        self.cluster_id = cluster_id
        self.hostnames = hostnames
        self.page_number = page_number
        self.page_size = page_size
        self.private_ip_address = private_ip_address
        self.queue_names = queue_names
        self.sequence = sequence
        self.sort_by = sort_by
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.hostnames is not None:
            result['Hostnames'] = self.hostnames
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        if self.queue_names is not None:
            result['QueueNames'] = self.queue_names
        if self.sequence is not None:
            result['Sequence'] = self.sequence
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Hostnames') is not None:
            self.hostnames = m.get('Hostnames')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')
        if m.get('QueueNames') is not None:
            self.queue_names = m.get('QueueNames')
        if m.get('Sequence') is not None:
            self.sequence = m.get('Sequence')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListNodesShrinkRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        hostnames_shrink: str = None,
        page_number: int = None,
        page_size: int = None,
        private_ip_address_shrink: str = None,
        queue_names_shrink: str = None,
        sequence: str = None,
        sort_by: str = None,
        status_shrink: str = None,
    ):
        self.cluster_id = cluster_id
        self.hostnames_shrink = hostnames_shrink
        self.page_number = page_number
        self.page_size = page_size
        self.private_ip_address_shrink = private_ip_address_shrink
        self.queue_names_shrink = queue_names_shrink
        self.sequence = sequence
        self.sort_by = sort_by
        self.status_shrink = status_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.hostnames_shrink is not None:
            result['Hostnames'] = self.hostnames_shrink
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.private_ip_address_shrink is not None:
            result['PrivateIpAddress'] = self.private_ip_address_shrink
        if self.queue_names_shrink is not None:
            result['QueueNames'] = self.queue_names_shrink
        if self.sequence is not None:
            result['Sequence'] = self.sequence
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.status_shrink is not None:
            result['Status'] = self.status_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Hostnames') is not None:
            self.hostnames_shrink = m.get('Hostnames')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address_shrink = m.get('PrivateIpAddress')
        if m.get('QueueNames') is not None:
            self.queue_names_shrink = m.get('QueueNames')
        if m.get('Sequence') is not None:
            self.sequence = m.get('Sequence')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('Status') is not None:
            self.status_shrink = m.get('Status')
        return self


class ListNodesResponseBodyNodesTotalResources(TeaModel):
    def __init__(
        self,
        cpu: int = None,
        gpu: int = None,
        memory: int = None,
    ):
        self.cpu = cpu
        self.gpu = gpu
        self.memory = memory

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.gpu is not None:
            result['Gpu'] = self.gpu
        if self.memory is not None:
            result['Memory'] = self.memory
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        return self


class ListNodesResponseBodyNodes(TeaModel):
    def __init__(
        self,
        add_time: str = None,
        expired_time: str = None,
        hostname: str = None,
        ht_enabled: bool = None,
        id: str = None,
        image_id: str = None,
        instance_type: str = None,
        ip_address: str = None,
        keep_alive: bool = None,
        public_ip_address: str = None,
        queue_name: str = None,
        spot_strategy: str = None,
        state_in_sched: str = None,
        status: str = None,
        total_resources: ListNodesResponseBodyNodesTotalResources = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        self.add_time = add_time
        self.expired_time = expired_time
        self.hostname = hostname
        self.ht_enabled = ht_enabled
        self.id = id
        self.image_id = image_id
        self.instance_type = instance_type
        self.ip_address = ip_address
        self.keep_alive = keep_alive
        self.public_ip_address = public_ip_address
        self.queue_name = queue_name
        self.spot_strategy = spot_strategy
        self.state_in_sched = state_in_sched
        self.status = status
        self.total_resources = total_resources
        self.v_switch_id = v_switch_id
        self.vpc_id = vpc_id
        self.zone_id = zone_id

    def validate(self):
        if self.total_resources:
            self.total_resources.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_time is not None:
            result['AddTime'] = self.add_time
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.ht_enabled is not None:
            result['HtEnabled'] = self.ht_enabled
        if self.id is not None:
            result['Id'] = self.id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address
        if self.keep_alive is not None:
            result['KeepAlive'] = self.keep_alive
        if self.public_ip_address is not None:
            result['PublicIpAddress'] = self.public_ip_address
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        if self.state_in_sched is not None:
            result['StateInSched'] = self.state_in_sched
        if self.status is not None:
            result['Status'] = self.status
        if self.total_resources is not None:
            result['TotalResources'] = self.total_resources.to_map()
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddTime') is not None:
            self.add_time = m.get('AddTime')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('HtEnabled') is not None:
            self.ht_enabled = m.get('HtEnabled')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')
        if m.get('KeepAlive') is not None:
            self.keep_alive = m.get('KeepAlive')
        if m.get('PublicIpAddress') is not None:
            self.public_ip_address = m.get('PublicIpAddress')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        if m.get('StateInSched') is not None:
            self.state_in_sched = m.get('StateInSched')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TotalResources') is not None:
            temp_model = ListNodesResponseBodyNodesTotalResources()
            self.total_resources = temp_model.from_map(m['TotalResources'])
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListNodesResponseBody(TeaModel):
    def __init__(
        self,
        nodes: List[ListNodesResponseBodyNodes] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.nodes = nodes
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
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
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = ListNodesResponseBodyNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListNodesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListNodesResponseBody = None,
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
            temp_model = ListNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListQueuesRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        queue_names: List[str] = None,
    ):
        self.cluster_id = cluster_id
        self.queue_names = queue_names

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.queue_names is not None:
            result['QueueNames'] = self.queue_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('QueueNames') is not None:
            self.queue_names = m.get('QueueNames')
        return self


class ListQueuesShrinkRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        queue_names_shrink: str = None,
    ):
        self.cluster_id = cluster_id
        self.queue_names_shrink = queue_names_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.queue_names_shrink is not None:
            result['QueueNames'] = self.queue_names_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('QueueNames') is not None:
            self.queue_names_shrink = m.get('QueueNames')
        return self


class ListQueuesResponseBodyQueuesNodes(TeaModel):
    def __init__(
        self,
        creating_counts: int = None,
        exception_counts: int = None,
        running_counts: int = None,
    ):
        self.creating_counts = creating_counts
        self.exception_counts = exception_counts
        self.running_counts = running_counts

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creating_counts is not None:
            result['CreatingCounts'] = self.creating_counts
        if self.exception_counts is not None:
            result['ExceptionCounts'] = self.exception_counts
        if self.running_counts is not None:
            result['RunningCounts'] = self.running_counts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatingCounts') is not None:
            self.creating_counts = m.get('CreatingCounts')
        if m.get('ExceptionCounts') is not None:
            self.exception_counts = m.get('ExceptionCounts')
        if m.get('RunningCounts') is not None:
            self.running_counts = m.get('RunningCounts')
        return self


class ListQueuesResponseBodyQueues(TeaModel):
    def __init__(
        self,
        compute_nodes: List[NodeTemplate] = None,
        create_time: str = None,
        enable_scale_in: bool = None,
        enable_scale_out: bool = None,
        max_count: int = None,
        max_count_per_cycle: int = None,
        min_count: int = None,
        nodes: ListQueuesResponseBodyQueuesNodes = None,
        queue_name: str = None,
        total_cores: int = None,
        update_time: str = None,
        v_switch_ids: List[str] = None,
    ):
        self.compute_nodes = compute_nodes
        self.create_time = create_time
        self.enable_scale_in = enable_scale_in
        self.enable_scale_out = enable_scale_out
        self.max_count = max_count
        self.max_count_per_cycle = max_count_per_cycle
        self.min_count = min_count
        self.nodes = nodes
        self.queue_name = queue_name
        self.total_cores = total_cores
        self.update_time = update_time
        self.v_switch_ids = v_switch_ids

    def validate(self):
        if self.compute_nodes:
            for k in self.compute_nodes:
                if k:
                    k.validate()
        if self.nodes:
            self.nodes.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ComputeNodes'] = []
        if self.compute_nodes is not None:
            for k in self.compute_nodes:
                result['ComputeNodes'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.enable_scale_in is not None:
            result['EnableScaleIn'] = self.enable_scale_in
        if self.enable_scale_out is not None:
            result['EnableScaleOut'] = self.enable_scale_out
        if self.max_count is not None:
            result['MaxCount'] = self.max_count
        if self.max_count_per_cycle is not None:
            result['MaxCountPerCycle'] = self.max_count_per_cycle
        if self.min_count is not None:
            result['MinCount'] = self.min_count
        if self.nodes is not None:
            result['Nodes'] = self.nodes.to_map()
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.total_cores is not None:
            result['TotalCores'] = self.total_cores
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.compute_nodes = []
        if m.get('ComputeNodes') is not None:
            for k in m.get('ComputeNodes'):
                temp_model = NodeTemplate()
                self.compute_nodes.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EnableScaleIn') is not None:
            self.enable_scale_in = m.get('EnableScaleIn')
        if m.get('EnableScaleOut') is not None:
            self.enable_scale_out = m.get('EnableScaleOut')
        if m.get('MaxCount') is not None:
            self.max_count = m.get('MaxCount')
        if m.get('MaxCountPerCycle') is not None:
            self.max_count_per_cycle = m.get('MaxCountPerCycle')
        if m.get('MinCount') is not None:
            self.min_count = m.get('MinCount')
        if m.get('Nodes') is not None:
            temp_model = ListQueuesResponseBodyQueuesNodes()
            self.nodes = temp_model.from_map(m['Nodes'])
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('TotalCores') is not None:
            self.total_cores = m.get('TotalCores')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        return self


class ListQueuesResponseBody(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        page_number: int = None,
        page_size: int = None,
        queues: List[ListQueuesResponseBodyQueues] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.cluster_id = cluster_id
        self.page_number = page_number
        self.page_size = page_size
        self.queues = queues
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.queues:
            for k in self.queues:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Queues'] = []
        if self.queues is not None:
            for k in self.queues:
                result['Queues'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.queues = []
        if m.get('Queues') is not None:
            for k in m.get('Queues'):
                temp_model = ListQueuesResponseBodyQueues()
                self.queues.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListQueuesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListQueuesResponseBody = None,
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
            temp_model = ListQueuesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSharedStoragesRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        file_system_id: str = None,
        file_system_type: str = None,
    ):
        # The cluster ID.
        # 
        # You can call the [ListClusters](https://help.aliyun.com/document_detail/87116.html) operation to query the cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The ID of the attached file system.
        self.file_system_id = file_system_id
        # The type of the attached file system. Valid values:
        # 
        # *   nas
        # *   cpfs
        self.file_system_type = file_system_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        return self


class ListSharedStoragesResponseBodySharedStoragesMountInfo(TeaModel):
    def __init__(
        self,
        mount_directory: str = None,
        mount_options: str = None,
        mount_target: str = None,
        protocol_type: str = None,
        storage_directory: str = None,
    ):
        # The local mount directory of the attached file system.
        self.mount_directory = mount_directory
        # The mount options for the attached file system. Valid values:
        # 
        # *   \\-t nfs -o vers=3,nolock,proto=tcp,noresvport
        # *   \\-t nfs -o vers=4.0,noresvport
        self.mount_options = mount_options
        # The mount target of the attached file system.
        self.mount_target = mount_target
        # The protocol used by the mount target of the attached file system. Valid values:
        # 
        # *   nfs3
        # *   nfs4
        # *   cpfs
        self.protocol_type = protocol_type
        # The storage directory of the attached file system.
        self.storage_directory = storage_directory

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mount_directory is not None:
            result['MountDirectory'] = self.mount_directory
        if self.mount_options is not None:
            result['MountOptions'] = self.mount_options
        if self.mount_target is not None:
            result['MountTarget'] = self.mount_target
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.storage_directory is not None:
            result['StorageDirectory'] = self.storage_directory
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MountDirectory') is not None:
            self.mount_directory = m.get('MountDirectory')
        if m.get('MountOptions') is not None:
            self.mount_options = m.get('MountOptions')
        if m.get('MountTarget') is not None:
            self.mount_target = m.get('MountTarget')
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('StorageDirectory') is not None:
            self.storage_directory = m.get('StorageDirectory')
        return self


class ListSharedStoragesResponseBodySharedStorages(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        file_system_protocol: str = None,
        file_system_type: str = None,
        mount_info: List[ListSharedStoragesResponseBodySharedStoragesMountInfo] = None,
    ):
        # The ID of the attached file system.
        self.file_system_id = file_system_id
        # The protocol used by the attached file system. Valid values:
        # 
        # *   nfs3
        # *   nfs4
        # *   cpfs
        self.file_system_protocol = file_system_protocol
        # The type of the attached file system. Valid values:
        # 
        # *   nas
        # *   cpfs
        self.file_system_type = file_system_type
        # The mount information.
        self.mount_info = mount_info

    def validate(self):
        if self.mount_info:
            for k in self.mount_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.file_system_protocol is not None:
            result['FileSystemProtocol'] = self.file_system_protocol
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        result['MountInfo'] = []
        if self.mount_info is not None:
            for k in self.mount_info:
                result['MountInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('FileSystemProtocol') is not None:
            self.file_system_protocol = m.get('FileSystemProtocol')
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        self.mount_info = []
        if m.get('MountInfo') is not None:
            for k in m.get('MountInfo'):
                temp_model = ListSharedStoragesResponseBodySharedStoragesMountInfo()
                self.mount_info.append(temp_model.from_map(k))
        return self


class ListSharedStoragesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        shared_storages: List[ListSharedStoragesResponseBodySharedStorages] = None,
        success: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the attached shared storage.
        self.shared_storages = shared_storages
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        if self.shared_storages:
            for k in self.shared_storages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SharedStorages'] = []
        if self.shared_storages is not None:
            for k in self.shared_storages:
                result['SharedStorages'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.shared_storages = []
        if m.get('SharedStorages') is not None:
            for k in m.get('SharedStorages'):
                temp_model = ListSharedStoragesResponseBodySharedStorages()
                self.shared_storages.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListSharedStoragesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSharedStoragesResponseBody = None,
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
            temp_model = ListSharedStoragesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSoftwaresRequestOsInfos(TeaModel):
    def __init__(
        self,
        architecture: str = None,
        os_tag: str = None,
    ):
        # The OS architecture. Valid values:
        # 
        # *   x86_64
        # *   arm64
        self.architecture = architecture
        # The image tag.
        self.os_tag = os_tag

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture is not None:
            result['Architecture'] = self.architecture
        if self.os_tag is not None:
            result['OsTag'] = self.os_tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Architecture') is not None:
            self.architecture = m.get('Architecture')
        if m.get('OsTag') is not None:
            self.os_tag = m.get('OsTag')
        return self


class ListSoftwaresRequest(TeaModel):
    def __init__(
        self,
        category: str = None,
        cluster_id: str = None,
        name: str = None,
        os_infos: List[ListSoftwaresRequestOsInfos] = None,
        page_number: str = None,
        page_size: str = None,
    ):
        # The application category.
        self.category = category
        # The cluster ID.
        self.cluster_id = cluster_id
        # The software name.
        self.name = name
        # The operating system (OS) information.
        self.os_infos = os_infos
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size

    def validate(self):
        if self.os_infos:
            for k in self.os_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.name is not None:
            result['Name'] = self.name
        result['OsInfos'] = []
        if self.os_infos is not None:
            for k in self.os_infos:
                result['OsInfos'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.os_infos = []
        if m.get('OsInfos') is not None:
            for k in m.get('OsInfos'):
                temp_model = ListSoftwaresRequestOsInfos()
                self.os_infos.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListSoftwaresResponseBodyAdditionalPackagesAdditionalPackageInfosVersionsVersionInfosSupportOsSupportOsInfos(TeaModel):
    def __init__(
        self,
        architecture: str = None,
        os_tag: str = None,
    ):
        # The OS architecture. Valid values:
        # 
        # *   x86_64
        # *   arm64
        self.architecture = architecture
        # The image tag.
        self.os_tag = os_tag

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture is not None:
            result['Architecture'] = self.architecture
        if self.os_tag is not None:
            result['OsTag'] = self.os_tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Architecture') is not None:
            self.architecture = m.get('Architecture')
        if m.get('OsTag') is not None:
            self.os_tag = m.get('OsTag')
        return self


class ListSoftwaresResponseBodyAdditionalPackagesAdditionalPackageInfosVersionsVersionInfosSupportOs(TeaModel):
    def __init__(
        self,
        support_os_infos: List[ListSoftwaresResponseBodyAdditionalPackagesAdditionalPackageInfosVersionsVersionInfosSupportOsSupportOsInfos] = None,
    ):
        self.support_os_infos = support_os_infos

    def validate(self):
        if self.support_os_infos:
            for k in self.support_os_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SupportOsInfos'] = []
        if self.support_os_infos is not None:
            for k in self.support_os_infos:
                result['SupportOsInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.support_os_infos = []
        if m.get('SupportOsInfos') is not None:
            for k in m.get('SupportOsInfos'):
                temp_model = ListSoftwaresResponseBodyAdditionalPackagesAdditionalPackageInfosVersionsVersionInfosSupportOsSupportOsInfos()
                self.support_os_infos.append(temp_model.from_map(k))
        return self


class ListSoftwaresResponseBodyAdditionalPackagesAdditionalPackageInfosVersionsVersionInfos(TeaModel):
    def __init__(
        self,
        latest: str = None,
        support_os: ListSoftwaresResponseBodyAdditionalPackagesAdditionalPackageInfosVersionsVersionInfosSupportOs = None,
        version: str = None,
    ):
        # Indicates whether the version is the latest.
        self.latest = latest
        # The information about the supported OSs.
        self.support_os = support_os
        # The software version.
        self.version = version

    def validate(self):
        if self.support_os:
            self.support_os.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.latest is not None:
            result['Latest'] = self.latest
        if self.support_os is not None:
            result['SupportOs'] = self.support_os.to_map()
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Latest') is not None:
            self.latest = m.get('Latest')
        if m.get('SupportOs') is not None:
            temp_model = ListSoftwaresResponseBodyAdditionalPackagesAdditionalPackageInfosVersionsVersionInfosSupportOs()
            self.support_os = temp_model.from_map(m['SupportOs'])
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListSoftwaresResponseBodyAdditionalPackagesAdditionalPackageInfosVersions(TeaModel):
    def __init__(
        self,
        version_infos: List[ListSoftwaresResponseBodyAdditionalPackagesAdditionalPackageInfosVersionsVersionInfos] = None,
    ):
        self.version_infos = version_infos

    def validate(self):
        if self.version_infos:
            for k in self.version_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['VersionInfos'] = []
        if self.version_infos is not None:
            for k in self.version_infos:
                result['VersionInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.version_infos = []
        if m.get('VersionInfos') is not None:
            for k in m.get('VersionInfos'):
                temp_model = ListSoftwaresResponseBodyAdditionalPackagesAdditionalPackageInfosVersionsVersionInfos()
                self.version_infos.append(temp_model.from_map(k))
        return self


class ListSoftwaresResponseBodyAdditionalPackagesAdditionalPackageInfos(TeaModel):
    def __init__(
        self,
        category: str = None,
        description: str = None,
        icon: str = None,
        name: str = None,
        versions: ListSoftwaresResponseBodyAdditionalPackagesAdditionalPackageInfosVersions = None,
    ):
        # The application category.
        self.category = category
        # The software description.
        self.description = description
        # The URL of the software icon.
        self.icon = icon
        # The software name.
        self.name = name
        # The information about the software versions that can be installed in the cluster.
        self.versions = versions

    def validate(self):
        if self.versions:
            self.versions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.description is not None:
            result['Description'] = self.description
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.name is not None:
            result['Name'] = self.name
        if self.versions is not None:
            result['Versions'] = self.versions.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Versions') is not None:
            temp_model = ListSoftwaresResponseBodyAdditionalPackagesAdditionalPackageInfosVersions()
            self.versions = temp_model.from_map(m['Versions'])
        return self


class ListSoftwaresResponseBodyAdditionalPackages(TeaModel):
    def __init__(
        self,
        additional_package_infos: List[ListSoftwaresResponseBodyAdditionalPackagesAdditionalPackageInfos] = None,
    ):
        self.additional_package_infos = additional_package_infos

    def validate(self):
        if self.additional_package_infos:
            for k in self.additional_package_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AdditionalPackageInfos'] = []
        if self.additional_package_infos is not None:
            for k in self.additional_package_infos:
                result['AdditionalPackageInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.additional_package_infos = []
        if m.get('AdditionalPackageInfos') is not None:
            for k in m.get('AdditionalPackageInfos'):
                temp_model = ListSoftwaresResponseBodyAdditionalPackagesAdditionalPackageInfos()
                self.additional_package_infos.append(temp_model.from_map(k))
        return self


class ListSoftwaresResponseBody(TeaModel):
    def __init__(
        self,
        additional_packages: ListSoftwaresResponseBodyAdditionalPackages = None,
        page_number: str = None,
        page_size: str = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # The information about the software that can be installed in the cluster.
        self.additional_packages = additional_packages
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.additional_packages:
            self.additional_packages.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.additional_packages is not None:
            result['AdditionalPackages'] = self.additional_packages.to_map()
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
        if m.get('AdditionalPackages') is not None:
            temp_model = ListSoftwaresResponseBodyAdditionalPackages()
            self.additional_packages = temp_model.from_map(m['AdditionalPackages'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListSoftwaresResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSoftwaresResponseBody = None,
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
            temp_model = ListSoftwaresResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUsersRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The page number.
        # 
        # Pages start from page 1.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 50.
        # 
        # Default value: 10.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListUsersResponseBodyUsersUserInfo(TeaModel):
    def __init__(
        self,
        add_time: str = None,
        group: str = None,
        group_id: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        # The time when the user was first added.
        self.add_time = add_time
        # The name of the permission group. Valid values:
        # 
        # users: ordinary permissions, which are suitable for regular users that need only to submit and debug jobs.
        # 
        # wheel: sudo permissions, which are suitable for administrators who need to manage clusters. In addition to submitting and debugging jobs, you can also run sudo commands to install software and restart nodes.
        self.group = group
        # The permission group ID.
        self.group_id = group_id
        # The user ID.
        self.user_id = user_id
        # The username.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_time is not None:
            result['AddTime'] = self.add_time
        if self.group is not None:
            result['Group'] = self.group
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddTime') is not None:
            self.add_time = m.get('AddTime')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class ListUsersResponseBodyUsers(TeaModel):
    def __init__(
        self,
        user_info: List[ListUsersResponseBodyUsersUserInfo] = None,
    ):
        self.user_info = user_info

    def validate(self):
        if self.user_info:
            for k in self.user_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['UserInfo'] = []
        if self.user_info is not None:
            for k in self.user_info:
                result['UserInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.user_info = []
        if m.get('UserInfo') is not None:
            for k in m.get('UserInfo'):
                temp_model = ListUsersResponseBodyUsersUserInfo()
                self.user_info.append(temp_model.from_map(k))
        return self


class ListUsersResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        users: ListUsersResponseBodyUsers = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count
        # The information about the users.
        self.users = users

    def validate(self):
        if self.users:
            self.users.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.users is not None:
            result['Users'] = self.users.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Users') is not None:
            temp_model = ListUsersResponseBodyUsers()
            self.users = temp_model.from_map(m['Users'])
        return self


class ListUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUsersResponseBody = None,
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
            temp_model = ListUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnInstallAddonRequest(TeaModel):
    def __init__(
        self,
        addon_id: str = None,
        cluster_id: str = None,
    ):
        # The addon ID.
        # 
        # This parameter is required.
        self.addon_id = addon_id
        # The cluster ID.
        # 
        # You can call the [ListClusters](https://help.aliyun.com/document_detail/87116.html) operation to query the cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.addon_id is not None:
            result['AddonId'] = self.addon_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddonId') is not None:
            self.addon_id = m.get('AddonId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class UnInstallAddonResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class UnInstallAddonResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UnInstallAddonResponseBody = None,
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
            temp_model = UnInstallAddonResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UninstallSoftwaresRequestAdditionalPackages(TeaModel):
    def __init__(
        self,
        name: str = None,
        version: str = None,
    ):
        # The software name.
        self.name = name
        # The software version.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class UninstallSoftwaresRequest(TeaModel):
    def __init__(
        self,
        additional_packages: List[UninstallSoftwaresRequestAdditionalPackages] = None,
        cluster_id: str = None,
    ):
        # The information about the software systems that you want to uninstall.
        self.additional_packages = additional_packages
        # The cluster ID.
        # 
        # You can call the [ListClusters](https://help.aliyun.com/document_detail/87116.html) operation to query the cluster ID.
        self.cluster_id = cluster_id

    def validate(self):
        if self.additional_packages:
            for k in self.additional_packages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AdditionalPackages'] = []
        if self.additional_packages is not None:
            for k in self.additional_packages:
                result['AdditionalPackages'].append(k.to_map() if k else None)
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.additional_packages = []
        if m.get('AdditionalPackages') is not None:
            for k in m.get('AdditionalPackages'):
                temp_model = UninstallSoftwaresRequestAdditionalPackages()
                self.additional_packages.append(temp_model.from_map(k))
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class UninstallSoftwaresShrinkRequest(TeaModel):
    def __init__(
        self,
        additional_packages_shrink: str = None,
        cluster_id: str = None,
    ):
        # The information about the software systems that you want to uninstall.
        self.additional_packages_shrink = additional_packages_shrink
        # The cluster ID.
        # 
        # You can call the [ListClusters](https://help.aliyun.com/document_detail/87116.html) operation to query the cluster ID.
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.additional_packages_shrink is not None:
            result['AdditionalPackages'] = self.additional_packages_shrink
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdditionalPackages') is not None:
            self.additional_packages_shrink = m.get('AdditionalPackages')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class UninstallSoftwaresResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class UninstallSoftwaresResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UninstallSoftwaresResponseBody = None,
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
            temp_model = UninstallSoftwaresResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateClusterRequestClusterCustomConfiguration(TeaModel):
    def __init__(
        self,
        args: str = None,
        script: str = None,
    ):
        self.args = args
        self.script = script

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class UpdateClusterRequest(TeaModel):
    def __init__(
        self,
        client_version: str = None,
        cluster_custom_configuration: UpdateClusterRequestClusterCustomConfiguration = None,
        cluster_description: str = None,
        cluster_id: str = None,
        cluster_name: str = None,
        deletion_protection: bool = None,
        enable_scale_in: bool = None,
        enable_scale_out: bool = None,
        grow_interval: int = None,
        idle_interval: int = None,
        max_core_count: int = None,
        max_count: int = None,
    ):
        self.client_version = client_version
        self.cluster_custom_configuration = cluster_custom_configuration
        self.cluster_description = cluster_description
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.deletion_protection = deletion_protection
        self.enable_scale_in = enable_scale_in
        self.enable_scale_out = enable_scale_out
        self.grow_interval = grow_interval
        self.idle_interval = idle_interval
        self.max_core_count = max_core_count
        self.max_count = max_count

    def validate(self):
        if self.cluster_custom_configuration:
            self.cluster_custom_configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.cluster_custom_configuration is not None:
            result['ClusterCustomConfiguration'] = self.cluster_custom_configuration.to_map()
        if self.cluster_description is not None:
            result['ClusterDescription'] = self.cluster_description
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection
        if self.enable_scale_in is not None:
            result['EnableScaleIn'] = self.enable_scale_in
        if self.enable_scale_out is not None:
            result['EnableScaleOut'] = self.enable_scale_out
        if self.grow_interval is not None:
            result['GrowInterval'] = self.grow_interval
        if self.idle_interval is not None:
            result['IdleInterval'] = self.idle_interval
        if self.max_core_count is not None:
            result['MaxCoreCount'] = self.max_core_count
        if self.max_count is not None:
            result['MaxCount'] = self.max_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('ClusterCustomConfiguration') is not None:
            temp_model = UpdateClusterRequestClusterCustomConfiguration()
            self.cluster_custom_configuration = temp_model.from_map(m['ClusterCustomConfiguration'])
        if m.get('ClusterDescription') is not None:
            self.cluster_description = m.get('ClusterDescription')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')
        if m.get('EnableScaleIn') is not None:
            self.enable_scale_in = m.get('EnableScaleIn')
        if m.get('EnableScaleOut') is not None:
            self.enable_scale_out = m.get('EnableScaleOut')
        if m.get('GrowInterval') is not None:
            self.grow_interval = m.get('GrowInterval')
        if m.get('IdleInterval') is not None:
            self.idle_interval = m.get('IdleInterval')
        if m.get('MaxCoreCount') is not None:
            self.max_core_count = m.get('MaxCoreCount')
        if m.get('MaxCount') is not None:
            self.max_count = m.get('MaxCount')
        return self


class UpdateClusterShrinkRequest(TeaModel):
    def __init__(
        self,
        client_version: str = None,
        cluster_custom_configuration_shrink: str = None,
        cluster_description: str = None,
        cluster_id: str = None,
        cluster_name: str = None,
        deletion_protection: bool = None,
        enable_scale_in: bool = None,
        enable_scale_out: bool = None,
        grow_interval: int = None,
        idle_interval: int = None,
        max_core_count: int = None,
        max_count: int = None,
    ):
        self.client_version = client_version
        self.cluster_custom_configuration_shrink = cluster_custom_configuration_shrink
        self.cluster_description = cluster_description
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.deletion_protection = deletion_protection
        self.enable_scale_in = enable_scale_in
        self.enable_scale_out = enable_scale_out
        self.grow_interval = grow_interval
        self.idle_interval = idle_interval
        self.max_core_count = max_core_count
        self.max_count = max_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.cluster_custom_configuration_shrink is not None:
            result['ClusterCustomConfiguration'] = self.cluster_custom_configuration_shrink
        if self.cluster_description is not None:
            result['ClusterDescription'] = self.cluster_description
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection
        if self.enable_scale_in is not None:
            result['EnableScaleIn'] = self.enable_scale_in
        if self.enable_scale_out is not None:
            result['EnableScaleOut'] = self.enable_scale_out
        if self.grow_interval is not None:
            result['GrowInterval'] = self.grow_interval
        if self.idle_interval is not None:
            result['IdleInterval'] = self.idle_interval
        if self.max_core_count is not None:
            result['MaxCoreCount'] = self.max_core_count
        if self.max_count is not None:
            result['MaxCount'] = self.max_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('ClusterCustomConfiguration') is not None:
            self.cluster_custom_configuration_shrink = m.get('ClusterCustomConfiguration')
        if m.get('ClusterDescription') is not None:
            self.cluster_description = m.get('ClusterDescription')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')
        if m.get('EnableScaleIn') is not None:
            self.enable_scale_in = m.get('EnableScaleIn')
        if m.get('EnableScaleOut') is not None:
            self.enable_scale_out = m.get('EnableScaleOut')
        if m.get('GrowInterval') is not None:
            self.grow_interval = m.get('GrowInterval')
        if m.get('IdleInterval') is not None:
            self.idle_interval = m.get('IdleInterval')
        if m.get('MaxCoreCount') is not None:
            self.max_core_count = m.get('MaxCoreCount')
        if m.get('MaxCount') is not None:
            self.max_count = m.get('MaxCount')
        return self


class UpdateClusterResponseBody(TeaModel):
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


class UpdateClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateClusterResponseBody = None,
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
            temp_model = UpdateClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateNodesRequestInstances(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        keep_alive: bool = None,
    ):
        # The instance ID of the compute node.
        self.instance_id = instance_id
        # Specifies whether to enable deletion protection for the compute node.
        self.keep_alive = keep_alive

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.keep_alive is not None:
            result['KeepAlive'] = self.keep_alive
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('KeepAlive') is not None:
            self.keep_alive = m.get('KeepAlive')
        return self


class UpdateNodesRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        instances: List[UpdateNodesRequestInstances] = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # The information about the compute nodes that you want to update.
        self.instances = instances

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = UpdateNodesRequestInstances()
                self.instances.append(temp_model.from_map(k))
        return self


class UpdateNodesShrinkRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        instances_shrink: str = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # The information about the compute nodes that you want to update.
        self.instances_shrink = instances_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.instances_shrink is not None:
            result['Instances'] = self.instances_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Instances') is not None:
            self.instances_shrink = m.get('Instances')
        return self


class UpdateNodesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The request result. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
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


class UpdateNodesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateNodesResponseBody = None,
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
            temp_model = UpdateNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateQueueRequestQueue(TeaModel):
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
        queue_name: str = None,
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
        # This parameter is required.
        self.queue_name = queue_name
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
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
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
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('RamRole') is not None:
            self.ram_role = m.get('RamRole')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        return self


class UpdateQueueRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        queue: UpdateQueueRequestQueue = None,
    ):
        self.cluster_id = cluster_id
        self.queue = queue

    def validate(self):
        if self.queue:
            self.queue.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.queue is not None:
            result['Queue'] = self.queue.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Queue') is not None:
            temp_model = UpdateQueueRequestQueue()
            self.queue = temp_model.from_map(m['Queue'])
        return self


class UpdateQueueShrinkRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        queue_shrink: str = None,
    ):
        self.cluster_id = cluster_id
        self.queue_shrink = queue_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.queue_shrink is not None:
            result['Queue'] = self.queue_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Queue') is not None:
            self.queue_shrink = m.get('Queue')
        return self


class UpdateQueueResponseBody(TeaModel):
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


class UpdateQueueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateQueueResponseBody = None,
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
            temp_model = UpdateQueueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUserRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        group: str = None,
        password: str = None,
        user_name: str = None,
    ):
        # This parameter is required.
        self.cluster_id = cluster_id
        self.group = group
        self.password = password
        # This parameter is required.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.group is not None:
            result['Group'] = self.group
        if self.password is not None:
            result['Password'] = self.password
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class UpdateUserResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: str = None,
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


class UpdateUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateUserResponseBody = None,
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
            temp_model = UpdateUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


