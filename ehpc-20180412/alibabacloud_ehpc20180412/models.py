# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class AddContainerAppRequest(TeaModel):
    def __init__(
        self,
        container_type: str = None,
        description: str = None,
        image_tag: str = None,
        name: str = None,
        repository: str = None,
    ):
        self.container_type = container_type
        self.description = description
        self.image_tag = image_tag
        self.name = name
        self.repository = repository

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_type is not None:
            result['ContainerType'] = self.container_type
        if self.description is not None:
            result['Description'] = self.description
        if self.image_tag is not None:
            result['ImageTag'] = self.image_tag
        if self.name is not None:
            result['Name'] = self.name
        if self.repository is not None:
            result['Repository'] = self.repository
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerType') is not None:
            self.container_type = m.get('ContainerType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ImageTag') is not None:
            self.image_tag = m.get('ImageTag')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Repository') is not None:
            self.repository = m.get('Repository')
        return self


class AddContainerAppResponseBodyContainerId(TeaModel):
    def __init__(
        self,
        container_id: List[str] = None,
    ):
        self.container_id = container_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_id is not None:
            result['ContainerId'] = self.container_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerId') is not None:
            self.container_id = m.get('ContainerId')
        return self


class AddContainerAppResponseBody(TeaModel):
    def __init__(
        self,
        container_id: AddContainerAppResponseBodyContainerId = None,
        request_id: str = None,
    ):
        self.container_id = container_id
        self.request_id = request_id

    def validate(self):
        if self.container_id:
            self.container_id.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_id is not None:
            result['ContainerId'] = self.container_id.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerId') is not None:
            temp_model = AddContainerAppResponseBodyContainerId()
            self.container_id = temp_model.from_map(m['ContainerId'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddContainerAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddContainerAppResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = AddContainerAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddExistedNodesRequestInstance(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class AddExistedNodesRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        image_id: str = None,
        image_owner_alias: str = None,
        instance: List[AddExistedNodesRequestInstance] = None,
        job_queue: str = None,
    ):
        self.cluster_id = cluster_id
        self.image_id = image_id
        self.image_owner_alias = image_owner_alias
        self.instance = instance
        self.job_queue = job_queue

    def validate(self):
        if self.instance:
            for k in self.instance:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_owner_alias is not None:
            result['ImageOwnerAlias'] = self.image_owner_alias
        result['Instance'] = []
        if self.instance is not None:
            for k in self.instance:
                result['Instance'].append(k.to_map() if k else None)
        if self.job_queue is not None:
            result['JobQueue'] = self.job_queue
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageOwnerAlias') is not None:
            self.image_owner_alias = m.get('ImageOwnerAlias')
        self.instance = []
        if m.get('Instance') is not None:
            for k in m.get('Instance'):
                temp_model = AddExistedNodesRequestInstance()
                self.instance.append(temp_model.from_map(k))
        if m.get('JobQueue') is not None:
            self.job_queue = m.get('JobQueue')
        return self


class AddExistedNodesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        self.request_id = request_id
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
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class AddExistedNodesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddExistedNodesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = AddExistedNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddLocalNodesRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        nodes: str = None,
        queue: str = None,
    ):
        self.cluster_id = cluster_id
        self.nodes = nodes
        self.queue = queue

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.nodes is not None:
            result['Nodes'] = self.nodes
        if self.queue is not None:
            result['Queue'] = self.queue
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Nodes') is not None:
            self.nodes = m.get('Nodes')
        if m.get('Queue') is not None:
            self.queue = m.get('Queue')
        return self


class AddLocalNodesResponseBodyInstanceIds(TeaModel):
    def __init__(
        self,
        instance_id: List[str] = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class AddLocalNodesResponseBody(TeaModel):
    def __init__(
        self,
        instance_ids: AddLocalNodesResponseBodyInstanceIds = None,
        request_id: str = None,
    ):
        self.instance_ids = instance_ids
        self.request_id = request_id

    def validate(self):
        if self.instance_ids:
            self.instance_ids.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            temp_model = AddLocalNodesResponseBodyInstanceIds()
            self.instance_ids = temp_model.from_map(m['InstanceIds'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddLocalNodesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddLocalNodesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = AddLocalNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddNodesRequestDataDisks(TeaModel):
    def __init__(
        self,
        data_disk_category: str = None,
        data_disk_delete_with_instance: bool = None,
        data_disk_encrypted: bool = None,
        data_disk_kmskey_id: str = None,
        data_disk_performance_level: str = None,
        data_disk_size: int = None,
    ):
        self.data_disk_category = data_disk_category
        self.data_disk_delete_with_instance = data_disk_delete_with_instance
        self.data_disk_encrypted = data_disk_encrypted
        self.data_disk_kmskey_id = data_disk_kmskey_id
        self.data_disk_performance_level = data_disk_performance_level
        self.data_disk_size = data_disk_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_disk_category is not None:
            result['DataDiskCategory'] = self.data_disk_category
        if self.data_disk_delete_with_instance is not None:
            result['DataDiskDeleteWithInstance'] = self.data_disk_delete_with_instance
        if self.data_disk_encrypted is not None:
            result['DataDiskEncrypted'] = self.data_disk_encrypted
        if self.data_disk_kmskey_id is not None:
            result['DataDiskKMSKeyId'] = self.data_disk_kmskey_id
        if self.data_disk_performance_level is not None:
            result['DataDiskPerformanceLevel'] = self.data_disk_performance_level
        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataDiskCategory') is not None:
            self.data_disk_category = m.get('DataDiskCategory')
        if m.get('DataDiskDeleteWithInstance') is not None:
            self.data_disk_delete_with_instance = m.get('DataDiskDeleteWithInstance')
        if m.get('DataDiskEncrypted') is not None:
            self.data_disk_encrypted = m.get('DataDiskEncrypted')
        if m.get('DataDiskKMSKeyId') is not None:
            self.data_disk_kmskey_id = m.get('DataDiskKMSKeyId')
        if m.get('DataDiskPerformanceLevel') is not None:
            self.data_disk_performance_level = m.get('DataDiskPerformanceLevel')
        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')
        return self


class AddNodesRequest(TeaModel):
    def __init__(
        self,
        allocate_public_address: bool = None,
        auto_renew: str = None,
        auto_renew_period: int = None,
        client_token: str = None,
        cluster_id: str = None,
        compute_enable_ht: bool = None,
        compute_spot_price_limit: str = None,
        compute_spot_strategy: str = None,
        count: int = None,
        create_mode: str = None,
        data_disks: List[AddNodesRequestDataDisks] = None,
        ecs_charge_type: str = None,
        host_name_prefix: str = None,
        host_name_suffix: str = None,
        image_id: str = None,
        image_owner_alias: str = None,
        instance_type: str = None,
        internet_charge_type: str = None,
        internet_max_band_width_in: int = None,
        internet_max_band_width_out: int = None,
        job_queue: str = None,
        min_count: int = None,
        period: int = None,
        period_unit: str = None,
        sync: bool = None,
        system_disk_level: str = None,
        system_disk_size: int = None,
        system_disk_type: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        self.allocate_public_address = allocate_public_address
        self.auto_renew = auto_renew
        self.auto_renew_period = auto_renew_period
        self.client_token = client_token
        self.cluster_id = cluster_id
        self.compute_enable_ht = compute_enable_ht
        self.compute_spot_price_limit = compute_spot_price_limit
        self.compute_spot_strategy = compute_spot_strategy
        self.count = count
        self.create_mode = create_mode
        self.data_disks = data_disks
        self.ecs_charge_type = ecs_charge_type
        self.host_name_prefix = host_name_prefix
        self.host_name_suffix = host_name_suffix
        self.image_id = image_id
        self.image_owner_alias = image_owner_alias
        self.instance_type = instance_type
        self.internet_charge_type = internet_charge_type
        self.internet_max_band_width_in = internet_max_band_width_in
        self.internet_max_band_width_out = internet_max_band_width_out
        self.job_queue = job_queue
        self.min_count = min_count
        self.period = period
        self.period_unit = period_unit
        self.sync = sync
        self.system_disk_level = system_disk_level
        self.system_disk_size = system_disk_size
        self.system_disk_type = system_disk_type
        self.v_switch_id = v_switch_id
        self.zone_id = zone_id

    def validate(self):
        if self.data_disks:
            for k in self.data_disks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allocate_public_address is not None:
            result['AllocatePublicAddress'] = self.allocate_public_address
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.compute_enable_ht is not None:
            result['ComputeEnableHt'] = self.compute_enable_ht
        if self.compute_spot_price_limit is not None:
            result['ComputeSpotPriceLimit'] = self.compute_spot_price_limit
        if self.compute_spot_strategy is not None:
            result['ComputeSpotStrategy'] = self.compute_spot_strategy
        if self.count is not None:
            result['Count'] = self.count
        if self.create_mode is not None:
            result['CreateMode'] = self.create_mode
        result['DataDisks'] = []
        if self.data_disks is not None:
            for k in self.data_disks:
                result['DataDisks'].append(k.to_map() if k else None)
        if self.ecs_charge_type is not None:
            result['EcsChargeType'] = self.ecs_charge_type
        if self.host_name_prefix is not None:
            result['HostNamePrefix'] = self.host_name_prefix
        if self.host_name_suffix is not None:
            result['HostNameSuffix'] = self.host_name_suffix
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_owner_alias is not None:
            result['ImageOwnerAlias'] = self.image_owner_alias
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.internet_max_band_width_in is not None:
            result['InternetMaxBandWidthIn'] = self.internet_max_band_width_in
        if self.internet_max_band_width_out is not None:
            result['InternetMaxBandWidthOut'] = self.internet_max_band_width_out
        if self.job_queue is not None:
            result['JobQueue'] = self.job_queue
        if self.min_count is not None:
            result['MinCount'] = self.min_count
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.sync is not None:
            result['Sync'] = self.sync
        if self.system_disk_level is not None:
            result['SystemDiskLevel'] = self.system_disk_level
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        if self.system_disk_type is not None:
            result['SystemDiskType'] = self.system_disk_type
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocatePublicAddress') is not None:
            self.allocate_public_address = m.get('AllocatePublicAddress')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ComputeEnableHt') is not None:
            self.compute_enable_ht = m.get('ComputeEnableHt')
        if m.get('ComputeSpotPriceLimit') is not None:
            self.compute_spot_price_limit = m.get('ComputeSpotPriceLimit')
        if m.get('ComputeSpotStrategy') is not None:
            self.compute_spot_strategy = m.get('ComputeSpotStrategy')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('CreateMode') is not None:
            self.create_mode = m.get('CreateMode')
        self.data_disks = []
        if m.get('DataDisks') is not None:
            for k in m.get('DataDisks'):
                temp_model = AddNodesRequestDataDisks()
                self.data_disks.append(temp_model.from_map(k))
        if m.get('EcsChargeType') is not None:
            self.ecs_charge_type = m.get('EcsChargeType')
        if m.get('HostNamePrefix') is not None:
            self.host_name_prefix = m.get('HostNamePrefix')
        if m.get('HostNameSuffix') is not None:
            self.host_name_suffix = m.get('HostNameSuffix')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageOwnerAlias') is not None:
            self.image_owner_alias = m.get('ImageOwnerAlias')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('InternetMaxBandWidthIn') is not None:
            self.internet_max_band_width_in = m.get('InternetMaxBandWidthIn')
        if m.get('InternetMaxBandWidthOut') is not None:
            self.internet_max_band_width_out = m.get('InternetMaxBandWidthOut')
        if m.get('JobQueue') is not None:
            self.job_queue = m.get('JobQueue')
        if m.get('MinCount') is not None:
            self.min_count = m.get('MinCount')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('Sync') is not None:
            self.sync = m.get('Sync')
        if m.get('SystemDiskLevel') is not None:
            self.system_disk_level = m.get('SystemDiskLevel')
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        if m.get('SystemDiskType') is not None:
            self.system_disk_type = m.get('SystemDiskType')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class AddNodesResponseBodyInstanceIds(TeaModel):
    def __init__(
        self,
        instance_id: List[str] = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class AddNodesResponseBody(TeaModel):
    def __init__(
        self,
        instance_ids: AddNodesResponseBodyInstanceIds = None,
        request_id: str = None,
        task_id: str = None,
    ):
        self.instance_ids = instance_ids
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        if self.instance_ids:
            self.instance_ids.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            temp_model = AddNodesResponseBodyInstanceIds()
            self.instance_ids = temp_model.from_map(m['InstanceIds'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class AddNodesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddNodesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = AddNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddQueueRequest(TeaModel):
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


class AddQueueResponseBody(TeaModel):
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


class AddQueueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddQueueResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = AddQueueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddSecurityGroupRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        cluster_id: str = None,
        security_group_id: str = None,
    ):
        self.client_token = client_token
        self.cluster_id = cluster_id
        self.security_group_id = security_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        return self


class AddSecurityGroupResponseBody(TeaModel):
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


class AddSecurityGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddSecurityGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = AddSecurityGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddUsersRequestUser(TeaModel):
    def __init__(
        self,
        group: str = None,
        name: str = None,
        password: str = None,
    ):
        self.group = group
        self.name = name
        self.password = password

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group is not None:
            result['Group'] = self.group
        if self.name is not None:
            result['Name'] = self.name
        if self.password is not None:
            result['Password'] = self.password
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        return self


class AddUsersRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        user: List[AddUsersRequestUser] = None,
    ):
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
                temp_model = AddUsersRequestUser()
                self.user.append(temp_model.from_map(k))
        return self


class AddUsersResponseBody(TeaModel):
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


class AddUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddUsersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = AddUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApplyNodesRequestInstanceTypeModel(TeaModel):
    def __init__(
        self,
        instance_type: str = None,
        max_price: float = None,
        target_image_id: str = None,
    ):
        self.instance_type = instance_type
        self.max_price = max_price
        self.target_image_id = target_image_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.max_price is not None:
            result['MaxPrice'] = self.max_price
        if self.target_image_id is not None:
            result['TargetImageId'] = self.target_image_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('MaxPrice') is not None:
            self.max_price = m.get('MaxPrice')
        if m.get('TargetImageId') is not None:
            self.target_image_id = m.get('TargetImageId')
        return self


class ApplyNodesRequestTag(TeaModel):
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


class ApplyNodesRequestZoneInfos(TeaModel):
    def __init__(
        self,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        self.v_switch_id = v_switch_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ApplyNodesRequest(TeaModel):
    def __init__(
        self,
        allocate_public_address: bool = None,
        cluster_id: str = None,
        compute_spot_price_limit: float = None,
        compute_spot_strategy: str = None,
        cores: int = None,
        host_name_prefix: str = None,
        host_name_suffix: str = None,
        image_id: str = None,
        instance_family_level: str = None,
        instance_type_model: List[ApplyNodesRequestInstanceTypeModel] = None,
        internet_charge_type: str = None,
        internet_max_band_width_in: int = None,
        internet_max_band_width_out: int = None,
        interval: int = None,
        job_queue: str = None,
        memory: int = None,
        priority_strategy: str = None,
        resource_amount_type: str = None,
        round: int = None,
        strict_resource_provision: bool = None,
        strict_satisfied_target_capacity: bool = None,
        system_disk_level: str = None,
        system_disk_size: int = None,
        system_disk_type: str = None,
        tag: List[ApplyNodesRequestTag] = None,
        target_capacity: int = None,
        zone_infos: List[ApplyNodesRequestZoneInfos] = None,
    ):
        self.allocate_public_address = allocate_public_address
        self.cluster_id = cluster_id
        self.compute_spot_price_limit = compute_spot_price_limit
        self.compute_spot_strategy = compute_spot_strategy
        self.cores = cores
        self.host_name_prefix = host_name_prefix
        self.host_name_suffix = host_name_suffix
        self.image_id = image_id
        self.instance_family_level = instance_family_level
        self.instance_type_model = instance_type_model
        self.internet_charge_type = internet_charge_type
        self.internet_max_band_width_in = internet_max_band_width_in
        self.internet_max_band_width_out = internet_max_band_width_out
        self.interval = interval
        self.job_queue = job_queue
        self.memory = memory
        self.priority_strategy = priority_strategy
        self.resource_amount_type = resource_amount_type
        self.round = round
        self.strict_resource_provision = strict_resource_provision
        self.strict_satisfied_target_capacity = strict_satisfied_target_capacity
        self.system_disk_level = system_disk_level
        self.system_disk_size = system_disk_size
        self.system_disk_type = system_disk_type
        self.tag = tag
        self.target_capacity = target_capacity
        self.zone_infos = zone_infos

    def validate(self):
        if self.instance_type_model:
            for k in self.instance_type_model:
                if k:
                    k.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()
        if self.zone_infos:
            for k in self.zone_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allocate_public_address is not None:
            result['AllocatePublicAddress'] = self.allocate_public_address
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.compute_spot_price_limit is not None:
            result['ComputeSpotPriceLimit'] = self.compute_spot_price_limit
        if self.compute_spot_strategy is not None:
            result['ComputeSpotStrategy'] = self.compute_spot_strategy
        if self.cores is not None:
            result['Cores'] = self.cores
        if self.host_name_prefix is not None:
            result['HostNamePrefix'] = self.host_name_prefix
        if self.host_name_suffix is not None:
            result['HostNameSuffix'] = self.host_name_suffix
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.instance_family_level is not None:
            result['InstanceFamilyLevel'] = self.instance_family_level
        result['InstanceTypeModel'] = []
        if self.instance_type_model is not None:
            for k in self.instance_type_model:
                result['InstanceTypeModel'].append(k.to_map() if k else None)
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.internet_max_band_width_in is not None:
            result['InternetMaxBandWidthIn'] = self.internet_max_band_width_in
        if self.internet_max_band_width_out is not None:
            result['InternetMaxBandWidthOut'] = self.internet_max_band_width_out
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.job_queue is not None:
            result['JobQueue'] = self.job_queue
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.priority_strategy is not None:
            result['PriorityStrategy'] = self.priority_strategy
        if self.resource_amount_type is not None:
            result['ResourceAmountType'] = self.resource_amount_type
        if self.round is not None:
            result['Round'] = self.round
        if self.strict_resource_provision is not None:
            result['StrictResourceProvision'] = self.strict_resource_provision
        if self.strict_satisfied_target_capacity is not None:
            result['StrictSatisfiedTargetCapacity'] = self.strict_satisfied_target_capacity
        if self.system_disk_level is not None:
            result['SystemDiskLevel'] = self.system_disk_level
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        if self.system_disk_type is not None:
            result['SystemDiskType'] = self.system_disk_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.target_capacity is not None:
            result['TargetCapacity'] = self.target_capacity
        result['ZoneInfos'] = []
        if self.zone_infos is not None:
            for k in self.zone_infos:
                result['ZoneInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocatePublicAddress') is not None:
            self.allocate_public_address = m.get('AllocatePublicAddress')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ComputeSpotPriceLimit') is not None:
            self.compute_spot_price_limit = m.get('ComputeSpotPriceLimit')
        if m.get('ComputeSpotStrategy') is not None:
            self.compute_spot_strategy = m.get('ComputeSpotStrategy')
        if m.get('Cores') is not None:
            self.cores = m.get('Cores')
        if m.get('HostNamePrefix') is not None:
            self.host_name_prefix = m.get('HostNamePrefix')
        if m.get('HostNameSuffix') is not None:
            self.host_name_suffix = m.get('HostNameSuffix')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('InstanceFamilyLevel') is not None:
            self.instance_family_level = m.get('InstanceFamilyLevel')
        self.instance_type_model = []
        if m.get('InstanceTypeModel') is not None:
            for k in m.get('InstanceTypeModel'):
                temp_model = ApplyNodesRequestInstanceTypeModel()
                self.instance_type_model.append(temp_model.from_map(k))
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('InternetMaxBandWidthIn') is not None:
            self.internet_max_band_width_in = m.get('InternetMaxBandWidthIn')
        if m.get('InternetMaxBandWidthOut') is not None:
            self.internet_max_band_width_out = m.get('InternetMaxBandWidthOut')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('JobQueue') is not None:
            self.job_queue = m.get('JobQueue')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('PriorityStrategy') is not None:
            self.priority_strategy = m.get('PriorityStrategy')
        if m.get('ResourceAmountType') is not None:
            self.resource_amount_type = m.get('ResourceAmountType')
        if m.get('Round') is not None:
            self.round = m.get('Round')
        if m.get('StrictResourceProvision') is not None:
            self.strict_resource_provision = m.get('StrictResourceProvision')
        if m.get('StrictSatisfiedTargetCapacity') is not None:
            self.strict_satisfied_target_capacity = m.get('StrictSatisfiedTargetCapacity')
        if m.get('SystemDiskLevel') is not None:
            self.system_disk_level = m.get('SystemDiskLevel')
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        if m.get('SystemDiskType') is not None:
            self.system_disk_type = m.get('SystemDiskType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ApplyNodesRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('TargetCapacity') is not None:
            self.target_capacity = m.get('TargetCapacity')
        self.zone_infos = []
        if m.get('ZoneInfos') is not None:
            for k in m.get('ZoneInfos'):
                temp_model = ApplyNodesRequestZoneInfos()
                self.zone_infos.append(temp_model.from_map(k))
        return self


class ApplyNodesResponseBodyInstanceIds(TeaModel):
    def __init__(
        self,
        instance_id: List[str] = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ApplyNodesResponseBody(TeaModel):
    def __init__(
        self,
        detail: str = None,
        instance_ids: ApplyNodesResponseBodyInstanceIds = None,
        request_id: str = None,
        satisfied_amount: int = None,
        task_id: str = None,
    ):
        self.detail = detail
        self.instance_ids = instance_ids
        self.request_id = request_id
        self.satisfied_amount = satisfied_amount
        self.task_id = task_id

    def validate(self):
        if self.instance_ids:
            self.instance_ids.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.satisfied_amount is not None:
            result['SatisfiedAmount'] = self.satisfied_amount
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('InstanceIds') is not None:
            temp_model = ApplyNodesResponseBodyInstanceIds()
            self.instance_ids = temp_model.from_map(m['InstanceIds'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SatisfiedAmount') is not None:
            self.satisfied_amount = m.get('SatisfiedAmount')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ApplyNodesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ApplyNodesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ApplyNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateClusterRequestEcsOrderCompute(TeaModel):
    def __init__(
        self,
        count: int = None,
        instance_type: str = None,
    ):
        self.count = count
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class CreateClusterRequestEcsOrderLogin(TeaModel):
    def __init__(
        self,
        count: int = None,
        instance_type: str = None,
    ):
        self.count = count
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class CreateClusterRequestEcsOrderManager(TeaModel):
    def __init__(
        self,
        count: int = None,
        instance_type: str = None,
    ):
        self.count = count
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class CreateClusterRequestEcsOrder(TeaModel):
    def __init__(
        self,
        compute: CreateClusterRequestEcsOrderCompute = None,
        login: CreateClusterRequestEcsOrderLogin = None,
        manager: CreateClusterRequestEcsOrderManager = None,
    ):
        self.compute = compute
        self.login = login
        self.manager = manager

    def validate(self):
        self.validate_required(self.compute, 'compute')
        if self.compute:
            self.compute.validate()
        self.validate_required(self.login, 'login')
        if self.login:
            self.login.validate()
        self.validate_required(self.manager, 'manager')
        if self.manager:
            self.manager.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compute is not None:
            result['Compute'] = self.compute.to_map()
        if self.login is not None:
            result['Login'] = self.login.to_map()
        if self.manager is not None:
            result['Manager'] = self.manager.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Compute') is not None:
            temp_model = CreateClusterRequestEcsOrderCompute()
            self.compute = temp_model.from_map(m['Compute'])
        if m.get('Login') is not None:
            temp_model = CreateClusterRequestEcsOrderLogin()
            self.login = temp_model.from_map(m['Login'])
        if m.get('Manager') is not None:
            temp_model = CreateClusterRequestEcsOrderManager()
            self.manager = temp_model.from_map(m['Manager'])
        return self


class CreateClusterRequestAdditionalVolumesRoles(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateClusterRequestAdditionalVolumes(TeaModel):
    def __init__(
        self,
        job_queue: str = None,
        local_directory: str = None,
        location: str = None,
        remote_directory: str = None,
        roles: List[CreateClusterRequestAdditionalVolumesRoles] = None,
        volume_id: str = None,
        volume_mount_option: str = None,
        volume_mountpoint: str = None,
        volume_protocol: str = None,
        volume_type: str = None,
    ):
        self.job_queue = job_queue
        self.local_directory = local_directory
        self.location = location
        self.remote_directory = remote_directory
        self.roles = roles
        self.volume_id = volume_id
        self.volume_mount_option = volume_mount_option
        self.volume_mountpoint = volume_mountpoint
        self.volume_protocol = volume_protocol
        self.volume_type = volume_type

    def validate(self):
        if self.roles:
            for k in self.roles:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_queue is not None:
            result['JobQueue'] = self.job_queue
        if self.local_directory is not None:
            result['LocalDirectory'] = self.local_directory
        if self.location is not None:
            result['Location'] = self.location
        if self.remote_directory is not None:
            result['RemoteDirectory'] = self.remote_directory
        result['Roles'] = []
        if self.roles is not None:
            for k in self.roles:
                result['Roles'].append(k.to_map() if k else None)
        if self.volume_id is not None:
            result['VolumeId'] = self.volume_id
        if self.volume_mount_option is not None:
            result['VolumeMountOption'] = self.volume_mount_option
        if self.volume_mountpoint is not None:
            result['VolumeMountpoint'] = self.volume_mountpoint
        if self.volume_protocol is not None:
            result['VolumeProtocol'] = self.volume_protocol
        if self.volume_type is not None:
            result['VolumeType'] = self.volume_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobQueue') is not None:
            self.job_queue = m.get('JobQueue')
        if m.get('LocalDirectory') is not None:
            self.local_directory = m.get('LocalDirectory')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('RemoteDirectory') is not None:
            self.remote_directory = m.get('RemoteDirectory')
        self.roles = []
        if m.get('Roles') is not None:
            for k in m.get('Roles'):
                temp_model = CreateClusterRequestAdditionalVolumesRoles()
                self.roles.append(temp_model.from_map(k))
        if m.get('VolumeId') is not None:
            self.volume_id = m.get('VolumeId')
        if m.get('VolumeMountOption') is not None:
            self.volume_mount_option = m.get('VolumeMountOption')
        if m.get('VolumeMountpoint') is not None:
            self.volume_mountpoint = m.get('VolumeMountpoint')
        if m.get('VolumeProtocol') is not None:
            self.volume_protocol = m.get('VolumeProtocol')
        if m.get('VolumeType') is not None:
            self.volume_type = m.get('VolumeType')
        return self


class CreateClusterRequestApplication(TeaModel):
    def __init__(
        self,
        tag: str = None,
    ):
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class CreateClusterRequestPostInstallScript(TeaModel):
    def __init__(
        self,
        args: str = None,
        url: str = None,
    ):
        self.args = args
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.args is not None:
            result['Args'] = self.args
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Args') is not None:
            self.args = m.get('Args')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class CreateClusterRequestTag(TeaModel):
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
        ecs_order: CreateClusterRequestEcsOrder = None,
        account_type: str = None,
        additional_volumes: List[CreateClusterRequestAdditionalVolumes] = None,
        application: List[CreateClusterRequestApplication] = None,
        auto_renew: str = None,
        auto_renew_period: int = None,
        client_token: str = None,
        client_version: str = None,
        cluster_version: str = None,
        compute_enable_ht: bool = None,
        compute_spot_price_limit: str = None,
        compute_spot_strategy: str = None,
        deploy_mode: str = None,
        description: str = None,
        domain: str = None,
        ecs_charge_type: str = None,
        ehpc_version: str = None,
        ha_enable: bool = None,
        image_id: str = None,
        image_owner_alias: str = None,
        input_file_url: str = None,
        is_compute_ess: bool = None,
        job_queue: str = None,
        key_pair_name: str = None,
        name: str = None,
        os_tag: str = None,
        password: str = None,
        period: int = None,
        period_unit: str = None,
        plugin: str = None,
        post_install_script: List[CreateClusterRequestPostInstallScript] = None,
        ram_node_types: List[str] = None,
        ram_role_name: str = None,
        remote_directory: str = None,
        remote_vis_enable: str = None,
        resource_group_id: str = None,
        scc_cluster_id: str = None,
        scheduler_type: str = None,
        security_group_id: str = None,
        security_group_name: str = None,
        system_disk_level: str = None,
        system_disk_size: int = None,
        system_disk_type: str = None,
        tag: List[CreateClusterRequestTag] = None,
        v_switch_id: str = None,
        volume_id: str = None,
        volume_mount_option: str = None,
        volume_mountpoint: str = None,
        volume_protocol: str = None,
        volume_type: str = None,
        vpc_id: str = None,
        without_agent: bool = None,
        without_elastic_ip: bool = None,
        zone_id: str = None,
    ):
        self.ecs_order = ecs_order
        self.account_type = account_type
        self.additional_volumes = additional_volumes
        self.application = application
        self.auto_renew = auto_renew
        self.auto_renew_period = auto_renew_period
        self.client_token = client_token
        self.client_version = client_version
        self.cluster_version = cluster_version
        self.compute_enable_ht = compute_enable_ht
        self.compute_spot_price_limit = compute_spot_price_limit
        self.compute_spot_strategy = compute_spot_strategy
        self.deploy_mode = deploy_mode
        self.description = description
        self.domain = domain
        self.ecs_charge_type = ecs_charge_type
        self.ehpc_version = ehpc_version
        self.ha_enable = ha_enable
        self.image_id = image_id
        self.image_owner_alias = image_owner_alias
        self.input_file_url = input_file_url
        self.is_compute_ess = is_compute_ess
        self.job_queue = job_queue
        self.key_pair_name = key_pair_name
        self.name = name
        self.os_tag = os_tag
        self.password = password
        self.period = period
        self.period_unit = period_unit
        self.plugin = plugin
        self.post_install_script = post_install_script
        self.ram_node_types = ram_node_types
        self.ram_role_name = ram_role_name
        self.remote_directory = remote_directory
        self.remote_vis_enable = remote_vis_enable
        self.resource_group_id = resource_group_id
        self.scc_cluster_id = scc_cluster_id
        self.scheduler_type = scheduler_type
        self.security_group_id = security_group_id
        self.security_group_name = security_group_name
        self.system_disk_level = system_disk_level
        self.system_disk_size = system_disk_size
        self.system_disk_type = system_disk_type
        self.tag = tag
        self.v_switch_id = v_switch_id
        self.volume_id = volume_id
        self.volume_mount_option = volume_mount_option
        self.volume_mountpoint = volume_mountpoint
        self.volume_protocol = volume_protocol
        self.volume_type = volume_type
        self.vpc_id = vpc_id
        self.without_agent = without_agent
        self.without_elastic_ip = without_elastic_ip
        self.zone_id = zone_id

    def validate(self):
        if self.ecs_order:
            self.ecs_order.validate()
        if self.additional_volumes:
            for k in self.additional_volumes:
                if k:
                    k.validate()
        if self.application:
            for k in self.application:
                if k:
                    k.validate()
        if self.post_install_script:
            for k in self.post_install_script:
                if k:
                    k.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ecs_order is not None:
            result['EcsOrder'] = self.ecs_order.to_map()
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        result['AdditionalVolumes'] = []
        if self.additional_volumes is not None:
            for k in self.additional_volumes:
                result['AdditionalVolumes'].append(k.to_map() if k else None)
        result['Application'] = []
        if self.application is not None:
            for k in self.application:
                result['Application'].append(k.to_map() if k else None)
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.cluster_version is not None:
            result['ClusterVersion'] = self.cluster_version
        if self.compute_enable_ht is not None:
            result['ComputeEnableHt'] = self.compute_enable_ht
        if self.compute_spot_price_limit is not None:
            result['ComputeSpotPriceLimit'] = self.compute_spot_price_limit
        if self.compute_spot_strategy is not None:
            result['ComputeSpotStrategy'] = self.compute_spot_strategy
        if self.deploy_mode is not None:
            result['DeployMode'] = self.deploy_mode
        if self.description is not None:
            result['Description'] = self.description
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.ecs_charge_type is not None:
            result['EcsChargeType'] = self.ecs_charge_type
        if self.ehpc_version is not None:
            result['EhpcVersion'] = self.ehpc_version
        if self.ha_enable is not None:
            result['HaEnable'] = self.ha_enable
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_owner_alias is not None:
            result['ImageOwnerAlias'] = self.image_owner_alias
        if self.input_file_url is not None:
            result['InputFileUrl'] = self.input_file_url
        if self.is_compute_ess is not None:
            result['IsComputeEss'] = self.is_compute_ess
        if self.job_queue is not None:
            result['JobQueue'] = self.job_queue
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.name is not None:
            result['Name'] = self.name
        if self.os_tag is not None:
            result['OsTag'] = self.os_tag
        if self.password is not None:
            result['Password'] = self.password
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.plugin is not None:
            result['Plugin'] = self.plugin
        result['PostInstallScript'] = []
        if self.post_install_script is not None:
            for k in self.post_install_script:
                result['PostInstallScript'].append(k.to_map() if k else None)
        if self.ram_node_types is not None:
            result['RamNodeTypes'] = self.ram_node_types
        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name
        if self.remote_directory is not None:
            result['RemoteDirectory'] = self.remote_directory
        if self.remote_vis_enable is not None:
            result['RemoteVisEnable'] = self.remote_vis_enable
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.scc_cluster_id is not None:
            result['SccClusterId'] = self.scc_cluster_id
        if self.scheduler_type is not None:
            result['SchedulerType'] = self.scheduler_type
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.security_group_name is not None:
            result['SecurityGroupName'] = self.security_group_name
        if self.system_disk_level is not None:
            result['SystemDiskLevel'] = self.system_disk_level
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        if self.system_disk_type is not None:
            result['SystemDiskType'] = self.system_disk_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.volume_id is not None:
            result['VolumeId'] = self.volume_id
        if self.volume_mount_option is not None:
            result['VolumeMountOption'] = self.volume_mount_option
        if self.volume_mountpoint is not None:
            result['VolumeMountpoint'] = self.volume_mountpoint
        if self.volume_protocol is not None:
            result['VolumeProtocol'] = self.volume_protocol
        if self.volume_type is not None:
            result['VolumeType'] = self.volume_type
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.without_agent is not None:
            result['WithoutAgent'] = self.without_agent
        if self.without_elastic_ip is not None:
            result['WithoutElasticIp'] = self.without_elastic_ip
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EcsOrder') is not None:
            temp_model = CreateClusterRequestEcsOrder()
            self.ecs_order = temp_model.from_map(m['EcsOrder'])
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        self.additional_volumes = []
        if m.get('AdditionalVolumes') is not None:
            for k in m.get('AdditionalVolumes'):
                temp_model = CreateClusterRequestAdditionalVolumes()
                self.additional_volumes.append(temp_model.from_map(k))
        self.application = []
        if m.get('Application') is not None:
            for k in m.get('Application'):
                temp_model = CreateClusterRequestApplication()
                self.application.append(temp_model.from_map(k))
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('ClusterVersion') is not None:
            self.cluster_version = m.get('ClusterVersion')
        if m.get('ComputeEnableHt') is not None:
            self.compute_enable_ht = m.get('ComputeEnableHt')
        if m.get('ComputeSpotPriceLimit') is not None:
            self.compute_spot_price_limit = m.get('ComputeSpotPriceLimit')
        if m.get('ComputeSpotStrategy') is not None:
            self.compute_spot_strategy = m.get('ComputeSpotStrategy')
        if m.get('DeployMode') is not None:
            self.deploy_mode = m.get('DeployMode')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('EcsChargeType') is not None:
            self.ecs_charge_type = m.get('EcsChargeType')
        if m.get('EhpcVersion') is not None:
            self.ehpc_version = m.get('EhpcVersion')
        if m.get('HaEnable') is not None:
            self.ha_enable = m.get('HaEnable')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageOwnerAlias') is not None:
            self.image_owner_alias = m.get('ImageOwnerAlias')
        if m.get('InputFileUrl') is not None:
            self.input_file_url = m.get('InputFileUrl')
        if m.get('IsComputeEss') is not None:
            self.is_compute_ess = m.get('IsComputeEss')
        if m.get('JobQueue') is not None:
            self.job_queue = m.get('JobQueue')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OsTag') is not None:
            self.os_tag = m.get('OsTag')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('Plugin') is not None:
            self.plugin = m.get('Plugin')
        self.post_install_script = []
        if m.get('PostInstallScript') is not None:
            for k in m.get('PostInstallScript'):
                temp_model = CreateClusterRequestPostInstallScript()
                self.post_install_script.append(temp_model.from_map(k))
        if m.get('RamNodeTypes') is not None:
            self.ram_node_types = m.get('RamNodeTypes')
        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')
        if m.get('RemoteDirectory') is not None:
            self.remote_directory = m.get('RemoteDirectory')
        if m.get('RemoteVisEnable') is not None:
            self.remote_vis_enable = m.get('RemoteVisEnable')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SccClusterId') is not None:
            self.scc_cluster_id = m.get('SccClusterId')
        if m.get('SchedulerType') is not None:
            self.scheduler_type = m.get('SchedulerType')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('SecurityGroupName') is not None:
            self.security_group_name = m.get('SecurityGroupName')
        if m.get('SystemDiskLevel') is not None:
            self.system_disk_level = m.get('SystemDiskLevel')
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        if m.get('SystemDiskType') is not None:
            self.system_disk_type = m.get('SystemDiskType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateClusterRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VolumeId') is not None:
            self.volume_id = m.get('VolumeId')
        if m.get('VolumeMountOption') is not None:
            self.volume_mount_option = m.get('VolumeMountOption')
        if m.get('VolumeMountpoint') is not None:
            self.volume_mountpoint = m.get('VolumeMountpoint')
        if m.get('VolumeProtocol') is not None:
            self.volume_protocol = m.get('VolumeProtocol')
        if m.get('VolumeType') is not None:
            self.volume_type = m.get('VolumeType')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('WithoutAgent') is not None:
            self.without_agent = m.get('WithoutAgent')
        if m.get('WithoutElasticIp') is not None:
            self.without_elastic_ip = m.get('WithoutElasticIp')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateClusterResponseBody(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.request_id = request_id
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
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class CreateGWSClusterRequest(TeaModel):
    def __init__(
        self,
        cluster_type: str = None,
        name: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        self.cluster_type = cluster_type
        self.name = name
        self.v_switch_id = v_switch_id
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.name is not None:
            result['Name'] = self.name
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class CreateGWSClusterResponseBody(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        request_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateGWSClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateGWSClusterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateGWSClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGWSImageRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        name: str = None,
    ):
        self.instance_id = instance_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateGWSImageResponseBody(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        request_id: str = None,
    ):
        self.image_id = image_id
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateGWSImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateGWSImageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateGWSImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGWSInstanceRequest(TeaModel):
    def __init__(
        self,
        allocate_public_address: bool = None,
        app_list: str = None,
        auto_renew: bool = None,
        cluster_id: str = None,
        image_id: str = None,
        instance_charge_type: str = None,
        instance_type: str = None,
        internet_charge_type: str = None,
        internet_max_bandwidth_in: int = None,
        internet_max_bandwidth_out: int = None,
        name: str = None,
        period: str = None,
        period_unit: str = None,
        system_disk_category: str = None,
        system_disk_size: int = None,
        v_switch_id: str = None,
        work_mode: str = None,
    ):
        self.allocate_public_address = allocate_public_address
        self.app_list = app_list
        self.auto_renew = auto_renew
        self.cluster_id = cluster_id
        self.image_id = image_id
        self.instance_charge_type = instance_charge_type
        self.instance_type = instance_type
        self.internet_charge_type = internet_charge_type
        self.internet_max_bandwidth_in = internet_max_bandwidth_in
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        self.name = name
        self.period = period
        self.period_unit = period_unit
        self.system_disk_category = system_disk_category
        self.system_disk_size = system_disk_size
        self.v_switch_id = v_switch_id
        self.work_mode = work_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allocate_public_address is not None:
            result['AllocatePublicAddress'] = self.allocate_public_address
        if self.app_list is not None:
            result['AppList'] = self.app_list
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.internet_max_bandwidth_in is not None:
            result['InternetMaxBandwidthIn'] = self.internet_max_bandwidth_in
        if self.internet_max_bandwidth_out is not None:
            result['InternetMaxBandwidthOut'] = self.internet_max_bandwidth_out
        if self.name is not None:
            result['Name'] = self.name
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.system_disk_category is not None:
            result['SystemDiskCategory'] = self.system_disk_category
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.work_mode is not None:
            result['WorkMode'] = self.work_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocatePublicAddress') is not None:
            self.allocate_public_address = m.get('AllocatePublicAddress')
        if m.get('AppList') is not None:
            self.app_list = m.get('AppList')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('InternetMaxBandwidthIn') is not None:
            self.internet_max_bandwidth_in = m.get('InternetMaxBandwidthIn')
        if m.get('InternetMaxBandwidthOut') is not None:
            self.internet_max_bandwidth_out = m.get('InternetMaxBandwidthOut')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('SystemDiskCategory') is not None:
            self.system_disk_category = m.get('SystemDiskCategory')
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('WorkMode') is not None:
            self.work_mode = m.get('WorkMode')
        return self


class CreateGWSInstanceResponseBody(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        request_id: str = None,
    ):
        self.instance_id = instance_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateGWSInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateGWSInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateGWSInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateHybridClusterRequestEcsOrderCompute(TeaModel):
    def __init__(
        self,
        instance_type: str = None,
    ):
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class CreateHybridClusterRequestEcsOrderManager(TeaModel):
    def __init__(
        self,
        instance_type: str = None,
    ):
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class CreateHybridClusterRequestEcsOrder(TeaModel):
    def __init__(
        self,
        compute: CreateHybridClusterRequestEcsOrderCompute = None,
        manager: CreateHybridClusterRequestEcsOrderManager = None,
    ):
        self.compute = compute
        self.manager = manager

    def validate(self):
        self.validate_required(self.compute, 'compute')
        if self.compute:
            self.compute.validate()
        self.validate_required(self.manager, 'manager')
        if self.manager:
            self.manager.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compute is not None:
            result['Compute'] = self.compute.to_map()
        if self.manager is not None:
            result['Manager'] = self.manager.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Compute') is not None:
            temp_model = CreateHybridClusterRequestEcsOrderCompute()
            self.compute = temp_model.from_map(m['Compute'])
        if m.get('Manager') is not None:
            temp_model = CreateHybridClusterRequestEcsOrderManager()
            self.manager = temp_model.from_map(m['Manager'])
        return self


class CreateHybridClusterRequestApplication(TeaModel):
    def __init__(
        self,
        tag: str = None,
    ):
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class CreateHybridClusterRequestNodes(TeaModel):
    def __init__(
        self,
        account_type: str = None,
        dir: str = None,
        host_name: str = None,
        ip_address: str = None,
        role: str = None,
        scheduler_type: str = None,
    ):
        self.account_type = account_type
        self.dir = dir
        self.host_name = host_name
        self.ip_address = ip_address
        self.role = role
        self.scheduler_type = scheduler_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address
        if self.role is not None:
            result['Role'] = self.role
        if self.scheduler_type is not None:
            result['SchedulerType'] = self.scheduler_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('SchedulerType') is not None:
            self.scheduler_type = m.get('SchedulerType')
        return self


class CreateHybridClusterRequestOpenldapPar(TeaModel):
    def __init__(
        self,
        base_dn: str = None,
        ldap_server_ip: str = None,
    ):
        self.base_dn = base_dn
        self.ldap_server_ip = ldap_server_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_dn is not None:
            result['BaseDn'] = self.base_dn
        if self.ldap_server_ip is not None:
            result['LdapServerIp'] = self.ldap_server_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseDn') is not None:
            self.base_dn = m.get('BaseDn')
        if m.get('LdapServerIp') is not None:
            self.ldap_server_ip = m.get('LdapServerIp')
        return self


class CreateHybridClusterRequestPostInstallScript(TeaModel):
    def __init__(
        self,
        args: str = None,
        url: str = None,
    ):
        self.args = args
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.args is not None:
            result['Args'] = self.args
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Args') is not None:
            self.args = m.get('Args')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class CreateHybridClusterRequestWinAdPar(TeaModel):
    def __init__(
        self,
        ad_dc: str = None,
        ad_ip: str = None,
        ad_user: str = None,
        ad_user_passwd: str = None,
    ):
        self.ad_dc = ad_dc
        self.ad_ip = ad_ip
        self.ad_user = ad_user
        self.ad_user_passwd = ad_user_passwd

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ad_dc is not None:
            result['AdDc'] = self.ad_dc
        if self.ad_ip is not None:
            result['AdIp'] = self.ad_ip
        if self.ad_user is not None:
            result['AdUser'] = self.ad_user
        if self.ad_user_passwd is not None:
            result['AdUserPasswd'] = self.ad_user_passwd
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdDc') is not None:
            self.ad_dc = m.get('AdDc')
        if m.get('AdIp') is not None:
            self.ad_ip = m.get('AdIp')
        if m.get('AdUser') is not None:
            self.ad_user = m.get('AdUser')
        if m.get('AdUserPasswd') is not None:
            self.ad_user_passwd = m.get('AdUserPasswd')
        return self


class CreateHybridClusterRequest(TeaModel):
    def __init__(
        self,
        ecs_order: CreateHybridClusterRequestEcsOrder = None,
        application: List[CreateHybridClusterRequestApplication] = None,
        client_token: str = None,
        client_version: str = None,
        compute_spot_price_limit: float = None,
        compute_spot_strategy: str = None,
        description: str = None,
        domain: str = None,
        ehpc_version: str = None,
        image_id: str = None,
        image_owner_alias: str = None,
        job_queue: str = None,
        key_pair_name: str = None,
        location: str = None,
        multi_os: bool = None,
        name: str = None,
        nodes: List[CreateHybridClusterRequestNodes] = None,
        on_premise_volume_local_path: str = None,
        on_premise_volume_mount_point: str = None,
        on_premise_volume_protocol: str = None,
        on_premise_volume_remote_path: str = None,
        openldap_par: CreateHybridClusterRequestOpenldapPar = None,
        os_tag: str = None,
        password: str = None,
        plugin: str = None,
        post_install_script: List[CreateHybridClusterRequestPostInstallScript] = None,
        remote_directory: str = None,
        resource_group_id: str = None,
        scheduler_pre_install: bool = None,
        security_group_id: str = None,
        security_group_name: str = None,
        v_switch_id: str = None,
        volume_id: str = None,
        volume_mountpoint: str = None,
        volume_protocol: str = None,
        volume_type: str = None,
        vpc_id: str = None,
        win_ad_par: CreateHybridClusterRequestWinAdPar = None,
        zone_id: str = None,
    ):
        self.ecs_order = ecs_order
        self.application = application
        self.client_token = client_token
        self.client_version = client_version
        self.compute_spot_price_limit = compute_spot_price_limit
        self.compute_spot_strategy = compute_spot_strategy
        self.description = description
        self.domain = domain
        self.ehpc_version = ehpc_version
        self.image_id = image_id
        self.image_owner_alias = image_owner_alias
        self.job_queue = job_queue
        self.key_pair_name = key_pair_name
        self.location = location
        self.multi_os = multi_os
        self.name = name
        self.nodes = nodes
        self.on_premise_volume_local_path = on_premise_volume_local_path
        self.on_premise_volume_mount_point = on_premise_volume_mount_point
        self.on_premise_volume_protocol = on_premise_volume_protocol
        self.on_premise_volume_remote_path = on_premise_volume_remote_path
        self.openldap_par = openldap_par
        self.os_tag = os_tag
        self.password = password
        self.plugin = plugin
        self.post_install_script = post_install_script
        self.remote_directory = remote_directory
        self.resource_group_id = resource_group_id
        self.scheduler_pre_install = scheduler_pre_install
        self.security_group_id = security_group_id
        self.security_group_name = security_group_name
        self.v_switch_id = v_switch_id
        self.volume_id = volume_id
        self.volume_mountpoint = volume_mountpoint
        self.volume_protocol = volume_protocol
        self.volume_type = volume_type
        self.vpc_id = vpc_id
        self.win_ad_par = win_ad_par
        self.zone_id = zone_id

    def validate(self):
        if self.ecs_order:
            self.ecs_order.validate()
        if self.application:
            for k in self.application:
                if k:
                    k.validate()
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()
        if self.openldap_par:
            self.openldap_par.validate()
        if self.post_install_script:
            for k in self.post_install_script:
                if k:
                    k.validate()
        if self.win_ad_par:
            self.win_ad_par.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ecs_order is not None:
            result['EcsOrder'] = self.ecs_order.to_map()
        result['Application'] = []
        if self.application is not None:
            for k in self.application:
                result['Application'].append(k.to_map() if k else None)
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.compute_spot_price_limit is not None:
            result['ComputeSpotPriceLimit'] = self.compute_spot_price_limit
        if self.compute_spot_strategy is not None:
            result['ComputeSpotStrategy'] = self.compute_spot_strategy
        if self.description is not None:
            result['Description'] = self.description
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.ehpc_version is not None:
            result['EhpcVersion'] = self.ehpc_version
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_owner_alias is not None:
            result['ImageOwnerAlias'] = self.image_owner_alias
        if self.job_queue is not None:
            result['JobQueue'] = self.job_queue
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.location is not None:
            result['Location'] = self.location
        if self.multi_os is not None:
            result['MultiOs'] = self.multi_os
        if self.name is not None:
            result['Name'] = self.name
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        if self.on_premise_volume_local_path is not None:
            result['OnPremiseVolumeLocalPath'] = self.on_premise_volume_local_path
        if self.on_premise_volume_mount_point is not None:
            result['OnPremiseVolumeMountPoint'] = self.on_premise_volume_mount_point
        if self.on_premise_volume_protocol is not None:
            result['OnPremiseVolumeProtocol'] = self.on_premise_volume_protocol
        if self.on_premise_volume_remote_path is not None:
            result['OnPremiseVolumeRemotePath'] = self.on_premise_volume_remote_path
        if self.openldap_par is not None:
            result['OpenldapPar'] = self.openldap_par.to_map()
        if self.os_tag is not None:
            result['OsTag'] = self.os_tag
        if self.password is not None:
            result['Password'] = self.password
        if self.plugin is not None:
            result['Plugin'] = self.plugin
        result['PostInstallScript'] = []
        if self.post_install_script is not None:
            for k in self.post_install_script:
                result['PostInstallScript'].append(k.to_map() if k else None)
        if self.remote_directory is not None:
            result['RemoteDirectory'] = self.remote_directory
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.scheduler_pre_install is not None:
            result['SchedulerPreInstall'] = self.scheduler_pre_install
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.security_group_name is not None:
            result['SecurityGroupName'] = self.security_group_name
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.volume_id is not None:
            result['VolumeId'] = self.volume_id
        if self.volume_mountpoint is not None:
            result['VolumeMountpoint'] = self.volume_mountpoint
        if self.volume_protocol is not None:
            result['VolumeProtocol'] = self.volume_protocol
        if self.volume_type is not None:
            result['VolumeType'] = self.volume_type
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.win_ad_par is not None:
            result['WinAdPar'] = self.win_ad_par.to_map()
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EcsOrder') is not None:
            temp_model = CreateHybridClusterRequestEcsOrder()
            self.ecs_order = temp_model.from_map(m['EcsOrder'])
        self.application = []
        if m.get('Application') is not None:
            for k in m.get('Application'):
                temp_model = CreateHybridClusterRequestApplication()
                self.application.append(temp_model.from_map(k))
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('ComputeSpotPriceLimit') is not None:
            self.compute_spot_price_limit = m.get('ComputeSpotPriceLimit')
        if m.get('ComputeSpotStrategy') is not None:
            self.compute_spot_strategy = m.get('ComputeSpotStrategy')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('EhpcVersion') is not None:
            self.ehpc_version = m.get('EhpcVersion')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageOwnerAlias') is not None:
            self.image_owner_alias = m.get('ImageOwnerAlias')
        if m.get('JobQueue') is not None:
            self.job_queue = m.get('JobQueue')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('MultiOs') is not None:
            self.multi_os = m.get('MultiOs')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = CreateHybridClusterRequestNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('OnPremiseVolumeLocalPath') is not None:
            self.on_premise_volume_local_path = m.get('OnPremiseVolumeLocalPath')
        if m.get('OnPremiseVolumeMountPoint') is not None:
            self.on_premise_volume_mount_point = m.get('OnPremiseVolumeMountPoint')
        if m.get('OnPremiseVolumeProtocol') is not None:
            self.on_premise_volume_protocol = m.get('OnPremiseVolumeProtocol')
        if m.get('OnPremiseVolumeRemotePath') is not None:
            self.on_premise_volume_remote_path = m.get('OnPremiseVolumeRemotePath')
        if m.get('OpenldapPar') is not None:
            temp_model = CreateHybridClusterRequestOpenldapPar()
            self.openldap_par = temp_model.from_map(m['OpenldapPar'])
        if m.get('OsTag') is not None:
            self.os_tag = m.get('OsTag')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Plugin') is not None:
            self.plugin = m.get('Plugin')
        self.post_install_script = []
        if m.get('PostInstallScript') is not None:
            for k in m.get('PostInstallScript'):
                temp_model = CreateHybridClusterRequestPostInstallScript()
                self.post_install_script.append(temp_model.from_map(k))
        if m.get('RemoteDirectory') is not None:
            self.remote_directory = m.get('RemoteDirectory')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SchedulerPreInstall') is not None:
            self.scheduler_pre_install = m.get('SchedulerPreInstall')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('SecurityGroupName') is not None:
            self.security_group_name = m.get('SecurityGroupName')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VolumeId') is not None:
            self.volume_id = m.get('VolumeId')
        if m.get('VolumeMountpoint') is not None:
            self.volume_mountpoint = m.get('VolumeMountpoint')
        if m.get('VolumeProtocol') is not None:
            self.volume_protocol = m.get('VolumeProtocol')
        if m.get('VolumeType') is not None:
            self.volume_type = m.get('VolumeType')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('WinAdPar') is not None:
            temp_model = CreateHybridClusterRequestWinAdPar()
            self.win_ad_par = temp_model.from_map(m['WinAdPar'])
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateHybridClusterResponseBody(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.request_id = request_id
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
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateHybridClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateHybridClusterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateHybridClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateJobFileRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        content: str = None,
        runas_user: str = None,
        runas_user_password: str = None,
        target_file: str = None,
    ):
        self.cluster_id = cluster_id
        self.content = content
        self.runas_user = runas_user
        self.runas_user_password = runas_user_password
        self.target_file = target_file

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.content is not None:
            result['Content'] = self.content
        if self.runas_user is not None:
            result['RunasUser'] = self.runas_user
        if self.runas_user_password is not None:
            result['RunasUserPassword'] = self.runas_user_password
        if self.target_file is not None:
            result['TargetFile'] = self.target_file
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RunasUser') is not None:
            self.runas_user = m.get('RunasUser')
        if m.get('RunasUserPassword') is not None:
            self.runas_user_password = m.get('RunasUserPassword')
        if m.get('TargetFile') is not None:
            self.target_file = m.get('TargetFile')
        return self


class CreateJobFileResponseBody(TeaModel):
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


class CreateJobFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateJobFileResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateJobFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateJobTemplateRequest(TeaModel):
    def __init__(
        self,
        array_request: str = None,
        clock_time: str = None,
        command_line: str = None,
        gpu: int = None,
        input_file_url: str = None,
        mem: str = None,
        name: str = None,
        node: int = None,
        package_path: str = None,
        priority: int = None,
        queue: str = None,
        re_runable: bool = None,
        runas_user: str = None,
        stderr_redirect_path: str = None,
        stdout_redirect_path: str = None,
        task: int = None,
        thread: int = None,
        unzip_cmd: str = None,
        variables: str = None,
        with_unzip_cmd: bool = None,
    ):
        self.array_request = array_request
        self.clock_time = clock_time
        self.command_line = command_line
        self.gpu = gpu
        self.input_file_url = input_file_url
        self.mem = mem
        self.name = name
        self.node = node
        self.package_path = package_path
        self.priority = priority
        self.queue = queue
        self.re_runable = re_runable
        self.runas_user = runas_user
        self.stderr_redirect_path = stderr_redirect_path
        self.stdout_redirect_path = stdout_redirect_path
        self.task = task
        self.thread = thread
        self.unzip_cmd = unzip_cmd
        self.variables = variables
        self.with_unzip_cmd = with_unzip_cmd

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.array_request is not None:
            result['ArrayRequest'] = self.array_request
        if self.clock_time is not None:
            result['ClockTime'] = self.clock_time
        if self.command_line is not None:
            result['CommandLine'] = self.command_line
        if self.gpu is not None:
            result['Gpu'] = self.gpu
        if self.input_file_url is not None:
            result['InputFileUrl'] = self.input_file_url
        if self.mem is not None:
            result['Mem'] = self.mem
        if self.name is not None:
            result['Name'] = self.name
        if self.node is not None:
            result['Node'] = self.node
        if self.package_path is not None:
            result['PackagePath'] = self.package_path
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.queue is not None:
            result['Queue'] = self.queue
        if self.re_runable is not None:
            result['ReRunable'] = self.re_runable
        if self.runas_user is not None:
            result['RunasUser'] = self.runas_user
        if self.stderr_redirect_path is not None:
            result['StderrRedirectPath'] = self.stderr_redirect_path
        if self.stdout_redirect_path is not None:
            result['StdoutRedirectPath'] = self.stdout_redirect_path
        if self.task is not None:
            result['Task'] = self.task
        if self.thread is not None:
            result['Thread'] = self.thread
        if self.unzip_cmd is not None:
            result['UnzipCmd'] = self.unzip_cmd
        if self.variables is not None:
            result['Variables'] = self.variables
        if self.with_unzip_cmd is not None:
            result['WithUnzipCmd'] = self.with_unzip_cmd
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArrayRequest') is not None:
            self.array_request = m.get('ArrayRequest')
        if m.get('ClockTime') is not None:
            self.clock_time = m.get('ClockTime')
        if m.get('CommandLine') is not None:
            self.command_line = m.get('CommandLine')
        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')
        if m.get('InputFileUrl') is not None:
            self.input_file_url = m.get('InputFileUrl')
        if m.get('Mem') is not None:
            self.mem = m.get('Mem')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Node') is not None:
            self.node = m.get('Node')
        if m.get('PackagePath') is not None:
            self.package_path = m.get('PackagePath')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Queue') is not None:
            self.queue = m.get('Queue')
        if m.get('ReRunable') is not None:
            self.re_runable = m.get('ReRunable')
        if m.get('RunasUser') is not None:
            self.runas_user = m.get('RunasUser')
        if m.get('StderrRedirectPath') is not None:
            self.stderr_redirect_path = m.get('StderrRedirectPath')
        if m.get('StdoutRedirectPath') is not None:
            self.stdout_redirect_path = m.get('StdoutRedirectPath')
        if m.get('Task') is not None:
            self.task = m.get('Task')
        if m.get('Thread') is not None:
            self.thread = m.get('Thread')
        if m.get('UnzipCmd') is not None:
            self.unzip_cmd = m.get('UnzipCmd')
        if m.get('Variables') is not None:
            self.variables = m.get('Variables')
        if m.get('WithUnzipCmd') is not None:
            self.with_unzip_cmd = m.get('WithUnzipCmd')
        return self


class CreateJobTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        template_id: str = None,
    ):
        self.request_id = request_id
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class CreateJobTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateJobTemplateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateJobTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteClusterRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        release_instance: str = None,
    ):
        self.cluster_id = cluster_id
        self.release_instance = release_instance

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.release_instance is not None:
            result['ReleaseInstance'] = self.release_instance
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ReleaseInstance') is not None:
            self.release_instance = m.get('ReleaseInstance')
        return self


class DeleteClusterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        self.request_id = request_id
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
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class DeleteContainerAppsRequestContainerApp(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteContainerAppsRequest(TeaModel):
    def __init__(
        self,
        container_app: List[DeleteContainerAppsRequestContainerApp] = None,
    ):
        self.container_app = container_app

    def validate(self):
        if self.container_app:
            for k in self.container_app:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ContainerApp'] = []
        if self.container_app is not None:
            for k in self.container_app:
                result['ContainerApp'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.container_app = []
        if m.get('ContainerApp') is not None:
            for k in m.get('ContainerApp'):
                temp_model = DeleteContainerAppsRequestContainerApp()
                self.container_app.append(temp_model.from_map(k))
        return self


class DeleteContainerAppsResponseBody(TeaModel):
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


class DeleteContainerAppsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteContainerAppsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeleteContainerAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGWSClusterRequest(TeaModel):
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


class DeleteGWSClusterResponseBody(TeaModel):
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


class DeleteGWSClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteGWSClusterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeleteGWSClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGWSInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteGWSInstanceResponseBody(TeaModel):
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


class DeleteGWSInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteGWSInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeleteGWSInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteImageRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        container_type: str = None,
        image_tag: str = None,
        repository: str = None,
    ):
        self.cluster_id = cluster_id
        self.container_type = container_type
        self.image_tag = image_tag
        self.repository = repository

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.container_type is not None:
            result['ContainerType'] = self.container_type
        if self.image_tag is not None:
            result['ImageTag'] = self.image_tag
        if self.repository is not None:
            result['Repository'] = self.repository
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ContainerType') is not None:
            self.container_type = m.get('ContainerType')
        if m.get('ImageTag') is not None:
            self.image_tag = m.get('ImageTag')
        if m.get('Repository') is not None:
            self.repository = m.get('Repository')
        return self


class DeleteImageResponseBody(TeaModel):
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


class DeleteImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteImageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeleteImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteJobTemplatesRequest(TeaModel):
    def __init__(
        self,
        templates: str = None,
    ):
        self.templates = templates

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.templates is not None:
            result['Templates'] = self.templates
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Templates') is not None:
            self.templates = m.get('Templates')
        return self


class DeleteJobTemplatesResponseBody(TeaModel):
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


class DeleteJobTemplatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteJobTemplatesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeleteJobTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteJobsRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        jobs: str = None,
    ):
        self.cluster_id = cluster_id
        self.jobs = jobs

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.jobs is not None:
            result['Jobs'] = self.jobs
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Jobs') is not None:
            self.jobs = m.get('Jobs')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class DeleteLocalImageRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        container_type: str = None,
        image_name: str = None,
    ):
        self.cluster_id = cluster_id
        self.container_type = container_type
        self.image_name = image_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.container_type is not None:
            result['ContainerType'] = self.container_type
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ContainerType') is not None:
            self.container_type = m.get('ContainerType')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        return self


class DeleteLocalImageResponseBody(TeaModel):
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


class DeleteLocalImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteLocalImageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeleteLocalImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteNodesRequestInstance(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteNodesRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        instance: List[DeleteNodesRequestInstance] = None,
        release_instance: bool = None,
        sync: bool = None,
    ):
        self.cluster_id = cluster_id
        self.instance = instance
        self.release_instance = release_instance
        self.sync = sync

    def validate(self):
        if self.instance:
            for k in self.instance:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        result['Instance'] = []
        if self.instance is not None:
            for k in self.instance:
                result['Instance'].append(k.to_map() if k else None)
        if self.release_instance is not None:
            result['ReleaseInstance'] = self.release_instance
        if self.sync is not None:
            result['Sync'] = self.sync
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        self.instance = []
        if m.get('Instance') is not None:
            for k in m.get('Instance'):
                temp_model = DeleteNodesRequestInstance()
                self.instance.append(temp_model.from_map(k))
        if m.get('ReleaseInstance') is not None:
            self.release_instance = m.get('ReleaseInstance')
        if m.get('Sync') is not None:
            self.sync = m.get('Sync')
        return self


class DeleteNodesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        self.request_id = request_id
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
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class DeleteQueueRequest(TeaModel):
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


class DeleteQueueResponseBody(TeaModel):
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


class DeleteQueueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteQueueResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeleteQueueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSecurityGroupRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        security_group_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.security_group_id = security_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        return self


class DeleteSecurityGroupResponseBody(TeaModel):
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


class DeleteSecurityGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSecurityGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeleteSecurityGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUsersRequestUser(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DeleteUsersRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        user: List[DeleteUsersRequestUser] = None,
    ):
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
                temp_model = DeleteUsersRequestUser()
                self.user.append(temp_model.from_map(k))
        return self


class DeleteUsersResponseBody(TeaModel):
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class DescribeAutoScaleConfigRequest(TeaModel):
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


class DescribeAutoScaleConfigResponseBody(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_type: str = None,
        enable_auto_grow: bool = None,
        enable_auto_shrink: bool = None,
        exclude_nodes: str = None,
        extra_nodes_grow_ratio: int = None,
        grow_interval_in_minutes: int = None,
        grow_ratio: int = None,
        grow_timeout_in_minutes: int = None,
        max_nodes_in_cluster: int = None,
        request_id: str = None,
        shrink_idle_times: int = None,
        shrink_interval_in_minutes: int = None,
        spot_price_limit: str = None,
        spot_strategy: str = None,
        uid: str = None,
    ):
        self.cluster_id = cluster_id
        self.cluster_type = cluster_type
        self.enable_auto_grow = enable_auto_grow
        self.enable_auto_shrink = enable_auto_shrink
        self.exclude_nodes = exclude_nodes
        self.extra_nodes_grow_ratio = extra_nodes_grow_ratio
        self.grow_interval_in_minutes = grow_interval_in_minutes
        self.grow_ratio = grow_ratio
        self.grow_timeout_in_minutes = grow_timeout_in_minutes
        self.max_nodes_in_cluster = max_nodes_in_cluster
        self.request_id = request_id
        self.shrink_idle_times = shrink_idle_times
        self.shrink_interval_in_minutes = shrink_interval_in_minutes
        self.spot_price_limit = spot_price_limit
        self.spot_strategy = spot_strategy
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.enable_auto_grow is not None:
            result['EnableAutoGrow'] = self.enable_auto_grow
        if self.enable_auto_shrink is not None:
            result['EnableAutoShrink'] = self.enable_auto_shrink
        if self.exclude_nodes is not None:
            result['ExcludeNodes'] = self.exclude_nodes
        if self.extra_nodes_grow_ratio is not None:
            result['ExtraNodesGrowRatio'] = self.extra_nodes_grow_ratio
        if self.grow_interval_in_minutes is not None:
            result['GrowIntervalInMinutes'] = self.grow_interval_in_minutes
        if self.grow_ratio is not None:
            result['GrowRatio'] = self.grow_ratio
        if self.grow_timeout_in_minutes is not None:
            result['GrowTimeoutInMinutes'] = self.grow_timeout_in_minutes
        if self.max_nodes_in_cluster is not None:
            result['MaxNodesInCluster'] = self.max_nodes_in_cluster
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.shrink_idle_times is not None:
            result['ShrinkIdleTimes'] = self.shrink_idle_times
        if self.shrink_interval_in_minutes is not None:
            result['ShrinkIntervalInMinutes'] = self.shrink_interval_in_minutes
        if self.spot_price_limit is not None:
            result['SpotPriceLimit'] = self.spot_price_limit
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('EnableAutoGrow') is not None:
            self.enable_auto_grow = m.get('EnableAutoGrow')
        if m.get('EnableAutoShrink') is not None:
            self.enable_auto_shrink = m.get('EnableAutoShrink')
        if m.get('ExcludeNodes') is not None:
            self.exclude_nodes = m.get('ExcludeNodes')
        if m.get('ExtraNodesGrowRatio') is not None:
            self.extra_nodes_grow_ratio = m.get('ExtraNodesGrowRatio')
        if m.get('GrowIntervalInMinutes') is not None:
            self.grow_interval_in_minutes = m.get('GrowIntervalInMinutes')
        if m.get('GrowRatio') is not None:
            self.grow_ratio = m.get('GrowRatio')
        if m.get('GrowTimeoutInMinutes') is not None:
            self.grow_timeout_in_minutes = m.get('GrowTimeoutInMinutes')
        if m.get('MaxNodesInCluster') is not None:
            self.max_nodes_in_cluster = m.get('MaxNodesInCluster')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ShrinkIdleTimes') is not None:
            self.shrink_idle_times = m.get('ShrinkIdleTimes')
        if m.get('ShrinkIntervalInMinutes') is not None:
            self.shrink_interval_in_minutes = m.get('ShrinkIntervalInMinutes')
        if m.get('SpotPriceLimit') is not None:
            self.spot_price_limit = m.get('SpotPriceLimit')
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class DescribeAutoScaleConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAutoScaleConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeAutoScaleConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClusterRequest(TeaModel):
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


class DescribeClusterResponseBodyClusterInfoApplicationsApplicationInfo(TeaModel):
    def __init__(
        self,
        name: str = None,
        tag: str = None,
        version: str = None,
    ):
        self.name = name
        self.tag = tag
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
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeClusterResponseBodyClusterInfoApplications(TeaModel):
    def __init__(
        self,
        application_info: List[DescribeClusterResponseBodyClusterInfoApplicationsApplicationInfo] = None,
    ):
        self.application_info = application_info

    def validate(self):
        if self.application_info:
            for k in self.application_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApplicationInfo'] = []
        if self.application_info is not None:
            for k in self.application_info:
                result['ApplicationInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.application_info = []
        if m.get('ApplicationInfo') is not None:
            for k in m.get('ApplicationInfo'):
                temp_model = DescribeClusterResponseBodyClusterInfoApplicationsApplicationInfo()
                self.application_info.append(temp_model.from_map(k))
        return self


class DescribeClusterResponseBodyClusterInfoEcsInfoCompute(TeaModel):
    def __init__(
        self,
        count: int = None,
        instance_type: str = None,
    ):
        self.count = count
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class DescribeClusterResponseBodyClusterInfoEcsInfoLogin(TeaModel):
    def __init__(
        self,
        count: int = None,
        instance_type: str = None,
    ):
        self.count = count
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class DescribeClusterResponseBodyClusterInfoEcsInfoManager(TeaModel):
    def __init__(
        self,
        count: int = None,
        instance_type: str = None,
    ):
        self.count = count
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class DescribeClusterResponseBodyClusterInfoEcsInfoProxyMgr(TeaModel):
    def __init__(
        self,
        count: int = None,
        instance_type: str = None,
    ):
        self.count = count
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class DescribeClusterResponseBodyClusterInfoEcsInfo(TeaModel):
    def __init__(
        self,
        compute: DescribeClusterResponseBodyClusterInfoEcsInfoCompute = None,
        login: DescribeClusterResponseBodyClusterInfoEcsInfoLogin = None,
        manager: DescribeClusterResponseBodyClusterInfoEcsInfoManager = None,
        proxy_mgr: DescribeClusterResponseBodyClusterInfoEcsInfoProxyMgr = None,
    ):
        self.compute = compute
        self.login = login
        self.manager = manager
        self.proxy_mgr = proxy_mgr

    def validate(self):
        if self.compute:
            self.compute.validate()
        if self.login:
            self.login.validate()
        if self.manager:
            self.manager.validate()
        if self.proxy_mgr:
            self.proxy_mgr.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compute is not None:
            result['Compute'] = self.compute.to_map()
        if self.login is not None:
            result['Login'] = self.login.to_map()
        if self.manager is not None:
            result['Manager'] = self.manager.to_map()
        if self.proxy_mgr is not None:
            result['ProxyMgr'] = self.proxy_mgr.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Compute') is not None:
            temp_model = DescribeClusterResponseBodyClusterInfoEcsInfoCompute()
            self.compute = temp_model.from_map(m['Compute'])
        if m.get('Login') is not None:
            temp_model = DescribeClusterResponseBodyClusterInfoEcsInfoLogin()
            self.login = temp_model.from_map(m['Login'])
        if m.get('Manager') is not None:
            temp_model = DescribeClusterResponseBodyClusterInfoEcsInfoManager()
            self.manager = temp_model.from_map(m['Manager'])
        if m.get('ProxyMgr') is not None:
            temp_model = DescribeClusterResponseBodyClusterInfoEcsInfoProxyMgr()
            self.proxy_mgr = temp_model.from_map(m['ProxyMgr'])
        return self


class DescribeClusterResponseBodyClusterInfoOnPremiseInfoOnPremiseInfo(TeaModel):
    def __init__(
        self,
        host_name: str = None,
        ip: str = None,
        type: str = None,
    ):
        self.host_name = host_name
        self.ip = ip
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.ip is not None:
            result['IP'] = self.ip
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeClusterResponseBodyClusterInfoOnPremiseInfo(TeaModel):
    def __init__(
        self,
        on_premise_info: List[DescribeClusterResponseBodyClusterInfoOnPremiseInfoOnPremiseInfo] = None,
    ):
        self.on_premise_info = on_premise_info

    def validate(self):
        if self.on_premise_info:
            for k in self.on_premise_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OnPremiseInfo'] = []
        if self.on_premise_info is not None:
            for k in self.on_premise_info:
                result['OnPremiseInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.on_premise_info = []
        if m.get('OnPremiseInfo') is not None:
            for k in m.get('OnPremiseInfo'):
                temp_model = DescribeClusterResponseBodyClusterInfoOnPremiseInfoOnPremiseInfo()
                self.on_premise_info.append(temp_model.from_map(k))
        return self


class DescribeClusterResponseBodyClusterInfoPostInstallScriptsPostInstallScriptInfo(TeaModel):
    def __init__(
        self,
        args: str = None,
        url: str = None,
    ):
        self.args = args
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.args is not None:
            result['Args'] = self.args
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Args') is not None:
            self.args = m.get('Args')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeClusterResponseBodyClusterInfoPostInstallScripts(TeaModel):
    def __init__(
        self,
        post_install_script_info: List[DescribeClusterResponseBodyClusterInfoPostInstallScriptsPostInstallScriptInfo] = None,
    ):
        self.post_install_script_info = post_install_script_info

    def validate(self):
        if self.post_install_script_info:
            for k in self.post_install_script_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PostInstallScriptInfo'] = []
        if self.post_install_script_info is not None:
            for k in self.post_install_script_info:
                result['PostInstallScriptInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.post_install_script_info = []
        if m.get('PostInstallScriptInfo') is not None:
            for k in m.get('PostInstallScriptInfo'):
                temp_model = DescribeClusterResponseBodyClusterInfoPostInstallScriptsPostInstallScriptInfo()
                self.post_install_script_info.append(temp_model.from_map(k))
        return self


class DescribeClusterResponseBodyClusterInfo(TeaModel):
    def __init__(
        self,
        account_type: str = None,
        applications: DescribeClusterResponseBodyClusterInfoApplications = None,
        base_os_tag: str = None,
        client_version: str = None,
        create_time: str = None,
        deploy_mode: str = None,
        description: str = None,
        ecs_charge_type: str = None,
        ecs_info: DescribeClusterResponseBodyClusterInfoEcsInfo = None,
        ha_enable: bool = None,
        id: str = None,
        image_id: str = None,
        image_name: str = None,
        image_owner_alias: str = None,
        key_pair_name: str = None,
        location: str = None,
        name: str = None,
        on_premise_info: DescribeClusterResponseBodyClusterInfoOnPremiseInfo = None,
        os_tag: str = None,
        post_install_scripts: DescribeClusterResponseBodyClusterInfoPostInstallScripts = None,
        region_id: str = None,
        remote_directory: str = None,
        scc_cluster_id: str = None,
        scheduler_type: str = None,
        security_group_id: str = None,
        status: str = None,
        v_switch_id: str = None,
        volume_id: str = None,
        volume_mountpoint: str = None,
        volume_protocol: str = None,
        volume_type: str = None,
        vpc_id: str = None,
    ):
        self.account_type = account_type
        self.applications = applications
        self.base_os_tag = base_os_tag
        self.client_version = client_version
        self.create_time = create_time
        self.deploy_mode = deploy_mode
        self.description = description
        self.ecs_charge_type = ecs_charge_type
        self.ecs_info = ecs_info
        self.ha_enable = ha_enable
        self.id = id
        self.image_id = image_id
        self.image_name = image_name
        self.image_owner_alias = image_owner_alias
        self.key_pair_name = key_pair_name
        self.location = location
        self.name = name
        self.on_premise_info = on_premise_info
        self.os_tag = os_tag
        self.post_install_scripts = post_install_scripts
        self.region_id = region_id
        self.remote_directory = remote_directory
        self.scc_cluster_id = scc_cluster_id
        self.scheduler_type = scheduler_type
        self.security_group_id = security_group_id
        self.status = status
        self.v_switch_id = v_switch_id
        self.volume_id = volume_id
        self.volume_mountpoint = volume_mountpoint
        self.volume_protocol = volume_protocol
        self.volume_type = volume_type
        self.vpc_id = vpc_id

    def validate(self):
        if self.applications:
            self.applications.validate()
        if self.ecs_info:
            self.ecs_info.validate()
        if self.on_premise_info:
            self.on_premise_info.validate()
        if self.post_install_scripts:
            self.post_install_scripts.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.applications is not None:
            result['Applications'] = self.applications.to_map()
        if self.base_os_tag is not None:
            result['BaseOsTag'] = self.base_os_tag
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deploy_mode is not None:
            result['DeployMode'] = self.deploy_mode
        if self.description is not None:
            result['Description'] = self.description
        if self.ecs_charge_type is not None:
            result['EcsChargeType'] = self.ecs_charge_type
        if self.ecs_info is not None:
            result['EcsInfo'] = self.ecs_info.to_map()
        if self.ha_enable is not None:
            result['HaEnable'] = self.ha_enable
        if self.id is not None:
            result['Id'] = self.id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.image_owner_alias is not None:
            result['ImageOwnerAlias'] = self.image_owner_alias
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.location is not None:
            result['Location'] = self.location
        if self.name is not None:
            result['Name'] = self.name
        if self.on_premise_info is not None:
            result['OnPremiseInfo'] = self.on_premise_info.to_map()
        if self.os_tag is not None:
            result['OsTag'] = self.os_tag
        if self.post_install_scripts is not None:
            result['PostInstallScripts'] = self.post_install_scripts.to_map()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.remote_directory is not None:
            result['RemoteDirectory'] = self.remote_directory
        if self.scc_cluster_id is not None:
            result['SccClusterId'] = self.scc_cluster_id
        if self.scheduler_type is not None:
            result['SchedulerType'] = self.scheduler_type
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.status is not None:
            result['Status'] = self.status
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.volume_id is not None:
            result['VolumeId'] = self.volume_id
        if self.volume_mountpoint is not None:
            result['VolumeMountpoint'] = self.volume_mountpoint
        if self.volume_protocol is not None:
            result['VolumeProtocol'] = self.volume_protocol
        if self.volume_type is not None:
            result['VolumeType'] = self.volume_type
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('Applications') is not None:
            temp_model = DescribeClusterResponseBodyClusterInfoApplications()
            self.applications = temp_model.from_map(m['Applications'])
        if m.get('BaseOsTag') is not None:
            self.base_os_tag = m.get('BaseOsTag')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DeployMode') is not None:
            self.deploy_mode = m.get('DeployMode')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EcsChargeType') is not None:
            self.ecs_charge_type = m.get('EcsChargeType')
        if m.get('EcsInfo') is not None:
            temp_model = DescribeClusterResponseBodyClusterInfoEcsInfo()
            self.ecs_info = temp_model.from_map(m['EcsInfo'])
        if m.get('HaEnable') is not None:
            self.ha_enable = m.get('HaEnable')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('ImageOwnerAlias') is not None:
            self.image_owner_alias = m.get('ImageOwnerAlias')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OnPremiseInfo') is not None:
            temp_model = DescribeClusterResponseBodyClusterInfoOnPremiseInfo()
            self.on_premise_info = temp_model.from_map(m['OnPremiseInfo'])
        if m.get('OsTag') is not None:
            self.os_tag = m.get('OsTag')
        if m.get('PostInstallScripts') is not None:
            temp_model = DescribeClusterResponseBodyClusterInfoPostInstallScripts()
            self.post_install_scripts = temp_model.from_map(m['PostInstallScripts'])
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RemoteDirectory') is not None:
            self.remote_directory = m.get('RemoteDirectory')
        if m.get('SccClusterId') is not None:
            self.scc_cluster_id = m.get('SccClusterId')
        if m.get('SchedulerType') is not None:
            self.scheduler_type = m.get('SchedulerType')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VolumeId') is not None:
            self.volume_id = m.get('VolumeId')
        if m.get('VolumeMountpoint') is not None:
            self.volume_mountpoint = m.get('VolumeMountpoint')
        if m.get('VolumeProtocol') is not None:
            self.volume_protocol = m.get('VolumeProtocol')
        if m.get('VolumeType') is not None:
            self.volume_type = m.get('VolumeType')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeClusterResponseBody(TeaModel):
    def __init__(
        self,
        cluster_info: DescribeClusterResponseBodyClusterInfo = None,
        request_id: str = None,
    ):
        self.cluster_info = cluster_info
        self.request_id = request_id

    def validate(self):
        if self.cluster_info:
            self.cluster_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_info is not None:
            result['ClusterInfo'] = self.cluster_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterInfo') is not None:
            temp_model = DescribeClusterResponseBodyClusterInfo()
            self.cluster_info = temp_model.from_map(m['ClusterInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeClusterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeContainerAppRequest(TeaModel):
    def __init__(
        self,
        container_id: str = None,
    ):
        self.container_id = container_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_id is not None:
            result['ContainerId'] = self.container_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerId') is not None:
            self.container_id = m.get('ContainerId')
        return self


class DescribeContainerAppResponseBodyContainerAppInfo(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        id: str = None,
        image_tag: str = None,
        name: str = None,
        repository: str = None,
        type: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.id = id
        self.image_tag = image_tag
        self.name = name
        self.repository = repository
        self.type = type

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
        if self.id is not None:
            result['Id'] = self.id
        if self.image_tag is not None:
            result['ImageTag'] = self.image_tag
        if self.name is not None:
            result['Name'] = self.name
        if self.repository is not None:
            result['Repository'] = self.repository
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ImageTag') is not None:
            self.image_tag = m.get('ImageTag')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Repository') is not None:
            self.repository = m.get('Repository')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeContainerAppResponseBody(TeaModel):
    def __init__(
        self,
        container_app_info: DescribeContainerAppResponseBodyContainerAppInfo = None,
        request_id: str = None,
    ):
        self.container_app_info = container_app_info
        self.request_id = request_id

    def validate(self):
        if self.container_app_info:
            self.container_app_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_app_info is not None:
            result['ContainerAppInfo'] = self.container_app_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerAppInfo') is not None:
            temp_model = DescribeContainerAppResponseBodyContainerAppInfo()
            self.container_app_info = temp_model.from_map(m['ContainerAppInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeContainerAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeContainerAppResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeContainerAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEstackImageRequest(TeaModel):
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


class DescribeEstackImageResponseBodyImageListImageListInfo(TeaModel):
    def __init__(
        self,
        image_name: str = None,
        image_size: int = None,
        image_type: str = None,
        image_url: str = None,
        recent_update_time: str = None,
    ):
        self.image_name = image_name
        self.image_size = image_size
        self.image_type = image_type
        self.image_url = image_url
        self.recent_update_time = recent_update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.image_size is not None:
            result['ImageSize'] = self.image_size
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.recent_update_time is not None:
            result['RecentUpdateTime'] = self.recent_update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('ImageSize') is not None:
            self.image_size = m.get('ImageSize')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('RecentUpdateTime') is not None:
            self.recent_update_time = m.get('RecentUpdateTime')
        return self


class DescribeEstackImageResponseBodyImageList(TeaModel):
    def __init__(
        self,
        image_list_info: List[DescribeEstackImageResponseBodyImageListImageListInfo] = None,
    ):
        self.image_list_info = image_list_info

    def validate(self):
        if self.image_list_info:
            for k in self.image_list_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ImageListInfo'] = []
        if self.image_list_info is not None:
            for k in self.image_list_info:
                result['ImageListInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.image_list_info = []
        if m.get('ImageListInfo') is not None:
            for k in m.get('ImageListInfo'):
                temp_model = DescribeEstackImageResponseBodyImageListImageListInfo()
                self.image_list_info.append(temp_model.from_map(k))
        return self


class DescribeEstackImageResponseBody(TeaModel):
    def __init__(
        self,
        image_list: DescribeEstackImageResponseBodyImageList = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.image_list = image_list
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.image_list:
            self.image_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_list is not None:
            result['ImageList'] = self.image_list.to_map()
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
        if m.get('ImageList') is not None:
            temp_model = DescribeEstackImageResponseBodyImageList()
            self.image_list = temp_model.from_map(m['ImageList'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeEstackImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeEstackImageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeEstackImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGWSClusterPolicyRequest(TeaModel):
    def __init__(
        self,
        async_mode: bool = None,
        cluster_id: str = None,
        task_id: str = None,
    ):
        self.async_mode = async_mode
        self.cluster_id = cluster_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.async_mode is not None:
            result['AsyncMode'] = self.async_mode
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsyncMode') is not None:
            self.async_mode = m.get('AsyncMode')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeGWSClusterPolicyResponseBody(TeaModel):
    def __init__(
        self,
        clipboard: str = None,
        local_drive: str = None,
        request_id: str = None,
        usb_redirect: str = None,
        watermark: str = None,
    ):
        self.clipboard = clipboard
        self.local_drive = local_drive
        self.request_id = request_id
        self.usb_redirect = usb_redirect
        self.watermark = watermark

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clipboard is not None:
            result['Clipboard'] = self.clipboard
        if self.local_drive is not None:
            result['LocalDrive'] = self.local_drive
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.usb_redirect is not None:
            result['UsbRedirect'] = self.usb_redirect
        if self.watermark is not None:
            result['Watermark'] = self.watermark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Clipboard') is not None:
            self.clipboard = m.get('Clipboard')
        if m.get('LocalDrive') is not None:
            self.local_drive = m.get('LocalDrive')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UsbRedirect') is not None:
            self.usb_redirect = m.get('UsbRedirect')
        if m.get('Watermark') is not None:
            self.watermark = m.get('Watermark')
        return self


class DescribeGWSClusterPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeGWSClusterPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeGWSClusterPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGWSClustersRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
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


class DescribeGWSClustersResponseBodyClustersClusterInfo(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        create_time: str = None,
        instance_count: int = None,
        status: str = None,
        vpc_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.create_time = create_time
        self.instance_count = instance_count
        self.status = status
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count
        if self.status is not None:
            result['Status'] = self.status
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeGWSClustersResponseBodyClusters(TeaModel):
    def __init__(
        self,
        cluster_info: List[DescribeGWSClustersResponseBodyClustersClusterInfo] = None,
    ):
        self.cluster_info = cluster_info

    def validate(self):
        if self.cluster_info:
            for k in self.cluster_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ClusterInfo'] = []
        if self.cluster_info is not None:
            for k in self.cluster_info:
                result['ClusterInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cluster_info = []
        if m.get('ClusterInfo') is not None:
            for k in m.get('ClusterInfo'):
                temp_model = DescribeGWSClustersResponseBodyClustersClusterInfo()
                self.cluster_info.append(temp_model.from_map(k))
        return self


class DescribeGWSClustersResponseBody(TeaModel):
    def __init__(
        self,
        caller_type: str = None,
        clusters: DescribeGWSClustersResponseBodyClusters = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.caller_type = caller_type
        self.clusters = clusters
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.clusters:
            self.clusters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.caller_type is not None:
            result['CallerType'] = self.caller_type
        if self.clusters is not None:
            result['Clusters'] = self.clusters.to_map()
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
        if m.get('CallerType') is not None:
            self.caller_type = m.get('CallerType')
        if m.get('Clusters') is not None:
            temp_model = DescribeGWSClustersResponseBodyClusters()
            self.clusters = temp_model.from_map(m['Clusters'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeGWSClustersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeGWSClustersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeGWSClustersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGWSImagesRequest(TeaModel):
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


class DescribeGWSImagesResponseBodyImagesImageInfo(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        image_id: str = None,
        image_type: str = None,
        name: str = None,
        progress: str = None,
        size: int = None,
        status: str = None,
    ):
        self.create_time = create_time
        self.image_id = image_id
        self.image_type = image_type
        self.name = name
        self.progress = progress
        self.size = size
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.name is not None:
            result['Name'] = self.name
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.size is not None:
            result['Size'] = self.size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeGWSImagesResponseBodyImages(TeaModel):
    def __init__(
        self,
        image_info: List[DescribeGWSImagesResponseBodyImagesImageInfo] = None,
    ):
        self.image_info = image_info

    def validate(self):
        if self.image_info:
            for k in self.image_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ImageInfo'] = []
        if self.image_info is not None:
            for k in self.image_info:
                result['ImageInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.image_info = []
        if m.get('ImageInfo') is not None:
            for k in m.get('ImageInfo'):
                temp_model = DescribeGWSImagesResponseBodyImagesImageInfo()
                self.image_info.append(temp_model.from_map(k))
        return self


class DescribeGWSImagesResponseBody(TeaModel):
    def __init__(
        self,
        images: DescribeGWSImagesResponseBodyImages = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.images = images
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.images:
            self.images.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.images is not None:
            result['Images'] = self.images.to_map()
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
        if m.get('Images') is not None:
            temp_model = DescribeGWSImagesResponseBodyImages()
            self.images = temp_model.from_map(m['Images'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeGWSImagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeGWSImagesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeGWSImagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGWSInstancesRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
        user_name: str = None,
        user_uid: int = None,
    ):
        self.cluster_id = cluster_id
        self.instance_id = instance_id
        self.page_number = page_number
        self.page_size = page_size
        self.user_name = user_name
        self.user_uid = user_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.user_uid is not None:
            result['UserUid'] = self.user_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('UserUid') is not None:
            self.user_uid = m.get('UserUid')
        return self


class DescribeGWSInstancesResponseBodyInstancesInstanceInfoAppListAppInfo(TeaModel):
    def __init__(
        self,
        app_args: str = None,
        app_name: str = None,
        app_path: str = None,
    ):
        self.app_args = app_args
        self.app_name = app_name
        self.app_path = app_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_args is not None:
            result['AppArgs'] = self.app_args
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_path is not None:
            result['AppPath'] = self.app_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppArgs') is not None:
            self.app_args = m.get('AppArgs')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppPath') is not None:
            self.app_path = m.get('AppPath')
        return self


class DescribeGWSInstancesResponseBodyInstancesInstanceInfoAppList(TeaModel):
    def __init__(
        self,
        app_info: List[DescribeGWSInstancesResponseBodyInstancesInstanceInfoAppListAppInfo] = None,
    ):
        self.app_info = app_info

    def validate(self):
        if self.app_info:
            for k in self.app_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AppInfo'] = []
        if self.app_info is not None:
            for k in self.app_info:
                result['AppInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app_info = []
        if m.get('AppInfo') is not None:
            for k in m.get('AppInfo'):
                temp_model = DescribeGWSInstancesResponseBodyInstancesInstanceInfoAppListAppInfo()
                self.app_info.append(temp_model.from_map(k))
        return self


class DescribeGWSInstancesResponseBodyInstancesInstanceInfo(TeaModel):
    def __init__(
        self,
        app_list: DescribeGWSInstancesResponseBodyInstancesInstanceInfoAppList = None,
        cluster_id: str = None,
        create_time: str = None,
        expire_time: str = None,
        instance_id: str = None,
        instance_type: str = None,
        name: str = None,
        status: str = None,
        user_name: str = None,
        work_mode: str = None,
    ):
        self.app_list = app_list
        self.cluster_id = cluster_id
        self.create_time = create_time
        self.expire_time = expire_time
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.name = name
        self.status = status
        self.user_name = user_name
        self.work_mode = work_mode

    def validate(self):
        if self.app_list:
            self.app_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_list is not None:
            result['AppList'] = self.app_list.to_map()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.work_mode is not None:
            result['WorkMode'] = self.work_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppList') is not None:
            temp_model = DescribeGWSInstancesResponseBodyInstancesInstanceInfoAppList()
            self.app_list = temp_model.from_map(m['AppList'])
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('WorkMode') is not None:
            self.work_mode = m.get('WorkMode')
        return self


class DescribeGWSInstancesResponseBodyInstances(TeaModel):
    def __init__(
        self,
        instance_info: List[DescribeGWSInstancesResponseBodyInstancesInstanceInfo] = None,
    ):
        self.instance_info = instance_info

    def validate(self):
        if self.instance_info:
            for k in self.instance_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceInfo'] = []
        if self.instance_info is not None:
            for k in self.instance_info:
                result['InstanceInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_info = []
        if m.get('InstanceInfo') is not None:
            for k in m.get('InstanceInfo'):
                temp_model = DescribeGWSInstancesResponseBodyInstancesInstanceInfo()
                self.instance_info.append(temp_model.from_map(k))
        return self


class DescribeGWSInstancesResponseBody(TeaModel):
    def __init__(
        self,
        instances: DescribeGWSInstancesResponseBodyInstances = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.instances = instances
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.instances:
            self.instances.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instances is not None:
            result['Instances'] = self.instances.to_map()
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
        if m.get('Instances') is not None:
            temp_model = DescribeGWSInstancesResponseBodyInstances()
            self.instances = temp_model.from_map(m['Instances'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeGWSInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeGWSInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeGWSInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeImageRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        container_type: str = None,
        image_tag: str = None,
        repository: str = None,
    ):
        self.cluster_id = cluster_id
        self.container_type = container_type
        self.image_tag = image_tag
        self.repository = repository

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.container_type is not None:
            result['ContainerType'] = self.container_type
        if self.image_tag is not None:
            result['ImageTag'] = self.image_tag
        if self.repository is not None:
            result['Repository'] = self.repository
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ContainerType') is not None:
            self.container_type = m.get('ContainerType')
        if m.get('ImageTag') is not None:
            self.image_tag = m.get('ImageTag')
        if m.get('Repository') is not None:
            self.repository = m.get('Repository')
        return self


class DescribeImageResponseBodyImageInfo(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        repository: str = None,
        status: str = None,
        system: str = None,
        tag: str = None,
        type: str = None,
        update_date_time: str = None,
    ):
        self.image_id = image_id
        self.repository = repository
        self.status = status
        self.system = system
        self.tag = tag
        self.type = type
        self.update_date_time = update_date_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.repository is not None:
            result['Repository'] = self.repository
        if self.status is not None:
            result['Status'] = self.status
        if self.system is not None:
            result['System'] = self.system
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.type is not None:
            result['Type'] = self.type
        if self.update_date_time is not None:
            result['UpdateDateTime'] = self.update_date_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('Repository') is not None:
            self.repository = m.get('Repository')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('System') is not None:
            self.system = m.get('System')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdateDateTime') is not None:
            self.update_date_time = m.get('UpdateDateTime')
        return self


class DescribeImageResponseBody(TeaModel):
    def __init__(
        self,
        image_info: DescribeImageResponseBodyImageInfo = None,
        request_id: str = None,
    ):
        self.image_info = image_info
        self.request_id = request_id

    def validate(self):
        if self.image_info:
            self.image_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_info is not None:
            result['ImageInfo'] = self.image_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageInfo') is not None:
            temp_model = DescribeImageResponseBodyImageInfo()
            self.image_info = temp_model.from_map(m['ImageInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeImageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeImageGatewayConfigRequest(TeaModel):
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


class DescribeImageGatewayConfigResponseBodyImagegwLocationsLocationInfo(TeaModel):
    def __init__(
        self,
        authentication: str = None,
        location: str = None,
        remote_type: str = None,
        url: str = None,
    ):
        self.authentication = authentication
        self.location = location
        self.remote_type = remote_type
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authentication is not None:
            result['Authentication'] = self.authentication
        if self.location is not None:
            result['Location'] = self.location
        if self.remote_type is not None:
            result['RemoteType'] = self.remote_type
        if self.url is not None:
            result['URL'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Authentication') is not None:
            self.authentication = m.get('Authentication')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('RemoteType') is not None:
            self.remote_type = m.get('RemoteType')
        if m.get('URL') is not None:
            self.url = m.get('URL')
        return self


class DescribeImageGatewayConfigResponseBodyImagegwLocations(TeaModel):
    def __init__(
        self,
        location_info: List[DescribeImageGatewayConfigResponseBodyImagegwLocationsLocationInfo] = None,
    ):
        self.location_info = location_info

    def validate(self):
        if self.location_info:
            for k in self.location_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LocationInfo'] = []
        if self.location_info is not None:
            for k in self.location_info:
                result['LocationInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.location_info = []
        if m.get('LocationInfo') is not None:
            for k in m.get('LocationInfo'):
                temp_model = DescribeImageGatewayConfigResponseBodyImagegwLocationsLocationInfo()
                self.location_info.append(temp_model.from_map(k))
        return self


class DescribeImageGatewayConfigResponseBodyImagegw(TeaModel):
    def __init__(
        self,
        default_image_location: str = None,
        image_expiration_timeout: str = None,
        locations: DescribeImageGatewayConfigResponseBodyImagegwLocations = None,
        mongo_dburi: str = None,
        pull_update_timeout: int = None,
        update_date_time: str = None,
    ):
        self.default_image_location = default_image_location
        self.image_expiration_timeout = image_expiration_timeout
        self.locations = locations
        self.mongo_dburi = mongo_dburi
        self.pull_update_timeout = pull_update_timeout
        self.update_date_time = update_date_time

    def validate(self):
        if self.locations:
            self.locations.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_image_location is not None:
            result['DefaultImageLocation'] = self.default_image_location
        if self.image_expiration_timeout is not None:
            result['ImageExpirationTimeout'] = self.image_expiration_timeout
        if self.locations is not None:
            result['Locations'] = self.locations.to_map()
        if self.mongo_dburi is not None:
            result['MongoDBURI'] = self.mongo_dburi
        if self.pull_update_timeout is not None:
            result['PullUpdateTimeout'] = self.pull_update_timeout
        if self.update_date_time is not None:
            result['UpdateDateTime'] = self.update_date_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultImageLocation') is not None:
            self.default_image_location = m.get('DefaultImageLocation')
        if m.get('ImageExpirationTimeout') is not None:
            self.image_expiration_timeout = m.get('ImageExpirationTimeout')
        if m.get('Locations') is not None:
            temp_model = DescribeImageGatewayConfigResponseBodyImagegwLocations()
            self.locations = temp_model.from_map(m['Locations'])
        if m.get('MongoDBURI') is not None:
            self.mongo_dburi = m.get('MongoDBURI')
        if m.get('PullUpdateTimeout') is not None:
            self.pull_update_timeout = m.get('PullUpdateTimeout')
        if m.get('UpdateDateTime') is not None:
            self.update_date_time = m.get('UpdateDateTime')
        return self


class DescribeImageGatewayConfigResponseBody(TeaModel):
    def __init__(
        self,
        imagegw: DescribeImageGatewayConfigResponseBodyImagegw = None,
        request_id: str = None,
    ):
        self.imagegw = imagegw
        self.request_id = request_id

    def validate(self):
        if self.imagegw:
            self.imagegw.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.imagegw is not None:
            result['Imagegw'] = self.imagegw.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Imagegw') is not None:
            temp_model = DescribeImageGatewayConfigResponseBodyImagegw()
            self.imagegw = temp_model.from_map(m['Imagegw'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeImageGatewayConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeImageGatewayConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeImageGatewayConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeImagePriceRequest(TeaModel):
    def __init__(
        self,
        amount: int = None,
        image_id: str = None,
        order_type: str = None,
        period: int = None,
        price_unit: str = None,
        sku_code: str = None,
    ):
        self.amount = amount
        self.image_id = image_id
        self.order_type = order_type
        self.period = period
        self.price_unit = price_unit
        self.sku_code = sku_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.period is not None:
            result['Period'] = self.period
        if self.price_unit is not None:
            result['PriceUnit'] = self.price_unit
        if self.sku_code is not None:
            result['SkuCode'] = self.sku_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PriceUnit') is not None:
            self.price_unit = m.get('PriceUnit')
        if m.get('SkuCode') is not None:
            self.sku_code = m.get('SkuCode')
        return self


class DescribeImagePriceResponseBody(TeaModel):
    def __init__(
        self,
        amount: int = None,
        discount_price: float = None,
        image_id: str = None,
        original_price: float = None,
        request_id: str = None,
        trade_price: float = None,
    ):
        self.amount = amount
        self.discount_price = discount_price
        self.image_id = image_id
        self.original_price = original_price
        self.request_id = request_id
        self.trade_price = trade_price

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        return self


class DescribeImagePriceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeImagePriceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeImagePriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeJobRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        job_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class DescribeJobResponseBodyMessage(TeaModel):
    def __init__(
        self,
        job_info: str = None,
    ):
        self.job_info = job_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_info is not None:
            result['JobInfo'] = self.job_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobInfo') is not None:
            self.job_info = m.get('JobInfo')
        return self


class DescribeJobResponseBody(TeaModel):
    def __init__(
        self,
        message: DescribeJobResponseBodyMessage = None,
        request_id: str = None,
    ):
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.message:
            self.message.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            temp_model = DescribeJobResponseBodyMessage()
            self.message = temp_model.from_map(m['Message'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNFSClientStatusRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeNFSClientStatusResponseBodyResult(TeaModel):
    def __init__(
        self,
        exit_code: int = None,
        invoke_record_status: str = None,
        output: str = None,
    ):
        self.exit_code = exit_code
        self.invoke_record_status = invoke_record_status
        self.output = output

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exit_code is not None:
            result['ExitCode'] = self.exit_code
        if self.invoke_record_status is not None:
            result['InvokeRecordStatus'] = self.invoke_record_status
        if self.output is not None:
            result['Output'] = self.output
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExitCode') is not None:
            self.exit_code = m.get('ExitCode')
        if m.get('InvokeRecordStatus') is not None:
            self.invoke_record_status = m.get('InvokeRecordStatus')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        return self


class DescribeNFSClientStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DescribeNFSClientStatusResponseBodyResult = None,
        status: str = None,
    ):
        self.request_id = request_id
        self.result = result
        self.status = status

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeNFSClientStatusResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeNFSClientStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeNFSClientStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeNFSClientStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePriceRequestCommoditiesDataDisks(TeaModel):
    def __init__(
        self,
        category: str = None,
        delete_with_instance: bool = None,
        encrypted: bool = None,
        performance_level: str = None,
        size: int = None,
    ):
        self.category = category
        self.delete_with_instance = delete_with_instance
        self.encrypted = encrypted
        self.performance_level = performance_level
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.delete_with_instance is not None:
            result['deleteWithInstance'] = self.delete_with_instance
        if self.encrypted is not None:
            result['encrypted'] = self.encrypted
        if self.performance_level is not None:
            result['performanceLevel'] = self.performance_level
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('deleteWithInstance') is not None:
            self.delete_with_instance = m.get('deleteWithInstance')
        if m.get('encrypted') is not None:
            self.encrypted = m.get('encrypted')
        if m.get('performanceLevel') is not None:
            self.performance_level = m.get('performanceLevel')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class DescribePriceRequestCommodities(TeaModel):
    def __init__(
        self,
        amount: int = None,
        data_disks: List[DescribePriceRequestCommoditiesDataDisks] = None,
        instance_type: str = None,
        internet_charge_type: str = None,
        internet_max_band_width_out: int = None,
        network_type: str = None,
        node_type: str = None,
        period: int = None,
        system_disk_category: str = None,
        system_disk_performance_level: str = None,
        system_disk_size: int = None,
    ):
        self.amount = amount
        self.data_disks = data_disks
        self.instance_type = instance_type
        self.internet_charge_type = internet_charge_type
        self.internet_max_band_width_out = internet_max_band_width_out
        self.network_type = network_type
        self.node_type = node_type
        self.period = period
        self.system_disk_category = system_disk_category
        self.system_disk_performance_level = system_disk_performance_level
        self.system_disk_size = system_disk_size

    def validate(self):
        if self.data_disks:
            for k in self.data_disks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        result['DataDisks'] = []
        if self.data_disks is not None:
            for k in self.data_disks:
                result['DataDisks'].append(k.to_map() if k else None)
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.internet_max_band_width_out is not None:
            result['InternetMaxBandWidthOut'] = self.internet_max_band_width_out
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        if self.period is not None:
            result['Period'] = self.period
        if self.system_disk_category is not None:
            result['SystemDiskCategory'] = self.system_disk_category
        if self.system_disk_performance_level is not None:
            result['SystemDiskPerformanceLevel'] = self.system_disk_performance_level
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        self.data_disks = []
        if m.get('DataDisks') is not None:
            for k in m.get('DataDisks'):
                temp_model = DescribePriceRequestCommoditiesDataDisks()
                self.data_disks.append(temp_model.from_map(k))
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('InternetMaxBandWidthOut') is not None:
            self.internet_max_band_width_out = m.get('InternetMaxBandWidthOut')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('SystemDiskCategory') is not None:
            self.system_disk_category = m.get('SystemDiskCategory')
        if m.get('SystemDiskPerformanceLevel') is not None:
            self.system_disk_performance_level = m.get('SystemDiskPerformanceLevel')
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        return self


class DescribePriceRequest(TeaModel):
    def __init__(
        self,
        charge_type: str = None,
        commodities: List[DescribePriceRequestCommodities] = None,
        order_type: str = None,
        price_unit: str = None,
    ):
        self.charge_type = charge_type
        self.commodities = commodities
        self.order_type = order_type
        self.price_unit = price_unit

    def validate(self):
        if self.commodities:
            for k in self.commodities:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        result['Commodities'] = []
        if self.commodities is not None:
            for k in self.commodities:
                result['Commodities'].append(k.to_map() if k else None)
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.price_unit is not None:
            result['PriceUnit'] = self.price_unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        self.commodities = []
        if m.get('Commodities') is not None:
            for k in m.get('Commodities'):
                temp_model = DescribePriceRequestCommodities()
                self.commodities.append(temp_model.from_map(k))
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('PriceUnit') is not None:
            self.price_unit = m.get('PriceUnit')
        return self


class DescribePriceResponseBodyPricesPriceInfo(TeaModel):
    def __init__(
        self,
        currency: str = None,
        node_type: str = None,
        original_price: float = None,
        trade_price: float = None,
    ):
        self.currency = currency
        self.node_type = node_type
        self.original_price = original_price
        self.trade_price = trade_price

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        return self


class DescribePriceResponseBodyPrices(TeaModel):
    def __init__(
        self,
        price_info: List[DescribePriceResponseBodyPricesPriceInfo] = None,
    ):
        self.price_info = price_info

    def validate(self):
        if self.price_info:
            for k in self.price_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PriceInfo'] = []
        if self.price_info is not None:
            for k in self.price_info:
                result['PriceInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.price_info = []
        if m.get('PriceInfo') is not None:
            for k in m.get('PriceInfo'):
                temp_model = DescribePriceResponseBodyPricesPriceInfo()
                self.price_info.append(temp_model.from_map(k))
        return self


class DescribePriceResponseBody(TeaModel):
    def __init__(
        self,
        prices: DescribePriceResponseBodyPrices = None,
        request_id: str = None,
        total_trade_price: float = None,
    ):
        self.prices = prices
        self.request_id = request_id
        self.total_trade_price = total_trade_price

    def validate(self):
        if self.prices:
            self.prices.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.prices is not None:
            result['Prices'] = self.prices.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_trade_price is not None:
            result['TotalTradePrice'] = self.total_trade_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Prices') is not None:
            temp_model = DescribePriceResponseBodyPrices()
            self.prices = temp_model.from_map(m['Prices'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalTradePrice') is not None:
            self.total_trade_price = m.get('TotalTradePrice')
        return self


class DescribePriceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribePriceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribePriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EditJobTemplateRequest(TeaModel):
    def __init__(
        self,
        array_request: str = None,
        clock_time: str = None,
        command_line: str = None,
        gpu: int = None,
        input_file_url: str = None,
        mem: str = None,
        name: str = None,
        node: int = None,
        package_path: str = None,
        priority: int = None,
        queue: str = None,
        re_runable: bool = None,
        runas_user: str = None,
        stderr_redirect_path: str = None,
        stdout_redirect_path: str = None,
        task: int = None,
        template_id: str = None,
        thread: int = None,
        unzip_cmd: str = None,
        variables: str = None,
        with_unzip_cmd: bool = None,
    ):
        self.array_request = array_request
        self.clock_time = clock_time
        self.command_line = command_line
        self.gpu = gpu
        self.input_file_url = input_file_url
        self.mem = mem
        self.name = name
        self.node = node
        self.package_path = package_path
        self.priority = priority
        self.queue = queue
        self.re_runable = re_runable
        self.runas_user = runas_user
        self.stderr_redirect_path = stderr_redirect_path
        self.stdout_redirect_path = stdout_redirect_path
        self.task = task
        self.template_id = template_id
        self.thread = thread
        self.unzip_cmd = unzip_cmd
        self.variables = variables
        self.with_unzip_cmd = with_unzip_cmd

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.array_request is not None:
            result['ArrayRequest'] = self.array_request
        if self.clock_time is not None:
            result['ClockTime'] = self.clock_time
        if self.command_line is not None:
            result['CommandLine'] = self.command_line
        if self.gpu is not None:
            result['Gpu'] = self.gpu
        if self.input_file_url is not None:
            result['InputFileUrl'] = self.input_file_url
        if self.mem is not None:
            result['Mem'] = self.mem
        if self.name is not None:
            result['Name'] = self.name
        if self.node is not None:
            result['Node'] = self.node
        if self.package_path is not None:
            result['PackagePath'] = self.package_path
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.queue is not None:
            result['Queue'] = self.queue
        if self.re_runable is not None:
            result['ReRunable'] = self.re_runable
        if self.runas_user is not None:
            result['RunasUser'] = self.runas_user
        if self.stderr_redirect_path is not None:
            result['StderrRedirectPath'] = self.stderr_redirect_path
        if self.stdout_redirect_path is not None:
            result['StdoutRedirectPath'] = self.stdout_redirect_path
        if self.task is not None:
            result['Task'] = self.task
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.thread is not None:
            result['Thread'] = self.thread
        if self.unzip_cmd is not None:
            result['UnzipCmd'] = self.unzip_cmd
        if self.variables is not None:
            result['Variables'] = self.variables
        if self.with_unzip_cmd is not None:
            result['WithUnzipCmd'] = self.with_unzip_cmd
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArrayRequest') is not None:
            self.array_request = m.get('ArrayRequest')
        if m.get('ClockTime') is not None:
            self.clock_time = m.get('ClockTime')
        if m.get('CommandLine') is not None:
            self.command_line = m.get('CommandLine')
        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')
        if m.get('InputFileUrl') is not None:
            self.input_file_url = m.get('InputFileUrl')
        if m.get('Mem') is not None:
            self.mem = m.get('Mem')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Node') is not None:
            self.node = m.get('Node')
        if m.get('PackagePath') is not None:
            self.package_path = m.get('PackagePath')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Queue') is not None:
            self.queue = m.get('Queue')
        if m.get('ReRunable') is not None:
            self.re_runable = m.get('ReRunable')
        if m.get('RunasUser') is not None:
            self.runas_user = m.get('RunasUser')
        if m.get('StderrRedirectPath') is not None:
            self.stderr_redirect_path = m.get('StderrRedirectPath')
        if m.get('StdoutRedirectPath') is not None:
            self.stdout_redirect_path = m.get('StdoutRedirectPath')
        if m.get('Task') is not None:
            self.task = m.get('Task')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('Thread') is not None:
            self.thread = m.get('Thread')
        if m.get('UnzipCmd') is not None:
            self.unzip_cmd = m.get('UnzipCmd')
        if m.get('Variables') is not None:
            self.variables = m.get('Variables')
        if m.get('WithUnzipCmd') is not None:
            self.with_unzip_cmd = m.get('WithUnzipCmd')
        return self


class EditJobTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        template_id: str = None,
    ):
        self.request_id = request_id
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class EditJobTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EditJobTemplateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = EditJobTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAccountingReportRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        dim: str = None,
        end_time: int = None,
        filter_value: str = None,
        job_id: str = None,
        page_number: int = None,
        page_size: int = None,
        report_type: str = None,
        start_time: int = None,
    ):
        self.cluster_id = cluster_id
        self.dim = dim
        self.end_time = end_time
        self.filter_value = filter_value
        self.job_id = job_id
        self.page_number = page_number
        self.page_size = page_size
        self.report_type = report_type
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.dim is not None:
            result['Dim'] = self.dim
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.filter_value is not None:
            result['FilterValue'] = self.filter_value
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.report_type is not None:
            result['ReportType'] = self.report_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Dim') is not None:
            self.dim = m.get('Dim')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FilterValue') is not None:
            self.filter_value = m.get('FilterValue')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ReportType') is not None:
            self.report_type = m.get('ReportType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class GetAccountingReportResponseBodyData(TeaModel):
    def __init__(
        self,
        data: List[str] = None,
    ):
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class GetAccountingReportResponseBody(TeaModel):
    def __init__(
        self,
        data: GetAccountingReportResponseBodyData = None,
        metrics: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_core_time: int = None,
        total_count: int = None,
    ):
        self.data = data
        self.metrics = metrics
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_core_time = total_core_time
        self.total_count = total_count

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.metrics is not None:
            result['Metrics'] = self.metrics
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_core_time is not None:
            result['TotalCoreTime'] = self.total_core_time
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetAccountingReportResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Metrics') is not None:
            self.metrics = m.get('Metrics')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCoreTime') is not None:
            self.total_core_time = m.get('TotalCoreTime')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetAccountingReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAccountingReportResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetAccountingReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAutoScaleConfigRequest(TeaModel):
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


class GetAutoScaleConfigResponseBodyQueuesQueueInfoDataDisksDataDisksInfo(TeaModel):
    def __init__(
        self,
        data_disk_category: str = None,
        data_disk_delete_with_instance: bool = None,
        data_disk_encrypted: bool = None,
        data_disk_kmskey_id: str = None,
        data_disk_performance_level: str = None,
        data_disk_size: int = None,
    ):
        self.data_disk_category = data_disk_category
        self.data_disk_delete_with_instance = data_disk_delete_with_instance
        self.data_disk_encrypted = data_disk_encrypted
        self.data_disk_kmskey_id = data_disk_kmskey_id
        self.data_disk_performance_level = data_disk_performance_level
        self.data_disk_size = data_disk_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_disk_category is not None:
            result['DataDiskCategory'] = self.data_disk_category
        if self.data_disk_delete_with_instance is not None:
            result['DataDiskDeleteWithInstance'] = self.data_disk_delete_with_instance
        if self.data_disk_encrypted is not None:
            result['DataDiskEncrypted'] = self.data_disk_encrypted
        if self.data_disk_kmskey_id is not None:
            result['DataDiskKMSKeyId'] = self.data_disk_kmskey_id
        if self.data_disk_performance_level is not None:
            result['DataDiskPerformanceLevel'] = self.data_disk_performance_level
        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataDiskCategory') is not None:
            self.data_disk_category = m.get('DataDiskCategory')
        if m.get('DataDiskDeleteWithInstance') is not None:
            self.data_disk_delete_with_instance = m.get('DataDiskDeleteWithInstance')
        if m.get('DataDiskEncrypted') is not None:
            self.data_disk_encrypted = m.get('DataDiskEncrypted')
        if m.get('DataDiskKMSKeyId') is not None:
            self.data_disk_kmskey_id = m.get('DataDiskKMSKeyId')
        if m.get('DataDiskPerformanceLevel') is not None:
            self.data_disk_performance_level = m.get('DataDiskPerformanceLevel')
        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')
        return self


class GetAutoScaleConfigResponseBodyQueuesQueueInfoDataDisks(TeaModel):
    def __init__(
        self,
        data_disks_info: List[GetAutoScaleConfigResponseBodyQueuesQueueInfoDataDisksDataDisksInfo] = None,
    ):
        self.data_disks_info = data_disks_info

    def validate(self):
        if self.data_disks_info:
            for k in self.data_disks_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataDisksInfo'] = []
        if self.data_disks_info is not None:
            for k in self.data_disks_info:
                result['DataDisksInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_disks_info = []
        if m.get('DataDisksInfo') is not None:
            for k in m.get('DataDisksInfo'):
                temp_model = GetAutoScaleConfigResponseBodyQueuesQueueInfoDataDisksDataDisksInfo()
                self.data_disks_info.append(temp_model.from_map(k))
        return self


class GetAutoScaleConfigResponseBodyQueuesQueueInfoInstanceTypesInstanceTypeInfo(TeaModel):
    def __init__(
        self,
        host_name_prefix: str = None,
        instance_type: str = None,
        spot_price_limit: float = None,
        spot_strategy: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        self.host_name_prefix = host_name_prefix
        self.instance_type = instance_type
        self.spot_price_limit = spot_price_limit
        self.spot_strategy = spot_strategy
        self.v_switch_id = v_switch_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_name_prefix is not None:
            result['HostNamePrefix'] = self.host_name_prefix
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.spot_price_limit is not None:
            result['SpotPriceLimit'] = self.spot_price_limit
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostNamePrefix') is not None:
            self.host_name_prefix = m.get('HostNamePrefix')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('SpotPriceLimit') is not None:
            self.spot_price_limit = m.get('SpotPriceLimit')
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class GetAutoScaleConfigResponseBodyQueuesQueueInfoInstanceTypes(TeaModel):
    def __init__(
        self,
        instance_type_info: List[GetAutoScaleConfigResponseBodyQueuesQueueInfoInstanceTypesInstanceTypeInfo] = None,
    ):
        self.instance_type_info = instance_type_info

    def validate(self):
        if self.instance_type_info:
            for k in self.instance_type_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceTypeInfo'] = []
        if self.instance_type_info is not None:
            for k in self.instance_type_info:
                result['InstanceTypeInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_type_info = []
        if m.get('InstanceTypeInfo') is not None:
            for k in m.get('InstanceTypeInfo'):
                temp_model = GetAutoScaleConfigResponseBodyQueuesQueueInfoInstanceTypesInstanceTypeInfo()
                self.instance_type_info.append(temp_model.from_map(k))
        return self


class GetAutoScaleConfigResponseBodyQueuesQueueInfo(TeaModel):
    def __init__(
        self,
        data_disks: GetAutoScaleConfigResponseBodyQueuesQueueInfoDataDisks = None,
        enable_auto_grow: bool = None,
        enable_auto_shrink: bool = None,
        host_name_prefix: str = None,
        host_name_suffix: str = None,
        instance_type: str = None,
        instance_types: GetAutoScaleConfigResponseBodyQueuesQueueInfoInstanceTypes = None,
        max_nodes_in_queue: int = None,
        max_nodes_per_cycle: int = None,
        min_nodes_in_queue: int = None,
        min_nodes_per_cycle: int = None,
        queue_image_id: str = None,
        queue_name: str = None,
        resource_group_id: str = None,
        spot_price_limit: float = None,
        spot_strategy: str = None,
        system_disk_category: str = None,
        system_disk_level: str = None,
        system_disk_size: int = None,
    ):
        self.data_disks = data_disks
        self.enable_auto_grow = enable_auto_grow
        self.enable_auto_shrink = enable_auto_shrink
        self.host_name_prefix = host_name_prefix
        self.host_name_suffix = host_name_suffix
        self.instance_type = instance_type
        self.instance_types = instance_types
        self.max_nodes_in_queue = max_nodes_in_queue
        self.max_nodes_per_cycle = max_nodes_per_cycle
        self.min_nodes_in_queue = min_nodes_in_queue
        self.min_nodes_per_cycle = min_nodes_per_cycle
        self.queue_image_id = queue_image_id
        self.queue_name = queue_name
        self.resource_group_id = resource_group_id
        self.spot_price_limit = spot_price_limit
        self.spot_strategy = spot_strategy
        self.system_disk_category = system_disk_category
        self.system_disk_level = system_disk_level
        self.system_disk_size = system_disk_size

    def validate(self):
        if self.data_disks:
            self.data_disks.validate()
        if self.instance_types:
            self.instance_types.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_disks is not None:
            result['DataDisks'] = self.data_disks.to_map()
        if self.enable_auto_grow is not None:
            result['EnableAutoGrow'] = self.enable_auto_grow
        if self.enable_auto_shrink is not None:
            result['EnableAutoShrink'] = self.enable_auto_shrink
        if self.host_name_prefix is not None:
            result['HostNamePrefix'] = self.host_name_prefix
        if self.host_name_suffix is not None:
            result['HostNameSuffix'] = self.host_name_suffix
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.instance_types is not None:
            result['InstanceTypes'] = self.instance_types.to_map()
        if self.max_nodes_in_queue is not None:
            result['MaxNodesInQueue'] = self.max_nodes_in_queue
        if self.max_nodes_per_cycle is not None:
            result['MaxNodesPerCycle'] = self.max_nodes_per_cycle
        if self.min_nodes_in_queue is not None:
            result['MinNodesInQueue'] = self.min_nodes_in_queue
        if self.min_nodes_per_cycle is not None:
            result['MinNodesPerCycle'] = self.min_nodes_per_cycle
        if self.queue_image_id is not None:
            result['QueueImageId'] = self.queue_image_id
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.spot_price_limit is not None:
            result['SpotPriceLimit'] = self.spot_price_limit
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        if self.system_disk_category is not None:
            result['SystemDiskCategory'] = self.system_disk_category
        if self.system_disk_level is not None:
            result['SystemDiskLevel'] = self.system_disk_level
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataDisks') is not None:
            temp_model = GetAutoScaleConfigResponseBodyQueuesQueueInfoDataDisks()
            self.data_disks = temp_model.from_map(m['DataDisks'])
        if m.get('EnableAutoGrow') is not None:
            self.enable_auto_grow = m.get('EnableAutoGrow')
        if m.get('EnableAutoShrink') is not None:
            self.enable_auto_shrink = m.get('EnableAutoShrink')
        if m.get('HostNamePrefix') is not None:
            self.host_name_prefix = m.get('HostNamePrefix')
        if m.get('HostNameSuffix') is not None:
            self.host_name_suffix = m.get('HostNameSuffix')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InstanceTypes') is not None:
            temp_model = GetAutoScaleConfigResponseBodyQueuesQueueInfoInstanceTypes()
            self.instance_types = temp_model.from_map(m['InstanceTypes'])
        if m.get('MaxNodesInQueue') is not None:
            self.max_nodes_in_queue = m.get('MaxNodesInQueue')
        if m.get('MaxNodesPerCycle') is not None:
            self.max_nodes_per_cycle = m.get('MaxNodesPerCycle')
        if m.get('MinNodesInQueue') is not None:
            self.min_nodes_in_queue = m.get('MinNodesInQueue')
        if m.get('MinNodesPerCycle') is not None:
            self.min_nodes_per_cycle = m.get('MinNodesPerCycle')
        if m.get('QueueImageId') is not None:
            self.queue_image_id = m.get('QueueImageId')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SpotPriceLimit') is not None:
            self.spot_price_limit = m.get('SpotPriceLimit')
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        if m.get('SystemDiskCategory') is not None:
            self.system_disk_category = m.get('SystemDiskCategory')
        if m.get('SystemDiskLevel') is not None:
            self.system_disk_level = m.get('SystemDiskLevel')
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        return self


class GetAutoScaleConfigResponseBodyQueues(TeaModel):
    def __init__(
        self,
        queue_info: List[GetAutoScaleConfigResponseBodyQueuesQueueInfo] = None,
    ):
        self.queue_info = queue_info

    def validate(self):
        if self.queue_info:
            for k in self.queue_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['QueueInfo'] = []
        if self.queue_info is not None:
            for k in self.queue_info:
                result['QueueInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.queue_info = []
        if m.get('QueueInfo') is not None:
            for k in m.get('QueueInfo'):
                temp_model = GetAutoScaleConfigResponseBodyQueuesQueueInfo()
                self.queue_info.append(temp_model.from_map(k))
        return self


class GetAutoScaleConfigResponseBody(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_type: str = None,
        enable_auto_grow: bool = None,
        enable_auto_shrink: bool = None,
        exclude_nodes: str = None,
        extra_nodes_grow_ratio: int = None,
        grow_interval_in_minutes: int = None,
        grow_ratio: int = None,
        grow_timeout_in_minutes: int = None,
        image_id: str = None,
        max_nodes_in_cluster: int = None,
        queues: GetAutoScaleConfigResponseBodyQueues = None,
        request_id: str = None,
        shrink_idle_times: int = None,
        shrink_interval_in_minutes: int = None,
        spot_price_limit: float = None,
        spot_strategy: str = None,
        uid: str = None,
    ):
        self.cluster_id = cluster_id
        self.cluster_type = cluster_type
        self.enable_auto_grow = enable_auto_grow
        self.enable_auto_shrink = enable_auto_shrink
        self.exclude_nodes = exclude_nodes
        self.extra_nodes_grow_ratio = extra_nodes_grow_ratio
        self.grow_interval_in_minutes = grow_interval_in_minutes
        self.grow_ratio = grow_ratio
        self.grow_timeout_in_minutes = grow_timeout_in_minutes
        self.image_id = image_id
        self.max_nodes_in_cluster = max_nodes_in_cluster
        self.queues = queues
        self.request_id = request_id
        self.shrink_idle_times = shrink_idle_times
        self.shrink_interval_in_minutes = shrink_interval_in_minutes
        self.spot_price_limit = spot_price_limit
        self.spot_strategy = spot_strategy
        self.uid = uid

    def validate(self):
        if self.queues:
            self.queues.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.enable_auto_grow is not None:
            result['EnableAutoGrow'] = self.enable_auto_grow
        if self.enable_auto_shrink is not None:
            result['EnableAutoShrink'] = self.enable_auto_shrink
        if self.exclude_nodes is not None:
            result['ExcludeNodes'] = self.exclude_nodes
        if self.extra_nodes_grow_ratio is not None:
            result['ExtraNodesGrowRatio'] = self.extra_nodes_grow_ratio
        if self.grow_interval_in_minutes is not None:
            result['GrowIntervalInMinutes'] = self.grow_interval_in_minutes
        if self.grow_ratio is not None:
            result['GrowRatio'] = self.grow_ratio
        if self.grow_timeout_in_minutes is not None:
            result['GrowTimeoutInMinutes'] = self.grow_timeout_in_minutes
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.max_nodes_in_cluster is not None:
            result['MaxNodesInCluster'] = self.max_nodes_in_cluster
        if self.queues is not None:
            result['Queues'] = self.queues.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.shrink_idle_times is not None:
            result['ShrinkIdleTimes'] = self.shrink_idle_times
        if self.shrink_interval_in_minutes is not None:
            result['ShrinkIntervalInMinutes'] = self.shrink_interval_in_minutes
        if self.spot_price_limit is not None:
            result['SpotPriceLimit'] = self.spot_price_limit
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('EnableAutoGrow') is not None:
            self.enable_auto_grow = m.get('EnableAutoGrow')
        if m.get('EnableAutoShrink') is not None:
            self.enable_auto_shrink = m.get('EnableAutoShrink')
        if m.get('ExcludeNodes') is not None:
            self.exclude_nodes = m.get('ExcludeNodes')
        if m.get('ExtraNodesGrowRatio') is not None:
            self.extra_nodes_grow_ratio = m.get('ExtraNodesGrowRatio')
        if m.get('GrowIntervalInMinutes') is not None:
            self.grow_interval_in_minutes = m.get('GrowIntervalInMinutes')
        if m.get('GrowRatio') is not None:
            self.grow_ratio = m.get('GrowRatio')
        if m.get('GrowTimeoutInMinutes') is not None:
            self.grow_timeout_in_minutes = m.get('GrowTimeoutInMinutes')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('MaxNodesInCluster') is not None:
            self.max_nodes_in_cluster = m.get('MaxNodesInCluster')
        if m.get('Queues') is not None:
            temp_model = GetAutoScaleConfigResponseBodyQueues()
            self.queues = temp_model.from_map(m['Queues'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ShrinkIdleTimes') is not None:
            self.shrink_idle_times = m.get('ShrinkIdleTimes')
        if m.get('ShrinkIntervalInMinutes') is not None:
            self.shrink_interval_in_minutes = m.get('ShrinkIntervalInMinutes')
        if m.get('SpotPriceLimit') is not None:
            self.spot_price_limit = m.get('SpotPriceLimit')
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class GetAutoScaleConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAutoScaleConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetAutoScaleConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCloudMetricLogsRequest(TeaModel):
    def __init__(
        self,
        aggregation_interval: int = None,
        aggregation_type: str = None,
        cluster_id: str = None,
        filter: str = None,
        from_: int = None,
        metric_categories: str = None,
        metric_scope: str = None,
        reverse: bool = None,
        to: int = None,
    ):
        self.aggregation_interval = aggregation_interval
        self.aggregation_type = aggregation_type
        self.cluster_id = cluster_id
        self.filter = filter
        self.from_ = from_
        self.metric_categories = metric_categories
        self.metric_scope = metric_scope
        self.reverse = reverse
        self.to = to

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregation_interval is not None:
            result['AggregationInterval'] = self.aggregation_interval
        if self.aggregation_type is not None:
            result['AggregationType'] = self.aggregation_type
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.from_ is not None:
            result['From'] = self.from_
        if self.metric_categories is not None:
            result['MetricCategories'] = self.metric_categories
        if self.metric_scope is not None:
            result['MetricScope'] = self.metric_scope
        if self.reverse is not None:
            result['Reverse'] = self.reverse
        if self.to is not None:
            result['To'] = self.to
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregationInterval') is not None:
            self.aggregation_interval = m.get('AggregationInterval')
        if m.get('AggregationType') is not None:
            self.aggregation_type = m.get('AggregationType')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('MetricCategories') is not None:
            self.metric_categories = m.get('MetricCategories')
        if m.get('MetricScope') is not None:
            self.metric_scope = m.get('MetricScope')
        if m.get('Reverse') is not None:
            self.reverse = m.get('Reverse')
        if m.get('To') is not None:
            self.to = m.get('To')
        return self


class GetCloudMetricLogsResponseBodyMetricLogsMetricLog(TeaModel):
    def __init__(
        self,
        disk_device: str = None,
        hostname: str = None,
        instance_id: str = None,
        metric_data: str = None,
        network_interface: str = None,
        time: int = None,
    ):
        self.disk_device = disk_device
        self.hostname = hostname
        self.instance_id = instance_id
        self.metric_data = metric_data
        self.network_interface = network_interface
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk_device is not None:
            result['DiskDevice'] = self.disk_device
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.metric_data is not None:
            result['MetricData'] = self.metric_data
        if self.network_interface is not None:
            result['NetworkInterface'] = self.network_interface
        if self.time is not None:
            result['Time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskDevice') is not None:
            self.disk_device = m.get('DiskDevice')
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MetricData') is not None:
            self.metric_data = m.get('MetricData')
        if m.get('NetworkInterface') is not None:
            self.network_interface = m.get('NetworkInterface')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        return self


class GetCloudMetricLogsResponseBodyMetricLogs(TeaModel):
    def __init__(
        self,
        metric_log: List[GetCloudMetricLogsResponseBodyMetricLogsMetricLog] = None,
    ):
        self.metric_log = metric_log

    def validate(self):
        if self.metric_log:
            for k in self.metric_log:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MetricLog'] = []
        if self.metric_log is not None:
            for k in self.metric_log:
                result['MetricLog'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.metric_log = []
        if m.get('MetricLog') is not None:
            for k in m.get('MetricLog'):
                temp_model = GetCloudMetricLogsResponseBodyMetricLogsMetricLog()
                self.metric_log.append(temp_model.from_map(k))
        return self


class GetCloudMetricLogsResponseBody(TeaModel):
    def __init__(
        self,
        metric_logs: GetCloudMetricLogsResponseBodyMetricLogs = None,
        request_id: str = None,
    ):
        self.metric_logs = metric_logs
        self.request_id = request_id

    def validate(self):
        if self.metric_logs:
            self.metric_logs.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metric_logs is not None:
            result['MetricLogs'] = self.metric_logs.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetricLogs') is not None:
            temp_model = GetCloudMetricLogsResponseBodyMetricLogs()
            self.metric_logs = temp_model.from_map(m['MetricLogs'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetCloudMetricLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCloudMetricLogsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetCloudMetricLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCloudMetricProfilingRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        profiling_id: str = None,
        region_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.profiling_id = profiling_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.profiling_id is not None:
            result['ProfilingId'] = self.profiling_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ProfilingId') is not None:
            self.profiling_id = m.get('ProfilingId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetCloudMetricProfilingResponseBodySvgUrlsSvgInfo(TeaModel):
    def __init__(
        self,
        name: str = None,
        size: int = None,
        type: str = None,
        url: str = None,
    ):
        self.name = name
        self.size = size
        self.type = type
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.size is not None:
            result['Size'] = self.size
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetCloudMetricProfilingResponseBodySvgUrls(TeaModel):
    def __init__(
        self,
        svg_info: List[GetCloudMetricProfilingResponseBodySvgUrlsSvgInfo] = None,
    ):
        self.svg_info = svg_info

    def validate(self):
        if self.svg_info:
            for k in self.svg_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SvgInfo'] = []
        if self.svg_info is not None:
            for k in self.svg_info:
                result['SvgInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.svg_info = []
        if m.get('SvgInfo') is not None:
            for k in m.get('SvgInfo'):
                temp_model = GetCloudMetricProfilingResponseBodySvgUrlsSvgInfo()
                self.svg_info.append(temp_model.from_map(k))
        return self


class GetCloudMetricProfilingResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        svg_urls: GetCloudMetricProfilingResponseBodySvgUrls = None,
    ):
        self.request_id = request_id
        self.svg_urls = svg_urls

    def validate(self):
        if self.svg_urls:
            self.svg_urls.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.svg_urls is not None:
            result['SvgUrls'] = self.svg_urls.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SvgUrls') is not None:
            temp_model = GetCloudMetricProfilingResponseBodySvgUrls()
            self.svg_urls = temp_model.from_map(m['SvgUrls'])
        return self


class GetCloudMetricProfilingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCloudMetricProfilingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetCloudMetricProfilingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetClusterVolumesRequest(TeaModel):
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


class GetClusterVolumesResponseBodyVolumesVolumeInfoRolesRoleInfo(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetClusterVolumesResponseBodyVolumesVolumeInfoRoles(TeaModel):
    def __init__(
        self,
        role_info: List[GetClusterVolumesResponseBodyVolumesVolumeInfoRolesRoleInfo] = None,
    ):
        self.role_info = role_info

    def validate(self):
        if self.role_info:
            for k in self.role_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RoleInfo'] = []
        if self.role_info is not None:
            for k in self.role_info:
                result['RoleInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.role_info = []
        if m.get('RoleInfo') is not None:
            for k in m.get('RoleInfo'):
                temp_model = GetClusterVolumesResponseBodyVolumesVolumeInfoRolesRoleInfo()
                self.role_info.append(temp_model.from_map(k))
        return self


class GetClusterVolumesResponseBodyVolumesVolumeInfo(TeaModel):
    def __init__(
        self,
        job_queue: str = None,
        local_directory: str = None,
        location: str = None,
        must_keep: bool = None,
        remote_directory: str = None,
        roles: GetClusterVolumesResponseBodyVolumesVolumeInfoRoles = None,
        volume_id: str = None,
        volume_mountpoint: str = None,
        volume_protocol: str = None,
        volume_type: str = None,
    ):
        self.job_queue = job_queue
        self.local_directory = local_directory
        self.location = location
        self.must_keep = must_keep
        self.remote_directory = remote_directory
        self.roles = roles
        self.volume_id = volume_id
        self.volume_mountpoint = volume_mountpoint
        self.volume_protocol = volume_protocol
        self.volume_type = volume_type

    def validate(self):
        if self.roles:
            self.roles.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_queue is not None:
            result['JobQueue'] = self.job_queue
        if self.local_directory is not None:
            result['LocalDirectory'] = self.local_directory
        if self.location is not None:
            result['Location'] = self.location
        if self.must_keep is not None:
            result['MustKeep'] = self.must_keep
        if self.remote_directory is not None:
            result['RemoteDirectory'] = self.remote_directory
        if self.roles is not None:
            result['Roles'] = self.roles.to_map()
        if self.volume_id is not None:
            result['VolumeId'] = self.volume_id
        if self.volume_mountpoint is not None:
            result['VolumeMountpoint'] = self.volume_mountpoint
        if self.volume_protocol is not None:
            result['VolumeProtocol'] = self.volume_protocol
        if self.volume_type is not None:
            result['VolumeType'] = self.volume_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobQueue') is not None:
            self.job_queue = m.get('JobQueue')
        if m.get('LocalDirectory') is not None:
            self.local_directory = m.get('LocalDirectory')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('MustKeep') is not None:
            self.must_keep = m.get('MustKeep')
        if m.get('RemoteDirectory') is not None:
            self.remote_directory = m.get('RemoteDirectory')
        if m.get('Roles') is not None:
            temp_model = GetClusterVolumesResponseBodyVolumesVolumeInfoRoles()
            self.roles = temp_model.from_map(m['Roles'])
        if m.get('VolumeId') is not None:
            self.volume_id = m.get('VolumeId')
        if m.get('VolumeMountpoint') is not None:
            self.volume_mountpoint = m.get('VolumeMountpoint')
        if m.get('VolumeProtocol') is not None:
            self.volume_protocol = m.get('VolumeProtocol')
        if m.get('VolumeType') is not None:
            self.volume_type = m.get('VolumeType')
        return self


class GetClusterVolumesResponseBodyVolumes(TeaModel):
    def __init__(
        self,
        volume_info: List[GetClusterVolumesResponseBodyVolumesVolumeInfo] = None,
    ):
        self.volume_info = volume_info

    def validate(self):
        if self.volume_info:
            for k in self.volume_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['VolumeInfo'] = []
        if self.volume_info is not None:
            for k in self.volume_info:
                result['VolumeInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.volume_info = []
        if m.get('VolumeInfo') is not None:
            for k in m.get('VolumeInfo'):
                temp_model = GetClusterVolumesResponseBodyVolumesVolumeInfo()
                self.volume_info.append(temp_model.from_map(k))
        return self


class GetClusterVolumesResponseBody(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        request_id: str = None,
        volumes: GetClusterVolumesResponseBodyVolumes = None,
    ):
        self.region_id = region_id
        self.request_id = request_id
        self.volumes = volumes

    def validate(self):
        if self.volumes:
            self.volumes.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.volumes is not None:
            result['Volumes'] = self.volumes.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Volumes') is not None:
            temp_model = GetClusterVolumesResponseBodyVolumes()
            self.volumes = temp_model.from_map(m['Volumes'])
        return self


class GetClusterVolumesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetClusterVolumesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetClusterVolumesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCommonImageRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        contain_type: str = None,
        image_name: str = None,
        region_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.contain_type = contain_type
        self.image_name = image_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.contain_type is not None:
            result['ContainType'] = self.contain_type
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ContainType') is not None:
            self.contain_type = m.get('ContainType')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetCommonImageResponseBody(TeaModel):
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


class GetCommonImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCommonImageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetCommonImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGWSConnectTicketRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        instance_id: str = None,
    ):
        self.app_name = app_name
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetGWSConnectTicketResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        ticket: str = None,
    ):
        self.request_id = request_id
        self.ticket = ticket

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.ticket is not None:
            result['Ticket'] = self.ticket
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Ticket') is not None:
            self.ticket = m.get('Ticket')
        return self


class GetGWSConnectTicketResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetGWSConnectTicketResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetGWSConnectTicketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHybridClusterConfigRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        node: str = None,
    ):
        self.cluster_id = cluster_id
        self.node = node

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.node is not None:
            result['Node'] = self.node
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Node') is not None:
            self.node = m.get('Node')
        return self


class GetHybridClusterConfigResponseBody(TeaModel):
    def __init__(
        self,
        cluster_config: str = None,
        request_id: str = None,
    ):
        self.cluster_config = cluster_config
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_config is not None:
            result['ClusterConfig'] = self.cluster_config
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterConfig') is not None:
            self.cluster_config = m.get('ClusterConfig')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetHybridClusterConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetHybridClusterConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetHybridClusterConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetIfEcsTypeSupportHtConfigRequest(TeaModel):
    def __init__(
        self,
        instance_type: str = None,
    ):
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class GetIfEcsTypeSupportHtConfigResponseBody(TeaModel):
    def __init__(
        self,
        default_ht_enabled: bool = None,
        instance_type: str = None,
        request_id: str = None,
        support_ht_config: bool = None,
    ):
        self.default_ht_enabled = default_ht_enabled
        self.instance_type = instance_type
        self.request_id = request_id
        self.support_ht_config = support_ht_config

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_ht_enabled is not None:
            result['DefaultHtEnabled'] = self.default_ht_enabled
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.support_ht_config is not None:
            result['SupportHtConfig'] = self.support_ht_config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultHtEnabled') is not None:
            self.default_ht_enabled = m.get('DefaultHtEnabled')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SupportHtConfig') is not None:
            self.support_ht_config = m.get('SupportHtConfig')
        return self


class GetIfEcsTypeSupportHtConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetIfEcsTypeSupportHtConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetIfEcsTypeSupportHtConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJobLogRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        exec_host: str = None,
        job_id: str = None,
        offset: int = None,
        size: int = None,
    ):
        self.cluster_id = cluster_id
        self.exec_host = exec_host
        self.job_id = job_id
        self.offset = offset
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.exec_host is not None:
            result['ExecHost'] = self.exec_host
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ExecHost') is not None:
            self.exec_host = m.get('ExecHost')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class GetJobLogResponseBody(TeaModel):
    def __init__(
        self,
        error_log: str = None,
        job_id: str = None,
        output_log: str = None,
        request_id: str = None,
    ):
        self.error_log = error_log
        self.job_id = job_id
        self.output_log = output_log
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_log is not None:
            result['ErrorLog'] = self.error_log
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.output_log is not None:
            result['OutputLog'] = self.output_log
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorLog') is not None:
            self.error_log = m.get('ErrorLog')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('OutputLog') is not None:
            self.output_log = m.get('OutputLog')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetJobLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetJobLogResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetJobLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPostScriptsRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        region_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetPostScriptsResponseBodyPostInstallScripts(TeaModel):
    def __init__(
        self,
        args: str = None,
        url: str = None,
    ):
        self.args = args
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.args is not None:
            result['Args'] = self.args
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Args') is not None:
            self.args = m.get('Args')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetPostScriptsResponseBody(TeaModel):
    def __init__(
        self,
        post_install_scripts: List[GetPostScriptsResponseBodyPostInstallScripts] = None,
        request_id: str = None,
    ):
        self.post_install_scripts = post_install_scripts
        self.request_id = request_id

    def validate(self):
        if self.post_install_scripts:
            for k in self.post_install_scripts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PostInstallScripts'] = []
        if self.post_install_scripts is not None:
            for k in self.post_install_scripts:
                result['PostInstallScripts'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.post_install_scripts = []
        if m.get('PostInstallScripts') is not None:
            for k in m.get('PostInstallScripts'):
                temp_model = GetPostScriptsResponseBodyPostInstallScripts()
                self.post_install_scripts.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPostScriptsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPostScriptsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetPostScriptsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSchedulerInfoRequestScheduler(TeaModel):
    def __init__(
        self,
        sched_name: str = None,
    ):
        self.sched_name = sched_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sched_name is not None:
            result['SchedName'] = self.sched_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SchedName') is not None:
            self.sched_name = m.get('SchedName')
        return self


class GetSchedulerInfoRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        region_id: str = None,
        scheduler: List[GetSchedulerInfoRequestScheduler] = None,
    ):
        self.cluster_id = cluster_id
        self.region_id = region_id
        self.scheduler = scheduler

    def validate(self):
        if self.scheduler:
            for k in self.scheduler:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['Scheduler'] = []
        if self.scheduler is not None:
            for k in self.scheduler:
                result['Scheduler'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.scheduler = []
        if m.get('Scheduler') is not None:
            for k in m.get('Scheduler'):
                temp_model = GetSchedulerInfoRequestScheduler()
                self.scheduler.append(temp_model.from_map(k))
        return self


class GetSchedulerInfoResponseBodySchedInfo(TeaModel):
    def __init__(
        self,
        configuration: str = None,
        sched_name: str = None,
    ):
        self.configuration = configuration
        self.sched_name = sched_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.configuration is not None:
            result['Configuration'] = self.configuration
        if self.sched_name is not None:
            result['SchedName'] = self.sched_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Configuration') is not None:
            self.configuration = m.get('Configuration')
        if m.get('SchedName') is not None:
            self.sched_name = m.get('SchedName')
        return self


class GetSchedulerInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        sched_info: List[GetSchedulerInfoResponseBodySchedInfo] = None,
    ):
        self.request_id = request_id
        self.sched_info = sched_info

    def validate(self):
        if self.sched_info:
            for k in self.sched_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SchedInfo'] = []
        if self.sched_info is not None:
            for k in self.sched_info:
                result['SchedInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.sched_info = []
        if m.get('SchedInfo') is not None:
            for k in m.get('SchedInfo'):
                temp_model = GetSchedulerInfoResponseBodySchedInfo()
                self.sched_info.append(temp_model.from_map(k))
        return self


class GetSchedulerInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSchedulerInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetSchedulerInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserImageRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        container_type: str = None,
        image_name: str = None,
        image_path: str = None,
        ossbucket: str = None,
        ossend_point: str = None,
    ):
        self.cluster_id = cluster_id
        self.container_type = container_type
        self.image_name = image_name
        self.image_path = image_path
        self.ossbucket = ossbucket
        self.ossend_point = ossend_point

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.container_type is not None:
            result['ContainerType'] = self.container_type
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.image_path is not None:
            result['ImagePath'] = self.image_path
        if self.ossbucket is not None:
            result['OSSBucket'] = self.ossbucket
        if self.ossend_point is not None:
            result['OSSEndPoint'] = self.ossend_point
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ContainerType') is not None:
            self.container_type = m.get('ContainerType')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('ImagePath') is not None:
            self.image_path = m.get('ImagePath')
        if m.get('OSSBucket') is not None:
            self.ossbucket = m.get('OSSBucket')
        if m.get('OSSEndPoint') is not None:
            self.ossend_point = m.get('OSSEndPoint')
        return self


class GetUserImageResponseBody(TeaModel):
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


class GetUserImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserImageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetUserImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVisualServiceStatusRequest(TeaModel):
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


class GetVisualServiceStatusResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
    ):
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetVisualServiceStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetVisualServiceStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetVisualServiceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InitializeEHPCRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class InitializeEHPCResponseBody(TeaModel):
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


class InitializeEHPCResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InitializeEHPCResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = InitializeEHPCResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InspectImageRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        container_type: str = None,
        image_name: str = None,
    ):
        self.cluster_id = cluster_id
        self.container_type = container_type
        self.image_name = image_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.container_type is not None:
            result['ContainerType'] = self.container_type
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ContainerType') is not None:
            self.container_type = m.get('ContainerType')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        return self


class InspectImageResponseBodyImageStatusImageInspectInfo(TeaModel):
    def __init__(
        self,
        boot_strap: str = None,
        build_arch: str = None,
        build_date: str = None,
        container_version: str = None,
        def_from: str = None,
        schema_version: str = None,
    ):
        self.boot_strap = boot_strap
        self.build_arch = build_arch
        self.build_date = build_date
        self.container_version = container_version
        self.def_from = def_from
        self.schema_version = schema_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.boot_strap is not None:
            result['BootStrap'] = self.boot_strap
        if self.build_arch is not None:
            result['BuildArch'] = self.build_arch
        if self.build_date is not None:
            result['BuildDate'] = self.build_date
        if self.container_version is not None:
            result['ContainerVersion'] = self.container_version
        if self.def_from is not None:
            result['DefFrom'] = self.def_from
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BootStrap') is not None:
            self.boot_strap = m.get('BootStrap')
        if m.get('BuildArch') is not None:
            self.build_arch = m.get('BuildArch')
        if m.get('BuildDate') is not None:
            self.build_date = m.get('BuildDate')
        if m.get('ContainerVersion') is not None:
            self.container_version = m.get('ContainerVersion')
        if m.get('DefFrom') is not None:
            self.def_from = m.get('DefFrom')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        return self


class InspectImageResponseBodyImageStatus(TeaModel):
    def __init__(
        self,
        image_inspect_info: InspectImageResponseBodyImageStatusImageInspectInfo = None,
    ):
        self.image_inspect_info = image_inspect_info

    def validate(self):
        if self.image_inspect_info:
            self.image_inspect_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_inspect_info is not None:
            result['ImageInspectInfo'] = self.image_inspect_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageInspectInfo') is not None:
            temp_model = InspectImageResponseBodyImageStatusImageInspectInfo()
            self.image_inspect_info = temp_model.from_map(m['ImageInspectInfo'])
        return self


class InspectImageResponseBody(TeaModel):
    def __init__(
        self,
        image_status: InspectImageResponseBodyImageStatus = None,
        request_id: str = None,
    ):
        self.image_status = image_status
        self.request_id = request_id

    def validate(self):
        if self.image_status:
            self.image_status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_status is not None:
            result['ImageStatus'] = self.image_status.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageStatus') is not None:
            temp_model = InspectImageResponseBodyImageStatus()
            self.image_status = temp_model.from_map(m['ImageStatus'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class InspectImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InspectImageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = InspectImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InstallSoftwareRequest(TeaModel):
    def __init__(
        self,
        application: str = None,
        cluster_id: str = None,
    ):
        self.application = application
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application is not None:
            result['Application'] = self.application
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Application') is not None:
            self.application = m.get('Application')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class InstallSoftwareResponseBody(TeaModel):
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


class InstallSoftwareResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InstallSoftwareResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = InstallSoftwareResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InvokeShellCommandRequestInstance(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class InvokeShellCommandRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        command: str = None,
        instance: List[InvokeShellCommandRequestInstance] = None,
        timeout: int = None,
        working_dir: str = None,
    ):
        self.cluster_id = cluster_id
        self.command = command
        self.instance = instance
        self.timeout = timeout
        self.working_dir = working_dir

    def validate(self):
        if self.instance:
            for k in self.instance:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.command is not None:
            result['Command'] = self.command
        result['Instance'] = []
        if self.instance is not None:
            for k in self.instance:
                result['Instance'].append(k.to_map() if k else None)
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.working_dir is not None:
            result['WorkingDir'] = self.working_dir
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Command') is not None:
            self.command = m.get('Command')
        self.instance = []
        if m.get('Instance') is not None:
            for k in m.get('Instance'):
                temp_model = InvokeShellCommandRequestInstance()
                self.instance.append(temp_model.from_map(k))
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')
        return self


class InvokeShellCommandResponseBodyInstanceIds(TeaModel):
    def __init__(
        self,
        instance_id: List[str] = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class InvokeShellCommandResponseBody(TeaModel):
    def __init__(
        self,
        command_id: str = None,
        instance_ids: InvokeShellCommandResponseBodyInstanceIds = None,
        request_id: str = None,
    ):
        self.command_id = command_id
        self.instance_ids = instance_ids
        self.request_id = request_id

    def validate(self):
        if self.instance_ids:
            self.instance_ids.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command_id is not None:
            result['CommandId'] = self.command_id
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandId') is not None:
            self.command_id = m.get('CommandId')
        if m.get('InstanceIds') is not None:
            temp_model = InvokeShellCommandResponseBodyInstanceIds()
            self.instance_ids = temp_model.from_map(m['InstanceIds'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class InvokeShellCommandResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InvokeShellCommandResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = InvokeShellCommandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAvailableEcsTypesRequest(TeaModel):
    def __init__(
        self,
        instance_charge_type: str = None,
        show_sold_out: bool = None,
        spot_strategy: str = None,
        zone_id: str = None,
    ):
        self.instance_charge_type = instance_charge_type
        self.show_sold_out = show_sold_out
        self.spot_strategy = spot_strategy
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type
        if self.show_sold_out is not None:
            result['ShowSoldOut'] = self.show_sold_out
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')
        if m.get('ShowSoldOut') is not None:
            self.show_sold_out = m.get('ShowSoldOut')
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListAvailableEcsTypesResponseBodyInstanceTypeFamiliesInstanceTypeFamilyInfoTypesTypesInfoZoneIds(TeaModel):
    def __init__(
        self,
        zone_id: List[str] = None,
    ):
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListAvailableEcsTypesResponseBodyInstanceTypeFamiliesInstanceTypeFamilyInfoTypesTypesInfo(TeaModel):
    def __init__(
        self,
        cpu_core_count: int = None,
        eni_quantity: int = None,
        gpuamount: int = None,
        gpuspec: str = None,
        instance_bandwidth_rx: int = None,
        instance_bandwidth_tx: int = None,
        instance_pps_rx: int = None,
        instance_pps_tx: int = None,
        instance_type_id: str = None,
        memory_size: int = None,
        status: str = None,
        zone_ids: ListAvailableEcsTypesResponseBodyInstanceTypeFamiliesInstanceTypeFamilyInfoTypesTypesInfoZoneIds = None,
    ):
        self.cpu_core_count = cpu_core_count
        self.eni_quantity = eni_quantity
        self.gpuamount = gpuamount
        self.gpuspec = gpuspec
        self.instance_bandwidth_rx = instance_bandwidth_rx
        self.instance_bandwidth_tx = instance_bandwidth_tx
        self.instance_pps_rx = instance_pps_rx
        self.instance_pps_tx = instance_pps_tx
        self.instance_type_id = instance_type_id
        self.memory_size = memory_size
        self.status = status
        self.zone_ids = zone_ids

    def validate(self):
        if self.zone_ids:
            self.zone_ids.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_core_count is not None:
            result['CpuCoreCount'] = self.cpu_core_count
        if self.eni_quantity is not None:
            result['EniQuantity'] = self.eni_quantity
        if self.gpuamount is not None:
            result['GPUAmount'] = self.gpuamount
        if self.gpuspec is not None:
            result['GPUSpec'] = self.gpuspec
        if self.instance_bandwidth_rx is not None:
            result['InstanceBandwidthRx'] = self.instance_bandwidth_rx
        if self.instance_bandwidth_tx is not None:
            result['InstanceBandwidthTx'] = self.instance_bandwidth_tx
        if self.instance_pps_rx is not None:
            result['InstancePpsRx'] = self.instance_pps_rx
        if self.instance_pps_tx is not None:
            result['InstancePpsTx'] = self.instance_pps_tx
        if self.instance_type_id is not None:
            result['InstanceTypeId'] = self.instance_type_id
        if self.memory_size is not None:
            result['MemorySize'] = self.memory_size
        if self.status is not None:
            result['Status'] = self.status
        if self.zone_ids is not None:
            result['ZoneIds'] = self.zone_ids.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuCoreCount') is not None:
            self.cpu_core_count = m.get('CpuCoreCount')
        if m.get('EniQuantity') is not None:
            self.eni_quantity = m.get('EniQuantity')
        if m.get('GPUAmount') is not None:
            self.gpuamount = m.get('GPUAmount')
        if m.get('GPUSpec') is not None:
            self.gpuspec = m.get('GPUSpec')
        if m.get('InstanceBandwidthRx') is not None:
            self.instance_bandwidth_rx = m.get('InstanceBandwidthRx')
        if m.get('InstanceBandwidthTx') is not None:
            self.instance_bandwidth_tx = m.get('InstanceBandwidthTx')
        if m.get('InstancePpsRx') is not None:
            self.instance_pps_rx = m.get('InstancePpsRx')
        if m.get('InstancePpsTx') is not None:
            self.instance_pps_tx = m.get('InstancePpsTx')
        if m.get('InstanceTypeId') is not None:
            self.instance_type_id = m.get('InstanceTypeId')
        if m.get('MemorySize') is not None:
            self.memory_size = m.get('MemorySize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ZoneIds') is not None:
            temp_model = ListAvailableEcsTypesResponseBodyInstanceTypeFamiliesInstanceTypeFamilyInfoTypesTypesInfoZoneIds()
            self.zone_ids = temp_model.from_map(m['ZoneIds'])
        return self


class ListAvailableEcsTypesResponseBodyInstanceTypeFamiliesInstanceTypeFamilyInfoTypes(TeaModel):
    def __init__(
        self,
        types_info: List[ListAvailableEcsTypesResponseBodyInstanceTypeFamiliesInstanceTypeFamilyInfoTypesTypesInfo] = None,
    ):
        self.types_info = types_info

    def validate(self):
        if self.types_info:
            for k in self.types_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TypesInfo'] = []
        if self.types_info is not None:
            for k in self.types_info:
                result['TypesInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.types_info = []
        if m.get('TypesInfo') is not None:
            for k in m.get('TypesInfo'):
                temp_model = ListAvailableEcsTypesResponseBodyInstanceTypeFamiliesInstanceTypeFamilyInfoTypesTypesInfo()
                self.types_info.append(temp_model.from_map(k))
        return self


class ListAvailableEcsTypesResponseBodyInstanceTypeFamiliesInstanceTypeFamilyInfo(TeaModel):
    def __init__(
        self,
        generation: str = None,
        instance_type_family_id: str = None,
        types: ListAvailableEcsTypesResponseBodyInstanceTypeFamiliesInstanceTypeFamilyInfoTypes = None,
    ):
        self.generation = generation
        self.instance_type_family_id = instance_type_family_id
        self.types = types

    def validate(self):
        if self.types:
            self.types.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.generation is not None:
            result['Generation'] = self.generation
        if self.instance_type_family_id is not None:
            result['InstanceTypeFamilyId'] = self.instance_type_family_id
        if self.types is not None:
            result['Types'] = self.types.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Generation') is not None:
            self.generation = m.get('Generation')
        if m.get('InstanceTypeFamilyId') is not None:
            self.instance_type_family_id = m.get('InstanceTypeFamilyId')
        if m.get('Types') is not None:
            temp_model = ListAvailableEcsTypesResponseBodyInstanceTypeFamiliesInstanceTypeFamilyInfoTypes()
            self.types = temp_model.from_map(m['Types'])
        return self


class ListAvailableEcsTypesResponseBodyInstanceTypeFamilies(TeaModel):
    def __init__(
        self,
        instance_type_family_info: List[ListAvailableEcsTypesResponseBodyInstanceTypeFamiliesInstanceTypeFamilyInfo] = None,
    ):
        self.instance_type_family_info = instance_type_family_info

    def validate(self):
        if self.instance_type_family_info:
            for k in self.instance_type_family_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceTypeFamilyInfo'] = []
        if self.instance_type_family_info is not None:
            for k in self.instance_type_family_info:
                result['InstanceTypeFamilyInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_type_family_info = []
        if m.get('InstanceTypeFamilyInfo') is not None:
            for k in m.get('InstanceTypeFamilyInfo'):
                temp_model = ListAvailableEcsTypesResponseBodyInstanceTypeFamiliesInstanceTypeFamilyInfo()
                self.instance_type_family_info.append(temp_model.from_map(k))
        return self


class ListAvailableEcsTypesResponseBody(TeaModel):
    def __init__(
        self,
        instance_type_families: ListAvailableEcsTypesResponseBodyInstanceTypeFamilies = None,
        request_id: str = None,
        support_spot_instance: bool = None,
    ):
        self.instance_type_families = instance_type_families
        self.request_id = request_id
        self.support_spot_instance = support_spot_instance

    def validate(self):
        if self.instance_type_families:
            self.instance_type_families.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type_families is not None:
            result['InstanceTypeFamilies'] = self.instance_type_families.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.support_spot_instance is not None:
            result['SupportSpotInstance'] = self.support_spot_instance
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceTypeFamilies') is not None:
            temp_model = ListAvailableEcsTypesResponseBodyInstanceTypeFamilies()
            self.instance_type_families = temp_model.from_map(m['InstanceTypeFamilies'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SupportSpotInstance') is not None:
            self.support_spot_instance = m.get('SupportSpotInstance')
        return self


class ListAvailableEcsTypesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAvailableEcsTypesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListAvailableEcsTypesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCloudMetricProfilingsRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
    ):
        self.cluster_id = cluster_id
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
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListCloudMetricProfilingsResponseBodyProfilingsProfilingInfo(TeaModel):
    def __init__(
        self,
        duration: int = None,
        freq: int = None,
        host_name: str = None,
        instance_id: str = None,
        pid: int = None,
        profiling_id: str = None,
        trigger_time: str = None,
    ):
        self.duration = duration
        self.freq = freq
        self.host_name = host_name
        self.instance_id = instance_id
        self.pid = pid
        self.profiling_id = profiling_id
        self.trigger_time = trigger_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.freq is not None:
            result['Freq'] = self.freq
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.profiling_id is not None:
            result['ProfilingId'] = self.profiling_id
        if self.trigger_time is not None:
            result['TriggerTime'] = self.trigger_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Freq') is not None:
            self.freq = m.get('Freq')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('ProfilingId') is not None:
            self.profiling_id = m.get('ProfilingId')
        if m.get('TriggerTime') is not None:
            self.trigger_time = m.get('TriggerTime')
        return self


class ListCloudMetricProfilingsResponseBodyProfilings(TeaModel):
    def __init__(
        self,
        profiling_info: List[ListCloudMetricProfilingsResponseBodyProfilingsProfilingInfo] = None,
    ):
        self.profiling_info = profiling_info

    def validate(self):
        if self.profiling_info:
            for k in self.profiling_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ProfilingInfo'] = []
        if self.profiling_info is not None:
            for k in self.profiling_info:
                result['ProfilingInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.profiling_info = []
        if m.get('ProfilingInfo') is not None:
            for k in m.get('ProfilingInfo'):
                temp_model = ListCloudMetricProfilingsResponseBodyProfilingsProfilingInfo()
                self.profiling_info.append(temp_model.from_map(k))
        return self


class ListCloudMetricProfilingsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        profilings: ListCloudMetricProfilingsResponseBodyProfilings = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.profilings = profilings
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.profilings:
            self.profilings.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.profilings is not None:
            result['Profilings'] = self.profilings.to_map()
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
        if m.get('Profilings') is not None:
            temp_model = ListCloudMetricProfilingsResponseBodyProfilings()
            self.profilings = temp_model.from_map(m['Profilings'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListCloudMetricProfilingsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCloudMetricProfilingsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListCloudMetricProfilingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClusterLogsRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
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


class ListClusterLogsResponseBodyLogsLogInfo(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        level: str = None,
        message: str = None,
        operation: str = None,
    ):
        self.create_time = create_time
        self.level = level
        self.message = message
        self.operation = operation

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.level is not None:
            result['Level'] = self.level
        if self.message is not None:
            result['Message'] = self.message
        if self.operation is not None:
            result['Operation'] = self.operation
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        return self


class ListClusterLogsResponseBodyLogs(TeaModel):
    def __init__(
        self,
        log_info: List[ListClusterLogsResponseBodyLogsLogInfo] = None,
    ):
        self.log_info = log_info

    def validate(self):
        if self.log_info:
            for k in self.log_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LogInfo'] = []
        if self.log_info is not None:
            for k in self.log_info:
                result['LogInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.log_info = []
        if m.get('LogInfo') is not None:
            for k in m.get('LogInfo'):
                temp_model = ListClusterLogsResponseBodyLogsLogInfo()
                self.log_info.append(temp_model.from_map(k))
        return self


class ListClusterLogsResponseBody(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        logs: ListClusterLogsResponseBodyLogs = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.cluster_id = cluster_id
        self.logs = logs
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.logs:
            self.logs.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.logs is not None:
            result['Logs'] = self.logs.to_map()
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
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Logs') is not None:
            temp_model = ListClusterLogsResponseBodyLogs()
            self.logs = temp_model.from_map(m['Logs'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListClusterLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListClusterLogsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListClusterLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClustersRequest(TeaModel):
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


class ListClustersResponseBodyClustersClusterInfoSimpleComputes(TeaModel):
    def __init__(
        self,
        exception_count: int = None,
        normal_count: int = None,
        operating_count: int = None,
        stopped_count: int = None,
        total: int = None,
    ):
        self.exception_count = exception_count
        self.normal_count = normal_count
        self.operating_count = operating_count
        self.stopped_count = stopped_count
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exception_count is not None:
            result['ExceptionCount'] = self.exception_count
        if self.normal_count is not None:
            result['NormalCount'] = self.normal_count
        if self.operating_count is not None:
            result['OperatingCount'] = self.operating_count
        if self.stopped_count is not None:
            result['StoppedCount'] = self.stopped_count
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExceptionCount') is not None:
            self.exception_count = m.get('ExceptionCount')
        if m.get('NormalCount') is not None:
            self.normal_count = m.get('NormalCount')
        if m.get('OperatingCount') is not None:
            self.operating_count = m.get('OperatingCount')
        if m.get('StoppedCount') is not None:
            self.stopped_count = m.get('StoppedCount')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListClustersResponseBodyClustersClusterInfoSimpleManagers(TeaModel):
    def __init__(
        self,
        exception_count: int = None,
        normal_count: int = None,
        operating_count: int = None,
        stopped_count: int = None,
        total: int = None,
    ):
        self.exception_count = exception_count
        self.normal_count = normal_count
        self.operating_count = operating_count
        self.stopped_count = stopped_count
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exception_count is not None:
            result['ExceptionCount'] = self.exception_count
        if self.normal_count is not None:
            result['NormalCount'] = self.normal_count
        if self.operating_count is not None:
            result['OperatingCount'] = self.operating_count
        if self.stopped_count is not None:
            result['StoppedCount'] = self.stopped_count
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExceptionCount') is not None:
            self.exception_count = m.get('ExceptionCount')
        if m.get('NormalCount') is not None:
            self.normal_count = m.get('NormalCount')
        if m.get('OperatingCount') is not None:
            self.operating_count = m.get('OperatingCount')
        if m.get('StoppedCount') is not None:
            self.stopped_count = m.get('StoppedCount')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListClustersResponseBodyClustersClusterInfoSimpleTotalResources(TeaModel):
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


class ListClustersResponseBodyClustersClusterInfoSimpleUsedResources(TeaModel):
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


class ListClustersResponseBodyClustersClusterInfoSimple(TeaModel):
    def __init__(
        self,
        account_type: str = None,
        base_os_tag: str = None,
        client_version: str = None,
        compute_spot_price_limit: float = None,
        compute_spot_strategy: str = None,
        computes: ListClustersResponseBodyClustersClusterInfoSimpleComputes = None,
        count: int = None,
        create_time: str = None,
        deploy_mode: str = None,
        description: str = None,
        ehpc_version: str = None,
        has_plugin: bool = None,
        id: str = None,
        image_id: str = None,
        image_owner_alias: str = None,
        instance_charge_type: str = None,
        instance_type: str = None,
        is_compute_ess: bool = None,
        location: str = None,
        login_nodes: str = None,
        managers: ListClustersResponseBodyClustersClusterInfoSimpleManagers = None,
        name: str = None,
        node_prefix: str = None,
        node_suffix: str = None,
        os_tag: str = None,
        region_id: str = None,
        scheduler_type: str = None,
        status: str = None,
        total_resources: ListClustersResponseBodyClustersClusterInfoSimpleTotalResources = None,
        used_resources: ListClustersResponseBodyClustersClusterInfoSimpleUsedResources = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        self.account_type = account_type
        self.base_os_tag = base_os_tag
        self.client_version = client_version
        self.compute_spot_price_limit = compute_spot_price_limit
        self.compute_spot_strategy = compute_spot_strategy
        self.computes = computes
        self.count = count
        self.create_time = create_time
        self.deploy_mode = deploy_mode
        self.description = description
        self.ehpc_version = ehpc_version
        self.has_plugin = has_plugin
        self.id = id
        self.image_id = image_id
        self.image_owner_alias = image_owner_alias
        self.instance_charge_type = instance_charge_type
        self.instance_type = instance_type
        self.is_compute_ess = is_compute_ess
        self.location = location
        self.login_nodes = login_nodes
        self.managers = managers
        self.name = name
        self.node_prefix = node_prefix
        self.node_suffix = node_suffix
        self.os_tag = os_tag
        self.region_id = region_id
        self.scheduler_type = scheduler_type
        self.status = status
        self.total_resources = total_resources
        self.used_resources = used_resources
        self.v_switch_id = v_switch_id
        self.vpc_id = vpc_id
        self.zone_id = zone_id

    def validate(self):
        if self.computes:
            self.computes.validate()
        if self.managers:
            self.managers.validate()
        if self.total_resources:
            self.total_resources.validate()
        if self.used_resources:
            self.used_resources.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.base_os_tag is not None:
            result['BaseOsTag'] = self.base_os_tag
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.compute_spot_price_limit is not None:
            result['ComputeSpotPriceLimit'] = self.compute_spot_price_limit
        if self.compute_spot_strategy is not None:
            result['ComputeSpotStrategy'] = self.compute_spot_strategy
        if self.computes is not None:
            result['Computes'] = self.computes.to_map()
        if self.count is not None:
            result['Count'] = self.count
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deploy_mode is not None:
            result['DeployMode'] = self.deploy_mode
        if self.description is not None:
            result['Description'] = self.description
        if self.ehpc_version is not None:
            result['EhpcVersion'] = self.ehpc_version
        if self.has_plugin is not None:
            result['HasPlugin'] = self.has_plugin
        if self.id is not None:
            result['Id'] = self.id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_owner_alias is not None:
            result['ImageOwnerAlias'] = self.image_owner_alias
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.is_compute_ess is not None:
            result['IsComputeEss'] = self.is_compute_ess
        if self.location is not None:
            result['Location'] = self.location
        if self.login_nodes is not None:
            result['LoginNodes'] = self.login_nodes
        if self.managers is not None:
            result['Managers'] = self.managers.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.node_prefix is not None:
            result['NodePrefix'] = self.node_prefix
        if self.node_suffix is not None:
            result['NodeSuffix'] = self.node_suffix
        if self.os_tag is not None:
            result['OsTag'] = self.os_tag
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scheduler_type is not None:
            result['SchedulerType'] = self.scheduler_type
        if self.status is not None:
            result['Status'] = self.status
        if self.total_resources is not None:
            result['TotalResources'] = self.total_resources.to_map()
        if self.used_resources is not None:
            result['UsedResources'] = self.used_resources.to_map()
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('BaseOsTag') is not None:
            self.base_os_tag = m.get('BaseOsTag')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('ComputeSpotPriceLimit') is not None:
            self.compute_spot_price_limit = m.get('ComputeSpotPriceLimit')
        if m.get('ComputeSpotStrategy') is not None:
            self.compute_spot_strategy = m.get('ComputeSpotStrategy')
        if m.get('Computes') is not None:
            temp_model = ListClustersResponseBodyClustersClusterInfoSimpleComputes()
            self.computes = temp_model.from_map(m['Computes'])
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DeployMode') is not None:
            self.deploy_mode = m.get('DeployMode')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EhpcVersion') is not None:
            self.ehpc_version = m.get('EhpcVersion')
        if m.get('HasPlugin') is not None:
            self.has_plugin = m.get('HasPlugin')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageOwnerAlias') is not None:
            self.image_owner_alias = m.get('ImageOwnerAlias')
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('IsComputeEss') is not None:
            self.is_compute_ess = m.get('IsComputeEss')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('LoginNodes') is not None:
            self.login_nodes = m.get('LoginNodes')
        if m.get('Managers') is not None:
            temp_model = ListClustersResponseBodyClustersClusterInfoSimpleManagers()
            self.managers = temp_model.from_map(m['Managers'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NodePrefix') is not None:
            self.node_prefix = m.get('NodePrefix')
        if m.get('NodeSuffix') is not None:
            self.node_suffix = m.get('NodeSuffix')
        if m.get('OsTag') is not None:
            self.os_tag = m.get('OsTag')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SchedulerType') is not None:
            self.scheduler_type = m.get('SchedulerType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TotalResources') is not None:
            temp_model = ListClustersResponseBodyClustersClusterInfoSimpleTotalResources()
            self.total_resources = temp_model.from_map(m['TotalResources'])
        if m.get('UsedResources') is not None:
            temp_model = ListClustersResponseBodyClustersClusterInfoSimpleUsedResources()
            self.used_resources = temp_model.from_map(m['UsedResources'])
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListClustersResponseBodyClusters(TeaModel):
    def __init__(
        self,
        cluster_info_simple: List[ListClustersResponseBodyClustersClusterInfoSimple] = None,
    ):
        self.cluster_info_simple = cluster_info_simple

    def validate(self):
        if self.cluster_info_simple:
            for k in self.cluster_info_simple:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ClusterInfoSimple'] = []
        if self.cluster_info_simple is not None:
            for k in self.cluster_info_simple:
                result['ClusterInfoSimple'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cluster_info_simple = []
        if m.get('ClusterInfoSimple') is not None:
            for k in m.get('ClusterInfoSimple'):
                temp_model = ListClustersResponseBodyClustersClusterInfoSimple()
                self.cluster_info_simple.append(temp_model.from_map(k))
        return self


class ListClustersResponseBody(TeaModel):
    def __init__(
        self,
        clusters: ListClustersResponseBodyClusters = None,
        page_number: int = None,
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
            self.clusters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clusters is not None:
            result['Clusters'] = self.clusters.to_map()
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
        if m.get('Clusters') is not None:
            temp_model = ListClustersResponseBodyClusters()
            self.clusters = temp_model.from_map(m['Clusters'])
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class ListClustersMetaRequest(TeaModel):
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


class ListClustersMetaResponseBodyClustersClusterInfoSimple(TeaModel):
    def __init__(
        self,
        account_type: str = None,
        client_version: str = None,
        deploy_mode: str = None,
        description: str = None,
        has_plugin: bool = None,
        id: str = None,
        is_compute_ess: bool = None,
        location: str = None,
        name: str = None,
        os_tag: str = None,
        scheduler_type: str = None,
        status: str = None,
        vpc_id: str = None,
    ):
        self.account_type = account_type
        self.client_version = client_version
        self.deploy_mode = deploy_mode
        self.description = description
        self.has_plugin = has_plugin
        self.id = id
        self.is_compute_ess = is_compute_ess
        self.location = location
        self.name = name
        self.os_tag = os_tag
        self.scheduler_type = scheduler_type
        self.status = status
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.deploy_mode is not None:
            result['DeployMode'] = self.deploy_mode
        if self.description is not None:
            result['Description'] = self.description
        if self.has_plugin is not None:
            result['HasPlugin'] = self.has_plugin
        if self.id is not None:
            result['Id'] = self.id
        if self.is_compute_ess is not None:
            result['IsComputeEss'] = self.is_compute_ess
        if self.location is not None:
            result['Location'] = self.location
        if self.name is not None:
            result['Name'] = self.name
        if self.os_tag is not None:
            result['OsTag'] = self.os_tag
        if self.scheduler_type is not None:
            result['SchedulerType'] = self.scheduler_type
        if self.status is not None:
            result['Status'] = self.status
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('DeployMode') is not None:
            self.deploy_mode = m.get('DeployMode')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('HasPlugin') is not None:
            self.has_plugin = m.get('HasPlugin')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsComputeEss') is not None:
            self.is_compute_ess = m.get('IsComputeEss')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OsTag') is not None:
            self.os_tag = m.get('OsTag')
        if m.get('SchedulerType') is not None:
            self.scheduler_type = m.get('SchedulerType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ListClustersMetaResponseBodyClusters(TeaModel):
    def __init__(
        self,
        cluster_info_simple: List[ListClustersMetaResponseBodyClustersClusterInfoSimple] = None,
    ):
        self.cluster_info_simple = cluster_info_simple

    def validate(self):
        if self.cluster_info_simple:
            for k in self.cluster_info_simple:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ClusterInfoSimple'] = []
        if self.cluster_info_simple is not None:
            for k in self.cluster_info_simple:
                result['ClusterInfoSimple'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cluster_info_simple = []
        if m.get('ClusterInfoSimple') is not None:
            for k in m.get('ClusterInfoSimple'):
                temp_model = ListClustersMetaResponseBodyClustersClusterInfoSimple()
                self.cluster_info_simple.append(temp_model.from_map(k))
        return self


class ListClustersMetaResponseBody(TeaModel):
    def __init__(
        self,
        clusters: ListClustersMetaResponseBodyClusters = None,
        page_number: int = None,
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
            self.clusters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clusters is not None:
            result['Clusters'] = self.clusters.to_map()
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
        if m.get('Clusters') is not None:
            temp_model = ListClustersMetaResponseBodyClusters()
            self.clusters = temp_model.from_map(m['Clusters'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListClustersMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListClustersMetaResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListClustersMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCommandsRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        command_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.cluster_id = cluster_id
        self.command_id = command_id
        self.page_number = page_number
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
        if self.command_id is not None:
            result['CommandId'] = self.command_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CommandId') is not None:
            self.command_id = m.get('CommandId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListCommandsResponseBodyCommandsCommand(TeaModel):
    def __init__(
        self,
        command_content: str = None,
        command_id: str = None,
        timeout: str = None,
        working_dir: str = None,
    ):
        self.command_content = command_content
        self.command_id = command_id
        self.timeout = timeout
        self.working_dir = working_dir

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command_content is not None:
            result['CommandContent'] = self.command_content
        if self.command_id is not None:
            result['CommandId'] = self.command_id
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.working_dir is not None:
            result['WorkingDir'] = self.working_dir
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandContent') is not None:
            self.command_content = m.get('CommandContent')
        if m.get('CommandId') is not None:
            self.command_id = m.get('CommandId')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')
        return self


class ListCommandsResponseBodyCommands(TeaModel):
    def __init__(
        self,
        command: List[ListCommandsResponseBodyCommandsCommand] = None,
    ):
        self.command = command

    def validate(self):
        if self.command:
            for k in self.command:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Command'] = []
        if self.command is not None:
            for k in self.command:
                result['Command'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.command = []
        if m.get('Command') is not None:
            for k in m.get('Command'):
                temp_model = ListCommandsResponseBodyCommandsCommand()
                self.command.append(temp_model.from_map(k))
        return self


class ListCommandsResponseBody(TeaModel):
    def __init__(
        self,
        commands: ListCommandsResponseBodyCommands = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.commands = commands
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.commands:
            self.commands.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commands is not None:
            result['Commands'] = self.commands.to_map()
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
        if m.get('Commands') is not None:
            temp_model = ListCommandsResponseBodyCommands()
            self.commands = temp_model.from_map(m['Commands'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListCommandsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCommandsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListCommandsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCommunityImagesRequest(TeaModel):
    def __init__(
        self,
        base_os_tag: str = None,
        cluster_id: str = None,
        instance_type: str = None,
    ):
        self.base_os_tag = base_os_tag
        self.cluster_id = cluster_id
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_os_tag is not None:
            result['BaseOsTag'] = self.base_os_tag
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseOsTag') is not None:
            self.base_os_tag = m.get('BaseOsTag')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class ListCommunityImagesResponseBodyImagesImageInfoBaseOsTag(TeaModel):
    def __init__(
        self,
        architecture: str = None,
        os_tag: str = None,
        platform: str = None,
        version: str = None,
    ):
        self.architecture = architecture
        self.os_tag = os_tag
        self.platform = platform
        self.version = version

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
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Architecture') is not None:
            self.architecture = m.get('Architecture')
        if m.get('OsTag') is not None:
            self.os_tag = m.get('OsTag')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListCommunityImagesResponseBodyImagesImageInfoOsTag(TeaModel):
    def __init__(
        self,
        architecture: str = None,
        base_os_tag: str = None,
        os_tag: str = None,
        platform: str = None,
        version: str = None,
    ):
        self.architecture = architecture
        self.base_os_tag = base_os_tag
        self.os_tag = os_tag
        self.platform = platform
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture is not None:
            result['Architecture'] = self.architecture
        if self.base_os_tag is not None:
            result['BaseOsTag'] = self.base_os_tag
        if self.os_tag is not None:
            result['OsTag'] = self.os_tag
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Architecture') is not None:
            self.architecture = m.get('Architecture')
        if m.get('BaseOsTag') is not None:
            self.base_os_tag = m.get('BaseOsTag')
        if m.get('OsTag') is not None:
            self.os_tag = m.get('OsTag')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListCommunityImagesResponseBodyImagesImageInfo(TeaModel):
    def __init__(
        self,
        base_os_tag: ListCommunityImagesResponseBodyImagesImageInfoBaseOsTag = None,
        description: str = None,
        image_id: str = None,
        image_name: str = None,
        image_owner_alias: str = None,
        os_tag: ListCommunityImagesResponseBodyImagesImageInfoOsTag = None,
        post_install_script: str = None,
        pricing_cycle: str = None,
        product_code: str = None,
        size: int = None,
        sku_code: str = None,
        status: str = None,
        uid: str = None,
    ):
        self.base_os_tag = base_os_tag
        self.description = description
        self.image_id = image_id
        self.image_name = image_name
        self.image_owner_alias = image_owner_alias
        self.os_tag = os_tag
        self.post_install_script = post_install_script
        self.pricing_cycle = pricing_cycle
        self.product_code = product_code
        self.size = size
        self.sku_code = sku_code
        self.status = status
        self.uid = uid

    def validate(self):
        if self.base_os_tag:
            self.base_os_tag.validate()
        if self.os_tag:
            self.os_tag.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_os_tag is not None:
            result['BaseOsTag'] = self.base_os_tag.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.image_owner_alias is not None:
            result['ImageOwnerAlias'] = self.image_owner_alias
        if self.os_tag is not None:
            result['OsTag'] = self.os_tag.to_map()
        if self.post_install_script is not None:
            result['PostInstallScript'] = self.post_install_script
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.size is not None:
            result['Size'] = self.size
        if self.sku_code is not None:
            result['SkuCode'] = self.sku_code
        if self.status is not None:
            result['Status'] = self.status
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseOsTag') is not None:
            temp_model = ListCommunityImagesResponseBodyImagesImageInfoBaseOsTag()
            self.base_os_tag = temp_model.from_map(m['BaseOsTag'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('ImageOwnerAlias') is not None:
            self.image_owner_alias = m.get('ImageOwnerAlias')
        if m.get('OsTag') is not None:
            temp_model = ListCommunityImagesResponseBodyImagesImageInfoOsTag()
            self.os_tag = temp_model.from_map(m['OsTag'])
        if m.get('PostInstallScript') is not None:
            self.post_install_script = m.get('PostInstallScript')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('SkuCode') is not None:
            self.sku_code = m.get('SkuCode')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class ListCommunityImagesResponseBodyImages(TeaModel):
    def __init__(
        self,
        image_info: List[ListCommunityImagesResponseBodyImagesImageInfo] = None,
    ):
        self.image_info = image_info

    def validate(self):
        if self.image_info:
            for k in self.image_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ImageInfo'] = []
        if self.image_info is not None:
            for k in self.image_info:
                result['ImageInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.image_info = []
        if m.get('ImageInfo') is not None:
            for k in m.get('ImageInfo'):
                temp_model = ListCommunityImagesResponseBodyImagesImageInfo()
                self.image_info.append(temp_model.from_map(k))
        return self


class ListCommunityImagesResponseBody(TeaModel):
    def __init__(
        self,
        images: ListCommunityImagesResponseBodyImages = None,
        request_id: str = None,
    ):
        self.images = images
        self.request_id = request_id

    def validate(self):
        if self.images:
            self.images.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.images is not None:
            result['Images'] = self.images.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Images') is not None:
            temp_model = ListCommunityImagesResponseBodyImages()
            self.images = temp_model.from_map(m['Images'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListCommunityImagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCommunityImagesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListCommunityImagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListContainerAppsRequest(TeaModel):
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


class ListContainerAppsResponseBodyContainerAppsContainerApps(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        id: str = None,
        image_tag: str = None,
        name: str = None,
        repository: str = None,
        type: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.id = id
        self.image_tag = image_tag
        self.name = name
        self.repository = repository
        self.type = type

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
        if self.id is not None:
            result['Id'] = self.id
        if self.image_tag is not None:
            result['ImageTag'] = self.image_tag
        if self.name is not None:
            result['Name'] = self.name
        if self.repository is not None:
            result['Repository'] = self.repository
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ImageTag') is not None:
            self.image_tag = m.get('ImageTag')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Repository') is not None:
            self.repository = m.get('Repository')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListContainerAppsResponseBodyContainerApps(TeaModel):
    def __init__(
        self,
        container_apps: List[ListContainerAppsResponseBodyContainerAppsContainerApps] = None,
    ):
        self.container_apps = container_apps

    def validate(self):
        if self.container_apps:
            for k in self.container_apps:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ContainerApps'] = []
        if self.container_apps is not None:
            for k in self.container_apps:
                result['ContainerApps'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.container_apps = []
        if m.get('ContainerApps') is not None:
            for k in m.get('ContainerApps'):
                temp_model = ListContainerAppsResponseBodyContainerAppsContainerApps()
                self.container_apps.append(temp_model.from_map(k))
        return self


class ListContainerAppsResponseBody(TeaModel):
    def __init__(
        self,
        container_apps: ListContainerAppsResponseBodyContainerApps = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.container_apps = container_apps
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.container_apps:
            self.container_apps.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_apps is not None:
            result['ContainerApps'] = self.container_apps.to_map()
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
        if m.get('ContainerApps') is not None:
            temp_model = ListContainerAppsResponseBodyContainerApps()
            self.container_apps = temp_model.from_map(m['ContainerApps'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListContainerAppsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListContainerAppsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListContainerAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListContainerImagesRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        container_type: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.cluster_id = cluster_id
        self.container_type = container_type
        self.page_number = page_number
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
        if self.container_type is not None:
            result['ContainerType'] = self.container_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ContainerType') is not None:
            self.container_type = m.get('ContainerType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListContainerImagesResponseBodyImagesImages(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        repository: str = None,
        status: str = None,
        system: str = None,
        tag: str = None,
        type: str = None,
        update_date_time: str = None,
    ):
        self.image_id = image_id
        self.repository = repository
        self.status = status
        self.system = system
        self.tag = tag
        self.type = type
        self.update_date_time = update_date_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.repository is not None:
            result['Repository'] = self.repository
        if self.status is not None:
            result['Status'] = self.status
        if self.system is not None:
            result['System'] = self.system
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.type is not None:
            result['Type'] = self.type
        if self.update_date_time is not None:
            result['UpdateDateTime'] = self.update_date_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('Repository') is not None:
            self.repository = m.get('Repository')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('System') is not None:
            self.system = m.get('System')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdateDateTime') is not None:
            self.update_date_time = m.get('UpdateDateTime')
        return self


class ListContainerImagesResponseBodyImages(TeaModel):
    def __init__(
        self,
        images: List[ListContainerImagesResponseBodyImagesImages] = None,
    ):
        self.images = images

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.images = []
        if m.get('Images') is not None:
            for k in m.get('Images'):
                temp_model = ListContainerImagesResponseBodyImagesImages()
                self.images.append(temp_model.from_map(k))
        return self


class ListContainerImagesResponseBody(TeaModel):
    def __init__(
        self,
        dbinfo: str = None,
        images: ListContainerImagesResponseBodyImages = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.dbinfo = dbinfo
        self.images = images
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.images:
            self.images.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinfo is not None:
            result['DBInfo'] = self.dbinfo
        if self.images is not None:
            result['Images'] = self.images.to_map()
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
        if m.get('DBInfo') is not None:
            self.dbinfo = m.get('DBInfo')
        if m.get('Images') is not None:
            temp_model = ListContainerImagesResponseBodyImages()
            self.images = temp_model.from_map(m['Images'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListContainerImagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListContainerImagesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListContainerImagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCpfsFileSystemsRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.file_system_id = file_system_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListCpfsFileSystemsResponseBodyFileSystemListFileSystemsMountTargetListMountTargets(TeaModel):
    def __init__(
        self,
        mount_target_domain: str = None,
        network_type: str = None,
        status: str = None,
        vpc_id: str = None,
        vsw_id: str = None,
    ):
        self.mount_target_domain = mount_target_domain
        self.network_type = network_type
        self.status = status
        self.vpc_id = vpc_id
        self.vsw_id = vsw_id

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
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vsw_id is not None:
            result['VswId'] = self.vsw_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MountTargetDomain') is not None:
            self.mount_target_domain = m.get('MountTargetDomain')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswId') is not None:
            self.vsw_id = m.get('VswId')
        return self


class ListCpfsFileSystemsResponseBodyFileSystemListFileSystemsMountTargetList(TeaModel):
    def __init__(
        self,
        mount_targets: List[ListCpfsFileSystemsResponseBodyFileSystemListFileSystemsMountTargetListMountTargets] = None,
    ):
        self.mount_targets = mount_targets

    def validate(self):
        if self.mount_targets:
            for k in self.mount_targets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MountTargets'] = []
        if self.mount_targets is not None:
            for k in self.mount_targets:
                result['MountTargets'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.mount_targets = []
        if m.get('MountTargets') is not None:
            for k in m.get('MountTargets'):
                temp_model = ListCpfsFileSystemsResponseBodyFileSystemListFileSystemsMountTargetListMountTargets()
                self.mount_targets.append(temp_model.from_map(k))
        return self


class ListCpfsFileSystemsResponseBodyFileSystemListFileSystems(TeaModel):
    def __init__(
        self,
        capacity: str = None,
        create_time: str = None,
        destription: str = None,
        file_system_id: str = None,
        mount_target_list: ListCpfsFileSystemsResponseBodyFileSystemListFileSystemsMountTargetList = None,
        protocol_type: str = None,
        region_id: str = None,
        zone_id: str = None,
    ):
        self.capacity = capacity
        self.create_time = create_time
        self.destription = destription
        self.file_system_id = file_system_id
        self.mount_target_list = mount_target_list
        self.protocol_type = protocol_type
        self.region_id = region_id
        self.zone_id = zone_id

    def validate(self):
        if self.mount_target_list:
            self.mount_target_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.destription is not None:
            result['Destription'] = self.destription
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.mount_target_list is not None:
            result['MountTargetList'] = self.mount_target_list.to_map()
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Destription') is not None:
            self.destription = m.get('Destription')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('MountTargetList') is not None:
            temp_model = ListCpfsFileSystemsResponseBodyFileSystemListFileSystemsMountTargetList()
            self.mount_target_list = temp_model.from_map(m['MountTargetList'])
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListCpfsFileSystemsResponseBodyFileSystemList(TeaModel):
    def __init__(
        self,
        file_systems: List[ListCpfsFileSystemsResponseBodyFileSystemListFileSystems] = None,
    ):
        self.file_systems = file_systems

    def validate(self):
        if self.file_systems:
            for k in self.file_systems:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FileSystems'] = []
        if self.file_systems is not None:
            for k in self.file_systems:
                result['FileSystems'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.file_systems = []
        if m.get('FileSystems') is not None:
            for k in m.get('FileSystems'):
                temp_model = ListCpfsFileSystemsResponseBodyFileSystemListFileSystems()
                self.file_systems.append(temp_model.from_map(k))
        return self


class ListCpfsFileSystemsResponseBody(TeaModel):
    def __init__(
        self,
        file_system_list: ListCpfsFileSystemsResponseBodyFileSystemList = None,
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
            self.file_system_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_list is not None:
            result['FileSystemList'] = self.file_system_list.to_map()
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
        if m.get('FileSystemList') is not None:
            temp_model = ListCpfsFileSystemsResponseBodyFileSystemList()
            self.file_system_list = temp_model.from_map(m['FileSystemList'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListCpfsFileSystemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCpfsFileSystemsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListCpfsFileSystemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCurrentClientVersionResponseBody(TeaModel):
    def __init__(
        self,
        client_version: str = None,
        request_id: str = None,
    ):
        self.client_version = client_version
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListCurrentClientVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCurrentClientVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListCurrentClientVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCustomImagesRequest(TeaModel):
    def __init__(
        self,
        base_os_tag: str = None,
        cluster_id: str = None,
        image_owner_alias: str = None,
        instance_type: str = None,
    ):
        self.base_os_tag = base_os_tag
        self.cluster_id = cluster_id
        self.image_owner_alias = image_owner_alias
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_os_tag is not None:
            result['BaseOsTag'] = self.base_os_tag
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.image_owner_alias is not None:
            result['ImageOwnerAlias'] = self.image_owner_alias
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseOsTag') is not None:
            self.base_os_tag = m.get('BaseOsTag')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ImageOwnerAlias') is not None:
            self.image_owner_alias = m.get('ImageOwnerAlias')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class ListCustomImagesResponseBodyImagesImageInfoBaseOsTag(TeaModel):
    def __init__(
        self,
        architecture: str = None,
        os_tag: str = None,
        platform: str = None,
        version: str = None,
    ):
        self.architecture = architecture
        self.os_tag = os_tag
        self.platform = platform
        self.version = version

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
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Architecture') is not None:
            self.architecture = m.get('Architecture')
        if m.get('OsTag') is not None:
            self.os_tag = m.get('OsTag')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListCustomImagesResponseBodyImagesImageInfoOsTag(TeaModel):
    def __init__(
        self,
        architecture: str = None,
        base_os_tag: str = None,
        os_tag: str = None,
        platform: str = None,
        version: str = None,
    ):
        self.architecture = architecture
        self.base_os_tag = base_os_tag
        self.os_tag = os_tag
        self.platform = platform
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture is not None:
            result['Architecture'] = self.architecture
        if self.base_os_tag is not None:
            result['BaseOsTag'] = self.base_os_tag
        if self.os_tag is not None:
            result['OsTag'] = self.os_tag
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Architecture') is not None:
            self.architecture = m.get('Architecture')
        if m.get('BaseOsTag') is not None:
            self.base_os_tag = m.get('BaseOsTag')
        if m.get('OsTag') is not None:
            self.os_tag = m.get('OsTag')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListCustomImagesResponseBodyImagesImageInfo(TeaModel):
    def __init__(
        self,
        base_os_tag: ListCustomImagesResponseBodyImagesImageInfoBaseOsTag = None,
        description: str = None,
        image_id: str = None,
        image_name: str = None,
        image_owner_alias: str = None,
        os_tag: ListCustomImagesResponseBodyImagesImageInfoOsTag = None,
        post_install_script: str = None,
        pricing_cycle: str = None,
        product_code: str = None,
        size: int = None,
        sku_code: str = None,
        status: str = None,
        uid: str = None,
    ):
        self.base_os_tag = base_os_tag
        self.description = description
        self.image_id = image_id
        self.image_name = image_name
        self.image_owner_alias = image_owner_alias
        self.os_tag = os_tag
        self.post_install_script = post_install_script
        self.pricing_cycle = pricing_cycle
        self.product_code = product_code
        self.size = size
        self.sku_code = sku_code
        self.status = status
        self.uid = uid

    def validate(self):
        if self.base_os_tag:
            self.base_os_tag.validate()
        if self.os_tag:
            self.os_tag.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_os_tag is not None:
            result['BaseOsTag'] = self.base_os_tag.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.image_owner_alias is not None:
            result['ImageOwnerAlias'] = self.image_owner_alias
        if self.os_tag is not None:
            result['OsTag'] = self.os_tag.to_map()
        if self.post_install_script is not None:
            result['PostInstallScript'] = self.post_install_script
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.size is not None:
            result['Size'] = self.size
        if self.sku_code is not None:
            result['SkuCode'] = self.sku_code
        if self.status is not None:
            result['Status'] = self.status
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseOsTag') is not None:
            temp_model = ListCustomImagesResponseBodyImagesImageInfoBaseOsTag()
            self.base_os_tag = temp_model.from_map(m['BaseOsTag'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('ImageOwnerAlias') is not None:
            self.image_owner_alias = m.get('ImageOwnerAlias')
        if m.get('OsTag') is not None:
            temp_model = ListCustomImagesResponseBodyImagesImageInfoOsTag()
            self.os_tag = temp_model.from_map(m['OsTag'])
        if m.get('PostInstallScript') is not None:
            self.post_install_script = m.get('PostInstallScript')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('SkuCode') is not None:
            self.sku_code = m.get('SkuCode')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class ListCustomImagesResponseBodyImages(TeaModel):
    def __init__(
        self,
        image_info: List[ListCustomImagesResponseBodyImagesImageInfo] = None,
    ):
        self.image_info = image_info

    def validate(self):
        if self.image_info:
            for k in self.image_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ImageInfo'] = []
        if self.image_info is not None:
            for k in self.image_info:
                result['ImageInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.image_info = []
        if m.get('ImageInfo') is not None:
            for k in m.get('ImageInfo'):
                temp_model = ListCustomImagesResponseBodyImagesImageInfo()
                self.image_info.append(temp_model.from_map(k))
        return self


class ListCustomImagesResponseBody(TeaModel):
    def __init__(
        self,
        images: ListCustomImagesResponseBodyImages = None,
        request_id: str = None,
    ):
        self.images = images
        self.request_id = request_id

    def validate(self):
        if self.images:
            self.images.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.images is not None:
            result['Images'] = self.images.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Images') is not None:
            temp_model = ListCustomImagesResponseBodyImages()
            self.images = temp_model.from_map(m['Images'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListCustomImagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCustomImagesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListCustomImagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFileSystemWithMountTargetsRequest(TeaModel):
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


class ListFileSystemWithMountTargetsResponseBodyFileSystemListFileSystemsMountTargetListMountTargets(TeaModel):
    def __init__(
        self,
        access_group: str = None,
        mount_target_domain: str = None,
        network_type: str = None,
        status: str = None,
        vpc_id: str = None,
        vsw_id: str = None,
    ):
        self.access_group = access_group
        self.mount_target_domain = mount_target_domain
        self.network_type = network_type
        self.status = status
        self.vpc_id = vpc_id
        self.vsw_id = vsw_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group is not None:
            result['AccessGroup'] = self.access_group
        if self.mount_target_domain is not None:
            result['MountTargetDomain'] = self.mount_target_domain
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.status is not None:
            result['Status'] = self.status
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vsw_id is not None:
            result['VswId'] = self.vsw_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroup') is not None:
            self.access_group = m.get('AccessGroup')
        if m.get('MountTargetDomain') is not None:
            self.mount_target_domain = m.get('MountTargetDomain')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswId') is not None:
            self.vsw_id = m.get('VswId')
        return self


class ListFileSystemWithMountTargetsResponseBodyFileSystemListFileSystemsMountTargetList(TeaModel):
    def __init__(
        self,
        mount_targets: List[ListFileSystemWithMountTargetsResponseBodyFileSystemListFileSystemsMountTargetListMountTargets] = None,
    ):
        self.mount_targets = mount_targets

    def validate(self):
        if self.mount_targets:
            for k in self.mount_targets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MountTargets'] = []
        if self.mount_targets is not None:
            for k in self.mount_targets:
                result['MountTargets'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.mount_targets = []
        if m.get('MountTargets') is not None:
            for k in m.get('MountTargets'):
                temp_model = ListFileSystemWithMountTargetsResponseBodyFileSystemListFileSystemsMountTargetListMountTargets()
                self.mount_targets.append(temp_model.from_map(k))
        return self


class ListFileSystemWithMountTargetsResponseBodyFileSystemListFileSystemsPackageListPackages(TeaModel):
    def __init__(
        self,
        package_id: str = None,
    ):
        self.package_id = package_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.package_id is not None:
            result['PackageId'] = self.package_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PackageId') is not None:
            self.package_id = m.get('PackageId')
        return self


class ListFileSystemWithMountTargetsResponseBodyFileSystemListFileSystemsPackageList(TeaModel):
    def __init__(
        self,
        packages: List[ListFileSystemWithMountTargetsResponseBodyFileSystemListFileSystemsPackageListPackages] = None,
    ):
        self.packages = packages

    def validate(self):
        if self.packages:
            for k in self.packages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Packages'] = []
        if self.packages is not None:
            for k in self.packages:
                result['Packages'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.packages = []
        if m.get('Packages') is not None:
            for k in m.get('Packages'):
                temp_model = ListFileSystemWithMountTargetsResponseBodyFileSystemListFileSystemsPackageListPackages()
                self.packages.append(temp_model.from_map(k))
        return self


class ListFileSystemWithMountTargetsResponseBodyFileSystemListFileSystems(TeaModel):
    def __init__(
        self,
        band_width: int = None,
        capacity: int = None,
        create_time: str = None,
        destription: str = None,
        encrypt_type: int = None,
        file_system_id: str = None,
        file_system_type: str = None,
        metered_size: int = None,
        mount_target_list: ListFileSystemWithMountTargetsResponseBodyFileSystemListFileSystemsMountTargetList = None,
        package_list: ListFileSystemWithMountTargetsResponseBodyFileSystemListFileSystemsPackageList = None,
        protocol_type: str = None,
        region_id: str = None,
        status: str = None,
        storage_type: str = None,
        vpc_id: str = None,
    ):
        self.band_width = band_width
        self.capacity = capacity
        self.create_time = create_time
        self.destription = destription
        self.encrypt_type = encrypt_type
        self.file_system_id = file_system_id
        self.file_system_type = file_system_type
        self.metered_size = metered_size
        self.mount_target_list = mount_target_list
        self.package_list = package_list
        self.protocol_type = protocol_type
        self.region_id = region_id
        self.status = status
        self.storage_type = storage_type
        self.vpc_id = vpc_id

    def validate(self):
        if self.mount_target_list:
            self.mount_target_list.validate()
        if self.package_list:
            self.package_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.band_width is not None:
            result['BandWidth'] = self.band_width
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.destription is not None:
            result['Destription'] = self.destription
        if self.encrypt_type is not None:
            result['EncryptType'] = self.encrypt_type
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        if self.metered_size is not None:
            result['MeteredSize'] = self.metered_size
        if self.mount_target_list is not None:
            result['MountTargetList'] = self.mount_target_list.to_map()
        if self.package_list is not None:
            result['PackageList'] = self.package_list.to_map()
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandWidth') is not None:
            self.band_width = m.get('BandWidth')
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Destription') is not None:
            self.destription = m.get('Destription')
        if m.get('EncryptType') is not None:
            self.encrypt_type = m.get('EncryptType')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        if m.get('MeteredSize') is not None:
            self.metered_size = m.get('MeteredSize')
        if m.get('MountTargetList') is not None:
            temp_model = ListFileSystemWithMountTargetsResponseBodyFileSystemListFileSystemsMountTargetList()
            self.mount_target_list = temp_model.from_map(m['MountTargetList'])
        if m.get('PackageList') is not None:
            temp_model = ListFileSystemWithMountTargetsResponseBodyFileSystemListFileSystemsPackageList()
            self.package_list = temp_model.from_map(m['PackageList'])
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ListFileSystemWithMountTargetsResponseBodyFileSystemList(TeaModel):
    def __init__(
        self,
        file_systems: List[ListFileSystemWithMountTargetsResponseBodyFileSystemListFileSystems] = None,
    ):
        self.file_systems = file_systems

    def validate(self):
        if self.file_systems:
            for k in self.file_systems:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FileSystems'] = []
        if self.file_systems is not None:
            for k in self.file_systems:
                result['FileSystems'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.file_systems = []
        if m.get('FileSystems') is not None:
            for k in m.get('FileSystems'):
                temp_model = ListFileSystemWithMountTargetsResponseBodyFileSystemListFileSystems()
                self.file_systems.append(temp_model.from_map(k))
        return self


class ListFileSystemWithMountTargetsResponseBody(TeaModel):
    def __init__(
        self,
        file_system_list: ListFileSystemWithMountTargetsResponseBodyFileSystemList = None,
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
            self.file_system_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_list is not None:
            result['FileSystemList'] = self.file_system_list.to_map()
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
        if m.get('FileSystemList') is not None:
            temp_model = ListFileSystemWithMountTargetsResponseBodyFileSystemList()
            self.file_system_list = temp_model.from_map(m['FileSystemList'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListFileSystemWithMountTargetsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFileSystemWithMountTargetsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListFileSystemWithMountTargetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListImagesRequest(TeaModel):
    def __init__(
        self,
        base_os_tag: str = None,
        instance_type: str = None,
    ):
        self.base_os_tag = base_os_tag
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_os_tag is not None:
            result['BaseOsTag'] = self.base_os_tag
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseOsTag') is not None:
            self.base_os_tag = m.get('BaseOsTag')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class ListImagesResponseBodyOsTagsOsInfo(TeaModel):
    def __init__(
        self,
        architecture: str = None,
        base_os_tag: str = None,
        image_id: str = None,
        os_tag: str = None,
        platform: str = None,
        version: str = None,
    ):
        self.architecture = architecture
        self.base_os_tag = base_os_tag
        self.image_id = image_id
        self.os_tag = os_tag
        self.platform = platform
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture is not None:
            result['Architecture'] = self.architecture
        if self.base_os_tag is not None:
            result['BaseOsTag'] = self.base_os_tag
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.os_tag is not None:
            result['OsTag'] = self.os_tag
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Architecture') is not None:
            self.architecture = m.get('Architecture')
        if m.get('BaseOsTag') is not None:
            self.base_os_tag = m.get('BaseOsTag')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('OsTag') is not None:
            self.os_tag = m.get('OsTag')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListImagesResponseBodyOsTags(TeaModel):
    def __init__(
        self,
        os_info: List[ListImagesResponseBodyOsTagsOsInfo] = None,
    ):
        self.os_info = os_info

    def validate(self):
        if self.os_info:
            for k in self.os_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OsInfo'] = []
        if self.os_info is not None:
            for k in self.os_info:
                result['OsInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.os_info = []
        if m.get('OsInfo') is not None:
            for k in m.get('OsInfo'):
                temp_model = ListImagesResponseBodyOsTagsOsInfo()
                self.os_info.append(temp_model.from_map(k))
        return self


class ListImagesResponseBody(TeaModel):
    def __init__(
        self,
        os_tags: ListImagesResponseBodyOsTags = None,
        request_id: str = None,
    ):
        self.os_tags = os_tags
        self.request_id = request_id

    def validate(self):
        if self.os_tags:
            self.os_tags.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.os_tags is not None:
            result['OsTags'] = self.os_tags.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OsTags') is not None:
            temp_model = ListImagesResponseBodyOsTags()
            self.os_tags = temp_model.from_map(m['OsTags'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class ListInstalledSoftwareRequest(TeaModel):
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


class ListInstalledSoftwareResponseBodySoftwareListSoftwareList(TeaModel):
    def __init__(
        self,
        software_id: str = None,
        software_name: str = None,
        software_status: str = None,
        software_version: str = None,
    ):
        self.software_id = software_id
        self.software_name = software_name
        self.software_status = software_status
        self.software_version = software_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.software_id is not None:
            result['SoftwareId'] = self.software_id
        if self.software_name is not None:
            result['SoftwareName'] = self.software_name
        if self.software_status is not None:
            result['SoftwareStatus'] = self.software_status
        if self.software_version is not None:
            result['SoftwareVersion'] = self.software_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SoftwareId') is not None:
            self.software_id = m.get('SoftwareId')
        if m.get('SoftwareName') is not None:
            self.software_name = m.get('SoftwareName')
        if m.get('SoftwareStatus') is not None:
            self.software_status = m.get('SoftwareStatus')
        if m.get('SoftwareVersion') is not None:
            self.software_version = m.get('SoftwareVersion')
        return self


class ListInstalledSoftwareResponseBodySoftwareList(TeaModel):
    def __init__(
        self,
        software_list: List[ListInstalledSoftwareResponseBodySoftwareListSoftwareList] = None,
    ):
        self.software_list = software_list

    def validate(self):
        if self.software_list:
            for k in self.software_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SoftwareList'] = []
        if self.software_list is not None:
            for k in self.software_list:
                result['SoftwareList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.software_list = []
        if m.get('SoftwareList') is not None:
            for k in m.get('SoftwareList'):
                temp_model = ListInstalledSoftwareResponseBodySoftwareListSoftwareList()
                self.software_list.append(temp_model.from_map(k))
        return self


class ListInstalledSoftwareResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        software_list: ListInstalledSoftwareResponseBodySoftwareList = None,
    ):
        self.request_id = request_id
        self.software_list = software_list

    def validate(self):
        if self.software_list:
            self.software_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.software_list is not None:
            result['SoftwareList'] = self.software_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SoftwareList') is not None:
            temp_model = ListInstalledSoftwareResponseBodySoftwareList()
            self.software_list = temp_model.from_map(m['SoftwareList'])
        return self


class ListInstalledSoftwareResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInstalledSoftwareResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListInstalledSoftwareResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInvocationResultsRequestInstance(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListInvocationResultsRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        command_id: str = None,
        instance: List[ListInvocationResultsRequestInstance] = None,
        invoke_record_status: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.cluster_id = cluster_id
        self.command_id = command_id
        self.instance = instance
        self.invoke_record_status = invoke_record_status
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        if self.instance:
            for k in self.instance:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.command_id is not None:
            result['CommandId'] = self.command_id
        result['Instance'] = []
        if self.instance is not None:
            for k in self.instance:
                result['Instance'].append(k.to_map() if k else None)
        if self.invoke_record_status is not None:
            result['InvokeRecordStatus'] = self.invoke_record_status
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CommandId') is not None:
            self.command_id = m.get('CommandId')
        self.instance = []
        if m.get('Instance') is not None:
            for k in m.get('Instance'):
                temp_model = ListInvocationResultsRequestInstance()
                self.instance.append(temp_model.from_map(k))
        if m.get('InvokeRecordStatus') is not None:
            self.invoke_record_status = m.get('InvokeRecordStatus')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListInvocationResultsResponseBodyInvocationResultsInvocationResult(TeaModel):
    def __init__(
        self,
        command_id: str = None,
        exit_code: int = None,
        finished_time: str = None,
        instance_id: str = None,
        invoke_record_status: str = None,
        message: str = None,
        success: bool = None,
    ):
        self.command_id = command_id
        self.exit_code = exit_code
        self.finished_time = finished_time
        self.instance_id = instance_id
        self.invoke_record_status = invoke_record_status
        self.message = message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command_id is not None:
            result['CommandId'] = self.command_id
        if self.exit_code is not None:
            result['ExitCode'] = self.exit_code
        if self.finished_time is not None:
            result['FinishedTime'] = self.finished_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.invoke_record_status is not None:
            result['InvokeRecordStatus'] = self.invoke_record_status
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandId') is not None:
            self.command_id = m.get('CommandId')
        if m.get('ExitCode') is not None:
            self.exit_code = m.get('ExitCode')
        if m.get('FinishedTime') is not None:
            self.finished_time = m.get('FinishedTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InvokeRecordStatus') is not None:
            self.invoke_record_status = m.get('InvokeRecordStatus')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListInvocationResultsResponseBodyInvocationResults(TeaModel):
    def __init__(
        self,
        invocation_result: List[ListInvocationResultsResponseBodyInvocationResultsInvocationResult] = None,
    ):
        self.invocation_result = invocation_result

    def validate(self):
        if self.invocation_result:
            for k in self.invocation_result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InvocationResult'] = []
        if self.invocation_result is not None:
            for k in self.invocation_result:
                result['InvocationResult'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.invocation_result = []
        if m.get('InvocationResult') is not None:
            for k in m.get('InvocationResult'):
                temp_model = ListInvocationResultsResponseBodyInvocationResultsInvocationResult()
                self.invocation_result.append(temp_model.from_map(k))
        return self


class ListInvocationResultsResponseBody(TeaModel):
    def __init__(
        self,
        invocation_results: ListInvocationResultsResponseBodyInvocationResults = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.invocation_results = invocation_results
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.invocation_results:
            self.invocation_results.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.invocation_results is not None:
            result['InvocationResults'] = self.invocation_results.to_map()
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
        if m.get('InvocationResults') is not None:
            temp_model = ListInvocationResultsResponseBodyInvocationResults()
            self.invocation_results = temp_model.from_map(m['InvocationResults'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListInvocationResultsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInvocationResultsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListInvocationResultsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInvocationStatusRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        command_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.command_id = command_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.command_id is not None:
            result['CommandId'] = self.command_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CommandId') is not None:
            self.command_id = m.get('CommandId')
        return self


class ListInvocationStatusResponseBodyInvokeInstancesInvokeInstance(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_invoke_status: str = None,
    ):
        self.instance_id = instance_id
        self.instance_invoke_status = instance_invoke_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_invoke_status is not None:
            result['InstanceInvokeStatus'] = self.instance_invoke_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceInvokeStatus') is not None:
            self.instance_invoke_status = m.get('InstanceInvokeStatus')
        return self


class ListInvocationStatusResponseBodyInvokeInstances(TeaModel):
    def __init__(
        self,
        invoke_instance: List[ListInvocationStatusResponseBodyInvokeInstancesInvokeInstance] = None,
    ):
        self.invoke_instance = invoke_instance

    def validate(self):
        if self.invoke_instance:
            for k in self.invoke_instance:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InvokeInstance'] = []
        if self.invoke_instance is not None:
            for k in self.invoke_instance:
                result['InvokeInstance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.invoke_instance = []
        if m.get('InvokeInstance') is not None:
            for k in m.get('InvokeInstance'):
                temp_model = ListInvocationStatusResponseBodyInvokeInstancesInvokeInstance()
                self.invoke_instance.append(temp_model.from_map(k))
        return self


class ListInvocationStatusResponseBody(TeaModel):
    def __init__(
        self,
        command_id: str = None,
        invoke_instances: ListInvocationStatusResponseBodyInvokeInstances = None,
        invoke_status: str = None,
        request_id: str = None,
    ):
        self.command_id = command_id
        self.invoke_instances = invoke_instances
        self.invoke_status = invoke_status
        self.request_id = request_id

    def validate(self):
        if self.invoke_instances:
            self.invoke_instances.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command_id is not None:
            result['CommandId'] = self.command_id
        if self.invoke_instances is not None:
            result['InvokeInstances'] = self.invoke_instances.to_map()
        if self.invoke_status is not None:
            result['InvokeStatus'] = self.invoke_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandId') is not None:
            self.command_id = m.get('CommandId')
        if m.get('InvokeInstances') is not None:
            temp_model = ListInvocationStatusResponseBodyInvokeInstances()
            self.invoke_instances = temp_model.from_map(m['InvokeInstances'])
        if m.get('InvokeStatus') is not None:
            self.invoke_status = m.get('InvokeStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListInvocationStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInvocationStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListInvocationStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListJobTemplatesRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.name = name
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListJobTemplatesResponseBodyTemplatesJobTemplates(TeaModel):
    def __init__(
        self,
        array_request: str = None,
        clock_time: str = None,
        command_line: str = None,
        gpu: int = None,
        id: str = None,
        input_file_url: str = None,
        mem: str = None,
        name: str = None,
        node: int = None,
        package_path: str = None,
        priority: int = None,
        queue: str = None,
        re_runable: bool = None,
        runas_user: str = None,
        stderr_redirect_path: str = None,
        stdout_redirect_path: str = None,
        task: int = None,
        thread: int = None,
        unzip_cmd: str = None,
        variables: str = None,
        with_unzip_cmd: bool = None,
    ):
        self.array_request = array_request
        self.clock_time = clock_time
        self.command_line = command_line
        self.gpu = gpu
        self.id = id
        self.input_file_url = input_file_url
        self.mem = mem
        self.name = name
        self.node = node
        self.package_path = package_path
        self.priority = priority
        self.queue = queue
        self.re_runable = re_runable
        self.runas_user = runas_user
        self.stderr_redirect_path = stderr_redirect_path
        self.stdout_redirect_path = stdout_redirect_path
        self.task = task
        self.thread = thread
        self.unzip_cmd = unzip_cmd
        self.variables = variables
        self.with_unzip_cmd = with_unzip_cmd

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.array_request is not None:
            result['ArrayRequest'] = self.array_request
        if self.clock_time is not None:
            result['ClockTime'] = self.clock_time
        if self.command_line is not None:
            result['CommandLine'] = self.command_line
        if self.gpu is not None:
            result['Gpu'] = self.gpu
        if self.id is not None:
            result['Id'] = self.id
        if self.input_file_url is not None:
            result['InputFileUrl'] = self.input_file_url
        if self.mem is not None:
            result['Mem'] = self.mem
        if self.name is not None:
            result['Name'] = self.name
        if self.node is not None:
            result['Node'] = self.node
        if self.package_path is not None:
            result['PackagePath'] = self.package_path
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.queue is not None:
            result['Queue'] = self.queue
        if self.re_runable is not None:
            result['ReRunable'] = self.re_runable
        if self.runas_user is not None:
            result['RunasUser'] = self.runas_user
        if self.stderr_redirect_path is not None:
            result['StderrRedirectPath'] = self.stderr_redirect_path
        if self.stdout_redirect_path is not None:
            result['StdoutRedirectPath'] = self.stdout_redirect_path
        if self.task is not None:
            result['Task'] = self.task
        if self.thread is not None:
            result['Thread'] = self.thread
        if self.unzip_cmd is not None:
            result['UnzipCmd'] = self.unzip_cmd
        if self.variables is not None:
            result['Variables'] = self.variables
        if self.with_unzip_cmd is not None:
            result['WithUnzipCmd'] = self.with_unzip_cmd
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArrayRequest') is not None:
            self.array_request = m.get('ArrayRequest')
        if m.get('ClockTime') is not None:
            self.clock_time = m.get('ClockTime')
        if m.get('CommandLine') is not None:
            self.command_line = m.get('CommandLine')
        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InputFileUrl') is not None:
            self.input_file_url = m.get('InputFileUrl')
        if m.get('Mem') is not None:
            self.mem = m.get('Mem')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Node') is not None:
            self.node = m.get('Node')
        if m.get('PackagePath') is not None:
            self.package_path = m.get('PackagePath')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Queue') is not None:
            self.queue = m.get('Queue')
        if m.get('ReRunable') is not None:
            self.re_runable = m.get('ReRunable')
        if m.get('RunasUser') is not None:
            self.runas_user = m.get('RunasUser')
        if m.get('StderrRedirectPath') is not None:
            self.stderr_redirect_path = m.get('StderrRedirectPath')
        if m.get('StdoutRedirectPath') is not None:
            self.stdout_redirect_path = m.get('StdoutRedirectPath')
        if m.get('Task') is not None:
            self.task = m.get('Task')
        if m.get('Thread') is not None:
            self.thread = m.get('Thread')
        if m.get('UnzipCmd') is not None:
            self.unzip_cmd = m.get('UnzipCmd')
        if m.get('Variables') is not None:
            self.variables = m.get('Variables')
        if m.get('WithUnzipCmd') is not None:
            self.with_unzip_cmd = m.get('WithUnzipCmd')
        return self


class ListJobTemplatesResponseBodyTemplates(TeaModel):
    def __init__(
        self,
        job_templates: List[ListJobTemplatesResponseBodyTemplatesJobTemplates] = None,
    ):
        self.job_templates = job_templates

    def validate(self):
        if self.job_templates:
            for k in self.job_templates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['JobTemplates'] = []
        if self.job_templates is not None:
            for k in self.job_templates:
                result['JobTemplates'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.job_templates = []
        if m.get('JobTemplates') is not None:
            for k in m.get('JobTemplates'):
                temp_model = ListJobTemplatesResponseBodyTemplatesJobTemplates()
                self.job_templates.append(temp_model.from_map(k))
        return self


class ListJobTemplatesResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        templates: ListJobTemplatesResponseBodyTemplates = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.templates = templates
        self.total_count = total_count

    def validate(self):
        if self.templates:
            self.templates.validate()

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
        if self.templates is not None:
            result['Templates'] = self.templates.to_map()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Templates') is not None:
            temp_model = ListJobTemplatesResponseBodyTemplates()
            self.templates = temp_model.from_map(m['Templates'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListJobTemplatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListJobTemplatesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListJobTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListJobsRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        owner: str = None,
        page_number: int = None,
        page_size: int = None,
        rerunable: str = None,
        state: str = None,
    ):
        self.cluster_id = cluster_id
        self.owner = owner
        self.page_number = page_number
        self.page_size = page_size
        self.rerunable = rerunable
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.rerunable is not None:
            result['Rerunable'] = self.rerunable
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Rerunable') is not None:
            self.rerunable = m.get('Rerunable')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class ListJobsResponseBodyJobsJobInfoResources(TeaModel):
    def __init__(
        self,
        cores: int = None,
        nodes: int = None,
    ):
        self.cores = cores
        self.nodes = nodes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cores is not None:
            result['Cores'] = self.cores
        if self.nodes is not None:
            result['Nodes'] = self.nodes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cores') is not None:
            self.cores = m.get('Cores')
        if m.get('Nodes') is not None:
            self.nodes = m.get('Nodes')
        return self


class ListJobsResponseBodyJobsJobInfo(TeaModel):
    def __init__(
        self,
        array_request: str = None,
        comment: str = None,
        id: str = None,
        last_modify_time: str = None,
        name: str = None,
        node_list: str = None,
        owner: str = None,
        priority: str = None,
        resources: ListJobsResponseBodyJobsJobInfoResources = None,
        shell_path: str = None,
        start_time: str = None,
        state: str = None,
        stderr: str = None,
        stdout: str = None,
        submit_time: str = None,
    ):
        self.array_request = array_request
        self.comment = comment
        self.id = id
        self.last_modify_time = last_modify_time
        self.name = name
        self.node_list = node_list
        self.owner = owner
        self.priority = priority
        self.resources = resources
        self.shell_path = shell_path
        self.start_time = start_time
        self.state = state
        self.stderr = stderr
        self.stdout = stdout
        self.submit_time = submit_time

    def validate(self):
        if self.resources:
            self.resources.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.array_request is not None:
            result['ArrayRequest'] = self.array_request
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.id is not None:
            result['Id'] = self.id
        if self.last_modify_time is not None:
            result['LastModifyTime'] = self.last_modify_time
        if self.name is not None:
            result['Name'] = self.name
        if self.node_list is not None:
            result['NodeList'] = self.node_list
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.resources is not None:
            result['Resources'] = self.resources.to_map()
        if self.shell_path is not None:
            result['ShellPath'] = self.shell_path
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.state is not None:
            result['State'] = self.state
        if self.stderr is not None:
            result['Stderr'] = self.stderr
        if self.stdout is not None:
            result['Stdout'] = self.stdout
        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArrayRequest') is not None:
            self.array_request = m.get('ArrayRequest')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LastModifyTime') is not None:
            self.last_modify_time = m.get('LastModifyTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NodeList') is not None:
            self.node_list = m.get('NodeList')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Resources') is not None:
            temp_model = ListJobsResponseBodyJobsJobInfoResources()
            self.resources = temp_model.from_map(m['Resources'])
        if m.get('ShellPath') is not None:
            self.shell_path = m.get('ShellPath')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Stderr') is not None:
            self.stderr = m.get('Stderr')
        if m.get('Stdout') is not None:
            self.stdout = m.get('Stdout')
        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')
        return self


class ListJobsResponseBodyJobs(TeaModel):
    def __init__(
        self,
        job_info: List[ListJobsResponseBodyJobsJobInfo] = None,
    ):
        self.job_info = job_info

    def validate(self):
        if self.job_info:
            for k in self.job_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['JobInfo'] = []
        if self.job_info is not None:
            for k in self.job_info:
                result['JobInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.job_info = []
        if m.get('JobInfo') is not None:
            for k in m.get('JobInfo'):
                temp_model = ListJobsResponseBodyJobsJobInfo()
                self.job_info.append(temp_model.from_map(k))
        return self


class ListJobsResponseBody(TeaModel):
    def __init__(
        self,
        jobs: ListJobsResponseBodyJobs = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.jobs = jobs
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.jobs:
            self.jobs.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.jobs is not None:
            result['Jobs'] = self.jobs.to_map()
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
        if m.get('Jobs') is not None:
            temp_model = ListJobsResponseBodyJobs()
            self.jobs = temp_model.from_map(m['Jobs'])
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class ListJobsWithFiltersRequest(TeaModel):
    def __init__(
        self,
        async_: bool = None,
        cluster_id: str = None,
        create_time_end: str = None,
        create_time_start: str = None,
        execute_order: str = None,
        job_name: str = None,
        job_status: str = None,
        nodes: List[str] = None,
        page_number: int = None,
        page_size: int = None,
        pend_order: str = None,
        queues: List[str] = None,
        region_id: str = None,
        submit_order: str = None,
        users: List[str] = None,
    ):
        self.async_ = async_
        self.cluster_id = cluster_id
        self.create_time_end = create_time_end
        self.create_time_start = create_time_start
        self.execute_order = execute_order
        self.job_name = job_name
        self.job_status = job_status
        self.nodes = nodes
        self.page_number = page_number
        self.page_size = page_size
        self.pend_order = pend_order
        self.queues = queues
        self.region_id = region_id
        self.submit_order = submit_order
        self.users = users

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.async_ is not None:
            result['Async'] = self.async_
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.create_time_end is not None:
            result['CreateTimeEnd'] = self.create_time_end
        if self.create_time_start is not None:
            result['CreateTimeStart'] = self.create_time_start
        if self.execute_order is not None:
            result['ExecuteOrder'] = self.execute_order
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.job_status is not None:
            result['JobStatus'] = self.job_status
        if self.nodes is not None:
            result['Nodes'] = self.nodes
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pend_order is not None:
            result['PendOrder'] = self.pend_order
        if self.queues is not None:
            result['Queues'] = self.queues
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.submit_order is not None:
            result['SubmitOrder'] = self.submit_order
        if self.users is not None:
            result['Users'] = self.users
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Async') is not None:
            self.async_ = m.get('Async')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CreateTimeEnd') is not None:
            self.create_time_end = m.get('CreateTimeEnd')
        if m.get('CreateTimeStart') is not None:
            self.create_time_start = m.get('CreateTimeStart')
        if m.get('ExecuteOrder') is not None:
            self.execute_order = m.get('ExecuteOrder')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('JobStatus') is not None:
            self.job_status = m.get('JobStatus')
        if m.get('Nodes') is not None:
            self.nodes = m.get('Nodes')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PendOrder') is not None:
            self.pend_order = m.get('PendOrder')
        if m.get('Queues') is not None:
            self.queues = m.get('Queues')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SubmitOrder') is not None:
            self.submit_order = m.get('SubmitOrder')
        if m.get('Users') is not None:
            self.users = m.get('Users')
        return self


class ListJobsWithFiltersResponseBodyJobsResources(TeaModel):
    def __init__(
        self,
        cores: int = None,
        nodes: int = None,
    ):
        self.cores = cores
        self.nodes = nodes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cores is not None:
            result['Cores'] = self.cores
        if self.nodes is not None:
            result['Nodes'] = self.nodes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cores') is not None:
            self.cores = m.get('Cores')
        if m.get('Nodes') is not None:
            self.nodes = m.get('Nodes')
        return self


class ListJobsWithFiltersResponseBodyJobs(TeaModel):
    def __init__(
        self,
        array_request: str = None,
        comment: str = None,
        id: str = None,
        last_modify_time: str = None,
        name: str = None,
        node_list: str = None,
        owner: str = None,
        priority: str = None,
        queue: str = None,
        rerunable: bool = None,
        resources: ListJobsWithFiltersResponseBodyJobsResources = None,
        shell_path: str = None,
        start_time: str = None,
        state: str = None,
        stderr: str = None,
        stdout: str = None,
        submit_time: str = None,
        variable_list: str = None,
    ):
        self.array_request = array_request
        self.comment = comment
        self.id = id
        self.last_modify_time = last_modify_time
        self.name = name
        self.node_list = node_list
        self.owner = owner
        self.priority = priority
        self.queue = queue
        self.rerunable = rerunable
        self.resources = resources
        self.shell_path = shell_path
        self.start_time = start_time
        self.state = state
        self.stderr = stderr
        self.stdout = stdout
        self.submit_time = submit_time
        self.variable_list = variable_list

    def validate(self):
        if self.resources:
            self.resources.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.array_request is not None:
            result['ArrayRequest'] = self.array_request
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.id is not None:
            result['Id'] = self.id
        if self.last_modify_time is not None:
            result['LastModifyTime'] = self.last_modify_time
        if self.name is not None:
            result['Name'] = self.name
        if self.node_list is not None:
            result['NodeList'] = self.node_list
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.queue is not None:
            result['Queue'] = self.queue
        if self.rerunable is not None:
            result['Rerunable'] = self.rerunable
        if self.resources is not None:
            result['Resources'] = self.resources.to_map()
        if self.shell_path is not None:
            result['ShellPath'] = self.shell_path
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.state is not None:
            result['State'] = self.state
        if self.stderr is not None:
            result['Stderr'] = self.stderr
        if self.stdout is not None:
            result['Stdout'] = self.stdout
        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time
        if self.variable_list is not None:
            result['VariableList'] = self.variable_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArrayRequest') is not None:
            self.array_request = m.get('ArrayRequest')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LastModifyTime') is not None:
            self.last_modify_time = m.get('LastModifyTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NodeList') is not None:
            self.node_list = m.get('NodeList')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Queue') is not None:
            self.queue = m.get('Queue')
        if m.get('Rerunable') is not None:
            self.rerunable = m.get('Rerunable')
        if m.get('Resources') is not None:
            temp_model = ListJobsWithFiltersResponseBodyJobsResources()
            self.resources = temp_model.from_map(m['Resources'])
        if m.get('ShellPath') is not None:
            self.shell_path = m.get('ShellPath')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Stderr') is not None:
            self.stderr = m.get('Stderr')
        if m.get('Stdout') is not None:
            self.stdout = m.get('Stdout')
        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')
        if m.get('VariableList') is not None:
            self.variable_list = m.get('VariableList')
        return self


class ListJobsWithFiltersResponseBody(TeaModel):
    def __init__(
        self,
        jobs: List[ListJobsWithFiltersResponseBodyJobs] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.jobs = jobs
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.jobs:
            for k in self.jobs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Jobs'] = []
        if self.jobs is not None:
            for k in self.jobs:
                result['Jobs'].append(k.to_map() if k else None)
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
        self.jobs = []
        if m.get('Jobs') is not None:
            for k in m.get('Jobs'):
                temp_model = ListJobsWithFiltersResponseBodyJobs()
                self.jobs.append(temp_model.from_map(k))
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


class ListJobsWithFiltersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListJobsWithFiltersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListJobsWithFiltersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNodesRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        filter: str = None,
        host_name: str = None,
        host_name_prefix: str = None,
        host_name_suffix: str = None,
        page_number: int = None,
        page_size: int = None,
        private_ip_address: str = None,
        role: str = None,
        sequence: str = None,
        sort_by: str = None,
    ):
        self.cluster_id = cluster_id
        self.filter = filter
        self.host_name = host_name
        self.host_name_prefix = host_name_prefix
        self.host_name_suffix = host_name_suffix
        self.page_number = page_number
        self.page_size = page_size
        self.private_ip_address = private_ip_address
        self.role = role
        self.sequence = sequence
        self.sort_by = sort_by

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.host_name_prefix is not None:
            result['HostNamePrefix'] = self.host_name_prefix
        if self.host_name_suffix is not None:
            result['HostNameSuffix'] = self.host_name_suffix
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        if self.role is not None:
            result['Role'] = self.role
        if self.sequence is not None:
            result['Sequence'] = self.sequence
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('HostNamePrefix') is not None:
            self.host_name_prefix = m.get('HostNamePrefix')
        if m.get('HostNameSuffix') is not None:
            self.host_name_suffix = m.get('HostNameSuffix')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Sequence') is not None:
            self.sequence = m.get('Sequence')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        return self


class ListNodesResponseBodyNodesNodeInfoRoles(TeaModel):
    def __init__(
        self,
        role: List[str] = None,
    ):
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role is not None:
            result['Role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Role') is not None:
            self.role = m.get('Role')
        return self


class ListNodesResponseBodyNodesNodeInfoTotalResources(TeaModel):
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


class ListNodesResponseBodyNodesNodeInfoUsedResources(TeaModel):
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


class ListNodesResponseBodyNodesNodeInfo(TeaModel):
    def __init__(
        self,
        add_time: str = None,
        create_mode: str = None,
        created_by_ehpc: bool = None,
        expired: bool = None,
        expired_time: str = None,
        host_name: str = None,
        ht_enabled: bool = None,
        id: str = None,
        image_id: str = None,
        image_owner_alias: str = None,
        instance_type: str = None,
        ip_address: str = None,
        location: str = None,
        lock_reason: str = None,
        public_ip_address: str = None,
        region_id: str = None,
        roles: ListNodesResponseBodyNodesNodeInfoRoles = None,
        spot_strategy: str = None,
        state_in_sched: str = None,
        status: str = None,
        total_resources: ListNodesResponseBodyNodesNodeInfoTotalResources = None,
        used_resources: ListNodesResponseBodyNodesNodeInfoUsedResources = None,
        v_switch_id: str = None,
        version: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        self.add_time = add_time
        self.create_mode = create_mode
        self.created_by_ehpc = created_by_ehpc
        self.expired = expired
        self.expired_time = expired_time
        self.host_name = host_name
        self.ht_enabled = ht_enabled
        self.id = id
        self.image_id = image_id
        self.image_owner_alias = image_owner_alias
        self.instance_type = instance_type
        self.ip_address = ip_address
        self.location = location
        self.lock_reason = lock_reason
        self.public_ip_address = public_ip_address
        self.region_id = region_id
        self.roles = roles
        self.spot_strategy = spot_strategy
        self.state_in_sched = state_in_sched
        self.status = status
        self.total_resources = total_resources
        self.used_resources = used_resources
        self.v_switch_id = v_switch_id
        self.version = version
        self.vpc_id = vpc_id
        self.zone_id = zone_id

    def validate(self):
        if self.roles:
            self.roles.validate()
        if self.total_resources:
            self.total_resources.validate()
        if self.used_resources:
            self.used_resources.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_time is not None:
            result['AddTime'] = self.add_time
        if self.create_mode is not None:
            result['CreateMode'] = self.create_mode
        if self.created_by_ehpc is not None:
            result['CreatedByEhpc'] = self.created_by_ehpc
        if self.expired is not None:
            result['Expired'] = self.expired
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.ht_enabled is not None:
            result['HtEnabled'] = self.ht_enabled
        if self.id is not None:
            result['Id'] = self.id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_owner_alias is not None:
            result['ImageOwnerAlias'] = self.image_owner_alias
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address
        if self.location is not None:
            result['Location'] = self.location
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason
        if self.public_ip_address is not None:
            result['PublicIpAddress'] = self.public_ip_address
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.roles is not None:
            result['Roles'] = self.roles.to_map()
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        if self.state_in_sched is not None:
            result['StateInSched'] = self.state_in_sched
        if self.status is not None:
            result['Status'] = self.status
        if self.total_resources is not None:
            result['TotalResources'] = self.total_resources.to_map()
        if self.used_resources is not None:
            result['UsedResources'] = self.used_resources.to_map()
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.version is not None:
            result['Version'] = self.version
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddTime') is not None:
            self.add_time = m.get('AddTime')
        if m.get('CreateMode') is not None:
            self.create_mode = m.get('CreateMode')
        if m.get('CreatedByEhpc') is not None:
            self.created_by_ehpc = m.get('CreatedByEhpc')
        if m.get('Expired') is not None:
            self.expired = m.get('Expired')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('HtEnabled') is not None:
            self.ht_enabled = m.get('HtEnabled')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageOwnerAlias') is not None:
            self.image_owner_alias = m.get('ImageOwnerAlias')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')
        if m.get('PublicIpAddress') is not None:
            self.public_ip_address = m.get('PublicIpAddress')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Roles') is not None:
            temp_model = ListNodesResponseBodyNodesNodeInfoRoles()
            self.roles = temp_model.from_map(m['Roles'])
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        if m.get('StateInSched') is not None:
            self.state_in_sched = m.get('StateInSched')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TotalResources') is not None:
            temp_model = ListNodesResponseBodyNodesNodeInfoTotalResources()
            self.total_resources = temp_model.from_map(m['TotalResources'])
        if m.get('UsedResources') is not None:
            temp_model = ListNodesResponseBodyNodesNodeInfoUsedResources()
            self.used_resources = temp_model.from_map(m['UsedResources'])
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListNodesResponseBodyNodes(TeaModel):
    def __init__(
        self,
        node_info: List[ListNodesResponseBodyNodesNodeInfo] = None,
    ):
        self.node_info = node_info

    def validate(self):
        if self.node_info:
            for k in self.node_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['NodeInfo'] = []
        if self.node_info is not None:
            for k in self.node_info:
                result['NodeInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.node_info = []
        if m.get('NodeInfo') is not None:
            for k in m.get('NodeInfo'):
                temp_model = ListNodesResponseBodyNodesNodeInfo()
                self.node_info.append(temp_model.from_map(k))
        return self


class ListNodesResponseBody(TeaModel):
    def __init__(
        self,
        nodes: ListNodesResponseBodyNodes = None,
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
            self.nodes.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.nodes is not None:
            result['Nodes'] = self.nodes.to_map()
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
        if m.get('Nodes') is not None:
            temp_model = ListNodesResponseBodyNodes()
            self.nodes = temp_model.from_map(m['Nodes'])
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class ListNodesByQueueRequest(TeaModel):
    def __init__(
        self,
        async_: bool = None,
        cluster_id: str = None,
        page_number: int = None,
        page_size: int = None,
        queue_name: str = None,
    ):
        self.async_ = async_
        self.cluster_id = cluster_id
        self.page_number = page_number
        self.page_size = page_size
        self.queue_name = queue_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.async_ is not None:
            result['Async'] = self.async_
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Async') is not None:
            self.async_ = m.get('Async')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        return self


class ListNodesByQueueResponseBodyNodesNodeInfoTotalResources(TeaModel):
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


class ListNodesByQueueResponseBodyNodesNodeInfoUsedResources(TeaModel):
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


class ListNodesByQueueResponseBodyNodesNodeInfo(TeaModel):
    def __init__(
        self,
        add_time: str = None,
        create_mode: str = None,
        created_by_ehpc: bool = None,
        expired: bool = None,
        expired_time: str = None,
        host_name: str = None,
        ht_enabled: bool = None,
        id: str = None,
        image_id: str = None,
        image_owner_alias: str = None,
        ip_address: str = None,
        location: str = None,
        lock_reason: str = None,
        public_ip_address: str = None,
        region_id: str = None,
        spot_strategy: str = None,
        state_in_sched: str = None,
        status: str = None,
        total_resources: ListNodesByQueueResponseBodyNodesNodeInfoTotalResources = None,
        used_resources: ListNodesByQueueResponseBodyNodesNodeInfoUsedResources = None,
        v_switch_id: str = None,
        version: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        self.add_time = add_time
        self.create_mode = create_mode
        self.created_by_ehpc = created_by_ehpc
        self.expired = expired
        self.expired_time = expired_time
        self.host_name = host_name
        self.ht_enabled = ht_enabled
        self.id = id
        self.image_id = image_id
        self.image_owner_alias = image_owner_alias
        self.ip_address = ip_address
        self.location = location
        self.lock_reason = lock_reason
        self.public_ip_address = public_ip_address
        self.region_id = region_id
        self.spot_strategy = spot_strategy
        self.state_in_sched = state_in_sched
        self.status = status
        self.total_resources = total_resources
        self.used_resources = used_resources
        self.v_switch_id = v_switch_id
        self.version = version
        self.vpc_id = vpc_id
        self.zone_id = zone_id

    def validate(self):
        if self.total_resources:
            self.total_resources.validate()
        if self.used_resources:
            self.used_resources.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_time is not None:
            result['AddTime'] = self.add_time
        if self.create_mode is not None:
            result['CreateMode'] = self.create_mode
        if self.created_by_ehpc is not None:
            result['CreatedByEhpc'] = self.created_by_ehpc
        if self.expired is not None:
            result['Expired'] = self.expired
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.ht_enabled is not None:
            result['HtEnabled'] = self.ht_enabled
        if self.id is not None:
            result['Id'] = self.id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_owner_alias is not None:
            result['ImageOwnerAlias'] = self.image_owner_alias
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address
        if self.location is not None:
            result['Location'] = self.location
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason
        if self.public_ip_address is not None:
            result['PublicIpAddress'] = self.public_ip_address
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        if self.state_in_sched is not None:
            result['StateInSched'] = self.state_in_sched
        if self.status is not None:
            result['Status'] = self.status
        if self.total_resources is not None:
            result['TotalResources'] = self.total_resources.to_map()
        if self.used_resources is not None:
            result['UsedResources'] = self.used_resources.to_map()
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.version is not None:
            result['Version'] = self.version
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddTime') is not None:
            self.add_time = m.get('AddTime')
        if m.get('CreateMode') is not None:
            self.create_mode = m.get('CreateMode')
        if m.get('CreatedByEhpc') is not None:
            self.created_by_ehpc = m.get('CreatedByEhpc')
        if m.get('Expired') is not None:
            self.expired = m.get('Expired')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('HtEnabled') is not None:
            self.ht_enabled = m.get('HtEnabled')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageOwnerAlias') is not None:
            self.image_owner_alias = m.get('ImageOwnerAlias')
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')
        if m.get('PublicIpAddress') is not None:
            self.public_ip_address = m.get('PublicIpAddress')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        if m.get('StateInSched') is not None:
            self.state_in_sched = m.get('StateInSched')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TotalResources') is not None:
            temp_model = ListNodesByQueueResponseBodyNodesNodeInfoTotalResources()
            self.total_resources = temp_model.from_map(m['TotalResources'])
        if m.get('UsedResources') is not None:
            temp_model = ListNodesByQueueResponseBodyNodesNodeInfoUsedResources()
            self.used_resources = temp_model.from_map(m['UsedResources'])
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListNodesByQueueResponseBodyNodes(TeaModel):
    def __init__(
        self,
        node_info: List[ListNodesByQueueResponseBodyNodesNodeInfo] = None,
    ):
        self.node_info = node_info

    def validate(self):
        if self.node_info:
            for k in self.node_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['NodeInfo'] = []
        if self.node_info is not None:
            for k in self.node_info:
                result['NodeInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.node_info = []
        if m.get('NodeInfo') is not None:
            for k in m.get('NodeInfo'):
                temp_model = ListNodesByQueueResponseBodyNodesNodeInfo()
                self.node_info.append(temp_model.from_map(k))
        return self


class ListNodesByQueueResponseBody(TeaModel):
    def __init__(
        self,
        nodes: ListNodesByQueueResponseBodyNodes = None,
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
            self.nodes.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.nodes is not None:
            result['Nodes'] = self.nodes.to_map()
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
        if m.get('Nodes') is not None:
            temp_model = ListNodesByQueueResponseBodyNodes()
            self.nodes = temp_model.from_map(m['Nodes'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListNodesByQueueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListNodesByQueueResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListNodesByQueueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNodesNoPagingRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        host_name: str = None,
        role: str = None,
        sequence: str = None,
    ):
        self.cluster_id = cluster_id
        self.host_name = host_name
        self.role = role
        self.sequence = sequence

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.role is not None:
            result['Role'] = self.role
        if self.sequence is not None:
            result['Sequence'] = self.sequence
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Sequence') is not None:
            self.sequence = m.get('Sequence')
        return self


class ListNodesNoPagingResponseBodyNodesNodeInfo(TeaModel):
    def __init__(
        self,
        host_name: str = None,
        id: str = None,
        image_id: str = None,
        instance_type: str = None,
        status: str = None,
    ):
        self.host_name = host_name
        self.id = id
        self.image_id = image_id
        self.instance_type = instance_type
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.id is not None:
            result['Id'] = self.id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListNodesNoPagingResponseBodyNodes(TeaModel):
    def __init__(
        self,
        node_info: List[ListNodesNoPagingResponseBodyNodesNodeInfo] = None,
    ):
        self.node_info = node_info

    def validate(self):
        if self.node_info:
            for k in self.node_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['NodeInfo'] = []
        if self.node_info is not None:
            for k in self.node_info:
                result['NodeInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.node_info = []
        if m.get('NodeInfo') is not None:
            for k in m.get('NodeInfo'):
                temp_model = ListNodesNoPagingResponseBodyNodesNodeInfo()
                self.node_info.append(temp_model.from_map(k))
        return self


class ListNodesNoPagingResponseBody(TeaModel):
    def __init__(
        self,
        nodes: ListNodesNoPagingResponseBodyNodes = None,
        request_id: str = None,
    ):
        self.nodes = nodes
        self.request_id = request_id

    def validate(self):
        if self.nodes:
            self.nodes.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.nodes is not None:
            result['Nodes'] = self.nodes.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Nodes') is not None:
            temp_model = ListNodesNoPagingResponseBodyNodes()
            self.nodes = temp_model.from_map(m['Nodes'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListNodesNoPagingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListNodesNoPagingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListNodesNoPagingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPreferredEcsTypesRequest(TeaModel):
    def __init__(
        self,
        instance_charge_type: str = None,
        spot_strategy: str = None,
        zone_id: str = None,
    ):
        self.instance_charge_type = instance_charge_type
        self.spot_strategy = spot_strategy
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListPreferredEcsTypesResponseBodySeriesSeriesInfoRolesCompute(TeaModel):
    def __init__(
        self,
        instance_type_id: List[str] = None,
    ):
        self.instance_type_id = instance_type_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type_id is not None:
            result['InstanceTypeId'] = self.instance_type_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceTypeId') is not None:
            self.instance_type_id = m.get('InstanceTypeId')
        return self


class ListPreferredEcsTypesResponseBodySeriesSeriesInfoRolesLogin(TeaModel):
    def __init__(
        self,
        instance_type_id: List[str] = None,
    ):
        self.instance_type_id = instance_type_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type_id is not None:
            result['InstanceTypeId'] = self.instance_type_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceTypeId') is not None:
            self.instance_type_id = m.get('InstanceTypeId')
        return self


class ListPreferredEcsTypesResponseBodySeriesSeriesInfoRolesManager(TeaModel):
    def __init__(
        self,
        instance_type_id: List[str] = None,
    ):
        self.instance_type_id = instance_type_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type_id is not None:
            result['InstanceTypeId'] = self.instance_type_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceTypeId') is not None:
            self.instance_type_id = m.get('InstanceTypeId')
        return self


class ListPreferredEcsTypesResponseBodySeriesSeriesInfoRoles(TeaModel):
    def __init__(
        self,
        compute: ListPreferredEcsTypesResponseBodySeriesSeriesInfoRolesCompute = None,
        login: ListPreferredEcsTypesResponseBodySeriesSeriesInfoRolesLogin = None,
        manager: ListPreferredEcsTypesResponseBodySeriesSeriesInfoRolesManager = None,
    ):
        self.compute = compute
        self.login = login
        self.manager = manager

    def validate(self):
        if self.compute:
            self.compute.validate()
        if self.login:
            self.login.validate()
        if self.manager:
            self.manager.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compute is not None:
            result['Compute'] = self.compute.to_map()
        if self.login is not None:
            result['Login'] = self.login.to_map()
        if self.manager is not None:
            result['Manager'] = self.manager.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Compute') is not None:
            temp_model = ListPreferredEcsTypesResponseBodySeriesSeriesInfoRolesCompute()
            self.compute = temp_model.from_map(m['Compute'])
        if m.get('Login') is not None:
            temp_model = ListPreferredEcsTypesResponseBodySeriesSeriesInfoRolesLogin()
            self.login = temp_model.from_map(m['Login'])
        if m.get('Manager') is not None:
            temp_model = ListPreferredEcsTypesResponseBodySeriesSeriesInfoRolesManager()
            self.manager = temp_model.from_map(m['Manager'])
        return self


class ListPreferredEcsTypesResponseBodySeriesSeriesInfo(TeaModel):
    def __init__(
        self,
        roles: ListPreferredEcsTypesResponseBodySeriesSeriesInfoRoles = None,
        series_id: str = None,
        series_name: str = None,
    ):
        self.roles = roles
        self.series_id = series_id
        self.series_name = series_name

    def validate(self):
        if self.roles:
            self.roles.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.roles is not None:
            result['Roles'] = self.roles.to_map()
        if self.series_id is not None:
            result['SeriesId'] = self.series_id
        if self.series_name is not None:
            result['SeriesName'] = self.series_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Roles') is not None:
            temp_model = ListPreferredEcsTypesResponseBodySeriesSeriesInfoRoles()
            self.roles = temp_model.from_map(m['Roles'])
        if m.get('SeriesId') is not None:
            self.series_id = m.get('SeriesId')
        if m.get('SeriesName') is not None:
            self.series_name = m.get('SeriesName')
        return self


class ListPreferredEcsTypesResponseBodySeries(TeaModel):
    def __init__(
        self,
        series_info: List[ListPreferredEcsTypesResponseBodySeriesSeriesInfo] = None,
    ):
        self.series_info = series_info

    def validate(self):
        if self.series_info:
            for k in self.series_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SeriesInfo'] = []
        if self.series_info is not None:
            for k in self.series_info:
                result['SeriesInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.series_info = []
        if m.get('SeriesInfo') is not None:
            for k in m.get('SeriesInfo'):
                temp_model = ListPreferredEcsTypesResponseBodySeriesSeriesInfo()
                self.series_info.append(temp_model.from_map(k))
        return self


class ListPreferredEcsTypesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        series: ListPreferredEcsTypesResponseBodySeries = None,
        support_spot_instance: bool = None,
    ):
        self.request_id = request_id
        self.series = series
        self.support_spot_instance = support_spot_instance

    def validate(self):
        if self.series:
            self.series.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.series is not None:
            result['Series'] = self.series.to_map()
        if self.support_spot_instance is not None:
            result['SupportSpotInstance'] = self.support_spot_instance
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Series') is not None:
            temp_model = ListPreferredEcsTypesResponseBodySeries()
            self.series = temp_model.from_map(m['Series'])
        if m.get('SupportSpotInstance') is not None:
            self.support_spot_instance = m.get('SupportSpotInstance')
        return self


class ListPreferredEcsTypesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPreferredEcsTypesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListPreferredEcsTypesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListQueuesRequest(TeaModel):
    def __init__(
        self,
        async_: bool = None,
        cluster_id: str = None,
    ):
        self.async_ = async_
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.async_ is not None:
            result['Async'] = self.async_
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Async') is not None:
            self.async_ = m.get('Async')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class ListQueuesResponseBodyQueuesQueueInfoComputeInstanceType(TeaModel):
    def __init__(
        self,
        instance_type: List[str] = None,
    ):
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class ListQueuesResponseBodyQueuesQueueInfoSpotInstanceTypesInstance(TeaModel):
    def __init__(
        self,
        instance_type: str = None,
        spot_price_limit: float = None,
    ):
        self.instance_type = instance_type
        self.spot_price_limit = spot_price_limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.spot_price_limit is not None:
            result['SpotPriceLimit'] = self.spot_price_limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('SpotPriceLimit') is not None:
            self.spot_price_limit = m.get('SpotPriceLimit')
        return self


class ListQueuesResponseBodyQueuesQueueInfoSpotInstanceTypes(TeaModel):
    def __init__(
        self,
        instance: List[ListQueuesResponseBodyQueuesQueueInfoSpotInstanceTypesInstance] = None,
    ):
        self.instance = instance

    def validate(self):
        if self.instance:
            for k in self.instance:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Instance'] = []
        if self.instance is not None:
            for k in self.instance:
                result['Instance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance = []
        if m.get('Instance') is not None:
            for k in m.get('Instance'):
                temp_model = ListQueuesResponseBodyQueuesQueueInfoSpotInstanceTypesInstance()
                self.instance.append(temp_model.from_map(k))
        return self


class ListQueuesResponseBodyQueuesQueueInfo(TeaModel):
    def __init__(
        self,
        compute_instance_type: ListQueuesResponseBodyQueuesQueueInfoComputeInstanceType = None,
        enable_auto_grow: bool = None,
        host_name_prefix: str = None,
        host_name_suffix: str = None,
        image_id: str = None,
        queue_name: str = None,
        resource_group_id: str = None,
        spot_instance_types: ListQueuesResponseBodyQueuesQueueInfoSpotInstanceTypes = None,
        spot_strategy: str = None,
        type: str = None,
    ):
        self.compute_instance_type = compute_instance_type
        self.enable_auto_grow = enable_auto_grow
        self.host_name_prefix = host_name_prefix
        self.host_name_suffix = host_name_suffix
        self.image_id = image_id
        self.queue_name = queue_name
        self.resource_group_id = resource_group_id
        self.spot_instance_types = spot_instance_types
        self.spot_strategy = spot_strategy
        self.type = type

    def validate(self):
        if self.compute_instance_type:
            self.compute_instance_type.validate()
        if self.spot_instance_types:
            self.spot_instance_types.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compute_instance_type is not None:
            result['ComputeInstanceType'] = self.compute_instance_type.to_map()
        if self.enable_auto_grow is not None:
            result['EnableAutoGrow'] = self.enable_auto_grow
        if self.host_name_prefix is not None:
            result['HostNamePrefix'] = self.host_name_prefix
        if self.host_name_suffix is not None:
            result['HostNameSuffix'] = self.host_name_suffix
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.spot_instance_types is not None:
            result['SpotInstanceTypes'] = self.spot_instance_types.to_map()
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComputeInstanceType') is not None:
            temp_model = ListQueuesResponseBodyQueuesQueueInfoComputeInstanceType()
            self.compute_instance_type = temp_model.from_map(m['ComputeInstanceType'])
        if m.get('EnableAutoGrow') is not None:
            self.enable_auto_grow = m.get('EnableAutoGrow')
        if m.get('HostNamePrefix') is not None:
            self.host_name_prefix = m.get('HostNamePrefix')
        if m.get('HostNameSuffix') is not None:
            self.host_name_suffix = m.get('HostNameSuffix')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SpotInstanceTypes') is not None:
            temp_model = ListQueuesResponseBodyQueuesQueueInfoSpotInstanceTypes()
            self.spot_instance_types = temp_model.from_map(m['SpotInstanceTypes'])
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListQueuesResponseBodyQueues(TeaModel):
    def __init__(
        self,
        queue_info: List[ListQueuesResponseBodyQueuesQueueInfo] = None,
    ):
        self.queue_info = queue_info

    def validate(self):
        if self.queue_info:
            for k in self.queue_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['QueueInfo'] = []
        if self.queue_info is not None:
            for k in self.queue_info:
                result['QueueInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.queue_info = []
        if m.get('QueueInfo') is not None:
            for k in m.get('QueueInfo'):
                temp_model = ListQueuesResponseBodyQueuesQueueInfo()
                self.queue_info.append(temp_model.from_map(k))
        return self


class ListQueuesResponseBody(TeaModel):
    def __init__(
        self,
        queues: ListQueuesResponseBodyQueues = None,
        request_id: str = None,
    ):
        self.queues = queues
        self.request_id = request_id

    def validate(self):
        if self.queues:
            self.queues.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.queues is not None:
            result['Queues'] = self.queues.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Queues') is not None:
            temp_model = ListQueuesResponseBodyQueues()
            self.queues = temp_model.from_map(m['Queues'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class ListRegionsResponseBodyRegionsRegionInfo(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        region_id: str = None,
    ):
        self.local_name = local_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        region_info: List[ListRegionsResponseBodyRegionsRegionInfo] = None,
    ):
        self.region_info = region_info

    def validate(self):
        if self.region_info:
            for k in self.region_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RegionInfo'] = []
        if self.region_info is not None:
            for k in self.region_info:
                result['RegionInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region_info = []
        if m.get('RegionInfo') is not None:
            for k in m.get('RegionInfo'):
                temp_model = ListRegionsResponseBodyRegionsRegionInfo()
                self.region_info.append(temp_model.from_map(k))
        return self


class ListRegionsResponseBody(TeaModel):
    def __init__(
        self,
        regions: ListRegionsResponseBodyRegions = None,
        request_id: str = None,
    ):
        self.regions = regions
        self.request_id = request_id

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Regions') is not None:
            temp_model = ListRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRegionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSecurityGroupsRequest(TeaModel):
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


class ListSecurityGroupsResponseBodySecurityGroups(TeaModel):
    def __init__(
        self,
        security_group: List[str] = None,
    ):
        self.security_group = security_group

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_group is not None:
            result['SecurityGroup'] = self.security_group
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityGroup') is not None:
            self.security_group = m.get('SecurityGroup')
        return self


class ListSecurityGroupsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        security_groups: ListSecurityGroupsResponseBodySecurityGroups = None,
        total_count: int = None,
    ):
        self.request_id = request_id
        self.security_groups = security_groups
        self.total_count = total_count

    def validate(self):
        if self.security_groups:
            self.security_groups.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.security_groups is not None:
            result['SecurityGroups'] = self.security_groups.to_map()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecurityGroups') is not None:
            temp_model = ListSecurityGroupsResponseBodySecurityGroups()
            self.security_groups = temp_model.from_map(m['SecurityGroups'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListSecurityGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSecurityGroupsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListSecurityGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSoftwaresRequest(TeaModel):
    def __init__(
        self,
        ehpc_version: str = None,
        os_tag: str = None,
    ):
        self.ehpc_version = ehpc_version
        self.os_tag = os_tag

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ehpc_version is not None:
            result['EhpcVersion'] = self.ehpc_version
        if self.os_tag is not None:
            result['OsTag'] = self.os_tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EhpcVersion') is not None:
            self.ehpc_version = m.get('EhpcVersion')
        if m.get('OsTag') is not None:
            self.os_tag = m.get('OsTag')
        return self


class ListSoftwaresResponseBodySoftwaresSoftwareInfoApplicationsApplicationInfo(TeaModel):
    def __init__(
        self,
        name: str = None,
        required: bool = None,
        tag: str = None,
        version: str = None,
    ):
        self.name = name
        self.required = required
        self.tag = tag
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
        if self.required is not None:
            result['Required'] = self.required
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListSoftwaresResponseBodySoftwaresSoftwareInfoApplications(TeaModel):
    def __init__(
        self,
        application_info: List[ListSoftwaresResponseBodySoftwaresSoftwareInfoApplicationsApplicationInfo] = None,
    ):
        self.application_info = application_info

    def validate(self):
        if self.application_info:
            for k in self.application_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApplicationInfo'] = []
        if self.application_info is not None:
            for k in self.application_info:
                result['ApplicationInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.application_info = []
        if m.get('ApplicationInfo') is not None:
            for k in m.get('ApplicationInfo'):
                temp_model = ListSoftwaresResponseBodySoftwaresSoftwareInfoApplicationsApplicationInfo()
                self.application_info.append(temp_model.from_map(k))
        return self


class ListSoftwaresResponseBodySoftwaresSoftwareInfo(TeaModel):
    def __init__(
        self,
        account_type: str = None,
        account_version: str = None,
        applications: ListSoftwaresResponseBodySoftwaresSoftwareInfoApplications = None,
        ehpc_version: str = None,
        os_tag: str = None,
        scheduler_type: str = None,
        scheduler_version: str = None,
    ):
        self.account_type = account_type
        self.account_version = account_version
        self.applications = applications
        self.ehpc_version = ehpc_version
        self.os_tag = os_tag
        self.scheduler_type = scheduler_type
        self.scheduler_version = scheduler_version

    def validate(self):
        if self.applications:
            self.applications.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.account_version is not None:
            result['AccountVersion'] = self.account_version
        if self.applications is not None:
            result['Applications'] = self.applications.to_map()
        if self.ehpc_version is not None:
            result['EhpcVersion'] = self.ehpc_version
        if self.os_tag is not None:
            result['OsTag'] = self.os_tag
        if self.scheduler_type is not None:
            result['SchedulerType'] = self.scheduler_type
        if self.scheduler_version is not None:
            result['SchedulerVersion'] = self.scheduler_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('AccountVersion') is not None:
            self.account_version = m.get('AccountVersion')
        if m.get('Applications') is not None:
            temp_model = ListSoftwaresResponseBodySoftwaresSoftwareInfoApplications()
            self.applications = temp_model.from_map(m['Applications'])
        if m.get('EhpcVersion') is not None:
            self.ehpc_version = m.get('EhpcVersion')
        if m.get('OsTag') is not None:
            self.os_tag = m.get('OsTag')
        if m.get('SchedulerType') is not None:
            self.scheduler_type = m.get('SchedulerType')
        if m.get('SchedulerVersion') is not None:
            self.scheduler_version = m.get('SchedulerVersion')
        return self


class ListSoftwaresResponseBodySoftwares(TeaModel):
    def __init__(
        self,
        software_info: List[ListSoftwaresResponseBodySoftwaresSoftwareInfo] = None,
    ):
        self.software_info = software_info

    def validate(self):
        if self.software_info:
            for k in self.software_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SoftwareInfo'] = []
        if self.software_info is not None:
            for k in self.software_info:
                result['SoftwareInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.software_info = []
        if m.get('SoftwareInfo') is not None:
            for k in m.get('SoftwareInfo'):
                temp_model = ListSoftwaresResponseBodySoftwaresSoftwareInfo()
                self.software_info.append(temp_model.from_map(k))
        return self


class ListSoftwaresResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        softwares: ListSoftwaresResponseBodySoftwares = None,
    ):
        self.request_id = request_id
        self.softwares = softwares

    def validate(self):
        if self.softwares:
            self.softwares.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.softwares is not None:
            result['Softwares'] = self.softwares.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Softwares') is not None:
            temp_model = ListSoftwaresResponseBodySoftwares()
            self.softwares = temp_model.from_map(m['Softwares'])
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        next_token: str = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[ListTagResourcesRequestTag] = None,
    ):
        self.next_token = next_token
        self.region_id = region_id
        self.resource_id = resource_id
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
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
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
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class ListTasksRequest(TeaModel):
    def __init__(
        self,
        archived: bool = None,
        cluster_id: str = None,
        page_number: int = None,
        page_size: int = None,
        task_id: str = None,
    ):
        self.archived = archived
        self.cluster_id = cluster_id
        self.page_number = page_number
        self.page_size = page_size
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.archived is not None:
            result['Archived'] = self.archived
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Archived') is not None:
            self.archived = m.get('Archived')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ListTasksResponseBodyTasks(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        current_step: int = None,
        errors: str = None,
        request: str = None,
        result: str = None,
        status: str = None,
        task_id: str = None,
        task_type: str = None,
        total_steps: int = None,
    ):
        self.cluster_id = cluster_id
        self.current_step = current_step
        self.errors = errors
        self.request = request
        self.result = result
        self.status = status
        self.task_id = task_id
        self.task_type = task_type
        self.total_steps = total_steps

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.current_step is not None:
            result['CurrentStep'] = self.current_step
        if self.errors is not None:
            result['Errors'] = self.errors
        if self.request is not None:
            result['Request'] = self.request
        if self.result is not None:
            result['Result'] = self.result
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.total_steps is not None:
            result['TotalSteps'] = self.total_steps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CurrentStep') is not None:
            self.current_step = m.get('CurrentStep')
        if m.get('Errors') is not None:
            self.errors = m.get('Errors')
        if m.get('Request') is not None:
            self.request = m.get('Request')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TotalSteps') is not None:
            self.total_steps = m.get('TotalSteps')
        return self


class ListTasksResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        tasks: List[ListTasksResponseBodyTasks] = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.tasks = tasks
        self.total_count = total_count

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
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tasks = []
        if m.get('Tasks') is not None:
            for k in m.get('Tasks'):
                temp_model = ListTasksResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTasksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUpgradeClientsRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        region_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListUpgradeClientsResponseBodyClientRecords(TeaModel):
    def __init__(
        self,
        new_version: str = None,
        old_version: str = None,
        sub_uid: str = None,
        update_time: str = None,
    ):
        self.new_version = new_version
        self.old_version = old_version
        self.sub_uid = sub_uid
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_version is not None:
            result['NewVersion'] = self.new_version
        if self.old_version is not None:
            result['OldVersion'] = self.old_version
        if self.sub_uid is not None:
            result['SubUid'] = self.sub_uid
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewVersion') is not None:
            self.new_version = m.get('NewVersion')
        if m.get('OldVersion') is not None:
            self.old_version = m.get('OldVersion')
        if m.get('SubUid') is not None:
            self.sub_uid = m.get('SubUid')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListUpgradeClientsResponseBody(TeaModel):
    def __init__(
        self,
        client_records: List[ListUpgradeClientsResponseBodyClientRecords] = None,
        current_version: str = None,
        latest_version: str = None,
        request_id: str = None,
    ):
        self.client_records = client_records
        self.current_version = current_version
        self.latest_version = latest_version
        self.request_id = request_id

    def validate(self):
        if self.client_records:
            for k in self.client_records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ClientRecords'] = []
        if self.client_records is not None:
            for k in self.client_records:
                result['ClientRecords'].append(k.to_map() if k else None)
        if self.current_version is not None:
            result['CurrentVersion'] = self.current_version
        if self.latest_version is not None:
            result['LatestVersion'] = self.latest_version
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.client_records = []
        if m.get('ClientRecords') is not None:
            for k in m.get('ClientRecords'):
                temp_model = ListUpgradeClientsResponseBodyClientRecords()
                self.client_records.append(temp_model.from_map(k))
        if m.get('CurrentVersion') is not None:
            self.current_version = m.get('CurrentVersion')
        if m.get('LatestVersion') is not None:
            self.latest_version = m.get('LatestVersion')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListUpgradeClientsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUpgradeClientsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListUpgradeClientsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUsersRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
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
        name: str = None,
    ):
        self.add_time = add_time
        self.group = group
        self.name = name

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
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddTime') is not None:
            self.add_time = m.get('AddTime')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('Name') is not None:
            self.name = m.get('Name')
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
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class ListUsersAsyncRequest(TeaModel):
    def __init__(
        self,
        async_id: str = None,
        cluster_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.async_id = async_id
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
        if self.async_id is not None:
            result['AsyncId'] = self.async_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsyncId') is not None:
            self.async_id = m.get('AsyncId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListUsersAsyncResponseBodyUsersUserInfo(TeaModel):
    def __init__(
        self,
        add_time: str = None,
        group: str = None,
        group_id: str = None,
        name: str = None,
        user_id: str = None,
    ):
        self.add_time = add_time
        self.group = group
        self.group_id = group_id
        self.name = name
        self.user_id = user_id

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
        if self.name is not None:
            result['Name'] = self.name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddTime') is not None:
            self.add_time = m.get('AddTime')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListUsersAsyncResponseBodyUsers(TeaModel):
    def __init__(
        self,
        user_info: List[ListUsersAsyncResponseBodyUsersUserInfo] = None,
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
                temp_model = ListUsersAsyncResponseBodyUsersUserInfo()
                self.user_info.append(temp_model.from_map(k))
        return self


class ListUsersAsyncResponseBody(TeaModel):
    def __init__(
        self,
        async_id: str = None,
        async_status: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        users: ListUsersAsyncResponseBodyUsers = None,
    ):
        self.async_id = async_id
        self.async_status = async_status
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count
        self.users = users

    def validate(self):
        if self.users:
            self.users.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.async_id is not None:
            result['AsyncId'] = self.async_id
        if self.async_status is not None:
            result['AsyncStatus'] = self.async_status
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
        if m.get('AsyncId') is not None:
            self.async_id = m.get('AsyncId')
        if m.get('AsyncStatus') is not None:
            self.async_status = m.get('AsyncStatus')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Users') is not None:
            temp_model = ListUsersAsyncResponseBodyUsers()
            self.users = temp_model.from_map(m['Users'])
        return self


class ListUsersAsyncResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUsersAsyncResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListUsersAsyncResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVolumesRequest(TeaModel):
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


class ListVolumesResponseBodyVolumesVolumeInfoAdditionalVolumesVolumeInfo(TeaModel):
    def __init__(
        self,
        job_queue: str = None,
        local_directory: str = None,
        location: str = None,
        remote_directory: str = None,
        role: str = None,
        volume_id: str = None,
        volume_mountpoint: str = None,
        volume_protocol: str = None,
        volume_type: str = None,
    ):
        self.job_queue = job_queue
        self.local_directory = local_directory
        self.location = location
        self.remote_directory = remote_directory
        self.role = role
        self.volume_id = volume_id
        self.volume_mountpoint = volume_mountpoint
        self.volume_protocol = volume_protocol
        self.volume_type = volume_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_queue is not None:
            result['JobQueue'] = self.job_queue
        if self.local_directory is not None:
            result['LocalDirectory'] = self.local_directory
        if self.location is not None:
            result['Location'] = self.location
        if self.remote_directory is not None:
            result['RemoteDirectory'] = self.remote_directory
        if self.role is not None:
            result['Role'] = self.role
        if self.volume_id is not None:
            result['VolumeId'] = self.volume_id
        if self.volume_mountpoint is not None:
            result['VolumeMountpoint'] = self.volume_mountpoint
        if self.volume_protocol is not None:
            result['VolumeProtocol'] = self.volume_protocol
        if self.volume_type is not None:
            result['VolumeType'] = self.volume_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobQueue') is not None:
            self.job_queue = m.get('JobQueue')
        if m.get('LocalDirectory') is not None:
            self.local_directory = m.get('LocalDirectory')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('RemoteDirectory') is not None:
            self.remote_directory = m.get('RemoteDirectory')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('VolumeId') is not None:
            self.volume_id = m.get('VolumeId')
        if m.get('VolumeMountpoint') is not None:
            self.volume_mountpoint = m.get('VolumeMountpoint')
        if m.get('VolumeProtocol') is not None:
            self.volume_protocol = m.get('VolumeProtocol')
        if m.get('VolumeType') is not None:
            self.volume_type = m.get('VolumeType')
        return self


class ListVolumesResponseBodyVolumesVolumeInfoAdditionalVolumes(TeaModel):
    def __init__(
        self,
        volume_info: List[ListVolumesResponseBodyVolumesVolumeInfoAdditionalVolumesVolumeInfo] = None,
    ):
        self.volume_info = volume_info

    def validate(self):
        if self.volume_info:
            for k in self.volume_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['VolumeInfo'] = []
        if self.volume_info is not None:
            for k in self.volume_info:
                result['VolumeInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.volume_info = []
        if m.get('VolumeInfo') is not None:
            for k in m.get('VolumeInfo'):
                temp_model = ListVolumesResponseBodyVolumesVolumeInfoAdditionalVolumesVolumeInfo()
                self.volume_info.append(temp_model.from_map(k))
        return self


class ListVolumesResponseBodyVolumesVolumeInfo(TeaModel):
    def __init__(
        self,
        additional_volumes: ListVolumesResponseBodyVolumesVolumeInfoAdditionalVolumes = None,
        cluster_id: str = None,
        cluster_name: str = None,
        region_id: str = None,
        remote_directory: str = None,
        volume_id: str = None,
        volume_mountpoint: str = None,
        volume_protocol: str = None,
        volume_type: str = None,
    ):
        self.additional_volumes = additional_volumes
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.region_id = region_id
        self.remote_directory = remote_directory
        self.volume_id = volume_id
        self.volume_mountpoint = volume_mountpoint
        self.volume_protocol = volume_protocol
        self.volume_type = volume_type

    def validate(self):
        if self.additional_volumes:
            self.additional_volumes.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.additional_volumes is not None:
            result['AdditionalVolumes'] = self.additional_volumes.to_map()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.remote_directory is not None:
            result['RemoteDirectory'] = self.remote_directory
        if self.volume_id is not None:
            result['VolumeId'] = self.volume_id
        if self.volume_mountpoint is not None:
            result['VolumeMountpoint'] = self.volume_mountpoint
        if self.volume_protocol is not None:
            result['VolumeProtocol'] = self.volume_protocol
        if self.volume_type is not None:
            result['VolumeType'] = self.volume_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdditionalVolumes') is not None:
            temp_model = ListVolumesResponseBodyVolumesVolumeInfoAdditionalVolumes()
            self.additional_volumes = temp_model.from_map(m['AdditionalVolumes'])
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RemoteDirectory') is not None:
            self.remote_directory = m.get('RemoteDirectory')
        if m.get('VolumeId') is not None:
            self.volume_id = m.get('VolumeId')
        if m.get('VolumeMountpoint') is not None:
            self.volume_mountpoint = m.get('VolumeMountpoint')
        if m.get('VolumeProtocol') is not None:
            self.volume_protocol = m.get('VolumeProtocol')
        if m.get('VolumeType') is not None:
            self.volume_type = m.get('VolumeType')
        return self


class ListVolumesResponseBodyVolumes(TeaModel):
    def __init__(
        self,
        volume_info: List[ListVolumesResponseBodyVolumesVolumeInfo] = None,
    ):
        self.volume_info = volume_info

    def validate(self):
        if self.volume_info:
            for k in self.volume_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['VolumeInfo'] = []
        if self.volume_info is not None:
            for k in self.volume_info:
                result['VolumeInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.volume_info = []
        if m.get('VolumeInfo') is not None:
            for k in m.get('VolumeInfo'):
                temp_model = ListVolumesResponseBodyVolumesVolumeInfo()
                self.volume_info.append(temp_model.from_map(k))
        return self


class ListVolumesResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        volumes: ListVolumesResponseBodyVolumes = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count
        self.volumes = volumes

    def validate(self):
        if self.volumes:
            self.volumes.validate()

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
        if self.volumes is not None:
            result['Volumes'] = self.volumes.to_map()
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
        if m.get('Volumes') is not None:
            temp_model = ListVolumesResponseBodyVolumes()
            self.volumes = temp_model.from_map(m['Volumes'])
        return self


class ListVolumesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListVolumesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListVolumesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyClusterAttributesRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        description: str = None,
        image_id: str = None,
        image_owner_alias: str = None,
        name: str = None,
    ):
        self.cluster_id = cluster_id
        self.description = description
        self.image_id = image_id
        self.image_owner_alias = image_owner_alias
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.description is not None:
            result['Description'] = self.description
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_owner_alias is not None:
            result['ImageOwnerAlias'] = self.image_owner_alias
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageOwnerAlias') is not None:
            self.image_owner_alias = m.get('ImageOwnerAlias')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ModifyClusterAttributesResponseBody(TeaModel):
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


class ModifyClusterAttributesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyClusterAttributesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ModifyClusterAttributesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyContainerAppAttributesRequest(TeaModel):
    def __init__(
        self,
        container_id: str = None,
        description: str = None,
    ):
        self.container_id = container_id
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_id is not None:
            result['ContainerId'] = self.container_id
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerId') is not None:
            self.container_id = m.get('ContainerId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class ModifyContainerAppAttributesResponseBody(TeaModel):
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


class ModifyContainerAppAttributesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyContainerAppAttributesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ModifyContainerAppAttributesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyImageGatewayConfigRequestRepo(TeaModel):
    def __init__(
        self,
        auth: str = None,
        location: str = None,
        url: str = None,
    ):
        self.auth = auth
        self.location = location
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth is not None:
            result['Auth'] = self.auth
        if self.location is not None:
            result['Location'] = self.location
        if self.url is not None:
            result['URL'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Auth') is not None:
            self.auth = m.get('Auth')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('URL') is not None:
            self.url = m.get('URL')
        return self


class ModifyImageGatewayConfigRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        dbpassword: str = None,
        dbserver_info: str = None,
        dbtype: str = None,
        dbusername: str = None,
        default_repo_location: str = None,
        image_expiration_timeout: str = None,
        pull_update_timeout: int = None,
        repo: List[ModifyImageGatewayConfigRequestRepo] = None,
    ):
        self.cluster_id = cluster_id
        self.dbpassword = dbpassword
        self.dbserver_info = dbserver_info
        self.dbtype = dbtype
        self.dbusername = dbusername
        self.default_repo_location = default_repo_location
        self.image_expiration_timeout = image_expiration_timeout
        self.pull_update_timeout = pull_update_timeout
        self.repo = repo

    def validate(self):
        if self.repo:
            for k in self.repo:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.dbpassword is not None:
            result['DBPassword'] = self.dbpassword
        if self.dbserver_info is not None:
            result['DBServerInfo'] = self.dbserver_info
        if self.dbtype is not None:
            result['DBType'] = self.dbtype
        if self.dbusername is not None:
            result['DBUsername'] = self.dbusername
        if self.default_repo_location is not None:
            result['DefaultRepoLocation'] = self.default_repo_location
        if self.image_expiration_timeout is not None:
            result['ImageExpirationTimeout'] = self.image_expiration_timeout
        if self.pull_update_timeout is not None:
            result['PullUpdateTimeout'] = self.pull_update_timeout
        result['Repo'] = []
        if self.repo is not None:
            for k in self.repo:
                result['Repo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DBPassword') is not None:
            self.dbpassword = m.get('DBPassword')
        if m.get('DBServerInfo') is not None:
            self.dbserver_info = m.get('DBServerInfo')
        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')
        if m.get('DBUsername') is not None:
            self.dbusername = m.get('DBUsername')
        if m.get('DefaultRepoLocation') is not None:
            self.default_repo_location = m.get('DefaultRepoLocation')
        if m.get('ImageExpirationTimeout') is not None:
            self.image_expiration_timeout = m.get('ImageExpirationTimeout')
        if m.get('PullUpdateTimeout') is not None:
            self.pull_update_timeout = m.get('PullUpdateTimeout')
        self.repo = []
        if m.get('Repo') is not None:
            for k in m.get('Repo'):
                temp_model = ModifyImageGatewayConfigRequestRepo()
                self.repo.append(temp_model.from_map(k))
        return self


class ModifyImageGatewayConfigResponseBody(TeaModel):
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


class ModifyImageGatewayConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyImageGatewayConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ModifyImageGatewayConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyUserGroupsRequestUser(TeaModel):
    def __init__(
        self,
        group: str = None,
        name: str = None,
    ):
        self.group = group
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group is not None:
            result['Group'] = self.group
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ModifyUserGroupsRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        user: List[ModifyUserGroupsRequestUser] = None,
    ):
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
                temp_model = ModifyUserGroupsRequestUser()
                self.user.append(temp_model.from_map(k))
        return self


class ModifyUserGroupsResponseBody(TeaModel):
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


class ModifyUserGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyUserGroupsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ModifyUserGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyUserPasswordsRequestUser(TeaModel):
    def __init__(
        self,
        name: str = None,
        password: str = None,
    ):
        self.name = name
        self.password = password

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.password is not None:
            result['Password'] = self.password
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        return self


class ModifyUserPasswordsRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        user: List[ModifyUserPasswordsRequestUser] = None,
    ):
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
                temp_model = ModifyUserPasswordsRequestUser()
                self.user.append(temp_model.from_map(k))
        return self


class ModifyUserPasswordsResponseBody(TeaModel):
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


class ModifyUserPasswordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyUserPasswordsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ModifyUserPasswordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyVisualServicePasswdRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        passwd: str = None,
        runas_user: str = None,
        runas_user_password: str = None,
    ):
        self.cluster_id = cluster_id
        self.passwd = passwd
        self.runas_user = runas_user
        self.runas_user_password = runas_user_password

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.passwd is not None:
            result['Passwd'] = self.passwd
        if self.runas_user is not None:
            result['RunasUser'] = self.runas_user
        if self.runas_user_password is not None:
            result['RunasUserPassword'] = self.runas_user_password
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Passwd') is not None:
            self.passwd = m.get('Passwd')
        if m.get('RunasUser') is not None:
            self.runas_user = m.get('RunasUser')
        if m.get('RunasUserPassword') is not None:
            self.runas_user_password = m.get('RunasUserPassword')
        return self


class ModifyVisualServicePasswdResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
    ):
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyVisualServicePasswdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyVisualServicePasswdResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ModifyVisualServicePasswdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MountNFSRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        mount_dir: str = None,
        nfs_dir: str = None,
        protocol_type: str = None,
        remote_dir: str = None,
    ):
        self.instance_id = instance_id
        self.mount_dir = mount_dir
        self.nfs_dir = nfs_dir
        self.protocol_type = protocol_type
        self.remote_dir = remote_dir

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.mount_dir is not None:
            result['MountDir'] = self.mount_dir
        if self.nfs_dir is not None:
            result['NfsDir'] = self.nfs_dir
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.remote_dir is not None:
            result['RemoteDir'] = self.remote_dir
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MountDir') is not None:
            self.mount_dir = m.get('MountDir')
        if m.get('NfsDir') is not None:
            self.nfs_dir = m.get('NfsDir')
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('RemoteDir') is not None:
            self.remote_dir = m.get('RemoteDir')
        return self


class MountNFSResponseBody(TeaModel):
    def __init__(
        self,
        invoke_id: str = None,
        request_id: str = None,
    ):
        self.invoke_id = invoke_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class MountNFSResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: MountNFSResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = MountNFSResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PullImageRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        container_type: str = None,
        image_tag: str = None,
        repository: str = None,
    ):
        self.cluster_id = cluster_id
        self.container_type = container_type
        self.image_tag = image_tag
        self.repository = repository

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.container_type is not None:
            result['ContainerType'] = self.container_type
        if self.image_tag is not None:
            result['ImageTag'] = self.image_tag
        if self.repository is not None:
            result['Repository'] = self.repository
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ContainerType') is not None:
            self.container_type = m.get('ContainerType')
        if m.get('ImageTag') is not None:
            self.image_tag = m.get('ImageTag')
        if m.get('Repository') is not None:
            self.repository = m.get('Repository')
        return self


class PullImageResponseBody(TeaModel):
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


class PullImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PullImageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = PullImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryServicePackAndPriceResponseBodyServicePackServicePackInfo(TeaModel):
    def __init__(
        self,
        capacity: int = None,
        end_time: int = None,
        instance_name: str = None,
        start_time: int = None,
    ):
        self.capacity = capacity
        self.end_time = end_time
        self.instance_name = instance_name
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class QueryServicePackAndPriceResponseBodyServicePack(TeaModel):
    def __init__(
        self,
        service_pack_info: List[QueryServicePackAndPriceResponseBodyServicePackServicePackInfo] = None,
    ):
        self.service_pack_info = service_pack_info

    def validate(self):
        if self.service_pack_info:
            for k in self.service_pack_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ServicePackInfo'] = []
        if self.service_pack_info is not None:
            for k in self.service_pack_info:
                result['ServicePackInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.service_pack_info = []
        if m.get('ServicePackInfo') is not None:
            for k in m.get('ServicePackInfo'):
                temp_model = QueryServicePackAndPriceResponseBodyServicePackServicePackInfo()
                self.service_pack_info.append(temp_model.from_map(k))
        return self


class QueryServicePackAndPriceResponseBody(TeaModel):
    def __init__(
        self,
        charge_amount: int = None,
        currency: str = None,
        discount_price: float = None,
        original_amount: int = None,
        original_price: float = None,
        region_id: str = None,
        request_id: str = None,
        service_pack: QueryServicePackAndPriceResponseBodyServicePack = None,
        trade_price: float = None,
    ):
        self.charge_amount = charge_amount
        self.currency = currency
        self.discount_price = discount_price
        self.original_amount = original_amount
        self.original_price = original_price
        self.region_id = region_id
        self.request_id = request_id
        self.service_pack = service_pack
        self.trade_price = trade_price

    def validate(self):
        if self.service_pack:
            self.service_pack.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_amount is not None:
            result['ChargeAmount'] = self.charge_amount
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.original_amount is not None:
            result['OriginalAmount'] = self.original_amount
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_pack is not None:
            result['ServicePack'] = self.service_pack.to_map()
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeAmount') is not None:
            self.charge_amount = m.get('ChargeAmount')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('OriginalAmount') is not None:
            self.original_amount = m.get('OriginalAmount')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServicePack') is not None:
            temp_model = QueryServicePackAndPriceResponseBodyServicePack()
            self.service_pack = temp_model.from_map(m['ServicePack'])
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        return self


class QueryServicePackAndPriceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryServicePackAndPriceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = QueryServicePackAndPriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecoverClusterRequest(TeaModel):
    def __init__(
        self,
        account_type: str = None,
        client_version: str = None,
        cluster_id: str = None,
        image_id: str = None,
        image_owner_alias: str = None,
        os_tag: str = None,
        scheduler_type: str = None,
    ):
        self.account_type = account_type
        self.client_version = client_version
        self.cluster_id = cluster_id
        self.image_id = image_id
        self.image_owner_alias = image_owner_alias
        self.os_tag = os_tag
        self.scheduler_type = scheduler_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_owner_alias is not None:
            result['ImageOwnerAlias'] = self.image_owner_alias
        if self.os_tag is not None:
            result['OsTag'] = self.os_tag
        if self.scheduler_type is not None:
            result['SchedulerType'] = self.scheduler_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageOwnerAlias') is not None:
            self.image_owner_alias = m.get('ImageOwnerAlias')
        if m.get('OsTag') is not None:
            self.os_tag = m.get('OsTag')
        if m.get('SchedulerType') is not None:
            self.scheduler_type = m.get('SchedulerType')
        return self


class RecoverClusterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        self.request_id = request_id
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
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class RecoverClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RecoverClusterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = RecoverClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RerunJobsRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        jobs: str = None,
    ):
        self.cluster_id = cluster_id
        self.jobs = jobs

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.jobs is not None:
            result['Jobs'] = self.jobs
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Jobs') is not None:
            self.jobs = m.get('Jobs')
        return self


class RerunJobsResponseBody(TeaModel):
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


class RerunJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RerunJobsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = RerunJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetNodesRequestInstance(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ResetNodesRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        instance: List[ResetNodesRequestInstance] = None,
    ):
        self.cluster_id = cluster_id
        self.instance = instance

    def validate(self):
        if self.instance:
            for k in self.instance:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        result['Instance'] = []
        if self.instance is not None:
            for k in self.instance:
                result['Instance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        self.instance = []
        if m.get('Instance') is not None:
            for k in m.get('Instance'):
                temp_model = ResetNodesRequestInstance()
                self.instance.append(temp_model.from_map(k))
        return self


class ResetNodesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        self.request_id = request_id
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
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ResetNodesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResetNodesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ResetNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunCloudMetricProfilingRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        duration: int = None,
        freq: int = None,
        host_name: str = None,
        process_id: int = None,
        region_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.duration = duration
        self.freq = freq
        self.host_name = host_name
        self.process_id = process_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.freq is not None:
            result['Freq'] = self.freq
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.process_id is not None:
            result['ProcessId'] = self.process_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Freq') is not None:
            self.freq = m.get('Freq')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('ProcessId') is not None:
            self.process_id = m.get('ProcessId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class RunCloudMetricProfilingResponseBody(TeaModel):
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


class RunCloudMetricProfilingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunCloudMetricProfilingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = RunCloudMetricProfilingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetAutoScaleConfigRequestQueuesDataDisks(TeaModel):
    def __init__(
        self,
        data_disk_category: str = None,
        data_disk_delete_with_instance: bool = None,
        data_disk_encrypted: bool = None,
        data_disk_kmskey_id: str = None,
        data_disk_performance_level: str = None,
        data_disk_size: int = None,
    ):
        self.data_disk_category = data_disk_category
        self.data_disk_delete_with_instance = data_disk_delete_with_instance
        self.data_disk_encrypted = data_disk_encrypted
        self.data_disk_kmskey_id = data_disk_kmskey_id
        self.data_disk_performance_level = data_disk_performance_level
        self.data_disk_size = data_disk_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_disk_category is not None:
            result['DataDiskCategory'] = self.data_disk_category
        if self.data_disk_delete_with_instance is not None:
            result['DataDiskDeleteWithInstance'] = self.data_disk_delete_with_instance
        if self.data_disk_encrypted is not None:
            result['DataDiskEncrypted'] = self.data_disk_encrypted
        if self.data_disk_kmskey_id is not None:
            result['DataDiskKMSKeyId'] = self.data_disk_kmskey_id
        if self.data_disk_performance_level is not None:
            result['DataDiskPerformanceLevel'] = self.data_disk_performance_level
        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataDiskCategory') is not None:
            self.data_disk_category = m.get('DataDiskCategory')
        if m.get('DataDiskDeleteWithInstance') is not None:
            self.data_disk_delete_with_instance = m.get('DataDiskDeleteWithInstance')
        if m.get('DataDiskEncrypted') is not None:
            self.data_disk_encrypted = m.get('DataDiskEncrypted')
        if m.get('DataDiskKMSKeyId') is not None:
            self.data_disk_kmskey_id = m.get('DataDiskKMSKeyId')
        if m.get('DataDiskPerformanceLevel') is not None:
            self.data_disk_performance_level = m.get('DataDiskPerformanceLevel')
        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')
        return self


class SetAutoScaleConfigRequestQueuesInstanceTypes(TeaModel):
    def __init__(
        self,
        instance_type: str = None,
        spot_price_limit: float = None,
        spot_strategy: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        self.instance_type = instance_type
        self.spot_price_limit = spot_price_limit
        self.spot_strategy = spot_strategy
        self.v_switch_id = v_switch_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.spot_price_limit is not None:
            result['SpotPriceLimit'] = self.spot_price_limit
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('SpotPriceLimit') is not None:
            self.spot_price_limit = m.get('SpotPriceLimit')
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class SetAutoScaleConfigRequestQueues(TeaModel):
    def __init__(
        self,
        data_disks: List[SetAutoScaleConfigRequestQueuesDataDisks] = None,
        enable_auto_grow: bool = None,
        enable_auto_shrink: bool = None,
        host_name_prefix: str = None,
        host_name_suffix: str = None,
        instance_type: str = None,
        instance_types: List[SetAutoScaleConfigRequestQueuesInstanceTypes] = None,
        max_nodes_in_queue: int = None,
        max_nodes_per_cycle: int = None,
        min_nodes_in_queue: int = None,
        min_nodes_per_cycle: int = None,
        queue_image_id: str = None,
        queue_name: str = None,
        spot_price_limit: float = None,
        spot_strategy: str = None,
        system_disk_category: str = None,
        system_disk_level: str = None,
        system_disk_size: int = None,
    ):
        self.data_disks = data_disks
        self.enable_auto_grow = enable_auto_grow
        self.enable_auto_shrink = enable_auto_shrink
        self.host_name_prefix = host_name_prefix
        self.host_name_suffix = host_name_suffix
        self.instance_type = instance_type
        self.instance_types = instance_types
        self.max_nodes_in_queue = max_nodes_in_queue
        self.max_nodes_per_cycle = max_nodes_per_cycle
        self.min_nodes_in_queue = min_nodes_in_queue
        self.min_nodes_per_cycle = min_nodes_per_cycle
        self.queue_image_id = queue_image_id
        self.queue_name = queue_name
        self.spot_price_limit = spot_price_limit
        self.spot_strategy = spot_strategy
        self.system_disk_category = system_disk_category
        self.system_disk_level = system_disk_level
        self.system_disk_size = system_disk_size

    def validate(self):
        if self.data_disks:
            for k in self.data_disks:
                if k:
                    k.validate()
        if self.instance_types:
            for k in self.instance_types:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataDisks'] = []
        if self.data_disks is not None:
            for k in self.data_disks:
                result['DataDisks'].append(k.to_map() if k else None)
        if self.enable_auto_grow is not None:
            result['EnableAutoGrow'] = self.enable_auto_grow
        if self.enable_auto_shrink is not None:
            result['EnableAutoShrink'] = self.enable_auto_shrink
        if self.host_name_prefix is not None:
            result['HostNamePrefix'] = self.host_name_prefix
        if self.host_name_suffix is not None:
            result['HostNameSuffix'] = self.host_name_suffix
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        result['InstanceTypes'] = []
        if self.instance_types is not None:
            for k in self.instance_types:
                result['InstanceTypes'].append(k.to_map() if k else None)
        if self.max_nodes_in_queue is not None:
            result['MaxNodesInQueue'] = self.max_nodes_in_queue
        if self.max_nodes_per_cycle is not None:
            result['MaxNodesPerCycle'] = self.max_nodes_per_cycle
        if self.min_nodes_in_queue is not None:
            result['MinNodesInQueue'] = self.min_nodes_in_queue
        if self.min_nodes_per_cycle is not None:
            result['MinNodesPerCycle'] = self.min_nodes_per_cycle
        if self.queue_image_id is not None:
            result['QueueImageId'] = self.queue_image_id
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.spot_price_limit is not None:
            result['SpotPriceLimit'] = self.spot_price_limit
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        if self.system_disk_category is not None:
            result['SystemDiskCategory'] = self.system_disk_category
        if self.system_disk_level is not None:
            result['SystemDiskLevel'] = self.system_disk_level
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_disks = []
        if m.get('DataDisks') is not None:
            for k in m.get('DataDisks'):
                temp_model = SetAutoScaleConfigRequestQueuesDataDisks()
                self.data_disks.append(temp_model.from_map(k))
        if m.get('EnableAutoGrow') is not None:
            self.enable_auto_grow = m.get('EnableAutoGrow')
        if m.get('EnableAutoShrink') is not None:
            self.enable_auto_shrink = m.get('EnableAutoShrink')
        if m.get('HostNamePrefix') is not None:
            self.host_name_prefix = m.get('HostNamePrefix')
        if m.get('HostNameSuffix') is not None:
            self.host_name_suffix = m.get('HostNameSuffix')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        self.instance_types = []
        if m.get('InstanceTypes') is not None:
            for k in m.get('InstanceTypes'):
                temp_model = SetAutoScaleConfigRequestQueuesInstanceTypes()
                self.instance_types.append(temp_model.from_map(k))
        if m.get('MaxNodesInQueue') is not None:
            self.max_nodes_in_queue = m.get('MaxNodesInQueue')
        if m.get('MaxNodesPerCycle') is not None:
            self.max_nodes_per_cycle = m.get('MaxNodesPerCycle')
        if m.get('MinNodesInQueue') is not None:
            self.min_nodes_in_queue = m.get('MinNodesInQueue')
        if m.get('MinNodesPerCycle') is not None:
            self.min_nodes_per_cycle = m.get('MinNodesPerCycle')
        if m.get('QueueImageId') is not None:
            self.queue_image_id = m.get('QueueImageId')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('SpotPriceLimit') is not None:
            self.spot_price_limit = m.get('SpotPriceLimit')
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        if m.get('SystemDiskCategory') is not None:
            self.system_disk_category = m.get('SystemDiskCategory')
        if m.get('SystemDiskLevel') is not None:
            self.system_disk_level = m.get('SystemDiskLevel')
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        return self


class SetAutoScaleConfigRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        enable_auto_grow: bool = None,
        enable_auto_shrink: bool = None,
        exclude_nodes: str = None,
        extra_nodes_grow_ratio: int = None,
        grow_interval_in_minutes: int = None,
        grow_ratio: int = None,
        grow_timeout_in_minutes: int = None,
        image_id: str = None,
        max_nodes_in_cluster: int = None,
        queues: List[SetAutoScaleConfigRequestQueues] = None,
        shrink_idle_times: int = None,
        shrink_interval_in_minutes: int = None,
        spot_price_limit: float = None,
        spot_strategy: str = None,
    ):
        self.cluster_id = cluster_id
        self.enable_auto_grow = enable_auto_grow
        self.enable_auto_shrink = enable_auto_shrink
        self.exclude_nodes = exclude_nodes
        self.extra_nodes_grow_ratio = extra_nodes_grow_ratio
        self.grow_interval_in_minutes = grow_interval_in_minutes
        self.grow_ratio = grow_ratio
        self.grow_timeout_in_minutes = grow_timeout_in_minutes
        self.image_id = image_id
        self.max_nodes_in_cluster = max_nodes_in_cluster
        self.queues = queues
        self.shrink_idle_times = shrink_idle_times
        self.shrink_interval_in_minutes = shrink_interval_in_minutes
        self.spot_price_limit = spot_price_limit
        self.spot_strategy = spot_strategy

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
        if self.enable_auto_grow is not None:
            result['EnableAutoGrow'] = self.enable_auto_grow
        if self.enable_auto_shrink is not None:
            result['EnableAutoShrink'] = self.enable_auto_shrink
        if self.exclude_nodes is not None:
            result['ExcludeNodes'] = self.exclude_nodes
        if self.extra_nodes_grow_ratio is not None:
            result['ExtraNodesGrowRatio'] = self.extra_nodes_grow_ratio
        if self.grow_interval_in_minutes is not None:
            result['GrowIntervalInMinutes'] = self.grow_interval_in_minutes
        if self.grow_ratio is not None:
            result['GrowRatio'] = self.grow_ratio
        if self.grow_timeout_in_minutes is not None:
            result['GrowTimeoutInMinutes'] = self.grow_timeout_in_minutes
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.max_nodes_in_cluster is not None:
            result['MaxNodesInCluster'] = self.max_nodes_in_cluster
        result['Queues'] = []
        if self.queues is not None:
            for k in self.queues:
                result['Queues'].append(k.to_map() if k else None)
        if self.shrink_idle_times is not None:
            result['ShrinkIdleTimes'] = self.shrink_idle_times
        if self.shrink_interval_in_minutes is not None:
            result['ShrinkIntervalInMinutes'] = self.shrink_interval_in_minutes
        if self.spot_price_limit is not None:
            result['SpotPriceLimit'] = self.spot_price_limit
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('EnableAutoGrow') is not None:
            self.enable_auto_grow = m.get('EnableAutoGrow')
        if m.get('EnableAutoShrink') is not None:
            self.enable_auto_shrink = m.get('EnableAutoShrink')
        if m.get('ExcludeNodes') is not None:
            self.exclude_nodes = m.get('ExcludeNodes')
        if m.get('ExtraNodesGrowRatio') is not None:
            self.extra_nodes_grow_ratio = m.get('ExtraNodesGrowRatio')
        if m.get('GrowIntervalInMinutes') is not None:
            self.grow_interval_in_minutes = m.get('GrowIntervalInMinutes')
        if m.get('GrowRatio') is not None:
            self.grow_ratio = m.get('GrowRatio')
        if m.get('GrowTimeoutInMinutes') is not None:
            self.grow_timeout_in_minutes = m.get('GrowTimeoutInMinutes')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('MaxNodesInCluster') is not None:
            self.max_nodes_in_cluster = m.get('MaxNodesInCluster')
        self.queues = []
        if m.get('Queues') is not None:
            for k in m.get('Queues'):
                temp_model = SetAutoScaleConfigRequestQueues()
                self.queues.append(temp_model.from_map(k))
        if m.get('ShrinkIdleTimes') is not None:
            self.shrink_idle_times = m.get('ShrinkIdleTimes')
        if m.get('ShrinkIntervalInMinutes') is not None:
            self.shrink_interval_in_minutes = m.get('ShrinkIntervalInMinutes')
        if m.get('SpotPriceLimit') is not None:
            self.spot_price_limit = m.get('SpotPriceLimit')
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        return self


class SetAutoScaleConfigResponseBody(TeaModel):
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


class SetAutoScaleConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetAutoScaleConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = SetAutoScaleConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetGWSClusterPolicyRequest(TeaModel):
    def __init__(
        self,
        async_mode: bool = None,
        clipboard: str = None,
        cluster_id: str = None,
        local_drive: str = None,
        udp_port: str = None,
        usb_redirect: str = None,
        watermark: str = None,
    ):
        self.async_mode = async_mode
        self.clipboard = clipboard
        self.cluster_id = cluster_id
        self.local_drive = local_drive
        self.udp_port = udp_port
        self.usb_redirect = usb_redirect
        self.watermark = watermark

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.async_mode is not None:
            result['AsyncMode'] = self.async_mode
        if self.clipboard is not None:
            result['Clipboard'] = self.clipboard
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.local_drive is not None:
            result['LocalDrive'] = self.local_drive
        if self.udp_port is not None:
            result['UdpPort'] = self.udp_port
        if self.usb_redirect is not None:
            result['UsbRedirect'] = self.usb_redirect
        if self.watermark is not None:
            result['Watermark'] = self.watermark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsyncMode') is not None:
            self.async_mode = m.get('AsyncMode')
        if m.get('Clipboard') is not None:
            self.clipboard = m.get('Clipboard')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('LocalDrive') is not None:
            self.local_drive = m.get('LocalDrive')
        if m.get('UdpPort') is not None:
            self.udp_port = m.get('UdpPort')
        if m.get('UsbRedirect') is not None:
            self.usb_redirect = m.get('UsbRedirect')
        if m.get('Watermark') is not None:
            self.watermark = m.get('Watermark')
        return self


class SetGWSClusterPolicyResponseBody(TeaModel):
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


class SetGWSClusterPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetGWSClusterPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = SetGWSClusterPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetGWSInstanceNameRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        name: str = None,
    ):
        self.instance_id = instance_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class SetGWSInstanceNameResponseBody(TeaModel):
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


class SetGWSInstanceNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetGWSInstanceNameResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = SetGWSInstanceNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetGWSInstanceUserRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        user_name: str = None,
        user_uid: str = None,
    ):
        self.instance_id = instance_id
        self.user_name = user_name
        self.user_uid = user_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.user_uid is not None:
            result['UserUid'] = self.user_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('UserUid') is not None:
            self.user_uid = m.get('UserUid')
        return self


class SetGWSInstanceUserResponseBody(TeaModel):
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


class SetGWSInstanceUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetGWSInstanceUserResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = SetGWSInstanceUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetPostScriptsRequestPostInstallScripts(TeaModel):
    def __init__(
        self,
        args: str = None,
        url: str = None,
    ):
        self.args = args
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.args is not None:
            result['Args'] = self.args
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Args') is not None:
            self.args = m.get('Args')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class SetPostScriptsRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        post_install_scripts: List[SetPostScriptsRequestPostInstallScripts] = None,
        region_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.post_install_scripts = post_install_scripts
        self.region_id = region_id

    def validate(self):
        if self.post_install_scripts:
            for k in self.post_install_scripts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        result['PostInstallScripts'] = []
        if self.post_install_scripts is not None:
            for k in self.post_install_scripts:
                result['PostInstallScripts'].append(k.to_map() if k else None)
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        self.post_install_scripts = []
        if m.get('PostInstallScripts') is not None:
            for k in m.get('PostInstallScripts'):
                temp_model = SetPostScriptsRequestPostInstallScripts()
                self.post_install_scripts.append(temp_model.from_map(k))
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SetPostScriptsResponseBody(TeaModel):
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


class SetPostScriptsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetPostScriptsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = SetPostScriptsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetQueueRequestNode(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class SetQueueRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        node: List[SetQueueRequestNode] = None,
        queue_name: str = None,
    ):
        self.cluster_id = cluster_id
        self.node = node
        self.queue_name = queue_name

    def validate(self):
        if self.node:
            for k in self.node:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        result['Node'] = []
        if self.node is not None:
            for k in self.node:
                result['Node'].append(k.to_map() if k else None)
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        self.node = []
        if m.get('Node') is not None:
            for k in m.get('Node'):
                temp_model = SetQueueRequestNode()
                self.node.append(temp_model.from_map(k))
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        return self


class SetQueueResponseBody(TeaModel):
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


class SetQueueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetQueueResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = SetQueueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetSchedulerInfoRequestPbsInfoAclLimit(TeaModel):
    def __init__(
        self,
        acl_users: str = None,
        queue: str = None,
    ):
        self.acl_users = acl_users
        self.queue = queue

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_users is not None:
            result['AclUsers'] = self.acl_users
        if self.queue is not None:
            result['Queue'] = self.queue
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclUsers') is not None:
            self.acl_users = m.get('AclUsers')
        if m.get('Queue') is not None:
            self.queue = m.get('Queue')
        return self


class SetSchedulerInfoRequestPbsInfoResourceLimit(TeaModel):
    def __init__(
        self,
        cpus: int = None,
        max_jobs: int = None,
        mem: str = None,
        nodes: int = None,
        queue: str = None,
        user: str = None,
    ):
        self.cpus = cpus
        self.max_jobs = max_jobs
        self.mem = mem
        self.nodes = nodes
        self.queue = queue
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpus is not None:
            result['Cpus'] = self.cpus
        if self.max_jobs is not None:
            result['MaxJobs'] = self.max_jobs
        if self.mem is not None:
            result['Mem'] = self.mem
        if self.nodes is not None:
            result['Nodes'] = self.nodes
        if self.queue is not None:
            result['Queue'] = self.queue
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpus') is not None:
            self.cpus = m.get('Cpus')
        if m.get('MaxJobs') is not None:
            self.max_jobs = m.get('MaxJobs')
        if m.get('Mem') is not None:
            self.mem = m.get('Mem')
        if m.get('Nodes') is not None:
            self.nodes = m.get('Nodes')
        if m.get('Queue') is not None:
            self.queue = m.get('Queue')
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class SetSchedulerInfoRequestPbsInfo(TeaModel):
    def __init__(
        self,
        acl_limit: List[SetSchedulerInfoRequestPbsInfoAclLimit] = None,
        job_history_duration: int = None,
        resource_limit: List[SetSchedulerInfoRequestPbsInfoResourceLimit] = None,
        sched_interval: int = None,
        sched_max_jobs: int = None,
        sched_max_queued_jobs: int = None,
    ):
        self.acl_limit = acl_limit
        self.job_history_duration = job_history_duration
        self.resource_limit = resource_limit
        self.sched_interval = sched_interval
        self.sched_max_jobs = sched_max_jobs
        self.sched_max_queued_jobs = sched_max_queued_jobs

    def validate(self):
        if self.acl_limit:
            for k in self.acl_limit:
                if k:
                    k.validate()
        if self.resource_limit:
            for k in self.resource_limit:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AclLimit'] = []
        if self.acl_limit is not None:
            for k in self.acl_limit:
                result['AclLimit'].append(k.to_map() if k else None)
        if self.job_history_duration is not None:
            result['JobHistoryDuration'] = self.job_history_duration
        result['ResourceLimit'] = []
        if self.resource_limit is not None:
            for k in self.resource_limit:
                result['ResourceLimit'].append(k.to_map() if k else None)
        if self.sched_interval is not None:
            result['SchedInterval'] = self.sched_interval
        if self.sched_max_jobs is not None:
            result['SchedMaxJobs'] = self.sched_max_jobs
        if self.sched_max_queued_jobs is not None:
            result['SchedMaxQueuedJobs'] = self.sched_max_queued_jobs
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.acl_limit = []
        if m.get('AclLimit') is not None:
            for k in m.get('AclLimit'):
                temp_model = SetSchedulerInfoRequestPbsInfoAclLimit()
                self.acl_limit.append(temp_model.from_map(k))
        if m.get('JobHistoryDuration') is not None:
            self.job_history_duration = m.get('JobHistoryDuration')
        self.resource_limit = []
        if m.get('ResourceLimit') is not None:
            for k in m.get('ResourceLimit'):
                temp_model = SetSchedulerInfoRequestPbsInfoResourceLimit()
                self.resource_limit.append(temp_model.from_map(k))
        if m.get('SchedInterval') is not None:
            self.sched_interval = m.get('SchedInterval')
        if m.get('SchedMaxJobs') is not None:
            self.sched_max_jobs = m.get('SchedMaxJobs')
        if m.get('SchedMaxQueuedJobs') is not None:
            self.sched_max_queued_jobs = m.get('SchedMaxQueuedJobs')
        return self


class SetSchedulerInfoRequestScheduler(TeaModel):
    def __init__(
        self,
        sched_name: str = None,
    ):
        self.sched_name = sched_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sched_name is not None:
            result['SchedName'] = self.sched_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SchedName') is not None:
            self.sched_name = m.get('SchedName')
        return self


class SetSchedulerInfoRequestSlurmInfo(TeaModel):
    def __init__(
        self,
        backfill_interval: int = None,
        sched_interval: int = None,
    ):
        self.backfill_interval = backfill_interval
        self.sched_interval = sched_interval

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backfill_interval is not None:
            result['BackfillInterval'] = self.backfill_interval
        if self.sched_interval is not None:
            result['SchedInterval'] = self.sched_interval
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackfillInterval') is not None:
            self.backfill_interval = m.get('BackfillInterval')
        if m.get('SchedInterval') is not None:
            self.sched_interval = m.get('SchedInterval')
        return self


class SetSchedulerInfoRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        pbs_info: List[SetSchedulerInfoRequestPbsInfo] = None,
        region_id: str = None,
        scheduler: List[SetSchedulerInfoRequestScheduler] = None,
        slurm_info: List[SetSchedulerInfoRequestSlurmInfo] = None,
    ):
        self.cluster_id = cluster_id
        self.pbs_info = pbs_info
        self.region_id = region_id
        self.scheduler = scheduler
        self.slurm_info = slurm_info

    def validate(self):
        if self.pbs_info:
            for k in self.pbs_info:
                if k:
                    k.validate()
        if self.scheduler:
            for k in self.scheduler:
                if k:
                    k.validate()
        if self.slurm_info:
            for k in self.slurm_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        result['PbsInfo'] = []
        if self.pbs_info is not None:
            for k in self.pbs_info:
                result['PbsInfo'].append(k.to_map() if k else None)
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['Scheduler'] = []
        if self.scheduler is not None:
            for k in self.scheduler:
                result['Scheduler'].append(k.to_map() if k else None)
        result['SlurmInfo'] = []
        if self.slurm_info is not None:
            for k in self.slurm_info:
                result['SlurmInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        self.pbs_info = []
        if m.get('PbsInfo') is not None:
            for k in m.get('PbsInfo'):
                temp_model = SetSchedulerInfoRequestPbsInfo()
                self.pbs_info.append(temp_model.from_map(k))
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.scheduler = []
        if m.get('Scheduler') is not None:
            for k in m.get('Scheduler'):
                temp_model = SetSchedulerInfoRequestScheduler()
                self.scheduler.append(temp_model.from_map(k))
        self.slurm_info = []
        if m.get('SlurmInfo') is not None:
            for k in m.get('SlurmInfo'):
                temp_model = SetSchedulerInfoRequestSlurmInfo()
                self.slurm_info.append(temp_model.from_map(k))
        return self


class SetSchedulerInfoResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
    ):
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetSchedulerInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetSchedulerInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = SetSchedulerInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartClusterRequest(TeaModel):
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


class StartClusterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        self.request_id = request_id
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
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class StartClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartClusterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = StartClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartGWSInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class StartGWSInstanceResponseBody(TeaModel):
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


class StartGWSInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartGWSInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = StartGWSInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartNodesRequestInstance(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class StartNodesRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        instance: List[StartNodesRequestInstance] = None,
        role: str = None,
    ):
        self.cluster_id = cluster_id
        self.instance = instance
        self.role = role

    def validate(self):
        if self.instance:
            for k in self.instance:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        result['Instance'] = []
        if self.instance is not None:
            for k in self.instance:
                result['Instance'].append(k.to_map() if k else None)
        if self.role is not None:
            result['Role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        self.instance = []
        if m.get('Instance') is not None:
            for k in m.get('Instance'):
                temp_model = StartNodesRequestInstance()
                self.instance.append(temp_model.from_map(k))
        if m.get('Role') is not None:
            self.role = m.get('Role')
        return self


class StartNodesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        self.request_id = request_id
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
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class StartNodesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartNodesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = StartNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartVisualServiceRequest(TeaModel):
    def __init__(
        self,
        cidr_ip: str = None,
        cluster_id: str = None,
        port: int = None,
    ):
        self.cidr_ip = cidr_ip
        self.cluster_id = cluster_id
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr_ip is not None:
            result['CidrIp'] = self.cidr_ip
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrIp') is not None:
            self.cidr_ip = m.get('CidrIp')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class StartVisualServiceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
    ):
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartVisualServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartVisualServiceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = StartVisualServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopClusterRequest(TeaModel):
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


class StopClusterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        self.request_id = request_id
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
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class StopClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopClusterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = StopClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopGWSInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class StopGWSInstanceResponseBody(TeaModel):
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


class StopGWSInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopGWSInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = StopGWSInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopJobsRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        jobs: str = None,
    ):
        self.cluster_id = cluster_id
        self.jobs = jobs

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.jobs is not None:
            result['Jobs'] = self.jobs
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Jobs') is not None:
            self.jobs = m.get('Jobs')
        return self


class StopJobsResponseBody(TeaModel):
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


class StopJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopJobsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = StopJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopNodesRequestInstance(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class StopNodesRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        instance: List[StopNodesRequestInstance] = None,
        role: str = None,
    ):
        self.cluster_id = cluster_id
        self.instance = instance
        self.role = role

    def validate(self):
        if self.instance:
            for k in self.instance:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        result['Instance'] = []
        if self.instance is not None:
            for k in self.instance:
                result['Instance'].append(k.to_map() if k else None)
        if self.role is not None:
            result['Role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        self.instance = []
        if m.get('Instance') is not None:
            for k in m.get('Instance'):
                temp_model = StopNodesRequestInstance()
                self.instance.append(temp_model.from_map(k))
        if m.get('Role') is not None:
            self.role = m.get('Role')
        return self


class StopNodesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        self.request_id = request_id
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
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class StopNodesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopNodesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = StopNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopVisualServiceRequest(TeaModel):
    def __init__(
        self,
        cidr_ip: str = None,
        cluster_id: str = None,
        port: int = None,
    ):
        self.cidr_ip = cidr_ip
        self.cluster_id = cluster_id
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr_ip is not None:
            result['CidrIp'] = self.cidr_ip
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrIp') is not None:
            self.cidr_ip = m.get('CidrIp')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class StopVisualServiceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
    ):
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopVisualServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopVisualServiceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = StopVisualServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitJobRequest(TeaModel):
    def __init__(
        self,
        array_request: str = None,
        clock_time: str = None,
        cluster_id: str = None,
        command_line: str = None,
        container_id: str = None,
        gpu: int = None,
        input_file_url: str = None,
        job_queue: str = None,
        mem: str = None,
        name: str = None,
        node: int = None,
        package_path: str = None,
        post_cmd_line: str = None,
        priority: int = None,
        re_runable: bool = None,
        runas_user: str = None,
        runas_user_password: str = None,
        stderr_redirect_path: str = None,
        stdout_redirect_path: str = None,
        task: int = None,
        thread: int = None,
        unzip_cmd: str = None,
        variables: str = None,
    ):
        self.array_request = array_request
        self.clock_time = clock_time
        self.cluster_id = cluster_id
        self.command_line = command_line
        self.container_id = container_id
        self.gpu = gpu
        self.input_file_url = input_file_url
        self.job_queue = job_queue
        self.mem = mem
        self.name = name
        self.node = node
        self.package_path = package_path
        self.post_cmd_line = post_cmd_line
        self.priority = priority
        self.re_runable = re_runable
        self.runas_user = runas_user
        self.runas_user_password = runas_user_password
        self.stderr_redirect_path = stderr_redirect_path
        self.stdout_redirect_path = stdout_redirect_path
        self.task = task
        self.thread = thread
        self.unzip_cmd = unzip_cmd
        self.variables = variables

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.array_request is not None:
            result['ArrayRequest'] = self.array_request
        if self.clock_time is not None:
            result['ClockTime'] = self.clock_time
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.command_line is not None:
            result['CommandLine'] = self.command_line
        if self.container_id is not None:
            result['ContainerId'] = self.container_id
        if self.gpu is not None:
            result['Gpu'] = self.gpu
        if self.input_file_url is not None:
            result['InputFileUrl'] = self.input_file_url
        if self.job_queue is not None:
            result['JobQueue'] = self.job_queue
        if self.mem is not None:
            result['Mem'] = self.mem
        if self.name is not None:
            result['Name'] = self.name
        if self.node is not None:
            result['Node'] = self.node
        if self.package_path is not None:
            result['PackagePath'] = self.package_path
        if self.post_cmd_line is not None:
            result['PostCmdLine'] = self.post_cmd_line
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.re_runable is not None:
            result['ReRunable'] = self.re_runable
        if self.runas_user is not None:
            result['RunasUser'] = self.runas_user
        if self.runas_user_password is not None:
            result['RunasUserPassword'] = self.runas_user_password
        if self.stderr_redirect_path is not None:
            result['StderrRedirectPath'] = self.stderr_redirect_path
        if self.stdout_redirect_path is not None:
            result['StdoutRedirectPath'] = self.stdout_redirect_path
        if self.task is not None:
            result['Task'] = self.task
        if self.thread is not None:
            result['Thread'] = self.thread
        if self.unzip_cmd is not None:
            result['UnzipCmd'] = self.unzip_cmd
        if self.variables is not None:
            result['Variables'] = self.variables
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArrayRequest') is not None:
            self.array_request = m.get('ArrayRequest')
        if m.get('ClockTime') is not None:
            self.clock_time = m.get('ClockTime')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CommandLine') is not None:
            self.command_line = m.get('CommandLine')
        if m.get('ContainerId') is not None:
            self.container_id = m.get('ContainerId')
        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')
        if m.get('InputFileUrl') is not None:
            self.input_file_url = m.get('InputFileUrl')
        if m.get('JobQueue') is not None:
            self.job_queue = m.get('JobQueue')
        if m.get('Mem') is not None:
            self.mem = m.get('Mem')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Node') is not None:
            self.node = m.get('Node')
        if m.get('PackagePath') is not None:
            self.package_path = m.get('PackagePath')
        if m.get('PostCmdLine') is not None:
            self.post_cmd_line = m.get('PostCmdLine')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('ReRunable') is not None:
            self.re_runable = m.get('ReRunable')
        if m.get('RunasUser') is not None:
            self.runas_user = m.get('RunasUser')
        if m.get('RunasUserPassword') is not None:
            self.runas_user_password = m.get('RunasUserPassword')
        if m.get('StderrRedirectPath') is not None:
            self.stderr_redirect_path = m.get('StderrRedirectPath')
        if m.get('StdoutRedirectPath') is not None:
            self.stdout_redirect_path = m.get('StdoutRedirectPath')
        if m.get('Task') is not None:
            self.task = m.get('Task')
        if m.get('Thread') is not None:
            self.thread = m.get('Thread')
        if m.get('UnzipCmd') is not None:
            self.unzip_cmd = m.get('UnzipCmd')
        if m.get('Variables') is not None:
            self.variables = m.get('Variables')
        return self


class SubmitJobResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        self.job_id = job_id
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


class SubmitJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = SubmitJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SummaryImagesRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        container_type: str = None,
    ):
        self.cluster_id = cluster_id
        self.container_type = container_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.container_type is not None:
            result['ContainerType'] = self.container_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ContainerType') is not None:
            self.container_type = m.get('ContainerType')
        return self


class SummaryImagesResponseBody(TeaModel):
    def __init__(
        self,
        images_name: str = None,
        request_id: str = None,
    ):
        self.images_name = images_name
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.images_name is not None:
            result['ImagesName'] = self.images_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImagesName') is not None:
            self.images_name = m.get('ImagesName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SummaryImagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SummaryImagesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = SummaryImagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SummaryImagesInfoRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        container_type: str = None,
        image_name: str = None,
    ):
        self.cluster_id = cluster_id
        self.container_type = container_type
        self.image_name = image_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.container_type is not None:
            result['ContainerType'] = self.container_type
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ContainerType') is not None:
            self.container_type = m.get('ContainerType')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        return self


class SummaryImagesInfoResponseBody(TeaModel):
    def __init__(
        self,
        images_info: str = None,
        request_id: str = None,
    ):
        self.images_info = images_info
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.images_info is not None:
            result['ImagesInfo'] = self.images_info
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImagesInfo') is not None:
            self.images_info = m.get('ImagesInfo')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SummaryImagesInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SummaryImagesInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = SummaryImagesInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SyncUsersRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        region_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SyncUsersResponseBody(TeaModel):
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


class SyncUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SyncUsersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = SyncUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
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


class TagResourcesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[TagResourcesRequestTag] = None,
    ):
        self.region_id = region_id
        self.resource_id = resource_id
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
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
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        region_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag_key: List[str] = None,
    ):
        self.all = all
        self.region_id = region_id
        self.resource_id = resource_id
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
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
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class UninstallSoftwareRequest(TeaModel):
    def __init__(
        self,
        application: str = None,
        cluster_id: str = None,
    ):
        self.application = application
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application is not None:
            result['Application'] = self.application
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Application') is not None:
            self.application = m.get('Application')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class UninstallSoftwareResponseBody(TeaModel):
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


class UninstallSoftwareResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UninstallSoftwareResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UninstallSoftwareResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateClusterVolumesRequestAdditionalVolumesRoles(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateClusterVolumesRequestAdditionalVolumes(TeaModel):
    def __init__(
        self,
        job_queue: str = None,
        local_directory: str = None,
        location: str = None,
        remote_directory: str = None,
        roles: List[UpdateClusterVolumesRequestAdditionalVolumesRoles] = None,
        volume_id: str = None,
        volume_mountpoint: str = None,
        volume_protocol: str = None,
        volume_type: str = None,
    ):
        self.job_queue = job_queue
        self.local_directory = local_directory
        self.location = location
        self.remote_directory = remote_directory
        self.roles = roles
        self.volume_id = volume_id
        self.volume_mountpoint = volume_mountpoint
        self.volume_protocol = volume_protocol
        self.volume_type = volume_type

    def validate(self):
        if self.roles:
            for k in self.roles:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_queue is not None:
            result['JobQueue'] = self.job_queue
        if self.local_directory is not None:
            result['LocalDirectory'] = self.local_directory
        if self.location is not None:
            result['Location'] = self.location
        if self.remote_directory is not None:
            result['RemoteDirectory'] = self.remote_directory
        result['Roles'] = []
        if self.roles is not None:
            for k in self.roles:
                result['Roles'].append(k.to_map() if k else None)
        if self.volume_id is not None:
            result['VolumeId'] = self.volume_id
        if self.volume_mountpoint is not None:
            result['VolumeMountpoint'] = self.volume_mountpoint
        if self.volume_protocol is not None:
            result['VolumeProtocol'] = self.volume_protocol
        if self.volume_type is not None:
            result['VolumeType'] = self.volume_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobQueue') is not None:
            self.job_queue = m.get('JobQueue')
        if m.get('LocalDirectory') is not None:
            self.local_directory = m.get('LocalDirectory')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('RemoteDirectory') is not None:
            self.remote_directory = m.get('RemoteDirectory')
        self.roles = []
        if m.get('Roles') is not None:
            for k in m.get('Roles'):
                temp_model = UpdateClusterVolumesRequestAdditionalVolumesRoles()
                self.roles.append(temp_model.from_map(k))
        if m.get('VolumeId') is not None:
            self.volume_id = m.get('VolumeId')
        if m.get('VolumeMountpoint') is not None:
            self.volume_mountpoint = m.get('VolumeMountpoint')
        if m.get('VolumeProtocol') is not None:
            self.volume_protocol = m.get('VolumeProtocol')
        if m.get('VolumeType') is not None:
            self.volume_type = m.get('VolumeType')
        return self


class UpdateClusterVolumesRequest(TeaModel):
    def __init__(
        self,
        additional_volumes: List[UpdateClusterVolumesRequestAdditionalVolumes] = None,
        cluster_id: str = None,
    ):
        self.additional_volumes = additional_volumes
        self.cluster_id = cluster_id

    def validate(self):
        if self.additional_volumes:
            for k in self.additional_volumes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AdditionalVolumes'] = []
        if self.additional_volumes is not None:
            for k in self.additional_volumes:
                result['AdditionalVolumes'].append(k.to_map() if k else None)
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.additional_volumes = []
        if m.get('AdditionalVolumes') is not None:
            for k in m.get('AdditionalVolumes'):
                temp_model = UpdateClusterVolumesRequestAdditionalVolumes()
                self.additional_volumes.append(temp_model.from_map(k))
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class UpdateClusterVolumesResponseBody(TeaModel):
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


class UpdateClusterVolumesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateClusterVolumesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UpdateClusterVolumesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateQueueConfigRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        compute_instance_type: str = None,
        queue_name: str = None,
        resource_group_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.compute_instance_type = compute_instance_type
        self.queue_name = queue_name
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.compute_instance_type is not None:
            result['ComputeInstanceType'] = self.compute_instance_type
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ComputeInstanceType') is not None:
            self.compute_instance_type = m.get('ComputeInstanceType')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class UpdateQueueConfigResponseBody(TeaModel):
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


class UpdateQueueConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateQueueConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UpdateQueueConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeClientRequest(TeaModel):
    def __init__(
        self,
        client_version: str = None,
        cluster_id: str = None,
    ):
        self.client_version = client_version
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class UpgradeClientResponseBody(TeaModel):
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


class UpgradeClientResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpgradeClientResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UpgradeClientResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


