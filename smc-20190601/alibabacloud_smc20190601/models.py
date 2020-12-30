# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class CreateReplicationJobRequestDataDiskPart(TeaModel):
    def __init__(
        self,
        size_bytes: int = None,
        block: bool = None,
        device: str = None,
    ):
        self.size_bytes = size_bytes
        self.block = block
        self.device = device

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.size_bytes is not None:
            result['SizeBytes'] = self.size_bytes
        if self.block is not None:
            result['Block'] = self.block
        if self.device is not None:
            result['Device'] = self.device
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SizeBytes') is not None:
            self.size_bytes = m.get('SizeBytes')
        if m.get('Block') is not None:
            self.block = m.get('Block')
        if m.get('Device') is not None:
            self.device = m.get('Device')
        return self


class CreateReplicationJobRequestDataDisk(TeaModel):
    def __init__(
        self,
        index: int = None,
        part: List[CreateReplicationJobRequestDataDiskPart] = None,
        size: int = None,
    ):
        self.index = index
        self.part = part
        self.size = size

    def validate(self):
        if self.part:
            for k in self.part:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        result['Part'] = []
        if self.part is not None:
            for k in self.part:
                result['Part'].append(k.to_map() if k else None)
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        self.part = []
        if m.get('Part') is not None:
            for k in m.get('Part'):
                temp_model = CreateReplicationJobRequestDataDiskPart()
                self.part.append(temp_model.from_map(k))
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class CreateReplicationJobRequestTag(TeaModel):
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


class CreateReplicationJobRequestSystemDiskPart(TeaModel):
    def __init__(
        self,
        size_bytes: int = None,
        block: bool = None,
        device: str = None,
    ):
        self.size_bytes = size_bytes
        self.block = block
        self.device = device

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.size_bytes is not None:
            result['SizeBytes'] = self.size_bytes
        if self.block is not None:
            result['Block'] = self.block
        if self.device is not None:
            result['Device'] = self.device
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SizeBytes') is not None:
            self.size_bytes = m.get('SizeBytes')
        if m.get('Block') is not None:
            self.block = m.get('Block')
        if m.get('Device') is not None:
            self.device = m.get('Device')
        return self


class CreateReplicationJobRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        region_id: str = None,
        client_token: str = None,
        name: str = None,
        description: str = None,
        source_id: str = None,
        target_type: str = None,
        scheduled_start_time: str = None,
        valid_time: str = None,
        image_name: str = None,
        instance_id: str = None,
        system_disk_size: int = None,
        vpc_id: str = None,
        v_switch_id: str = None,
        replication_parameters: str = None,
        net_mode: int = None,
        run_once: bool = None,
        frequency: int = None,
        max_number_of_image_to_keep: int = None,
        instance_type: str = None,
        launch_template_id: str = None,
        launch_template_version: str = None,
        instance_ram_role: str = None,
        container_namespace: str = None,
        container_repository: str = None,
        container_tag: str = None,
        license_type: str = None,
        data_disk: List[CreateReplicationJobRequestDataDisk] = None,
        tag: List[CreateReplicationJobRequestTag] = None,
        system_disk_part: List[CreateReplicationJobRequestSystemDiskPart] = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.region_id = region_id
        self.client_token = client_token
        self.name = name
        self.description = description
        self.source_id = source_id
        self.target_type = target_type
        self.scheduled_start_time = scheduled_start_time
        self.valid_time = valid_time
        self.image_name = image_name
        self.instance_id = instance_id
        self.system_disk_size = system_disk_size
        self.vpc_id = vpc_id
        self.v_switch_id = v_switch_id
        self.replication_parameters = replication_parameters
        self.net_mode = net_mode
        self.run_once = run_once
        self.frequency = frequency
        self.max_number_of_image_to_keep = max_number_of_image_to_keep
        self.instance_type = instance_type
        self.launch_template_id = launch_template_id
        self.launch_template_version = launch_template_version
        self.instance_ram_role = instance_ram_role
        self.container_namespace = container_namespace
        self.container_repository = container_repository
        self.container_tag = container_tag
        self.license_type = license_type
        self.data_disk = data_disk
        self.tag = tag
        self.system_disk_part = system_disk_part

    def validate(self):
        if self.data_disk:
            for k in self.data_disk:
                if k:
                    k.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()
        if self.system_disk_part:
            for k in self.system_disk_part:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.scheduled_start_time is not None:
            result['ScheduledStartTime'] = self.scheduled_start_time
        if self.valid_time is not None:
            result['ValidTime'] = self.valid_time
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.replication_parameters is not None:
            result['ReplicationParameters'] = self.replication_parameters
        if self.net_mode is not None:
            result['NetMode'] = self.net_mode
        if self.run_once is not None:
            result['RunOnce'] = self.run_once
        if self.frequency is not None:
            result['Frequency'] = self.frequency
        if self.max_number_of_image_to_keep is not None:
            result['MaxNumberOfImageToKeep'] = self.max_number_of_image_to_keep
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.launch_template_id is not None:
            result['LaunchTemplateId'] = self.launch_template_id
        if self.launch_template_version is not None:
            result['LaunchTemplateVersion'] = self.launch_template_version
        if self.instance_ram_role is not None:
            result['InstanceRamRole'] = self.instance_ram_role
        if self.container_namespace is not None:
            result['ContainerNamespace'] = self.container_namespace
        if self.container_repository is not None:
            result['ContainerRepository'] = self.container_repository
        if self.container_tag is not None:
            result['ContainerTag'] = self.container_tag
        if self.license_type is not None:
            result['LicenseType'] = self.license_type
        result['DataDisk'] = []
        if self.data_disk is not None:
            for k in self.data_disk:
                result['DataDisk'].append(k.to_map() if k else None)
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        result['SystemDiskPart'] = []
        if self.system_disk_part is not None:
            for k in self.system_disk_part:
                result['SystemDiskPart'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('ScheduledStartTime') is not None:
            self.scheduled_start_time = m.get('ScheduledStartTime')
        if m.get('ValidTime') is not None:
            self.valid_time = m.get('ValidTime')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ReplicationParameters') is not None:
            self.replication_parameters = m.get('ReplicationParameters')
        if m.get('NetMode') is not None:
            self.net_mode = m.get('NetMode')
        if m.get('RunOnce') is not None:
            self.run_once = m.get('RunOnce')
        if m.get('Frequency') is not None:
            self.frequency = m.get('Frequency')
        if m.get('MaxNumberOfImageToKeep') is not None:
            self.max_number_of_image_to_keep = m.get('MaxNumberOfImageToKeep')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('LaunchTemplateId') is not None:
            self.launch_template_id = m.get('LaunchTemplateId')
        if m.get('LaunchTemplateVersion') is not None:
            self.launch_template_version = m.get('LaunchTemplateVersion')
        if m.get('InstanceRamRole') is not None:
            self.instance_ram_role = m.get('InstanceRamRole')
        if m.get('ContainerNamespace') is not None:
            self.container_namespace = m.get('ContainerNamespace')
        if m.get('ContainerRepository') is not None:
            self.container_repository = m.get('ContainerRepository')
        if m.get('ContainerTag') is not None:
            self.container_tag = m.get('ContainerTag')
        if m.get('LicenseType') is not None:
            self.license_type = m.get('LicenseType')
        self.data_disk = []
        if m.get('DataDisk') is not None:
            for k in m.get('DataDisk'):
                temp_model = CreateReplicationJobRequestDataDisk()
                self.data_disk.append(temp_model.from_map(k))
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateReplicationJobRequestTag()
                self.tag.append(temp_model.from_map(k))
        self.system_disk_part = []
        if m.get('SystemDiskPart') is not None:
            for k in m.get('SystemDiskPart'):
                temp_model = CreateReplicationJobRequestSystemDiskPart()
                self.system_disk_part.append(temp_model.from_map(k))
        return self


class CreateReplicationJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        job_id: str = None,
    ):
        self.request_id = request_id
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class CreateReplicationJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateReplicationJobResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateReplicationJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CutOverReplicationJobRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        job_id: str = None,
        sync_data: bool = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.job_id = job_id
        self.sync_data = sync_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.sync_data is not None:
            result['SyncData'] = self.sync_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('SyncData') is not None:
            self.sync_data = m.get('SyncData')
        return self


class CutOverReplicationJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CutOverReplicationJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CutOverReplicationJobResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CutOverReplicationJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteReplicationJobRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        job_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class DeleteReplicationJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteReplicationJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteReplicationJobResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteReplicationJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSourceServerRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        source_id: str = None,
        force: bool = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.source_id = source_id
        self.force = force

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.force is not None:
            result['Force'] = self.force
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('Force') is not None:
            self.force = m.get('Force')
        return self


class DeleteSourceServerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteSourceServerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteSourceServerResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteSourceServerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeReplicationJobsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        name: str = None,
        region_id: str = None,
        status: str = None,
        business_status: str = None,
        page_number: int = None,
        page_size: int = None,
        source_id: List[str] = None,
        job_id: List[str] = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.name = name
        self.region_id = region_id
        self.status = status
        self.business_status = business_status
        self.page_number = page_number
        self.page_size = page_size
        self.source_id = source_id
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.business_status is not None:
            result['BusinessStatus'] = self.business_status
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('BusinessStatus') is not None:
            self.business_status = m.get('BusinessStatus')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDataDisksDataDiskPartsPart(TeaModel):
    def __init__(
        self,
        size_bytes: int = None,
        block: bool = None,
        device: str = None,
    ):
        self.size_bytes = size_bytes
        self.block = block
        self.device = device

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.size_bytes is not None:
            result['SizeBytes'] = self.size_bytes
        if self.block is not None:
            result['Block'] = self.block
        if self.device is not None:
            result['Device'] = self.device
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SizeBytes') is not None:
            self.size_bytes = m.get('SizeBytes')
        if m.get('Block') is not None:
            self.block = m.get('Block')
        if m.get('Device') is not None:
            self.device = m.get('Device')
        return self


class DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDataDisksDataDiskParts(TeaModel):
    def __init__(
        self,
        part: List[DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDataDisksDataDiskPartsPart] = None,
    ):
        self.part = part

    def validate(self):
        if self.part:
            for k in self.part:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Part'] = []
        if self.part is not None:
            for k in self.part:
                result['Part'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.part = []
        if m.get('Part') is not None:
            for k in m.get('Part'):
                temp_model = DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDataDisksDataDiskPartsPart()
                self.part.append(temp_model.from_map(k))
        return self


class DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDataDisksDataDisk(TeaModel):
    def __init__(
        self,
        index: int = None,
        size: int = None,
        parts: DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDataDisksDataDiskParts = None,
    ):
        self.index = index
        self.size = size
        self.parts = parts

    def validate(self):
        if self.parts:
            self.parts.validate()

    def to_map(self):
        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.size is not None:
            result['Size'] = self.size
        if self.parts is not None:
            result['Parts'] = self.parts.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Parts') is not None:
            temp_model = DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDataDisksDataDiskParts()
            self.parts = temp_model.from_map(m['Parts'])
        return self


class DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDataDisks(TeaModel):
    def __init__(
        self,
        data_disk: List[DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDataDisksDataDisk] = None,
    ):
        self.data_disk = data_disk

    def validate(self):
        if self.data_disk:
            for k in self.data_disk:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['DataDisk'] = []
        if self.data_disk is not None:
            for k in self.data_disk:
                result['DataDisk'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_disk = []
        if m.get('DataDisk') is not None:
            for k in m.get('DataDisk'):
                temp_model = DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDataDisksDataDisk()
                self.data_disk.append(temp_model.from_map(k))
        return self


class DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobSystemDiskPartsSystemDiskPart(TeaModel):
    def __init__(
        self,
        size_bytes: int = None,
        block: bool = None,
        device: str = None,
    ):
        self.size_bytes = size_bytes
        self.block = block
        self.device = device

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.size_bytes is not None:
            result['SizeBytes'] = self.size_bytes
        if self.block is not None:
            result['Block'] = self.block
        if self.device is not None:
            result['Device'] = self.device
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SizeBytes') is not None:
            self.size_bytes = m.get('SizeBytes')
        if m.get('Block') is not None:
            self.block = m.get('Block')
        if m.get('Device') is not None:
            self.device = m.get('Device')
        return self


class DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobSystemDiskParts(TeaModel):
    def __init__(
        self,
        system_disk_part: List[DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobSystemDiskPartsSystemDiskPart] = None,
    ):
        self.system_disk_part = system_disk_part

    def validate(self):
        if self.system_disk_part:
            for k in self.system_disk_part:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['SystemDiskPart'] = []
        if self.system_disk_part is not None:
            for k in self.system_disk_part:
                result['SystemDiskPart'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.system_disk_part = []
        if m.get('SystemDiskPart') is not None:
            for k in m.get('SystemDiskPart'):
                temp_model = DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobSystemDiskPartsSystemDiskPart()
                self.system_disk_part.append(temp_model.from_map(k))
        return self


class DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobReplicationJobRunsReplicationJobRun(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        type: str = None,
        start_time: str = None,
        image_id: str = None,
    ):
        self.end_time = end_time
        self.type = type
        self.start_time = start_time
        self.image_id = image_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.type is not None:
            result['Type'] = self.type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        return self


class DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobReplicationJobRuns(TeaModel):
    def __init__(
        self,
        replication_job_run: List[DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobReplicationJobRunsReplicationJobRun] = None,
    ):
        self.replication_job_run = replication_job_run

    def validate(self):
        if self.replication_job_run:
            for k in self.replication_job_run:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ReplicationJobRun'] = []
        if self.replication_job_run is not None:
            for k in self.replication_job_run:
                result['ReplicationJobRun'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.replication_job_run = []
        if m.get('ReplicationJobRun') is not None:
            for k in m.get('ReplicationJobRun'):
                temp_model = DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobReplicationJobRunsReplicationJobRun()
                self.replication_job_run.append(temp_model.from_map(k))
        return self


class DescribeReplicationJobsResponseBodyReplicationJobsReplicationJob(TeaModel):
    def __init__(
        self,
        frequency: int = None,
        vpc_id: str = None,
        creation_time: str = None,
        status: str = None,
        scheduled_start_time: str = None,
        max_number_of_image_to_keep: int = None,
        container_namespace: str = None,
        data_disks: DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDataDisks = None,
        status_info: str = None,
        instance_ram_role: str = None,
        system_disk_size: int = None,
        description: str = None,
        replication_parameters: str = None,
        error_code: str = None,
        valid_time: str = None,
        net_mode: int = None,
        container_tag: str = None,
        license_type: str = None,
        name: str = None,
        image_id: str = None,
        progress: float = None,
        run_once: bool = None,
        launch_template_id: str = None,
        container_repository: str = None,
        instance_id: str = None,
        system_disk_parts: DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobSystemDiskParts = None,
        instance_type: str = None,
        source_id: str = None,
        launch_template_version: str = None,
        region_id: str = None,
        transition_instance_id: str = None,
        end_time: str = None,
        start_time: str = None,
        v_switch_id: str = None,
        job_id: str = None,
        image_name: str = None,
        business_status: str = None,
        replication_job_runs: DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobReplicationJobRuns = None,
        target_type: str = None,
    ):
        self.frequency = frequency
        self.vpc_id = vpc_id
        self.creation_time = creation_time
        self.status = status
        self.scheduled_start_time = scheduled_start_time
        self.max_number_of_image_to_keep = max_number_of_image_to_keep
        self.container_namespace = container_namespace
        self.data_disks = data_disks
        self.status_info = status_info
        self.instance_ram_role = instance_ram_role
        self.system_disk_size = system_disk_size
        self.description = description
        self.replication_parameters = replication_parameters
        self.error_code = error_code
        self.valid_time = valid_time
        self.net_mode = net_mode
        self.container_tag = container_tag
        self.license_type = license_type
        self.name = name
        self.image_id = image_id
        self.progress = progress
        self.run_once = run_once
        self.launch_template_id = launch_template_id
        self.container_repository = container_repository
        self.instance_id = instance_id
        self.system_disk_parts = system_disk_parts
        self.instance_type = instance_type
        self.source_id = source_id
        self.launch_template_version = launch_template_version
        self.region_id = region_id
        self.transition_instance_id = transition_instance_id
        self.end_time = end_time
        self.start_time = start_time
        self.v_switch_id = v_switch_id
        self.job_id = job_id
        self.image_name = image_name
        self.business_status = business_status
        self.replication_job_runs = replication_job_runs
        self.target_type = target_type

    def validate(self):
        if self.data_disks:
            self.data_disks.validate()
        if self.system_disk_parts:
            self.system_disk_parts.validate()
        if self.replication_job_runs:
            self.replication_job_runs.validate()

    def to_map(self):
        result = dict()
        if self.frequency is not None:
            result['Frequency'] = self.frequency
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.status is not None:
            result['Status'] = self.status
        if self.scheduled_start_time is not None:
            result['ScheduledStartTime'] = self.scheduled_start_time
        if self.max_number_of_image_to_keep is not None:
            result['MaxNumberOfImageToKeep'] = self.max_number_of_image_to_keep
        if self.container_namespace is not None:
            result['ContainerNamespace'] = self.container_namespace
        if self.data_disks is not None:
            result['DataDisks'] = self.data_disks.to_map()
        if self.status_info is not None:
            result['StatusInfo'] = self.status_info
        if self.instance_ram_role is not None:
            result['InstanceRamRole'] = self.instance_ram_role
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        if self.description is not None:
            result['Description'] = self.description
        if self.replication_parameters is not None:
            result['ReplicationParameters'] = self.replication_parameters
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.valid_time is not None:
            result['ValidTime'] = self.valid_time
        if self.net_mode is not None:
            result['NetMode'] = self.net_mode
        if self.container_tag is not None:
            result['ContainerTag'] = self.container_tag
        if self.license_type is not None:
            result['LicenseType'] = self.license_type
        if self.name is not None:
            result['Name'] = self.name
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.run_once is not None:
            result['RunOnce'] = self.run_once
        if self.launch_template_id is not None:
            result['LaunchTemplateId'] = self.launch_template_id
        if self.container_repository is not None:
            result['ContainerRepository'] = self.container_repository
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.system_disk_parts is not None:
            result['SystemDiskParts'] = self.system_disk_parts.to_map()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.launch_template_version is not None:
            result['LaunchTemplateVersion'] = self.launch_template_version
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.transition_instance_id is not None:
            result['TransitionInstanceId'] = self.transition_instance_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.business_status is not None:
            result['BusinessStatus'] = self.business_status
        if self.replication_job_runs is not None:
            result['ReplicationJobRuns'] = self.replication_job_runs.to_map()
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Frequency') is not None:
            self.frequency = m.get('Frequency')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ScheduledStartTime') is not None:
            self.scheduled_start_time = m.get('ScheduledStartTime')
        if m.get('MaxNumberOfImageToKeep') is not None:
            self.max_number_of_image_to_keep = m.get('MaxNumberOfImageToKeep')
        if m.get('ContainerNamespace') is not None:
            self.container_namespace = m.get('ContainerNamespace')
        if m.get('DataDisks') is not None:
            temp_model = DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDataDisks()
            self.data_disks = temp_model.from_map(m['DataDisks'])
        if m.get('StatusInfo') is not None:
            self.status_info = m.get('StatusInfo')
        if m.get('InstanceRamRole') is not None:
            self.instance_ram_role = m.get('InstanceRamRole')
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ReplicationParameters') is not None:
            self.replication_parameters = m.get('ReplicationParameters')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ValidTime') is not None:
            self.valid_time = m.get('ValidTime')
        if m.get('NetMode') is not None:
            self.net_mode = m.get('NetMode')
        if m.get('ContainerTag') is not None:
            self.container_tag = m.get('ContainerTag')
        if m.get('LicenseType') is not None:
            self.license_type = m.get('LicenseType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RunOnce') is not None:
            self.run_once = m.get('RunOnce')
        if m.get('LaunchTemplateId') is not None:
            self.launch_template_id = m.get('LaunchTemplateId')
        if m.get('ContainerRepository') is not None:
            self.container_repository = m.get('ContainerRepository')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SystemDiskParts') is not None:
            temp_model = DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobSystemDiskParts()
            self.system_disk_parts = temp_model.from_map(m['SystemDiskParts'])
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('LaunchTemplateVersion') is not None:
            self.launch_template_version = m.get('LaunchTemplateVersion')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TransitionInstanceId') is not None:
            self.transition_instance_id = m.get('TransitionInstanceId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('BusinessStatus') is not None:
            self.business_status = m.get('BusinessStatus')
        if m.get('ReplicationJobRuns') is not None:
            temp_model = DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobReplicationJobRuns()
            self.replication_job_runs = temp_model.from_map(m['ReplicationJobRuns'])
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class DescribeReplicationJobsResponseBodyReplicationJobs(TeaModel):
    def __init__(
        self,
        replication_job: List[DescribeReplicationJobsResponseBodyReplicationJobsReplicationJob] = None,
    ):
        self.replication_job = replication_job

    def validate(self):
        if self.replication_job:
            for k in self.replication_job:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ReplicationJob'] = []
        if self.replication_job is not None:
            for k in self.replication_job:
                result['ReplicationJob'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.replication_job = []
        if m.get('ReplicationJob') is not None:
            for k in m.get('ReplicationJob'):
                temp_model = DescribeReplicationJobsResponseBodyReplicationJobsReplicationJob()
                self.replication_job.append(temp_model.from_map(k))
        return self


class DescribeReplicationJobsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        replication_jobs: DescribeReplicationJobsResponseBodyReplicationJobs = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
    ):
        self.total_count = total_count
        self.replication_jobs = replication_jobs
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number

    def validate(self):
        if self.replication_jobs:
            self.replication_jobs.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.replication_jobs is not None:
            result['ReplicationJobs'] = self.replication_jobs.to_map()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('ReplicationJobs') is not None:
            temp_model = DescribeReplicationJobsResponseBodyReplicationJobs()
            self.replication_jobs = temp_model.from_map(m['ReplicationJobs'])
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DescribeReplicationJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeReplicationJobsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeReplicationJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSourceServersRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        job_id: str = None,
        state: str = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        source_id: List[str] = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.job_id = job_id
        self.state = state
        self.name = name
        self.page_number = page_number
        self.page_size = page_size
        self.source_id = source_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.state is not None:
            result['State'] = self.state
        if self.name is not None:
            result['Name'] = self.name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        return self


class DescribeSourceServersResponseBodySourceServersSourceServerDataDisksDataDiskPartsPart(TeaModel):
    def __init__(
        self,
        can_block: bool = None,
        size_bytes: int = None,
        need: bool = None,
        device: str = None,
        path: str = None,
    ):
        self.can_block = can_block
        self.size_bytes = size_bytes
        self.need = need
        self.device = device
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.can_block is not None:
            result['CanBlock'] = self.can_block
        if self.size_bytes is not None:
            result['SizeBytes'] = self.size_bytes
        if self.need is not None:
            result['Need'] = self.need
        if self.device is not None:
            result['Device'] = self.device
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanBlock') is not None:
            self.can_block = m.get('CanBlock')
        if m.get('SizeBytes') is not None:
            self.size_bytes = m.get('SizeBytes')
        if m.get('Need') is not None:
            self.need = m.get('Need')
        if m.get('Device') is not None:
            self.device = m.get('Device')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class DescribeSourceServersResponseBodySourceServersSourceServerDataDisksDataDiskParts(TeaModel):
    def __init__(
        self,
        part: List[DescribeSourceServersResponseBodySourceServersSourceServerDataDisksDataDiskPartsPart] = None,
    ):
        self.part = part

    def validate(self):
        if self.part:
            for k in self.part:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Part'] = []
        if self.part is not None:
            for k in self.part:
                result['Part'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.part = []
        if m.get('Part') is not None:
            for k in m.get('Part'):
                temp_model = DescribeSourceServersResponseBodySourceServersSourceServerDataDisksDataDiskPartsPart()
                self.part.append(temp_model.from_map(k))
        return self


class DescribeSourceServersResponseBodySourceServersSourceServerDataDisksDataDisk(TeaModel):
    def __init__(
        self,
        index: int = None,
        size: int = None,
        parts: DescribeSourceServersResponseBodySourceServersSourceServerDataDisksDataDiskParts = None,
        path: str = None,
    ):
        self.index = index
        self.size = size
        self.parts = parts
        self.path = path

    def validate(self):
        if self.parts:
            self.parts.validate()

    def to_map(self):
        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.size is not None:
            result['Size'] = self.size
        if self.parts is not None:
            result['Parts'] = self.parts.to_map()
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Parts') is not None:
            temp_model = DescribeSourceServersResponseBodySourceServersSourceServerDataDisksDataDiskParts()
            self.parts = temp_model.from_map(m['Parts'])
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class DescribeSourceServersResponseBodySourceServersSourceServerDataDisks(TeaModel):
    def __init__(
        self,
        data_disk: List[DescribeSourceServersResponseBodySourceServersSourceServerDataDisksDataDisk] = None,
    ):
        self.data_disk = data_disk

    def validate(self):
        if self.data_disk:
            for k in self.data_disk:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['DataDisk'] = []
        if self.data_disk is not None:
            for k in self.data_disk:
                result['DataDisk'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_disk = []
        if m.get('DataDisk') is not None:
            for k in m.get('DataDisk'):
                temp_model = DescribeSourceServersResponseBodySourceServersSourceServerDataDisksDataDisk()
                self.data_disk.append(temp_model.from_map(k))
        return self


class DescribeSourceServersResponseBodySourceServersSourceServerSystemDiskPartsSystemDiskPart(TeaModel):
    def __init__(
        self,
        can_block: bool = None,
        size_bytes: int = None,
        need: bool = None,
        device: str = None,
        path: str = None,
    ):
        self.can_block = can_block
        self.size_bytes = size_bytes
        self.need = need
        self.device = device
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.can_block is not None:
            result['CanBlock'] = self.can_block
        if self.size_bytes is not None:
            result['SizeBytes'] = self.size_bytes
        if self.need is not None:
            result['Need'] = self.need
        if self.device is not None:
            result['Device'] = self.device
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanBlock') is not None:
            self.can_block = m.get('CanBlock')
        if m.get('SizeBytes') is not None:
            self.size_bytes = m.get('SizeBytes')
        if m.get('Need') is not None:
            self.need = m.get('Need')
        if m.get('Device') is not None:
            self.device = m.get('Device')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class DescribeSourceServersResponseBodySourceServersSourceServerSystemDiskParts(TeaModel):
    def __init__(
        self,
        system_disk_part: List[DescribeSourceServersResponseBodySourceServersSourceServerSystemDiskPartsSystemDiskPart] = None,
    ):
        self.system_disk_part = system_disk_part

    def validate(self):
        if self.system_disk_part:
            for k in self.system_disk_part:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['SystemDiskPart'] = []
        if self.system_disk_part is not None:
            for k in self.system_disk_part:
                result['SystemDiskPart'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.system_disk_part = []
        if m.get('SystemDiskPart') is not None:
            for k in m.get('SystemDiskPart'):
                temp_model = DescribeSourceServersResponseBodySourceServersSourceServerSystemDiskPartsSystemDiskPart()
                self.system_disk_part.append(temp_model.from_map(k))
        return self


class DescribeSourceServersResponseBodySourceServersSourceServer(TeaModel):
    def __init__(
        self,
        creation_time: str = None,
        heartbeat_rate: int = None,
        state: str = None,
        data_disks: DescribeSourceServersResponseBodySourceServersSourceServerDataDisks = None,
        system_disk_parts: DescribeSourceServersResponseBodySourceServersSourceServerSystemDiskParts = None,
        kernel_level: int = None,
        source_id: str = None,
        agent_version: str = None,
        status_info: str = None,
        system_disk_size: int = None,
        description: str = None,
        error_code: str = None,
        job_id: str = None,
        platform: str = None,
        replication_driver: str = None,
        name: str = None,
        system_info: str = None,
        architecture: str = None,
    ):
        self.creation_time = creation_time
        self.heartbeat_rate = heartbeat_rate
        self.state = state
        self.data_disks = data_disks
        self.system_disk_parts = system_disk_parts
        self.kernel_level = kernel_level
        self.source_id = source_id
        self.agent_version = agent_version
        self.status_info = status_info
        self.system_disk_size = system_disk_size
        self.description = description
        self.error_code = error_code
        self.job_id = job_id
        self.platform = platform
        self.replication_driver = replication_driver
        self.name = name
        self.system_info = system_info
        self.architecture = architecture

    def validate(self):
        if self.data_disks:
            self.data_disks.validate()
        if self.system_disk_parts:
            self.system_disk_parts.validate()

    def to_map(self):
        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.heartbeat_rate is not None:
            result['HeartbeatRate'] = self.heartbeat_rate
        if self.state is not None:
            result['State'] = self.state
        if self.data_disks is not None:
            result['DataDisks'] = self.data_disks.to_map()
        if self.system_disk_parts is not None:
            result['SystemDiskParts'] = self.system_disk_parts.to_map()
        if self.kernel_level is not None:
            result['KernelLevel'] = self.kernel_level
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.agent_version is not None:
            result['AgentVersion'] = self.agent_version
        if self.status_info is not None:
            result['StatusInfo'] = self.status_info
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        if self.description is not None:
            result['Description'] = self.description
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.replication_driver is not None:
            result['ReplicationDriver'] = self.replication_driver
        if self.name is not None:
            result['Name'] = self.name
        if self.system_info is not None:
            result['SystemInfo'] = self.system_info
        if self.architecture is not None:
            result['Architecture'] = self.architecture
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('HeartbeatRate') is not None:
            self.heartbeat_rate = m.get('HeartbeatRate')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('DataDisks') is not None:
            temp_model = DescribeSourceServersResponseBodySourceServersSourceServerDataDisks()
            self.data_disks = temp_model.from_map(m['DataDisks'])
        if m.get('SystemDiskParts') is not None:
            temp_model = DescribeSourceServersResponseBodySourceServersSourceServerSystemDiskParts()
            self.system_disk_parts = temp_model.from_map(m['SystemDiskParts'])
        if m.get('KernelLevel') is not None:
            self.kernel_level = m.get('KernelLevel')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('AgentVersion') is not None:
            self.agent_version = m.get('AgentVersion')
        if m.get('StatusInfo') is not None:
            self.status_info = m.get('StatusInfo')
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('ReplicationDriver') is not None:
            self.replication_driver = m.get('ReplicationDriver')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SystemInfo') is not None:
            self.system_info = m.get('SystemInfo')
        if m.get('Architecture') is not None:
            self.architecture = m.get('Architecture')
        return self


class DescribeSourceServersResponseBodySourceServers(TeaModel):
    def __init__(
        self,
        source_server: List[DescribeSourceServersResponseBodySourceServersSourceServer] = None,
    ):
        self.source_server = source_server

    def validate(self):
        if self.source_server:
            for k in self.source_server:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['SourceServer'] = []
        if self.source_server is not None:
            for k in self.source_server:
                result['SourceServer'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.source_server = []
        if m.get('SourceServer') is not None:
            for k in m.get('SourceServer'):
                temp_model = DescribeSourceServersResponseBodySourceServersSourceServer()
                self.source_server.append(temp_model.from_map(k))
        return self


class DescribeSourceServersResponseBody(TeaModel):
    def __init__(
        self,
        source_servers: DescribeSourceServersResponseBodySourceServers = None,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
    ):
        self.source_servers = source_servers
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number

    def validate(self):
        if self.source_servers:
            self.source_servers.validate()

    def to_map(self):
        result = dict()
        if self.source_servers is not None:
            result['SourceServers'] = self.source_servers.to_map()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceServers') is not None:
            temp_model = DescribeSourceServersResponseBodySourceServers()
            self.source_servers = temp_model.from_map(m['SourceServers'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DescribeSourceServersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSourceServersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSourceServersResponseBody()
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
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_type: str = None,
        next_token: str = None,
        resource_id: List[str] = None,
        tag: List[ListTagResourcesRequestTag] = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_type = resource_type
        self.next_token = next_token
        self.resource_id = resource_id
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResourcesTagResource(TeaModel):
    def __init__(
        self,
        resource_type: str = None,
        tag_value: str = None,
        resource_id: str = None,
        tag_key: str = None,
    ):
        self.resource_type = resource_type
        self.tag_value = tag_value
        self.resource_id = resource_id
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
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
        body: ListTagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyReplicationJobAttributeRequestSystemDiskPart(TeaModel):
    def __init__(
        self,
        size_bytes: int = None,
        block: bool = None,
        device: str = None,
    ):
        self.size_bytes = size_bytes
        self.block = block
        self.device = device

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.size_bytes is not None:
            result['SizeBytes'] = self.size_bytes
        if self.block is not None:
            result['Block'] = self.block
        if self.device is not None:
            result['Device'] = self.device
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SizeBytes') is not None:
            self.size_bytes = m.get('SizeBytes')
        if m.get('Block') is not None:
            self.block = m.get('Block')
        if m.get('Device') is not None:
            self.device = m.get('Device')
        return self


class ModifyReplicationJobAttributeRequestDataDiskPart(TeaModel):
    def __init__(
        self,
        size_bytes: int = None,
        block: bool = None,
        device: str = None,
    ):
        self.size_bytes = size_bytes
        self.block = block
        self.device = device

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.size_bytes is not None:
            result['SizeBytes'] = self.size_bytes
        if self.block is not None:
            result['Block'] = self.block
        if self.device is not None:
            result['Device'] = self.device
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SizeBytes') is not None:
            self.size_bytes = m.get('SizeBytes')
        if m.get('Block') is not None:
            self.block = m.get('Block')
        if m.get('Device') is not None:
            self.device = m.get('Device')
        return self


class ModifyReplicationJobAttributeRequestDataDisk(TeaModel):
    def __init__(
        self,
        index: int = None,
        part: List[ModifyReplicationJobAttributeRequestDataDiskPart] = None,
        size: int = None,
    ):
        self.index = index
        self.part = part
        self.size = size

    def validate(self):
        if self.part:
            for k in self.part:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        result['Part'] = []
        if self.part is not None:
            for k in self.part:
                result['Part'].append(k.to_map() if k else None)
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        self.part = []
        if m.get('Part') is not None:
            for k in m.get('Part'):
                temp_model = ModifyReplicationJobAttributeRequestDataDiskPart()
                self.part.append(temp_model.from_map(k))
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class ModifyReplicationJobAttributeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        job_id: str = None,
        name: str = None,
        description: str = None,
        target_type: str = None,
        scheduled_start_time: str = None,
        image_name: str = None,
        instance_id: str = None,
        system_disk_size: int = None,
        frequency: int = None,
        max_number_of_image_to_keep: int = None,
        instance_type: str = None,
        launch_template_id: str = None,
        launch_template_version: str = None,
        instance_ram_role: str = None,
        container_namespace: str = None,
        container_repository: str = None,
        container_tag: str = None,
        valid_time: str = None,
        system_disk_part: List[ModifyReplicationJobAttributeRequestSystemDiskPart] = None,
        data_disk: List[ModifyReplicationJobAttributeRequestDataDisk] = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.job_id = job_id
        self.name = name
        self.description = description
        self.target_type = target_type
        self.scheduled_start_time = scheduled_start_time
        self.image_name = image_name
        self.instance_id = instance_id
        self.system_disk_size = system_disk_size
        self.frequency = frequency
        self.max_number_of_image_to_keep = max_number_of_image_to_keep
        self.instance_type = instance_type
        self.launch_template_id = launch_template_id
        self.launch_template_version = launch_template_version
        self.instance_ram_role = instance_ram_role
        self.container_namespace = container_namespace
        self.container_repository = container_repository
        self.container_tag = container_tag
        self.valid_time = valid_time
        self.system_disk_part = system_disk_part
        self.data_disk = data_disk

    def validate(self):
        if self.system_disk_part:
            for k in self.system_disk_part:
                if k:
                    k.validate()
        if self.data_disk:
            for k in self.data_disk:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.scheduled_start_time is not None:
            result['ScheduledStartTime'] = self.scheduled_start_time
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        if self.frequency is not None:
            result['Frequency'] = self.frequency
        if self.max_number_of_image_to_keep is not None:
            result['MaxNumberOfImageToKeep'] = self.max_number_of_image_to_keep
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.launch_template_id is not None:
            result['LaunchTemplateId'] = self.launch_template_id
        if self.launch_template_version is not None:
            result['LaunchTemplateVersion'] = self.launch_template_version
        if self.instance_ram_role is not None:
            result['InstanceRamRole'] = self.instance_ram_role
        if self.container_namespace is not None:
            result['ContainerNamespace'] = self.container_namespace
        if self.container_repository is not None:
            result['ContainerRepository'] = self.container_repository
        if self.container_tag is not None:
            result['ContainerTag'] = self.container_tag
        if self.valid_time is not None:
            result['ValidTime'] = self.valid_time
        result['SystemDiskPart'] = []
        if self.system_disk_part is not None:
            for k in self.system_disk_part:
                result['SystemDiskPart'].append(k.to_map() if k else None)
        result['DataDisk'] = []
        if self.data_disk is not None:
            for k in self.data_disk:
                result['DataDisk'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('ScheduledStartTime') is not None:
            self.scheduled_start_time = m.get('ScheduledStartTime')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        if m.get('Frequency') is not None:
            self.frequency = m.get('Frequency')
        if m.get('MaxNumberOfImageToKeep') is not None:
            self.max_number_of_image_to_keep = m.get('MaxNumberOfImageToKeep')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('LaunchTemplateId') is not None:
            self.launch_template_id = m.get('LaunchTemplateId')
        if m.get('LaunchTemplateVersion') is not None:
            self.launch_template_version = m.get('LaunchTemplateVersion')
        if m.get('InstanceRamRole') is not None:
            self.instance_ram_role = m.get('InstanceRamRole')
        if m.get('ContainerNamespace') is not None:
            self.container_namespace = m.get('ContainerNamespace')
        if m.get('ContainerRepository') is not None:
            self.container_repository = m.get('ContainerRepository')
        if m.get('ContainerTag') is not None:
            self.container_tag = m.get('ContainerTag')
        if m.get('ValidTime') is not None:
            self.valid_time = m.get('ValidTime')
        self.system_disk_part = []
        if m.get('SystemDiskPart') is not None:
            for k in m.get('SystemDiskPart'):
                temp_model = ModifyReplicationJobAttributeRequestSystemDiskPart()
                self.system_disk_part.append(temp_model.from_map(k))
        self.data_disk = []
        if m.get('DataDisk') is not None:
            for k in m.get('DataDisk'):
                temp_model = ModifyReplicationJobAttributeRequestDataDisk()
                self.data_disk.append(temp_model.from_map(k))
        return self


class ModifyReplicationJobAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyReplicationJobAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyReplicationJobAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyReplicationJobAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySourceServerAttributeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        source_id: str = None,
        name: str = None,
        description: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.source_id = source_id
        self.name = name
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class ModifySourceServerAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifySourceServerAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifySourceServerAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifySourceServerAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartReplicationJobRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        job_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class StartReplicationJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartReplicationJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartReplicationJobResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StartReplicationJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopReplicationJobRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        job_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class StopReplicationJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopReplicationJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopReplicationJobResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StopReplicationJobResponseBody()
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
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_type: str = None,
        resource_id: List[str] = None,
        tag: List[TagResourcesRequestTag] = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
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
        body: TagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_type: str = None,
        all: bool = None,
        resource_id: List[str] = None,
        tag_key: List[str] = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_type = resource_type
        self.all = all
        self.resource_id = resource_id
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.all is not None:
            result['All'] = self.all
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UntagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UntagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


