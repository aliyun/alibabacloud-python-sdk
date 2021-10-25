# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class CreateConstantsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        page_number: int = None,
        page_size: int = None,
        constants_data: str = None,
    ):
        self.region_id = region_id
        self.page_number = page_number
        self.page_size = page_size
        self.constants_data = constants_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.constants_data is not None:
            result['ConstantsData'] = self.constants_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ConstantsData') is not None:
            self.constants_data = m.get('ConstantsData')
        return self


class CreateConstantsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
        page_size: int = None,
        total_count: int = None,
        page_number: int = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.data = data
        self.page_size = page_size
        self.total_count = total_count
        self.page_number = page_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class CreateConstantsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateConstantsResponseBody = None,
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
            temp_model = CreateConstantsResponseBody()
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


class DeleteConstantsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        page_number: int = None,
        page_size: int = None,
        constants_data: str = None,
    ):
        self.region_id = region_id
        self.page_number = page_number
        self.page_size = page_size
        self.constants_data = constants_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.constants_data is not None:
            result['ConstantsData'] = self.constants_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ConstantsData') is not None:
            self.constants_data = m.get('ConstantsData')
        return self


class DeleteConstantsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
        page_size: int = None,
        total_count: int = None,
        page_number: int = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.data = data
        self.page_size = page_size
        self.total_count = total_count
        self.page_number = page_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DeleteConstantsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteConstantsResponseBody = None,
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
            temp_model = DeleteConstantsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceLinkedRoleRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        client_token: str = None,
    ):
        self.region_id = region_id
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
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


class ResizeDbfsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        fs_id: str = None,
        new_size_g: int = None,
    ):
        self.region_id = region_id
        self.fs_id = fs_id
        self.new_size_g = new_size_g

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.fs_id is not None:
            result['FsId'] = self.fs_id
        if self.new_size_g is not None:
            result['NewSizeG'] = self.new_size_g
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('FsId') is not None:
            self.fs_id = m.get('FsId')
        if m.get('NewSizeG') is not None:
            self.new_size_g = m.get('NewSizeG')
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


class PublishUpgradeTaskRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        page_number: int = None,
        page_size: int = None,
        batch_strategy_list: str = None,
    ):
        self.region_id = region_id
        self.page_number = page_number
        self.page_size = page_size
        self.batch_strategy_list = batch_strategy_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.batch_strategy_list is not None:
            result['BatchStrategyList'] = self.batch_strategy_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('BatchStrategyList') is not None:
            self.batch_strategy_list = m.get('BatchStrategyList')
        return self


class PublishUpgradeTaskResponseBody(TeaModel):
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


class PublishUpgradeTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PublishUpgradeTaskResponseBody = None,
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
            temp_model = PublishUpgradeTaskResponseBody()
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


class DeleteSnapshotRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        snapshot_id: str = None,
        force: bool = None,
    ):
        self.region_id = region_id
        self.snapshot_id = snapshot_id
        self.force = force

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.force is not None:
            result['Force'] = self.force
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('Force') is not None:
            self.force = m.get('Force')
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


class DetachDbfsRequest(TeaModel):
    def __init__(
        self,
        fs_id: str = None,
        ecsinstance_id: str = None,
        region_id: str = None,
    ):
        self.fs_id = fs_id
        self.ecsinstance_id = ecsinstance_id
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
        if self.ecsinstance_id is not None:
            result['ECSInstanceId'] = self.ecsinstance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FsId') is not None:
            self.fs_id = m.get('FsId')
        if m.get('ECSInstanceId') is not None:
            self.ecsinstance_id = m.get('ECSInstanceId')
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


class GenerateUpgradeRecordRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        page_number: int = None,
        page_size: int = None,
        batch_strategy_list: str = None,
    ):
        self.region_id = region_id
        self.page_number = page_number
        self.page_size = page_size
        self.batch_strategy_list = batch_strategy_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.batch_strategy_list is not None:
            result['BatchStrategyList'] = self.batch_strategy_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('BatchStrategyList') is not None:
            self.batch_strategy_list = m.get('BatchStrategyList')
        return self


class GenerateUpgradeRecordResponseBodyRecords(TeaModel):
    def __init__(
        self,
        id: int = None,
        batch_strategy_no: str = None,
        account_id: str = None,
        dbfs_id: str = None,
        ecs_id: str = None,
        task_id: str = None,
        region_id: str = None,
        zone_id: str = None,
        state: str = None,
        current_version: str = None,
        target_version: str = None,
        upgrade_start_time: int = None,
        upgrade_end_time: int = None,
        task_execution_counts: int = None,
        task_error_reason: str = None,
        create_time: int = None,
        update_time: int = None,
    ):
        self.id = id
        self.batch_strategy_no = batch_strategy_no
        self.account_id = account_id
        self.dbfs_id = dbfs_id
        self.ecs_id = ecs_id
        self.task_id = task_id
        self.region_id = region_id
        self.zone_id = zone_id
        self.state = state
        self.current_version = current_version
        self.target_version = target_version
        self.upgrade_start_time = upgrade_start_time
        self.upgrade_end_time = upgrade_end_time
        self.task_execution_counts = task_execution_counts
        self.task_error_reason = task_error_reason
        self.create_time = create_time
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.batch_strategy_no is not None:
            result['BatchStrategyNo'] = self.batch_strategy_no
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.dbfs_id is not None:
            result['DbfsId'] = self.dbfs_id
        if self.ecs_id is not None:
            result['EcsId'] = self.ecs_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.state is not None:
            result['State'] = self.state
        if self.current_version is not None:
            result['CurrentVersion'] = self.current_version
        if self.target_version is not None:
            result['TargetVersion'] = self.target_version
        if self.upgrade_start_time is not None:
            result['UpgradeStartTime'] = self.upgrade_start_time
        if self.upgrade_end_time is not None:
            result['UpgradeEndTime'] = self.upgrade_end_time
        if self.task_execution_counts is not None:
            result['TaskExecutionCounts'] = self.task_execution_counts
        if self.task_error_reason is not None:
            result['TaskErrorReason'] = self.task_error_reason
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('BatchStrategyNo') is not None:
            self.batch_strategy_no = m.get('BatchStrategyNo')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('DbfsId') is not None:
            self.dbfs_id = m.get('DbfsId')
        if m.get('EcsId') is not None:
            self.ecs_id = m.get('EcsId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('CurrentVersion') is not None:
            self.current_version = m.get('CurrentVersion')
        if m.get('TargetVersion') is not None:
            self.target_version = m.get('TargetVersion')
        if m.get('UpgradeStartTime') is not None:
            self.upgrade_start_time = m.get('UpgradeStartTime')
        if m.get('UpgradeEndTime') is not None:
            self.upgrade_end_time = m.get('UpgradeEndTime')
        if m.get('TaskExecutionCounts') is not None:
            self.task_execution_counts = m.get('TaskExecutionCounts')
        if m.get('TaskErrorReason') is not None:
            self.task_error_reason = m.get('TaskErrorReason')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class GenerateUpgradeRecordResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        records: List[GenerateUpgradeRecordResponseBodyRecords] = None,
    ):
        self.request_id = request_id
        self.records = records

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = GenerateUpgradeRecordResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        return self


class GenerateUpgradeRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GenerateUpgradeRecordResponseBody = None,
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
            temp_model = GenerateUpgradeRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetDbfsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        fs_id: str = None,
        snapshot_id: str = None,
    ):
        self.region_id = region_id
        self.fs_id = fs_id
        self.snapshot_id = snapshot_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.fs_id is not None:
            result['FsId'] = self.fs_id
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('FsId') is not None:
            self.fs_id = m.get('FsId')
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


class GetDbfsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        fs_id: str = None,
    ):
        self.region_id = region_id
        self.fs_id = fs_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.fs_id is not None:
            result['FsId'] = self.fs_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('FsId') is not None:
            self.fs_id = m.get('FsId')
        return self


class GetDbfsResponseBodyDBFSInfoTags(TeaModel):
    def __init__(
        self,
        tag_value: str = None,
        id: int = None,
        tag_key: str = None,
    ):
        self.tag_value = tag_value
        self.id = id
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        if self.id is not None:
            result['Id'] = self.id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
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


class GetDbfsResponseBodyDBFSInfo(TeaModel):
    def __init__(
        self,
        status: str = None,
        pay_type: str = None,
        fs_id: str = None,
        tags: List[GetDbfsResponseBodyDBFSInfoTags] = None,
        size_g: int = None,
        ecs_list: List[GetDbfsResponseBodyDBFSInfoEcsList] = None,
        region_id: str = None,
        dbfscluster_id: str = None,
        description: str = None,
        zone_id: str = None,
        fs_name: str = None,
        category: str = None,
        created_time: str = None,
        attach_node_number: int = None,
        kmskey_id: str = None,
        encryption: bool = None,
        performance_level: str = None,
        used_scene: str = None,
        last_mount_time: str = None,
        last_umount_time: str = None,
        enable_raid: bool = None,
        raid_strip: int = None,
        ebs_list: List[GetDbfsResponseBodyDBFSInfoEbsList] = None,
    ):
        self.status = status
        self.pay_type = pay_type
        self.fs_id = fs_id
        self.tags = tags
        self.size_g = size_g
        self.ecs_list = ecs_list
        self.region_id = region_id
        self.dbfscluster_id = dbfscluster_id
        self.description = description
        self.zone_id = zone_id
        self.fs_name = fs_name
        self.category = category
        self.created_time = created_time
        self.attach_node_number = attach_node_number
        self.kmskey_id = kmskey_id
        self.encryption = encryption
        self.performance_level = performance_level
        self.used_scene = used_scene
        self.last_mount_time = last_mount_time
        self.last_umount_time = last_umount_time
        self.enable_raid = enable_raid
        self.raid_strip = raid_strip
        self.ebs_list = ebs_list

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.ecs_list:
            for k in self.ecs_list:
                if k:
                    k.validate()
        if self.ebs_list:
            for k in self.ebs_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.fs_id is not None:
            result['FsId'] = self.fs_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.size_g is not None:
            result['SizeG'] = self.size_g
        result['EcsList'] = []
        if self.ecs_list is not None:
            for k in self.ecs_list:
                result['EcsList'].append(k.to_map() if k else None)
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dbfscluster_id is not None:
            result['DBFSClusterId'] = self.dbfscluster_id
        if self.description is not None:
            result['Description'] = self.description
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.fs_name is not None:
            result['FsName'] = self.fs_name
        if self.category is not None:
            result['Category'] = self.category
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.attach_node_number is not None:
            result['AttachNodeNumber'] = self.attach_node_number
        if self.kmskey_id is not None:
            result['KMSKeyId'] = self.kmskey_id
        if self.encryption is not None:
            result['Encryption'] = self.encryption
        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level
        if self.used_scene is not None:
            result['UsedScene'] = self.used_scene
        if self.last_mount_time is not None:
            result['LastMountTime'] = self.last_mount_time
        if self.last_umount_time is not None:
            result['LastUmountTime'] = self.last_umount_time
        if self.enable_raid is not None:
            result['EnableRaid'] = self.enable_raid
        if self.raid_strip is not None:
            result['RaidStrip'] = self.raid_strip
        result['EbsList'] = []
        if self.ebs_list is not None:
            for k in self.ebs_list:
                result['EbsList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('FsId') is not None:
            self.fs_id = m.get('FsId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = GetDbfsResponseBodyDBFSInfoTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('SizeG') is not None:
            self.size_g = m.get('SizeG')
        self.ecs_list = []
        if m.get('EcsList') is not None:
            for k in m.get('EcsList'):
                temp_model = GetDbfsResponseBodyDBFSInfoEcsList()
                self.ecs_list.append(temp_model.from_map(k))
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DBFSClusterId') is not None:
            self.dbfscluster_id = m.get('DBFSClusterId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('FsName') is not None:
            self.fs_name = m.get('FsName')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('AttachNodeNumber') is not None:
            self.attach_node_number = m.get('AttachNodeNumber')
        if m.get('KMSKeyId') is not None:
            self.kmskey_id = m.get('KMSKeyId')
        if m.get('Encryption') is not None:
            self.encryption = m.get('Encryption')
        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')
        if m.get('UsedScene') is not None:
            self.used_scene = m.get('UsedScene')
        if m.get('LastMountTime') is not None:
            self.last_mount_time = m.get('LastMountTime')
        if m.get('LastUmountTime') is not None:
            self.last_umount_time = m.get('LastUmountTime')
        if m.get('EnableRaid') is not None:
            self.enable_raid = m.get('EnableRaid')
        if m.get('RaidStrip') is not None:
            self.raid_strip = m.get('RaidStrip')
        self.ebs_list = []
        if m.get('EbsList') is not None:
            for k in m.get('EbsList'):
                temp_model = GetDbfsResponseBodyDBFSInfoEbsList()
                self.ebs_list.append(temp_model.from_map(k))
        return self


class GetDbfsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        dbfsinfo: GetDbfsResponseBodyDBFSInfo = None,
    ):
        self.request_id = request_id
        self.dbfsinfo = dbfsinfo

    def validate(self):
        if self.dbfsinfo:
            self.dbfsinfo.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.dbfsinfo is not None:
            result['DBFSInfo'] = self.dbfsinfo.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DBFSInfo') is not None:
            temp_model = GetDbfsResponseBodyDBFSInfo()
            self.dbfsinfo = temp_model.from_map(m['DBFSInfo'])
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


class DbfsRecordRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        page_number: int = None,
        page_size: int = None,
        data: str = None,
    ):
        self.region_id = region_id
        self.page_number = page_number
        self.page_size = page_size
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class DbfsRecordResponseBodyRecords(TeaModel):
    def __init__(
        self,
        id: int = None,
        batch_strategy_no: str = None,
        account_id: str = None,
        dbfs_id: str = None,
        ecs_id: str = None,
        task_id: str = None,
        region_id: str = None,
        zone_id: str = None,
        state: str = None,
        current_version: str = None,
        target_version: str = None,
        upgrade_start_time: int = None,
        upgrade_end_time: int = None,
        task_execution_counts: int = None,
        task_error_reason: str = None,
        create_time: int = None,
        update_time: int = None,
        is_del: str = None,
    ):
        self.id = id
        self.batch_strategy_no = batch_strategy_no
        self.account_id = account_id
        self.dbfs_id = dbfs_id
        self.ecs_id = ecs_id
        self.task_id = task_id
        self.region_id = region_id
        self.zone_id = zone_id
        self.state = state
        self.current_version = current_version
        self.target_version = target_version
        self.upgrade_start_time = upgrade_start_time
        self.upgrade_end_time = upgrade_end_time
        self.task_execution_counts = task_execution_counts
        self.task_error_reason = task_error_reason
        self.create_time = create_time
        self.update_time = update_time
        self.is_del = is_del

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.batch_strategy_no is not None:
            result['BatchStrategyNo'] = self.batch_strategy_no
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.dbfs_id is not None:
            result['DbfsId'] = self.dbfs_id
        if self.ecs_id is not None:
            result['EcsId'] = self.ecs_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.state is not None:
            result['State'] = self.state
        if self.current_version is not None:
            result['CurrentVersion'] = self.current_version
        if self.target_version is not None:
            result['TargetVersion'] = self.target_version
        if self.upgrade_start_time is not None:
            result['UpgradeStartTime'] = self.upgrade_start_time
        if self.upgrade_end_time is not None:
            result['UpgradeEndTime'] = self.upgrade_end_time
        if self.task_execution_counts is not None:
            result['TaskExecutionCounts'] = self.task_execution_counts
        if self.task_error_reason is not None:
            result['TaskErrorReason'] = self.task_error_reason
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.is_del is not None:
            result['IsDel'] = self.is_del
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('BatchStrategyNo') is not None:
            self.batch_strategy_no = m.get('BatchStrategyNo')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('DbfsId') is not None:
            self.dbfs_id = m.get('DbfsId')
        if m.get('EcsId') is not None:
            self.ecs_id = m.get('EcsId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('CurrentVersion') is not None:
            self.current_version = m.get('CurrentVersion')
        if m.get('TargetVersion') is not None:
            self.target_version = m.get('TargetVersion')
        if m.get('UpgradeStartTime') is not None:
            self.upgrade_start_time = m.get('UpgradeStartTime')
        if m.get('UpgradeEndTime') is not None:
            self.upgrade_end_time = m.get('UpgradeEndTime')
        if m.get('TaskExecutionCounts') is not None:
            self.task_execution_counts = m.get('TaskExecutionCounts')
        if m.get('TaskErrorReason') is not None:
            self.task_error_reason = m.get('TaskErrorReason')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('IsDel') is not None:
            self.is_del = m.get('IsDel')
        return self


class DbfsRecordResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        records: List[DbfsRecordResponseBodyRecords] = None,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.request_id = request_id
        self.records = records
        self.page_no = page_no
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = DbfsRecordResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DbfsRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DbfsRecordResponseBody = None,
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
            temp_model = DbfsRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopUpgradeTaskRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        page_number: int = None,
        page_size: int = None,
        batch_strategy_list: str = None,
    ):
        self.region_id = region_id
        self.page_number = page_number
        self.page_size = page_size
        self.batch_strategy_list = batch_strategy_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.batch_strategy_list is not None:
            result['BatchStrategyList'] = self.batch_strategy_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('BatchStrategyList') is not None:
            self.batch_strategy_list = m.get('BatchStrategyList')
        return self


class StopUpgradeTaskResponseBody(TeaModel):
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


class StopUpgradeTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopUpgradeTaskResponseBody = None,
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
            temp_model = StopUpgradeTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDbfsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        fs_name: str = None,
        category: str = None,
        size_g: int = None,
        zone_id: str = None,
        client_token: str = None,
        snapshot_id: str = None,
        delete_snapshot: bool = None,
        performance_level: str = None,
        enable_raid: bool = None,
        raid_stripe_unit_number: int = None,
        kmskey_id: str = None,
        encryption: bool = None,
        used_scene: str = None,
        instance_type: str = None,
    ):
        self.region_id = region_id
        self.fs_name = fs_name
        self.category = category
        self.size_g = size_g
        self.zone_id = zone_id
        self.client_token = client_token
        self.snapshot_id = snapshot_id
        self.delete_snapshot = delete_snapshot
        self.performance_level = performance_level
        self.enable_raid = enable_raid
        self.raid_stripe_unit_number = raid_stripe_unit_number
        self.kmskey_id = kmskey_id
        self.encryption = encryption
        self.used_scene = used_scene
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.fs_name is not None:
            result['FsName'] = self.fs_name
        if self.category is not None:
            result['Category'] = self.category
        if self.size_g is not None:
            result['SizeG'] = self.size_g
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.delete_snapshot is not None:
            result['DeleteSnapshot'] = self.delete_snapshot
        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level
        if self.enable_raid is not None:
            result['EnableRaid'] = self.enable_raid
        if self.raid_stripe_unit_number is not None:
            result['RaidStripeUnitNumber'] = self.raid_stripe_unit_number
        if self.kmskey_id is not None:
            result['KMSKeyId'] = self.kmskey_id
        if self.encryption is not None:
            result['Encryption'] = self.encryption
        if self.used_scene is not None:
            result['UsedScene'] = self.used_scene
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('FsName') is not None:
            self.fs_name = m.get('FsName')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('SizeG') is not None:
            self.size_g = m.get('SizeG')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('DeleteSnapshot') is not None:
            self.delete_snapshot = m.get('DeleteSnapshot')
        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')
        if m.get('EnableRaid') is not None:
            self.enable_raid = m.get('EnableRaid')
        if m.get('RaidStripeUnitNumber') is not None:
            self.raid_stripe_unit_number = m.get('RaidStripeUnitNumber')
        if m.get('KMSKeyId') is not None:
            self.kmskey_id = m.get('KMSKeyId')
        if m.get('Encryption') is not None:
            self.encryption = m.get('Encryption')
        if m.get('UsedScene') is not None:
            self.used_scene = m.get('UsedScene')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class CreateDbfsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        fs_id: str = None,
    ):
        self.request_id = request_id
        self.fs_id = fs_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.fs_id is not None:
            result['FsId'] = self.fs_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('FsId') is not None:
            self.fs_id = m.get('FsId')
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


class UpdateTaskRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        task_ids: str = None,
        task_progress: int = None,
    ):
        self.region_id = region_id
        self.task_ids = task_ids
        self.task_progress = task_progress

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.task_ids is not None:
            result['TaskIds'] = self.task_ids
        if self.task_progress is not None:
            result['TaskProgress'] = self.task_progress
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TaskIds') is not None:
            self.task_ids = m.get('TaskIds')
        if m.get('TaskProgress') is not None:
            self.task_progress = m.get('TaskProgress')
        return self


class UpdateTaskResponseBody(TeaModel):
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


class UpdateTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateTaskResponseBody = None,
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
            temp_model = UpdateTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTagsBatchRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        dbfs_list: str = None,
        tags: str = None,
    ):
        self.region_id = region_id
        self.dbfs_list = dbfs_list
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dbfs_list is not None:
            result['DbfsList'] = self.dbfs_list
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DbfsList') is not None:
            self.dbfs_list = m.get('DbfsList')
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
        request_id: str = None,
        dbfs_linked_role: bool = None,
        region_id: str = None,
    ):
        self.account_id = account_id
        self.request_id = request_id
        self.dbfs_linked_role = dbfs_linked_role
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.dbfs_linked_role is not None:
            result['DbfsLinkedRole'] = self.dbfs_linked_role
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DbfsLinkedRole') is not None:
            self.dbfs_linked_role = m.get('DbfsLinkedRole')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
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


class UpdateConstantsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        page_number: int = None,
        page_size: int = None,
        constants_data: str = None,
    ):
        self.region_id = region_id
        self.page_number = page_number
        self.page_size = page_size
        self.constants_data = constants_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.constants_data is not None:
            result['ConstantsData'] = self.constants_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ConstantsData') is not None:
            self.constants_data = m.get('ConstantsData')
        return self


class UpdateConstantsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
        page_size: int = None,
        total_count: int = None,
        page_number: int = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.data = data
        self.page_size = page_size
        self.total_count = total_count
        self.page_number = page_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class UpdateConstantsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateConstantsResponseBody = None,
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
            temp_model = UpdateConstantsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InsertSynchronizConstantsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        access_data: str = None,
        endpoint_data: str = None,
        master_data: str = None,
        product_code_data: str = None,
        osversion_data: str = None,
        zone_data: str = None,
        region_data: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.region_id = region_id
        self.access_data = access_data
        self.endpoint_data = endpoint_data
        self.master_data = master_data
        self.product_code_data = product_code_data
        self.osversion_data = osversion_data
        self.zone_data = zone_data
        self.region_data = region_data
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.access_data is not None:
            result['AccessData'] = self.access_data
        if self.endpoint_data is not None:
            result['EndpointData'] = self.endpoint_data
        if self.master_data is not None:
            result['MasterData'] = self.master_data
        if self.product_code_data is not None:
            result['ProductCodeData'] = self.product_code_data
        if self.osversion_data is not None:
            result['OsversionData'] = self.osversion_data
        if self.zone_data is not None:
            result['ZoneData'] = self.zone_data
        if self.region_data is not None:
            result['RegionData'] = self.region_data
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AccessData') is not None:
            self.access_data = m.get('AccessData')
        if m.get('EndpointData') is not None:
            self.endpoint_data = m.get('EndpointData')
        if m.get('MasterData') is not None:
            self.master_data = m.get('MasterData')
        if m.get('ProductCodeData') is not None:
            self.product_code_data = m.get('ProductCodeData')
        if m.get('OsversionData') is not None:
            self.osversion_data = m.get('OsversionData')
        if m.get('ZoneData') is not None:
            self.zone_data = m.get('ZoneData')
        if m.get('RegionData') is not None:
            self.region_data = m.get('RegionData')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class InsertSynchronizConstantsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
        page_size: int = None,
        total_count: int = None,
        page_number: int = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.data = data
        self.page_size = page_size
        self.total_count = total_count
        self.page_number = page_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class InsertSynchronizConstantsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: InsertSynchronizConstantsResponseBody = None,
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
            temp_model = InsertSynchronizConstantsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachDbfsRequest(TeaModel):
    def __init__(
        self,
        ecsinstance_id: str = None,
        server_url: str = None,
        fs_id: str = None,
        region_id: str = None,
        attach_mode: str = None,
        attach_point: str = None,
    ):
        self.ecsinstance_id = ecsinstance_id
        self.server_url = server_url
        self.fs_id = fs_id
        self.region_id = region_id
        self.attach_mode = attach_mode
        self.attach_point = attach_point

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ecsinstance_id is not None:
            result['ECSInstanceId'] = self.ecsinstance_id
        if self.server_url is not None:
            result['ServerUrl'] = self.server_url
        if self.fs_id is not None:
            result['FsId'] = self.fs_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.attach_mode is not None:
            result['AttachMode'] = self.attach_mode
        if self.attach_point is not None:
            result['AttachPoint'] = self.attach_point
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ECSInstanceId') is not None:
            self.ecsinstance_id = m.get('ECSInstanceId')
        if m.get('ServerUrl') is not None:
            self.server_url = m.get('ServerUrl')
        if m.get('FsId') is not None:
            self.fs_id = m.get('FsId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AttachMode') is not None:
            self.attach_mode = m.get('AttachMode')
        if m.get('AttachPoint') is not None:
            self.attach_point = m.get('AttachPoint')
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


class ListTaskRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        page_number: int = None,
        page_size: int = None,
        sort_key: str = None,
        sort_type: str = None,
        filter_key: str = None,
        filter_value: str = None,
    ):
        self.region_id = region_id
        self.page_number = page_number
        self.page_size = page_size
        self.sort_key = sort_key
        self.sort_type = sort_type
        self.filter_key = filter_key
        self.filter_value = filter_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_key is not None:
            result['SortKey'] = self.sort_key
        if self.sort_type is not None:
            result['SortType'] = self.sort_type
        if self.filter_key is not None:
            result['FilterKey'] = self.filter_key
        if self.filter_value is not None:
            result['FilterValue'] = self.filter_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortKey') is not None:
            self.sort_key = m.get('SortKey')
        if m.get('SortType') is not None:
            self.sort_type = m.get('SortType')
        if m.get('FilterKey') is not None:
            self.filter_key = m.get('FilterKey')
        if m.get('FilterValue') is not None:
            self.filter_value = m.get('FilterValue')
        return self


class ListTaskResponseBodyTasks(TeaModel):
    def __init__(
        self,
        task_error_reason: str = None,
        task_name: str = None,
        priority: str = None,
        next_execution_time: str = None,
        completion_time: str = None,
        task_type: str = None,
        task_status: str = None,
        task_status_code: int = None,
        task_execution_counts: int = None,
        client_token: str = None,
        task_adder: str = None,
        task_progress_description: str = None,
        created_time: str = None,
        task_runner: str = None,
        task_progress: int = None,
        task_owner: str = None,
        id: int = None,
        max_retry: int = None,
    ):
        self.task_error_reason = task_error_reason
        self.task_name = task_name
        self.priority = priority
        self.next_execution_time = next_execution_time
        self.completion_time = completion_time
        self.task_type = task_type
        self.task_status = task_status
        self.task_status_code = task_status_code
        self.task_execution_counts = task_execution_counts
        self.client_token = client_token
        self.task_adder = task_adder
        self.task_progress_description = task_progress_description
        self.created_time = created_time
        self.task_runner = task_runner
        self.task_progress = task_progress
        self.task_owner = task_owner
        self.id = id
        self.max_retry = max_retry

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_error_reason is not None:
            result['TaskErrorReason'] = self.task_error_reason
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.next_execution_time is not None:
            result['NextExecutionTime'] = self.next_execution_time
        if self.completion_time is not None:
            result['CompletionTime'] = self.completion_time
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_status_code is not None:
            result['TaskStatusCode'] = self.task_status_code
        if self.task_execution_counts is not None:
            result['TaskExecutionCounts'] = self.task_execution_counts
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.task_adder is not None:
            result['TaskAdder'] = self.task_adder
        if self.task_progress_description is not None:
            result['TaskProgressDescription'] = self.task_progress_description
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.task_runner is not None:
            result['TaskRunner'] = self.task_runner
        if self.task_progress is not None:
            result['TaskProgress'] = self.task_progress
        if self.task_owner is not None:
            result['TaskOwner'] = self.task_owner
        if self.id is not None:
            result['Id'] = self.id
        if self.max_retry is not None:
            result['MaxRetry'] = self.max_retry
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskErrorReason') is not None:
            self.task_error_reason = m.get('TaskErrorReason')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('NextExecutionTime') is not None:
            self.next_execution_time = m.get('NextExecutionTime')
        if m.get('CompletionTime') is not None:
            self.completion_time = m.get('CompletionTime')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskStatusCode') is not None:
            self.task_status_code = m.get('TaskStatusCode')
        if m.get('TaskExecutionCounts') is not None:
            self.task_execution_counts = m.get('TaskExecutionCounts')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('TaskAdder') is not None:
            self.task_adder = m.get('TaskAdder')
        if m.get('TaskProgressDescription') is not None:
            self.task_progress_description = m.get('TaskProgressDescription')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('TaskRunner') is not None:
            self.task_runner = m.get('TaskRunner')
        if m.get('TaskProgress') is not None:
            self.task_progress = m.get('TaskProgress')
        if m.get('TaskOwner') is not None:
            self.task_owner = m.get('TaskOwner')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MaxRetry') is not None:
            self.max_retry = m.get('MaxRetry')
        return self


class ListTaskResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        tasks: List[ListTaskResponseBodyTasks] = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
    ):
        self.total_count = total_count
        self.tasks = tasks
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number

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
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
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
        self.tasks = []
        if m.get('Tasks') is not None:
            for k in m.get('Tasks'):
                temp_model = ListTaskResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class ListTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTaskResponseBody = None,
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
            temp_model = ListTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDbfsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        page_number: int = None,
        page_size: int = None,
        sort_key: str = None,
        sort_type: str = None,
        filter_key: str = None,
        filter_value: str = None,
        tags: str = None,
    ):
        self.region_id = region_id
        self.page_number = page_number
        self.page_size = page_size
        self.sort_key = sort_key
        self.sort_type = sort_type
        self.filter_key = filter_key
        self.filter_value = filter_value
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_key is not None:
            result['SortKey'] = self.sort_key
        if self.sort_type is not None:
            result['SortType'] = self.sort_type
        if self.filter_key is not None:
            result['FilterKey'] = self.filter_key
        if self.filter_value is not None:
            result['FilterValue'] = self.filter_value
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortKey') is not None:
            self.sort_key = m.get('SortKey')
        if m.get('SortType') is not None:
            self.sort_type = m.get('SortType')
        if m.get('FilterKey') is not None:
            self.filter_key = m.get('FilterKey')
        if m.get('FilterValue') is not None:
            self.filter_value = m.get('FilterValue')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class ListDbfsResponseBodyDBFSInfoTags(TeaModel):
    def __init__(
        self,
        tag_value: str = None,
        id: int = None,
        tag_key: str = None,
    ):
        self.tag_value = tag_value
        self.id = id
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        if self.id is not None:
            result['Id'] = self.id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
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


class ListDbfsResponseBodyDBFSInfo(TeaModel):
    def __init__(
        self,
        status: str = None,
        encryption: bool = None,
        pay_type: str = None,
        fs_id: str = None,
        tags: List[ListDbfsResponseBodyDBFSInfoTags] = None,
        size_g: int = None,
        ecs_list: List[ListDbfsResponseBodyDBFSInfoEcsList] = None,
        ebs_list: List[ListDbfsResponseBodyDBFSInfoEbsList] = None,
        region_id: str = None,
        dbfscluster_id: str = None,
        zone_id: str = None,
        fs_name: str = None,
        category: str = None,
        created_time: str = None,
        attach_node_number: int = None,
        kmskey_id: str = None,
        performance_level: str = None,
        used_scene: str = None,
        last_mount_time: str = None,
        last_umount_time: str = None,
        enable_raid: bool = None,
        raid_strip: int = None,
    ):
        self.status = status
        self.encryption = encryption
        self.pay_type = pay_type
        self.fs_id = fs_id
        self.tags = tags
        self.size_g = size_g
        self.ecs_list = ecs_list
        self.ebs_list = ebs_list
        self.region_id = region_id
        self.dbfscluster_id = dbfscluster_id
        self.zone_id = zone_id
        self.fs_name = fs_name
        self.category = category
        self.created_time = created_time
        self.attach_node_number = attach_node_number
        self.kmskey_id = kmskey_id
        self.performance_level = performance_level
        self.used_scene = used_scene
        self.last_mount_time = last_mount_time
        self.last_umount_time = last_umount_time
        self.enable_raid = enable_raid
        self.raid_strip = raid_strip

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.ecs_list:
            for k in self.ecs_list:
                if k:
                    k.validate()
        if self.ebs_list:
            for k in self.ebs_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.encryption is not None:
            result['Encryption'] = self.encryption
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.fs_id is not None:
            result['FsId'] = self.fs_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.size_g is not None:
            result['SizeG'] = self.size_g
        result['EcsList'] = []
        if self.ecs_list is not None:
            for k in self.ecs_list:
                result['EcsList'].append(k.to_map() if k else None)
        result['EbsList'] = []
        if self.ebs_list is not None:
            for k in self.ebs_list:
                result['EbsList'].append(k.to_map() if k else None)
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dbfscluster_id is not None:
            result['DBFSClusterId'] = self.dbfscluster_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.fs_name is not None:
            result['FsName'] = self.fs_name
        if self.category is not None:
            result['Category'] = self.category
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.attach_node_number is not None:
            result['AttachNodeNumber'] = self.attach_node_number
        if self.kmskey_id is not None:
            result['KMSKeyId'] = self.kmskey_id
        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level
        if self.used_scene is not None:
            result['UsedScene'] = self.used_scene
        if self.last_mount_time is not None:
            result['LastMountTime'] = self.last_mount_time
        if self.last_umount_time is not None:
            result['LastUmountTime'] = self.last_umount_time
        if self.enable_raid is not None:
            result['EnableRaid'] = self.enable_raid
        if self.raid_strip is not None:
            result['RaidStrip'] = self.raid_strip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Encryption') is not None:
            self.encryption = m.get('Encryption')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('FsId') is not None:
            self.fs_id = m.get('FsId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListDbfsResponseBodyDBFSInfoTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('SizeG') is not None:
            self.size_g = m.get('SizeG')
        self.ecs_list = []
        if m.get('EcsList') is not None:
            for k in m.get('EcsList'):
                temp_model = ListDbfsResponseBodyDBFSInfoEcsList()
                self.ecs_list.append(temp_model.from_map(k))
        self.ebs_list = []
        if m.get('EbsList') is not None:
            for k in m.get('EbsList'):
                temp_model = ListDbfsResponseBodyDBFSInfoEbsList()
                self.ebs_list.append(temp_model.from_map(k))
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DBFSClusterId') is not None:
            self.dbfscluster_id = m.get('DBFSClusterId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('FsName') is not None:
            self.fs_name = m.get('FsName')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('AttachNodeNumber') is not None:
            self.attach_node_number = m.get('AttachNodeNumber')
        if m.get('KMSKeyId') is not None:
            self.kmskey_id = m.get('KMSKeyId')
        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')
        if m.get('UsedScene') is not None:
            self.used_scene = m.get('UsedScene')
        if m.get('LastMountTime') is not None:
            self.last_mount_time = m.get('LastMountTime')
        if m.get('LastUmountTime') is not None:
            self.last_umount_time = m.get('LastUmountTime')
        if m.get('EnableRaid') is not None:
            self.enable_raid = m.get('EnableRaid')
        if m.get('RaidStrip') is not None:
            self.raid_strip = m.get('RaidStrip')
        return self


class ListDbfsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        dbfsinfo: List[ListDbfsResponseBodyDBFSInfo] = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.dbfsinfo = dbfsinfo

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
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['DBFSInfo'] = []
        if self.dbfsinfo is not None:
            for k in self.dbfsinfo:
                result['DBFSInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.dbfsinfo = []
        if m.get('DBFSInfo') is not None:
            for k in m.get('DBFSInfo'):
                temp_model = ListDbfsResponseBodyDBFSInfo()
                self.dbfsinfo.append(temp_model.from_map(k))
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


class AddTagsBatchRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        dbfs_list: str = None,
        tags: str = None,
        client_token: str = None,
    ):
        self.region_id = region_id
        self.dbfs_list = dbfs_list
        self.tags = tags
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dbfs_list is not None:
            result['DbfsList'] = self.dbfs_list
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DbfsList') is not None:
            self.dbfs_list = m.get('DbfsList')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
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


class TagDbfsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        dbfs_id: str = None,
        tags: str = None,
    ):
        self.region_id = region_id
        self.dbfs_id = dbfs_id
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dbfs_id is not None:
            result['DbfsId'] = self.dbfs_id
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DbfsId') is not None:
            self.dbfs_id = m.get('DbfsId')
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


class GetSynchronizConstantsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.region_id = region_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class GetSynchronizConstantsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
        page_size: int = None,
        total_count: int = None,
        page_number: int = None,
        region_data: str = None,
        zone_data: str = None,
        osversion_data: str = None,
        product_code_data: str = None,
        master_data: str = None,
        endpoint_data: str = None,
        access_data: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.data = data
        self.page_size = page_size
        self.total_count = total_count
        self.page_number = page_number
        self.region_data = region_data
        self.zone_data = zone_data
        self.osversion_data = osversion_data
        self.product_code_data = product_code_data
        self.master_data = master_data
        self.endpoint_data = endpoint_data
        self.access_data = access_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.region_data is not None:
            result['RegionData'] = self.region_data
        if self.zone_data is not None:
            result['ZoneData'] = self.zone_data
        if self.osversion_data is not None:
            result['OsversionData'] = self.osversion_data
        if self.product_code_data is not None:
            result['ProductCodeData'] = self.product_code_data
        if self.master_data is not None:
            result['MasterData'] = self.master_data
        if self.endpoint_data is not None:
            result['EndpointData'] = self.endpoint_data
        if self.access_data is not None:
            result['AccessData'] = self.access_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('RegionData') is not None:
            self.region_data = m.get('RegionData')
        if m.get('ZoneData') is not None:
            self.zone_data = m.get('ZoneData')
        if m.get('OsversionData') is not None:
            self.osversion_data = m.get('OsversionData')
        if m.get('ProductCodeData') is not None:
            self.product_code_data = m.get('ProductCodeData')
        if m.get('MasterData') is not None:
            self.master_data = m.get('MasterData')
        if m.get('EndpointData') is not None:
            self.endpoint_data = m.get('EndpointData')
        if m.get('AccessData') is not None:
            self.access_data = m.get('AccessData')
        return self


class GetSynchronizConstantsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSynchronizConstantsResponseBody = None,
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
            temp_model = GetSynchronizConstantsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpreateConstantsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        page_number: int = None,
        page_size: int = None,
        constants_data: str = None,
    ):
        self.region_id = region_id
        self.page_number = page_number
        self.page_size = page_size
        self.constants_data = constants_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.constants_data is not None:
            result['ConstantsData'] = self.constants_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ConstantsData') is not None:
            self.constants_data = m.get('ConstantsData')
        return self


class OpreateConstantsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
        region_data: str = None,
        zone_data: str = None,
        osversion_data: str = None,
        page_size: int = None,
        total_count: int = None,
        page_number: int = None,
        product_code_data: str = None,
        master_data: str = None,
        endpoint_data: str = None,
        access_data: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.data = data
        self.region_data = region_data
        self.zone_data = zone_data
        self.osversion_data = osversion_data
        self.page_size = page_size
        self.total_count = total_count
        self.page_number = page_number
        self.product_code_data = product_code_data
        self.master_data = master_data
        self.endpoint_data = endpoint_data
        self.access_data = access_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.region_data is not None:
            result['RegionData'] = self.region_data
        if self.zone_data is not None:
            result['ZoneData'] = self.zone_data
        if self.osversion_data is not None:
            result['OsversionData'] = self.osversion_data
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.product_code_data is not None:
            result['ProductCodeData'] = self.product_code_data
        if self.master_data is not None:
            result['MasterData'] = self.master_data
        if self.endpoint_data is not None:
            result['EndpointData'] = self.endpoint_data
        if self.access_data is not None:
            result['AccessData'] = self.access_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RegionData') is not None:
            self.region_data = m.get('RegionData')
        if m.get('ZoneData') is not None:
            self.zone_data = m.get('ZoneData')
        if m.get('OsversionData') is not None:
            self.osversion_data = m.get('OsversionData')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('ProductCodeData') is not None:
            self.product_code_data = m.get('ProductCodeData')
        if m.get('MasterData') is not None:
            self.master_data = m.get('MasterData')
        if m.get('EndpointData') is not None:
            self.endpoint_data = m.get('EndpointData')
        if m.get('AccessData') is not None:
            self.access_data = m.get('AccessData')
        return self


class OpreateConstantsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OpreateConstantsResponseBody = None,
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
            temp_model = OpreateConstantsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenameDbfsRequest(TeaModel):
    def __init__(
        self,
        fs_name: str = None,
        fs_id: str = None,
        region_id: str = None,
    ):
        self.fs_name = fs_name
        self.fs_id = fs_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fs_name is not None:
            result['FsName'] = self.fs_name
        if self.fs_id is not None:
            result['FsId'] = self.fs_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FsName') is not None:
            self.fs_name = m.get('FsName')
        if m.get('FsId') is not None:
            self.fs_id = m.get('FsId')
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


class ListConstantsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        page_number: int = None,
        page_size: int = None,
        constants_data: str = None,
    ):
        self.region_id = region_id
        self.page_number = page_number
        self.page_size = page_size
        self.constants_data = constants_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.constants_data is not None:
            result['ConstantsData'] = self.constants_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ConstantsData') is not None:
            self.constants_data = m.get('ConstantsData')
        return self


class ListConstantsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
        page_size: int = None,
        total_count: int = None,
        page_number: int = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.data = data
        self.page_size = page_size
        self.total_count = total_count
        self.page_number = page_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class ListConstantsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListConstantsResponseBody = None,
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
            temp_model = ListConstantsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSnapshotRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        page_number: int = None,
        page_size: int = None,
        sort_key: str = None,
        sort_type: str = None,
        filter_key: str = None,
        filter_value: str = None,
        fs_id: str = None,
        status: str = None,
        snapshot_name: str = None,
        snapshot_type: str = None,
        snapshot_ids: str = None,
    ):
        self.region_id = region_id
        self.page_number = page_number
        self.page_size = page_size
        self.sort_key = sort_key
        self.sort_type = sort_type
        self.filter_key = filter_key
        self.filter_value = filter_value
        self.fs_id = fs_id
        self.status = status
        self.snapshot_name = snapshot_name
        self.snapshot_type = snapshot_type
        self.snapshot_ids = snapshot_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_key is not None:
            result['SortKey'] = self.sort_key
        if self.sort_type is not None:
            result['SortType'] = self.sort_type
        if self.filter_key is not None:
            result['FilterKey'] = self.filter_key
        if self.filter_value is not None:
            result['FilterValue'] = self.filter_value
        if self.fs_id is not None:
            result['FsId'] = self.fs_id
        if self.status is not None:
            result['Status'] = self.status
        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name
        if self.snapshot_type is not None:
            result['SnapshotType'] = self.snapshot_type
        if self.snapshot_ids is not None:
            result['SnapshotIds'] = self.snapshot_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortKey') is not None:
            self.sort_key = m.get('SortKey')
        if m.get('SortType') is not None:
            self.sort_type = m.get('SortType')
        if m.get('FilterKey') is not None:
            self.filter_key = m.get('FilterKey')
        if m.get('FilterValue') is not None:
            self.filter_value = m.get('FilterValue')
        if m.get('FsId') is not None:
            self.fs_id = m.get('FsId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')
        if m.get('SnapshotType') is not None:
            self.snapshot_type = m.get('SnapshotType')
        if m.get('SnapshotIds') is not None:
            self.snapshot_ids = m.get('SnapshotIds')
        return self


class ListSnapshotResponseBodySnapshots(TeaModel):
    def __init__(
        self,
        status: str = None,
        creation_time: str = None,
        progress: str = None,
        source_fs_size: int = None,
        retention_days: int = None,
        remain_time: int = None,
        last_modified_time: str = None,
        snapshot_type: str = None,
        snapshot_name: str = None,
        description: str = None,
        source_fs_id: str = None,
        snapshot_id: str = None,
        category: str = None,
    ):
        self.status = status
        self.creation_time = creation_time
        self.progress = progress
        self.source_fs_size = source_fs_size
        self.retention_days = retention_days
        self.remain_time = remain_time
        self.last_modified_time = last_modified_time
        self.snapshot_type = snapshot_type
        self.snapshot_name = snapshot_name
        self.description = description
        self.source_fs_id = source_fs_id
        self.snapshot_id = snapshot_id
        self.category = category

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.source_fs_size is not None:
            result['SourceFsSize'] = self.source_fs_size
        if self.retention_days is not None:
            result['RetentionDays'] = self.retention_days
        if self.remain_time is not None:
            result['RemainTime'] = self.remain_time
        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time
        if self.snapshot_type is not None:
            result['SnapshotType'] = self.snapshot_type
        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name
        if self.description is not None:
            result['Description'] = self.description
        if self.source_fs_id is not None:
            result['SourceFsId'] = self.source_fs_id
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.category is not None:
            result['Category'] = self.category
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('SourceFsSize') is not None:
            self.source_fs_size = m.get('SourceFsSize')
        if m.get('RetentionDays') is not None:
            self.retention_days = m.get('RetentionDays')
        if m.get('RemainTime') is not None:
            self.remain_time = m.get('RemainTime')
        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')
        if m.get('SnapshotType') is not None:
            self.snapshot_type = m.get('SnapshotType')
        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SourceFsId') is not None:
            self.source_fs_id = m.get('SourceFsId')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        return self


class ListSnapshotResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        snapshots: List[ListSnapshotResponseBodySnapshots] = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.snapshots = snapshots

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
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Snapshots'] = []
        if self.snapshots is not None:
            for k in self.snapshots:
                result['Snapshots'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.snapshots = []
        if m.get('Snapshots') is not None:
            for k in m.get('Snapshots'):
                temp_model = ListSnapshotResponseBodySnapshots()
                self.snapshots.append(temp_model.from_map(k))
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


class DescribeDbfsSpecificationsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        ecs_instance_type: str = None,
        category: str = None,
    ):
        self.region_id = region_id
        self.ecs_instance_type = ecs_instance_type
        self.category = category

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.ecs_instance_type is not None:
            result['EcsInstanceType'] = self.ecs_instance_type
        if self.category is not None:
            result['Category'] = self.category
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('EcsInstanceType') is not None:
            self.ecs_instance_type = m.get('EcsInstanceType')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        return self


class DescribeDbfsSpecificationsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        supported_ecs_instance_type_family: List[str] = None,
        max_dbfs_number_per_ecs: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.supported_ecs_instance_type_family = supported_ecs_instance_type_family
        self.max_dbfs_number_per_ecs = max_dbfs_number_per_ecs

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.supported_ecs_instance_type_family is not None:
            result['SupportedEcsInstanceTypeFamily'] = self.supported_ecs_instance_type_family
        if self.max_dbfs_number_per_ecs is not None:
            result['MaxDbfsNumberPerEcs'] = self.max_dbfs_number_per_ecs
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SupportedEcsInstanceTypeFamily') is not None:
            self.supported_ecs_instance_type_family = m.get('SupportedEcsInstanceTypeFamily')
        if m.get('MaxDbfsNumberPerEcs') is not None:
            self.max_dbfs_number_per_ecs = m.get('MaxDbfsNumberPerEcs')
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


class CreateSnapshotRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        fs_id: str = None,
        snapshot_name: str = None,
        description: str = None,
        retention_days: int = None,
        client_token: str = None,
    ):
        self.region_id = region_id
        self.fs_id = fs_id
        self.snapshot_name = snapshot_name
        self.description = description
        self.retention_days = retention_days
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.fs_id is not None:
            result['FsId'] = self.fs_id
        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name
        if self.description is not None:
            result['Description'] = self.description
        if self.retention_days is not None:
            result['RetentionDays'] = self.retention_days
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('FsId') is not None:
            self.fs_id = m.get('FsId')
        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RetentionDays') is not None:
            self.retention_days = m.get('RetentionDays')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateSnapshotResponseBody(TeaModel):
    def __init__(
        self,
        snapshot_id: str = None,
        request_id: str = None,
    ):
        self.snapshot_id = snapshot_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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


