# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any, List


class CreateAccessGroupRequest(TeaModel):
    def __init__(
        self,
        access_group_name: str = None,
        description: str = None,
        input_region_id: str = None,
        network_type: str = None,
    ):
        self.access_group_name = access_group_name
        self.description = description
        self.input_region_id = input_region_id
        self.network_type = network_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_name is not None:
            result['AccessGroupName'] = self.access_group_name
        if self.description is not None:
            result['Description'] = self.description
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroupName') is not None:
            self.access_group_name = m.get('AccessGroupName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        return self


class CreateAccessGroupResponseBody(TeaModel):
    def __init__(
        self,
        access_group_id: str = None,
        request_id: str = None,
    ):
        self.access_group_id = access_group_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_id is not None:
            result['AccessGroupId'] = self.access_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroupId') is not None:
            self.access_group_id = m.get('AccessGroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAccessGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAccessGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateAccessGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAccessRuleRequest(TeaModel):
    def __init__(
        self,
        access_group_id: str = None,
        description: str = None,
        input_region_id: str = None,
        network_segment: str = None,
        priority: int = None,
        rwaccess_type: str = None,
    ):
        self.access_group_id = access_group_id
        self.description = description
        self.input_region_id = input_region_id
        self.network_segment = network_segment
        self.priority = priority
        self.rwaccess_type = rwaccess_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_id is not None:
            result['AccessGroupId'] = self.access_group_id
        if self.description is not None:
            result['Description'] = self.description
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id
        if self.network_segment is not None:
            result['NetworkSegment'] = self.network_segment
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.rwaccess_type is not None:
            result['RWAccessType'] = self.rwaccess_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroupId') is not None:
            self.access_group_id = m.get('AccessGroupId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')
        if m.get('NetworkSegment') is not None:
            self.network_segment = m.get('NetworkSegment')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('RWAccessType') is not None:
            self.rwaccess_type = m.get('RWAccessType')
        return self


class CreateAccessRuleResponseBody(TeaModel):
    def __init__(
        self,
        access_rule_id: str = None,
        request_id: str = None,
    ):
        self.access_rule_id = access_rule_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_rule_id is not None:
            result['AccessRuleId'] = self.access_rule_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessRuleId') is not None:
            self.access_rule_id = m.get('AccessRuleId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAccessRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAccessRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateAccessRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFileSystemRequest(TeaModel):
    def __init__(
        self,
        data_redundancy_type: str = None,
        description: str = None,
        file_system_name: str = None,
        input_region_id: str = None,
        partition_number: int = None,
        protocol_type: str = None,
        provisioned_throughput_in_mi_bps: int = None,
        space_capacity: int = None,
        storage_set_name: str = None,
        storage_type: str = None,
        throughput_mode: str = None,
        zone_id: str = None,
    ):
        self.data_redundancy_type = data_redundancy_type
        self.description = description
        self.file_system_name = file_system_name
        self.input_region_id = input_region_id
        self.partition_number = partition_number
        self.protocol_type = protocol_type
        self.provisioned_throughput_in_mi_bps = provisioned_throughput_in_mi_bps
        self.space_capacity = space_capacity
        self.storage_set_name = storage_set_name
        self.storage_type = storage_type
        self.throughput_mode = throughput_mode
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_redundancy_type is not None:
            result['DataRedundancyType'] = self.data_redundancy_type
        if self.description is not None:
            result['Description'] = self.description
        if self.file_system_name is not None:
            result['FileSystemName'] = self.file_system_name
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id
        if self.partition_number is not None:
            result['PartitionNumber'] = self.partition_number
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.provisioned_throughput_in_mi_bps is not None:
            result['ProvisionedThroughputInMiBps'] = self.provisioned_throughput_in_mi_bps
        if self.space_capacity is not None:
            result['SpaceCapacity'] = self.space_capacity
        if self.storage_set_name is not None:
            result['StorageSetName'] = self.storage_set_name
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.throughput_mode is not None:
            result['ThroughputMode'] = self.throughput_mode
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataRedundancyType') is not None:
            self.data_redundancy_type = m.get('DataRedundancyType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileSystemName') is not None:
            self.file_system_name = m.get('FileSystemName')
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')
        if m.get('PartitionNumber') is not None:
            self.partition_number = m.get('PartitionNumber')
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('ProvisionedThroughputInMiBps') is not None:
            self.provisioned_throughput_in_mi_bps = m.get('ProvisionedThroughputInMiBps')
        if m.get('SpaceCapacity') is not None:
            self.space_capacity = m.get('SpaceCapacity')
        if m.get('StorageSetName') is not None:
            self.storage_set_name = m.get('StorageSetName')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('ThroughputMode') is not None:
            self.throughput_mode = m.get('ThroughputMode')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateFileSystemResponseBody(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        request_id: str = None,
    ):
        self.file_system_id = file_system_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateFileSystemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateFileSystemResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateFileSystemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMountPointRequest(TeaModel):
    def __init__(
        self,
        access_group_id: str = None,
        description: str = None,
        file_system_id: str = None,
        input_region_id: str = None,
        network_type: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        self.access_group_id = access_group_id
        self.description = description
        self.file_system_id = file_system_id
        self.input_region_id = input_region_id
        self.network_type = network_type
        self.v_switch_id = v_switch_id
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_id is not None:
            result['AccessGroupId'] = self.access_group_id
        if self.description is not None:
            result['Description'] = self.description
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroupId') is not None:
            self.access_group_id = m.get('AccessGroupId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class CreateMountPointResponseBody(TeaModel):
    def __init__(
        self,
        mount_point_id: str = None,
        request_id: str = None,
    ):
        self.mount_point_id = mount_point_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mount_point_id is not None:
            result['MountPointId'] = self.mount_point_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MountPointId') is not None:
            self.mount_point_id = m.get('MountPointId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateMountPointResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateMountPointResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateMountPointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUserGroupsMappingRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        group_names: Dict[str, Any] = None,
        input_region_id: str = None,
        user_name: str = None,
    ):
        self.file_system_id = file_system_id
        self.group_names = group_names
        self.input_region_id = input_region_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.group_names is not None:
            result['GroupNames'] = self.group_names
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('GroupNames') is not None:
            self.group_names = m.get('GroupNames')
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class CreateUserGroupsMappingShrinkRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        group_names_shrink: str = None,
        input_region_id: str = None,
        user_name: str = None,
    ):
        self.file_system_id = file_system_id
        self.group_names_shrink = group_names_shrink
        self.input_region_id = input_region_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.group_names_shrink is not None:
            result['GroupNames'] = self.group_names_shrink
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('GroupNames') is not None:
            self.group_names_shrink = m.get('GroupNames')
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class CreateUserGroupsMappingResponseBody(TeaModel):
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


class CreateUserGroupsMappingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateUserGroupsMappingResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateUserGroupsMappingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAccessGroupRequest(TeaModel):
    def __init__(
        self,
        access_group_id: str = None,
        input_region_id: str = None,
    ):
        self.access_group_id = access_group_id
        self.input_region_id = input_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_id is not None:
            result['AccessGroupId'] = self.access_group_id
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroupId') is not None:
            self.access_group_id = m.get('AccessGroupId')
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')
        return self


class DeleteAccessGroupResponseBody(TeaModel):
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


class DeleteAccessGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteAccessGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteAccessGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAccessRuleRequest(TeaModel):
    def __init__(
        self,
        access_group_id: str = None,
        access_rule_id: str = None,
        input_region_id: str = None,
    ):
        self.access_group_id = access_group_id
        self.access_rule_id = access_rule_id
        self.input_region_id = input_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_id is not None:
            result['AccessGroupId'] = self.access_group_id
        if self.access_rule_id is not None:
            result['AccessRuleId'] = self.access_rule_id
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroupId') is not None:
            self.access_group_id = m.get('AccessGroupId')
        if m.get('AccessRuleId') is not None:
            self.access_rule_id = m.get('AccessRuleId')
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')
        return self


class DeleteAccessRuleResponseBody(TeaModel):
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


class DeleteAccessRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteAccessRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteAccessRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFileSystemRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        input_region_id: str = None,
    ):
        self.file_system_id = file_system_id
        self.input_region_id = input_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')
        return self


class DeleteFileSystemResponseBody(TeaModel):
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


class DeleteFileSystemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteFileSystemResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteFileSystemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMountPointRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        input_region_id: str = None,
        mount_point_id: str = None,
    ):
        self.file_system_id = file_system_id
        self.input_region_id = input_region_id
        self.mount_point_id = mount_point_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id
        if self.mount_point_id is not None:
            result['MountPointId'] = self.mount_point_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')
        if m.get('MountPointId') is not None:
            self.mount_point_id = m.get('MountPointId')
        return self


class DeleteMountPointResponseBody(TeaModel):
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


class DeleteMountPointResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteMountPointResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteMountPointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserGroupsMappingRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        group_names: Dict[str, Any] = None,
        input_region_id: str = None,
        user_name: str = None,
    ):
        self.file_system_id = file_system_id
        self.group_names = group_names
        self.input_region_id = input_region_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.group_names is not None:
            result['GroupNames'] = self.group_names
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('GroupNames') is not None:
            self.group_names = m.get('GroupNames')
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DeleteUserGroupsMappingShrinkRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        group_names_shrink: str = None,
        input_region_id: str = None,
        user_name: str = None,
    ):
        self.file_system_id = file_system_id
        self.group_names_shrink = group_names_shrink
        self.input_region_id = input_region_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.group_names_shrink is not None:
            result['GroupNames'] = self.group_names_shrink
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('GroupNames') is not None:
            self.group_names_shrink = m.get('GroupNames')
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DeleteUserGroupsMappingResponseBody(TeaModel):
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


class DeleteUserGroupsMappingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteUserGroupsMappingResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteUserGroupsMappingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        input_region_id: str = None,
    ):
        self.accept_language = accept_language
        self.input_region_id = input_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')
        return self


class DescribeRegionsResponseBodyRegionsRegion(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        region_endpoint: str = None,
        region_id: str = None,
    ):
        self.local_name = local_name
        self.region_endpoint = region_endpoint
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
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        region: List[DescribeRegionsResponseBodyRegionsRegion] = None,
    ):
        self.region = region

    def validate(self):
        if self.region:
            for k in self.region:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Region'] = []
        if self.region is not None:
            for k in self.region:
                result['Region'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region = []
        if m.get('Region') is not None:
            for k in m.get('Region'):
                temp_model = DescribeRegionsResponseBodyRegionsRegion()
                self.region.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        regions: DescribeRegionsResponseBodyRegions = None,
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
            temp_model = DescribeRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRegionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAccessGroupRequest(TeaModel):
    def __init__(
        self,
        access_group_id: str = None,
        input_region_id: str = None,
    ):
        self.access_group_id = access_group_id
        self.input_region_id = input_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_id is not None:
            result['AccessGroupId'] = self.access_group_id
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroupId') is not None:
            self.access_group_id = m.get('AccessGroupId')
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')
        return self


class GetAccessGroupResponseBodyAccessGroup(TeaModel):
    def __init__(
        self,
        access_group_id: str = None,
        access_group_name: str = None,
        create_time: str = None,
        description: str = None,
        is_default: bool = None,
        mount_point_count: int = None,
        network_type: str = None,
        region_id: str = None,
        rule_count: int = None,
    ):
        self.access_group_id = access_group_id
        self.access_group_name = access_group_name
        self.create_time = create_time
        self.description = description
        self.is_default = is_default
        self.mount_point_count = mount_point_count
        self.network_type = network_type
        self.region_id = region_id
        self.rule_count = rule_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_id is not None:
            result['AccessGroupId'] = self.access_group_id
        if self.access_group_name is not None:
            result['AccessGroupName'] = self.access_group_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.mount_point_count is not None:
            result['MountPointCount'] = self.mount_point_count
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rule_count is not None:
            result['RuleCount'] = self.rule_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroupId') is not None:
            self.access_group_id = m.get('AccessGroupId')
        if m.get('AccessGroupName') is not None:
            self.access_group_name = m.get('AccessGroupName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('MountPointCount') is not None:
            self.mount_point_count = m.get('MountPointCount')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RuleCount') is not None:
            self.rule_count = m.get('RuleCount')
        return self


class GetAccessGroupResponseBody(TeaModel):
    def __init__(
        self,
        access_group: GetAccessGroupResponseBodyAccessGroup = None,
        request_id: str = None,
    ):
        self.access_group = access_group
        self.request_id = request_id

    def validate(self):
        if self.access_group:
            self.access_group.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group is not None:
            result['AccessGroup'] = self.access_group.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroup') is not None:
            temp_model = GetAccessGroupResponseBodyAccessGroup()
            self.access_group = temp_model.from_map(m['AccessGroup'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAccessGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAccessGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAccessGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAccessRuleRequest(TeaModel):
    def __init__(
        self,
        access_group_id: str = None,
        access_rule_id: str = None,
        input_region_id: str = None,
    ):
        self.access_group_id = access_group_id
        self.access_rule_id = access_rule_id
        self.input_region_id = input_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_id is not None:
            result['AccessGroupId'] = self.access_group_id
        if self.access_rule_id is not None:
            result['AccessRuleId'] = self.access_rule_id
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroupId') is not None:
            self.access_group_id = m.get('AccessGroupId')
        if m.get('AccessRuleId') is not None:
            self.access_rule_id = m.get('AccessRuleId')
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')
        return self


class GetAccessRuleResponseBodyAccessRule(TeaModel):
    def __init__(
        self,
        access_group_id: str = None,
        access_rule_id: str = None,
        create_time: str = None,
        description: str = None,
        network_segment: str = None,
        priority: int = None,
        rwaccess_type: str = None,
        region_id: str = None,
    ):
        self.access_group_id = access_group_id
        self.access_rule_id = access_rule_id
        self.create_time = create_time
        self.description = description
        self.network_segment = network_segment
        self.priority = priority
        self.rwaccess_type = rwaccess_type
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_id is not None:
            result['AccessGroupId'] = self.access_group_id
        if self.access_rule_id is not None:
            result['AccessRuleId'] = self.access_rule_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.network_segment is not None:
            result['NetworkSegment'] = self.network_segment
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.rwaccess_type is not None:
            result['RWAccessType'] = self.rwaccess_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroupId') is not None:
            self.access_group_id = m.get('AccessGroupId')
        if m.get('AccessRuleId') is not None:
            self.access_rule_id = m.get('AccessRuleId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('NetworkSegment') is not None:
            self.network_segment = m.get('NetworkSegment')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('RWAccessType') is not None:
            self.rwaccess_type = m.get('RWAccessType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetAccessRuleResponseBody(TeaModel):
    def __init__(
        self,
        access_rule: GetAccessRuleResponseBodyAccessRule = None,
        request_id: str = None,
    ):
        self.access_rule = access_rule
        self.request_id = request_id

    def validate(self):
        if self.access_rule:
            self.access_rule.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_rule is not None:
            result['AccessRule'] = self.access_rule.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessRule') is not None:
            temp_model = GetAccessRuleResponseBodyAccessRule()
            self.access_rule = temp_model.from_map(m['AccessRule'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAccessRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAccessRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAccessRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFileSystemRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        input_region_id: str = None,
    ):
        self.file_system_id = file_system_id
        self.input_region_id = input_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')
        return self


class GetFileSystemResponseBodyFileSystem(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        file_system_id: str = None,
        file_system_name: str = None,
        metering_space_size: float = None,
        mount_point_count: int = None,
        number_of_directories: int = None,
        number_of_files: int = None,
        protocol_type: str = None,
        provisioned_throughput_in_mi_bps: int = None,
        region_id: str = None,
        space_capacity: int = None,
        storage_package_id: str = None,
        storage_type: str = None,
        throughput_mode: str = None,
        used_space_size: float = None,
        version: str = None,
        zone_id: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.file_system_id = file_system_id
        self.file_system_name = file_system_name
        self.metering_space_size = metering_space_size
        self.mount_point_count = mount_point_count
        self.number_of_directories = number_of_directories
        self.number_of_files = number_of_files
        self.protocol_type = protocol_type
        self.provisioned_throughput_in_mi_bps = provisioned_throughput_in_mi_bps
        self.region_id = region_id
        self.space_capacity = space_capacity
        self.storage_package_id = storage_package_id
        self.storage_type = storage_type
        self.throughput_mode = throughput_mode
        self.used_space_size = used_space_size
        self.version = version
        self.zone_id = zone_id

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
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.file_system_name is not None:
            result['FileSystemName'] = self.file_system_name
        if self.metering_space_size is not None:
            result['MeteringSpaceSize'] = self.metering_space_size
        if self.mount_point_count is not None:
            result['MountPointCount'] = self.mount_point_count
        if self.number_of_directories is not None:
            result['NumberOfDirectories'] = self.number_of_directories
        if self.number_of_files is not None:
            result['NumberOfFiles'] = self.number_of_files
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.provisioned_throughput_in_mi_bps is not None:
            result['ProvisionedThroughputInMiBps'] = self.provisioned_throughput_in_mi_bps
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.space_capacity is not None:
            result['SpaceCapacity'] = self.space_capacity
        if self.storage_package_id is not None:
            result['StoragePackageId'] = self.storage_package_id
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.throughput_mode is not None:
            result['ThroughputMode'] = self.throughput_mode
        if self.used_space_size is not None:
            result['UsedSpaceSize'] = self.used_space_size
        if self.version is not None:
            result['Version'] = self.version
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('FileSystemName') is not None:
            self.file_system_name = m.get('FileSystemName')
        if m.get('MeteringSpaceSize') is not None:
            self.metering_space_size = m.get('MeteringSpaceSize')
        if m.get('MountPointCount') is not None:
            self.mount_point_count = m.get('MountPointCount')
        if m.get('NumberOfDirectories') is not None:
            self.number_of_directories = m.get('NumberOfDirectories')
        if m.get('NumberOfFiles') is not None:
            self.number_of_files = m.get('NumberOfFiles')
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('ProvisionedThroughputInMiBps') is not None:
            self.provisioned_throughput_in_mi_bps = m.get('ProvisionedThroughputInMiBps')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SpaceCapacity') is not None:
            self.space_capacity = m.get('SpaceCapacity')
        if m.get('StoragePackageId') is not None:
            self.storage_package_id = m.get('StoragePackageId')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('ThroughputMode') is not None:
            self.throughput_mode = m.get('ThroughputMode')
        if m.get('UsedSpaceSize') is not None:
            self.used_space_size = m.get('UsedSpaceSize')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class GetFileSystemResponseBody(TeaModel):
    def __init__(
        self,
        file_system: GetFileSystemResponseBodyFileSystem = None,
        request_id: str = None,
    ):
        self.file_system = file_system
        self.request_id = request_id

    def validate(self):
        if self.file_system:
            self.file_system.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system is not None:
            result['FileSystem'] = self.file_system.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystem') is not None:
            temp_model = GetFileSystemResponseBodyFileSystem()
            self.file_system = temp_model.from_map(m['FileSystem'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetFileSystemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetFileSystemResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetFileSystemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMountPointRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        input_region_id: str = None,
        mount_point_id: str = None,
    ):
        self.file_system_id = file_system_id
        self.input_region_id = input_region_id
        self.mount_point_id = mount_point_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id
        if self.mount_point_id is not None:
            result['MountPointId'] = self.mount_point_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')
        if m.get('MountPointId') is not None:
            self.mount_point_id = m.get('MountPointId')
        return self


class GetMountPointResponseBodyMountPoint(TeaModel):
    def __init__(
        self,
        access_group_id: str = None,
        create_time: str = None,
        description: str = None,
        file_system_id: str = None,
        mount_point_domain: str = None,
        mount_point_id: str = None,
        network_type: str = None,
        region_id: str = None,
        status: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        self.access_group_id = access_group_id
        self.create_time = create_time
        self.description = description
        self.file_system_id = file_system_id
        self.mount_point_domain = mount_point_domain
        self.mount_point_id = mount_point_id
        self.network_type = network_type
        self.region_id = region_id
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
        if self.access_group_id is not None:
            result['AccessGroupId'] = self.access_group_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.mount_point_domain is not None:
            result['MountPointDomain'] = self.mount_point_domain
        if self.mount_point_id is not None:
            result['MountPointId'] = self.mount_point_id
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroupId') is not None:
            self.access_group_id = m.get('AccessGroupId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('MountPointDomain') is not None:
            self.mount_point_domain = m.get('MountPointDomain')
        if m.get('MountPointId') is not None:
            self.mount_point_id = m.get('MountPointId')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class GetMountPointResponseBody(TeaModel):
    def __init__(
        self,
        mount_point: GetMountPointResponseBodyMountPoint = None,
        request_id: str = None,
    ):
        self.mount_point = mount_point
        self.request_id = request_id

    def validate(self):
        if self.mount_point:
            self.mount_point.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mount_point is not None:
            result['MountPoint'] = self.mount_point.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MountPoint') is not None:
            temp_model = GetMountPointResponseBodyMountPoint()
            self.mount_point = temp_model.from_map(m['MountPoint'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetMountPointResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetMountPointResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetMountPointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRegionRequest(TeaModel):
    def __init__(
        self,
        input_region_id: str = None,
    ):
        self.input_region_id = input_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')
        return self


class GetRegionResponseBodyAvailableZonesOptions(TeaModel):
    def __init__(
        self,
        protocol_type: str = None,
        storage_type: str = None,
    ):
        self.protocol_type = protocol_type
        self.storage_type = storage_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        return self


class GetRegionResponseBodyAvailableZones(TeaModel):
    def __init__(
        self,
        options: List[GetRegionResponseBodyAvailableZonesOptions] = None,
        zone_id: str = None,
    ):
        self.options = options
        self.zone_id = zone_id

    def validate(self):
        if self.options:
            for k in self.options:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Options'] = []
        if self.options is not None:
            for k in self.options:
                result['Options'].append(k.to_map() if k else None)
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.options = []
        if m.get('Options') is not None:
            for k in m.get('Options'):
                temp_model = GetRegionResponseBodyAvailableZonesOptions()
                self.options.append(temp_model.from_map(k))
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class GetRegionResponseBody(TeaModel):
    def __init__(
        self,
        available_zones: List[GetRegionResponseBodyAvailableZones] = None,
        request_id: str = None,
    ):
        self.available_zones = available_zones
        self.request_id = request_id

    def validate(self):
        if self.available_zones:
            for k in self.available_zones:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AvailableZones'] = []
        if self.available_zones is not None:
            for k in self.available_zones:
                result['AvailableZones'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.available_zones = []
        if m.get('AvailableZones') is not None:
            for k in m.get('AvailableZones'):
                temp_model = GetRegionResponseBodyAvailableZones()
                self.available_zones.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetRegionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetRegionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetRegionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAccessGroupsRequest(TeaModel):
    def __init__(
        self,
        input_region_id: str = None,
        limit: int = None,
        order_by: str = None,
        order_type: str = None,
        start_offset: int = None,
    ):
        self.input_region_id = input_region_id
        self.limit = limit
        self.order_by = order_by
        self.order_type = order_type
        self.start_offset = start_offset

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.start_offset is not None:
            result['StartOffset'] = self.start_offset
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('StartOffset') is not None:
            self.start_offset = m.get('StartOffset')
        return self


class ListAccessGroupsResponseBodyAccessGroups(TeaModel):
    def __init__(
        self,
        access_group_id: str = None,
        access_group_name: str = None,
        create_time: str = None,
        description: str = None,
        is_default: bool = None,
        mount_point_count: int = None,
        network_type: str = None,
        region_id: str = None,
        rule_count: int = None,
    ):
        self.access_group_id = access_group_id
        self.access_group_name = access_group_name
        self.create_time = create_time
        self.description = description
        self.is_default = is_default
        self.mount_point_count = mount_point_count
        self.network_type = network_type
        self.region_id = region_id
        self.rule_count = rule_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_id is not None:
            result['AccessGroupId'] = self.access_group_id
        if self.access_group_name is not None:
            result['AccessGroupName'] = self.access_group_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.mount_point_count is not None:
            result['MountPointCount'] = self.mount_point_count
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rule_count is not None:
            result['RuleCount'] = self.rule_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroupId') is not None:
            self.access_group_id = m.get('AccessGroupId')
        if m.get('AccessGroupName') is not None:
            self.access_group_name = m.get('AccessGroupName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('MountPointCount') is not None:
            self.mount_point_count = m.get('MountPointCount')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RuleCount') is not None:
            self.rule_count = m.get('RuleCount')
        return self


class ListAccessGroupsResponseBody(TeaModel):
    def __init__(
        self,
        access_groups: List[ListAccessGroupsResponseBodyAccessGroups] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.access_groups = access_groups
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.access_groups:
            for k in self.access_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AccessGroups'] = []
        if self.access_groups is not None:
            for k in self.access_groups:
                result['AccessGroups'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.access_groups = []
        if m.get('AccessGroups') is not None:
            for k in m.get('AccessGroups'):
                temp_model = ListAccessGroupsResponseBodyAccessGroups()
                self.access_groups.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAccessGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAccessGroupsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAccessGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAccessRulesRequest(TeaModel):
    def __init__(
        self,
        access_group_id: str = None,
        input_region_id: str = None,
        limit: int = None,
        order_by: str = None,
        order_type: str = None,
        start_offset: int = None,
    ):
        self.access_group_id = access_group_id
        self.input_region_id = input_region_id
        self.limit = limit
        self.order_by = order_by
        self.order_type = order_type
        self.start_offset = start_offset

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_id is not None:
            result['AccessGroupId'] = self.access_group_id
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.start_offset is not None:
            result['StartOffset'] = self.start_offset
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroupId') is not None:
            self.access_group_id = m.get('AccessGroupId')
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('StartOffset') is not None:
            self.start_offset = m.get('StartOffset')
        return self


class ListAccessRulesResponseBodyAccessRules(TeaModel):
    def __init__(
        self,
        access_group_id: str = None,
        access_rule_id: str = None,
        create_time: str = None,
        description: str = None,
        network_segment: str = None,
        priority: int = None,
        rwaccess_type: str = None,
        region_id: str = None,
    ):
        self.access_group_id = access_group_id
        self.access_rule_id = access_rule_id
        self.create_time = create_time
        self.description = description
        self.network_segment = network_segment
        self.priority = priority
        self.rwaccess_type = rwaccess_type
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_id is not None:
            result['AccessGroupId'] = self.access_group_id
        if self.access_rule_id is not None:
            result['AccessRuleId'] = self.access_rule_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.network_segment is not None:
            result['NetworkSegment'] = self.network_segment
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.rwaccess_type is not None:
            result['RWAccessType'] = self.rwaccess_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroupId') is not None:
            self.access_group_id = m.get('AccessGroupId')
        if m.get('AccessRuleId') is not None:
            self.access_rule_id = m.get('AccessRuleId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('NetworkSegment') is not None:
            self.network_segment = m.get('NetworkSegment')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('RWAccessType') is not None:
            self.rwaccess_type = m.get('RWAccessType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListAccessRulesResponseBody(TeaModel):
    def __init__(
        self,
        access_rules: List[ListAccessRulesResponseBodyAccessRules] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.access_rules = access_rules
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.access_rules:
            for k in self.access_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AccessRules'] = []
        if self.access_rules is not None:
            for k in self.access_rules:
                result['AccessRules'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.access_rules = []
        if m.get('AccessRules') is not None:
            for k in m.get('AccessRules'):
                temp_model = ListAccessRulesResponseBodyAccessRules()
                self.access_rules.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAccessRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAccessRulesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAccessRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFileSystemsRequest(TeaModel):
    def __init__(
        self,
        input_region_id: str = None,
        limit: int = None,
        order_by: str = None,
        order_type: str = None,
        start_offset: int = None,
    ):
        self.input_region_id = input_region_id
        self.limit = limit
        self.order_by = order_by
        self.order_type = order_type
        self.start_offset = start_offset

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.start_offset is not None:
            result['StartOffset'] = self.start_offset
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('StartOffset') is not None:
            self.start_offset = m.get('StartOffset')
        return self


class ListFileSystemsResponseBodyFileSystems(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        file_system_id: str = None,
        file_system_name: str = None,
        metering_space_size: float = None,
        mount_point_count: int = None,
        number_of_directories: int = None,
        number_of_files: int = None,
        protocol_type: str = None,
        provisioned_throughput_in_mi_bps: int = None,
        region_id: str = None,
        space_capacity: int = None,
        storage_package_id: str = None,
        storage_type: str = None,
        throughput_mode: str = None,
        used_space_size: float = None,
        version: str = None,
        zone_id: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.file_system_id = file_system_id
        self.file_system_name = file_system_name
        self.metering_space_size = metering_space_size
        self.mount_point_count = mount_point_count
        self.number_of_directories = number_of_directories
        self.number_of_files = number_of_files
        self.protocol_type = protocol_type
        self.provisioned_throughput_in_mi_bps = provisioned_throughput_in_mi_bps
        self.region_id = region_id
        self.space_capacity = space_capacity
        self.storage_package_id = storage_package_id
        self.storage_type = storage_type
        self.throughput_mode = throughput_mode
        self.used_space_size = used_space_size
        self.version = version
        self.zone_id = zone_id

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
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.file_system_name is not None:
            result['FileSystemName'] = self.file_system_name
        if self.metering_space_size is not None:
            result['MeteringSpaceSize'] = self.metering_space_size
        if self.mount_point_count is not None:
            result['MountPointCount'] = self.mount_point_count
        if self.number_of_directories is not None:
            result['NumberOfDirectories'] = self.number_of_directories
        if self.number_of_files is not None:
            result['NumberOfFiles'] = self.number_of_files
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.provisioned_throughput_in_mi_bps is not None:
            result['ProvisionedThroughputInMiBps'] = self.provisioned_throughput_in_mi_bps
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.space_capacity is not None:
            result['SpaceCapacity'] = self.space_capacity
        if self.storage_package_id is not None:
            result['StoragePackageId'] = self.storage_package_id
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.throughput_mode is not None:
            result['ThroughputMode'] = self.throughput_mode
        if self.used_space_size is not None:
            result['UsedSpaceSize'] = self.used_space_size
        if self.version is not None:
            result['Version'] = self.version
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('FileSystemName') is not None:
            self.file_system_name = m.get('FileSystemName')
        if m.get('MeteringSpaceSize') is not None:
            self.metering_space_size = m.get('MeteringSpaceSize')
        if m.get('MountPointCount') is not None:
            self.mount_point_count = m.get('MountPointCount')
        if m.get('NumberOfDirectories') is not None:
            self.number_of_directories = m.get('NumberOfDirectories')
        if m.get('NumberOfFiles') is not None:
            self.number_of_files = m.get('NumberOfFiles')
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('ProvisionedThroughputInMiBps') is not None:
            self.provisioned_throughput_in_mi_bps = m.get('ProvisionedThroughputInMiBps')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SpaceCapacity') is not None:
            self.space_capacity = m.get('SpaceCapacity')
        if m.get('StoragePackageId') is not None:
            self.storage_package_id = m.get('StoragePackageId')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('ThroughputMode') is not None:
            self.throughput_mode = m.get('ThroughputMode')
        if m.get('UsedSpaceSize') is not None:
            self.used_space_size = m.get('UsedSpaceSize')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListFileSystemsResponseBody(TeaModel):
    def __init__(
        self,
        file_systems: List[ListFileSystemsResponseBodyFileSystems] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.file_systems = file_systems
        self.request_id = request_id
        self.total_count = total_count

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.file_systems = []
        if m.get('FileSystems') is not None:
            for k in m.get('FileSystems'):
                temp_model = ListFileSystemsResponseBodyFileSystems()
                self.file_systems.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListFileSystemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListFileSystemsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListFileSystemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMountPointsRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        input_region_id: str = None,
        limit: int = None,
        order_by: str = None,
        order_type: str = None,
        start_offset: int = None,
    ):
        self.file_system_id = file_system_id
        self.input_region_id = input_region_id
        self.limit = limit
        self.order_by = order_by
        self.order_type = order_type
        self.start_offset = start_offset

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.start_offset is not None:
            result['StartOffset'] = self.start_offset
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('StartOffset') is not None:
            self.start_offset = m.get('StartOffset')
        return self


class ListMountPointsResponseBodyMountPoints(TeaModel):
    def __init__(
        self,
        access_group_id: str = None,
        create_time: str = None,
        description: str = None,
        file_system_id: str = None,
        mount_point_domain: str = None,
        mount_point_id: str = None,
        network_type: str = None,
        region_id: str = None,
        status: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        self.access_group_id = access_group_id
        self.create_time = create_time
        self.description = description
        self.file_system_id = file_system_id
        self.mount_point_domain = mount_point_domain
        self.mount_point_id = mount_point_id
        self.network_type = network_type
        self.region_id = region_id
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
        if self.access_group_id is not None:
            result['AccessGroupId'] = self.access_group_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.mount_point_domain is not None:
            result['MountPointDomain'] = self.mount_point_domain
        if self.mount_point_id is not None:
            result['MountPointId'] = self.mount_point_id
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroupId') is not None:
            self.access_group_id = m.get('AccessGroupId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('MountPointDomain') is not None:
            self.mount_point_domain = m.get('MountPointDomain')
        if m.get('MountPointId') is not None:
            self.mount_point_id = m.get('MountPointId')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ListMountPointsResponseBody(TeaModel):
    def __init__(
        self,
        mount_points: List[ListMountPointsResponseBodyMountPoints] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.mount_points = mount_points
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.mount_points:
            for k in self.mount_points:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MountPoints'] = []
        if self.mount_points is not None:
            for k in self.mount_points:
                result['MountPoints'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.mount_points = []
        if m.get('MountPoints') is not None:
            for k in m.get('MountPoints'):
                temp_model = ListMountPointsResponseBodyMountPoints()
                self.mount_points.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListMountPointsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListMountPointsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListMountPointsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserGroupsMappingsRequest(TeaModel):
    def __init__(
        self,
        filesystem_id: str = None,
        input_region_id: str = None,
        limit: int = None,
        next_token: str = None,
    ):
        self.filesystem_id = filesystem_id
        self.input_region_id = input_region_id
        self.limit = limit
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filesystem_id is not None:
            result['FilesystemId'] = self.filesystem_id
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilesystemId') is not None:
            self.filesystem_id = m.get('FilesystemId')
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListUserGroupsMappingsResponseBodyUserGroupsMappings(TeaModel):
    def __init__(
        self,
        group_names: List[str] = None,
        user_name: str = None,
    ):
        self.group_names = group_names
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_names is not None:
            result['GroupNames'] = self.group_names
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupNames') is not None:
            self.group_names = m.get('GroupNames')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class ListUserGroupsMappingsResponseBody(TeaModel):
    def __init__(
        self,
        has_more: bool = None,
        next_token: str = None,
        request_id: str = None,
        user_groups_mappings: List[ListUserGroupsMappingsResponseBodyUserGroupsMappings] = None,
    ):
        self.has_more = has_more
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        self.user_groups_mappings = user_groups_mappings

    def validate(self):
        if self.user_groups_mappings:
            for k in self.user_groups_mappings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_more is not None:
            result['HasMore'] = self.has_more
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['UserGroupsMappings'] = []
        if self.user_groups_mappings is not None:
            for k in self.user_groups_mappings:
                result['UserGroupsMappings'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.user_groups_mappings = []
        if m.get('UserGroupsMappings') is not None:
            for k in m.get('UserGroupsMappings'):
                temp_model = ListUserGroupsMappingsResponseBodyUserGroupsMappings()
                self.user_groups_mappings.append(temp_model.from_map(k))
        return self


class ListUserGroupsMappingsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListUserGroupsMappingsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListUserGroupsMappingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAccessGroupRequest(TeaModel):
    def __init__(
        self,
        access_group_id: str = None,
        access_group_name: str = None,
        description: str = None,
        input_region_id: str = None,
    ):
        self.access_group_id = access_group_id
        self.access_group_name = access_group_name
        self.description = description
        self.input_region_id = input_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_id is not None:
            result['AccessGroupId'] = self.access_group_id
        if self.access_group_name is not None:
            result['AccessGroupName'] = self.access_group_name
        if self.description is not None:
            result['Description'] = self.description
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroupId') is not None:
            self.access_group_id = m.get('AccessGroupId')
        if m.get('AccessGroupName') is not None:
            self.access_group_name = m.get('AccessGroupName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')
        return self


class ModifyAccessGroupResponseBody(TeaModel):
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


class ModifyAccessGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyAccessGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyAccessGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAccessRuleRequest(TeaModel):
    def __init__(
        self,
        access_group_id: str = None,
        access_rule_id: str = None,
        description: str = None,
        input_region_id: str = None,
        priority: int = None,
        rwaccess_type: str = None,
    ):
        self.access_group_id = access_group_id
        self.access_rule_id = access_rule_id
        self.description = description
        self.input_region_id = input_region_id
        self.priority = priority
        self.rwaccess_type = rwaccess_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_id is not None:
            result['AccessGroupId'] = self.access_group_id
        if self.access_rule_id is not None:
            result['AccessRuleId'] = self.access_rule_id
        if self.description is not None:
            result['Description'] = self.description
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.rwaccess_type is not None:
            result['RWAccessType'] = self.rwaccess_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroupId') is not None:
            self.access_group_id = m.get('AccessGroupId')
        if m.get('AccessRuleId') is not None:
            self.access_rule_id = m.get('AccessRuleId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('RWAccessType') is not None:
            self.rwaccess_type = m.get('RWAccessType')
        return self


class ModifyAccessRuleResponseBody(TeaModel):
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


class ModifyAccessRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyAccessRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyAccessRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyFileSystemRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        file_system_id: str = None,
        file_system_name: str = None,
        input_region_id: str = None,
        provisioned_throughput_in_mi_bps: int = None,
        space_capacity: int = None,
        throughput_mode: str = None,
    ):
        self.description = description
        self.file_system_id = file_system_id
        self.file_system_name = file_system_name
        self.input_region_id = input_region_id
        self.provisioned_throughput_in_mi_bps = provisioned_throughput_in_mi_bps
        self.space_capacity = space_capacity
        self.throughput_mode = throughput_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.file_system_name is not None:
            result['FileSystemName'] = self.file_system_name
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id
        if self.provisioned_throughput_in_mi_bps is not None:
            result['ProvisionedThroughputInMiBps'] = self.provisioned_throughput_in_mi_bps
        if self.space_capacity is not None:
            result['SpaceCapacity'] = self.space_capacity
        if self.throughput_mode is not None:
            result['ThroughputMode'] = self.throughput_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('FileSystemName') is not None:
            self.file_system_name = m.get('FileSystemName')
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')
        if m.get('ProvisionedThroughputInMiBps') is not None:
            self.provisioned_throughput_in_mi_bps = m.get('ProvisionedThroughputInMiBps')
        if m.get('SpaceCapacity') is not None:
            self.space_capacity = m.get('SpaceCapacity')
        if m.get('ThroughputMode') is not None:
            self.throughput_mode = m.get('ThroughputMode')
        return self


class ModifyFileSystemResponseBody(TeaModel):
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


class ModifyFileSystemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyFileSystemResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyFileSystemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyMountPointRequest(TeaModel):
    def __init__(
        self,
        access_group_id: str = None,
        description: str = None,
        file_system_id: str = None,
        input_region_id: str = None,
        mount_point_id: str = None,
        status: str = None,
    ):
        self.access_group_id = access_group_id
        self.description = description
        self.file_system_id = file_system_id
        self.input_region_id = input_region_id
        self.mount_point_id = mount_point_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_id is not None:
            result['AccessGroupId'] = self.access_group_id
        if self.description is not None:
            result['Description'] = self.description
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id
        if self.mount_point_id is not None:
            result['MountPointId'] = self.mount_point_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroupId') is not None:
            self.access_group_id = m.get('AccessGroupId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')
        if m.get('MountPointId') is not None:
            self.mount_point_id = m.get('MountPointId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ModifyMountPointResponseBody(TeaModel):
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


class ModifyMountPointResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyMountPointResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyMountPointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


