# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any, List


class AddTagsBatchRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dbfs_list: str = None,
        region_id: str = None,
        tags: str = None,
    ):
        self.client_token = client_token
        self.dbfs_list = dbfs_list
        self.region_id = region_id
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dbfs_list is not None:
            result['DbfsList'] = self.dbfs_list
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DbfsList') is not None:
            self.dbfs_list = m.get('DbfsList')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class AddTagsBatchResponseBody(TeaModel):
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


class AddTagsBatchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddTagsBatchResponseBody = None,
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
            temp_model = AddTagsBatchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachDbfsRequest(TeaModel):
    def __init__(
        self,
        attach_mode: str = None,
        attach_point: str = None,
        ecsinstance_id: str = None,
        fs_id: str = None,
        region_id: str = None,
        server_url: str = None,
    ):
        self.attach_mode = attach_mode
        self.attach_point = attach_point
        self.ecsinstance_id = ecsinstance_id
        self.fs_id = fs_id
        self.region_id = region_id
        self.server_url = server_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attach_mode is not None:
            result['AttachMode'] = self.attach_mode
        if self.attach_point is not None:
            result['AttachPoint'] = self.attach_point
        if self.ecsinstance_id is not None:
            result['ECSInstanceId'] = self.ecsinstance_id
        if self.fs_id is not None:
            result['FsId'] = self.fs_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.server_url is not None:
            result['ServerUrl'] = self.server_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachMode') is not None:
            self.attach_mode = m.get('AttachMode')
        if m.get('AttachPoint') is not None:
            self.attach_point = m.get('AttachPoint')
        if m.get('ECSInstanceId') is not None:
            self.ecsinstance_id = m.get('ECSInstanceId')
        if m.get('FsId') is not None:
            self.fs_id = m.get('FsId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServerUrl') is not None:
            self.server_url = m.get('ServerUrl')
        return self


class AttachDbfsResponseBody(TeaModel):
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


class AttachDbfsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AttachDbfsResponseBody = None,
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
            temp_model = AttachDbfsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDbfsRequest(TeaModel):
    def __init__(
        self,
        category: str = None,
        client_token: str = None,
        delete_snapshot: bool = None,
        enable_raid: bool = None,
        encryption: bool = None,
        fs_name: str = None,
        instance_type: str = None,
        kmskey_id: str = None,
        performance_level: str = None,
        raid_stripe_unit_number: int = None,
        region_id: str = None,
        size_g: int = None,
        snapshot_id: str = None,
        used_scene: str = None,
        zone_id: str = None,
    ):
        self.category = category
        self.client_token = client_token
        self.delete_snapshot = delete_snapshot
        self.enable_raid = enable_raid
        self.encryption = encryption
        self.fs_name = fs_name
        self.instance_type = instance_type
        self.kmskey_id = kmskey_id
        self.performance_level = performance_level
        self.raid_stripe_unit_number = raid_stripe_unit_number
        self.region_id = region_id
        self.size_g = size_g
        self.snapshot_id = snapshot_id
        self.used_scene = used_scene
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.delete_snapshot is not None:
            result['DeleteSnapshot'] = self.delete_snapshot
        if self.enable_raid is not None:
            result['EnableRaid'] = self.enable_raid
        if self.encryption is not None:
            result['Encryption'] = self.encryption
        if self.fs_name is not None:
            result['FsName'] = self.fs_name
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.kmskey_id is not None:
            result['KMSKeyId'] = self.kmskey_id
        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level
        if self.raid_stripe_unit_number is not None:
            result['RaidStripeUnitNumber'] = self.raid_stripe_unit_number
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.size_g is not None:
            result['SizeG'] = self.size_g
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.used_scene is not None:
            result['UsedScene'] = self.used_scene
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DeleteSnapshot') is not None:
            self.delete_snapshot = m.get('DeleteSnapshot')
        if m.get('EnableRaid') is not None:
            self.enable_raid = m.get('EnableRaid')
        if m.get('Encryption') is not None:
            self.encryption = m.get('Encryption')
        if m.get('FsName') is not None:
            self.fs_name = m.get('FsName')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('KMSKeyId') is not None:
            self.kmskey_id = m.get('KMSKeyId')
        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')
        if m.get('RaidStripeUnitNumber') is not None:
            self.raid_stripe_unit_number = m.get('RaidStripeUnitNumber')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SizeG') is not None:
            self.size_g = m.get('SizeG')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('UsedScene') is not None:
            self.used_scene = m.get('UsedScene')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateDbfsResponseBody(TeaModel):
    def __init__(
        self,
        fs_id: str = None,
        request_id: str = None,
    ):
        self.fs_id = fs_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fs_id is not None:
            result['FsId'] = self.fs_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FsId') is not None:
            self.fs_id = m.get('FsId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDbfsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDbfsResponseBody = None,
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
            temp_model = CreateDbfsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceLinkedRoleRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        region_id: str = None,
    ):
        self.client_token = client_token
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateServiceLinkedRoleResponseBody(TeaModel):
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


class CreateServiceLinkedRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateServiceLinkedRoleResponseBody = None,
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
            temp_model = CreateServiceLinkedRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSnapshotRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        fs_id: str = None,
        region_id: str = None,
        retention_days: int = None,
        snapshot_name: str = None,
    ):
        self.client_token = client_token
        self.description = description
        self.fs_id = fs_id
        self.region_id = region_id
        self.retention_days = retention_days
        self.snapshot_name = snapshot_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.fs_id is not None:
            result['FsId'] = self.fs_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.retention_days is not None:
            result['RetentionDays'] = self.retention_days
        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FsId') is not None:
            self.fs_id = m.get('FsId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RetentionDays') is not None:
            self.retention_days = m.get('RetentionDays')
        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')
        return self


class CreateSnapshotResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        snapshot_id: str = None,
    ):
        self.request_id = request_id
        self.snapshot_id = snapshot_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        return self


class CreateSnapshotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateSnapshotResponseBody = None,
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
            temp_model = CreateSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDbfsRequest(TeaModel):
    def __init__(
        self,
        fs_id: str = None,
        region_id: str = None,
    ):
        self.fs_id = fs_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fs_id is not None:
            result['FsId'] = self.fs_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FsId') is not None:
            self.fs_id = m.get('FsId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteDbfsResponseBody(TeaModel):
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


class DeleteDbfsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDbfsResponseBody = None,
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
            temp_model = DeleteDbfsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSnapshotRequest(TeaModel):
    def __init__(
        self,
        force: bool = None,
        region_id: str = None,
        snapshot_id: str = None,
    ):
        self.force = force
        self.region_id = region_id
        self.snapshot_id = snapshot_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.force is not None:
            result['Force'] = self.force
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Force') is not None:
            self.force = m.get('Force')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        return self


class DeleteSnapshotResponseBody(TeaModel):
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


class DeleteSnapshotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteSnapshotResponseBody = None,
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
            temp_model = DeleteSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTagsBatchRequest(TeaModel):
    def __init__(
        self,
        dbfs_list: str = None,
        region_id: str = None,
        tags: str = None,
    ):
        self.dbfs_list = dbfs_list
        self.region_id = region_id
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbfs_list is not None:
            result['DbfsList'] = self.dbfs_list
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbfsList') is not None:
            self.dbfs_list = m.get('DbfsList')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class DeleteTagsBatchResponseBody(TeaModel):
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


class DeleteTagsBatchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteTagsBatchResponseBody = None,
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
            temp_model = DeleteTagsBatchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDbfsSpecificationsRequest(TeaModel):
    def __init__(
        self,
        category: str = None,
        ecs_instance_type: str = None,
        region_id: str = None,
    ):
        self.category = category
        self.ecs_instance_type = ecs_instance_type
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.ecs_instance_type is not None:
            result['EcsInstanceType'] = self.ecs_instance_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('EcsInstanceType') is not None:
            self.ecs_instance_type = m.get('EcsInstanceType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDbfsSpecificationsResponseBody(TeaModel):
    def __init__(
        self,
        max_dbfs_number_per_ecs: Dict[str, Any] = None,
        request_id: str = None,
        supported_ecs_instance_type_family: List[str] = None,
    ):
        self.max_dbfs_number_per_ecs = max_dbfs_number_per_ecs
        self.request_id = request_id
        self.supported_ecs_instance_type_family = supported_ecs_instance_type_family

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_dbfs_number_per_ecs is not None:
            result['MaxDbfsNumberPerEcs'] = self.max_dbfs_number_per_ecs
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.supported_ecs_instance_type_family is not None:
            result['SupportedEcsInstanceTypeFamily'] = self.supported_ecs_instance_type_family
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxDbfsNumberPerEcs') is not None:
            self.max_dbfs_number_per_ecs = m.get('MaxDbfsNumberPerEcs')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SupportedEcsInstanceTypeFamily') is not None:
            self.supported_ecs_instance_type_family = m.get('SupportedEcsInstanceTypeFamily')
        return self


class DescribeDbfsSpecificationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDbfsSpecificationsResponseBody = None,
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
            temp_model = DescribeDbfsSpecificationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceTypesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        # 地域ID
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


class DescribeInstanceTypesResponseBodyInstanceTypes(TeaModel):
    def __init__(
        self,
        cpu_core_count: float = None,
        instance_type_description: str = None,
        instance_type_id: str = None,
        memory_size: float = None,
    ):
        self.cpu_core_count = cpu_core_count
        self.instance_type_description = instance_type_description
        self.instance_type_id = instance_type_id
        self.memory_size = memory_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_core_count is not None:
            result['CpuCoreCount'] = self.cpu_core_count
        if self.instance_type_description is not None:
            result['InstanceTypeDescription'] = self.instance_type_description
        if self.instance_type_id is not None:
            result['InstanceTypeId'] = self.instance_type_id
        if self.memory_size is not None:
            result['MemorySize'] = self.memory_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuCoreCount') is not None:
            self.cpu_core_count = m.get('CpuCoreCount')
        if m.get('InstanceTypeDescription') is not None:
            self.instance_type_description = m.get('InstanceTypeDescription')
        if m.get('InstanceTypeId') is not None:
            self.instance_type_id = m.get('InstanceTypeId')
        if m.get('MemorySize') is not None:
            self.memory_size = m.get('MemorySize')
        return self


class DescribeInstanceTypesResponseBody(TeaModel):
    def __init__(
        self,
        instance_types: List[DescribeInstanceTypesResponseBodyInstanceTypes] = None,
        request_id: str = None,
    ):
        # Array of InstanceType
        self.instance_types = instance_types
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.instance_types:
            for k in self.instance_types:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceTypes'] = []
        if self.instance_types is not None:
            for k in self.instance_types:
                result['InstanceTypes'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_types = []
        if m.get('InstanceTypes') is not None:
            for k in m.get('InstanceTypes'):
                temp_model = DescribeInstanceTypesResponseBodyInstanceTypes()
                self.instance_types.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeInstanceTypesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeInstanceTypesResponseBody = None,
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
            temp_model = DescribeInstanceTypesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachDbfsRequest(TeaModel):
    def __init__(
        self,
        ecsinstance_id: str = None,
        fs_id: str = None,
        region_id: str = None,
    ):
        self.ecsinstance_id = ecsinstance_id
        self.fs_id = fs_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ecsinstance_id is not None:
            result['ECSInstanceId'] = self.ecsinstance_id
        if self.fs_id is not None:
            result['FsId'] = self.fs_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ECSInstanceId') is not None:
            self.ecsinstance_id = m.get('ECSInstanceId')
        if m.get('FsId') is not None:
            self.fs_id = m.get('FsId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DetachDbfsResponseBody(TeaModel):
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


class DetachDbfsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DetachDbfsResponseBody = None,
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
            temp_model = DetachDbfsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDbfsRequest(TeaModel):
    def __init__(
        self,
        fs_id: str = None,
        region_id: str = None,
    ):
        self.fs_id = fs_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fs_id is not None:
            result['FsId'] = self.fs_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FsId') is not None:
            self.fs_id = m.get('FsId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetDbfsResponseBodyDBFSInfoEbsList(TeaModel):
    def __init__(
        self,
        ebs_id: str = None,
        size_g: int = None,
    ):
        self.ebs_id = ebs_id
        self.size_g = size_g

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ebs_id is not None:
            result['EbsId'] = self.ebs_id
        if self.size_g is not None:
            result['SizeG'] = self.size_g
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EbsId') is not None:
            self.ebs_id = m.get('EbsId')
        if m.get('SizeG') is not None:
            self.size_g = m.get('SizeG')
        return self


class GetDbfsResponseBodyDBFSInfoEcsList(TeaModel):
    def __init__(
        self,
        ecs_id: str = None,
    ):
        self.ecs_id = ecs_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ecs_id is not None:
            result['EcsId'] = self.ecs_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EcsId') is not None:
            self.ecs_id = m.get('EcsId')
        return self


class GetDbfsResponseBodyDBFSInfoTags(TeaModel):
    def __init__(
        self,
        id: int = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.id = id
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class GetDbfsResponseBodyDBFSInfo(TeaModel):
    def __init__(
        self,
        attach_node_number: int = None,
        category: str = None,
        created_time: str = None,
        dbfscluster_id: str = None,
        description: str = None,
        ebs_list: List[GetDbfsResponseBodyDBFSInfoEbsList] = None,
        ecs_list: List[GetDbfsResponseBodyDBFSInfoEcsList] = None,
        enable_raid: bool = None,
        encryption: bool = None,
        fs_id: str = None,
        fs_name: str = None,
        instance_type: str = None,
        kmskey_id: str = None,
        last_mount_time: str = None,
        last_umount_time: str = None,
        pay_type: str = None,
        performance_level: str = None,
        raid_strip: int = None,
        region_id: str = None,
        size_g: int = None,
        status: str = None,
        tags: List[GetDbfsResponseBodyDBFSInfoTags] = None,
        used_scene: str = None,
        zone_id: str = None,
    ):
        self.attach_node_number = attach_node_number
        self.category = category
        self.created_time = created_time
        self.dbfscluster_id = dbfscluster_id
        self.description = description
        self.ebs_list = ebs_list
        self.ecs_list = ecs_list
        self.enable_raid = enable_raid
        self.encryption = encryption
        self.fs_id = fs_id
        self.fs_name = fs_name
        self.instance_type = instance_type
        self.kmskey_id = kmskey_id
        self.last_mount_time = last_mount_time
        self.last_umount_time = last_umount_time
        self.pay_type = pay_type
        self.performance_level = performance_level
        self.raid_strip = raid_strip
        self.region_id = region_id
        self.size_g = size_g
        self.status = status
        self.tags = tags
        self.used_scene = used_scene
        self.zone_id = zone_id

    def validate(self):
        if self.ebs_list:
            for k in self.ebs_list:
                if k:
                    k.validate()
        if self.ecs_list:
            for k in self.ecs_list:
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
        if self.attach_node_number is not None:
            result['AttachNodeNumber'] = self.attach_node_number
        if self.category is not None:
            result['Category'] = self.category
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.dbfscluster_id is not None:
            result['DBFSClusterId'] = self.dbfscluster_id
        if self.description is not None:
            result['Description'] = self.description
        result['EbsList'] = []
        if self.ebs_list is not None:
            for k in self.ebs_list:
                result['EbsList'].append(k.to_map() if k else None)
        result['EcsList'] = []
        if self.ecs_list is not None:
            for k in self.ecs_list:
                result['EcsList'].append(k.to_map() if k else None)
        if self.enable_raid is not None:
            result['EnableRaid'] = self.enable_raid
        if self.encryption is not None:
            result['Encryption'] = self.encryption
        if self.fs_id is not None:
            result['FsId'] = self.fs_id
        if self.fs_name is not None:
            result['FsName'] = self.fs_name
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.kmskey_id is not None:
            result['KMSKeyId'] = self.kmskey_id
        if self.last_mount_time is not None:
            result['LastMountTime'] = self.last_mount_time
        if self.last_umount_time is not None:
            result['LastUmountTime'] = self.last_umount_time
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level
        if self.raid_strip is not None:
            result['RaidStrip'] = self.raid_strip
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.size_g is not None:
            result['SizeG'] = self.size_g
        if self.status is not None:
            result['Status'] = self.status
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.used_scene is not None:
            result['UsedScene'] = self.used_scene
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachNodeNumber') is not None:
            self.attach_node_number = m.get('AttachNodeNumber')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('DBFSClusterId') is not None:
            self.dbfscluster_id = m.get('DBFSClusterId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.ebs_list = []
        if m.get('EbsList') is not None:
            for k in m.get('EbsList'):
                temp_model = GetDbfsResponseBodyDBFSInfoEbsList()
                self.ebs_list.append(temp_model.from_map(k))
        self.ecs_list = []
        if m.get('EcsList') is not None:
            for k in m.get('EcsList'):
                temp_model = GetDbfsResponseBodyDBFSInfoEcsList()
                self.ecs_list.append(temp_model.from_map(k))
        if m.get('EnableRaid') is not None:
            self.enable_raid = m.get('EnableRaid')
        if m.get('Encryption') is not None:
            self.encryption = m.get('Encryption')
        if m.get('FsId') is not None:
            self.fs_id = m.get('FsId')
        if m.get('FsName') is not None:
            self.fs_name = m.get('FsName')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('KMSKeyId') is not None:
            self.kmskey_id = m.get('KMSKeyId')
        if m.get('LastMountTime') is not None:
            self.last_mount_time = m.get('LastMountTime')
        if m.get('LastUmountTime') is not None:
            self.last_umount_time = m.get('LastUmountTime')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')
        if m.get('RaidStrip') is not None:
            self.raid_strip = m.get('RaidStrip')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SizeG') is not None:
            self.size_g = m.get('SizeG')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = GetDbfsResponseBodyDBFSInfoTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('UsedScene') is not None:
            self.used_scene = m.get('UsedScene')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class GetDbfsResponseBody(TeaModel):
    def __init__(
        self,
        dbfsinfo: GetDbfsResponseBodyDBFSInfo = None,
        request_id: str = None,
    ):
        self.dbfsinfo = dbfsinfo
        self.request_id = request_id

    def validate(self):
        if self.dbfsinfo:
            self.dbfsinfo.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbfsinfo is not None:
            result['DBFSInfo'] = self.dbfsinfo.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBFSInfo') is not None:
            temp_model = GetDbfsResponseBodyDBFSInfo()
            self.dbfsinfo = temp_model.from_map(m['DBFSInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDbfsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDbfsResponseBody = None,
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
            temp_model = GetDbfsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceLinkedRoleRequest(TeaModel):
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


class GetServiceLinkedRoleResponseBody(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        dbfs_linked_role: bool = None,
        region_id: str = None,
        request_id: str = None,
    ):
        self.account_id = account_id
        self.dbfs_linked_role = dbfs_linked_role
        self.region_id = region_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.dbfs_linked_role is not None:
            result['DbfsLinkedRole'] = self.dbfs_linked_role
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('DbfsLinkedRole') is not None:
            self.dbfs_linked_role = m.get('DbfsLinkedRole')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetServiceLinkedRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetServiceLinkedRoleResponseBody = None,
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
            temp_model = GetServiceLinkedRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDbfsRequest(TeaModel):
    def __init__(
        self,
        filter_key: str = None,
        filter_value: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        sort_key: str = None,
        sort_type: str = None,
        tags: str = None,
    ):
        self.filter_key = filter_key
        self.filter_value = filter_value
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.sort_key = sort_key
        self.sort_type = sort_type
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter_key is not None:
            result['FilterKey'] = self.filter_key
        if self.filter_value is not None:
            result['FilterValue'] = self.filter_value
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sort_key is not None:
            result['SortKey'] = self.sort_key
        if self.sort_type is not None:
            result['SortType'] = self.sort_type
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilterKey') is not None:
            self.filter_key = m.get('FilterKey')
        if m.get('FilterValue') is not None:
            self.filter_value = m.get('FilterValue')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SortKey') is not None:
            self.sort_key = m.get('SortKey')
        if m.get('SortType') is not None:
            self.sort_type = m.get('SortType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class ListDbfsResponseBodyDBFSInfoEbsList(TeaModel):
    def __init__(
        self,
        ebs_id: str = None,
        size_g: int = None,
    ):
        self.ebs_id = ebs_id
        self.size_g = size_g

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ebs_id is not None:
            result['EbsId'] = self.ebs_id
        if self.size_g is not None:
            result['SizeG'] = self.size_g
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EbsId') is not None:
            self.ebs_id = m.get('EbsId')
        if m.get('SizeG') is not None:
            self.size_g = m.get('SizeG')
        return self


class ListDbfsResponseBodyDBFSInfoEcsList(TeaModel):
    def __init__(
        self,
        ecs_id: str = None,
    ):
        self.ecs_id = ecs_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ecs_id is not None:
            result['EcsId'] = self.ecs_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EcsId') is not None:
            self.ecs_id = m.get('EcsId')
        return self


class ListDbfsResponseBodyDBFSInfoTags(TeaModel):
    def __init__(
        self,
        id: int = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.id = id
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListDbfsResponseBodyDBFSInfo(TeaModel):
    def __init__(
        self,
        attach_node_number: int = None,
        category: str = None,
        created_time: str = None,
        dbfscluster_id: str = None,
        ebs_list: List[ListDbfsResponseBodyDBFSInfoEbsList] = None,
        ecs_list: List[ListDbfsResponseBodyDBFSInfoEcsList] = None,
        enable_raid: bool = None,
        encryption: bool = None,
        fs_id: str = None,
        fs_name: str = None,
        instance_type: str = None,
        kmskey_id: str = None,
        last_mount_time: str = None,
        last_umount_time: str = None,
        pay_type: str = None,
        performance_level: str = None,
        raid_strip: int = None,
        region_id: str = None,
        size_g: int = None,
        status: str = None,
        tags: List[ListDbfsResponseBodyDBFSInfoTags] = None,
        used_scene: str = None,
        zone_id: str = None,
    ):
        self.attach_node_number = attach_node_number
        self.category = category
        self.created_time = created_time
        self.dbfscluster_id = dbfscluster_id
        self.ebs_list = ebs_list
        self.ecs_list = ecs_list
        self.enable_raid = enable_raid
        self.encryption = encryption
        self.fs_id = fs_id
        self.fs_name = fs_name
        self.instance_type = instance_type
        self.kmskey_id = kmskey_id
        self.last_mount_time = last_mount_time
        self.last_umount_time = last_umount_time
        self.pay_type = pay_type
        self.performance_level = performance_level
        self.raid_strip = raid_strip
        self.region_id = region_id
        self.size_g = size_g
        self.status = status
        self.tags = tags
        self.used_scene = used_scene
        self.zone_id = zone_id

    def validate(self):
        if self.ebs_list:
            for k in self.ebs_list:
                if k:
                    k.validate()
        if self.ecs_list:
            for k in self.ecs_list:
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
        if self.attach_node_number is not None:
            result['AttachNodeNumber'] = self.attach_node_number
        if self.category is not None:
            result['Category'] = self.category
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.dbfscluster_id is not None:
            result['DBFSClusterId'] = self.dbfscluster_id
        result['EbsList'] = []
        if self.ebs_list is not None:
            for k in self.ebs_list:
                result['EbsList'].append(k.to_map() if k else None)
        result['EcsList'] = []
        if self.ecs_list is not None:
            for k in self.ecs_list:
                result['EcsList'].append(k.to_map() if k else None)
        if self.enable_raid is not None:
            result['EnableRaid'] = self.enable_raid
        if self.encryption is not None:
            result['Encryption'] = self.encryption
        if self.fs_id is not None:
            result['FsId'] = self.fs_id
        if self.fs_name is not None:
            result['FsName'] = self.fs_name
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.kmskey_id is not None:
            result['KMSKeyId'] = self.kmskey_id
        if self.last_mount_time is not None:
            result['LastMountTime'] = self.last_mount_time
        if self.last_umount_time is not None:
            result['LastUmountTime'] = self.last_umount_time
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level
        if self.raid_strip is not None:
            result['RaidStrip'] = self.raid_strip
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.size_g is not None:
            result['SizeG'] = self.size_g
        if self.status is not None:
            result['Status'] = self.status
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.used_scene is not None:
            result['UsedScene'] = self.used_scene
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachNodeNumber') is not None:
            self.attach_node_number = m.get('AttachNodeNumber')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('DBFSClusterId') is not None:
            self.dbfscluster_id = m.get('DBFSClusterId')
        self.ebs_list = []
        if m.get('EbsList') is not None:
            for k in m.get('EbsList'):
                temp_model = ListDbfsResponseBodyDBFSInfoEbsList()
                self.ebs_list.append(temp_model.from_map(k))
        self.ecs_list = []
        if m.get('EcsList') is not None:
            for k in m.get('EcsList'):
                temp_model = ListDbfsResponseBodyDBFSInfoEcsList()
                self.ecs_list.append(temp_model.from_map(k))
        if m.get('EnableRaid') is not None:
            self.enable_raid = m.get('EnableRaid')
        if m.get('Encryption') is not None:
            self.encryption = m.get('Encryption')
        if m.get('FsId') is not None:
            self.fs_id = m.get('FsId')
        if m.get('FsName') is not None:
            self.fs_name = m.get('FsName')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('KMSKeyId') is not None:
            self.kmskey_id = m.get('KMSKeyId')
        if m.get('LastMountTime') is not None:
            self.last_mount_time = m.get('LastMountTime')
        if m.get('LastUmountTime') is not None:
            self.last_umount_time = m.get('LastUmountTime')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')
        if m.get('RaidStrip') is not None:
            self.raid_strip = m.get('RaidStrip')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SizeG') is not None:
            self.size_g = m.get('SizeG')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListDbfsResponseBodyDBFSInfoTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('UsedScene') is not None:
            self.used_scene = m.get('UsedScene')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListDbfsResponseBody(TeaModel):
    def __init__(
        self,
        dbfsinfo: List[ListDbfsResponseBodyDBFSInfo] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.dbfsinfo = dbfsinfo
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.dbfsinfo:
            for k in self.dbfsinfo:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DBFSInfo'] = []
        if self.dbfsinfo is not None:
            for k in self.dbfsinfo:
                result['DBFSInfo'].append(k.to_map() if k else None)
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
        self.dbfsinfo = []
        if m.get('DBFSInfo') is not None:
            for k in m.get('DBFSInfo'):
                temp_model = ListDbfsResponseBodyDBFSInfo()
                self.dbfsinfo.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDbfsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDbfsResponseBody = None,
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
            temp_model = ListDbfsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDbfsAttachableEcsInstancesRequest(TeaModel):
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


class ListDbfsAttachableEcsInstancesResponseBodyEcsLabelInfo(TeaModel):
    def __init__(
        self,
        label: str = None,
        value: str = None,
    ):
        self.label = label
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['label'] = self.label
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('label') is not None:
            self.label = m.get('label')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ListDbfsAttachableEcsInstancesResponseBody(TeaModel):
    def __init__(
        self,
        ecs_label_info: List[ListDbfsAttachableEcsInstancesResponseBodyEcsLabelInfo] = None,
        request_id: str = None,
    ):
        self.ecs_label_info = ecs_label_info
        self.request_id = request_id

    def validate(self):
        if self.ecs_label_info:
            for k in self.ecs_label_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EcsLabelInfo'] = []
        if self.ecs_label_info is not None:
            for k in self.ecs_label_info:
                result['EcsLabelInfo'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ecs_label_info = []
        if m.get('EcsLabelInfo') is not None:
            for k in m.get('EcsLabelInfo'):
                temp_model = ListDbfsAttachableEcsInstancesResponseBodyEcsLabelInfo()
                self.ecs_label_info.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDbfsAttachableEcsInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDbfsAttachableEcsInstancesResponseBody = None,
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
            temp_model = ListDbfsAttachableEcsInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDbfsAttachedEcsInstancesRequest(TeaModel):
    def __init__(
        self,
        fs_id: str = None,
        region_id: str = None,
    ):
        self.fs_id = fs_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fs_id is not None:
            result['FsId'] = self.fs_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FsId') is not None:
            self.fs_id = m.get('FsId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListDbfsAttachedEcsInstancesResponseBodyEcsLabelInfo(TeaModel):
    def __init__(
        self,
        mount_point: str = None,
        mounted_time: str = None,
        label: str = None,
        value: str = None,
    ):
        self.mount_point = mount_point
        self.mounted_time = mounted_time
        self.label = label
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mount_point is not None:
            result['MountPoint'] = self.mount_point
        if self.mounted_time is not None:
            result['MountedTime'] = self.mounted_time
        if self.label is not None:
            result['label'] = self.label
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MountPoint') is not None:
            self.mount_point = m.get('MountPoint')
        if m.get('MountedTime') is not None:
            self.mounted_time = m.get('MountedTime')
        if m.get('label') is not None:
            self.label = m.get('label')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ListDbfsAttachedEcsInstancesResponseBody(TeaModel):
    def __init__(
        self,
        ecs_label_info: List[ListDbfsAttachedEcsInstancesResponseBodyEcsLabelInfo] = None,
        request_id: str = None,
    ):
        self.ecs_label_info = ecs_label_info
        self.request_id = request_id

    def validate(self):
        if self.ecs_label_info:
            for k in self.ecs_label_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EcsLabelInfo'] = []
        if self.ecs_label_info is not None:
            for k in self.ecs_label_info:
                result['EcsLabelInfo'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ecs_label_info = []
        if m.get('EcsLabelInfo') is not None:
            for k in m.get('EcsLabelInfo'):
                temp_model = ListDbfsAttachedEcsInstancesResponseBodyEcsLabelInfo()
                self.ecs_label_info.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDbfsAttachedEcsInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDbfsAttachedEcsInstancesResponseBody = None,
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
            temp_model = ListDbfsAttachedEcsInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSnapshotRequest(TeaModel):
    def __init__(
        self,
        filter_key: str = None,
        filter_value: str = None,
        fs_id: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        snapshot_ids: str = None,
        snapshot_name: str = None,
        snapshot_type: str = None,
        sort_key: str = None,
        sort_type: str = None,
        status: str = None,
    ):
        self.filter_key = filter_key
        self.filter_value = filter_value
        self.fs_id = fs_id
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.snapshot_ids = snapshot_ids
        self.snapshot_name = snapshot_name
        self.snapshot_type = snapshot_type
        self.sort_key = sort_key
        self.sort_type = sort_type
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter_key is not None:
            result['FilterKey'] = self.filter_key
        if self.filter_value is not None:
            result['FilterValue'] = self.filter_value
        if self.fs_id is not None:
            result['FsId'] = self.fs_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.snapshot_ids is not None:
            result['SnapshotIds'] = self.snapshot_ids
        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name
        if self.snapshot_type is not None:
            result['SnapshotType'] = self.snapshot_type
        if self.sort_key is not None:
            result['SortKey'] = self.sort_key
        if self.sort_type is not None:
            result['SortType'] = self.sort_type
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilterKey') is not None:
            self.filter_key = m.get('FilterKey')
        if m.get('FilterValue') is not None:
            self.filter_value = m.get('FilterValue')
        if m.get('FsId') is not None:
            self.fs_id = m.get('FsId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SnapshotIds') is not None:
            self.snapshot_ids = m.get('SnapshotIds')
        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')
        if m.get('SnapshotType') is not None:
            self.snapshot_type = m.get('SnapshotType')
        if m.get('SortKey') is not None:
            self.sort_key = m.get('SortKey')
        if m.get('SortType') is not None:
            self.sort_type = m.get('SortType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListSnapshotResponseBodySnapshots(TeaModel):
    def __init__(
        self,
        category: str = None,
        creation_time: str = None,
        description: str = None,
        last_modified_time: str = None,
        progress: str = None,
        remain_time: int = None,
        retention_days: int = None,
        snapshot_id: str = None,
        snapshot_name: str = None,
        snapshot_type: str = None,
        source_fs_id: str = None,
        source_fs_size: int = None,
        status: str = None,
    ):
        self.category = category
        self.creation_time = creation_time
        self.description = description
        self.last_modified_time = last_modified_time
        self.progress = progress
        self.remain_time = remain_time
        self.retention_days = retention_days
        self.snapshot_id = snapshot_id
        self.snapshot_name = snapshot_name
        self.snapshot_type = snapshot_type
        self.source_fs_id = source_fs_id
        self.source_fs_size = source_fs_size
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.description is not None:
            result['Description'] = self.description
        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.remain_time is not None:
            result['RemainTime'] = self.remain_time
        if self.retention_days is not None:
            result['RetentionDays'] = self.retention_days
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name
        if self.snapshot_type is not None:
            result['SnapshotType'] = self.snapshot_type
        if self.source_fs_id is not None:
            result['SourceFsId'] = self.source_fs_id
        if self.source_fs_size is not None:
            result['SourceFsSize'] = self.source_fs_size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RemainTime') is not None:
            self.remain_time = m.get('RemainTime')
        if m.get('RetentionDays') is not None:
            self.retention_days = m.get('RetentionDays')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')
        if m.get('SnapshotType') is not None:
            self.snapshot_type = m.get('SnapshotType')
        if m.get('SourceFsId') is not None:
            self.source_fs_id = m.get('SourceFsId')
        if m.get('SourceFsSize') is not None:
            self.source_fs_size = m.get('SourceFsSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListSnapshotResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        snapshots: List[ListSnapshotResponseBodySnapshots] = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.snapshots = snapshots
        self.total_count = total_count

    def validate(self):
        if self.snapshots:
            for k in self.snapshots:
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
        result['Snapshots'] = []
        if self.snapshots is not None:
            for k in self.snapshots:
                result['Snapshots'].append(k.to_map() if k else None)
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
        self.snapshots = []
        if m.get('Snapshots') is not None:
            for k in m.get('Snapshots'):
                temp_model = ListSnapshotResponseBodySnapshots()
                self.snapshots.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListSnapshotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSnapshotResponseBody = None,
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
            temp_model = ListSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagKeysRequest(TeaModel):
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


class ListTagKeysResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tag_keys: List[str] = None,
    ):
        self.request_id = request_id
        self.tag_keys = tag_keys

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_keys is not None:
            result['TagKeys'] = self.tag_keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagKeys') is not None:
            self.tag_keys = m.get('TagKeys')
        return self


class ListTagKeysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTagKeysResponseBody = None,
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
            temp_model = ListTagKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagValuesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        tag_key: str = None,
    ):
        self.region_id = region_id
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class ListTagValuesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tag_values: List[str] = None,
    ):
        self.request_id = request_id
        self.tag_values = tag_values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_values is not None:
            result['TagValues'] = self.tag_values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagValues') is not None:
            self.tag_values = m.get('TagValues')
        return self


class ListTagValuesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTagValuesResponseBody = None,
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
            temp_model = ListTagValuesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenameDbfsRequest(TeaModel):
    def __init__(
        self,
        fs_id: str = None,
        fs_name: str = None,
        region_id: str = None,
    ):
        self.fs_id = fs_id
        self.fs_name = fs_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fs_id is not None:
            result['FsId'] = self.fs_id
        if self.fs_name is not None:
            result['FsName'] = self.fs_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FsId') is not None:
            self.fs_id = m.get('FsId')
        if m.get('FsName') is not None:
            self.fs_name = m.get('FsName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class RenameDbfsResponseBody(TeaModel):
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


class RenameDbfsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RenameDbfsResponseBody = None,
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
            temp_model = RenameDbfsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetDbfsRequest(TeaModel):
    def __init__(
        self,
        fs_id: str = None,
        region_id: str = None,
        snapshot_id: str = None,
    ):
        self.fs_id = fs_id
        self.region_id = region_id
        self.snapshot_id = snapshot_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fs_id is not None:
            result['FsId'] = self.fs_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FsId') is not None:
            self.fs_id = m.get('FsId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        return self


class ResetDbfsResponseBody(TeaModel):
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


class ResetDbfsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ResetDbfsResponseBody = None,
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
            temp_model = ResetDbfsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResizeDbfsRequest(TeaModel):
    def __init__(
        self,
        fs_id: str = None,
        new_size_g: int = None,
        region_id: str = None,
    ):
        self.fs_id = fs_id
        self.new_size_g = new_size_g
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fs_id is not None:
            result['FsId'] = self.fs_id
        if self.new_size_g is not None:
            result['NewSizeG'] = self.new_size_g
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FsId') is not None:
            self.fs_id = m.get('FsId')
        if m.get('NewSizeG') is not None:
            self.new_size_g = m.get('NewSizeG')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ResizeDbfsResponseBody(TeaModel):
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


class ResizeDbfsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ResizeDbfsResponseBody = None,
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
            temp_model = ResizeDbfsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagDbfsRequest(TeaModel):
    def __init__(
        self,
        dbfs_id: str = None,
        region_id: str = None,
        tags: str = None,
    ):
        self.dbfs_id = dbfs_id
        self.region_id = region_id
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbfs_id is not None:
            result['DbfsId'] = self.dbfs_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbfsId') is not None:
            self.dbfs_id = m.get('DbfsId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class TagDbfsResponseBody(TeaModel):
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


class TagDbfsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: TagDbfsResponseBody = None,
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
            temp_model = TagDbfsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


