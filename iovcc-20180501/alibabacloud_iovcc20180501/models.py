# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AddUploadedFunctionFileInfoRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        object_key: str = None,
        file_name: str = None,
    ):
        self.project_id = project_id
        self.object_key = object_key
        self.file_name = file_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.object_key is not None:
            result['ObjectKey'] = self.object_key
        if self.file_name is not None:
            result['FileName'] = self.file_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ObjectKey') is not None:
            self.object_key = m.get('ObjectKey')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        return self


class AddUploadedFunctionFileInfoResponseBody(TeaModel):
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


class AddUploadedFunctionFileInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddUploadedFunctionFileInfoResponseBody = None,
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
            temp_model = AddUploadedFunctionFileInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddVersionBlackDevicesRequest(TeaModel):
    def __init__(
        self,
        device_ids: str = None,
        project_id: str = None,
        version_type: str = None,
        device_id_type: str = None,
        version_id: str = None,
    ):
        self.device_ids = device_ids
        self.project_id = project_id
        self.version_type = version_type
        self.device_id_type = device_id_type
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.device_ids is not None:
            result['DeviceIds'] = self.device_ids
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.version_type is not None:
            result['VersionType'] = self.version_type
        if self.device_id_type is not None:
            result['DeviceIdType'] = self.device_id_type
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceIds') is not None:
            self.device_ids = m.get('DeviceIds')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('VersionType') is not None:
            self.version_type = m.get('VersionType')
        if m.get('DeviceIdType') is not None:
            self.device_id_type = m.get('DeviceIdType')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class AddVersionBlackDevicesResponseBody(TeaModel):
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


class AddVersionBlackDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddVersionBlackDevicesResponseBody = None,
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
            temp_model = AddVersionBlackDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddVersionGroupDevicesRequest(TeaModel):
    def __init__(
        self,
        device_id_type: str = None,
        project_id: str = None,
        device_ids: str = None,
        device_group_id: str = None,
    ):
        self.device_id_type = device_id_type
        self.project_id = project_id
        self.device_ids = device_ids
        self.device_group_id = device_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.device_id_type is not None:
            result['DeviceIdType'] = self.device_id_type
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.device_ids is not None:
            result['DeviceIds'] = self.device_ids
        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceIdType') is not None:
            self.device_id_type = m.get('DeviceIdType')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('DeviceIds') is not None:
            self.device_ids = m.get('DeviceIds')
        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')
        return self


class AddVersionGroupDevicesResponseBody(TeaModel):
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


class AddVersionGroupDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddVersionGroupDevicesResponseBody = None,
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
            temp_model = AddVersionGroupDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddVersionWhiteDevicesRequest(TeaModel):
    def __init__(
        self,
        device_ids: str = None,
        project_id: str = None,
        version_type: str = None,
        device_id_type: str = None,
        version_id: str = None,
    ):
        self.device_ids = device_ids
        self.project_id = project_id
        self.version_type = version_type
        self.device_id_type = device_id_type
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.device_ids is not None:
            result['DeviceIds'] = self.device_ids
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.version_type is not None:
            result['VersionType'] = self.version_type
        if self.device_id_type is not None:
            result['DeviceIdType'] = self.device_id_type
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceIds') is not None:
            self.device_ids = m.get('DeviceIds')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('VersionType') is not None:
            self.version_type = m.get('VersionType')
        if m.get('DeviceIdType') is not None:
            self.device_id_type = m.get('DeviceIdType')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class AddVersionWhiteDevicesResponseBody(TeaModel):
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


class AddVersionWhiteDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddVersionWhiteDevicesResponseBody = None,
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
            temp_model = AddVersionWhiteDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddVersionWhiteDevicesByDeviceGroupsRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        version_type: str = None,
        group_ids: str = None,
        version_id: str = None,
    ):
        self.project_id = project_id
        self.version_type = version_type
        self.group_ids = group_ids
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.version_type is not None:
            result['VersionType'] = self.version_type
        if self.group_ids is not None:
            result['GroupIds'] = self.group_ids
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('VersionType') is not None:
            self.version_type = m.get('VersionType')
        if m.get('GroupIds') is not None:
            self.group_ids = m.get('GroupIds')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class AddVersionWhiteDevicesByDeviceGroupsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class AddVersionWhiteDevicesByDeviceGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddVersionWhiteDevicesByDeviceGroupsResponseBody = None,
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
            temp_model = AddVersionWhiteDevicesByDeviceGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConnectAssistDeviceRequest(TeaModel):
    def __init__(
        self,
        hardware_id: str = None,
        allow_command_extension: bool = None,
        device_id: str = None,
        serial_number: str = None,
        vin: str = None,
        uuid: str = None,
        project_id: str = None,
    ):
        self.hardware_id = hardware_id
        self.allow_command_extension = allow_command_extension
        self.device_id = device_id
        self.serial_number = serial_number
        self.vin = vin
        self.uuid = uuid
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.hardware_id is not None:
            result['HardwareId'] = self.hardware_id
        if self.allow_command_extension is not None:
            result['AllowCommandExtension'] = self.allow_command_extension
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.vin is not None:
            result['VIN'] = self.vin
        if self.uuid is not None:
            result['UUID'] = self.uuid
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HardwareId') is not None:
            self.hardware_id = m.get('HardwareId')
        if m.get('AllowCommandExtension') is not None:
            self.allow_command_extension = m.get('AllowCommandExtension')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('VIN') is not None:
            self.vin = m.get('VIN')
        if m.get('UUID') is not None:
            self.uuid = m.get('UUID')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class ConnectAssistDeviceResponseBody(TeaModel):
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


class ConnectAssistDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ConnectAssistDeviceResponseBody = None,
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
            temp_model = ConnectAssistDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CountDeviceBrandsRequest(TeaModel):
    def __init__(
        self,
        device_brand_id: int = None,
        device_brand: str = None,
        project_id: str = None,
    ):
        self.device_brand_id = device_brand_id
        self.device_brand = device_brand
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.device_brand_id is not None:
            result['DeviceBrandId'] = self.device_brand_id
        if self.device_brand is not None:
            result['DeviceBrand'] = self.device_brand
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceBrandId') is not None:
            self.device_brand_id = m.get('DeviceBrandId')
        if m.get('DeviceBrand') is not None:
            self.device_brand = m.get('DeviceBrand')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class CountDeviceBrandsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        brand_count: int = None,
    ):
        self.request_id = request_id
        self.brand_count = brand_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.brand_count is not None:
            result['BrandCount'] = self.brand_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('BrandCount') is not None:
            self.brand_count = m.get('BrandCount')
        return self


class CountDeviceBrandsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CountDeviceBrandsResponseBody = None,
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
            temp_model = CountDeviceBrandsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CountDeviceModelsRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        device_model_id: int = None,
        device_model: str = None,
        device_brand: str = None,
    ):
        self.project_id = project_id
        self.device_model_id = device_model_id
        self.device_model = device_model
        self.device_brand = device_brand

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.device_model_id is not None:
            result['DeviceModelId'] = self.device_model_id
        if self.device_model is not None:
            result['DeviceModel'] = self.device_model
        if self.device_brand is not None:
            result['DeviceBrand'] = self.device_brand
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('DeviceModelId') is not None:
            self.device_model_id = m.get('DeviceModelId')
        if m.get('DeviceModel') is not None:
            self.device_model = m.get('DeviceModel')
        if m.get('DeviceBrand') is not None:
            self.device_brand = m.get('DeviceBrand')
        return self


class CountDeviceModelsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        model_count: int = None,
    ):
        self.request_id = request_id
        self.model_count = model_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.model_count is not None:
            result['ModelCount'] = self.model_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ModelCount') is not None:
            self.model_count = m.get('ModelCount')
        return self


class CountDeviceModelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CountDeviceModelsResponseBody = None,
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
            temp_model = CountDeviceModelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CountDevicesRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        device_model_id: int = None,
        device_model: str = None,
    ):
        self.project_id = project_id
        self.device_model_id = device_model_id
        self.device_model = device_model

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.device_model_id is not None:
            result['DeviceModelId'] = self.device_model_id
        if self.device_model is not None:
            result['DeviceModel'] = self.device_model
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('DeviceModelId') is not None:
            self.device_model_id = m.get('DeviceModelId')
        if m.get('DeviceModel') is not None:
            self.device_model = m.get('DeviceModel')
        return self


class CountDevicesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        device_count: int = None,
    ):
        self.request_id = request_id
        self.device_count = device_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.device_count is not None:
            result['DeviceCount'] = self.device_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DeviceCount') is not None:
            self.device_count = m.get('DeviceCount')
        return self


class CountDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CountDevicesResponseBody = None,
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
            temp_model = CountDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CountProjectsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        project_count: int = None,
    ):
        self.request_id = request_id
        self.project_count = project_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.project_count is not None:
            result['ProjectCount'] = self.project_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ProjectCount') is not None:
            self.project_count = m.get('ProjectCount')
        return self


class CountProjectsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CountProjectsResponseBody = None,
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
            temp_model = CountProjectsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CountYunIdInfoResponseBodyYunIdInfo(TeaModel):
    def __init__(
        self,
        total_brand_count: int = None,
        total_device_count: int = None,
        total_device_model_count: int = None,
    ):
        self.total_brand_count = total_brand_count
        self.total_device_count = total_device_count
        self.total_device_model_count = total_device_model_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.total_brand_count is not None:
            result['TotalBrandCount'] = self.total_brand_count
        if self.total_device_count is not None:
            result['TotalDeviceCount'] = self.total_device_count
        if self.total_device_model_count is not None:
            result['TotalDeviceModelCount'] = self.total_device_model_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalBrandCount') is not None:
            self.total_brand_count = m.get('TotalBrandCount')
        if m.get('TotalDeviceCount') is not None:
            self.total_device_count = m.get('TotalDeviceCount')
        if m.get('TotalDeviceModelCount') is not None:
            self.total_device_model_count = m.get('TotalDeviceModelCount')
        return self


class CountYunIdInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        yun_id_info: List[CountYunIdInfoResponseBodyYunIdInfo] = None,
    ):
        self.request_id = request_id
        self.yun_id_info = yun_id_info

    def validate(self):
        if self.yun_id_info:
            for k in self.yun_id_info:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['YunIdInfo'] = []
        if self.yun_id_info is not None:
            for k in self.yun_id_info:
                result['YunIdInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.yun_id_info = []
        if m.get('YunIdInfo') is not None:
            for k in m.get('YunIdInfo'):
                temp_model = CountYunIdInfoResponseBodyYunIdInfo()
                self.yun_id_info.append(temp_model.from_map(k))
        return self


class CountYunIdInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CountYunIdInfoResponseBody = None,
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
            temp_model = CountYunIdInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppVersionRequest(TeaModel):
    def __init__(
        self,
        is_force_upgrade: str = None,
        is_allow_new_install: str = None,
        project_id: str = None,
        app_id: str = None,
        app_version: str = None,
        version_code: str = None,
        install_type: str = None,
        remark: str = None,
        release_note: str = None,
        is_silent_upgrade: str = None,
        package_url: str = None,
        is_need_restart: str = None,
        black_version_list: str = None,
        white_version_list: str = None,
        restart_type: str = None,
        restart_app_type: str = None,
        restart_app_param: str = None,
        device_adapter_list: str = None,
        apk_md_5: str = None,
    ):
        self.is_force_upgrade = is_force_upgrade
        self.is_allow_new_install = is_allow_new_install
        self.project_id = project_id
        self.app_id = app_id
        self.app_version = app_version
        self.version_code = version_code
        self.install_type = install_type
        self.remark = remark
        self.release_note = release_note
        self.is_silent_upgrade = is_silent_upgrade
        self.package_url = package_url
        self.is_need_restart = is_need_restart
        self.black_version_list = black_version_list
        self.white_version_list = white_version_list
        self.restart_type = restart_type
        self.restart_app_type = restart_app_type
        self.restart_app_param = restart_app_param
        self.device_adapter_list = device_adapter_list
        self.apk_md_5 = apk_md_5

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.is_force_upgrade is not None:
            result['IsForceUpgrade'] = self.is_force_upgrade
        if self.is_allow_new_install is not None:
            result['IsAllowNewInstall'] = self.is_allow_new_install
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.version_code is not None:
            result['VersionCode'] = self.version_code
        if self.install_type is not None:
            result['InstallType'] = self.install_type
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.release_note is not None:
            result['ReleaseNote'] = self.release_note
        if self.is_silent_upgrade is not None:
            result['IsSilentUpgrade'] = self.is_silent_upgrade
        if self.package_url is not None:
            result['PackageUrl'] = self.package_url
        if self.is_need_restart is not None:
            result['IsNeedRestart'] = self.is_need_restart
        if self.black_version_list is not None:
            result['BlackVersionList'] = self.black_version_list
        if self.white_version_list is not None:
            result['WhiteVersionList'] = self.white_version_list
        if self.restart_type is not None:
            result['RestartType'] = self.restart_type
        if self.restart_app_type is not None:
            result['RestartAppType'] = self.restart_app_type
        if self.restart_app_param is not None:
            result['RestartAppParam'] = self.restart_app_param
        if self.device_adapter_list is not None:
            result['DeviceAdapterList'] = self.device_adapter_list
        if self.apk_md_5 is not None:
            result['ApkMd5'] = self.apk_md_5
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsForceUpgrade') is not None:
            self.is_force_upgrade = m.get('IsForceUpgrade')
        if m.get('IsAllowNewInstall') is not None:
            self.is_allow_new_install = m.get('IsAllowNewInstall')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('VersionCode') is not None:
            self.version_code = m.get('VersionCode')
        if m.get('InstallType') is not None:
            self.install_type = m.get('InstallType')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ReleaseNote') is not None:
            self.release_note = m.get('ReleaseNote')
        if m.get('IsSilentUpgrade') is not None:
            self.is_silent_upgrade = m.get('IsSilentUpgrade')
        if m.get('PackageUrl') is not None:
            self.package_url = m.get('PackageUrl')
        if m.get('IsNeedRestart') is not None:
            self.is_need_restart = m.get('IsNeedRestart')
        if m.get('BlackVersionList') is not None:
            self.black_version_list = m.get('BlackVersionList')
        if m.get('WhiteVersionList') is not None:
            self.white_version_list = m.get('WhiteVersionList')
        if m.get('RestartType') is not None:
            self.restart_type = m.get('RestartType')
        if m.get('RestartAppType') is not None:
            self.restart_app_type = m.get('RestartAppType')
        if m.get('RestartAppParam') is not None:
            self.restart_app_param = m.get('RestartAppParam')
        if m.get('DeviceAdapterList') is not None:
            self.device_adapter_list = m.get('DeviceAdapterList')
        if m.get('ApkMd5') is not None:
            self.apk_md_5 = m.get('ApkMd5')
        return self


class CreateAppVersionResponseBody(TeaModel):
    def __init__(
        self,
        version_id: str = None,
        request_id: str = None,
    ):
        self.version_id = version_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAppVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAppVersionResponseBody = None,
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
            temp_model = CreateAppVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCustomizedFilterRequest(TeaModel):
    def __init__(
        self,
        version_type: str = None,
        black_white_type: str = None,
        value: str = None,
        project_id: str = None,
        value_compare_type: str = None,
        name: str = None,
        value_type: str = None,
        version_id: str = None,
    ):
        self.version_type = version_type
        self.black_white_type = black_white_type
        self.value = value
        self.project_id = project_id
        self.value_compare_type = value_compare_type
        self.name = name
        self.value_type = value_type
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version_type is not None:
            result['VersionType'] = self.version_type
        if self.black_white_type is not None:
            result['BlackWhiteType'] = self.black_white_type
        if self.value is not None:
            result['Value'] = self.value
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.value_compare_type is not None:
            result['ValueCompareType'] = self.value_compare_type
        if self.name is not None:
            result['Name'] = self.name
        if self.value_type is not None:
            result['ValueType'] = self.value_type
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VersionType') is not None:
            self.version_type = m.get('VersionType')
        if m.get('BlackWhiteType') is not None:
            self.black_white_type = m.get('BlackWhiteType')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ValueCompareType') is not None:
            self.value_compare_type = m.get('ValueCompareType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ValueType') is not None:
            self.value_type = m.get('ValueType')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class CreateCustomizedFilterResponseBody(TeaModel):
    def __init__(
        self,
        customized_filter_id: str = None,
        request_id: str = None,
    ):
        self.customized_filter_id = customized_filter_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.customized_filter_id is not None:
            result['CustomizedFilterId'] = self.customized_filter_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomizedFilterId') is not None:
            self.customized_filter_id = m.get('CustomizedFilterId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCustomizedFilterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateCustomizedFilterResponseBody = None,
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
            temp_model = CreateCustomizedFilterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCustomizedPropertyRequest(TeaModel):
    def __init__(
        self,
        version_id: str = None,
        project_id: str = None,
        name: str = None,
        value: str = None,
        version_type: str = None,
    ):
        self.version_id = version_id
        self.project_id = project_id
        self.name = name
        self.value = value
        self.version_type = version_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        if self.version_type is not None:
            result['VersionType'] = self.version_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('VersionType') is not None:
            self.version_type = m.get('VersionType')
        return self


class CreateCustomizedPropertyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        customized_property_id: str = None,
    ):
        self.request_id = request_id
        self.customized_property_id = customized_property_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.customized_property_id is not None:
            result['CustomizedPropertyId'] = self.customized_property_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CustomizedPropertyId') is not None:
            self.customized_property_id = m.get('CustomizedPropertyId')
        return self


class CreateCustomizedPropertyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateCustomizedPropertyResponseBody = None,
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
            temp_model = CreateCustomizedPropertyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDeviceRequest(TeaModel):
    def __init__(
        self,
        model_name: str = None,
        project_id: str = None,
        hardware_id: str = None,
    ):
        self.model_name = model_name
        self.project_id = project_id
        self.hardware_id = hardware_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.hardware_id is not None:
            result['HardwareId'] = self.hardware_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('HardwareId') is not None:
            self.hardware_id = m.get('HardwareId')
        return self


class CreateDeviceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        device_id: int = None,
    ):
        self.request_id = request_id
        self.device_id = device_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        return self


class CreateDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDeviceResponseBody = None,
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
            temp_model = CreateDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDeviceBrandRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        brand_name: str = None,
        manufacture: str = None,
        description: str = None,
    ):
        self.project_id = project_id
        self.brand_name = brand_name
        self.manufacture = manufacture
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.brand_name is not None:
            result['BrandName'] = self.brand_name
        if self.manufacture is not None:
            result['Manufacture'] = self.manufacture
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('BrandName') is not None:
            self.brand_name = m.get('BrandName')
        if m.get('Manufacture') is not None:
            self.manufacture = m.get('Manufacture')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class CreateDeviceBrandResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        brand_id: int = None,
    ):
        self.request_id = request_id
        self.brand_id = brand_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.brand_id is not None:
            result['BrandId'] = self.brand_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('BrandId') is not None:
            self.brand_id = m.get('BrandId')
        return self


class CreateDeviceBrandResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDeviceBrandResponseBody = None,
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
            temp_model = CreateDeviceBrandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDeviceModelRequest(TeaModel):
    def __init__(
        self,
        init_usage_type: str = None,
        can_create_device_id: str = None,
        model_name: str = None,
        hardware_type: str = None,
        brand_name: str = None,
        description: str = None,
        device_type: str = None,
        project_id: str = None,
        security_chip: str = None,
        os_platform: str = None,
        object_key: str = None,
        device_name: str = None,
    ):
        self.init_usage_type = init_usage_type
        self.can_create_device_id = can_create_device_id
        self.model_name = model_name
        self.hardware_type = hardware_type
        self.brand_name = brand_name
        self.description = description
        self.device_type = device_type
        self.project_id = project_id
        self.security_chip = security_chip
        self.os_platform = os_platform
        self.object_key = object_key
        self.device_name = device_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.init_usage_type is not None:
            result['InitUsageType'] = self.init_usage_type
        if self.can_create_device_id is not None:
            result['CanCreateDeviceId'] = self.can_create_device_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.hardware_type is not None:
            result['HardwareType'] = self.hardware_type
        if self.brand_name is not None:
            result['BrandName'] = self.brand_name
        if self.description is not None:
            result['Description'] = self.description
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.security_chip is not None:
            result['SecurityChip'] = self.security_chip
        if self.os_platform is not None:
            result['OsPlatform'] = self.os_platform
        if self.object_key is not None:
            result['ObjectKey'] = self.object_key
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InitUsageType') is not None:
            self.init_usage_type = m.get('InitUsageType')
        if m.get('CanCreateDeviceId') is not None:
            self.can_create_device_id = m.get('CanCreateDeviceId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('HardwareType') is not None:
            self.hardware_type = m.get('HardwareType')
        if m.get('BrandName') is not None:
            self.brand_name = m.get('BrandName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('SecurityChip') is not None:
            self.security_chip = m.get('SecurityChip')
        if m.get('OsPlatform') is not None:
            self.os_platform = m.get('OsPlatform')
        if m.get('ObjectKey') is not None:
            self.object_key = m.get('ObjectKey')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        return self


class CreateDeviceModelResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        device_model_id: int = None,
    ):
        self.request_id = request_id
        self.device_model_id = device_model_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.device_model_id is not None:
            result['DeviceModelId'] = self.device_model_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DeviceModelId') is not None:
            self.device_model_id = m.get('DeviceModelId')
        return self


class CreateDeviceModelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDeviceModelResponseBody = None,
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
            temp_model = CreateDeviceModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMqttRootTopicRequest(TeaModel):
    def __init__(
        self,
        app_key: str = None,
        root_topic: str = None,
        project_id: str = None,
        client_token: str = None,
    ):
        self.app_key = app_key
        self.root_topic = root_topic
        self.project_id = project_id
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.root_topic is not None:
            result['RootTopic'] = self.root_topic
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('RootTopic') is not None:
            self.root_topic = m.get('RootTopic')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateMqttRootTopicResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        queue_name: str = None,
    ):
        self.request_id = request_id
        self.queue_name = queue_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        return self


class CreateMqttRootTopicResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateMqttRootTopicResponseBody = None,
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
            temp_model = CreateMqttRootTopicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateNamespaceRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        auth_type: str = None,
        name: str = None,
        desc: str = None,
    ):
        self.project_id = project_id
        self.auth_type = auth_type
        self.name = name
        self.desc = desc

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type
        if self.name is not None:
            result['Name'] = self.name
        if self.desc is not None:
            result['Desc'] = self.desc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        return self


class CreateNamespaceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        namespace: str = None,
    ):
        self.request_id = request_id
        self.namespace = namespace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        return self


class CreateNamespaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateNamespaceResponseBody = None,
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
            temp_model = CreateNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOsVersionRequest(TeaModel):
    def __init__(
        self,
        is_force_night_upgrade: str = None,
        max_client_version: str = None,
        project_id: str = None,
        device_model_id: str = None,
        system_version: str = None,
        release_note: str = None,
        remark: str = None,
        black_version_list: str = None,
        is_milestone: str = None,
        min_client_version: str = None,
        white_version_list: str = None,
        is_force_upgrade: str = None,
        night_upgrade_download_type: str = None,
        night_upgrade_is_show_tip: str = None,
        night_upgrade_is_allowed_cancel: str = None,
        rom_list: str = None,
        enable_mobile_download: str = None,
        mobile_download_max_size: str = None,
    ):
        self.is_force_night_upgrade = is_force_night_upgrade
        self.max_client_version = max_client_version
        self.project_id = project_id
        self.device_model_id = device_model_id
        self.system_version = system_version
        self.release_note = release_note
        self.remark = remark
        self.black_version_list = black_version_list
        self.is_milestone = is_milestone
        self.min_client_version = min_client_version
        self.white_version_list = white_version_list
        self.is_force_upgrade = is_force_upgrade
        self.night_upgrade_download_type = night_upgrade_download_type
        self.night_upgrade_is_show_tip = night_upgrade_is_show_tip
        self.night_upgrade_is_allowed_cancel = night_upgrade_is_allowed_cancel
        self.rom_list = rom_list
        self.enable_mobile_download = enable_mobile_download
        self.mobile_download_max_size = mobile_download_max_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.is_force_night_upgrade is not None:
            result['IsForceNightUpgrade'] = self.is_force_night_upgrade
        if self.max_client_version is not None:
            result['MaxClientVersion'] = self.max_client_version
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.device_model_id is not None:
            result['DeviceModelId'] = self.device_model_id
        if self.system_version is not None:
            result['SystemVersion'] = self.system_version
        if self.release_note is not None:
            result['ReleaseNote'] = self.release_note
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.black_version_list is not None:
            result['BlackVersionList'] = self.black_version_list
        if self.is_milestone is not None:
            result['IsMilestone'] = self.is_milestone
        if self.min_client_version is not None:
            result['MinClientVersion'] = self.min_client_version
        if self.white_version_list is not None:
            result['WhiteVersionList'] = self.white_version_list
        if self.is_force_upgrade is not None:
            result['IsForceUpgrade'] = self.is_force_upgrade
        if self.night_upgrade_download_type is not None:
            result['NightUpgradeDownloadType'] = self.night_upgrade_download_type
        if self.night_upgrade_is_show_tip is not None:
            result['NightUpgradeIsShowTip'] = self.night_upgrade_is_show_tip
        if self.night_upgrade_is_allowed_cancel is not None:
            result['NightUpgradeIsAllowedCancel'] = self.night_upgrade_is_allowed_cancel
        if self.rom_list is not None:
            result['RomList'] = self.rom_list
        if self.enable_mobile_download is not None:
            result['EnableMobileDownload'] = self.enable_mobile_download
        if self.mobile_download_max_size is not None:
            result['MobileDownloadMaxSize'] = self.mobile_download_max_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsForceNightUpgrade') is not None:
            self.is_force_night_upgrade = m.get('IsForceNightUpgrade')
        if m.get('MaxClientVersion') is not None:
            self.max_client_version = m.get('MaxClientVersion')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('DeviceModelId') is not None:
            self.device_model_id = m.get('DeviceModelId')
        if m.get('SystemVersion') is not None:
            self.system_version = m.get('SystemVersion')
        if m.get('ReleaseNote') is not None:
            self.release_note = m.get('ReleaseNote')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('BlackVersionList') is not None:
            self.black_version_list = m.get('BlackVersionList')
        if m.get('IsMilestone') is not None:
            self.is_milestone = m.get('IsMilestone')
        if m.get('MinClientVersion') is not None:
            self.min_client_version = m.get('MinClientVersion')
        if m.get('WhiteVersionList') is not None:
            self.white_version_list = m.get('WhiteVersionList')
        if m.get('IsForceUpgrade') is not None:
            self.is_force_upgrade = m.get('IsForceUpgrade')
        if m.get('NightUpgradeDownloadType') is not None:
            self.night_upgrade_download_type = m.get('NightUpgradeDownloadType')
        if m.get('NightUpgradeIsShowTip') is not None:
            self.night_upgrade_is_show_tip = m.get('NightUpgradeIsShowTip')
        if m.get('NightUpgradeIsAllowedCancel') is not None:
            self.night_upgrade_is_allowed_cancel = m.get('NightUpgradeIsAllowedCancel')
        if m.get('RomList') is not None:
            self.rom_list = m.get('RomList')
        if m.get('EnableMobileDownload') is not None:
            self.enable_mobile_download = m.get('EnableMobileDownload')
        if m.get('MobileDownloadMaxSize') is not None:
            self.mobile_download_max_size = m.get('MobileDownloadMaxSize')
        return self


class CreateOsVersionResponseBody(TeaModel):
    def __init__(
        self,
        version_id: str = None,
        request_id: str = None,
    ):
        self.version_id = version_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateOsVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateOsVersionResponseBody = None,
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
            temp_model = CreateOsVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProjectRequest(TeaModel):
    def __init__(
        self,
        project_name: str = None,
        project_desc: str = None,
    ):
        self.project_name = project_name
        self.project_desc = project_desc

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.project_desc is not None:
            result['ProjectDesc'] = self.project_desc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ProjectDesc') is not None:
            self.project_desc = m.get('ProjectDesc')
        return self


class CreateProjectResponseBody(TeaModel):
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


class CreateProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateProjectResponseBody = None,
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
            temp_model = CreateProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProjectAppRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        app_name: str = None,
        app_pkg_name: str = None,
        os_type: int = None,
    ):
        self.project_id = project_id
        self.app_name = app_name
        self.app_pkg_name = app_pkg_name
        self.os_type = os_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_pkg_name is not None:
            result['AppPkgName'] = self.app_pkg_name
        if self.os_type is not None:
            result['OsType'] = self.os_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppPkgName') is not None:
            self.app_pkg_name = m.get('AppPkgName')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        return self


class CreateProjectAppResponseBody(TeaModel):
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


class CreateProjectAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateProjectAppResponseBody = None,
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
            temp_model = CreateProjectAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRpcServiceRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        app_key: str = None,
        interface_name: str = None,
        invoke_type: str = None,
        params: str = None,
        group_name: str = None,
        method_name: str = None,
        version_code: str = None,
    ):
        self.project_id = project_id
        self.app_key = app_key
        self.interface_name = interface_name
        self.invoke_type = invoke_type
        self.params = params
        self.group_name = group_name
        self.method_name = method_name
        self.version_code = version_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.interface_name is not None:
            result['InterfaceName'] = self.interface_name
        if self.invoke_type is not None:
            result['InvokeType'] = self.invoke_type
        if self.params is not None:
            result['Params'] = self.params
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.method_name is not None:
            result['MethodName'] = self.method_name
        if self.version_code is not None:
            result['VersionCode'] = self.version_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('InterfaceName') is not None:
            self.interface_name = m.get('InterfaceName')
        if m.get('InvokeType') is not None:
            self.invoke_type = m.get('InvokeType')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('MethodName') is not None:
            self.method_name = m.get('MethodName')
        if m.get('VersionCode') is not None:
            self.version_code = m.get('VersionCode')
        return self


class CreateRpcServiceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        id: int = None,
    ):
        self.request_id = request_id
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class CreateRpcServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateRpcServiceResponseBody = None,
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
            temp_model = CreateRpcServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSchemaSubscribeRequest(TeaModel):
    def __init__(
        self,
        device_model: str = None,
        subscribe_list: str = None,
        project_id: str = None,
        schema_version: str = None,
    ):
        self.device_model = device_model
        self.subscribe_list = subscribe_list
        self.project_id = project_id
        self.schema_version = schema_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.device_model is not None:
            result['DeviceModel'] = self.device_model
        if self.subscribe_list is not None:
            result['SubscribeList'] = self.subscribe_list
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceModel') is not None:
            self.device_model = m.get('DeviceModel')
        if m.get('SubscribeList') is not None:
            self.subscribe_list = m.get('SubscribeList')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        return self


class CreateSchemaSubscribeResponseBody(TeaModel):
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


class CreateSchemaSubscribeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateSchemaSubscribeResponseBody = None,
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
            temp_model = CreateSchemaSubscribeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateShadowSchemaRequest(TeaModel):
    def __init__(
        self,
        device_model_id: str = None,
        auth_type: str = None,
        namespace: str = None,
        project_id: str = None,
        schema: str = None,
    ):
        self.device_model_id = device_model_id
        self.auth_type = auth_type
        self.namespace = namespace
        self.project_id = project_id
        self.schema = schema

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.device_model_id is not None:
            result['DeviceModelId'] = self.device_model_id
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.schema is not None:
            result['Schema'] = self.schema
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceModelId') is not None:
            self.device_model_id = m.get('DeviceModelId')
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Schema') is not None:
            self.schema = m.get('Schema')
        return self


class CreateShadowSchemaResponseBody(TeaModel):
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


class CreateShadowSchemaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateShadowSchemaResponseBody = None,
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
            temp_model = CreateShadowSchemaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTriggerRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        namespace: str = None,
        source: str = None,
        file_ids: str = None,
        function_ids: str = None,
        invocation_mode: int = None,
        sandbox: int = None,
        production: int = None,
    ):
        self.project_id = project_id
        self.namespace = namespace
        self.source = source
        self.file_ids = file_ids
        self.function_ids = function_ids
        self.invocation_mode = invocation_mode
        self.sandbox = sandbox
        self.production = production

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.source is not None:
            result['Source'] = self.source
        if self.file_ids is not None:
            result['FileIds'] = self.file_ids
        if self.function_ids is not None:
            result['FunctionIds'] = self.function_ids
        if self.invocation_mode is not None:
            result['InvocationMode'] = self.invocation_mode
        if self.sandbox is not None:
            result['Sandbox'] = self.sandbox
        if self.production is not None:
            result['Production'] = self.production
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('FileIds') is not None:
            self.file_ids = m.get('FileIds')
        if m.get('FunctionIds') is not None:
            self.function_ids = m.get('FunctionIds')
        if m.get('InvocationMode') is not None:
            self.invocation_mode = m.get('InvocationMode')
        if m.get('Sandbox') is not None:
            self.sandbox = m.get('Sandbox')
        if m.get('Production') is not None:
            self.production = m.get('Production')
        return self


class CreateTriggerResponseBody(TeaModel):
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


class CreateTriggerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateTriggerResponseBody = None,
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
            temp_model = CreateTriggerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUpstreamAppKeyRelationRequest(TeaModel):
    def __init__(
        self,
        app_key: str = None,
        papp_key: str = None,
        project_id: str = None,
    ):
        self.app_key = app_key
        self.papp_key = papp_key
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.papp_key is not None:
            result['PAppKey'] = self.papp_key
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('PAppKey') is not None:
            self.papp_key = m.get('PAppKey')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class CreateUpstreamAppKeyRelationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        id: int = None,
    ):
        self.request_id = request_id
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class CreateUpstreamAppKeyRelationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateUpstreamAppKeyRelationResponseBody = None,
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
            temp_model = CreateUpstreamAppKeyRelationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUpstreamAppKeyRelationsRequest(TeaModel):
    def __init__(
        self,
        app_keys: str = None,
        app_server_id: str = None,
        project_id: str = None,
    ):
        self.app_keys = app_keys
        self.app_server_id = app_server_id
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_keys is not None:
            result['AppKeys'] = self.app_keys
        if self.app_server_id is not None:
            result['AppServerId'] = self.app_server_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKeys') is not None:
            self.app_keys = m.get('AppKeys')
        if m.get('AppServerId') is not None:
            self.app_server_id = m.get('AppServerId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class CreateUpstreamAppKeyRelationsResponseBody(TeaModel):
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


class CreateUpstreamAppKeyRelationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateUpstreamAppKeyRelationsResponseBody = None,
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
            temp_model = CreateUpstreamAppKeyRelationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUpstreamAppServerRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        name: str = None,
        tags: str = None,
    ):
        self.project_id = project_id
        self.name = name
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.name is not None:
            result['Name'] = self.name
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class CreateUpstreamAppServerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        id: int = None,
    ):
        self.request_id = request_id
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class CreateUpstreamAppServerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateUpstreamAppServerResponseBody = None,
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
            temp_model = CreateUpstreamAppServerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVersionDeviceGroupRequest(TeaModel):
    def __init__(
        self,
        max_count: str = None,
        project_id: str = None,
        name: str = None,
        description: str = None,
    ):
        self.max_count = max_count
        self.project_id = project_id
        self.name = name
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.max_count is not None:
            result['MaxCount'] = self.max_count
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxCount') is not None:
            self.max_count = m.get('MaxCount')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class CreateVersionDeviceGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        device_group_id: str = None,
    ):
        self.request_id = request_id
        self.device_group_id = device_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')
        return self


class CreateVersionDeviceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateVersionDeviceGroupResponseBody = None,
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
            temp_model = CreateVersionDeviceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVersionPrepublishRequest(TeaModel):
    def __init__(
        self,
        is_total_prepublish: str = None,
        version_id: str = None,
        version_type: str = None,
        name: str = None,
        project_id: str = None,
        barrier_count: str = None,
    ):
        self.is_total_prepublish = is_total_prepublish
        self.version_id = version_id
        self.version_type = version_type
        self.name = name
        self.project_id = project_id
        self.barrier_count = barrier_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.is_total_prepublish is not None:
            result['IsTotalPrepublish'] = self.is_total_prepublish
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.version_type is not None:
            result['VersionType'] = self.version_type
        if self.name is not None:
            result['Name'] = self.name
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.barrier_count is not None:
            result['BarrierCount'] = self.barrier_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsTotalPrepublish') is not None:
            self.is_total_prepublish = m.get('IsTotalPrepublish')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('VersionType') is not None:
            self.version_type = m.get('VersionType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('BarrierCount') is not None:
            self.barrier_count = m.get('BarrierCount')
        return self


class CreateVersionPrepublishResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prepublish_id: str = None,
    ):
        self.request_id = request_id
        self.prepublish_id = prepublish_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prepublish_id is not None:
            result['PrepublishId'] = self.prepublish_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PrepublishId') is not None:
            self.prepublish_id = m.get('PrepublishId')
        return self


class CreateVersionPrepublishResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateVersionPrepublishResponseBody = None,
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
            temp_model = CreateVersionPrepublishResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVersionTestRequest(TeaModel):
    def __init__(
        self,
        device_group_id: str = None,
        description: str = None,
        version_id: str = None,
        version_type: str = None,
        name: str = None,
        project_id: str = None,
    ):
        self.device_group_id = device_group_id
        self.description = description
        self.version_id = version_id
        self.version_type = version_type
        self.name = name
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id
        if self.description is not None:
            result['Description'] = self.description
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.version_type is not None:
            result['VersionType'] = self.version_type
        if self.name is not None:
            result['Name'] = self.name
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('VersionType') is not None:
            self.version_type = m.get('VersionType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class CreateVersionTestResponseBody(TeaModel):
    def __init__(
        self,
        test_id: str = None,
        request_id: str = None,
    ):
        self.test_id = test_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.test_id is not None:
            result['TestId'] = self.test_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TestId') is not None:
            self.test_id = m.get('TestId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateVersionTestResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateVersionTestResponseBody = None,
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
            temp_model = CreateVersionTestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DelayPublishOsVersionRequest(TeaModel):
    def __init__(
        self,
        version_id: str = None,
        project_id: str = None,
        prepub_time: int = None,
        publish_time: int = None,
        down_time: int = None,
        email: str = None,
        description: str = None,
        send_message: str = None,
        prepublish_count: str = None,
    ):
        self.version_id = version_id
        self.project_id = project_id
        self.prepub_time = prepub_time
        self.publish_time = publish_time
        self.down_time = down_time
        self.email = email
        self.description = description
        self.send_message = send_message
        self.prepublish_count = prepublish_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.prepub_time is not None:
            result['PrepubTime'] = self.prepub_time
        if self.publish_time is not None:
            result['PublishTime'] = self.publish_time
        if self.down_time is not None:
            result['DownTime'] = self.down_time
        if self.email is not None:
            result['Email'] = self.email
        if self.description is not None:
            result['Description'] = self.description
        if self.send_message is not None:
            result['SendMessage'] = self.send_message
        if self.prepublish_count is not None:
            result['PrepublishCount'] = self.prepublish_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('PrepubTime') is not None:
            self.prepub_time = m.get('PrepubTime')
        if m.get('PublishTime') is not None:
            self.publish_time = m.get('PublishTime')
        if m.get('DownTime') is not None:
            self.down_time = m.get('DownTime')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SendMessage') is not None:
            self.send_message = m.get('SendMessage')
        if m.get('PrepublishCount') is not None:
            self.prepublish_count = m.get('PrepublishCount')
        return self


class DelayPublishOsVersionResponseBody(TeaModel):
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


class DelayPublishOsVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DelayPublishOsVersionResponseBody = None,
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
            temp_model = DelayPublishOsVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAllCustomizedFiltersRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        version_id: str = None,
        version_type: str = None,
    ):
        self.project_id = project_id
        self.version_id = version_id
        self.version_type = version_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.version_type is not None:
            result['VersionType'] = self.version_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('VersionType') is not None:
            self.version_type = m.get('VersionType')
        return self


class DeleteAllCustomizedFiltersResponseBody(TeaModel):
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


class DeleteAllCustomizedFiltersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteAllCustomizedFiltersResponseBody = None,
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
            temp_model = DeleteAllCustomizedFiltersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAllVersionGroupDevicesRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        device_group_id: str = None,
    ):
        self.project_id = project_id
        self.device_group_id = device_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')
        return self


class DeleteAllVersionGroupDevicesResponseBody(TeaModel):
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


class DeleteAllVersionGroupDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteAllVersionGroupDevicesResponseBody = None,
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
            temp_model = DeleteAllVersionGroupDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCustomizedFilterRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        id: str = None,
    ):
        self.project_id = project_id
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteCustomizedFilterResponseBody(TeaModel):
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


class DeleteCustomizedFilterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteCustomizedFilterResponseBody = None,
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
            temp_model = DeleteCustomizedFilterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCustomizedPropertyRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        id: str = None,
    ):
        self.project_id = project_id
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteCustomizedPropertyResponseBody(TeaModel):
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


class DeleteCustomizedPropertyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteCustomizedPropertyResponseBody = None,
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
            temp_model = DeleteCustomizedPropertyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDeviceRequest(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        project_id: str = None,
    ):
        self.device_id = device_id
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class DeleteDeviceResponseBody(TeaModel):
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


class DeleteDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDeviceResponseBody = None,
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
            temp_model = DeleteDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFunctionFileRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        file_name: str = None,
        file_type: int = None,
    ):
        self.project_id = project_id
        self.file_name = file_name
        self.file_type = file_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_type is not None:
            result['FileType'] = self.file_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        return self


class DeleteFunctionFileResponseBody(TeaModel):
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


class DeleteFunctionFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteFunctionFileResponseBody = None,
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
            temp_model = DeleteFunctionFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMqttRootTopicRequest(TeaModel):
    def __init__(
        self,
        app_key: str = None,
        root_topic: str = None,
        project_id: str = None,
    ):
        self.app_key = app_key
        self.root_topic = root_topic
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.root_topic is not None:
            result['RootTopic'] = self.root_topic
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('RootTopic') is not None:
            self.root_topic = m.get('RootTopic')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class DeleteMqttRootTopicResponseBody(TeaModel):
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


class DeleteMqttRootTopicResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteMqttRootTopicResponseBody = None,
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
            temp_model = DeleteMqttRootTopicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteNamespaceRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        namespace: str = None,
    ):
        self.project_id = project_id
        self.namespace = namespace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        return self


class DeleteNamespaceResponseBody(TeaModel):
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


class DeleteNamespaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteNamespaceResponseBody = None,
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
            temp_model = DeleteNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteOpenAccountRequest(TeaModel):
    def __init__(
        self,
        identity_id: str = None,
        project_id: str = None,
    ):
        self.identity_id = identity_id
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.identity_id is not None:
            result['IdentityId'] = self.identity_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdentityId') is not None:
            self.identity_id = m.get('IdentityId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class DeleteOpenAccountResponseBody(TeaModel):
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


class DeleteOpenAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteOpenAccountResponseBody = None,
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
            temp_model = DeleteOpenAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProjectAppRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        app_id: str = None,
    ):
        self.project_id = project_id
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class DeleteProjectAppResponseBody(TeaModel):
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


class DeleteProjectAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteProjectAppResponseBody = None,
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
            temp_model = DeleteProjectAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRpcServiceRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        project_id: str = None,
    ):
        self.id = id
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class DeleteRpcServiceResponseBody(TeaModel):
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


class DeleteRpcServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteRpcServiceResponseBody = None,
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
            temp_model = DeleteRpcServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSchemaSubscribeRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        project_id: str = None,
    ):
        self.id = id
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class DeleteSchemaSubscribeResponseBody(TeaModel):
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


class DeleteSchemaSubscribeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteSchemaSubscribeResponseBody = None,
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
            temp_model = DeleteSchemaSubscribeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteShadowSchemaRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        project_id: str = None,
    ):
        self.id = id
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class DeleteShadowSchemaResponseBody(TeaModel):
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


class DeleteShadowSchemaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteShadowSchemaResponseBody = None,
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
            temp_model = DeleteShadowSchemaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTriggerRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        id: int = None,
    ):
        self.project_id = project_id
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteTriggerResponseBody(TeaModel):
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


class DeleteTriggerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteTriggerResponseBody = None,
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
            temp_model = DeleteTriggerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUpstreamAppKeyRelationRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        project_id: str = None,
    ):
        self.id = id
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class DeleteUpstreamAppKeyRelationResponseBody(TeaModel):
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


class DeleteUpstreamAppKeyRelationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteUpstreamAppKeyRelationResponseBody = None,
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
            temp_model = DeleteUpstreamAppKeyRelationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUpstreamAppServerRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        id: int = None,
    ):
        self.project_id = project_id
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteUpstreamAppServerResponseBody(TeaModel):
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


class DeleteUpstreamAppServerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteUpstreamAppServerResponseBody = None,
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
            temp_model = DeleteUpstreamAppServerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVersionAllBlackDevicesRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        version_type: str = None,
        version_id: str = None,
    ):
        self.project_id = project_id
        self.version_type = version_type
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.version_type is not None:
            result['VersionType'] = self.version_type
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('VersionType') is not None:
            self.version_type = m.get('VersionType')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class DeleteVersionAllBlackDevicesResponseBody(TeaModel):
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


class DeleteVersionAllBlackDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteVersionAllBlackDevicesResponseBody = None,
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
            temp_model = DeleteVersionAllBlackDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVersionAllWhiteDevicesRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        version_type: str = None,
        version_id: str = None,
    ):
        self.project_id = project_id
        self.version_type = version_type
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.version_type is not None:
            result['VersionType'] = self.version_type
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('VersionType') is not None:
            self.version_type = m.get('VersionType')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class DeleteVersionAllWhiteDevicesResponseBody(TeaModel):
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


class DeleteVersionAllWhiteDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteVersionAllWhiteDevicesResponseBody = None,
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
            temp_model = DeleteVersionAllWhiteDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVersionBlackDevicesRequest(TeaModel):
    def __init__(
        self,
        device_ids: str = None,
        project_id: str = None,
        version_type: str = None,
        version_id: str = None,
        device_id_type: str = None,
    ):
        self.device_ids = device_ids
        self.project_id = project_id
        self.version_type = version_type
        self.version_id = version_id
        self.device_id_type = device_id_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.device_ids is not None:
            result['DeviceIds'] = self.device_ids
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.version_type is not None:
            result['VersionType'] = self.version_type
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.device_id_type is not None:
            result['DeviceIdType'] = self.device_id_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceIds') is not None:
            self.device_ids = m.get('DeviceIds')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('VersionType') is not None:
            self.version_type = m.get('VersionType')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('DeviceIdType') is not None:
            self.device_id_type = m.get('DeviceIdType')
        return self


class DeleteVersionBlackDevicesResponseBody(TeaModel):
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


class DeleteVersionBlackDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteVersionBlackDevicesResponseBody = None,
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
            temp_model = DeleteVersionBlackDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVersionBlackDevicesByIdRequest(TeaModel):
    def __init__(
        self,
        ids: str = None,
        project_id: str = None,
        version_type: str = None,
        version_id: str = None,
    ):
        self.ids = ids
        self.project_id = project_id
        self.version_type = version_type
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ids is not None:
            result['Ids'] = self.ids
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.version_type is not None:
            result['VersionType'] = self.version_type
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('VersionType') is not None:
            self.version_type = m.get('VersionType')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class DeleteVersionBlackDevicesByIdResponseBody(TeaModel):
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


class DeleteVersionBlackDevicesByIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteVersionBlackDevicesByIdResponseBody = None,
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
            temp_model = DeleteVersionBlackDevicesByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVersionDeviceGroupRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        id: str = None,
    ):
        self.project_id = project_id
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteVersionDeviceGroupResponseBody(TeaModel):
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


class DeleteVersionDeviceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteVersionDeviceGroupResponseBody = None,
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
            temp_model = DeleteVersionDeviceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVersionGroupDeviceRequest(TeaModel):
    def __init__(
        self,
        device_ids: str = None,
        project_id: str = None,
        device_group_id: str = None,
        device_id_type: str = None,
    ):
        self.device_ids = device_ids
        self.project_id = project_id
        self.device_group_id = device_group_id
        self.device_id_type = device_id_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.device_ids is not None:
            result['DeviceIds'] = self.device_ids
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id
        if self.device_id_type is not None:
            result['DeviceIdType'] = self.device_id_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceIds') is not None:
            self.device_ids = m.get('DeviceIds')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')
        if m.get('DeviceIdType') is not None:
            self.device_id_type = m.get('DeviceIdType')
        return self


class DeleteVersionGroupDeviceResponseBody(TeaModel):
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


class DeleteVersionGroupDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteVersionGroupDeviceResponseBody = None,
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
            temp_model = DeleteVersionGroupDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVersionGroupDeviceByIdRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        device_group_id: str = None,
        ids: str = None,
    ):
        self.project_id = project_id
        self.device_group_id = device_group_id
        self.ids = ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id
        if self.ids is not None:
            result['Ids'] = self.ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        return self


class DeleteVersionGroupDeviceByIdResponseBody(TeaModel):
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


class DeleteVersionGroupDeviceByIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteVersionGroupDeviceByIdResponseBody = None,
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
            temp_model = DeleteVersionGroupDeviceByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVersionTestRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        id: str = None,
    ):
        self.project_id = project_id
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteVersionTestResponseBody(TeaModel):
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


class DeleteVersionTestResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteVersionTestResponseBody = None,
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
            temp_model = DeleteVersionTestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVersionWhiteDevicesRequest(TeaModel):
    def __init__(
        self,
        device_ids: str = None,
        project_id: str = None,
        version_type: str = None,
        version_id: str = None,
        device_id_type: str = None,
    ):
        self.device_ids = device_ids
        self.project_id = project_id
        self.version_type = version_type
        self.version_id = version_id
        self.device_id_type = device_id_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.device_ids is not None:
            result['DeviceIds'] = self.device_ids
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.version_type is not None:
            result['VersionType'] = self.version_type
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.device_id_type is not None:
            result['DeviceIdType'] = self.device_id_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceIds') is not None:
            self.device_ids = m.get('DeviceIds')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('VersionType') is not None:
            self.version_type = m.get('VersionType')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('DeviceIdType') is not None:
            self.device_id_type = m.get('DeviceIdType')
        return self


class DeleteVersionWhiteDevicesResponseBody(TeaModel):
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


class DeleteVersionWhiteDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteVersionWhiteDevicesResponseBody = None,
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
            temp_model = DeleteVersionWhiteDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVersionWhiteDevicesByIdRequest(TeaModel):
    def __init__(
        self,
        ids: str = None,
        project_id: str = None,
        version_type: str = None,
        version_id: str = None,
    ):
        self.ids = ids
        self.project_id = project_id
        self.version_type = version_type
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ids is not None:
            result['Ids'] = self.ids
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.version_type is not None:
            result['VersionType'] = self.version_type
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('VersionType') is not None:
            self.version_type = m.get('VersionType')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class DeleteVersionWhiteDevicesByIdResponseBody(TeaModel):
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


class DeleteVersionWhiteDevicesByIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteVersionWhiteDevicesByIdResponseBody = None,
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
            temp_model = DeleteVersionWhiteDevicesByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeployFunctionFileRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        file_id: str = None,
        deploy_env: int = None,
    ):
        self.project_id = project_id
        self.file_id = file_id
        self.deploy_env = deploy_env

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.deploy_env is not None:
            result['DeployEnv'] = self.deploy_env
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('DeployEnv') is not None:
            self.deploy_env = m.get('DeployEnv')
        return self


class DeployFunctionFileResponseBody(TeaModel):
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


class DeployFunctionFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeployFunctionFileResponseBody = None,
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
            temp_model = DeployFunctionFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApiGatewayAppSecurityRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        gateway_app_id: str = None,
    ):
        self.project_id = project_id
        self.gateway_app_id = gateway_app_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.gateway_app_id is not None:
            result['GatewayAppId'] = self.gateway_app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('GatewayAppId') is not None:
            self.gateway_app_id = m.get('GatewayAppId')
        return self


class DescribeApiGatewayAppSecurityResponseBodyApiGatewayAppSecurity(TeaModel):
    def __init__(
        self,
        gateway_app_key: str = None,
        gateway_app_secret: str = None,
        gateway_app_id: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
    ):
        self.gateway_app_key = gateway_app_key
        self.gateway_app_secret = gateway_app_secret
        self.gateway_app_id = gateway_app_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.gateway_app_key is not None:
            result['GatewayAppKey'] = self.gateway_app_key
        if self.gateway_app_secret is not None:
            result['GatewayAppSecret'] = self.gateway_app_secret
        if self.gateway_app_id is not None:
            result['GatewayAppId'] = self.gateway_app_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayAppKey') is not None:
            self.gateway_app_key = m.get('GatewayAppKey')
        if m.get('GatewayAppSecret') is not None:
            self.gateway_app_secret = m.get('GatewayAppSecret')
        if m.get('GatewayAppId') is not None:
            self.gateway_app_id = m.get('GatewayAppId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        return self


class DescribeApiGatewayAppSecurityResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        api_gateway_app_security: DescribeApiGatewayAppSecurityResponseBodyApiGatewayAppSecurity = None,
    ):
        self.request_id = request_id
        self.api_gateway_app_security = api_gateway_app_security

    def validate(self):
        if self.api_gateway_app_security:
            self.api_gateway_app_security.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.api_gateway_app_security is not None:
            result['ApiGatewayAppSecurity'] = self.api_gateway_app_security.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ApiGatewayAppSecurity') is not None:
            temp_model = DescribeApiGatewayAppSecurityResponseBodyApiGatewayAppSecurity()
            self.api_gateway_app_security = temp_model.from_map(m['ApiGatewayAppSecurity'])
        return self


class DescribeApiGatewayAppSecurityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeApiGatewayAppSecurityResponseBody = None,
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
            temp_model = DescribeApiGatewayAppSecurityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppVersionRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        version_id: str = None,
    ):
        self.project_id = project_id
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class DescribeAppVersionResponseBodyAppVersionAdapters(TeaModel):
    def __init__(
        self,
        device_model_id: str = None,
        max_os_version: str = None,
        min_os_version: str = None,
        version_id: int = None,
        id: int = None,
        device_model_name: str = None,
    ):
        self.device_model_id = device_model_id
        self.max_os_version = max_os_version
        self.min_os_version = min_os_version
        self.version_id = version_id
        self.id = id
        self.device_model_name = device_model_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.device_model_id is not None:
            result['DeviceModelId'] = self.device_model_id
        if self.max_os_version is not None:
            result['MaxOsVersion'] = self.max_os_version
        if self.min_os_version is not None:
            result['MinOsVersion'] = self.min_os_version
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.id is not None:
            result['Id'] = self.id
        if self.device_model_name is not None:
            result['DeviceModelName'] = self.device_model_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceModelId') is not None:
            self.device_model_id = m.get('DeviceModelId')
        if m.get('MaxOsVersion') is not None:
            self.max_os_version = m.get('MaxOsVersion')
        if m.get('MinOsVersion') is not None:
            self.min_os_version = m.get('MinOsVersion')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('DeviceModelName') is not None:
            self.device_model_name = m.get('DeviceModelName')
        return self


class DescribeAppVersionResponseBodyAppVersion(TeaModel):
    def __init__(
        self,
        status: str = None,
        is_allow_new_install: str = None,
        release_note: str = None,
        package_name: str = None,
        remark: str = None,
        status_name: str = None,
        apk_md_5: str = None,
        restart_app_param: str = None,
        white_version_list: str = None,
        app_name: str = None,
        app_id: str = None,
        restart_app_type: str = None,
        version_code: int = None,
        black_version_list: str = None,
        gmt_modify: str = None,
        download_url: str = None,
        adapters: List[DescribeAppVersionResponseBodyAppVersionAdapters] = None,
        is_silent_upgrade: str = None,
        install_type: str = None,
        is_need_restart: str = None,
        size: str = None,
        restart_type: str = None,
        gmt_create: str = None,
        md_5: str = None,
        app_version: str = None,
        is_force_upgrade: str = None,
        id: int = None,
        original_url: str = None,
    ):
        self.status = status
        self.is_allow_new_install = is_allow_new_install
        self.release_note = release_note
        self.package_name = package_name
        self.remark = remark
        self.status_name = status_name
        self.apk_md_5 = apk_md_5
        self.restart_app_param = restart_app_param
        self.white_version_list = white_version_list
        self.app_name = app_name
        self.app_id = app_id
        self.restart_app_type = restart_app_type
        self.version_code = version_code
        self.black_version_list = black_version_list
        self.gmt_modify = gmt_modify
        self.download_url = download_url
        self.adapters = adapters
        self.is_silent_upgrade = is_silent_upgrade
        self.install_type = install_type
        self.is_need_restart = is_need_restart
        self.size = size
        self.restart_type = restart_type
        self.gmt_create = gmt_create
        self.md_5 = md_5
        self.app_version = app_version
        self.is_force_upgrade = is_force_upgrade
        self.id = id
        self.original_url = original_url

    def validate(self):
        if self.adapters:
            for k in self.adapters:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.is_allow_new_install is not None:
            result['IsAllowNewInstall'] = self.is_allow_new_install
        if self.release_note is not None:
            result['ReleaseNote'] = self.release_note
        if self.package_name is not None:
            result['PackageName'] = self.package_name
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status_name is not None:
            result['StatusName'] = self.status_name
        if self.apk_md_5 is not None:
            result['ApkMd5'] = self.apk_md_5
        if self.restart_app_param is not None:
            result['RestartAppParam'] = self.restart_app_param
        if self.white_version_list is not None:
            result['WhiteVersionList'] = self.white_version_list
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.restart_app_type is not None:
            result['RestartAppType'] = self.restart_app_type
        if self.version_code is not None:
            result['VersionCode'] = self.version_code
        if self.black_version_list is not None:
            result['BlackVersionList'] = self.black_version_list
        if self.gmt_modify is not None:
            result['GmtModify'] = self.gmt_modify
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        result['Adapters'] = []
        if self.adapters is not None:
            for k in self.adapters:
                result['Adapters'].append(k.to_map() if k else None)
        if self.is_silent_upgrade is not None:
            result['IsSilentUpgrade'] = self.is_silent_upgrade
        if self.install_type is not None:
            result['InstallType'] = self.install_type
        if self.is_need_restart is not None:
            result['IsNeedRestart'] = self.is_need_restart
        if self.size is not None:
            result['Size'] = self.size
        if self.restart_type is not None:
            result['RestartType'] = self.restart_type
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.is_force_upgrade is not None:
            result['IsForceUpgrade'] = self.is_force_upgrade
        if self.id is not None:
            result['Id'] = self.id
        if self.original_url is not None:
            result['OriginalUrl'] = self.original_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('IsAllowNewInstall') is not None:
            self.is_allow_new_install = m.get('IsAllowNewInstall')
        if m.get('ReleaseNote') is not None:
            self.release_note = m.get('ReleaseNote')
        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('StatusName') is not None:
            self.status_name = m.get('StatusName')
        if m.get('ApkMd5') is not None:
            self.apk_md_5 = m.get('ApkMd5')
        if m.get('RestartAppParam') is not None:
            self.restart_app_param = m.get('RestartAppParam')
        if m.get('WhiteVersionList') is not None:
            self.white_version_list = m.get('WhiteVersionList')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RestartAppType') is not None:
            self.restart_app_type = m.get('RestartAppType')
        if m.get('VersionCode') is not None:
            self.version_code = m.get('VersionCode')
        if m.get('BlackVersionList') is not None:
            self.black_version_list = m.get('BlackVersionList')
        if m.get('GmtModify') is not None:
            self.gmt_modify = m.get('GmtModify')
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        self.adapters = []
        if m.get('Adapters') is not None:
            for k in m.get('Adapters'):
                temp_model = DescribeAppVersionResponseBodyAppVersionAdapters()
                self.adapters.append(temp_model.from_map(k))
        if m.get('IsSilentUpgrade') is not None:
            self.is_silent_upgrade = m.get('IsSilentUpgrade')
        if m.get('InstallType') is not None:
            self.install_type = m.get('InstallType')
        if m.get('IsNeedRestart') is not None:
            self.is_need_restart = m.get('IsNeedRestart')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('RestartType') is not None:
            self.restart_type = m.get('RestartType')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('IsForceUpgrade') is not None:
            self.is_force_upgrade = m.get('IsForceUpgrade')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OriginalUrl') is not None:
            self.original_url = m.get('OriginalUrl')
        return self


class DescribeAppVersionResponseBody(TeaModel):
    def __init__(
        self,
        app_version: DescribeAppVersionResponseBodyAppVersion = None,
        request_id: str = None,
    ):
        self.app_version = app_version
        self.request_id = request_id

    def validate(self):
        if self.app_version:
            self.app_version.validate()

    def to_map(self):
        result = dict()
        if self.app_version is not None:
            result['AppVersion'] = self.app_version.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppVersion') is not None:
            temp_model = DescribeAppVersionResponseBodyAppVersion()
            self.app_version = temp_model.from_map(m['AppVersion'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAppVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAppVersionResponseBody = None,
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
            temp_model = DescribeAppVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAssistReportRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        assist_id: str = None,
    ):
        self.project_id = project_id
        self.assist_id = assist_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.assist_id is not None:
            result['AssistId'] = self.assist_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('AssistId') is not None:
            self.assist_id = m.get('AssistId')
        return self


class DescribeAssistReportResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        assist_result: str = None,
        assist_reason: str = None,
        assist_id: str = None,
        assist_description: str = None,
        assist_tag: str = None,
    ):
        self.request_id = request_id
        self.assist_result = assist_result
        self.assist_reason = assist_reason
        self.assist_id = assist_id
        self.assist_description = assist_description
        self.assist_tag = assist_tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.assist_result is not None:
            result['AssistResult'] = self.assist_result
        if self.assist_reason is not None:
            result['AssistReason'] = self.assist_reason
        if self.assist_id is not None:
            result['AssistId'] = self.assist_id
        if self.assist_description is not None:
            result['AssistDescription'] = self.assist_description
        if self.assist_tag is not None:
            result['AssistTag'] = self.assist_tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AssistResult') is not None:
            self.assist_result = m.get('AssistResult')
        if m.get('AssistReason') is not None:
            self.assist_reason = m.get('AssistReason')
        if m.get('AssistId') is not None:
            self.assist_id = m.get('AssistId')
        if m.get('AssistDescription') is not None:
            self.assist_description = m.get('AssistDescription')
        if m.get('AssistTag') is not None:
            self.assist_tag = m.get('AssistTag')
        return self


class DescribeAssistReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAssistReportResponseBody = None,
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
            temp_model = DescribeAssistReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAssistRTMPServerAddressRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        device_id: str = None,
    ):
        self.project_id = project_id
        self.device_id = device_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        return self


class DescribeAssistRTMPServerAddressResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        rtmpserver: str = None,
        otp: str = None,
    ):
        self.request_id = request_id
        self.rtmpserver = rtmpserver
        self.otp = otp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rtmpserver is not None:
            result['RTMPServer'] = self.rtmpserver
        if self.otp is not None:
            result['OTP'] = self.otp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RTMPServer') is not None:
            self.rtmpserver = m.get('RTMPServer')
        if m.get('OTP') is not None:
            self.otp = m.get('OTP')
        return self


class DescribeAssistRTMPServerAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAssistRTMPServerAddressResponseBody = None,
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
            temp_model = DescribeAssistRTMPServerAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAssistWSServerAddressRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        device_id: str = None,
    ):
        self.project_id = project_id
        self.device_id = device_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        return self


class DescribeAssistWSServerAddressResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        ws_server: str = None,
        otp: str = None,
    ):
        self.request_id = request_id
        self.ws_server = ws_server
        self.otp = otp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.ws_server is not None:
            result['WsServer'] = self.ws_server
        if self.otp is not None:
            result['OTP'] = self.otp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('WsServer') is not None:
            self.ws_server = m.get('WsServer')
        if m.get('OTP') is not None:
            self.otp = m.get('OTP')
        return self


class DescribeAssistWSServerAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAssistWSServerAddressResponseBody = None,
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
            temp_model = DescribeAssistWSServerAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCustomizedFilterRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        id: str = None,
    ):
        self.project_id = project_id
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeCustomizedFilterResponseBodyCustomizedFilter(TeaModel):
    def __init__(
        self,
        gmt_create_timestamp: int = None,
        gmt_modify: str = None,
        value_compare_type: str = None,
        version_id: int = None,
        gmt_modify_timestamp: int = None,
        value: str = None,
        value_type: str = None,
        gmt_create: str = None,
        black_white_type: str = None,
        name: str = None,
        version_type: str = None,
        id: int = None,
    ):
        self.gmt_create_timestamp = gmt_create_timestamp
        self.gmt_modify = gmt_modify
        self.value_compare_type = value_compare_type
        self.version_id = version_id
        self.gmt_modify_timestamp = gmt_modify_timestamp
        self.value = value
        self.value_type = value_type
        self.gmt_create = gmt_create
        self.black_white_type = black_white_type
        self.name = name
        self.version_type = version_type
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.gmt_create_timestamp is not None:
            result['GmtCreateTimestamp'] = self.gmt_create_timestamp
        if self.gmt_modify is not None:
            result['GmtModify'] = self.gmt_modify
        if self.value_compare_type is not None:
            result['ValueCompareType'] = self.value_compare_type
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.gmt_modify_timestamp is not None:
            result['GmtModifyTimestamp'] = self.gmt_modify_timestamp
        if self.value is not None:
            result['Value'] = self.value
        if self.value_type is not None:
            result['ValueType'] = self.value_type
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.black_white_type is not None:
            result['BlackWhiteType'] = self.black_white_type
        if self.name is not None:
            result['Name'] = self.name
        if self.version_type is not None:
            result['VersionType'] = self.version_type
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreateTimestamp') is not None:
            self.gmt_create_timestamp = m.get('GmtCreateTimestamp')
        if m.get('GmtModify') is not None:
            self.gmt_modify = m.get('GmtModify')
        if m.get('ValueCompareType') is not None:
            self.value_compare_type = m.get('ValueCompareType')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('GmtModifyTimestamp') is not None:
            self.gmt_modify_timestamp = m.get('GmtModifyTimestamp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('ValueType') is not None:
            self.value_type = m.get('ValueType')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('BlackWhiteType') is not None:
            self.black_white_type = m.get('BlackWhiteType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('VersionType') is not None:
            self.version_type = m.get('VersionType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeCustomizedFilterResponseBody(TeaModel):
    def __init__(
        self,
        customized_filter: DescribeCustomizedFilterResponseBodyCustomizedFilter = None,
        request_id: str = None,
    ):
        self.customized_filter = customized_filter
        self.request_id = request_id

    def validate(self):
        if self.customized_filter:
            self.customized_filter.validate()

    def to_map(self):
        result = dict()
        if self.customized_filter is not None:
            result['CustomizedFilter'] = self.customized_filter.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomizedFilter') is not None:
            temp_model = DescribeCustomizedFilterResponseBodyCustomizedFilter()
            self.customized_filter = temp_model.from_map(m['CustomizedFilter'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCustomizedFilterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCustomizedFilterResponseBody = None,
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
            temp_model = DescribeCustomizedFilterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDefaultSchemaRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        device_model_id: str = None,
    ):
        self.project_id = project_id
        self.device_model_id = device_model_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.device_model_id is not None:
            result['DeviceModelId'] = self.device_model_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('DeviceModelId') is not None:
            self.device_model_id = m.get('DeviceModelId')
        return self


class DescribeDefaultSchemaResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        schema: str = None,
    ):
        self.request_id = request_id
        self.schema = schema

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.schema is not None:
            result['Schema'] = self.schema
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Schema') is not None:
            self.schema = m.get('Schema')
        return self


class DescribeDefaultSchemaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDefaultSchemaResponseBody = None,
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
            temp_model = DescribeDefaultSchemaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDeviceRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        device_id: str = None,
    ):
        self.project_id = project_id
        self.device_id = device_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        return self


class DescribeDeviceResponseBodyDeviceInfo(TeaModel):
    def __init__(
        self,
        serial_number: str = None,
        status: str = None,
        device_model_id: int = None,
        mac_address: str = None,
        device_id: str = None,
        device_type: str = None,
        project_id: str = None,
        os_platform: str = None,
        device_model: str = None,
        usage_type: int = None,
        vin: str = None,
        usage_type_desc: str = None,
        uuid: str = None,
        hardware_id: str = None,
        device_brand_id: int = None,
        region: str = None,
        attributes: str = None,
        software_id: str = None,
        name: str = None,
        device_brand: str = None,
        device_product: str = None,
    ):
        self.serial_number = serial_number
        self.status = status
        self.device_model_id = device_model_id
        self.mac_address = mac_address
        self.device_id = device_id
        self.device_type = device_type
        self.project_id = project_id
        self.os_platform = os_platform
        self.device_model = device_model
        self.usage_type = usage_type
        self.vin = vin
        self.usage_type_desc = usage_type_desc
        self.uuid = uuid
        self.hardware_id = hardware_id
        self.device_brand_id = device_brand_id
        self.region = region
        self.attributes = attributes
        self.software_id = software_id
        self.name = name
        self.device_brand = device_brand
        self.device_product = device_product

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.status is not None:
            result['Status'] = self.status
        if self.device_model_id is not None:
            result['DeviceModelId'] = self.device_model_id
        if self.mac_address is not None:
            result['MacAddress'] = self.mac_address
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.os_platform is not None:
            result['OsPlatform'] = self.os_platform
        if self.device_model is not None:
            result['DeviceModel'] = self.device_model
        if self.usage_type is not None:
            result['UsageType'] = self.usage_type
        if self.vin is not None:
            result['Vin'] = self.vin
        if self.usage_type_desc is not None:
            result['UsageTypeDesc'] = self.usage_type_desc
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.hardware_id is not None:
            result['HardwareId'] = self.hardware_id
        if self.device_brand_id is not None:
            result['DeviceBrandId'] = self.device_brand_id
        if self.region is not None:
            result['Region'] = self.region
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.software_id is not None:
            result['SoftwareId'] = self.software_id
        if self.name is not None:
            result['Name'] = self.name
        if self.device_brand is not None:
            result['DeviceBrand'] = self.device_brand
        if self.device_product is not None:
            result['DeviceProduct'] = self.device_product
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('DeviceModelId') is not None:
            self.device_model_id = m.get('DeviceModelId')
        if m.get('MacAddress') is not None:
            self.mac_address = m.get('MacAddress')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('OsPlatform') is not None:
            self.os_platform = m.get('OsPlatform')
        if m.get('DeviceModel') is not None:
            self.device_model = m.get('DeviceModel')
        if m.get('UsageType') is not None:
            self.usage_type = m.get('UsageType')
        if m.get('Vin') is not None:
            self.vin = m.get('Vin')
        if m.get('UsageTypeDesc') is not None:
            self.usage_type_desc = m.get('UsageTypeDesc')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('HardwareId') is not None:
            self.hardware_id = m.get('HardwareId')
        if m.get('DeviceBrandId') is not None:
            self.device_brand_id = m.get('DeviceBrandId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('SoftwareId') is not None:
            self.software_id = m.get('SoftwareId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('DeviceBrand') is not None:
            self.device_brand = m.get('DeviceBrand')
        if m.get('DeviceProduct') is not None:
            self.device_product = m.get('DeviceProduct')
        return self


class DescribeDeviceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        device_info: DescribeDeviceResponseBodyDeviceInfo = None,
    ):
        self.request_id = request_id
        self.device_info = device_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DeviceInfo') is not None:
            temp_model = DescribeDeviceResponseBodyDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        return self


class DescribeDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDeviceResponseBody = None,
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
            temp_model = DescribeDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDeviceBrandRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        device_brand_id: int = None,
        device_brand: str = None,
        start: str = None,
        length: str = None,
    ):
        self.project_id = project_id
        self.device_brand_id = device_brand_id
        self.device_brand = device_brand
        self.start = start
        self.length = length

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.device_brand_id is not None:
            result['DeviceBrandId'] = self.device_brand_id
        if self.device_brand is not None:
            result['DeviceBrand'] = self.device_brand
        if self.start is not None:
            result['Start'] = self.start
        if self.length is not None:
            result['Length'] = self.length
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('DeviceBrandId') is not None:
            self.device_brand_id = m.get('DeviceBrandId')
        if m.get('DeviceBrand') is not None:
            self.device_brand = m.get('DeviceBrand')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        if m.get('Length') is not None:
            self.length = m.get('Length')
        return self


class DescribeDeviceBrandResponseBodyDeviceBrand(TeaModel):
    def __init__(
        self,
        device_brand_id: int = None,
        description: str = None,
        project_id: str = None,
        manufacture: str = None,
        device_brand: str = None,
    ):
        self.device_brand_id = device_brand_id
        self.description = description
        self.project_id = project_id
        self.manufacture = manufacture
        self.device_brand = device_brand

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.device_brand_id is not None:
            result['DeviceBrandId'] = self.device_brand_id
        if self.description is not None:
            result['Description'] = self.description
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.manufacture is not None:
            result['Manufacture'] = self.manufacture
        if self.device_brand is not None:
            result['DeviceBrand'] = self.device_brand
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceBrandId') is not None:
            self.device_brand_id = m.get('DeviceBrandId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Manufacture') is not None:
            self.manufacture = m.get('Manufacture')
        if m.get('DeviceBrand') is not None:
            self.device_brand = m.get('DeviceBrand')
        return self


class DescribeDeviceBrandResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        device_brand: DescribeDeviceBrandResponseBodyDeviceBrand = None,
    ):
        self.request_id = request_id
        self.device_brand = device_brand

    def validate(self):
        if self.device_brand:
            self.device_brand.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.device_brand is not None:
            result['DeviceBrand'] = self.device_brand.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DeviceBrand') is not None:
            temp_model = DescribeDeviceBrandResponseBodyDeviceBrand()
            self.device_brand = temp_model.from_map(m['DeviceBrand'])
        return self


class DescribeDeviceBrandResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDeviceBrandResponseBody = None,
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
            temp_model = DescribeDeviceBrandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDeviceIdByOuterInfoRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        query_type: str = None,
        query_value: str = None,
    ):
        self.project_id = project_id
        self.query_type = query_type
        self.query_value = query_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.query_type is not None:
            result['QueryType'] = self.query_type
        if self.query_value is not None:
            result['QueryValue'] = self.query_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')
        if m.get('QueryValue') is not None:
            self.query_value = m.get('QueryValue')
        return self


class DescribeDeviceIdByOuterInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        device_id: str = None,
    ):
        self.request_id = request_id
        self.device_id = device_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        return self


class DescribeDeviceIdByOuterInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDeviceIdByOuterInfoResponseBody = None,
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
            temp_model = DescribeDeviceIdByOuterInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDeviceInfoRequest(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        device_token: str = None,
        project_id: str = None,
    ):
        self.device_id = device_id
        self.device_token = device_token
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.device_token is not None:
            result['DeviceToken'] = self.device_token
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('DeviceToken') is not None:
            self.device_token = m.get('DeviceToken')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class DescribeDeviceInfoResponseBodyDeviceInfo(TeaModel):
    def __init__(
        self,
        serial_number: str = None,
        status: str = None,
        device_model_id: int = None,
        mac_address: str = None,
        device_id: str = None,
        device_type: str = None,
        project_id: str = None,
        device_model: str = None,
        usage_type: int = None,
        vin: str = None,
        usage_type_desc: str = None,
        uuid: str = None,
        hardware_id: str = None,
        region: str = None,
        software_id: str = None,
        name: str = None,
        device_brand: str = None,
    ):
        self.serial_number = serial_number
        self.status = status
        self.device_model_id = device_model_id
        self.mac_address = mac_address
        self.device_id = device_id
        self.device_type = device_type
        self.project_id = project_id
        self.device_model = device_model
        self.usage_type = usage_type
        self.vin = vin
        self.usage_type_desc = usage_type_desc
        self.uuid = uuid
        self.hardware_id = hardware_id
        self.region = region
        self.software_id = software_id
        self.name = name
        self.device_brand = device_brand

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.status is not None:
            result['Status'] = self.status
        if self.device_model_id is not None:
            result['DeviceModelId'] = self.device_model_id
        if self.mac_address is not None:
            result['MacAddress'] = self.mac_address
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.device_model is not None:
            result['DeviceModel'] = self.device_model
        if self.usage_type is not None:
            result['UsageType'] = self.usage_type
        if self.vin is not None:
            result['Vin'] = self.vin
        if self.usage_type_desc is not None:
            result['UsageTypeDesc'] = self.usage_type_desc
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.hardware_id is not None:
            result['HardwareId'] = self.hardware_id
        if self.region is not None:
            result['Region'] = self.region
        if self.software_id is not None:
            result['SoftwareId'] = self.software_id
        if self.name is not None:
            result['Name'] = self.name
        if self.device_brand is not None:
            result['DeviceBrand'] = self.device_brand
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('DeviceModelId') is not None:
            self.device_model_id = m.get('DeviceModelId')
        if m.get('MacAddress') is not None:
            self.mac_address = m.get('MacAddress')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('DeviceModel') is not None:
            self.device_model = m.get('DeviceModel')
        if m.get('UsageType') is not None:
            self.usage_type = m.get('UsageType')
        if m.get('Vin') is not None:
            self.vin = m.get('Vin')
        if m.get('UsageTypeDesc') is not None:
            self.usage_type_desc = m.get('UsageTypeDesc')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('HardwareId') is not None:
            self.hardware_id = m.get('HardwareId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('SoftwareId') is not None:
            self.software_id = m.get('SoftwareId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('DeviceBrand') is not None:
            self.device_brand = m.get('DeviceBrand')
        return self


class DescribeDeviceInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        device_info: DescribeDeviceInfoResponseBodyDeviceInfo = None,
    ):
        self.request_id = request_id
        self.device_info = device_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DeviceInfo') is not None:
            temp_model = DescribeDeviceInfoResponseBodyDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        return self


class DescribeDeviceInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDeviceInfoResponseBody = None,
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
            temp_model = DescribeDeviceInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDeviceModelRequest(TeaModel):
    def __init__(
        self,
        device_model_id: int = None,
        device_model: str = None,
        project_id: str = None,
    ):
        self.device_model_id = device_model_id
        self.device_model = device_model
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.device_model_id is not None:
            result['DeviceModelId'] = self.device_model_id
        if self.device_model is not None:
            result['DeviceModel'] = self.device_model
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceModelId') is not None:
            self.device_model_id = m.get('DeviceModelId')
        if m.get('DeviceModel') is not None:
            self.device_model = m.get('DeviceModel')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class DescribeDeviceModelResponseBodyDeviceModel(TeaModel):
    def __init__(
        self,
        device_model_id: int = None,
        hardware_type: str = None,
        device_name: str = None,
        device_type: str = None,
        can_create_device_id: int = None,
        project_id: str = None,
        os_platform: str = None,
        device_model: str = None,
        security_chip: str = None,
        device_logo_url: str = None,
        description: str = None,
        object_key: str = None,
        init_usage_type_desc: str = None,
        init_usage_type: int = None,
        device_brand: str = None,
    ):
        self.device_model_id = device_model_id
        self.hardware_type = hardware_type
        self.device_name = device_name
        self.device_type = device_type
        self.can_create_device_id = can_create_device_id
        self.project_id = project_id
        self.os_platform = os_platform
        self.device_model = device_model
        self.security_chip = security_chip
        self.device_logo_url = device_logo_url
        self.description = description
        self.object_key = object_key
        self.init_usage_type_desc = init_usage_type_desc
        self.init_usage_type = init_usage_type
        self.device_brand = device_brand

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.device_model_id is not None:
            result['DeviceModelId'] = self.device_model_id
        if self.hardware_type is not None:
            result['HardwareType'] = self.hardware_type
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.can_create_device_id is not None:
            result['CanCreateDeviceId'] = self.can_create_device_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.os_platform is not None:
            result['OsPlatform'] = self.os_platform
        if self.device_model is not None:
            result['DeviceModel'] = self.device_model
        if self.security_chip is not None:
            result['SecurityChip'] = self.security_chip
        if self.device_logo_url is not None:
            result['DeviceLogoUrl'] = self.device_logo_url
        if self.description is not None:
            result['Description'] = self.description
        if self.object_key is not None:
            result['ObjectKey'] = self.object_key
        if self.init_usage_type_desc is not None:
            result['InitUsageTypeDesc'] = self.init_usage_type_desc
        if self.init_usage_type is not None:
            result['InitUsageType'] = self.init_usage_type
        if self.device_brand is not None:
            result['DeviceBrand'] = self.device_brand
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceModelId') is not None:
            self.device_model_id = m.get('DeviceModelId')
        if m.get('HardwareType') is not None:
            self.hardware_type = m.get('HardwareType')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('CanCreateDeviceId') is not None:
            self.can_create_device_id = m.get('CanCreateDeviceId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('OsPlatform') is not None:
            self.os_platform = m.get('OsPlatform')
        if m.get('DeviceModel') is not None:
            self.device_model = m.get('DeviceModel')
        if m.get('SecurityChip') is not None:
            self.security_chip = m.get('SecurityChip')
        if m.get('DeviceLogoUrl') is not None:
            self.device_logo_url = m.get('DeviceLogoUrl')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ObjectKey') is not None:
            self.object_key = m.get('ObjectKey')
        if m.get('InitUsageTypeDesc') is not None:
            self.init_usage_type_desc = m.get('InitUsageTypeDesc')
        if m.get('InitUsageType') is not None:
            self.init_usage_type = m.get('InitUsageType')
        if m.get('DeviceBrand') is not None:
            self.device_brand = m.get('DeviceBrand')
        return self


class DescribeDeviceModelResponseBody(TeaModel):
    def __init__(
        self,
        device_model: DescribeDeviceModelResponseBodyDeviceModel = None,
        request_id: str = None,
    ):
        self.device_model = device_model
        self.request_id = request_id

    def validate(self):
        if self.device_model:
            self.device_model.validate()

    def to_map(self):
        result = dict()
        if self.device_model is not None:
            result['DeviceModel'] = self.device_model.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceModel') is not None:
            temp_model = DescribeDeviceModelResponseBodyDeviceModel()
            self.device_model = temp_model.from_map(m['DeviceModel'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDeviceModelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDeviceModelResponseBody = None,
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
            temp_model = DescribeDeviceModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDeviceOnlineInfoRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        type: str = None,
        value: str = None,
    ):
        self.project_id = project_id
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDeviceOnlineInfoResponseBodyDevices(TeaModel):
    def __init__(
        self,
        login_time: int = None,
        device_id: str = None,
        online: int = None,
        project_id: str = None,
        ias_id: str = None,
        system_version: str = None,
        terminal: str = None,
        client_version: str = None,
    ):
        self.login_time = login_time
        self.device_id = device_id
        self.online = online
        self.project_id = project_id
        self.ias_id = ias_id
        self.system_version = system_version
        self.terminal = terminal
        self.client_version = client_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.login_time is not None:
            result['LoginTime'] = self.login_time
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.online is not None:
            result['Online'] = self.online
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.ias_id is not None:
            result['IasId'] = self.ias_id
        if self.system_version is not None:
            result['SystemVersion'] = self.system_version
        if self.terminal is not None:
            result['Terminal'] = self.terminal
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoginTime') is not None:
            self.login_time = m.get('LoginTime')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('Online') is not None:
            self.online = m.get('Online')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('IasId') is not None:
            self.ias_id = m.get('IasId')
        if m.get('SystemVersion') is not None:
            self.system_version = m.get('SystemVersion')
        if m.get('Terminal') is not None:
            self.terminal = m.get('Terminal')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        return self


class DescribeDeviceOnlineInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        devices: List[DescribeDeviceOnlineInfoResponseBodyDevices] = None,
    ):
        self.request_id = request_id
        self.devices = devices

    def validate(self):
        if self.devices:
            for k in self.devices:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Devices'] = []
        if self.devices is not None:
            for k in self.devices:
                result['Devices'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.devices = []
        if m.get('Devices') is not None:
            for k in m.get('Devices'):
                temp_model = DescribeDeviceOnlineInfoResponseBodyDevices()
                self.devices.append(temp_model.from_map(k))
        return self


class DescribeDeviceOnlineInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDeviceOnlineInfoResponseBody = None,
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
            temp_model = DescribeDeviceOnlineInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDeviceShadowRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        device_id: str = None,
        device_model: str = None,
        path: str = None,
        view_subscribed: bool = None,
    ):
        self.project_id = project_id
        self.device_id = device_id
        self.device_model = device_model
        self.path = path
        self.view_subscribed = view_subscribed

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.device_model is not None:
            result['DeviceModel'] = self.device_model
        if self.path is not None:
            result['Path'] = self.path
        if self.view_subscribed is not None:
            result['ViewSubscribed'] = self.view_subscribed
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('DeviceModel') is not None:
            self.device_model = m.get('DeviceModel')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('ViewSubscribed') is not None:
            self.view_subscribed = m.get('ViewSubscribed')
        return self


class DescribeDeviceShadowResponseBodyDeviceShadow(TeaModel):
    def __init__(
        self,
        device_shadow: str = None,
        device_info: str = None,
    ):
        self.device_shadow = device_shadow
        self.device_info = device_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.device_shadow is not None:
            result['DeviceShadow'] = self.device_shadow
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceShadow') is not None:
            self.device_shadow = m.get('DeviceShadow')
        if m.get('DeviceInfo') is not None:
            self.device_info = m.get('DeviceInfo')
        return self


class DescribeDeviceShadowResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        device_shadow: DescribeDeviceShadowResponseBodyDeviceShadow = None,
    ):
        self.request_id = request_id
        self.device_shadow = device_shadow

    def validate(self):
        if self.device_shadow:
            self.device_shadow.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.device_shadow is not None:
            result['DeviceShadow'] = self.device_shadow.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DeviceShadow') is not None:
            temp_model = DescribeDeviceShadowResponseBodyDeviceShadow()
            self.device_shadow = temp_model.from_map(m['DeviceShadow'])
        return self


class DescribeDeviceShadowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDeviceShadowResponseBody = None,
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
            temp_model = DescribeDeviceShadowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDeviceValiditySchemaRequest(TeaModel):
    def __init__(
        self,
        device_model: str = None,
        schema_version: str = None,
        project_id: str = None,
    ):
        self.device_model = device_model
        self.schema_version = schema_version
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.device_model is not None:
            result['DeviceModel'] = self.device_model
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceModel') is not None:
            self.device_model = m.get('DeviceModel')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class DescribeDeviceValiditySchemaResponseBodyItemList(TeaModel):
    def __init__(
        self,
        minimum: float = None,
        type: str = None,
        maximum: float = None,
        item_type: str = None,
        enum_list_str: str = None,
        exclusive_minimum: bool = None,
        max_length: int = None,
        required: str = None,
        description: str = None,
        exclusive_maximum: bool = None,
        path: str = None,
        min_length: int = None,
    ):
        self.minimum = minimum
        self.type = type
        self.maximum = maximum
        self.item_type = item_type
        self.enum_list_str = enum_list_str
        self.exclusive_minimum = exclusive_minimum
        self.max_length = max_length
        self.required = required
        self.description = description
        self.exclusive_maximum = exclusive_maximum
        self.path = path
        self.min_length = min_length

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.minimum is not None:
            result['Minimum'] = self.minimum
        if self.type is not None:
            result['Type'] = self.type
        if self.maximum is not None:
            result['Maximum'] = self.maximum
        if self.item_type is not None:
            result['ItemType'] = self.item_type
        if self.enum_list_str is not None:
            result['EnumListStr'] = self.enum_list_str
        if self.exclusive_minimum is not None:
            result['ExclusiveMinimum'] = self.exclusive_minimum
        if self.max_length is not None:
            result['MaxLength'] = self.max_length
        if self.required is not None:
            result['Required'] = self.required
        if self.description is not None:
            result['Description'] = self.description
        if self.exclusive_maximum is not None:
            result['ExclusiveMaximum'] = self.exclusive_maximum
        if self.path is not None:
            result['Path'] = self.path
        if self.min_length is not None:
            result['MinLength'] = self.min_length
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Minimum') is not None:
            self.minimum = m.get('Minimum')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Maximum') is not None:
            self.maximum = m.get('Maximum')
        if m.get('ItemType') is not None:
            self.item_type = m.get('ItemType')
        if m.get('EnumListStr') is not None:
            self.enum_list_str = m.get('EnumListStr')
        if m.get('ExclusiveMinimum') is not None:
            self.exclusive_minimum = m.get('ExclusiveMinimum')
        if m.get('MaxLength') is not None:
            self.max_length = m.get('MaxLength')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExclusiveMaximum') is not None:
            self.exclusive_maximum = m.get('ExclusiveMaximum')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('MinLength') is not None:
            self.min_length = m.get('MinLength')
        return self


class DescribeDeviceValiditySchemaResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        item_list: List[DescribeDeviceValiditySchemaResponseBodyItemList] = None,
    ):
        self.request_id = request_id
        self.item_list = item_list

    def validate(self):
        if self.item_list:
            for k in self.item_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ItemList'] = []
        if self.item_list is not None:
            for k in self.item_list:
                result['ItemList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.item_list = []
        if m.get('ItemList') is not None:
            for k in m.get('ItemList'):
                temp_model = DescribeDeviceValiditySchemaResponseBodyItemList()
                self.item_list.append(temp_model.from_map(k))
        return self


class DescribeDeviceValiditySchemaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDeviceValiditySchemaResponseBody = None,
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
            temp_model = DescribeDeviceValiditySchemaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMessageRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        message_id: int = None,
    ):
        self.project_id = project_id
        self.message_id = message_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        return self


class DescribeMessageResponseBodyMessage(TeaModel):
    def __init__(
        self,
        type: int = None,
        action: str = None,
        project_id: str = None,
        predict_send_cnt: int = None,
        uri: str = None,
        desc: str = None,
        audit_msg: str = None,
        app_name: str = None,
        app_key: str = None,
        gmt_create_time: int = None,
        exipired_time: int = None,
        ack_cnt: int = None,
        title: str = None,
        parameter: str = None,
        audit: int = None,
        id: int = None,
        send_status: int = None,
    ):
        self.type = type
        self.action = action
        self.project_id = project_id
        self.predict_send_cnt = predict_send_cnt
        self.uri = uri
        self.desc = desc
        self.audit_msg = audit_msg
        self.app_name = app_name
        self.app_key = app_key
        self.gmt_create_time = gmt_create_time
        self.exipired_time = exipired_time
        self.ack_cnt = ack_cnt
        self.title = title
        self.parameter = parameter
        self.audit = audit
        self.id = id
        self.send_status = send_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.action is not None:
            result['Action'] = self.action
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.predict_send_cnt is not None:
            result['PredictSendCnt'] = self.predict_send_cnt
        if self.uri is not None:
            result['Uri'] = self.uri
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.audit_msg is not None:
            result['AuditMsg'] = self.audit_msg
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.exipired_time is not None:
            result['ExipiredTime'] = self.exipired_time
        if self.ack_cnt is not None:
            result['AckCnt'] = self.ack_cnt
        if self.title is not None:
            result['Title'] = self.title
        if self.parameter is not None:
            result['Parameter'] = self.parameter
        if self.audit is not None:
            result['Audit'] = self.audit
        if self.id is not None:
            result['Id'] = self.id
        if self.send_status is not None:
            result['SendStatus'] = self.send_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('PredictSendCnt') is not None:
            self.predict_send_cnt = m.get('PredictSendCnt')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('AuditMsg') is not None:
            self.audit_msg = m.get('AuditMsg')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('ExipiredTime') is not None:
            self.exipired_time = m.get('ExipiredTime')
        if m.get('AckCnt') is not None:
            self.ack_cnt = m.get('AckCnt')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Parameter') is not None:
            self.parameter = m.get('Parameter')
        if m.get('Audit') is not None:
            self.audit = m.get('Audit')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('SendStatus') is not None:
            self.send_status = m.get('SendStatus')
        return self


class DescribeMessageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: DescribeMessageResponseBodyMessage = None,
    ):
        self.request_id = request_id
        self.message = message

    def validate(self):
        if self.message:
            self.message.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            temp_model = DescribeMessageResponseBodyMessage()
            self.message = temp_model.from_map(m['Message'])
        return self


class DescribeMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeMessageResponseBody = None,
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
            temp_model = DescribeMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMqttClientStatusRequest(TeaModel):
    def __init__(
        self,
        app_key: str = None,
        client_id: str = None,
        project_id: str = None,
    ):
        self.app_key = app_key
        self.client_id = client_id
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class DescribeMqttClientStatusResponseBodyClientStatus(TeaModel):
    def __init__(
        self,
        status: int = None,
        clean_session: str = None,
        last_update: int = None,
    ):
        self.status = status
        self.clean_session = clean_session
        self.last_update = last_update

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.clean_session is not None:
            result['CleanSession'] = self.clean_session
        if self.last_update is not None:
            result['LastUpdate'] = self.last_update
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CleanSession') is not None:
            self.clean_session = m.get('CleanSession')
        if m.get('LastUpdate') is not None:
            self.last_update = m.get('LastUpdate')
        return self


class DescribeMqttClientStatusResponseBody(TeaModel):
    def __init__(
        self,
        client_status: DescribeMqttClientStatusResponseBodyClientStatus = None,
        request_id: str = None,
    ):
        self.client_status = client_status
        self.request_id = request_id

    def validate(self):
        if self.client_status:
            self.client_status.validate()

    def to_map(self):
        result = dict()
        if self.client_status is not None:
            result['ClientStatus'] = self.client_status.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientStatus') is not None:
            temp_model = DescribeMqttClientStatusResponseBodyClientStatus()
            self.client_status = temp_model.from_map(m['ClientStatus'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeMqttClientStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeMqttClientStatusResponseBody = None,
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
            temp_model = DescribeMqttClientStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMqttMessageRequest(TeaModel):
    def __init__(
        self,
        app_key: str = None,
        mid: str = None,
        project_id: str = None,
    ):
        self.app_key = app_key
        self.mid = mid
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.mid is not None:
            result['Mid'] = self.mid
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('Mid') is not None:
            self.mid = m.get('Mid')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class DescribeMqttMessageResponseBodyMessage(TeaModel):
    def __init__(
        self,
        time: int = None,
        app_key: str = None,
        mid: str = None,
        topic: str = None,
        payload: str = None,
        qo_s: int = None,
    ):
        self.time = time
        self.app_key = app_key
        self.mid = mid
        self.topic = topic
        self.payload = payload
        self.qo_s = qo_s

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.time is not None:
            result['Time'] = self.time
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.mid is not None:
            result['Mid'] = self.mid
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.payload is not None:
            result['Payload'] = self.payload
        if self.qo_s is not None:
            result['QoS'] = self.qo_s
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('Mid') is not None:
            self.mid = m.get('Mid')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('Payload') is not None:
            self.payload = m.get('Payload')
        if m.get('QoS') is not None:
            self.qo_s = m.get('QoS')
        return self


class DescribeMqttMessageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: DescribeMqttMessageResponseBodyMessage = None,
    ):
        self.request_id = request_id
        self.message = message

    def validate(self):
        if self.message:
            self.message.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            temp_model = DescribeMqttMessageResponseBodyMessage()
            self.message = temp_model.from_map(m['Message'])
        return self


class DescribeMqttMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeMqttMessageResponseBody = None,
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
            temp_model = DescribeMqttMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMqttTopicSubscriptionRequest(TeaModel):
    def __init__(
        self,
        app_key: str = None,
        topic: str = None,
        project_id: str = None,
    ):
        self.app_key = app_key
        self.topic = topic
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class DescribeMqttTopicSubscriptionResponseBodySubscription(TeaModel):
    def __init__(
        self,
        topic: str = None,
        count: int = None,
    ):
        self.topic = topic
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeMqttTopicSubscriptionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        subscription: DescribeMqttTopicSubscriptionResponseBodySubscription = None,
    ):
        self.request_id = request_id
        self.subscription = subscription

    def validate(self):
        if self.subscription:
            self.subscription.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.subscription is not None:
            result['Subscription'] = self.subscription.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Subscription') is not None:
            temp_model = DescribeMqttTopicSubscriptionResponseBodySubscription()
            self.subscription = temp_model.from_map(m['Subscription'])
        return self


class DescribeMqttTopicSubscriptionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeMqttTopicSubscriptionResponseBody = None,
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
            temp_model = DescribeMqttTopicSubscriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOpenAccountRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        identity_id: str = None,
        idp: str = None,
        id_token: str = None,
        open_id: str = None,
    ):
        self.project_id = project_id
        self.identity_id = identity_id
        self.idp = idp
        self.id_token = id_token
        self.open_id = open_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.identity_id is not None:
            result['IdentityId'] = self.identity_id
        if self.idp is not None:
            result['Idp'] = self.idp
        if self.id_token is not None:
            result['IdToken'] = self.id_token
        if self.open_id is not None:
            result['OpenId'] = self.open_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('IdentityId') is not None:
            self.identity_id = m.get('IdentityId')
        if m.get('Idp') is not None:
            self.idp = m.get('Idp')
        if m.get('IdToken') is not None:
            self.id_token = m.get('IdToken')
        if m.get('OpenId') is not None:
            self.open_id = m.get('OpenId')
        return self


class DescribeOpenAccountResponseBodyOpenAccount(TeaModel):
    def __init__(
        self,
        status: int = None,
        type: int = None,
        display_name: str = None,
        create_access_key: str = None,
        open_id: str = None,
        mobile: str = None,
        region: str = None,
        identity_id: str = None,
        login_id: str = None,
        idp: str = None,
        aliyun_id: str = None,
    ):
        self.status = status
        self.type = type
        self.display_name = display_name
        self.create_access_key = create_access_key
        self.open_id = open_id
        self.mobile = mobile
        self.region = region
        self.identity_id = identity_id
        self.login_id = login_id
        self.idp = idp
        self.aliyun_id = aliyun_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.create_access_key is not None:
            result['CreateAccessKey'] = self.create_access_key
        if self.open_id is not None:
            result['OpenId'] = self.open_id
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.region is not None:
            result['Region'] = self.region
        if self.identity_id is not None:
            result['IdentityId'] = self.identity_id
        if self.login_id is not None:
            result['LoginId'] = self.login_id
        if self.idp is not None:
            result['Idp'] = self.idp
        if self.aliyun_id is not None:
            result['AliyunId'] = self.aliyun_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('CreateAccessKey') is not None:
            self.create_access_key = m.get('CreateAccessKey')
        if m.get('OpenId') is not None:
            self.open_id = m.get('OpenId')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('IdentityId') is not None:
            self.identity_id = m.get('IdentityId')
        if m.get('LoginId') is not None:
            self.login_id = m.get('LoginId')
        if m.get('Idp') is not None:
            self.idp = m.get('Idp')
        if m.get('AliyunId') is not None:
            self.aliyun_id = m.get('AliyunId')
        return self


class DescribeOpenAccountResponseBody(TeaModel):
    def __init__(
        self,
        open_account: DescribeOpenAccountResponseBodyOpenAccount = None,
        request_id: str = None,
    ):
        self.open_account = open_account
        self.request_id = request_id

    def validate(self):
        if self.open_account:
            self.open_account.validate()

    def to_map(self):
        result = dict()
        if self.open_account is not None:
            result['OpenAccount'] = self.open_account.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpenAccount') is not None:
            temp_model = DescribeOpenAccountResponseBodyOpenAccount()
            self.open_account = temp_model.from_map(m['OpenAccount'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeOpenAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeOpenAccountResponseBody = None,
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
            temp_model = DescribeOpenAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOsVersionRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        version_id: int = None,
    ):
        self.project_id = project_id
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class DescribeOsVersionResponseBodyOsVersionRomList(TeaModel):
    def __init__(
        self,
        gmt_modify: str = None,
        split_num: str = None,
        download_url: str = None,
        size: str = None,
        gmt_create: str = None,
        version_id: int = None,
        md_5: str = None,
        base_version: str = None,
        id: int = None,
        original_url: str = None,
    ):
        self.gmt_modify = gmt_modify
        self.split_num = split_num
        self.download_url = download_url
        self.size = size
        self.gmt_create = gmt_create
        self.version_id = version_id
        self.md_5 = md_5
        self.base_version = base_version
        self.id = id
        self.original_url = original_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.gmt_modify is not None:
            result['GmtModify'] = self.gmt_modify
        if self.split_num is not None:
            result['SplitNum'] = self.split_num
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        if self.size is not None:
            result['Size'] = self.size
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.base_version is not None:
            result['BaseVersion'] = self.base_version
        if self.id is not None:
            result['Id'] = self.id
        if self.original_url is not None:
            result['OriginalUrl'] = self.original_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtModify') is not None:
            self.gmt_modify = m.get('GmtModify')
        if m.get('SplitNum') is not None:
            self.split_num = m.get('SplitNum')
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('BaseVersion') is not None:
            self.base_version = m.get('BaseVersion')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OriginalUrl') is not None:
            self.original_url = m.get('OriginalUrl')
        return self


class DescribeOsVersionResponseBodyOsVersionNightUpgradeOption(TeaModel):
    def __init__(
        self,
        download_type: str = None,
        is_allowed_cancel: str = None,
        is_show_tip: str = None,
    ):
        self.download_type = download_type
        self.is_allowed_cancel = is_allowed_cancel
        self.is_show_tip = is_show_tip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.download_type is not None:
            result['DownloadType'] = self.download_type
        if self.is_allowed_cancel is not None:
            result['IsAllowedCancel'] = self.is_allowed_cancel
        if self.is_show_tip is not None:
            result['IsShowTip'] = self.is_show_tip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadType') is not None:
            self.download_type = m.get('DownloadType')
        if m.get('IsAllowedCancel') is not None:
            self.is_allowed_cancel = m.get('IsAllowedCancel')
        if m.get('IsShowTip') is not None:
            self.is_show_tip = m.get('IsShowTip')
        return self


class DescribeOsVersionResponseBodyOsVersion(TeaModel):
    def __init__(
        self,
        status: str = None,
        device_model_id: str = None,
        black_version_list: str = None,
        is_milestone: str = None,
        gmt_modify: str = None,
        release_note: str = None,
        remark: str = None,
        system_version: str = None,
        status_name: str = None,
        device_model_name: str = None,
        white_version_list: str = None,
        max_client_version: str = None,
        rom_list: List[DescribeOsVersionResponseBodyOsVersionRomList] = None,
        min_client_version: str = None,
        night_upgrade_option: DescribeOsVersionResponseBodyOsVersionNightUpgradeOption = None,
        gmt_create: str = None,
        is_force_night_upgrade: str = None,
        mobile_download_max_size: str = None,
        enable_mobile_download: str = None,
        is_force_upgrade: str = None,
        id: int = None,
    ):
        self.status = status
        self.device_model_id = device_model_id
        self.black_version_list = black_version_list
        self.is_milestone = is_milestone
        self.gmt_modify = gmt_modify
        self.release_note = release_note
        self.remark = remark
        self.system_version = system_version
        self.status_name = status_name
        self.device_model_name = device_model_name
        self.white_version_list = white_version_list
        self.max_client_version = max_client_version
        self.rom_list = rom_list
        self.min_client_version = min_client_version
        self.night_upgrade_option = night_upgrade_option
        self.gmt_create = gmt_create
        self.is_force_night_upgrade = is_force_night_upgrade
        self.mobile_download_max_size = mobile_download_max_size
        self.enable_mobile_download = enable_mobile_download
        self.is_force_upgrade = is_force_upgrade
        self.id = id

    def validate(self):
        if self.rom_list:
            for k in self.rom_list:
                if k:
                    k.validate()
        if self.night_upgrade_option:
            self.night_upgrade_option.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.device_model_id is not None:
            result['DeviceModelId'] = self.device_model_id
        if self.black_version_list is not None:
            result['BlackVersionList'] = self.black_version_list
        if self.is_milestone is not None:
            result['IsMilestone'] = self.is_milestone
        if self.gmt_modify is not None:
            result['GmtModify'] = self.gmt_modify
        if self.release_note is not None:
            result['ReleaseNote'] = self.release_note
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.system_version is not None:
            result['SystemVersion'] = self.system_version
        if self.status_name is not None:
            result['StatusName'] = self.status_name
        if self.device_model_name is not None:
            result['DeviceModelName'] = self.device_model_name
        if self.white_version_list is not None:
            result['WhiteVersionList'] = self.white_version_list
        if self.max_client_version is not None:
            result['MaxClientVersion'] = self.max_client_version
        result['RomList'] = []
        if self.rom_list is not None:
            for k in self.rom_list:
                result['RomList'].append(k.to_map() if k else None)
        if self.min_client_version is not None:
            result['MinClientVersion'] = self.min_client_version
        if self.night_upgrade_option is not None:
            result['NightUpgradeOption'] = self.night_upgrade_option.to_map()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.is_force_night_upgrade is not None:
            result['IsForceNightUpgrade'] = self.is_force_night_upgrade
        if self.mobile_download_max_size is not None:
            result['MobileDownloadMaxSize'] = self.mobile_download_max_size
        if self.enable_mobile_download is not None:
            result['EnableMobileDownload'] = self.enable_mobile_download
        if self.is_force_upgrade is not None:
            result['IsForceUpgrade'] = self.is_force_upgrade
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('DeviceModelId') is not None:
            self.device_model_id = m.get('DeviceModelId')
        if m.get('BlackVersionList') is not None:
            self.black_version_list = m.get('BlackVersionList')
        if m.get('IsMilestone') is not None:
            self.is_milestone = m.get('IsMilestone')
        if m.get('GmtModify') is not None:
            self.gmt_modify = m.get('GmtModify')
        if m.get('ReleaseNote') is not None:
            self.release_note = m.get('ReleaseNote')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('SystemVersion') is not None:
            self.system_version = m.get('SystemVersion')
        if m.get('StatusName') is not None:
            self.status_name = m.get('StatusName')
        if m.get('DeviceModelName') is not None:
            self.device_model_name = m.get('DeviceModelName')
        if m.get('WhiteVersionList') is not None:
            self.white_version_list = m.get('WhiteVersionList')
        if m.get('MaxClientVersion') is not None:
            self.max_client_version = m.get('MaxClientVersion')
        self.rom_list = []
        if m.get('RomList') is not None:
            for k in m.get('RomList'):
                temp_model = DescribeOsVersionResponseBodyOsVersionRomList()
                self.rom_list.append(temp_model.from_map(k))
        if m.get('MinClientVersion') is not None:
            self.min_client_version = m.get('MinClientVersion')
        if m.get('NightUpgradeOption') is not None:
            temp_model = DescribeOsVersionResponseBodyOsVersionNightUpgradeOption()
            self.night_upgrade_option = temp_model.from_map(m['NightUpgradeOption'])
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('IsForceNightUpgrade') is not None:
            self.is_force_night_upgrade = m.get('IsForceNightUpgrade')
        if m.get('MobileDownloadMaxSize') is not None:
            self.mobile_download_max_size = m.get('MobileDownloadMaxSize')
        if m.get('EnableMobileDownload') is not None:
            self.enable_mobile_download = m.get('EnableMobileDownload')
        if m.get('IsForceUpgrade') is not None:
            self.is_force_upgrade = m.get('IsForceUpgrade')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeOsVersionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        os_version: DescribeOsVersionResponseBodyOsVersion = None,
    ):
        self.request_id = request_id
        self.os_version = os_version

    def validate(self):
        if self.os_version:
            self.os_version.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.os_version is not None:
            result['OsVersion'] = self.os_version.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OsVersion') is not None:
            temp_model = DescribeOsVersionResponseBodyOsVersion()
            self.os_version = temp_model.from_map(m['OsVersion'])
        return self


class DescribeOsVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeOsVersionResponseBody = None,
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
            temp_model = DescribeOsVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeProjectRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
    ):
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class DescribeProjectResponseBodyProject(TeaModel):
    def __init__(
        self,
        status: int = None,
        description: str = None,
        user_id: str = None,
        project_id: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        name: str = None,
        id: int = None,
        creator: str = None,
    ):
        self.status = status
        self.description = description
        self.user_id = user_id
        self.project_id = project_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.name = name
        self.id = id
        self.creator = creator

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.description is not None:
            result['Description'] = self.description
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        if self.creator is not None:
            result['Creator'] = self.creator
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        return self


class DescribeProjectResponseBody(TeaModel):
    def __init__(
        self,
        project: DescribeProjectResponseBodyProject = None,
        request_id: str = None,
    ):
        self.project = project
        self.request_id = request_id

    def validate(self):
        if self.project:
            self.project.validate()

    def to_map(self):
        result = dict()
        if self.project is not None:
            result['Project'] = self.project.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            temp_model = DescribeProjectResponseBodyProject()
            self.project = temp_model.from_map(m['Project'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeProjectResponseBody = None,
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
            temp_model = DescribeProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeProjectAppSecurityRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        app_id: str = None,
    ):
        self.project_id = project_id
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class DescribeProjectAppSecurityResponseBodyProjectAppSecurity(TeaModel):
    def __init__(
        self,
        app_secret: str = None,
        app_key: str = None,
        app_id: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        id: int = None,
    ):
        self.app_secret = app_secret
        self.app_key = app_key
        self.app_id = app_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_secret is not None:
            result['AppSecret'] = self.app_secret
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppSecret') is not None:
            self.app_secret = m.get('AppSecret')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeProjectAppSecurityResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        project_app_security: DescribeProjectAppSecurityResponseBodyProjectAppSecurity = None,
    ):
        self.request_id = request_id
        self.project_app_security = project_app_security

    def validate(self):
        if self.project_app_security:
            self.project_app_security.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.project_app_security is not None:
            result['ProjectAppSecurity'] = self.project_app_security.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ProjectAppSecurity') is not None:
            temp_model = DescribeProjectAppSecurityResponseBodyProjectAppSecurity()
            self.project_app_security = temp_model.from_map(m['ProjectAppSecurity'])
        return self


class DescribeProjectAppSecurityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeProjectAppSecurityResponseBody = None,
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
            temp_model = DescribeProjectAppSecurityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeShadowSchemaRequest(TeaModel):
    def __init__(
        self,
        device_model: str = None,
        is_simple: bool = None,
        project_id: str = None,
    ):
        self.device_model = device_model
        self.is_simple = is_simple
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.device_model is not None:
            result['DeviceModel'] = self.device_model
        if self.is_simple is not None:
            result['IsSimple'] = self.is_simple
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceModel') is not None:
            self.device_model = m.get('DeviceModel')
        if m.get('IsSimple') is not None:
            self.is_simple = m.get('IsSimple')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class DescribeShadowSchemaResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        schema: str = None,
    ):
        self.request_id = request_id
        self.schema = schema

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.schema is not None:
            result['Schema'] = self.schema
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Schema') is not None:
            self.schema = m.get('Schema')
        return self


class DescribeShadowSchemaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeShadowSchemaResponseBody = None,
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
            temp_model = DescribeShadowSchemaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVersionDeviceGroupRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        id: str = None,
    ):
        self.project_id = project_id
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeVersionDeviceGroupResponseBodyDeviceGroup(TeaModel):
    def __init__(
        self,
        gmt_modify: str = None,
        description: str = None,
        gmt_create: str = None,
        name: str = None,
        id: int = None,
        max_count: str = None,
    ):
        self.gmt_modify = gmt_modify
        self.description = description
        self.gmt_create = gmt_create
        self.name = name
        self.id = id
        self.max_count = max_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.gmt_modify is not None:
            result['GmtModify'] = self.gmt_modify
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        if self.max_count is not None:
            result['MaxCount'] = self.max_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtModify') is not None:
            self.gmt_modify = m.get('GmtModify')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MaxCount') is not None:
            self.max_count = m.get('MaxCount')
        return self


class DescribeVersionDeviceGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        device_group: DescribeVersionDeviceGroupResponseBodyDeviceGroup = None,
    ):
        self.request_id = request_id
        self.device_group = device_group

    def validate(self):
        if self.device_group:
            self.device_group.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.device_group is not None:
            result['DeviceGroup'] = self.device_group.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DeviceGroup') is not None:
            temp_model = DescribeVersionDeviceGroupResponseBodyDeviceGroup()
            self.device_group = temp_model.from_map(m['DeviceGroup'])
        return self


class DescribeVersionDeviceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVersionDeviceGroupResponseBody = None,
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
            temp_model = DescribeVersionDeviceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DiagnosisVersionRequest(TeaModel):
    def __init__(
        self,
        original_id: str = None,
        project_id: str = None,
        version_type: str = None,
        version_id: str = None,
        id_type: str = None,
        diagnose_style: str = None,
        start_time: str = None,
        end_time: str = None,
    ):
        self.original_id = original_id
        self.project_id = project_id
        self.version_type = version_type
        self.version_id = version_id
        self.id_type = id_type
        self.diagnose_style = diagnose_style
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.original_id is not None:
            result['OriginalId'] = self.original_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.version_type is not None:
            result['VersionType'] = self.version_type
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.diagnose_style is not None:
            result['DiagnoseStyle'] = self.diagnose_style
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OriginalId') is not None:
            self.original_id = m.get('OriginalId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('VersionType') is not None:
            self.version_type = m.get('VersionType')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('DiagnoseStyle') is not None:
            self.diagnose_style = m.get('DiagnoseStyle')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DiagnosisVersionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        diagnosis_result: str = None,
    ):
        self.request_id = request_id
        self.diagnosis_result = diagnosis_result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.diagnosis_result is not None:
            result['DiagnosisResult'] = self.diagnosis_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DiagnosisResult') is not None:
            self.diagnosis_result = m.get('DiagnosisResult')
        return self


class DiagnosisVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DiagnosisVersionResponseBody = None,
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
            temp_model = DiagnosisVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FindAppVersionsRequest(TeaModel):
    def __init__(
        self,
        status: str = None,
        project_id: str = None,
        page_size: int = None,
        version_id: str = None,
        device_model_id: str = None,
        page_index: int = None,
        app_id: str = None,
        remark: str = None,
    ):
        self.status = status
        self.project_id = project_id
        self.page_size = page_size
        self.version_id = version_id
        self.device_model_id = device_model_id
        self.page_index = page_index
        self.app_id = app_id
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.device_model_id is not None:
            result['DeviceModelId'] = self.device_model_id
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('DeviceModelId') is not None:
            self.device_model_id = m.get('DeviceModelId')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class FindAppVersionsResponseBodyAppVersionListItems(TeaModel):
    def __init__(
        self,
        status: str = None,
        gmt_create_timestamp: int = None,
        gmt_modify: str = None,
        is_allow_new_install: str = None,
        status_name: str = None,
        restart_app_param: str = None,
        is_silent_upgrade: str = None,
        app_package_name: str = None,
        gmt_modify_timestamp: int = None,
        app_name: str = None,
        install_type: str = None,
        is_need_restart: str = None,
        restart_app_type: str = None,
        app_id: str = None,
        restart_type: str = None,
        gmt_create: str = None,
        app_version: str = None,
        version_code: str = None,
        is_force_upgrade: str = None,
        id: int = None,
    ):
        self.status = status
        self.gmt_create_timestamp = gmt_create_timestamp
        self.gmt_modify = gmt_modify
        self.is_allow_new_install = is_allow_new_install
        self.status_name = status_name
        self.restart_app_param = restart_app_param
        self.is_silent_upgrade = is_silent_upgrade
        self.app_package_name = app_package_name
        self.gmt_modify_timestamp = gmt_modify_timestamp
        self.app_name = app_name
        self.install_type = install_type
        self.is_need_restart = is_need_restart
        self.restart_app_type = restart_app_type
        self.app_id = app_id
        self.restart_type = restart_type
        self.gmt_create = gmt_create
        self.app_version = app_version
        self.version_code = version_code
        self.is_force_upgrade = is_force_upgrade
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.gmt_create_timestamp is not None:
            result['GmtCreateTimestamp'] = self.gmt_create_timestamp
        if self.gmt_modify is not None:
            result['GmtModify'] = self.gmt_modify
        if self.is_allow_new_install is not None:
            result['IsAllowNewInstall'] = self.is_allow_new_install
        if self.status_name is not None:
            result['StatusName'] = self.status_name
        if self.restart_app_param is not None:
            result['RestartAppParam'] = self.restart_app_param
        if self.is_silent_upgrade is not None:
            result['IsSilentUpgrade'] = self.is_silent_upgrade
        if self.app_package_name is not None:
            result['AppPackageName'] = self.app_package_name
        if self.gmt_modify_timestamp is not None:
            result['GmtModifyTimestamp'] = self.gmt_modify_timestamp
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.install_type is not None:
            result['InstallType'] = self.install_type
        if self.is_need_restart is not None:
            result['IsNeedRestart'] = self.is_need_restart
        if self.restart_app_type is not None:
            result['RestartAppType'] = self.restart_app_type
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.restart_type is not None:
            result['RestartType'] = self.restart_type
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.version_code is not None:
            result['VersionCode'] = self.version_code
        if self.is_force_upgrade is not None:
            result['IsForceUpgrade'] = self.is_force_upgrade
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('GmtCreateTimestamp') is not None:
            self.gmt_create_timestamp = m.get('GmtCreateTimestamp')
        if m.get('GmtModify') is not None:
            self.gmt_modify = m.get('GmtModify')
        if m.get('IsAllowNewInstall') is not None:
            self.is_allow_new_install = m.get('IsAllowNewInstall')
        if m.get('StatusName') is not None:
            self.status_name = m.get('StatusName')
        if m.get('RestartAppParam') is not None:
            self.restart_app_param = m.get('RestartAppParam')
        if m.get('IsSilentUpgrade') is not None:
            self.is_silent_upgrade = m.get('IsSilentUpgrade')
        if m.get('AppPackageName') is not None:
            self.app_package_name = m.get('AppPackageName')
        if m.get('GmtModifyTimestamp') is not None:
            self.gmt_modify_timestamp = m.get('GmtModifyTimestamp')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('InstallType') is not None:
            self.install_type = m.get('InstallType')
        if m.get('IsNeedRestart') is not None:
            self.is_need_restart = m.get('IsNeedRestart')
        if m.get('RestartAppType') is not None:
            self.restart_app_type = m.get('RestartAppType')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RestartType') is not None:
            self.restart_type = m.get('RestartType')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('VersionCode') is not None:
            self.version_code = m.get('VersionCode')
        if m.get('IsForceUpgrade') is not None:
            self.is_force_upgrade = m.get('IsForceUpgrade')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class FindAppVersionsResponseBodyAppVersionList(TeaModel):
    def __init__(
        self,
        items: List[FindAppVersionsResponseBodyAppVersionListItems] = None,
        total_count: int = None,
    ):
        self.items = items
        self.total_count = total_count

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = FindAppVersionsResponseBodyAppVersionListItems()
                self.items.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class FindAppVersionsResponseBody(TeaModel):
    def __init__(
        self,
        app_version_list: FindAppVersionsResponseBodyAppVersionList = None,
        request_id: str = None,
    ):
        self.app_version_list = app_version_list
        self.request_id = request_id

    def validate(self):
        if self.app_version_list:
            self.app_version_list.validate()

    def to_map(self):
        result = dict()
        if self.app_version_list is not None:
            result['AppVersionList'] = self.app_version_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppVersionList') is not None:
            temp_model = FindAppVersionsResponseBodyAppVersionList()
            self.app_version_list = temp_model.from_map(m['AppVersionList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class FindAppVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: FindAppVersionsResponseBody = None,
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
            temp_model = FindAppVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FindCustomizedFiltersRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        version_id: str = None,
        page_index: int = None,
        page_size: int = None,
        name: str = None,
        version_type: str = None,
    ):
        self.project_id = project_id
        self.version_id = version_id
        self.page_index = page_index
        self.page_size = page_size
        self.name = name
        self.version_type = version_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.name is not None:
            result['Name'] = self.name
        if self.version_type is not None:
            result['VersionType'] = self.version_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('VersionType') is not None:
            self.version_type = m.get('VersionType')
        return self


class FindCustomizedFiltersResponseBodyCustomizedFilterListItems(TeaModel):
    def __init__(
        self,
        gmt_modify_timestamp: int = None,
        gmt_create_timestamp: int = None,
        value: str = None,
        gmt_modify: str = None,
        value_compare_type: str = None,
        gmt_create: str = None,
        black_white_type: str = None,
        name: str = None,
        id: int = None,
    ):
        self.gmt_modify_timestamp = gmt_modify_timestamp
        self.gmt_create_timestamp = gmt_create_timestamp
        self.value = value
        self.gmt_modify = gmt_modify
        self.value_compare_type = value_compare_type
        self.gmt_create = gmt_create
        self.black_white_type = black_white_type
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.gmt_modify_timestamp is not None:
            result['GmtModifyTimestamp'] = self.gmt_modify_timestamp
        if self.gmt_create_timestamp is not None:
            result['GmtCreateTimestamp'] = self.gmt_create_timestamp
        if self.value is not None:
            result['Value'] = self.value
        if self.gmt_modify is not None:
            result['GmtModify'] = self.gmt_modify
        if self.value_compare_type is not None:
            result['ValueCompareType'] = self.value_compare_type
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.black_white_type is not None:
            result['BlackWhiteType'] = self.black_white_type
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtModifyTimestamp') is not None:
            self.gmt_modify_timestamp = m.get('GmtModifyTimestamp')
        if m.get('GmtCreateTimestamp') is not None:
            self.gmt_create_timestamp = m.get('GmtCreateTimestamp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('GmtModify') is not None:
            self.gmt_modify = m.get('GmtModify')
        if m.get('ValueCompareType') is not None:
            self.value_compare_type = m.get('ValueCompareType')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('BlackWhiteType') is not None:
            self.black_white_type = m.get('BlackWhiteType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class FindCustomizedFiltersResponseBodyCustomizedFilterList(TeaModel):
    def __init__(
        self,
        items: List[FindCustomizedFiltersResponseBodyCustomizedFilterListItems] = None,
        total_count: int = None,
    ):
        self.items = items
        self.total_count = total_count

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = FindCustomizedFiltersResponseBodyCustomizedFilterListItems()
                self.items.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class FindCustomizedFiltersResponseBody(TeaModel):
    def __init__(
        self,
        customized_filter_list: FindCustomizedFiltersResponseBodyCustomizedFilterList = None,
        request_id: str = None,
    ):
        self.customized_filter_list = customized_filter_list
        self.request_id = request_id

    def validate(self):
        if self.customized_filter_list:
            self.customized_filter_list.validate()

    def to_map(self):
        result = dict()
        if self.customized_filter_list is not None:
            result['CustomizedFilterList'] = self.customized_filter_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomizedFilterList') is not None:
            temp_model = FindCustomizedFiltersResponseBodyCustomizedFilterList()
            self.customized_filter_list = temp_model.from_map(m['CustomizedFilterList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class FindCustomizedFiltersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: FindCustomizedFiltersResponseBody = None,
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
            temp_model = FindCustomizedFiltersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FindCustomizedPropertiesRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        version_id: str = None,
        page_index: int = None,
        page_size: int = None,
        name: str = None,
        version_type: str = None,
    ):
        self.project_id = project_id
        self.version_id = version_id
        self.page_index = page_index
        self.page_size = page_size
        self.name = name
        self.version_type = version_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.name is not None:
            result['Name'] = self.name
        if self.version_type is not None:
            result['VersionType'] = self.version_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('VersionType') is not None:
            self.version_type = m.get('VersionType')
        return self


class FindCustomizedPropertiesResponseBodyCustomizedPropertyListItems(TeaModel):
    def __init__(
        self,
        gmt_create_timestamp: int = None,
        value: str = None,
        gmt_create: str = None,
        name: str = None,
        id: int = None,
    ):
        self.gmt_create_timestamp = gmt_create_timestamp
        self.value = value
        self.gmt_create = gmt_create
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.gmt_create_timestamp is not None:
            result['GmtCreateTimestamp'] = self.gmt_create_timestamp
        if self.value is not None:
            result['Value'] = self.value
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreateTimestamp') is not None:
            self.gmt_create_timestamp = m.get('GmtCreateTimestamp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class FindCustomizedPropertiesResponseBodyCustomizedPropertyList(TeaModel):
    def __init__(
        self,
        items: List[FindCustomizedPropertiesResponseBodyCustomizedPropertyListItems] = None,
        total_count: int = None,
    ):
        self.items = items
        self.total_count = total_count

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = FindCustomizedPropertiesResponseBodyCustomizedPropertyListItems()
                self.items.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class FindCustomizedPropertiesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        customized_property_list: FindCustomizedPropertiesResponseBodyCustomizedPropertyList = None,
    ):
        self.request_id = request_id
        self.customized_property_list = customized_property_list

    def validate(self):
        if self.customized_property_list:
            self.customized_property_list.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.customized_property_list is not None:
            result['CustomizedPropertyList'] = self.customized_property_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CustomizedPropertyList') is not None:
            temp_model = FindCustomizedPropertiesResponseBodyCustomizedPropertyList()
            self.customized_property_list = temp_model.from_map(m['CustomizedPropertyList'])
        return self


class FindCustomizedPropertiesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: FindCustomizedPropertiesResponseBody = None,
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
            temp_model = FindCustomizedPropertiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FindOsVersionsRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        page_index: int = None,
        page_size: int = None,
        version_id: str = None,
        device_model_id: str = None,
        system_version: str = None,
        status: str = None,
        is_milestone: str = None,
        remark: str = None,
    ):
        self.project_id = project_id
        self.page_index = page_index
        self.page_size = page_size
        self.version_id = version_id
        self.device_model_id = device_model_id
        self.system_version = system_version
        self.status = status
        self.is_milestone = is_milestone
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.device_model_id is not None:
            result['DeviceModelId'] = self.device_model_id
        if self.system_version is not None:
            result['SystemVersion'] = self.system_version
        if self.status is not None:
            result['Status'] = self.status
        if self.is_milestone is not None:
            result['IsMilestone'] = self.is_milestone
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('DeviceModelId') is not None:
            self.device_model_id = m.get('DeviceModelId')
        if m.get('SystemVersion') is not None:
            self.system_version = m.get('SystemVersion')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('IsMilestone') is not None:
            self.is_milestone = m.get('IsMilestone')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class FindOsVersionsResponseBodyOsVersionListItems(TeaModel):
    def __init__(
        self,
        status: str = None,
        gmt_create_timestamp: int = None,
        device_model_id: str = None,
        gmt_modify: str = None,
        is_milestone: str = None,
        remark: str = None,
        system_version: str = None,
        status_name: str = None,
        is_force_reboot: str = None,
        device_model_name: str = None,
        is_silent_upgrade: str = None,
        gmt_modify_timestamp: int = None,
        is_force_night_upgrade: str = None,
        gmt_create: str = None,
        is_force_upgrade: str = None,
        id: int = None,
    ):
        self.status = status
        self.gmt_create_timestamp = gmt_create_timestamp
        self.device_model_id = device_model_id
        self.gmt_modify = gmt_modify
        self.is_milestone = is_milestone
        self.remark = remark
        self.system_version = system_version
        self.status_name = status_name
        self.is_force_reboot = is_force_reboot
        self.device_model_name = device_model_name
        self.is_silent_upgrade = is_silent_upgrade
        self.gmt_modify_timestamp = gmt_modify_timestamp
        self.is_force_night_upgrade = is_force_night_upgrade
        self.gmt_create = gmt_create
        self.is_force_upgrade = is_force_upgrade
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.gmt_create_timestamp is not None:
            result['GmtCreateTimestamp'] = self.gmt_create_timestamp
        if self.device_model_id is not None:
            result['DeviceModelId'] = self.device_model_id
        if self.gmt_modify is not None:
            result['GmtModify'] = self.gmt_modify
        if self.is_milestone is not None:
            result['IsMilestone'] = self.is_milestone
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.system_version is not None:
            result['SystemVersion'] = self.system_version
        if self.status_name is not None:
            result['StatusName'] = self.status_name
        if self.is_force_reboot is not None:
            result['IsForceReboot'] = self.is_force_reboot
        if self.device_model_name is not None:
            result['DeviceModelName'] = self.device_model_name
        if self.is_silent_upgrade is not None:
            result['IsSilentUpgrade'] = self.is_silent_upgrade
        if self.gmt_modify_timestamp is not None:
            result['GmtModifyTimestamp'] = self.gmt_modify_timestamp
        if self.is_force_night_upgrade is not None:
            result['IsForceNightUpgrade'] = self.is_force_night_upgrade
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.is_force_upgrade is not None:
            result['IsForceUpgrade'] = self.is_force_upgrade
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('GmtCreateTimestamp') is not None:
            self.gmt_create_timestamp = m.get('GmtCreateTimestamp')
        if m.get('DeviceModelId') is not None:
            self.device_model_id = m.get('DeviceModelId')
        if m.get('GmtModify') is not None:
            self.gmt_modify = m.get('GmtModify')
        if m.get('IsMilestone') is not None:
            self.is_milestone = m.get('IsMilestone')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('SystemVersion') is not None:
            self.system_version = m.get('SystemVersion')
        if m.get('StatusName') is not None:
            self.status_name = m.get('StatusName')
        if m.get('IsForceReboot') is not None:
            self.is_force_reboot = m.get('IsForceReboot')
        if m.get('DeviceModelName') is not None:
            self.device_model_name = m.get('DeviceModelName')
        if m.get('IsSilentUpgrade') is not None:
            self.is_silent_upgrade = m.get('IsSilentUpgrade')
        if m.get('GmtModifyTimestamp') is not None:
            self.gmt_modify_timestamp = m.get('GmtModifyTimestamp')
        if m.get('IsForceNightUpgrade') is not None:
            self.is_force_night_upgrade = m.get('IsForceNightUpgrade')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('IsForceUpgrade') is not None:
            self.is_force_upgrade = m.get('IsForceUpgrade')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class FindOsVersionsResponseBodyOsVersionList(TeaModel):
    def __init__(
        self,
        items: List[FindOsVersionsResponseBodyOsVersionListItems] = None,
        total_count: int = None,
    ):
        self.items = items
        self.total_count = total_count

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = FindOsVersionsResponseBodyOsVersionListItems()
                self.items.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class FindOsVersionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        os_version_list: FindOsVersionsResponseBodyOsVersionList = None,
    ):
        self.request_id = request_id
        self.os_version_list = os_version_list

    def validate(self):
        if self.os_version_list:
            self.os_version_list.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.os_version_list is not None:
            result['OsVersionList'] = self.os_version_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OsVersionList') is not None:
            temp_model = FindOsVersionsResponseBodyOsVersionList()
            self.os_version_list = temp_model.from_map(m['OsVersionList'])
        return self


class FindOsVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: FindOsVersionsResponseBody = None,
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
            temp_model = FindOsVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FindPrepublishesByParentIdRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        parent_id: int = None,
    ):
        self.project_id = project_id
        self.parent_id = parent_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        return self


class FindPrepublishesByParentIdResponseBodyPrepublishListItems(TeaModel):
    def __init__(
        self,
        gmt_create_timestamp: int = None,
        device_model_id: str = None,
        gmt_modify: str = None,
        is_active: str = None,
        version_id: str = None,
        barrier_count: str = None,
        is_total_prepublish: str = None,
        gmt_modify_timestamp: int = None,
        parent_id: str = None,
        gmt_create: str = None,
        name: str = None,
        id: int = None,
        version_type: str = None,
    ):
        self.gmt_create_timestamp = gmt_create_timestamp
        self.device_model_id = device_model_id
        self.gmt_modify = gmt_modify
        self.is_active = is_active
        self.version_id = version_id
        self.barrier_count = barrier_count
        self.is_total_prepublish = is_total_prepublish
        self.gmt_modify_timestamp = gmt_modify_timestamp
        self.parent_id = parent_id
        self.gmt_create = gmt_create
        self.name = name
        self.id = id
        self.version_type = version_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.gmt_create_timestamp is not None:
            result['GmtCreateTimestamp'] = self.gmt_create_timestamp
        if self.device_model_id is not None:
            result['DeviceModelId'] = self.device_model_id
        if self.gmt_modify is not None:
            result['GmtModify'] = self.gmt_modify
        if self.is_active is not None:
            result['IsActive'] = self.is_active
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.barrier_count is not None:
            result['BarrierCount'] = self.barrier_count
        if self.is_total_prepublish is not None:
            result['IsTotalPrepublish'] = self.is_total_prepublish
        if self.gmt_modify_timestamp is not None:
            result['GmtModifyTimestamp'] = self.gmt_modify_timestamp
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        if self.version_type is not None:
            result['VersionType'] = self.version_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreateTimestamp') is not None:
            self.gmt_create_timestamp = m.get('GmtCreateTimestamp')
        if m.get('DeviceModelId') is not None:
            self.device_model_id = m.get('DeviceModelId')
        if m.get('GmtModify') is not None:
            self.gmt_modify = m.get('GmtModify')
        if m.get('IsActive') is not None:
            self.is_active = m.get('IsActive')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('BarrierCount') is not None:
            self.barrier_count = m.get('BarrierCount')
        if m.get('IsTotalPrepublish') is not None:
            self.is_total_prepublish = m.get('IsTotalPrepublish')
        if m.get('GmtModifyTimestamp') is not None:
            self.gmt_modify_timestamp = m.get('GmtModifyTimestamp')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('VersionType') is not None:
            self.version_type = m.get('VersionType')
        return self


class FindPrepublishesByParentIdResponseBodyPrepublishList(TeaModel):
    def __init__(
        self,
        items: List[FindPrepublishesByParentIdResponseBodyPrepublishListItems] = None,
        total_count: int = None,
    ):
        self.items = items
        self.total_count = total_count

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = FindPrepublishesByParentIdResponseBodyPrepublishListItems()
                self.items.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class FindPrepublishesByParentIdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prepublish_list: FindPrepublishesByParentIdResponseBodyPrepublishList = None,
    ):
        self.request_id = request_id
        self.prepublish_list = prepublish_list

    def validate(self):
        if self.prepublish_list:
            self.prepublish_list.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prepublish_list is not None:
            result['PrepublishList'] = self.prepublish_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PrepublishList') is not None:
            temp_model = FindPrepublishesByParentIdResponseBodyPrepublishList()
            self.prepublish_list = temp_model.from_map(m['PrepublishList'])
        return self


class FindPrepublishesByParentIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: FindPrepublishesByParentIdResponseBody = None,
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
            temp_model = FindPrepublishesByParentIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FindPrepublishesByVersionIdRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        version_id: int = None,
        version_type: str = None,
    ):
        self.project_id = project_id
        self.version_id = version_id
        self.version_type = version_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.version_type is not None:
            result['VersionType'] = self.version_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('VersionType') is not None:
            self.version_type = m.get('VersionType')
        return self


class FindPrepublishesByVersionIdResponseBodyPrepublishList(TeaModel):
    def __init__(
        self,
        gmt_create_timestamp: int = None,
        device_model_id: str = None,
        gmt_modify: str = None,
        is_active: str = None,
        version_id: str = None,
        barrier_count: str = None,
        device_model_name: str = None,
        is_total_prepublish: str = None,
        gmt_modify_timestamp: int = None,
        parent_id: str = None,
        gmt_create: str = None,
        name: str = None,
        id: str = None,
        version_type: str = None,
        passed_count: str = None,
    ):
        self.gmt_create_timestamp = gmt_create_timestamp
        self.device_model_id = device_model_id
        self.gmt_modify = gmt_modify
        self.is_active = is_active
        self.version_id = version_id
        self.barrier_count = barrier_count
        self.device_model_name = device_model_name
        self.is_total_prepublish = is_total_prepublish
        self.gmt_modify_timestamp = gmt_modify_timestamp
        self.parent_id = parent_id
        self.gmt_create = gmt_create
        self.name = name
        self.id = id
        self.version_type = version_type
        self.passed_count = passed_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.gmt_create_timestamp is not None:
            result['GmtCreateTimestamp'] = self.gmt_create_timestamp
        if self.device_model_id is not None:
            result['DeviceModelId'] = self.device_model_id
        if self.gmt_modify is not None:
            result['GmtModify'] = self.gmt_modify
        if self.is_active is not None:
            result['IsActive'] = self.is_active
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.barrier_count is not None:
            result['BarrierCount'] = self.barrier_count
        if self.device_model_name is not None:
            result['DeviceModelName'] = self.device_model_name
        if self.is_total_prepublish is not None:
            result['IsTotalPrepublish'] = self.is_total_prepublish
        if self.gmt_modify_timestamp is not None:
            result['GmtModifyTimestamp'] = self.gmt_modify_timestamp
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        if self.version_type is not None:
            result['VersionType'] = self.version_type
        if self.passed_count is not None:
            result['PassedCount'] = self.passed_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreateTimestamp') is not None:
            self.gmt_create_timestamp = m.get('GmtCreateTimestamp')
        if m.get('DeviceModelId') is not None:
            self.device_model_id = m.get('DeviceModelId')
        if m.get('GmtModify') is not None:
            self.gmt_modify = m.get('GmtModify')
        if m.get('IsActive') is not None:
            self.is_active = m.get('IsActive')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('BarrierCount') is not None:
            self.barrier_count = m.get('BarrierCount')
        if m.get('DeviceModelName') is not None:
            self.device_model_name = m.get('DeviceModelName')
        if m.get('IsTotalPrepublish') is not None:
            self.is_total_prepublish = m.get('IsTotalPrepublish')
        if m.get('GmtModifyTimestamp') is not None:
            self.gmt_modify_timestamp = m.get('GmtModifyTimestamp')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('VersionType') is not None:
            self.version_type = m.get('VersionType')
        if m.get('PassedCount') is not None:
            self.passed_count = m.get('PassedCount')
        return self


class FindPrepublishesByVersionIdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prepublish_list: List[FindPrepublishesByVersionIdResponseBodyPrepublishList] = None,
    ):
        self.request_id = request_id
        self.prepublish_list = prepublish_list

    def validate(self):
        if self.prepublish_list:
            for k in self.prepublish_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['PrepublishList'] = []
        if self.prepublish_list is not None:
            for k in self.prepublish_list:
                result['PrepublishList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.prepublish_list = []
        if m.get('PrepublishList') is not None:
            for k in m.get('PrepublishList'):
                temp_model = FindPrepublishesByVersionIdResponseBodyPrepublishList()
                self.prepublish_list.append(temp_model.from_map(k))
        return self


class FindPrepublishesByVersionIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: FindPrepublishesByVersionIdResponseBody = None,
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
            temp_model = FindPrepublishesByVersionIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FindPrepublishPassedDevicesRequest(TeaModel):
    def __init__(
        self,
        prepublish_id: str = None,
        project_id: str = None,
        page_index: int = None,
        page_size: int = None,
        device_id: str = None,
    ):
        self.prepublish_id = prepublish_id
        self.project_id = project_id
        self.page_index = page_index
        self.page_size = page_size
        self.device_id = device_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.prepublish_id is not None:
            result['PrepublishId'] = self.prepublish_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrepublishId') is not None:
            self.prepublish_id = m.get('PrepublishId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        return self


class FindPrepublishPassedDevicesResponseBodyDeviceListItems(TeaModel):
    def __init__(
        self,
        gmt_create_timestamp: int = None,
        device_id: str = None,
        gmt_create: str = None,
    ):
        self.gmt_create_timestamp = gmt_create_timestamp
        self.device_id = device_id
        self.gmt_create = gmt_create

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.gmt_create_timestamp is not None:
            result['GmtCreateTimestamp'] = self.gmt_create_timestamp
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreateTimestamp') is not None:
            self.gmt_create_timestamp = m.get('GmtCreateTimestamp')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        return self


class FindPrepublishPassedDevicesResponseBodyDeviceList(TeaModel):
    def __init__(
        self,
        items: List[FindPrepublishPassedDevicesResponseBodyDeviceListItems] = None,
        total_count: int = None,
    ):
        self.items = items
        self.total_count = total_count

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = FindPrepublishPassedDevicesResponseBodyDeviceListItems()
                self.items.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class FindPrepublishPassedDevicesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        device_list: FindPrepublishPassedDevicesResponseBodyDeviceList = None,
    ):
        self.request_id = request_id
        self.device_list = device_list

    def validate(self):
        if self.device_list:
            self.device_list.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.device_list is not None:
            result['DeviceList'] = self.device_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DeviceList') is not None:
            temp_model = FindPrepublishPassedDevicesResponseBodyDeviceList()
            self.device_list = temp_model.from_map(m['DeviceList'])
        return self


class FindPrepublishPassedDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: FindPrepublishPassedDevicesResponseBody = None,
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
            temp_model = FindPrepublishPassedDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FindVersionBlackDevicesRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        version_id: str = None,
        version_type: str = None,
        device_id: str = None,
        original_id: str = None,
        page_index: int = None,
        page_size: int = None,
    ):
        self.project_id = project_id
        self.version_id = version_id
        self.version_type = version_type
        self.device_id = device_id
        self.original_id = original_id
        self.page_index = page_index
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.version_type is not None:
            result['VersionType'] = self.version_type
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.original_id is not None:
            result['OriginalId'] = self.original_id
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('VersionType') is not None:
            self.version_type = m.get('VersionType')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('OriginalId') is not None:
            self.original_id = m.get('OriginalId')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class FindVersionBlackDevicesResponseBodyDeviceListItems(TeaModel):
    def __init__(
        self,
        gmt_create_timestamp: int = None,
        original_id: str = None,
        device_id: str = None,
        id_type: str = None,
        gmt_create: str = None,
        id: int = None,
    ):
        self.gmt_create_timestamp = gmt_create_timestamp
        self.original_id = original_id
        self.device_id = device_id
        self.id_type = id_type
        self.gmt_create = gmt_create
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.gmt_create_timestamp is not None:
            result['GmtCreateTimestamp'] = self.gmt_create_timestamp
        if self.original_id is not None:
            result['OriginalId'] = self.original_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreateTimestamp') is not None:
            self.gmt_create_timestamp = m.get('GmtCreateTimestamp')
        if m.get('OriginalId') is not None:
            self.original_id = m.get('OriginalId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class FindVersionBlackDevicesResponseBodyDeviceList(TeaModel):
    def __init__(
        self,
        items: List[FindVersionBlackDevicesResponseBodyDeviceListItems] = None,
        total_count: int = None,
    ):
        self.items = items
        self.total_count = total_count

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = FindVersionBlackDevicesResponseBodyDeviceListItems()
                self.items.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class FindVersionBlackDevicesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        device_list: FindVersionBlackDevicesResponseBodyDeviceList = None,
    ):
        self.request_id = request_id
        self.device_list = device_list

    def validate(self):
        if self.device_list:
            self.device_list.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.device_list is not None:
            result['DeviceList'] = self.device_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DeviceList') is not None:
            temp_model = FindVersionBlackDevicesResponseBodyDeviceList()
            self.device_list = temp_model.from_map(m['DeviceList'])
        return self


class FindVersionBlackDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: FindVersionBlackDevicesResponseBody = None,
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
            temp_model = FindVersionBlackDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FindVersionDeviceGroupsRequest(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        original_id: str = None,
        page_index: int = None,
        page_size: int = None,
        name: str = None,
        project_id: str = None,
    ):
        self.device_id = device_id
        self.original_id = original_id
        self.page_index = page_index
        self.page_size = page_size
        self.name = name
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.original_id is not None:
            result['OriginalId'] = self.original_id
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.name is not None:
            result['Name'] = self.name
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('OriginalId') is not None:
            self.original_id = m.get('OriginalId')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class FindVersionDeviceGroupsResponseBodyDeviceGroupListItems(TeaModel):
    def __init__(
        self,
        gmt_modify_timestamp: int = None,
        gmt_create_timestamp: int = None,
        gmt_modify: str = None,
        description: str = None,
        gmt_create: str = None,
        name: str = None,
        id: int = None,
        max_count: str = None,
    ):
        self.gmt_modify_timestamp = gmt_modify_timestamp
        self.gmt_create_timestamp = gmt_create_timestamp
        self.gmt_modify = gmt_modify
        self.description = description
        self.gmt_create = gmt_create
        self.name = name
        self.id = id
        self.max_count = max_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.gmt_modify_timestamp is not None:
            result['GmtModifyTimestamp'] = self.gmt_modify_timestamp
        if self.gmt_create_timestamp is not None:
            result['GmtCreateTimestamp'] = self.gmt_create_timestamp
        if self.gmt_modify is not None:
            result['GmtModify'] = self.gmt_modify
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        if self.max_count is not None:
            result['MaxCount'] = self.max_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtModifyTimestamp') is not None:
            self.gmt_modify_timestamp = m.get('GmtModifyTimestamp')
        if m.get('GmtCreateTimestamp') is not None:
            self.gmt_create_timestamp = m.get('GmtCreateTimestamp')
        if m.get('GmtModify') is not None:
            self.gmt_modify = m.get('GmtModify')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MaxCount') is not None:
            self.max_count = m.get('MaxCount')
        return self


class FindVersionDeviceGroupsResponseBodyDeviceGroupList(TeaModel):
    def __init__(
        self,
        items: List[FindVersionDeviceGroupsResponseBodyDeviceGroupListItems] = None,
        total_count: int = None,
    ):
        self.items = items
        self.total_count = total_count

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = FindVersionDeviceGroupsResponseBodyDeviceGroupListItems()
                self.items.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class FindVersionDeviceGroupsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        device_group_list: FindVersionDeviceGroupsResponseBodyDeviceGroupList = None,
    ):
        self.request_id = request_id
        self.device_group_list = device_group_list

    def validate(self):
        if self.device_group_list:
            self.device_group_list.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.device_group_list is not None:
            result['DeviceGroupList'] = self.device_group_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DeviceGroupList') is not None:
            temp_model = FindVersionDeviceGroupsResponseBodyDeviceGroupList()
            self.device_group_list = temp_model.from_map(m['DeviceGroupList'])
        return self


class FindVersionDeviceGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: FindVersionDeviceGroupsResponseBody = None,
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
            temp_model = FindVersionDeviceGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FindVersionGroupDevicesRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        original_id: str = None,
        page_index: int = None,
        page_size: int = None,
        device_group_id: str = None,
        device_id: str = None,
    ):
        self.project_id = project_id
        self.original_id = original_id
        self.page_index = page_index
        self.page_size = page_size
        self.device_group_id = device_group_id
        self.device_id = device_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.original_id is not None:
            result['OriginalId'] = self.original_id
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('OriginalId') is not None:
            self.original_id = m.get('OriginalId')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        return self


class FindVersionGroupDevicesResponseBodyGroupDeviceListItems(TeaModel):
    def __init__(
        self,
        gmt_create_timestamp: int = None,
        original_id: str = None,
        device_id: str = None,
        id_type: str = None,
        gmt_create: str = None,
        id: str = None,
    ):
        self.gmt_create_timestamp = gmt_create_timestamp
        self.original_id = original_id
        self.device_id = device_id
        self.id_type = id_type
        self.gmt_create = gmt_create
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.gmt_create_timestamp is not None:
            result['GmtCreateTimestamp'] = self.gmt_create_timestamp
        if self.original_id is not None:
            result['OriginalId'] = self.original_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreateTimestamp') is not None:
            self.gmt_create_timestamp = m.get('GmtCreateTimestamp')
        if m.get('OriginalId') is not None:
            self.original_id = m.get('OriginalId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class FindVersionGroupDevicesResponseBodyGroupDeviceList(TeaModel):
    def __init__(
        self,
        items: List[FindVersionGroupDevicesResponseBodyGroupDeviceListItems] = None,
        total_count: int = None,
    ):
        self.items = items
        self.total_count = total_count

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = FindVersionGroupDevicesResponseBodyGroupDeviceListItems()
                self.items.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class FindVersionGroupDevicesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        group_device_list: FindVersionGroupDevicesResponseBodyGroupDeviceList = None,
    ):
        self.request_id = request_id
        self.group_device_list = group_device_list

    def validate(self):
        if self.group_device_list:
            self.group_device_list.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.group_device_list is not None:
            result['GroupDeviceList'] = self.group_device_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('GroupDeviceList') is not None:
            temp_model = FindVersionGroupDevicesResponseBodyGroupDeviceList()
            self.group_device_list = temp_model.from_map(m['GroupDeviceList'])
        return self


class FindVersionGroupDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: FindVersionGroupDevicesResponseBody = None,
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
            temp_model = FindVersionGroupDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FindVersionMessagesRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        page_index: int = None,
        page_size: int = None,
        message_type: str = None,
        test_id: str = None,
        version_id: str = None,
        send_record_id: str = None,
        device_id: str = None,
        version_type: str = None,
    ):
        self.project_id = project_id
        self.page_index = page_index
        self.page_size = page_size
        self.message_type = message_type
        self.test_id = test_id
        self.version_id = version_id
        self.send_record_id = send_record_id
        self.device_id = device_id
        self.version_type = version_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.message_type is not None:
            result['MessageType'] = self.message_type
        if self.test_id is not None:
            result['TestId'] = self.test_id
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.send_record_id is not None:
            result['SendRecordId'] = self.send_record_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.version_type is not None:
            result['VersionType'] = self.version_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')
        if m.get('TestId') is not None:
            self.test_id = m.get('TestId')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('SendRecordId') is not None:
            self.send_record_id = m.get('SendRecordId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('VersionType') is not None:
            self.version_type = m.get('VersionType')
        return self


class FindVersionMessagesResponseBodyMessageListItems(TeaModel):
    def __init__(
        self,
        gmt_modify_timestamp: int = None,
        gmt_create_timestamp: int = None,
        status: str = None,
        gmt_modify: str = None,
        message_id: str = None,
        device_id: str = None,
        gmt_create: str = None,
        version_id: str = None,
        status_desc: str = None,
        test_id: str = None,
        id: int = None,
    ):
        self.gmt_modify_timestamp = gmt_modify_timestamp
        self.gmt_create_timestamp = gmt_create_timestamp
        self.status = status
        self.gmt_modify = gmt_modify
        self.message_id = message_id
        self.device_id = device_id
        self.gmt_create = gmt_create
        self.version_id = version_id
        self.status_desc = status_desc
        self.test_id = test_id
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.gmt_modify_timestamp is not None:
            result['GmtModifyTimestamp'] = self.gmt_modify_timestamp
        if self.gmt_create_timestamp is not None:
            result['GmtCreateTimestamp'] = self.gmt_create_timestamp
        if self.status is not None:
            result['Status'] = self.status
        if self.gmt_modify is not None:
            result['GmtModify'] = self.gmt_modify
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.status_desc is not None:
            result['StatusDesc'] = self.status_desc
        if self.test_id is not None:
            result['TestId'] = self.test_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtModifyTimestamp') is not None:
            self.gmt_modify_timestamp = m.get('GmtModifyTimestamp')
        if m.get('GmtCreateTimestamp') is not None:
            self.gmt_create_timestamp = m.get('GmtCreateTimestamp')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('GmtModify') is not None:
            self.gmt_modify = m.get('GmtModify')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('StatusDesc') is not None:
            self.status_desc = m.get('StatusDesc')
        if m.get('TestId') is not None:
            self.test_id = m.get('TestId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class FindVersionMessagesResponseBodyMessageList(TeaModel):
    def __init__(
        self,
        items: List[FindVersionMessagesResponseBodyMessageListItems] = None,
        total_count: int = None,
    ):
        self.items = items
        self.total_count = total_count

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = FindVersionMessagesResponseBodyMessageListItems()
                self.items.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class FindVersionMessagesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message_list: FindVersionMessagesResponseBodyMessageList = None,
    ):
        self.request_id = request_id
        self.message_list = message_list

    def validate(self):
        if self.message_list:
            self.message_list.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message_list is not None:
            result['MessageList'] = self.message_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MessageList') is not None:
            temp_model = FindVersionMessagesResponseBodyMessageList()
            self.message_list = temp_model.from_map(m['MessageList'])
        return self


class FindVersionMessagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: FindVersionMessagesResponseBody = None,
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
            temp_model = FindVersionMessagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FindVersionMessageSendRecordsRequest(TeaModel):
    def __init__(
        self,
        version_type: str = None,
        project_id: str = None,
        page_index: int = None,
        page_size: int = None,
        message_type: str = None,
        version_id: str = None,
    ):
        self.version_type = version_type
        self.project_id = project_id
        self.page_index = page_index
        self.page_size = page_size
        self.message_type = message_type
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version_type is not None:
            result['VersionType'] = self.version_type
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.message_type is not None:
            result['MessageType'] = self.message_type
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VersionType') is not None:
            self.version_type = m.get('VersionType')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class FindVersionMessageSendRecordsResponseBodyMessageSendRecordListItems(TeaModel):
    def __init__(
        self,
        gmt_create_timestamp: int = None,
        message_type: str = None,
        failed_count: str = None,
        skipped_count: str = None,
        result: str = None,
        succeeded_count: str = None,
        gmt_create: str = None,
        version_id: str = None,
        result_desc: str = None,
        target_id: str = None,
        id: int = None,
    ):
        self.gmt_create_timestamp = gmt_create_timestamp
        self.message_type = message_type
        self.failed_count = failed_count
        self.skipped_count = skipped_count
        self.result = result
        self.succeeded_count = succeeded_count
        self.gmt_create = gmt_create
        self.version_id = version_id
        self.result_desc = result_desc
        self.target_id = target_id
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.gmt_create_timestamp is not None:
            result['GmtCreateTimestamp'] = self.gmt_create_timestamp
        if self.message_type is not None:
            result['MessageType'] = self.message_type
        if self.failed_count is not None:
            result['FailedCount'] = self.failed_count
        if self.skipped_count is not None:
            result['SkippedCount'] = self.skipped_count
        if self.result is not None:
            result['Result'] = self.result
        if self.succeeded_count is not None:
            result['SucceededCount'] = self.succeeded_count
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.result_desc is not None:
            result['ResultDesc'] = self.result_desc
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreateTimestamp') is not None:
            self.gmt_create_timestamp = m.get('GmtCreateTimestamp')
        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')
        if m.get('FailedCount') is not None:
            self.failed_count = m.get('FailedCount')
        if m.get('SkippedCount') is not None:
            self.skipped_count = m.get('SkippedCount')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('SucceededCount') is not None:
            self.succeeded_count = m.get('SucceededCount')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('ResultDesc') is not None:
            self.result_desc = m.get('ResultDesc')
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class FindVersionMessageSendRecordsResponseBodyMessageSendRecordList(TeaModel):
    def __init__(
        self,
        items: List[FindVersionMessageSendRecordsResponseBodyMessageSendRecordListItems] = None,
        total_count: int = None,
    ):
        self.items = items
        self.total_count = total_count

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = FindVersionMessageSendRecordsResponseBodyMessageSendRecordListItems()
                self.items.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class FindVersionMessageSendRecordsResponseBody(TeaModel):
    def __init__(
        self,
        message_send_record_list: FindVersionMessageSendRecordsResponseBodyMessageSendRecordList = None,
        request_id: str = None,
    ):
        self.message_send_record_list = message_send_record_list
        self.request_id = request_id

    def validate(self):
        if self.message_send_record_list:
            self.message_send_record_list.validate()

    def to_map(self):
        result = dict()
        if self.message_send_record_list is not None:
            result['MessageSendRecordList'] = self.message_send_record_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MessageSendRecordList') is not None:
            temp_model = FindVersionMessageSendRecordsResponseBodyMessageSendRecordList()
            self.message_send_record_list = temp_model.from_map(m['MessageSendRecordList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class FindVersionMessageSendRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: FindVersionMessageSendRecordsResponseBody = None,
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
            temp_model = FindVersionMessageSendRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FindVersionTestsRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        page_index: int = None,
        page_size: int = None,
        version_id: str = None,
        version_type: str = None,
    ):
        self.project_id = project_id
        self.page_index = page_index
        self.page_size = page_size
        self.version_id = version_id
        self.version_type = version_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.version_type is not None:
            result['VersionType'] = self.version_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('VersionType') is not None:
            self.version_type = m.get('VersionType')
        return self


class FindVersionTestsResponseBodyVersionTestListItems(TeaModel):
    def __init__(
        self,
        gmt_create_timestamp: int = None,
        gmt_modify: str = None,
        version_id: str = None,
        gmt_modify_timestamp: int = None,
        failed_count: str = None,
        device_group_id: str = None,
        skipped_count: str = None,
        description: str = None,
        succeeded_count: str = None,
        device_group_name: str = None,
        gmt_create: str = None,
        name: str = None,
        id: int = None,
        version_type: str = None,
    ):
        self.gmt_create_timestamp = gmt_create_timestamp
        self.gmt_modify = gmt_modify
        self.version_id = version_id
        self.gmt_modify_timestamp = gmt_modify_timestamp
        self.failed_count = failed_count
        self.device_group_id = device_group_id
        self.skipped_count = skipped_count
        self.description = description
        self.succeeded_count = succeeded_count
        self.device_group_name = device_group_name
        self.gmt_create = gmt_create
        self.name = name
        self.id = id
        self.version_type = version_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.gmt_create_timestamp is not None:
            result['GmtCreateTimestamp'] = self.gmt_create_timestamp
        if self.gmt_modify is not None:
            result['GmtModify'] = self.gmt_modify
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.gmt_modify_timestamp is not None:
            result['GmtModifyTimestamp'] = self.gmt_modify_timestamp
        if self.failed_count is not None:
            result['FailedCount'] = self.failed_count
        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id
        if self.skipped_count is not None:
            result['SkippedCount'] = self.skipped_count
        if self.description is not None:
            result['Description'] = self.description
        if self.succeeded_count is not None:
            result['SucceededCount'] = self.succeeded_count
        if self.device_group_name is not None:
            result['DeviceGroupName'] = self.device_group_name
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        if self.version_type is not None:
            result['VersionType'] = self.version_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreateTimestamp') is not None:
            self.gmt_create_timestamp = m.get('GmtCreateTimestamp')
        if m.get('GmtModify') is not None:
            self.gmt_modify = m.get('GmtModify')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('GmtModifyTimestamp') is not None:
            self.gmt_modify_timestamp = m.get('GmtModifyTimestamp')
        if m.get('FailedCount') is not None:
            self.failed_count = m.get('FailedCount')
        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')
        if m.get('SkippedCount') is not None:
            self.skipped_count = m.get('SkippedCount')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SucceededCount') is not None:
            self.succeeded_count = m.get('SucceededCount')
        if m.get('DeviceGroupName') is not None:
            self.device_group_name = m.get('DeviceGroupName')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('VersionType') is not None:
            self.version_type = m.get('VersionType')
        return self


class FindVersionTestsResponseBodyVersionTestList(TeaModel):
    def __init__(
        self,
        items: List[FindVersionTestsResponseBodyVersionTestListItems] = None,
        total_count: int = None,
    ):
        self.items = items
        self.total_count = total_count

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = FindVersionTestsResponseBodyVersionTestListItems()
                self.items.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class FindVersionTestsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        version_test_list: FindVersionTestsResponseBodyVersionTestList = None,
    ):
        self.request_id = request_id
        self.version_test_list = version_test_list

    def validate(self):
        if self.version_test_list:
            self.version_test_list.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.version_test_list is not None:
            result['VersionTestList'] = self.version_test_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VersionTestList') is not None:
            temp_model = FindVersionTestsResponseBodyVersionTestList()
            self.version_test_list = temp_model.from_map(m['VersionTestList'])
        return self


class FindVersionTestsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: FindVersionTestsResponseBody = None,
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
            temp_model = FindVersionTestsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FindVersionWhiteDevicesRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        version_id: str = None,
        version_type: str = None,
        device_id: str = None,
        original_id: str = None,
        page_index: int = None,
        page_size: int = None,
    ):
        self.project_id = project_id
        self.version_id = version_id
        self.version_type = version_type
        self.device_id = device_id
        self.original_id = original_id
        self.page_index = page_index
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.version_type is not None:
            result['VersionType'] = self.version_type
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.original_id is not None:
            result['OriginalId'] = self.original_id
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('VersionType') is not None:
            self.version_type = m.get('VersionType')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('OriginalId') is not None:
            self.original_id = m.get('OriginalId')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class FindVersionWhiteDevicesResponseBodyDeviceListItems(TeaModel):
    def __init__(
        self,
        gmt_create_timestamp: int = None,
        original_id: str = None,
        device_id: str = None,
        id_type: str = None,
        gmt_create: str = None,
        id: int = None,
    ):
        self.gmt_create_timestamp = gmt_create_timestamp
        self.original_id = original_id
        self.device_id = device_id
        self.id_type = id_type
        self.gmt_create = gmt_create
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.gmt_create_timestamp is not None:
            result['GmtCreateTimestamp'] = self.gmt_create_timestamp
        if self.original_id is not None:
            result['OriginalId'] = self.original_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreateTimestamp') is not None:
            self.gmt_create_timestamp = m.get('GmtCreateTimestamp')
        if m.get('OriginalId') is not None:
            self.original_id = m.get('OriginalId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class FindVersionWhiteDevicesResponseBodyDeviceList(TeaModel):
    def __init__(
        self,
        items: List[FindVersionWhiteDevicesResponseBodyDeviceListItems] = None,
        total_count: int = None,
    ):
        self.items = items
        self.total_count = total_count

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = FindVersionWhiteDevicesResponseBodyDeviceListItems()
                self.items.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class FindVersionWhiteDevicesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        device_list: FindVersionWhiteDevicesResponseBodyDeviceList = None,
    ):
        self.request_id = request_id
        self.device_list = device_list

    def validate(self):
        if self.device_list:
            self.device_list.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.device_list is not None:
            result['DeviceList'] = self.device_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DeviceList') is not None:
            temp_model = FindVersionWhiteDevicesResponseBodyDeviceList()
            self.device_list = temp_model.from_map(m['DeviceList'])
        return self


class FindVersionWhiteDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: FindVersionWhiteDevicesResponseBody = None,
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
            temp_model = FindVersionWhiteDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateAssistFileUploadUrlRequest(TeaModel):
    def __init__(
        self,
        filename: str = None,
        project_id: str = None,
        device_id: str = None,
    ):
        self.filename = filename
        self.project_id = project_id
        self.device_id = device_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.filename is not None:
            result['Filename'] = self.filename
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Filename') is not None:
            self.filename = m.get('Filename')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        return self


class GenerateAssistFileUploadUrlResponseBody(TeaModel):
    def __init__(
        self,
        file_key: str = None,
        upload_url: str = None,
        request_id: str = None,
    ):
        self.file_key = file_key
        self.upload_url = upload_url
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.file_key is not None:
            result['FileKey'] = self.file_key
        if self.upload_url is not None:
            result['UploadUrl'] = self.upload_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileKey') is not None:
            self.file_key = m.get('FileKey')
        if m.get('UploadUrl') is not None:
            self.upload_url = m.get('UploadUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GenerateAssistFileUploadUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GenerateAssistFileUploadUrlResponseBody = None,
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
            temp_model = GenerateAssistFileUploadUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateFunctionFileUploadMetaRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        file_name: str = None,
    ):
        self.project_id = project_id
        self.file_name = file_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.file_name is not None:
            result['FileName'] = self.file_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        return self


class GenerateFunctionFileUploadMetaResponseBodyUploadMetaPostObjectPolicy(TeaModel):
    def __init__(
        self,
        signature: str = None,
        host: str = None,
        policy: str = None,
        expire: str = None,
        access_id: str = None,
    ):
        self.signature = signature
        self.host = host
        self.policy = policy
        self.expire = expire
        self.access_id = access_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.signature is not None:
            result['Signature'] = self.signature
        if self.host is not None:
            result['Host'] = self.host
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        return self


class GenerateFunctionFileUploadMetaResponseBodyUploadMeta(TeaModel):
    def __init__(
        self,
        post_object_policy: GenerateFunctionFileUploadMetaResponseBodyUploadMetaPostObjectPolicy = None,
        security_token: str = None,
        object_key: str = None,
    ):
        self.post_object_policy = post_object_policy
        self.security_token = security_token
        self.object_key = object_key

    def validate(self):
        if self.post_object_policy:
            self.post_object_policy.validate()

    def to_map(self):
        result = dict()
        if self.post_object_policy is not None:
            result['PostObjectPolicy'] = self.post_object_policy.to_map()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.object_key is not None:
            result['ObjectKey'] = self.object_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PostObjectPolicy') is not None:
            temp_model = GenerateFunctionFileUploadMetaResponseBodyUploadMetaPostObjectPolicy()
            self.post_object_policy = temp_model.from_map(m['PostObjectPolicy'])
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('ObjectKey') is not None:
            self.object_key = m.get('ObjectKey')
        return self


class GenerateFunctionFileUploadMetaResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        upload_meta: GenerateFunctionFileUploadMetaResponseBodyUploadMeta = None,
    ):
        self.request_id = request_id
        self.upload_meta = upload_meta

    def validate(self):
        if self.upload_meta:
            self.upload_meta.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.upload_meta is not None:
            result['UploadMeta'] = self.upload_meta.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UploadMeta') is not None:
            temp_model = GenerateFunctionFileUploadMetaResponseBodyUploadMeta()
            self.upload_meta = temp_model.from_map(m['UploadMeta'])
        return self


class GenerateFunctionFileUploadMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GenerateFunctionFileUploadMetaResponseBody = None,
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
            temp_model = GenerateFunctionFileUploadMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateOssPostPolicyRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        ext: str = None,
        access_id: str = None,
        access_key: str = None,
    ):
        self.project_id = project_id
        self.ext = ext
        self.access_id = access_id
        self.access_key = access_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        return self


class GenerateOssPostPolicyResponseBodyOssPostPolicy(TeaModel):
    def __init__(
        self,
        signature: str = None,
        host: str = None,
        policy: str = None,
        expire: str = None,
        access_id: str = None,
    ):
        self.signature = signature
        self.host = host
        self.policy = policy
        self.expire = expire
        self.access_id = access_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.signature is not None:
            result['Signature'] = self.signature
        if self.host is not None:
            result['Host'] = self.host
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        return self


class GenerateOssPostPolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        oss_post_policy: GenerateOssPostPolicyResponseBodyOssPostPolicy = None,
    ):
        self.request_id = request_id
        self.oss_post_policy = oss_post_policy

    def validate(self):
        if self.oss_post_policy:
            self.oss_post_policy.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.oss_post_policy is not None:
            result['OssPostPolicy'] = self.oss_post_policy.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OssPostPolicy') is not None:
            temp_model = GenerateOssPostPolicyResponseBodyOssPostPolicy()
            self.oss_post_policy = temp_model.from_map(m['OssPostPolicy'])
        return self


class GenerateOssPostPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GenerateOssPostPolicyResponseBody = None,
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
            temp_model = GenerateOssPostPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateOssUploadMetaRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        ext: str = None,
    ):
        self.project_id = project_id
        self.ext = ext

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.ext is not None:
            result['Ext'] = self.ext
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        return self


class GenerateOssUploadMetaResponseBodyOssUploadMeta(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        object_key: str = None,
        access_key_secret: str = None,
        access_key_id: str = None,
        bucket: str = None,
    ):
        self.security_token = security_token
        self.object_key = object_key
        self.access_key_secret = access_key_secret
        self.access_key_id = access_key_id
        self.bucket = bucket

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.object_key is not None:
            result['ObjectKey'] = self.object_key
        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('ObjectKey') is not None:
            self.object_key = m.get('ObjectKey')
        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        return self


class GenerateOssUploadMetaResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        oss_upload_meta: GenerateOssUploadMetaResponseBodyOssUploadMeta = None,
    ):
        self.request_id = request_id
        self.oss_upload_meta = oss_upload_meta

    def validate(self):
        if self.oss_upload_meta:
            self.oss_upload_meta.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.oss_upload_meta is not None:
            result['OssUploadMeta'] = self.oss_upload_meta.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OssUploadMeta') is not None:
            temp_model = GenerateOssUploadMetaResponseBodyOssUploadMeta()
            self.oss_upload_meta = temp_model.from_map(m['OssUploadMeta'])
        return self


class GenerateOssUploadMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GenerateOssUploadMetaResponseBody = None,
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
            temp_model = GenerateOssUploadMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateSdkDownloadInfoRequest(TeaModel):
    def __init__(
        self,
        sdks: str = None,
        app_id: str = None,
        os_type: int = None,
        pkg_name: str = None,
        project_id: str = None,
        cert_file_object_key: str = None,
    ):
        self.sdks = sdks
        self.app_id = app_id
        self.os_type = os_type
        self.pkg_name = pkg_name
        self.project_id = project_id
        self.cert_file_object_key = cert_file_object_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.sdks is not None:
            result['Sdks'] = self.sdks
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.pkg_name is not None:
            result['PkgName'] = self.pkg_name
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.cert_file_object_key is not None:
            result['CertFileObjectKey'] = self.cert_file_object_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Sdks') is not None:
            self.sdks = m.get('Sdks')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('PkgName') is not None:
            self.pkg_name = m.get('PkgName')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('CertFileObjectKey') is not None:
            self.cert_file_object_key = m.get('CertFileObjectKey')
        return self


class GenerateSdkDownloadInfoResponseBodySdkDownloadInfo(TeaModel):
    def __init__(
        self,
        url: str = None,
    ):
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GenerateSdkDownloadInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        sdk_download_info: GenerateSdkDownloadInfoResponseBodySdkDownloadInfo = None,
    ):
        self.request_id = request_id
        self.sdk_download_info = sdk_download_info

    def validate(self):
        if self.sdk_download_info:
            self.sdk_download_info.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sdk_download_info is not None:
            result['SdkDownloadInfo'] = self.sdk_download_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SdkDownloadInfo') is not None:
            temp_model = GenerateSdkDownloadInfoResponseBodySdkDownloadInfo()
            self.sdk_download_info = temp_model.from_map(m['SdkDownloadInfo'])
        return self


class GenerateSdkDownloadInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GenerateSdkDownloadInfoResponseBody = None,
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
            temp_model = GenerateSdkDownloadInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateSysAppDownloadInfoRequest(TeaModel):
    def __init__(
        self,
        plugins: str = None,
        sign_mode: str = None,
        os_type: int = None,
        pkg_name: str = None,
        project_id: str = None,
        cert_file_object_key: str = None,
    ):
        self.plugins = plugins
        self.sign_mode = sign_mode
        self.os_type = os_type
        self.pkg_name = pkg_name
        self.project_id = project_id
        self.cert_file_object_key = cert_file_object_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.plugins is not None:
            result['Plugins'] = self.plugins
        if self.sign_mode is not None:
            result['SignMode'] = self.sign_mode
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.pkg_name is not None:
            result['PkgName'] = self.pkg_name
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.cert_file_object_key is not None:
            result['CertFileObjectKey'] = self.cert_file_object_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Plugins') is not None:
            self.plugins = m.get('Plugins')
        if m.get('SignMode') is not None:
            self.sign_mode = m.get('SignMode')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('PkgName') is not None:
            self.pkg_name = m.get('PkgName')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('CertFileObjectKey') is not None:
            self.cert_file_object_key = m.get('CertFileObjectKey')
        return self


class GenerateSysAppDownloadInfoResponseBodySysAppDownloadInfo(TeaModel):
    def __init__(
        self,
        url: str = None,
    ):
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GenerateSysAppDownloadInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        sys_app_download_info: GenerateSysAppDownloadInfoResponseBodySysAppDownloadInfo = None,
    ):
        self.request_id = request_id
        self.sys_app_download_info = sys_app_download_info

    def validate(self):
        if self.sys_app_download_info:
            self.sys_app_download_info.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sys_app_download_info is not None:
            result['SysAppDownloadInfo'] = self.sys_app_download_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SysAppDownloadInfo') is not None:
            temp_model = GenerateSysAppDownloadInfoResponseBodySysAppDownloadInfo()
            self.sys_app_download_info = temp_model.from_map(m['SysAppDownloadInfo'])
        return self


class GenerateSysAppDownloadInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GenerateSysAppDownloadInfoResponseBody = None,
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
            temp_model = GenerateSysAppDownloadInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDeviceAppUpdateFunnelEventsRequest(TeaModel):
    def __init__(
        self,
        package_name: str = None,
        project_id: str = None,
        target_version_code: str = None,
        id_type: str = None,
        original_id: str = None,
    ):
        self.package_name = package_name
        self.project_id = project_id
        self.target_version_code = target_version_code
        self.id_type = id_type
        self.original_id = original_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.package_name is not None:
            result['PackageName'] = self.package_name
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.target_version_code is not None:
            result['TargetVersionCode'] = self.target_version_code
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.original_id is not None:
            result['OriginalId'] = self.original_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('TargetVersionCode') is not None:
            self.target_version_code = m.get('TargetVersionCode')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OriginalId') is not None:
            self.original_id = m.get('OriginalId')
        return self


class GetDeviceAppUpdateFunnelEventsResponseBodyEventList(TeaModel):
    def __init__(
        self,
        package_name: str = None,
        device_id: str = None,
        target_version_code: str = None,
        event: str = None,
        report_timestamp: int = None,
        report_time: str = None,
        tenant_id: str = None,
    ):
        self.package_name = package_name
        self.device_id = device_id
        self.target_version_code = target_version_code
        self.event = event
        self.report_timestamp = report_timestamp
        self.report_time = report_time
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.package_name is not None:
            result['PackageName'] = self.package_name
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.target_version_code is not None:
            result['TargetVersionCode'] = self.target_version_code
        if self.event is not None:
            result['Event'] = self.event
        if self.report_timestamp is not None:
            result['ReportTimestamp'] = self.report_timestamp
        if self.report_time is not None:
            result['ReportTime'] = self.report_time
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('TargetVersionCode') is not None:
            self.target_version_code = m.get('TargetVersionCode')
        if m.get('Event') is not None:
            self.event = m.get('Event')
        if m.get('ReportTimestamp') is not None:
            self.report_timestamp = m.get('ReportTimestamp')
        if m.get('ReportTime') is not None:
            self.report_time = m.get('ReportTime')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class GetDeviceAppUpdateFunnelEventsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        event_list: List[GetDeviceAppUpdateFunnelEventsResponseBodyEventList] = None,
    ):
        self.request_id = request_id
        self.event_list = event_list

    def validate(self):
        if self.event_list:
            for k in self.event_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['EventList'] = []
        if self.event_list is not None:
            for k in self.event_list:
                result['EventList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.event_list = []
        if m.get('EventList') is not None:
            for k in m.get('EventList'):
                temp_model = GetDeviceAppUpdateFunnelEventsResponseBodyEventList()
                self.event_list.append(temp_model.from_map(k))
        return self


class GetDeviceAppUpdateFunnelEventsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDeviceAppUpdateFunnelEventsResponseBody = None,
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
            temp_model = GetDeviceAppUpdateFunnelEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDeviceSystemUpdateFunnelEventsRequest(TeaModel):
    def __init__(
        self,
        original_id: str = None,
        project_id: str = None,
        target_version: str = None,
        id_type: str = None,
    ):
        self.original_id = original_id
        self.project_id = project_id
        self.target_version = target_version
        self.id_type = id_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.original_id is not None:
            result['OriginalId'] = self.original_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.target_version is not None:
            result['TargetVersion'] = self.target_version
        if self.id_type is not None:
            result['IdType'] = self.id_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OriginalId') is not None:
            self.original_id = m.get('OriginalId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('TargetVersion') is not None:
            self.target_version = m.get('TargetVersion')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        return self


class GetDeviceSystemUpdateFunnelEventsResponseBodyEventList(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        target_version: str = None,
        event: str = None,
        report_timestamp: int = None,
        report_time: str = None,
        tenant_id: str = None,
    ):
        self.device_id = device_id
        self.target_version = target_version
        self.event = event
        self.report_timestamp = report_timestamp
        self.report_time = report_time
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.target_version is not None:
            result['TargetVersion'] = self.target_version
        if self.event is not None:
            result['Event'] = self.event
        if self.report_timestamp is not None:
            result['ReportTimestamp'] = self.report_timestamp
        if self.report_time is not None:
            result['ReportTime'] = self.report_time
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('TargetVersion') is not None:
            self.target_version = m.get('TargetVersion')
        if m.get('Event') is not None:
            self.event = m.get('Event')
        if m.get('ReportTimestamp') is not None:
            self.report_timestamp = m.get('ReportTimestamp')
        if m.get('ReportTime') is not None:
            self.report_time = m.get('ReportTime')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class GetDeviceSystemUpdateFunnelEventsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        event_list: List[GetDeviceSystemUpdateFunnelEventsResponseBodyEventList] = None,
    ):
        self.request_id = request_id
        self.event_list = event_list

    def validate(self):
        if self.event_list:
            for k in self.event_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['EventList'] = []
        if self.event_list is not None:
            for k in self.event_list:
                result['EventList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.event_list = []
        if m.get('EventList') is not None:
            for k in m.get('EventList'):
                temp_model = GetDeviceSystemUpdateFunnelEventsResponseBodyEventList()
                self.event_list.append(temp_model.from_map(k))
        return self


class GetDeviceSystemUpdateFunnelEventsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDeviceSystemUpdateFunnelEventsResponseBody = None,
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
            temp_model = GetDeviceSystemUpdateFunnelEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNamespaceDataRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        namespace: str = None,
        auth_type: str = None,
        device_id_type: str = None,
        device_id: str = None,
        account_type: str = None,
        account_id: str = None,
    ):
        self.project_id = project_id
        self.namespace = namespace
        self.auth_type = auth_type
        self.device_id_type = device_id_type
        self.device_id = device_id
        self.account_type = account_type
        self.account_id = account_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type
        if self.device_id_type is not None:
            result['DeviceIdType'] = self.device_id_type
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')
        if m.get('DeviceIdType') is not None:
            self.device_id_type = m.get('DeviceIdType')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        return self


class GetNamespaceDataResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class GetNamespaceDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetNamespaceDataResponseBody = None,
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
            temp_model = GetNamespaceDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOssUploadMetaRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        ext: str = None,
    ):
        self.project_id = project_id
        self.ext = ext

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.ext is not None:
            result['Ext'] = self.ext
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        return self


class GetOssUploadMetaResponseBodyOssUploadMeta(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        signature: str = None,
        host: str = None,
        policy: str = None,
        security_token: str = None,
        object_key: str = None,
    ):
        self.access_key = access_key
        self.signature = signature
        self.host = host
        self.policy = policy
        self.security_token = security_token
        self.object_key = object_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        if self.signature is not None:
            result['Signature'] = self.signature
        if self.host is not None:
            result['Host'] = self.host
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.object_key is not None:
            result['ObjectKey'] = self.object_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('ObjectKey') is not None:
            self.object_key = m.get('ObjectKey')
        return self


class GetOssUploadMetaResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        oss_upload_meta: GetOssUploadMetaResponseBodyOssUploadMeta = None,
    ):
        self.request_id = request_id
        self.oss_upload_meta = oss_upload_meta

    def validate(self):
        if self.oss_upload_meta:
            self.oss_upload_meta.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.oss_upload_meta is not None:
            result['OssUploadMeta'] = self.oss_upload_meta.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OssUploadMeta') is not None:
            temp_model = GetOssUploadMetaResponseBodyOssUploadMeta()
            self.oss_upload_meta = temp_model.from_map(m['OssUploadMeta'])
        return self


class GetOssUploadMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetOssUploadMetaResponseBody = None,
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
            temp_model = GetOssUploadMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InvokeFunctionRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        file_id: int = None,
        function_name: str = None,
        env: int = None,
        parameters: str = None,
    ):
        self.project_id = project_id
        self.file_id = file_id
        self.function_name = function_name
        self.env = env
        self.parameters = parameters

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.env is not None:
            result['Env'] = self.env
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        return self


class InvokeFunctionResponseBodyResult(TeaModel):
    def __init__(
        self,
        output: str = None,
        back_end_request_id: str = None,
    ):
        self.output = output
        self.back_end_request_id = back_end_request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.output is not None:
            result['Output'] = self.output
        if self.back_end_request_id is not None:
            result['BackEndRequestId'] = self.back_end_request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('BackEndRequestId') is not None:
            self.back_end_request_id = m.get('BackEndRequestId')
        return self


class InvokeFunctionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: InvokeFunctionResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = InvokeFunctionResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class InvokeFunctionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: InvokeFunctionResponseBody = None,
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
            temp_model = InvokeFunctionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListApiGatewayAppsRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
    ):
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class ListApiGatewayAppsResponseBodyApiGatewayApps(TeaModel):
    def __init__(
        self,
        gateway_app_key: str = None,
        status: int = None,
        gateway_app_secret: str = None,
        gateway_app_id: str = None,
        user_id: str = None,
        project_id: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        id: int = None,
    ):
        self.gateway_app_key = gateway_app_key
        self.status = status
        self.gateway_app_secret = gateway_app_secret
        self.gateway_app_id = gateway_app_id
        self.user_id = user_id
        self.project_id = project_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.gateway_app_key is not None:
            result['GatewayAppKey'] = self.gateway_app_key
        if self.status is not None:
            result['Status'] = self.status
        if self.gateway_app_secret is not None:
            result['GatewayAppSecret'] = self.gateway_app_secret
        if self.gateway_app_id is not None:
            result['GatewayAppId'] = self.gateway_app_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayAppKey') is not None:
            self.gateway_app_key = m.get('GatewayAppKey')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('GatewayAppSecret') is not None:
            self.gateway_app_secret = m.get('GatewayAppSecret')
        if m.get('GatewayAppId') is not None:
            self.gateway_app_id = m.get('GatewayAppId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListApiGatewayAppsResponseBody(TeaModel):
    def __init__(
        self,
        api_gateway_apps: List[ListApiGatewayAppsResponseBodyApiGatewayApps] = None,
        request_id: str = None,
    ):
        self.api_gateway_apps = api_gateway_apps
        self.request_id = request_id

    def validate(self):
        if self.api_gateway_apps:
            for k in self.api_gateway_apps:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ApiGatewayApps'] = []
        if self.api_gateway_apps is not None:
            for k in self.api_gateway_apps:
                result['ApiGatewayApps'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_gateway_apps = []
        if m.get('ApiGatewayApps') is not None:
            for k in m.get('ApiGatewayApps'):
                temp_model = ListApiGatewayAppsResponseBodyApiGatewayApps()
                self.api_gateway_apps.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListApiGatewayAppsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListApiGatewayAppsResponseBody = None,
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
            temp_model = ListApiGatewayAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppsRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
    ):
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class ListAppsResponseBodyApps(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        app_key: str = None,
        os_type: int = None,
        app_package: str = None,
    ):
        self.app_name = app_name
        self.app_key = app_key
        self.os_type = os_type
        self.app_package = app_package

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.app_package is not None:
            result['AppPackage'] = self.app_package
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('AppPackage') is not None:
            self.app_package = m.get('AppPackage')
        return self


class ListAppsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        apps: List[ListAppsResponseBodyApps] = None,
    ):
        self.request_id = request_id
        self.apps = apps

    def validate(self):
        if self.apps:
            for k in self.apps:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Apps'] = []
        if self.apps is not None:
            for k in self.apps:
                result['Apps'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.apps = []
        if m.get('Apps') is not None:
            for k in m.get('Apps'):
                temp_model = ListAppsResponseBodyApps()
                self.apps.append(temp_model.from_map(k))
        return self


class ListAppsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAppsResponseBody = None,
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
            temp_model = ListAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAssistActionDetailsRequest(TeaModel):
    def __init__(
        self,
        action_timestamp: str = None,
        project_id: str = None,
    ):
        self.action_timestamp = action_timestamp
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.action_timestamp is not None:
            result['ActionTimestamp'] = self.action_timestamp
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionTimestamp') is not None:
            self.action_timestamp = m.get('ActionTimestamp')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class ListAssistActionDetailsResponseBodyResults(TeaModel):
    def __init__(
        self,
        type: str = None,
        action: str = None,
        data: str = None,
        device_id: str = None,
        created_at: int = None,
        updated_at: int = None,
        timestamp: str = None,
        id: str = None,
    ):
        self.type = type
        self.action = action
        self.data = data
        self.device_id = device_id
        self.created_at = created_at
        self.updated_at = updated_at
        self.timestamp = timestamp
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.action is not None:
            result['Action'] = self.action
        if self.data is not None:
            result['Data'] = self.data
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.id is not None:
            result['ID'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('ID') is not None:
            self.id = m.get('ID')
        return self


class ListAssistActionDetailsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[ListAssistActionDetailsResponseBodyResults] = None,
    ):
        self.request_id = request_id
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = ListAssistActionDetailsResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class ListAssistActionDetailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAssistActionDetailsResponseBody = None,
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
            temp_model = ListAssistActionDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAssistDevicesRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        page_index: int = None,
        condition: str = None,
        per_page: int = None,
    ):
        self.project_id = project_id
        self.page_index = page_index
        self.condition = condition
        self.per_page = per_page

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.condition is not None:
            result['Condition'] = self.condition
        if self.per_page is not None:
            result['PerPage'] = self.per_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('Condition') is not None:
            self.condition = m.get('Condition')
        if m.get('PerPage') is not None:
            self.per_page = m.get('PerPage')
        return self


class ListAssistDevicesResponseBodyDevices(TeaModel):
    def __init__(
        self,
        serial_number: str = None,
        hardware_id: str = None,
        device_name: str = None,
        access_time: int = None,
        device_id: str = None,
        uuid: str = None,
        vin: str = None,
    ):
        self.serial_number = serial_number
        self.hardware_id = hardware_id
        self.device_name = device_name
        self.access_time = access_time
        self.device_id = device_id
        self.uuid = uuid
        self.vin = vin

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.hardware_id is not None:
            result['HardwareId'] = self.hardware_id
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.access_time is not None:
            result['AccessTime'] = self.access_time
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.uuid is not None:
            result['UUID'] = self.uuid
        if self.vin is not None:
            result['VIN'] = self.vin
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('HardwareId') is not None:
            self.hardware_id = m.get('HardwareId')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('AccessTime') is not None:
            self.access_time = m.get('AccessTime')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('UUID') is not None:
            self.uuid = m.get('UUID')
        if m.get('VIN') is not None:
            self.vin = m.get('VIN')
        return self


class ListAssistDevicesResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        per_page: int = None,
        page_index: int = None,
        devices: List[ListAssistDevicesResponseBodyDevices] = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.per_page = per_page
        self.page_index = page_index
        self.devices = devices

    def validate(self):
        if self.devices:
            for k in self.devices:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.per_page is not None:
            result['PerPage'] = self.per_page
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        result['Devices'] = []
        if self.devices is not None:
            for k in self.devices:
                result['Devices'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PerPage') is not None:
            self.per_page = m.get('PerPage')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        self.devices = []
        if m.get('Devices') is not None:
            for k in m.get('Devices'):
                temp_model = ListAssistDevicesResponseBodyDevices()
                self.devices.append(temp_model.from_map(k))
        return self


class ListAssistDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAssistDevicesResponseBody = None,
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
            temp_model = ListAssistDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAssistHistoriesRequest(TeaModel):
    def __init__(
        self,
        per_page: int = None,
        page_index: int = None,
        condition: str = None,
        project_id: str = None,
    ):
        self.per_page = per_page
        self.page_index = page_index
        self.condition = condition
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.per_page is not None:
            result['PerPage'] = self.per_page
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.condition is not None:
            result['Condition'] = self.condition
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PerPage') is not None:
            self.per_page = m.get('PerPage')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('Condition') is not None:
            self.condition = m.get('Condition')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class ListAssistHistoriesResponseBodyHistories(TeaModel):
    def __init__(
        self,
        serial_number: str = None,
        end_time: int = None,
        start_time: int = None,
        uname: str = None,
        hardware_id: str = None,
        device_name: str = None,
        uuid: str = None,
        device_id: str = None,
        vin: str = None,
        uid: str = None,
        id: str = None,
    ):
        self.serial_number = serial_number
        self.end_time = end_time
        self.start_time = start_time
        self.uname = uname
        self.hardware_id = hardware_id
        self.device_name = device_name
        self.uuid = uuid
        self.device_id = device_id
        self.vin = vin
        self.uid = uid
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.uname is not None:
            result['UNAME'] = self.uname
        if self.hardware_id is not None:
            result['HardwareId'] = self.hardware_id
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.uuid is not None:
            result['UUID'] = self.uuid
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.vin is not None:
            result['VIN'] = self.vin
        if self.uid is not None:
            result['UID'] = self.uid
        if self.id is not None:
            result['ID'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('UNAME') is not None:
            self.uname = m.get('UNAME')
        if m.get('HardwareId') is not None:
            self.hardware_id = m.get('HardwareId')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('UUID') is not None:
            self.uuid = m.get('UUID')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('VIN') is not None:
            self.vin = m.get('VIN')
        if m.get('UID') is not None:
            self.uid = m.get('UID')
        if m.get('ID') is not None:
            self.id = m.get('ID')
        return self


class ListAssistHistoriesResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        per_page: int = None,
        histories: List[ListAssistHistoriesResponseBodyHistories] = None,
        page_index: int = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.per_page = per_page
        self.histories = histories
        self.page_index = page_index

    def validate(self):
        if self.histories:
            for k in self.histories:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.per_page is not None:
            result['PerPage'] = self.per_page
        result['Histories'] = []
        if self.histories is not None:
            for k in self.histories:
                result['Histories'].append(k.to_map() if k else None)
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PerPage') is not None:
            self.per_page = m.get('PerPage')
        self.histories = []
        if m.get('Histories') is not None:
            for k in m.get('Histories'):
                temp_model = ListAssistHistoriesResponseBodyHistories()
                self.histories.append(temp_model.from_map(k))
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        return self


class ListAssistHistoriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAssistHistoriesResponseBody = None,
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
            temp_model = ListAssistHistoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAssistHistoryDetailsRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        assist_id: str = None,
    ):
        self.project_id = project_id
        self.assist_id = assist_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.assist_id is not None:
            result['AssistId'] = self.assist_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('AssistId') is not None:
            self.assist_id = m.get('AssistId')
        return self


class ListAssistHistoryDetailsResponseBodyActions(TeaModel):
    def __init__(
        self,
        action: str = None,
        created_at: int = None,
        timestamp: str = None,
        updated_at: int = None,
        assist_id: str = None,
        id: str = None,
    ):
        self.action = action
        self.created_at = created_at
        self.timestamp = timestamp
        self.updated_at = updated_at
        self.assist_id = assist_id
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.assist_id is not None:
            result['AssistId'] = self.assist_id
        if self.id is not None:
            result['ID'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('AssistId') is not None:
            self.assist_id = m.get('AssistId')
        if m.get('ID') is not None:
            self.id = m.get('ID')
        return self


class ListAssistHistoryDetailsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        actions: List[ListAssistHistoryDetailsResponseBodyActions] = None,
    ):
        self.request_id = request_id
        self.actions = actions

    def validate(self):
        if self.actions:
            for k in self.actions:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Actions'] = []
        if self.actions is not None:
            for k in self.actions:
                result['Actions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.actions = []
        if m.get('Actions') is not None:
            for k in m.get('Actions'):
                temp_model = ListAssistHistoryDetailsResponseBodyActions()
                self.actions.append(temp_model.from_map(k))
        return self


class ListAssistHistoryDetailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAssistHistoryDetailsResponseBody = None,
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
            temp_model = ListAssistHistoryDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClientPluginsRequest(TeaModel):
    def __init__(
        self,
        os_type: str = None,
    ):
        self.os_type = os_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.os_type is not None:
            result['OsType'] = self.os_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        return self


class ListClientPluginsResponseBodyClientPlugins(TeaModel):
    def __init__(
        self,
        pkg_name: str = None,
        name: str = None,
    ):
        self.pkg_name = pkg_name
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.pkg_name is not None:
            result['PkgName'] = self.pkg_name
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PkgName') is not None:
            self.pkg_name = m.get('PkgName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListClientPluginsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        client_plugins: List[ListClientPluginsResponseBodyClientPlugins] = None,
    ):
        self.request_id = request_id
        self.client_plugins = client_plugins

    def validate(self):
        if self.client_plugins:
            for k in self.client_plugins:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ClientPlugins'] = []
        if self.client_plugins is not None:
            for k in self.client_plugins:
                result['ClientPlugins'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.client_plugins = []
        if m.get('ClientPlugins') is not None:
            for k in m.get('ClientPlugins'):
                temp_model = ListClientPluginsResponseBodyClientPlugins()
                self.client_plugins.append(temp_model.from_map(k))
        return self


class ListClientPluginsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListClientPluginsResponseBody = None,
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
            temp_model = ListClientPluginsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClientPluginVersionsRequest(TeaModel):
    def __init__(
        self,
        os_type: str = None,
        pkg_name: str = None,
    ):
        self.os_type = os_type
        self.pkg_name = pkg_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.pkg_name is not None:
            result['PkgName'] = self.pkg_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('PkgName') is not None:
            self.pkg_name = m.get('PkgName')
        return self


class ListClientPluginVersionsResponseBodyClientPluginVersions(TeaModel):
    def __init__(
        self,
        version: str = None,
        download_url: str = None,
        size: int = None,
        pkg_name: str = None,
        version_code: int = None,
        id: int = None,
    ):
        self.version = version
        self.download_url = download_url
        self.size = size
        self.pkg_name = pkg_name
        self.version_code = version_code
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        if self.size is not None:
            result['Size'] = self.size
        if self.pkg_name is not None:
            result['PkgName'] = self.pkg_name
        if self.version_code is not None:
            result['VersionCode'] = self.version_code
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('PkgName') is not None:
            self.pkg_name = m.get('PkgName')
        if m.get('VersionCode') is not None:
            self.version_code = m.get('VersionCode')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListClientPluginVersionsResponseBody(TeaModel):
    def __init__(
        self,
        client_plugin_versions: List[ListClientPluginVersionsResponseBodyClientPluginVersions] = None,
        request_id: str = None,
    ):
        self.client_plugin_versions = client_plugin_versions
        self.request_id = request_id

    def validate(self):
        if self.client_plugin_versions:
            for k in self.client_plugin_versions:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ClientPluginVersions'] = []
        if self.client_plugin_versions is not None:
            for k in self.client_plugin_versions:
                result['ClientPluginVersions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.client_plugin_versions = []
        if m.get('ClientPluginVersions') is not None:
            for k in m.get('ClientPluginVersions'):
                temp_model = ListClientPluginVersionsResponseBodyClientPluginVersions()
                self.client_plugin_versions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListClientPluginVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListClientPluginVersionsResponseBody = None,
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
            temp_model = ListClientPluginVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClientSdksRequest(TeaModel):
    def __init__(
        self,
        os_type: str = None,
    ):
        self.os_type = os_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.os_type is not None:
            result['OsType'] = self.os_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        return self


class ListClientSdksResponseBodyClientSdks(TeaModel):
    def __init__(
        self,
        os_type: int = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        name: str = None,
        pkg_name: str = None,
        pkg_type: int = None,
        id: int = None,
    ):
        self.os_type = os_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.name = name
        self.pkg_name = pkg_name
        self.pkg_type = pkg_type
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.name is not None:
            result['Name'] = self.name
        if self.pkg_name is not None:
            result['PkgName'] = self.pkg_name
        if self.pkg_type is not None:
            result['PkgType'] = self.pkg_type
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PkgName') is not None:
            self.pkg_name = m.get('PkgName')
        if m.get('PkgType') is not None:
            self.pkg_type = m.get('PkgType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListClientSdksResponseBody(TeaModel):
    def __init__(
        self,
        client_sdks: List[ListClientSdksResponseBodyClientSdks] = None,
        request_id: str = None,
    ):
        self.client_sdks = client_sdks
        self.request_id = request_id

    def validate(self):
        if self.client_sdks:
            for k in self.client_sdks:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ClientSdks'] = []
        if self.client_sdks is not None:
            for k in self.client_sdks:
                result['ClientSdks'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.client_sdks = []
        if m.get('ClientSdks') is not None:
            for k in m.get('ClientSdks'):
                temp_model = ListClientSdksResponseBodyClientSdks()
                self.client_sdks.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListClientSdksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListClientSdksResponseBody = None,
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
            temp_model = ListClientSdksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListConnectLogsRequest(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        project_id: str = None,
        device_id: str = None,
        start_time: int = None,
        end_time: int = None,
        page_index: int = None,
    ):
        self.page_size = page_size
        self.project_id = project_id
        self.device_id = device_id
        self.start_time = start_time
        self.end_time = end_time
        self.page_index = page_index

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        return self


class ListConnectLogsResponseBodyLogsPagination(TeaModel):
    def __init__(
        self,
        page_index: int = None,
        total_page_count: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.page_index = page_index
        self.total_page_count = total_page_count
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.total_page_count is not None:
            result['TotalPageCount'] = self.total_page_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('TotalPageCount') is not None:
            self.total_page_count = m.get('TotalPageCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListConnectLogsResponseBodyLogsList(TeaModel):
    def __init__(
        self,
        sid: str = None,
        status: str = None,
        time: int = None,
        device_id: str = None,
        system_version: str = None,
        ip: str = None,
        net_working: str = None,
        terminal: str = None,
    ):
        self.sid = sid
        self.status = status
        self.time = time
        self.device_id = device_id
        self.system_version = system_version
        self.ip = ip
        self.net_working = net_working
        self.terminal = terminal

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.sid is not None:
            result['Sid'] = self.sid
        if self.status is not None:
            result['Status'] = self.status
        if self.time is not None:
            result['Time'] = self.time
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.system_version is not None:
            result['SystemVersion'] = self.system_version
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.net_working is not None:
            result['NetWorking'] = self.net_working
        if self.terminal is not None:
            result['Terminal'] = self.terminal
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Sid') is not None:
            self.sid = m.get('Sid')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('SystemVersion') is not None:
            self.system_version = m.get('SystemVersion')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('NetWorking') is not None:
            self.net_working = m.get('NetWorking')
        if m.get('Terminal') is not None:
            self.terminal = m.get('Terminal')
        return self


class ListConnectLogsResponseBodyLogs(TeaModel):
    def __init__(
        self,
        pagination: ListConnectLogsResponseBodyLogsPagination = None,
        list: List[ListConnectLogsResponseBodyLogsList] = None,
    ):
        self.pagination = pagination
        self.list = list

    def validate(self):
        if self.pagination:
            self.pagination.validate()
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.pagination is not None:
            result['Pagination'] = self.pagination.to_map()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pagination') is not None:
            temp_model = ListConnectLogsResponseBodyLogsPagination()
            self.pagination = temp_model.from_map(m['Pagination'])
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListConnectLogsResponseBodyLogsList()
                self.list.append(temp_model.from_map(k))
        return self


class ListConnectLogsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        logs: ListConnectLogsResponseBodyLogs = None,
    ):
        self.request_id = request_id
        self.logs = logs

    def validate(self):
        if self.logs:
            self.logs.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.logs is not None:
            result['Logs'] = self.logs.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Logs') is not None:
            temp_model = ListConnectLogsResponseBodyLogs()
            self.logs = temp_model.from_map(m['Logs'])
        return self


class ListConnectLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListConnectLogsResponseBody = None,
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
            temp_model = ListConnectLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeployedFunctionsRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        file_id: int = None,
    ):
        self.project_id = project_id
        self.file_id = file_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.file_id is not None:
            result['FileId'] = self.file_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        return self


class ListDeployedFunctionsResponseBodyFunctions(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        gmt_create: int = None,
        name: str = None,
        gmt_modified: int = None,
        id: int = None,
        file_id: int = None,
    ):
        self.project_id = project_id
        self.gmt_create = gmt_create
        self.name = name
        self.gmt_modified = gmt_modified
        self.id = id
        self.file_id = file_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.name is not None:
            result['Name'] = self.name
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.file_id is not None:
            result['FileId'] = self.file_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        return self


class ListDeployedFunctionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        functions: List[ListDeployedFunctionsResponseBodyFunctions] = None,
    ):
        self.request_id = request_id
        self.functions = functions

    def validate(self):
        if self.functions:
            for k in self.functions:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Functions'] = []
        if self.functions is not None:
            for k in self.functions:
                result['Functions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.functions = []
        if m.get('Functions') is not None:
            for k in m.get('Functions'):
                temp_model = ListDeployedFunctionsResponseBodyFunctions()
                self.functions.append(temp_model.from_map(k))
        return self


class ListDeployedFunctionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDeployedFunctionsResponseBody = None,
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
            temp_model = ListDeployedFunctionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeviceBrandsRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        device_brand_id: int = None,
        device_brand: str = None,
        start: str = None,
        length: str = None,
    ):
        self.project_id = project_id
        self.device_brand_id = device_brand_id
        self.device_brand = device_brand
        self.start = start
        self.length = length

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.device_brand_id is not None:
            result['DeviceBrandId'] = self.device_brand_id
        if self.device_brand is not None:
            result['DeviceBrand'] = self.device_brand
        if self.start is not None:
            result['Start'] = self.start
        if self.length is not None:
            result['Length'] = self.length
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('DeviceBrandId') is not None:
            self.device_brand_id = m.get('DeviceBrandId')
        if m.get('DeviceBrand') is not None:
            self.device_brand = m.get('DeviceBrand')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        if m.get('Length') is not None:
            self.length = m.get('Length')
        return self


class ListDeviceBrandsResponseBodyDeviceBrands(TeaModel):
    def __init__(
        self,
        device_brand_id: int = None,
        description: str = None,
        project_id: str = None,
        manufacture: str = None,
        device_brand: str = None,
    ):
        self.device_brand_id = device_brand_id
        self.description = description
        self.project_id = project_id
        self.manufacture = manufacture
        self.device_brand = device_brand

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.device_brand_id is not None:
            result['DeviceBrandId'] = self.device_brand_id
        if self.description is not None:
            result['Description'] = self.description
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.manufacture is not None:
            result['Manufacture'] = self.manufacture
        if self.device_brand is not None:
            result['DeviceBrand'] = self.device_brand
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceBrandId') is not None:
            self.device_brand_id = m.get('DeviceBrandId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Manufacture') is not None:
            self.manufacture = m.get('Manufacture')
        if m.get('DeviceBrand') is not None:
            self.device_brand = m.get('DeviceBrand')
        return self


class ListDeviceBrandsResponseBody(TeaModel):
    def __init__(
        self,
        device_brands: List[ListDeviceBrandsResponseBodyDeviceBrands] = None,
        request_id: str = None,
    ):
        self.device_brands = device_brands
        self.request_id = request_id

    def validate(self):
        if self.device_brands:
            for k in self.device_brands:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['DeviceBrands'] = []
        if self.device_brands is not None:
            for k in self.device_brands:
                result['DeviceBrands'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.device_brands = []
        if m.get('DeviceBrands') is not None:
            for k in m.get('DeviceBrands'):
                temp_model = ListDeviceBrandsResponseBodyDeviceBrands()
                self.device_brands.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDeviceBrandsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDeviceBrandsResponseBody = None,
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
            temp_model = ListDeviceBrandsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeviceModelRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
    ):
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class ListDeviceModelResponseBodyModelList(TeaModel):
    def __init__(
        self,
        device_model_id: int = None,
        hardware_type: str = None,
        device_type: str = None,
        can_create_device_id: int = None,
        project_id: str = None,
        os_platform: str = None,
        device_model: str = None,
        security_chip: str = None,
        description: str = None,
        init_usage_type_desc: str = None,
        init_usage_type: int = None,
        device_brand: str = None,
    ):
        self.device_model_id = device_model_id
        self.hardware_type = hardware_type
        self.device_type = device_type
        self.can_create_device_id = can_create_device_id
        self.project_id = project_id
        self.os_platform = os_platform
        self.device_model = device_model
        self.security_chip = security_chip
        self.description = description
        self.init_usage_type_desc = init_usage_type_desc
        self.init_usage_type = init_usage_type
        self.device_brand = device_brand

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.device_model_id is not None:
            result['DeviceModelId'] = self.device_model_id
        if self.hardware_type is not None:
            result['HardwareType'] = self.hardware_type
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.can_create_device_id is not None:
            result['CanCreateDeviceId'] = self.can_create_device_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.os_platform is not None:
            result['OsPlatform'] = self.os_platform
        if self.device_model is not None:
            result['DeviceModel'] = self.device_model
        if self.security_chip is not None:
            result['SecurityChip'] = self.security_chip
        if self.description is not None:
            result['Description'] = self.description
        if self.init_usage_type_desc is not None:
            result['InitUsageTypeDesc'] = self.init_usage_type_desc
        if self.init_usage_type is not None:
            result['InitUsageType'] = self.init_usage_type
        if self.device_brand is not None:
            result['DeviceBrand'] = self.device_brand
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceModelId') is not None:
            self.device_model_id = m.get('DeviceModelId')
        if m.get('HardwareType') is not None:
            self.hardware_type = m.get('HardwareType')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('CanCreateDeviceId') is not None:
            self.can_create_device_id = m.get('CanCreateDeviceId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('OsPlatform') is not None:
            self.os_platform = m.get('OsPlatform')
        if m.get('DeviceModel') is not None:
            self.device_model = m.get('DeviceModel')
        if m.get('SecurityChip') is not None:
            self.security_chip = m.get('SecurityChip')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InitUsageTypeDesc') is not None:
            self.init_usage_type_desc = m.get('InitUsageTypeDesc')
        if m.get('InitUsageType') is not None:
            self.init_usage_type = m.get('InitUsageType')
        if m.get('DeviceBrand') is not None:
            self.device_brand = m.get('DeviceBrand')
        return self


class ListDeviceModelResponseBody(TeaModel):
    def __init__(
        self,
        model_list: List[ListDeviceModelResponseBodyModelList] = None,
        request_id: str = None,
    ):
        self.model_list = model_list
        self.request_id = request_id

    def validate(self):
        if self.model_list:
            for k in self.model_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ModelList'] = []
        if self.model_list is not None:
            for k in self.model_list:
                result['ModelList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.model_list = []
        if m.get('ModelList') is not None:
            for k in m.get('ModelList'):
                temp_model = ListDeviceModelResponseBodyModelList()
                self.model_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDeviceModelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDeviceModelResponseBody = None,
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
            temp_model = ListDeviceModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeviceModelsRequest(TeaModel):
    def __init__(
        self,
        device_model_id: int = None,
        length: str = None,
        device_model: str = None,
        device_brand: str = None,
        start: str = None,
        project_id: str = None,
        device_brand_id: int = None,
    ):
        self.device_model_id = device_model_id
        self.length = length
        self.device_model = device_model
        self.device_brand = device_brand
        self.start = start
        self.project_id = project_id
        self.device_brand_id = device_brand_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.device_model_id is not None:
            result['DeviceModelId'] = self.device_model_id
        if self.length is not None:
            result['Length'] = self.length
        if self.device_model is not None:
            result['DeviceModel'] = self.device_model
        if self.device_brand is not None:
            result['DeviceBrand'] = self.device_brand
        if self.start is not None:
            result['Start'] = self.start
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.device_brand_id is not None:
            result['DeviceBrandId'] = self.device_brand_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceModelId') is not None:
            self.device_model_id = m.get('DeviceModelId')
        if m.get('Length') is not None:
            self.length = m.get('Length')
        if m.get('DeviceModel') is not None:
            self.device_model = m.get('DeviceModel')
        if m.get('DeviceBrand') is not None:
            self.device_brand = m.get('DeviceBrand')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('DeviceBrandId') is not None:
            self.device_brand_id = m.get('DeviceBrandId')
        return self


class ListDeviceModelsResponseBodyDeviceModels(TeaModel):
    def __init__(
        self,
        device_model_id: int = None,
        hardware_type: str = None,
        device_name: str = None,
        device_type: str = None,
        can_create_device_id: int = None,
        project_id: str = None,
        os_platform: str = None,
        device_model: str = None,
        security_chip: str = None,
        device_logo_url: str = None,
        description: str = None,
        object_key: str = None,
        init_usage_type_desc: str = None,
        init_usage_type: int = None,
        device_brand: str = None,
    ):
        self.device_model_id = device_model_id
        self.hardware_type = hardware_type
        self.device_name = device_name
        self.device_type = device_type
        self.can_create_device_id = can_create_device_id
        self.project_id = project_id
        self.os_platform = os_platform
        self.device_model = device_model
        self.security_chip = security_chip
        self.device_logo_url = device_logo_url
        self.description = description
        self.object_key = object_key
        self.init_usage_type_desc = init_usage_type_desc
        self.init_usage_type = init_usage_type
        self.device_brand = device_brand

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.device_model_id is not None:
            result['DeviceModelId'] = self.device_model_id
        if self.hardware_type is not None:
            result['HardwareType'] = self.hardware_type
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.can_create_device_id is not None:
            result['CanCreateDeviceId'] = self.can_create_device_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.os_platform is not None:
            result['OsPlatform'] = self.os_platform
        if self.device_model is not None:
            result['DeviceModel'] = self.device_model
        if self.security_chip is not None:
            result['SecurityChip'] = self.security_chip
        if self.device_logo_url is not None:
            result['DeviceLogoUrl'] = self.device_logo_url
        if self.description is not None:
            result['Description'] = self.description
        if self.object_key is not None:
            result['ObjectKey'] = self.object_key
        if self.init_usage_type_desc is not None:
            result['InitUsageTypeDesc'] = self.init_usage_type_desc
        if self.init_usage_type is not None:
            result['InitUsageType'] = self.init_usage_type
        if self.device_brand is not None:
            result['DeviceBrand'] = self.device_brand
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceModelId') is not None:
            self.device_model_id = m.get('DeviceModelId')
        if m.get('HardwareType') is not None:
            self.hardware_type = m.get('HardwareType')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('CanCreateDeviceId') is not None:
            self.can_create_device_id = m.get('CanCreateDeviceId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('OsPlatform') is not None:
            self.os_platform = m.get('OsPlatform')
        if m.get('DeviceModel') is not None:
            self.device_model = m.get('DeviceModel')
        if m.get('SecurityChip') is not None:
            self.security_chip = m.get('SecurityChip')
        if m.get('DeviceLogoUrl') is not None:
            self.device_logo_url = m.get('DeviceLogoUrl')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ObjectKey') is not None:
            self.object_key = m.get('ObjectKey')
        if m.get('InitUsageTypeDesc') is not None:
            self.init_usage_type_desc = m.get('InitUsageTypeDesc')
        if m.get('InitUsageType') is not None:
            self.init_usage_type = m.get('InitUsageType')
        if m.get('DeviceBrand') is not None:
            self.device_brand = m.get('DeviceBrand')
        return self


class ListDeviceModelsResponseBody(TeaModel):
    def __init__(
        self,
        device_models: List[ListDeviceModelsResponseBodyDeviceModels] = None,
        request_id: str = None,
    ):
        self.device_models = device_models
        self.request_id = request_id

    def validate(self):
        if self.device_models:
            for k in self.device_models:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['DeviceModels'] = []
        if self.device_models is not None:
            for k in self.device_models:
                result['DeviceModels'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.device_models = []
        if m.get('DeviceModels') is not None:
            for k in m.get('DeviceModels'):
                temp_model = ListDeviceModelsResponseBodyDeviceModels()
                self.device_models.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDeviceModelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDeviceModelsResponseBody = None,
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
            temp_model = ListDeviceModelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDevicesRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        device_model_id: int = None,
        device_model: str = None,
        start: str = None,
        length: str = None,
    ):
        self.project_id = project_id
        self.device_model_id = device_model_id
        self.device_model = device_model
        self.start = start
        self.length = length

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.device_model_id is not None:
            result['DeviceModelId'] = self.device_model_id
        if self.device_model is not None:
            result['DeviceModel'] = self.device_model
        if self.start is not None:
            result['Start'] = self.start
        if self.length is not None:
            result['Length'] = self.length
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('DeviceModelId') is not None:
            self.device_model_id = m.get('DeviceModelId')
        if m.get('DeviceModel') is not None:
            self.device_model = m.get('DeviceModel')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        if m.get('Length') is not None:
            self.length = m.get('Length')
        return self


class ListDevicesResponseBodyDevices(TeaModel):
    def __init__(
        self,
        serial_number: str = None,
        status: str = None,
        device_model_id: int = None,
        mac_address: str = None,
        device_id: str = None,
        device_type: str = None,
        project_id: str = None,
        device_model: str = None,
        usage_type: int = None,
        vin: str = None,
        usage_type_desc: str = None,
        uuid: str = None,
        hardware_id: str = None,
        region: str = None,
        software_id: str = None,
        name: str = None,
        device_brand: str = None,
    ):
        self.serial_number = serial_number
        self.status = status
        self.device_model_id = device_model_id
        self.mac_address = mac_address
        self.device_id = device_id
        self.device_type = device_type
        self.project_id = project_id
        self.device_model = device_model
        self.usage_type = usage_type
        self.vin = vin
        self.usage_type_desc = usage_type_desc
        self.uuid = uuid
        self.hardware_id = hardware_id
        self.region = region
        self.software_id = software_id
        self.name = name
        self.device_brand = device_brand

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.status is not None:
            result['Status'] = self.status
        if self.device_model_id is not None:
            result['DeviceModelId'] = self.device_model_id
        if self.mac_address is not None:
            result['MacAddress'] = self.mac_address
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.device_model is not None:
            result['DeviceModel'] = self.device_model
        if self.usage_type is not None:
            result['UsageType'] = self.usage_type
        if self.vin is not None:
            result['Vin'] = self.vin
        if self.usage_type_desc is not None:
            result['UsageTypeDesc'] = self.usage_type_desc
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.hardware_id is not None:
            result['HardwareId'] = self.hardware_id
        if self.region is not None:
            result['Region'] = self.region
        if self.software_id is not None:
            result['SoftwareId'] = self.software_id
        if self.name is not None:
            result['Name'] = self.name
        if self.device_brand is not None:
            result['DeviceBrand'] = self.device_brand
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('DeviceModelId') is not None:
            self.device_model_id = m.get('DeviceModelId')
        if m.get('MacAddress') is not None:
            self.mac_address = m.get('MacAddress')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('DeviceModel') is not None:
            self.device_model = m.get('DeviceModel')
        if m.get('UsageType') is not None:
            self.usage_type = m.get('UsageType')
        if m.get('Vin') is not None:
            self.vin = m.get('Vin')
        if m.get('UsageTypeDesc') is not None:
            self.usage_type_desc = m.get('UsageTypeDesc')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('HardwareId') is not None:
            self.hardware_id = m.get('HardwareId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('SoftwareId') is not None:
            self.software_id = m.get('SoftwareId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('DeviceBrand') is not None:
            self.device_brand = m.get('DeviceBrand')
        return self


class ListDevicesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        devices: List[ListDevicesResponseBodyDevices] = None,
    ):
        self.request_id = request_id
        self.devices = devices

    def validate(self):
        if self.devices:
            for k in self.devices:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Devices'] = []
        if self.devices is not None:
            for k in self.devices:
                result['Devices'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.devices = []
        if m.get('Devices') is not None:
            for k in m.get('Devices'):
                temp_model = ListDevicesResponseBodyDevices()
                self.devices.append(temp_model.from_map(k))
        return self


class ListDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDevicesResponseBody = None,
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
            temp_model = ListDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeviceTypesRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
    ):
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class ListDeviceTypesResponseBodyDeviceTypes(TeaModel):
    def __init__(
        self,
        device_type: str = None,
        name: str = None,
    ):
        self.device_type = device_type
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListDeviceTypesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        device_types: List[ListDeviceTypesResponseBodyDeviceTypes] = None,
    ):
        self.request_id = request_id
        self.device_types = device_types

    def validate(self):
        if self.device_types:
            for k in self.device_types:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['DeviceTypes'] = []
        if self.device_types is not None:
            for k in self.device_types:
                result['DeviceTypes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.device_types = []
        if m.get('DeviceTypes') is not None:
            for k in m.get('DeviceTypes'):
                temp_model = ListDeviceTypesResponseBodyDeviceTypes()
                self.device_types.append(temp_model.from_map(k))
        return self


class ListDeviceTypesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDeviceTypesResponseBody = None,
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
            temp_model = ListDeviceTypesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFunctionExecuteLogRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        file_id: int = None,
        function_name: str = None,
        env: int = None,
        page_index: int = None,
        page_size: int = None,
    ):
        self.project_id = project_id
        self.file_id = file_id
        self.function_name = function_name
        self.env = env
        self.page_index = page_index
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.env is not None:
            result['Env'] = self.env
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListFunctionExecuteLogResponseBodyLogListPagination(TeaModel):
    def __init__(
        self,
        page_index: int = None,
        page_size: int = None,
        has_next_page: bool = None,
    ):
        self.page_index = page_index
        self.page_size = page_size
        self.has_next_page = has_next_page

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.has_next_page is not None:
            result['HasNextPage'] = self.has_next_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('HasNextPage') is not None:
            self.has_next_page = m.get('HasNextPage')
        return self


class ListFunctionExecuteLogResponseBodyLogListLogs(TeaModel):
    def __init__(
        self,
        message: str = None,
        back_end_request_id: str = None,
    ):
        self.message = message
        self.back_end_request_id = back_end_request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.back_end_request_id is not None:
            result['BackEndRequestId'] = self.back_end_request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('BackEndRequestId') is not None:
            self.back_end_request_id = m.get('BackEndRequestId')
        return self


class ListFunctionExecuteLogResponseBodyLogList(TeaModel):
    def __init__(
        self,
        pagination: ListFunctionExecuteLogResponseBodyLogListPagination = None,
        logs: List[ListFunctionExecuteLogResponseBodyLogListLogs] = None,
    ):
        self.pagination = pagination
        self.logs = logs

    def validate(self):
        if self.pagination:
            self.pagination.validate()
        if self.logs:
            for k in self.logs:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.pagination is not None:
            result['Pagination'] = self.pagination.to_map()
        result['Logs'] = []
        if self.logs is not None:
            for k in self.logs:
                result['Logs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pagination') is not None:
            temp_model = ListFunctionExecuteLogResponseBodyLogListPagination()
            self.pagination = temp_model.from_map(m['Pagination'])
        self.logs = []
        if m.get('Logs') is not None:
            for k in m.get('Logs'):
                temp_model = ListFunctionExecuteLogResponseBodyLogListLogs()
                self.logs.append(temp_model.from_map(k))
        return self


class ListFunctionExecuteLogResponseBody(TeaModel):
    def __init__(
        self,
        log_list: ListFunctionExecuteLogResponseBodyLogList = None,
        request_id: str = None,
    ):
        self.log_list = log_list
        self.request_id = request_id

    def validate(self):
        if self.log_list:
            self.log_list.validate()

    def to_map(self):
        result = dict()
        if self.log_list is not None:
            result['LogList'] = self.log_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogList') is not None:
            temp_model = ListFunctionExecuteLogResponseBodyLogList()
            self.log_list = temp_model.from_map(m['LogList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListFunctionExecuteLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListFunctionExecuteLogResponseBody = None,
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
            temp_model = ListFunctionExecuteLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFunctionFilesRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        file_type: int = None,
        page_index: int = None,
        page_size: int = None,
    ):
        self.project_id = project_id
        self.file_type = file_type
        self.page_index = page_index
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListFunctionFilesResponseBodyFileListPagination(TeaModel):
    def __init__(
        self,
        page_index: int = None,
        total_page_count: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.page_index = page_index
        self.total_page_count = total_page_count
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.total_page_count is not None:
            result['TotalPageCount'] = self.total_page_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('TotalPageCount') is not None:
            self.total_page_count = m.get('TotalPageCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListFunctionFilesResponseBodyFileListFiles(TeaModel):
    def __init__(
        self,
        status: int = None,
        production_deploy_time: int = None,
        production_deploy_status: int = None,
        description: str = None,
        sandbox_deploy_time: int = None,
        gmt_create: int = None,
        sandbox_deploy_status: int = None,
        gmt_modified: int = None,
        name: str = None,
        content_id: int = None,
        id: int = None,
    ):
        self.status = status
        self.production_deploy_time = production_deploy_time
        self.production_deploy_status = production_deploy_status
        self.description = description
        self.sandbox_deploy_time = sandbox_deploy_time
        self.gmt_create = gmt_create
        self.sandbox_deploy_status = sandbox_deploy_status
        self.gmt_modified = gmt_modified
        self.name = name
        self.content_id = content_id
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.production_deploy_time is not None:
            result['ProductionDeployTime'] = self.production_deploy_time
        if self.production_deploy_status is not None:
            result['ProductionDeployStatus'] = self.production_deploy_status
        if self.description is not None:
            result['Description'] = self.description
        if self.sandbox_deploy_time is not None:
            result['SandboxDeployTime'] = self.sandbox_deploy_time
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.sandbox_deploy_status is not None:
            result['SandboxDeployStatus'] = self.sandbox_deploy_status
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.name is not None:
            result['Name'] = self.name
        if self.content_id is not None:
            result['ContentId'] = self.content_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ProductionDeployTime') is not None:
            self.production_deploy_time = m.get('ProductionDeployTime')
        if m.get('ProductionDeployStatus') is not None:
            self.production_deploy_status = m.get('ProductionDeployStatus')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SandboxDeployTime') is not None:
            self.sandbox_deploy_time = m.get('SandboxDeployTime')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('SandboxDeployStatus') is not None:
            self.sandbox_deploy_status = m.get('SandboxDeployStatus')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ContentId') is not None:
            self.content_id = m.get('ContentId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListFunctionFilesResponseBodyFileList(TeaModel):
    def __init__(
        self,
        pagination: ListFunctionFilesResponseBodyFileListPagination = None,
        files: List[ListFunctionFilesResponseBodyFileListFiles] = None,
    ):
        self.pagination = pagination
        self.files = files

    def validate(self):
        if self.pagination:
            self.pagination.validate()
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.pagination is not None:
            result['Pagination'] = self.pagination.to_map()
        result['Files'] = []
        if self.files is not None:
            for k in self.files:
                result['Files'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pagination') is not None:
            temp_model = ListFunctionFilesResponseBodyFileListPagination()
            self.pagination = temp_model.from_map(m['Pagination'])
        self.files = []
        if m.get('Files') is not None:
            for k in m.get('Files'):
                temp_model = ListFunctionFilesResponseBodyFileListFiles()
                self.files.append(temp_model.from_map(k))
        return self


class ListFunctionFilesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        file_list: ListFunctionFilesResponseBodyFileList = None,
    ):
        self.request_id = request_id
        self.file_list = file_list

    def validate(self):
        if self.file_list:
            self.file_list.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.file_list is not None:
            result['FileList'] = self.file_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('FileList') is not None:
            temp_model = ListFunctionFilesResponseBodyFileList()
            self.file_list = temp_model.from_map(m['FileList'])
        return self


class ListFunctionFilesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListFunctionFilesResponseBody = None,
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
            temp_model = ListFunctionFilesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFunctionFilesByProjectIdRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        page_index: int = None,
        page_size: int = None,
    ):
        self.project_id = project_id
        self.page_index = page_index
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListFunctionFilesByProjectIdResponseBodyFiles(TeaModel):
    def __init__(
        self,
        type: int = None,
        status: int = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        name: str = None,
        id: int = None,
        content_id: int = None,
    ):
        self.type = type
        self.status = status
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.name = name
        self.id = id
        self.content_id = content_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.status is not None:
            result['Status'] = self.status
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        if self.content_id is not None:
            result['ContentId'] = self.content_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ContentId') is not None:
            self.content_id = m.get('ContentId')
        return self


class ListFunctionFilesByProjectIdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        files: List[ListFunctionFilesByProjectIdResponseBodyFiles] = None,
    ):
        self.request_id = request_id
        self.files = files

    def validate(self):
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Files'] = []
        if self.files is not None:
            for k in self.files:
                result['Files'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.files = []
        if m.get('Files') is not None:
            for k in m.get('Files'):
                temp_model = ListFunctionFilesByProjectIdResponseBodyFiles()
                self.files.append(temp_model.from_map(k))
        return self


class ListFunctionFilesByProjectIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListFunctionFilesByProjectIdResponseBody = None,
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
            temp_model = ListFunctionFilesByProjectIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMessageAcksRequest(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        project_id: str = None,
        device_id: str = None,
        message_id: int = None,
        page_index: int = None,
    ):
        self.page_size = page_size
        self.project_id = project_id
        self.device_id = device_id
        self.message_id = message_id
        self.page_index = page_index

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        return self


class ListMessageAcksResponseBodyMessageAcksPagination(TeaModel):
    def __init__(
        self,
        page_index: int = None,
        total_page_count: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.page_index = page_index
        self.total_page_count = total_page_count
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.total_page_count is not None:
            result['TotalPageCount'] = self.total_page_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('TotalPageCount') is not None:
            self.total_page_count = m.get('TotalPageCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListMessageAcksResponseBodyMessageAcksList(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        ack_time: int = None,
        mid: int = None,
    ):
        self.device_id = device_id
        self.ack_time = ack_time
        self.mid = mid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.ack_time is not None:
            result['AckTime'] = self.ack_time
        if self.mid is not None:
            result['Mid'] = self.mid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('AckTime') is not None:
            self.ack_time = m.get('AckTime')
        if m.get('Mid') is not None:
            self.mid = m.get('Mid')
        return self


class ListMessageAcksResponseBodyMessageAcks(TeaModel):
    def __init__(
        self,
        pagination: ListMessageAcksResponseBodyMessageAcksPagination = None,
        list: List[ListMessageAcksResponseBodyMessageAcksList] = None,
    ):
        self.pagination = pagination
        self.list = list

    def validate(self):
        if self.pagination:
            self.pagination.validate()
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.pagination is not None:
            result['Pagination'] = self.pagination.to_map()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pagination') is not None:
            temp_model = ListMessageAcksResponseBodyMessageAcksPagination()
            self.pagination = temp_model.from_map(m['Pagination'])
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListMessageAcksResponseBodyMessageAcksList()
                self.list.append(temp_model.from_map(k))
        return self


class ListMessageAcksResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message_acks: ListMessageAcksResponseBodyMessageAcks = None,
    ):
        self.request_id = request_id
        self.message_acks = message_acks

    def validate(self):
        if self.message_acks:
            self.message_acks.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message_acks is not None:
            result['MessageAcks'] = self.message_acks.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MessageAcks') is not None:
            temp_model = ListMessageAcksResponseBodyMessageAcks()
            self.message_acks = temp_model.from_map(m['MessageAcks'])
        return self


class ListMessageAcksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListMessageAcksResponseBody = None,
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
            temp_model = ListMessageAcksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMessageReceiversRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        message_id: str = None,
        page_index: int = None,
        page_size: int = None,
    ):
        self.project_id = project_id
        self.message_id = message_id
        self.page_index = page_index
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListMessageReceiversResponseBodyMessageReceiversPagination(TeaModel):
    def __init__(
        self,
        page_index: int = None,
        total_page_count: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.page_index = page_index
        self.total_page_count = total_page_count
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.total_page_count is not None:
            result['TotalPageCount'] = self.total_page_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('TotalPageCount') is not None:
            self.total_page_count = m.get('TotalPageCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListMessageReceiversResponseBodyMessageReceiversList(TeaModel):
    def __init__(
        self,
        type: str = None,
        value: str = None,
        mid: int = None,
    ):
        self.type = type
        self.value = value
        self.mid = mid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        if self.mid is not None:
            result['Mid'] = self.mid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Mid') is not None:
            self.mid = m.get('Mid')
        return self


class ListMessageReceiversResponseBodyMessageReceivers(TeaModel):
    def __init__(
        self,
        pagination: ListMessageReceiversResponseBodyMessageReceiversPagination = None,
        list: List[ListMessageReceiversResponseBodyMessageReceiversList] = None,
    ):
        self.pagination = pagination
        self.list = list

    def validate(self):
        if self.pagination:
            self.pagination.validate()
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.pagination is not None:
            result['Pagination'] = self.pagination.to_map()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pagination') is not None:
            temp_model = ListMessageReceiversResponseBodyMessageReceiversPagination()
            self.pagination = temp_model.from_map(m['Pagination'])
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListMessageReceiversResponseBodyMessageReceiversList()
                self.list.append(temp_model.from_map(k))
        return self


class ListMessageReceiversResponseBody(TeaModel):
    def __init__(
        self,
        message_receivers: ListMessageReceiversResponseBodyMessageReceivers = None,
        request_id: str = None,
    ):
        self.message_receivers = message_receivers
        self.request_id = request_id

    def validate(self):
        if self.message_receivers:
            self.message_receivers.validate()

    def to_map(self):
        result = dict()
        if self.message_receivers is not None:
            result['MessageReceivers'] = self.message_receivers.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MessageReceivers') is not None:
            temp_model = ListMessageReceiversResponseBodyMessageReceivers()
            self.message_receivers = temp_model.from_map(m['MessageReceivers'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListMessageReceiversResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListMessageReceiversResponseBody = None,
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
            temp_model = ListMessageReceiversResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMqttClientSubscriptionsRequest(TeaModel):
    def __init__(
        self,
        app_key: str = None,
        client_id: str = None,
        project_id: str = None,
    ):
        self.app_key = app_key
        self.client_id = client_id
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class ListMqttClientSubscriptionsResponseBodyClientSubscriptionsPagination(TeaModel):
    def __init__(
        self,
        page_index: int = None,
        total_page_count: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.page_index = page_index
        self.total_page_count = total_page_count
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.total_page_count is not None:
            result['TotalPageCount'] = self.total_page_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('TotalPageCount') is not None:
            self.total_page_count = m.get('TotalPageCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListMqttClientSubscriptionsResponseBodyClientSubscriptionsList(TeaModel):
    def __init__(
        self,
        topic: str = None,
        qo_s: int = None,
    ):
        self.topic = topic
        self.qo_s = qo_s

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.qo_s is not None:
            result['QoS'] = self.qo_s
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('QoS') is not None:
            self.qo_s = m.get('QoS')
        return self


class ListMqttClientSubscriptionsResponseBodyClientSubscriptions(TeaModel):
    def __init__(
        self,
        pagination: ListMqttClientSubscriptionsResponseBodyClientSubscriptionsPagination = None,
        list: List[ListMqttClientSubscriptionsResponseBodyClientSubscriptionsList] = None,
    ):
        self.pagination = pagination
        self.list = list

    def validate(self):
        if self.pagination:
            self.pagination.validate()
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.pagination is not None:
            result['Pagination'] = self.pagination.to_map()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pagination') is not None:
            temp_model = ListMqttClientSubscriptionsResponseBodyClientSubscriptionsPagination()
            self.pagination = temp_model.from_map(m['Pagination'])
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListMqttClientSubscriptionsResponseBodyClientSubscriptionsList()
                self.list.append(temp_model.from_map(k))
        return self


class ListMqttClientSubscriptionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        client_subscriptions: ListMqttClientSubscriptionsResponseBodyClientSubscriptions = None,
    ):
        self.request_id = request_id
        self.client_subscriptions = client_subscriptions

    def validate(self):
        if self.client_subscriptions:
            self.client_subscriptions.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.client_subscriptions is not None:
            result['ClientSubscriptions'] = self.client_subscriptions.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ClientSubscriptions') is not None:
            temp_model = ListMqttClientSubscriptionsResponseBodyClientSubscriptions()
            self.client_subscriptions = temp_model.from_map(m['ClientSubscriptions'])
        return self


class ListMqttClientSubscriptionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListMqttClientSubscriptionsResponseBody = None,
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
            temp_model = ListMqttClientSubscriptionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMqttMessageLogsRequest(TeaModel):
    def __init__(
        self,
        app_key: str = None,
        project_id: str = None,
        topic: str = None,
        mid: str = None,
        client_id: str = None,
        start_time: int = None,
        end_time: int = None,
        type: str = None,
    ):
        self.app_key = app_key
        self.project_id = project_id
        self.topic = topic
        self.mid = mid
        self.client_id = client_id
        self.start_time = start_time
        self.end_time = end_time
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.mid is not None:
            result['Mid'] = self.mid
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('Mid') is not None:
            self.mid = m.get('Mid')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListMqttMessageLogsResponseBodyTracesPagination(TeaModel):
    def __init__(
        self,
        page_index: int = None,
        total_page_count: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.page_index = page_index
        self.total_page_count = total_page_count
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.total_page_count is not None:
            result['TotalPageCount'] = self.total_page_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('TotalPageCount') is not None:
            self.total_page_count = m.get('TotalPageCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListMqttMessageLogsResponseBodyTracesList(TeaModel):
    def __init__(
        self,
        type: str = None,
        time: int = None,
        action: str = None,
        topic: str = None,
        mid: str = None,
        client_mid: str = None,
        client_id: str = None,
    ):
        self.type = type
        self.time = time
        self.action = action
        self.topic = topic
        self.mid = mid
        self.client_mid = client_mid
        self.client_id = client_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.time is not None:
            result['Time'] = self.time
        if self.action is not None:
            result['Action'] = self.action
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.mid is not None:
            result['Mid'] = self.mid
        if self.client_mid is not None:
            result['ClientMid'] = self.client_mid
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('Mid') is not None:
            self.mid = m.get('Mid')
        if m.get('ClientMid') is not None:
            self.client_mid = m.get('ClientMid')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        return self


class ListMqttMessageLogsResponseBodyTraces(TeaModel):
    def __init__(
        self,
        pagination: ListMqttMessageLogsResponseBodyTracesPagination = None,
        list: List[ListMqttMessageLogsResponseBodyTracesList] = None,
    ):
        self.pagination = pagination
        self.list = list

    def validate(self):
        if self.pagination:
            self.pagination.validate()
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.pagination is not None:
            result['Pagination'] = self.pagination.to_map()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pagination') is not None:
            temp_model = ListMqttMessageLogsResponseBodyTracesPagination()
            self.pagination = temp_model.from_map(m['Pagination'])
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListMqttMessageLogsResponseBodyTracesList()
                self.list.append(temp_model.from_map(k))
        return self


class ListMqttMessageLogsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        traces: ListMqttMessageLogsResponseBodyTraces = None,
    ):
        self.request_id = request_id
        self.traces = traces

    def validate(self):
        if self.traces:
            self.traces.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.traces is not None:
            result['Traces'] = self.traces.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Traces') is not None:
            temp_model = ListMqttMessageLogsResponseBodyTraces()
            self.traces = temp_model.from_map(m['Traces'])
        return self


class ListMqttMessageLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListMqttMessageLogsResponseBody = None,
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
            temp_model = ListMqttMessageLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMqttRootTopicsRequest(TeaModel):
    def __init__(
        self,
        app_key: str = None,
        project_id: str = None,
    ):
        self.app_key = app_key
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class ListMqttRootTopicsResponseBodyRootTopicsPagination(TeaModel):
    def __init__(
        self,
        page_index: int = None,
        total_page_count: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.page_index = page_index
        self.total_page_count = total_page_count
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.total_page_count is not None:
            result['TotalPageCount'] = self.total_page_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('TotalPageCount') is not None:
            self.total_page_count = m.get('TotalPageCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListMqttRootTopicsResponseBodyRootTopicsList(TeaModel):
    def __init__(
        self,
        type: str = None,
        app_key: str = None,
        queue_name: str = None,
        create_time: int = None,
        root_topic: str = None,
    ):
        self.type = type
        self.app_key = app_key
        self.queue_name = queue_name
        self.create_time = create_time
        self.root_topic = root_topic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.root_topic is not None:
            result['RootTopic'] = self.root_topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('RootTopic') is not None:
            self.root_topic = m.get('RootTopic')
        return self


class ListMqttRootTopicsResponseBodyRootTopics(TeaModel):
    def __init__(
        self,
        pagination: ListMqttRootTopicsResponseBodyRootTopicsPagination = None,
        list: List[ListMqttRootTopicsResponseBodyRootTopicsList] = None,
    ):
        self.pagination = pagination
        self.list = list

    def validate(self):
        if self.pagination:
            self.pagination.validate()
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.pagination is not None:
            result['Pagination'] = self.pagination.to_map()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pagination') is not None:
            temp_model = ListMqttRootTopicsResponseBodyRootTopicsPagination()
            self.pagination = temp_model.from_map(m['Pagination'])
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListMqttRootTopicsResponseBodyRootTopicsList()
                self.list.append(temp_model.from_map(k))
        return self


class ListMqttRootTopicsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        root_topics: ListMqttRootTopicsResponseBodyRootTopics = None,
    ):
        self.request_id = request_id
        self.root_topics = root_topics

    def validate(self):
        if self.root_topics:
            self.root_topics.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.root_topics is not None:
            result['RootTopics'] = self.root_topics.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RootTopics') is not None:
            temp_model = ListMqttRootTopicsResponseBodyRootTopics()
            self.root_topics = temp_model.from_map(m['RootTopics'])
        return self


class ListMqttRootTopicsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListMqttRootTopicsResponseBody = None,
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
            temp_model = ListMqttRootTopicsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNamespacesRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        auth_type: str = None,
    ):
        self.project_id = project_id
        self.auth_type = auth_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')
        return self


class ListNamespacesResponseBodyNamespaces(TeaModel):
    def __init__(
        self,
        auth_type: int = None,
        description: str = None,
        user_id: str = None,
        project_id: str = None,
        gmt_create: int = None,
        namespace: str = None,
        gmt_modified: int = None,
        name: str = None,
    ):
        self.auth_type = auth_type
        self.description = description
        self.user_id = user_id
        self.project_id = project_id
        self.gmt_create = gmt_create
        self.namespace = namespace
        self.gmt_modified = gmt_modified
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type
        if self.description is not None:
            result['Description'] = self.description
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListNamespacesResponseBody(TeaModel):
    def __init__(
        self,
        namespaces: List[ListNamespacesResponseBodyNamespaces] = None,
        request_id: str = None,
    ):
        self.namespaces = namespaces
        self.request_id = request_id

    def validate(self):
        if self.namespaces:
            for k in self.namespaces:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Namespaces'] = []
        if self.namespaces is not None:
            for k in self.namespaces:
                result['Namespaces'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.namespaces = []
        if m.get('Namespaces') is not None:
            for k in m.get('Namespaces'):
                temp_model = ListNamespacesResponseBodyNamespaces()
                self.namespaces.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListNamespacesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListNamespacesResponseBody = None,
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
            temp_model = ListNamespacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOfflineMessagesRequest(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        project_id: str = None,
        type: str = None,
        value: str = None,
        page_index: int = None,
    ):
        self.page_size = page_size
        self.project_id = project_id
        self.type = type
        self.value = value
        self.page_index = page_index

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        return self


class ListOfflineMessagesResponseBodyOfflineMessagesPagination(TeaModel):
    def __init__(
        self,
        page_index: int = None,
        total_page_count: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.page_index = page_index
        self.total_page_count = total_page_count
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.total_page_count is not None:
            result['TotalPageCount'] = self.total_page_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('TotalPageCount') is not None:
            self.total_page_count = m.get('TotalPageCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListOfflineMessagesResponseBodyOfflineMessagesList(TeaModel):
    def __init__(
        self,
        expired_time: int = None,
        mid: int = None,
        gmt_create: int = None,
    ):
        self.expired_time = expired_time
        self.mid = mid
        self.gmt_create = gmt_create

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.mid is not None:
            result['Mid'] = self.mid
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('Mid') is not None:
            self.mid = m.get('Mid')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        return self


class ListOfflineMessagesResponseBodyOfflineMessages(TeaModel):
    def __init__(
        self,
        pagination: ListOfflineMessagesResponseBodyOfflineMessagesPagination = None,
        list: List[ListOfflineMessagesResponseBodyOfflineMessagesList] = None,
    ):
        self.pagination = pagination
        self.list = list

    def validate(self):
        if self.pagination:
            self.pagination.validate()
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.pagination is not None:
            result['Pagination'] = self.pagination.to_map()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pagination') is not None:
            temp_model = ListOfflineMessagesResponseBodyOfflineMessagesPagination()
            self.pagination = temp_model.from_map(m['Pagination'])
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListOfflineMessagesResponseBodyOfflineMessagesList()
                self.list.append(temp_model.from_map(k))
        return self


class ListOfflineMessagesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        offline_messages: ListOfflineMessagesResponseBodyOfflineMessages = None,
    ):
        self.request_id = request_id
        self.offline_messages = offline_messages

    def validate(self):
        if self.offline_messages:
            self.offline_messages.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.offline_messages is not None:
            result['OfflineMessages'] = self.offline_messages.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OfflineMessages') is not None:
            temp_model = ListOfflineMessagesResponseBodyOfflineMessages()
            self.offline_messages = temp_model.from_map(m['OfflineMessages'])
        return self


class ListOfflineMessagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListOfflineMessagesResponseBody = None,
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
            temp_model = ListOfflineMessagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOpenAccountLinksRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        identity_id: str = None,
        idp: str = None,
        open_id: str = None,
    ):
        self.project_id = project_id
        self.identity_id = identity_id
        self.idp = idp
        self.open_id = open_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.identity_id is not None:
            result['IdentityId'] = self.identity_id
        if self.idp is not None:
            result['Idp'] = self.idp
        if self.open_id is not None:
            result['OpenId'] = self.open_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('IdentityId') is not None:
            self.identity_id = m.get('IdentityId')
        if m.get('Idp') is not None:
            self.idp = m.get('Idp')
        if m.get('OpenId') is not None:
            self.open_id = m.get('OpenId')
        return self


class ListOpenAccountLinksResponseBodyOpenAccounts(TeaModel):
    def __init__(
        self,
        status: int = None,
        type: int = None,
        display_name: str = None,
        create_access_key: str = None,
        open_id: str = None,
        mobile: str = None,
        region: str = None,
        identity_id: str = None,
        login_id: str = None,
        idp: str = None,
        aliyun_id: str = None,
    ):
        self.status = status
        self.type = type
        self.display_name = display_name
        self.create_access_key = create_access_key
        self.open_id = open_id
        self.mobile = mobile
        self.region = region
        self.identity_id = identity_id
        self.login_id = login_id
        self.idp = idp
        self.aliyun_id = aliyun_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.create_access_key is not None:
            result['CreateAccessKey'] = self.create_access_key
        if self.open_id is not None:
            result['OpenId'] = self.open_id
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.region is not None:
            result['Region'] = self.region
        if self.identity_id is not None:
            result['IdentityId'] = self.identity_id
        if self.login_id is not None:
            result['LoginId'] = self.login_id
        if self.idp is not None:
            result['Idp'] = self.idp
        if self.aliyun_id is not None:
            result['AliyunId'] = self.aliyun_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('CreateAccessKey') is not None:
            self.create_access_key = m.get('CreateAccessKey')
        if m.get('OpenId') is not None:
            self.open_id = m.get('OpenId')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('IdentityId') is not None:
            self.identity_id = m.get('IdentityId')
        if m.get('LoginId') is not None:
            self.login_id = m.get('LoginId')
        if m.get('Idp') is not None:
            self.idp = m.get('Idp')
        if m.get('AliyunId') is not None:
            self.aliyun_id = m.get('AliyunId')
        return self


class ListOpenAccountLinksResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        open_accounts: List[ListOpenAccountLinksResponseBodyOpenAccounts] = None,
    ):
        self.request_id = request_id
        self.open_accounts = open_accounts

    def validate(self):
        if self.open_accounts:
            for k in self.open_accounts:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['OpenAccounts'] = []
        if self.open_accounts is not None:
            for k in self.open_accounts:
                result['OpenAccounts'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.open_accounts = []
        if m.get('OpenAccounts') is not None:
            for k in m.get('OpenAccounts'):
                temp_model = ListOpenAccountLinksResponseBodyOpenAccounts()
                self.open_accounts.append(temp_model.from_map(k))
        return self


class ListOpenAccountLinksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListOpenAccountLinksResponseBody = None,
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
            temp_model = ListOpenAccountLinksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOpenAccountsRequest(TeaModel):
    def __init__(
        self,
        length: int = None,
        start: int = None,
        mobile: str = None,
        email: str = None,
        display_name: str = None,
        project_id: str = None,
    ):
        self.length = length
        self.start = start
        self.mobile = mobile
        self.email = email
        self.display_name = display_name
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.length is not None:
            result['Length'] = self.length
        if self.start is not None:
            result['Start'] = self.start
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.email is not None:
            result['Email'] = self.email
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Length') is not None:
            self.length = m.get('Length')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class ListOpenAccountsResponseBodyOpenAccounts(TeaModel):
    def __init__(
        self,
        status: int = None,
        type: int = None,
        display_name: str = None,
        create_access_key: str = None,
        open_id: str = None,
        mobile: str = None,
        region: str = None,
        identity_id: str = None,
        login_id: str = None,
        idp: str = None,
        aliyun_id: str = None,
    ):
        self.status = status
        self.type = type
        self.display_name = display_name
        self.create_access_key = create_access_key
        self.open_id = open_id
        self.mobile = mobile
        self.region = region
        self.identity_id = identity_id
        self.login_id = login_id
        self.idp = idp
        self.aliyun_id = aliyun_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.create_access_key is not None:
            result['CreateAccessKey'] = self.create_access_key
        if self.open_id is not None:
            result['OpenId'] = self.open_id
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.region is not None:
            result['Region'] = self.region
        if self.identity_id is not None:
            result['IdentityId'] = self.identity_id
        if self.login_id is not None:
            result['LoginId'] = self.login_id
        if self.idp is not None:
            result['Idp'] = self.idp
        if self.aliyun_id is not None:
            result['AliyunId'] = self.aliyun_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('CreateAccessKey') is not None:
            self.create_access_key = m.get('CreateAccessKey')
        if m.get('OpenId') is not None:
            self.open_id = m.get('OpenId')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('IdentityId') is not None:
            self.identity_id = m.get('IdentityId')
        if m.get('LoginId') is not None:
            self.login_id = m.get('LoginId')
        if m.get('Idp') is not None:
            self.idp = m.get('Idp')
        if m.get('AliyunId') is not None:
            self.aliyun_id = m.get('AliyunId')
        return self


class ListOpenAccountsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        open_accounts: List[ListOpenAccountsResponseBodyOpenAccounts] = None,
    ):
        self.request_id = request_id
        self.open_accounts = open_accounts

    def validate(self):
        if self.open_accounts:
            for k in self.open_accounts:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['OpenAccounts'] = []
        if self.open_accounts is not None:
            for k in self.open_accounts:
                result['OpenAccounts'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.open_accounts = []
        if m.get('OpenAccounts') is not None:
            for k in m.get('OpenAccounts'):
                temp_model = ListOpenAccountsResponseBodyOpenAccounts()
                self.open_accounts.append(temp_model.from_map(k))
        return self


class ListOpenAccountsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListOpenAccountsResponseBody = None,
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
            temp_model = ListOpenAccountsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPreChecksResponseBodyPreChecks(TeaModel):
    def __init__(
        self,
        key: str = None,
        link: str = None,
        price: str = None,
        state: str = None,
    ):
        self.key = key
        self.link = link
        self.price = price
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.link is not None:
            result['Link'] = self.link
        if self.price is not None:
            result['Price'] = self.price
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Link') is not None:
            self.link = m.get('Link')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class ListPreChecksResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        pre_checks: List[ListPreChecksResponseBodyPreChecks] = None,
    ):
        self.request_id = request_id
        self.pre_checks = pre_checks

    def validate(self):
        if self.pre_checks:
            for k in self.pre_checks:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['PreChecks'] = []
        if self.pre_checks is not None:
            for k in self.pre_checks:
                result['PreChecks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.pre_checks = []
        if m.get('PreChecks') is not None:
            for k in m.get('PreChecks'):
                temp_model = ListPreChecksResponseBodyPreChecks()
                self.pre_checks.append(temp_model.from_map(k))
        return self


class ListPreChecksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListPreChecksResponseBody = None,
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
            temp_model = ListPreChecksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProjectAppsRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        page_index: int = None,
        page_size: int = None,
        keywords: str = None,
    ):
        self.project_id = project_id
        self.page_index = page_index
        self.page_size = page_size
        self.keywords = keywords

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.keywords is not None:
            result['Keywords'] = self.keywords
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')
        return self


class ListProjectAppsResponseBodyResultProjectApps(TeaModel):
    def __init__(
        self,
        status: int = None,
        project_id: str = None,
        user_id: str = None,
        gmt_modified: int = None,
        app_pkg_name: str = None,
        app_name: str = None,
        app_secret: str = None,
        app_key: str = None,
        app_id: str = None,
        os_type: int = None,
        gmt_create: int = None,
        id: int = None,
    ):
        self.status = status
        self.project_id = project_id
        self.user_id = user_id
        self.gmt_modified = gmt_modified
        self.app_pkg_name = app_pkg_name
        self.app_name = app_name
        self.app_secret = app_secret
        self.app_key = app_key
        self.app_id = app_id
        self.os_type = os_type
        self.gmt_create = gmt_create
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.app_pkg_name is not None:
            result['AppPkgName'] = self.app_pkg_name
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_secret is not None:
            result['AppSecret'] = self.app_secret
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('AppPkgName') is not None:
            self.app_pkg_name = m.get('AppPkgName')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppSecret') is not None:
            self.app_secret = m.get('AppSecret')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListProjectAppsResponseBodyResult(TeaModel):
    def __init__(
        self,
        project_apps: List[ListProjectAppsResponseBodyResultProjectApps] = None,
        total_page: int = None,
        total_count: int = None,
    ):
        self.project_apps = project_apps
        self.total_page = total_page
        self.total_count = total_count

    def validate(self):
        if self.project_apps:
            for k in self.project_apps:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ProjectApps'] = []
        if self.project_apps is not None:
            for k in self.project_apps:
                result['ProjectApps'].append(k.to_map() if k else None)
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.project_apps = []
        if m.get('ProjectApps') is not None:
            for k in m.get('ProjectApps'):
                temp_model = ListProjectAppsResponseBodyResultProjectApps()
                self.project_apps.append(temp_model.from_map(k))
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListProjectAppsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: ListProjectAppsResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ListProjectAppsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListProjectAppsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListProjectAppsResponseBody = None,
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
            temp_model = ListProjectAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProjectsResponseBodyProjects(TeaModel):
    def __init__(
        self,
        status: int = None,
        description: str = None,
        user_id: str = None,
        project_id: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        name: str = None,
        id: int = None,
        creator: str = None,
    ):
        self.status = status
        self.description = description
        self.user_id = user_id
        self.project_id = project_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.name = name
        self.id = id
        self.creator = creator

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.description is not None:
            result['Description'] = self.description
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        if self.creator is not None:
            result['Creator'] = self.creator
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        return self


class ListProjectsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        projects: List[ListProjectsResponseBodyProjects] = None,
    ):
        self.request_id = request_id
        self.projects = projects

    def validate(self):
        if self.projects:
            for k in self.projects:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Projects'] = []
        if self.projects is not None:
            for k in self.projects:
                result['Projects'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.projects = []
        if m.get('Projects') is not None:
            for k in m.get('Projects'):
                temp_model = ListProjectsResponseBodyProjects()
                self.projects.append(temp_model.from_map(k))
        return self


class ListProjectsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListProjectsResponseBody = None,
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
            temp_model = ListProjectsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRpcServicesRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        page_index: int = None,
        page_size: int = None,
    ):
        self.project_id = project_id
        self.page_index = page_index
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListRpcServicesResponseBodyRpcServicesPagination(TeaModel):
    def __init__(
        self,
        page_index: int = None,
        total_page_count: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.page_index = page_index
        self.total_page_count = total_page_count
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.total_page_count is not None:
            result['TotalPageCount'] = self.total_page_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('TotalPageCount') is not None:
            self.total_page_count = m.get('TotalPageCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListRpcServicesResponseBodyRpcServicesList(TeaModel):
    def __init__(
        self,
        method_name: str = None,
        type: str = None,
        interface_name: str = None,
        params: str = None,
        app_key: str = None,
        group_name: str = None,
        gmt_create: int = None,
        is_delete: str = None,
        version_code: str = None,
        gmt_modified: int = None,
        id: int = None,
    ):
        self.method_name = method_name
        self.type = type
        self.interface_name = interface_name
        self.params = params
        self.app_key = app_key
        self.group_name = group_name
        self.gmt_create = gmt_create
        self.is_delete = is_delete
        self.version_code = version_code
        self.gmt_modified = gmt_modified
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.method_name is not None:
            result['MethodName'] = self.method_name
        if self.type is not None:
            result['Type'] = self.type
        if self.interface_name is not None:
            result['InterfaceName'] = self.interface_name
        if self.params is not None:
            result['Params'] = self.params
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.is_delete is not None:
            result['IsDelete'] = self.is_delete
        if self.version_code is not None:
            result['VersionCode'] = self.version_code
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MethodName') is not None:
            self.method_name = m.get('MethodName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('InterfaceName') is not None:
            self.interface_name = m.get('InterfaceName')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('IsDelete') is not None:
            self.is_delete = m.get('IsDelete')
        if m.get('VersionCode') is not None:
            self.version_code = m.get('VersionCode')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListRpcServicesResponseBodyRpcServices(TeaModel):
    def __init__(
        self,
        pagination: ListRpcServicesResponseBodyRpcServicesPagination = None,
        list: List[ListRpcServicesResponseBodyRpcServicesList] = None,
    ):
        self.pagination = pagination
        self.list = list

    def validate(self):
        if self.pagination:
            self.pagination.validate()
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.pagination is not None:
            result['Pagination'] = self.pagination.to_map()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pagination') is not None:
            temp_model = ListRpcServicesResponseBodyRpcServicesPagination()
            self.pagination = temp_model.from_map(m['Pagination'])
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListRpcServicesResponseBodyRpcServicesList()
                self.list.append(temp_model.from_map(k))
        return self


class ListRpcServicesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        rpc_services: ListRpcServicesResponseBodyRpcServices = None,
    ):
        self.request_id = request_id
        self.rpc_services = rpc_services

    def validate(self):
        if self.rpc_services:
            self.rpc_services.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rpc_services is not None:
            result['RpcServices'] = self.rpc_services.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RpcServices') is not None:
            temp_model = ListRpcServicesResponseBodyRpcServices()
            self.rpc_services = temp_model.from_map(m['RpcServices'])
        return self


class ListRpcServicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListRpcServicesResponseBody = None,
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
            temp_model = ListRpcServicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSchemaSubscribesRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        device_model: str = None,
        page_index: int = None,
        page_size: int = None,
    ):
        self.project_id = project_id
        self.device_model = device_model
        self.page_index = page_index
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.device_model is not None:
            result['DeviceModel'] = self.device_model
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('DeviceModel') is not None:
            self.device_model = m.get('DeviceModel')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListSchemaSubscribesResponseBodyPageListPagination(TeaModel):
    def __init__(
        self,
        page_index: int = None,
        total_page_count: int = None,
        page_size: int = None,
        total_count: int = None,
        simple_sign: bool = None,
        has_next_page: bool = None,
    ):
        self.page_index = page_index
        self.total_page_count = total_page_count
        self.page_size = page_size
        self.total_count = total_count
        self.simple_sign = simple_sign
        self.has_next_page = has_next_page

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.total_page_count is not None:
            result['TotalPageCount'] = self.total_page_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.simple_sign is not None:
            result['SimpleSign'] = self.simple_sign
        if self.has_next_page is not None:
            result['HasNextPage'] = self.has_next_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('TotalPageCount') is not None:
            self.total_page_count = m.get('TotalPageCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('SimpleSign') is not None:
            self.simple_sign = m.get('SimpleSign')
        if m.get('HasNextPage') is not None:
            self.has_next_page = m.get('HasNextPage')
        return self


class ListSchemaSubscribesResponseBodyPageListList(TeaModel):
    def __init__(
        self,
        device_model_id: int = None,
        version: str = None,
        project_id: str = None,
        gmt_create: int = None,
        namespace: str = None,
        validity_schema: str = None,
        device_model: str = None,
        gmt_modified: int = None,
        id: int = None,
    ):
        self.device_model_id = device_model_id
        self.version = version
        self.project_id = project_id
        self.gmt_create = gmt_create
        self.namespace = namespace
        self.validity_schema = validity_schema
        self.device_model = device_model
        self.gmt_modified = gmt_modified
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.device_model_id is not None:
            result['DeviceModelId'] = self.device_model_id
        if self.version is not None:
            result['Version'] = self.version
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.validity_schema is not None:
            result['ValiditySchema'] = self.validity_schema
        if self.device_model is not None:
            result['DeviceModel'] = self.device_model
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceModelId') is not None:
            self.device_model_id = m.get('DeviceModelId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('ValiditySchema') is not None:
            self.validity_schema = m.get('ValiditySchema')
        if m.get('DeviceModel') is not None:
            self.device_model = m.get('DeviceModel')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListSchemaSubscribesResponseBodyPageList(TeaModel):
    def __init__(
        self,
        pagination: ListSchemaSubscribesResponseBodyPageListPagination = None,
        list: List[ListSchemaSubscribesResponseBodyPageListList] = None,
    ):
        self.pagination = pagination
        self.list = list

    def validate(self):
        if self.pagination:
            self.pagination.validate()
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.pagination is not None:
            result['Pagination'] = self.pagination.to_map()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pagination') is not None:
            temp_model = ListSchemaSubscribesResponseBodyPageListPagination()
            self.pagination = temp_model.from_map(m['Pagination'])
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListSchemaSubscribesResponseBodyPageListList()
                self.list.append(temp_model.from_map(k))
        return self


class ListSchemaSubscribesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        page_list: List[ListSchemaSubscribesResponseBodyPageList] = None,
    ):
        self.request_id = request_id
        self.page_list = page_list

    def validate(self):
        if self.page_list:
            for k in self.page_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['PageList'] = []
        if self.page_list is not None:
            for k in self.page_list:
                result['PageList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.page_list = []
        if m.get('PageList') is not None:
            for k in m.get('PageList'):
                temp_model = ListSchemaSubscribesResponseBodyPageList()
                self.page_list.append(temp_model.from_map(k))
        return self


class ListSchemaSubscribesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSchemaSubscribesResponseBody = None,
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
            temp_model = ListSchemaSubscribesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServicesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        service_list: List[str] = None,
    ):
        self.request_id = request_id
        self.service_list = service_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_list is not None:
            result['ServiceList'] = self.service_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceList') is not None:
            self.service_list = m.get('ServiceList')
        return self


class ListServicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListServicesResponseBody = None,
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
            temp_model = ListServicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListShadowSchemaDeviceModelsRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
    ):
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class ListShadowSchemaDeviceModelsResponseBodyModelList(TeaModel):
    def __init__(
        self,
        device_model_id: int = None,
        hardware_type: str = None,
        device_type: str = None,
        can_create_device_id: int = None,
        project_id: str = None,
        os_platform: str = None,
        device_model: str = None,
        security_chip: int = None,
        description: str = None,
        init_usage_type_desc: str = None,
        init_usage_type: int = None,
        device_brand: str = None,
    ):
        self.device_model_id = device_model_id
        self.hardware_type = hardware_type
        self.device_type = device_type
        self.can_create_device_id = can_create_device_id
        self.project_id = project_id
        self.os_platform = os_platform
        self.device_model = device_model
        self.security_chip = security_chip
        self.description = description
        self.init_usage_type_desc = init_usage_type_desc
        self.init_usage_type = init_usage_type
        self.device_brand = device_brand

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.device_model_id is not None:
            result['DeviceModelId'] = self.device_model_id
        if self.hardware_type is not None:
            result['HardwareType'] = self.hardware_type
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.can_create_device_id is not None:
            result['CanCreateDeviceId'] = self.can_create_device_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.os_platform is not None:
            result['OsPlatform'] = self.os_platform
        if self.device_model is not None:
            result['DeviceModel'] = self.device_model
        if self.security_chip is not None:
            result['SecurityChip'] = self.security_chip
        if self.description is not None:
            result['Description'] = self.description
        if self.init_usage_type_desc is not None:
            result['InitUsageTypeDesc'] = self.init_usage_type_desc
        if self.init_usage_type is not None:
            result['InitUsageType'] = self.init_usage_type
        if self.device_brand is not None:
            result['DeviceBrand'] = self.device_brand
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceModelId') is not None:
            self.device_model_id = m.get('DeviceModelId')
        if m.get('HardwareType') is not None:
            self.hardware_type = m.get('HardwareType')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('CanCreateDeviceId') is not None:
            self.can_create_device_id = m.get('CanCreateDeviceId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('OsPlatform') is not None:
            self.os_platform = m.get('OsPlatform')
        if m.get('DeviceModel') is not None:
            self.device_model = m.get('DeviceModel')
        if m.get('SecurityChip') is not None:
            self.security_chip = m.get('SecurityChip')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InitUsageTypeDesc') is not None:
            self.init_usage_type_desc = m.get('InitUsageTypeDesc')
        if m.get('InitUsageType') is not None:
            self.init_usage_type = m.get('InitUsageType')
        if m.get('DeviceBrand') is not None:
            self.device_brand = m.get('DeviceBrand')
        return self


class ListShadowSchemaDeviceModelsResponseBody(TeaModel):
    def __init__(
        self,
        model_list: List[ListShadowSchemaDeviceModelsResponseBodyModelList] = None,
        request_id: str = None,
    ):
        self.model_list = model_list
        self.request_id = request_id

    def validate(self):
        if self.model_list:
            for k in self.model_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ModelList'] = []
        if self.model_list is not None:
            for k in self.model_list:
                result['ModelList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.model_list = []
        if m.get('ModelList') is not None:
            for k in m.get('ModelList'):
                temp_model = ListShadowSchemaDeviceModelsResponseBodyModelList()
                self.model_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListShadowSchemaDeviceModelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListShadowSchemaDeviceModelsResponseBody = None,
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
            temp_model = ListShadowSchemaDeviceModelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListShadowSchemasRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        query_type: str = None,
        query_value: str = None,
        page_index: int = None,
        page_size: int = None,
    ):
        self.project_id = project_id
        self.query_type = query_type
        self.query_value = query_value
        self.page_index = page_index
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.query_type is not None:
            result['QueryType'] = self.query_type
        if self.query_value is not None:
            result['QueryValue'] = self.query_value
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')
        if m.get('QueryValue') is not None:
            self.query_value = m.get('QueryValue')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListShadowSchemasResponseBodyPageListPagination(TeaModel):
    def __init__(
        self,
        page_index: int = None,
        total_page_count: int = None,
        page_size: int = None,
        total_count: int = None,
        simple_sign: bool = None,
        has_next_page: bool = None,
    ):
        self.page_index = page_index
        self.total_page_count = total_page_count
        self.page_size = page_size
        self.total_count = total_count
        self.simple_sign = simple_sign
        self.has_next_page = has_next_page

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.total_page_count is not None:
            result['TotalPageCount'] = self.total_page_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.simple_sign is not None:
            result['SimpleSign'] = self.simple_sign
        if self.has_next_page is not None:
            result['HasNextPage'] = self.has_next_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('TotalPageCount') is not None:
            self.total_page_count = m.get('TotalPageCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('SimpleSign') is not None:
            self.simple_sign = m.get('SimpleSign')
        if m.get('HasNextPage') is not None:
            self.has_next_page = m.get('HasNextPage')
        return self


class ListShadowSchemasResponseBodyPageListList(TeaModel):
    def __init__(
        self,
        auth_type_desc: str = None,
        device_model_id: int = None,
        auth_type: int = None,
        project_id: str = None,
        gmt_create: int = None,
        namespace: str = None,
        device_model: str = None,
        gmt_modified: int = None,
        module_schema: str = None,
        id: int = None,
    ):
        self.auth_type_desc = auth_type_desc
        self.device_model_id = device_model_id
        self.auth_type = auth_type
        self.project_id = project_id
        self.gmt_create = gmt_create
        self.namespace = namespace
        self.device_model = device_model
        self.gmt_modified = gmt_modified
        self.module_schema = module_schema
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.auth_type_desc is not None:
            result['AuthTypeDesc'] = self.auth_type_desc
        if self.device_model_id is not None:
            result['DeviceModelId'] = self.device_model_id
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.device_model is not None:
            result['DeviceModel'] = self.device_model
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.module_schema is not None:
            result['ModuleSchema'] = self.module_schema
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthTypeDesc') is not None:
            self.auth_type_desc = m.get('AuthTypeDesc')
        if m.get('DeviceModelId') is not None:
            self.device_model_id = m.get('DeviceModelId')
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('DeviceModel') is not None:
            self.device_model = m.get('DeviceModel')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('ModuleSchema') is not None:
            self.module_schema = m.get('ModuleSchema')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListShadowSchemasResponseBodyPageList(TeaModel):
    def __init__(
        self,
        pagination: ListShadowSchemasResponseBodyPageListPagination = None,
        list: List[ListShadowSchemasResponseBodyPageListList] = None,
    ):
        self.pagination = pagination
        self.list = list

    def validate(self):
        if self.pagination:
            self.pagination.validate()
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.pagination is not None:
            result['Pagination'] = self.pagination.to_map()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pagination') is not None:
            temp_model = ListShadowSchemasResponseBodyPageListPagination()
            self.pagination = temp_model.from_map(m['Pagination'])
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListShadowSchemasResponseBodyPageListList()
                self.list.append(temp_model.from_map(k))
        return self


class ListShadowSchemasResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        page_list: ListShadowSchemasResponseBodyPageList = None,
    ):
        self.request_id = request_id
        self.page_list = page_list

    def validate(self):
        if self.page_list:
            self.page_list.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_list is not None:
            result['PageList'] = self.page_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageList') is not None:
            temp_model = ListShadowSchemasResponseBodyPageList()
            self.page_list = temp_model.from_map(m['PageList'])
        return self


class ListShadowSchemasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListShadowSchemasResponseBody = None,
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
            temp_model = ListShadowSchemasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSupportFeaturesResponseBodySupportFeatures(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListSupportFeaturesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        support_features: List[ListSupportFeaturesResponseBodySupportFeatures] = None,
    ):
        self.request_id = request_id
        self.support_features = support_features

    def validate(self):
        if self.support_features:
            for k in self.support_features:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SupportFeatures'] = []
        if self.support_features is not None:
            for k in self.support_features:
                result['SupportFeatures'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.support_features = []
        if m.get('SupportFeatures') is not None:
            for k in m.get('SupportFeatures'):
                temp_model = ListSupportFeaturesResponseBodySupportFeatures()
                self.support_features.append(temp_model.from_map(k))
        return self


class ListSupportFeaturesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSupportFeaturesResponseBody = None,
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
            temp_model = ListSupportFeaturesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTriggersRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        namespace: str = None,
        page_index: int = None,
        page_size: int = None,
    ):
        self.project_id = project_id
        self.namespace = namespace
        self.page_index = page_index
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListTriggersResponseBodyTriggerListPagination(TeaModel):
    def __init__(
        self,
        page_index: int = None,
        total_page_count: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.page_index = page_index
        self.total_page_count = total_page_count
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.total_page_count is not None:
            result['TotalPageCount'] = self.total_page_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('TotalPageCount') is not None:
            self.total_page_count = m.get('TotalPageCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTriggersResponseBodyTriggerListTriggersFunctions(TeaModel):
    def __init__(
        self,
        gmt_create: int = None,
        file_name: str = None,
        name: str = None,
        gmt_modified: int = None,
        id: int = None,
        file_id: int = None,
    ):
        self.gmt_create = gmt_create
        self.file_name = file_name
        self.name = name
        self.gmt_modified = gmt_modified
        self.id = id
        self.file_id = file_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.name is not None:
            result['Name'] = self.name
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.file_id is not None:
            result['FileId'] = self.file_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        return self


class ListTriggersResponseBodyTriggerListTriggers(TeaModel):
    def __init__(
        self,
        status: int = None,
        type: int = None,
        production: int = None,
        functions: List[ListTriggersResponseBodyTriggerListTriggersFunctions] = None,
        sandbox: int = None,
        namespace: str = None,
        gmt_modified: int = None,
        source: str = None,
        chained_function_ids: str = None,
        gmt_create: int = None,
        invocation_mode: int = None,
        id: int = None,
    ):
        self.status = status
        self.type = type
        self.production = production
        self.functions = functions
        self.sandbox = sandbox
        self.namespace = namespace
        self.gmt_modified = gmt_modified
        self.source = source
        self.chained_function_ids = chained_function_ids
        self.gmt_create = gmt_create
        self.invocation_mode = invocation_mode
        self.id = id

    def validate(self):
        if self.functions:
            for k in self.functions:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.production is not None:
            result['Production'] = self.production
        result['Functions'] = []
        if self.functions is not None:
            for k in self.functions:
                result['Functions'].append(k.to_map() if k else None)
        if self.sandbox is not None:
            result['Sandbox'] = self.sandbox
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.source is not None:
            result['Source'] = self.source
        if self.chained_function_ids is not None:
            result['ChainedFunctionIds'] = self.chained_function_ids
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.invocation_mode is not None:
            result['InvocationMode'] = self.invocation_mode
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Production') is not None:
            self.production = m.get('Production')
        self.functions = []
        if m.get('Functions') is not None:
            for k in m.get('Functions'):
                temp_model = ListTriggersResponseBodyTriggerListTriggersFunctions()
                self.functions.append(temp_model.from_map(k))
        if m.get('Sandbox') is not None:
            self.sandbox = m.get('Sandbox')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('ChainedFunctionIds') is not None:
            self.chained_function_ids = m.get('ChainedFunctionIds')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('InvocationMode') is not None:
            self.invocation_mode = m.get('InvocationMode')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListTriggersResponseBodyTriggerList(TeaModel):
    def __init__(
        self,
        pagination: ListTriggersResponseBodyTriggerListPagination = None,
        triggers: List[ListTriggersResponseBodyTriggerListTriggers] = None,
    ):
        self.pagination = pagination
        self.triggers = triggers

    def validate(self):
        if self.pagination:
            self.pagination.validate()
        if self.triggers:
            for k in self.triggers:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.pagination is not None:
            result['Pagination'] = self.pagination.to_map()
        result['Triggers'] = []
        if self.triggers is not None:
            for k in self.triggers:
                result['Triggers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pagination') is not None:
            temp_model = ListTriggersResponseBodyTriggerListPagination()
            self.pagination = temp_model.from_map(m['Pagination'])
        self.triggers = []
        if m.get('Triggers') is not None:
            for k in m.get('Triggers'):
                temp_model = ListTriggersResponseBodyTriggerListTriggers()
                self.triggers.append(temp_model.from_map(k))
        return self


class ListTriggersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        trigger_list: ListTriggersResponseBodyTriggerList = None,
    ):
        self.request_id = request_id
        self.trigger_list = trigger_list

    def validate(self):
        if self.trigger_list:
            self.trigger_list.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.trigger_list is not None:
            result['TriggerList'] = self.trigger_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TriggerList') is not None:
            temp_model = ListTriggersResponseBodyTriggerList()
            self.trigger_list = temp_model.from_map(m['TriggerList'])
        return self


class ListTriggersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTriggersResponseBody = None,
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
            temp_model = ListTriggersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUpstreamAppKeyRelationsRequest(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        project_id: str = None,
        app_server_id: int = None,
        page_index: int = None,
    ):
        self.page_size = page_size
        self.project_id = project_id
        self.app_server_id = app_server_id
        self.page_index = page_index

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.app_server_id is not None:
            result['AppServerId'] = self.app_server_id
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('AppServerId') is not None:
            self.app_server_id = m.get('AppServerId')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        return self


class ListUpstreamAppKeyRelationsResponseBodyRelationListPagination(TeaModel):
    def __init__(
        self,
        page_index: int = None,
        total_page_count: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.page_index = page_index
        self.total_page_count = total_page_count
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.total_page_count is not None:
            result['TotalPageCount'] = self.total_page_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('TotalPageCount') is not None:
            self.total_page_count = m.get('TotalPageCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListUpstreamAppKeyRelationsResponseBodyRelationListList(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        app_key: str = None,
        app_package: str = None,
        project_id: str = None,
        gmt_create: int = None,
        papp_key: str = None,
        id: int = None,
    ):
        self.app_name = app_name
        self.app_key = app_key
        self.app_package = app_package
        self.project_id = project_id
        self.gmt_create = gmt_create
        self.papp_key = papp_key
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.app_package is not None:
            result['AppPackage'] = self.app_package
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.papp_key is not None:
            result['PAppKey'] = self.papp_key
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('AppPackage') is not None:
            self.app_package = m.get('AppPackage')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('PAppKey') is not None:
            self.papp_key = m.get('PAppKey')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListUpstreamAppKeyRelationsResponseBodyRelationList(TeaModel):
    def __init__(
        self,
        pagination: ListUpstreamAppKeyRelationsResponseBodyRelationListPagination = None,
        list: List[ListUpstreamAppKeyRelationsResponseBodyRelationListList] = None,
    ):
        self.pagination = pagination
        self.list = list

    def validate(self):
        if self.pagination:
            self.pagination.validate()
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.pagination is not None:
            result['Pagination'] = self.pagination.to_map()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pagination') is not None:
            temp_model = ListUpstreamAppKeyRelationsResponseBodyRelationListPagination()
            self.pagination = temp_model.from_map(m['Pagination'])
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListUpstreamAppKeyRelationsResponseBodyRelationListList()
                self.list.append(temp_model.from_map(k))
        return self


class ListUpstreamAppKeyRelationsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        relation_list: ListUpstreamAppKeyRelationsResponseBodyRelationList = None,
    ):
        self.request_id = request_id
        self.relation_list = relation_list

    def validate(self):
        if self.relation_list:
            self.relation_list.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.relation_list is not None:
            result['RelationList'] = self.relation_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RelationList') is not None:
            temp_model = ListUpstreamAppKeyRelationsResponseBodyRelationList()
            self.relation_list = temp_model.from_map(m['RelationList'])
        return self


class ListUpstreamAppKeyRelationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListUpstreamAppKeyRelationsResponseBody = None,
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
            temp_model = ListUpstreamAppKeyRelationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUpstreamAppServersRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        page_index: str = None,
        page_size: str = None,
    ):
        self.project_id = project_id
        self.page_index = page_index
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListUpstreamAppServersResponseBodyAppServersPagination(TeaModel):
    def __init__(
        self,
        page_index: int = None,
        total_page_count: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.page_index = page_index
        self.total_page_count = total_page_count
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.total_page_count is not None:
            result['TotalPageCount'] = self.total_page_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('TotalPageCount') is not None:
            self.total_page_count = m.get('TotalPageCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListUpstreamAppServersResponseBodyAppServersList(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        gmt_create: int = None,
        tags: str = None,
        queue_name_list: str = None,
        papp_key: str = None,
        gmt_modified: int = None,
        name: str = None,
        id: int = None,
    ):
        self.project_id = project_id
        self.gmt_create = gmt_create
        self.tags = tags
        self.queue_name_list = queue_name_list
        self.papp_key = papp_key
        self.gmt_modified = gmt_modified
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.queue_name_list is not None:
            result['QueueNameList'] = self.queue_name_list
        if self.papp_key is not None:
            result['PAppKey'] = self.papp_key
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('QueueNameList') is not None:
            self.queue_name_list = m.get('QueueNameList')
        if m.get('PAppKey') is not None:
            self.papp_key = m.get('PAppKey')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListUpstreamAppServersResponseBodyAppServers(TeaModel):
    def __init__(
        self,
        pagination: ListUpstreamAppServersResponseBodyAppServersPagination = None,
        list: List[ListUpstreamAppServersResponseBodyAppServersList] = None,
    ):
        self.pagination = pagination
        self.list = list

    def validate(self):
        if self.pagination:
            self.pagination.validate()
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.pagination is not None:
            result['Pagination'] = self.pagination.to_map()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pagination') is not None:
            temp_model = ListUpstreamAppServersResponseBodyAppServersPagination()
            self.pagination = temp_model.from_map(m['Pagination'])
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListUpstreamAppServersResponseBodyAppServersList()
                self.list.append(temp_model.from_map(k))
        return self


class ListUpstreamAppServersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        app_servers: ListUpstreamAppServersResponseBodyAppServers = None,
    ):
        self.request_id = request_id
        self.app_servers = app_servers

    def validate(self):
        if self.app_servers:
            self.app_servers.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.app_servers is not None:
            result['AppServers'] = self.app_servers.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AppServers') is not None:
            temp_model = ListUpstreamAppServersResponseBodyAppServers()
            self.app_servers = temp_model.from_map(m['AppServers'])
        return self


class ListUpstreamAppServersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListUpstreamAppServersResponseBody = None,
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
            temp_model = ListUpstreamAppServersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVersionDeviceGroupsRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
    ):
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class ListVersionDeviceGroupsResponseBodyDeviceGroupList(TeaModel):
    def __init__(
        self,
        gmt_modify: str = None,
        description: str = None,
        gmt_create: str = None,
        name: str = None,
        id: str = None,
    ):
        self.gmt_modify = gmt_modify
        self.description = description
        self.gmt_create = gmt_create
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.gmt_modify is not None:
            result['GmtModify'] = self.gmt_modify
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtModify') is not None:
            self.gmt_modify = m.get('GmtModify')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListVersionDeviceGroupsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        device_group_list: List[ListVersionDeviceGroupsResponseBodyDeviceGroupList] = None,
    ):
        self.request_id = request_id
        self.device_group_list = device_group_list

    def validate(self):
        if self.device_group_list:
            for k in self.device_group_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['DeviceGroupList'] = []
        if self.device_group_list is not None:
            for k in self.device_group_list:
                result['DeviceGroupList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.device_group_list = []
        if m.get('DeviceGroupList') is not None:
            for k in m.get('DeviceGroupList'):
                temp_model = ListVersionDeviceGroupsResponseBodyDeviceGroupList()
                self.device_group_list.append(temp_model.from_map(k))
        return self


class ListVersionDeviceGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListVersionDeviceGroupsResponseBody = None,
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
            temp_model = ListVersionDeviceGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishAppVersionRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        version_id: str = None,
        send_message: bool = None,
    ):
        self.project_id = project_id
        self.version_id = version_id
        self.send_message = send_message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.send_message is not None:
            result['SendMessage'] = self.send_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('SendMessage') is not None:
            self.send_message = m.get('SendMessage')
        return self


class PublishAppVersionResponseBody(TeaModel):
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


class PublishAppVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PublishAppVersionResponseBody = None,
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
            temp_model = PublishAppVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishMqttMessageRequest(TeaModel):
    def __init__(
        self,
        app_key: str = None,
        topic: str = None,
        project_id: str = None,
        message: str = None,
        qo_s: int = None,
    ):
        self.app_key = app_key
        self.topic = topic
        self.project_id = project_id
        self.message = message
        self.qo_s = qo_s

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.message is not None:
            result['Message'] = self.message
        if self.qo_s is not None:
            result['QoS'] = self.qo_s
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('QoS') is not None:
            self.qo_s = m.get('QoS')
        return self


class PublishMqttMessageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        mid: str = None,
    ):
        self.request_id = request_id
        self.mid = mid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.mid is not None:
            result['Mid'] = self.mid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Mid') is not None:
            self.mid = m.get('Mid')
        return self


class PublishMqttMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PublishMqttMessageResponseBody = None,
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
            temp_model = PublishMqttMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishOsVersionRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        version_id: str = None,
        send_message: bool = None,
    ):
        self.project_id = project_id
        self.version_id = version_id
        self.send_message = send_message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.send_message is not None:
            result['SendMessage'] = self.send_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('SendMessage') is not None:
            self.send_message = m.get('SendMessage')
        return self


class PublishOsVersionResponseBody(TeaModel):
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


class PublishOsVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PublishOsVersionResponseBody = None,
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
            temp_model = PublishOsVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushMessageRequest(TeaModel):
    def __init__(
        self,
        app_package: str = None,
        desc: str = None,
        act: str = None,
        uri: str = None,
        pkg_content: str = None,
        custom_content: str = None,
        receiver_type: str = None,
        receiver_values: str = None,
        expired_time: int = None,
        title: str = None,
        project_id: str = None,
        app_key: str = None,
        type: int = None,
    ):
        self.app_package = app_package
        self.desc = desc
        self.act = act
        self.uri = uri
        self.pkg_content = pkg_content
        self.custom_content = custom_content
        self.receiver_type = receiver_type
        self.receiver_values = receiver_values
        self.expired_time = expired_time
        self.title = title
        self.project_id = project_id
        self.app_key = app_key
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_package is not None:
            result['AppPackage'] = self.app_package
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.act is not None:
            result['Act'] = self.act
        if self.uri is not None:
            result['Uri'] = self.uri
        if self.pkg_content is not None:
            result['PkgContent'] = self.pkg_content
        if self.custom_content is not None:
            result['CustomContent'] = self.custom_content
        if self.receiver_type is not None:
            result['ReceiverType'] = self.receiver_type
        if self.receiver_values is not None:
            result['ReceiverValues'] = self.receiver_values
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.title is not None:
            result['Title'] = self.title
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppPackage') is not None:
            self.app_package = m.get('AppPackage')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('Act') is not None:
            self.act = m.get('Act')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        if m.get('PkgContent') is not None:
            self.pkg_content = m.get('PkgContent')
        if m.get('CustomContent') is not None:
            self.custom_content = m.get('CustomContent')
        if m.get('ReceiverType') is not None:
            self.receiver_type = m.get('ReceiverType')
        if m.get('ReceiverValues') is not None:
            self.receiver_values = m.get('ReceiverValues')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class PushMessageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        mid: int = None,
    ):
        self.request_id = request_id
        self.mid = mid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.mid is not None:
            result['Mid'] = self.mid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Mid') is not None:
            self.mid = m.get('Mid')
        return self


class PushMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PushMessageResponseBody = None,
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
            temp_model = PushMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushVersionMessageRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        version_id: str = None,
        version_type: str = None,
    ):
        self.project_id = project_id
        self.version_id = version_id
        self.version_type = version_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.version_type is not None:
            result['VersionType'] = self.version_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('VersionType') is not None:
            self.version_type = m.get('VersionType')
        return self


class PushVersionMessageResponseBody(TeaModel):
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


class PushVersionMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PushVersionMessageResponseBody = None,
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
            temp_model = PushVersionMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPrepublishPassedDeviceCountRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        prepublish_id: str = None,
    ):
        self.project_id = project_id
        self.prepublish_id = prepublish_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.prepublish_id is not None:
            result['PrepublishId'] = self.prepublish_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('PrepublishId') is not None:
            self.prepublish_id = m.get('PrepublishId')
        return self


class QueryPrepublishPassedDeviceCountResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        count: int = None,
    ):
        self.request_id = request_id
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class QueryPrepublishPassedDeviceCountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryPrepublishPassedDeviceCountResponseBody = None,
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
            temp_model = QueryPrepublishPassedDeviceCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitAssistReportRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        assist_id: str = None,
        assist_description: str = None,
        assist_result: str = None,
        assist_tag: str = None,
        assist_reason: str = None,
        device_model: str = None,
    ):
        self.project_id = project_id
        self.assist_id = assist_id
        self.assist_description = assist_description
        self.assist_result = assist_result
        self.assist_tag = assist_tag
        self.assist_reason = assist_reason
        self.device_model = device_model

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.assist_id is not None:
            result['AssistId'] = self.assist_id
        if self.assist_description is not None:
            result['AssistDescription'] = self.assist_description
        if self.assist_result is not None:
            result['AssistResult'] = self.assist_result
        if self.assist_tag is not None:
            result['AssistTag'] = self.assist_tag
        if self.assist_reason is not None:
            result['AssistReason'] = self.assist_reason
        if self.device_model is not None:
            result['DeviceModel'] = self.device_model
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('AssistId') is not None:
            self.assist_id = m.get('AssistId')
        if m.get('AssistDescription') is not None:
            self.assist_description = m.get('AssistDescription')
        if m.get('AssistResult') is not None:
            self.assist_result = m.get('AssistResult')
        if m.get('AssistTag') is not None:
            self.assist_tag = m.get('AssistTag')
        if m.get('AssistReason') is not None:
            self.assist_reason = m.get('AssistReason')
        if m.get('DeviceModel') is not None:
            self.device_model = m.get('DeviceModel')
        return self


class SubmitAssistReportResponseBody(TeaModel):
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


class SubmitAssistReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SubmitAssistReportResponseBody = None,
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
            temp_model = SubmitAssistReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateApiGatewayAppStatusRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        gateway_app_id: str = None,
        status: int = None,
    ):
        self.project_id = project_id
        self.gateway_app_id = gateway_app_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.gateway_app_id is not None:
            result['GatewayAppId'] = self.gateway_app_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('GatewayAppId') is not None:
            self.gateway_app_id = m.get('GatewayAppId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateApiGatewayAppStatusResponseBody(TeaModel):
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


class UpdateApiGatewayAppStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateApiGatewayAppStatusResponseBody = None,
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
            temp_model = UpdateApiGatewayAppStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAppBlackWhiteVersionsRequest(TeaModel):
    def __init__(
        self,
        white_app_versions: str = None,
        project_id: str = None,
        version_id: str = None,
        black_app_versions: str = None,
    ):
        self.white_app_versions = white_app_versions
        self.project_id = project_id
        self.version_id = version_id
        self.black_app_versions = black_app_versions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.white_app_versions is not None:
            result['WhiteAppVersions'] = self.white_app_versions
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.black_app_versions is not None:
            result['BlackAppVersions'] = self.black_app_versions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WhiteAppVersions') is not None:
            self.white_app_versions = m.get('WhiteAppVersions')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('BlackAppVersions') is not None:
            self.black_app_versions = m.get('BlackAppVersions')
        return self


class UpdateAppBlackWhiteVersionsResponseBody(TeaModel):
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


class UpdateAppBlackWhiteVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateAppBlackWhiteVersionsResponseBody = None,
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
            temp_model = UpdateAppBlackWhiteVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAppVersionRequest(TeaModel):
    def __init__(
        self,
        black_version_list: str = None,
        is_allow_new_install: str = None,
        project_id: str = None,
        app_id: str = None,
        app_version: str = None,
        version_code: str = None,
        install_type: str = None,
        remark: str = None,
        is_force_upgrade: str = None,
        is_silent_upgrade: str = None,
        is_need_restart: str = None,
        package_url: str = None,
        release_note: str = None,
        white_version_list: str = None,
        restart_type: str = None,
        restart_app_type: str = None,
        restart_app_param: str = None,
        device_adapter_list: str = None,
        version_id: str = None,
        apk_md_5: str = None,
    ):
        self.black_version_list = black_version_list
        self.is_allow_new_install = is_allow_new_install
        self.project_id = project_id
        self.app_id = app_id
        self.app_version = app_version
        self.version_code = version_code
        self.install_type = install_type
        self.remark = remark
        self.is_force_upgrade = is_force_upgrade
        self.is_silent_upgrade = is_silent_upgrade
        self.is_need_restart = is_need_restart
        self.package_url = package_url
        self.release_note = release_note
        self.white_version_list = white_version_list
        self.restart_type = restart_type
        self.restart_app_type = restart_app_type
        self.restart_app_param = restart_app_param
        self.device_adapter_list = device_adapter_list
        self.version_id = version_id
        self.apk_md_5 = apk_md_5

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.black_version_list is not None:
            result['BlackVersionList'] = self.black_version_list
        if self.is_allow_new_install is not None:
            result['IsAllowNewInstall'] = self.is_allow_new_install
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.version_code is not None:
            result['VersionCode'] = self.version_code
        if self.install_type is not None:
            result['InstallType'] = self.install_type
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.is_force_upgrade is not None:
            result['IsForceUpgrade'] = self.is_force_upgrade
        if self.is_silent_upgrade is not None:
            result['IsSilentUpgrade'] = self.is_silent_upgrade
        if self.is_need_restart is not None:
            result['IsNeedRestart'] = self.is_need_restart
        if self.package_url is not None:
            result['PackageUrl'] = self.package_url
        if self.release_note is not None:
            result['ReleaseNote'] = self.release_note
        if self.white_version_list is not None:
            result['WhiteVersionList'] = self.white_version_list
        if self.restart_type is not None:
            result['RestartType'] = self.restart_type
        if self.restart_app_type is not None:
            result['RestartAppType'] = self.restart_app_type
        if self.restart_app_param is not None:
            result['RestartAppParam'] = self.restart_app_param
        if self.device_adapter_list is not None:
            result['DeviceAdapterList'] = self.device_adapter_list
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.apk_md_5 is not None:
            result['ApkMd5'] = self.apk_md_5
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlackVersionList') is not None:
            self.black_version_list = m.get('BlackVersionList')
        if m.get('IsAllowNewInstall') is not None:
            self.is_allow_new_install = m.get('IsAllowNewInstall')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('VersionCode') is not None:
            self.version_code = m.get('VersionCode')
        if m.get('InstallType') is not None:
            self.install_type = m.get('InstallType')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('IsForceUpgrade') is not None:
            self.is_force_upgrade = m.get('IsForceUpgrade')
        if m.get('IsSilentUpgrade') is not None:
            self.is_silent_upgrade = m.get('IsSilentUpgrade')
        if m.get('IsNeedRestart') is not None:
            self.is_need_restart = m.get('IsNeedRestart')
        if m.get('PackageUrl') is not None:
            self.package_url = m.get('PackageUrl')
        if m.get('ReleaseNote') is not None:
            self.release_note = m.get('ReleaseNote')
        if m.get('WhiteVersionList') is not None:
            self.white_version_list = m.get('WhiteVersionList')
        if m.get('RestartType') is not None:
            self.restart_type = m.get('RestartType')
        if m.get('RestartAppType') is not None:
            self.restart_app_type = m.get('RestartAppType')
        if m.get('RestartAppParam') is not None:
            self.restart_app_param = m.get('RestartAppParam')
        if m.get('DeviceAdapterList') is not None:
            self.device_adapter_list = m.get('DeviceAdapterList')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('ApkMd5') is not None:
            self.apk_md_5 = m.get('ApkMd5')
        return self


class UpdateAppVersionResponseBody(TeaModel):
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


class UpdateAppVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateAppVersionResponseBody = None,
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
            temp_model = UpdateAppVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAppVersionReleaseNoteRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        version_id: str = None,
        release_note: str = None,
    ):
        self.project_id = project_id
        self.version_id = version_id
        self.release_note = release_note

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.release_note is not None:
            result['ReleaseNote'] = self.release_note
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('ReleaseNote') is not None:
            self.release_note = m.get('ReleaseNote')
        return self


class UpdateAppVersionReleaseNoteResponseBody(TeaModel):
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


class UpdateAppVersionReleaseNoteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateAppVersionReleaseNoteResponseBody = None,
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
            temp_model = UpdateAppVersionReleaseNoteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAppVersionRemarkRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        version_id: str = None,
        remark: str = None,
    ):
        self.project_id = project_id
        self.version_id = version_id
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class UpdateAppVersionRemarkResponseBody(TeaModel):
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


class UpdateAppVersionRemarkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateAppVersionRemarkResponseBody = None,
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
            temp_model = UpdateAppVersionRemarkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAppVersionStatusRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        id: str = None,
        status: str = None,
    ):
        self.project_id = project_id
        self.id = id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.id is not None:
            result['Id'] = self.id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateAppVersionStatusResponseBody(TeaModel):
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


class UpdateAppVersionStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateAppVersionStatusResponseBody = None,
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
            temp_model = UpdateAppVersionStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCustomizedFilterRequest(TeaModel):
    def __init__(
        self,
        black_white_type: str = None,
        project_id: str = None,
        name: str = None,
        value: str = None,
        value_type: str = None,
        value_compare_type: str = None,
        id: int = None,
    ):
        self.black_white_type = black_white_type
        self.project_id = project_id
        self.name = name
        self.value = value
        self.value_type = value_type
        self.value_compare_type = value_compare_type
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.black_white_type is not None:
            result['BlackWhiteType'] = self.black_white_type
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        if self.value_type is not None:
            result['ValueType'] = self.value_type
        if self.value_compare_type is not None:
            result['ValueCompareType'] = self.value_compare_type
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlackWhiteType') is not None:
            self.black_white_type = m.get('BlackWhiteType')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('ValueType') is not None:
            self.value_type = m.get('ValueType')
        if m.get('ValueCompareType') is not None:
            self.value_compare_type = m.get('ValueCompareType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class UpdateCustomizedFilterResponseBody(TeaModel):
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


class UpdateCustomizedFilterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateCustomizedFilterResponseBody = None,
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
            temp_model = UpdateCustomizedFilterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDeviceModelRequest(TeaModel):
    def __init__(
        self,
        init_usage_type: str = None,
        model_name: str = None,
        id: str = None,
        brand_name: str = None,
        description: str = None,
        device_type: str = None,
        can_create_device_id: str = None,
        project_id: str = None,
        hardware_type: str = None,
        security_chip: str = None,
        os_platform: str = None,
        object_key: str = None,
        device_name: str = None,
    ):
        self.init_usage_type = init_usage_type
        self.model_name = model_name
        self.id = id
        self.brand_name = brand_name
        self.description = description
        self.device_type = device_type
        self.can_create_device_id = can_create_device_id
        self.project_id = project_id
        self.hardware_type = hardware_type
        self.security_chip = security_chip
        self.os_platform = os_platform
        self.object_key = object_key
        self.device_name = device_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.init_usage_type is not None:
            result['InitUsageType'] = self.init_usage_type
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.id is not None:
            result['Id'] = self.id
        if self.brand_name is not None:
            result['BrandName'] = self.brand_name
        if self.description is not None:
            result['Description'] = self.description
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.can_create_device_id is not None:
            result['CanCreateDeviceId'] = self.can_create_device_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.hardware_type is not None:
            result['HardwareType'] = self.hardware_type
        if self.security_chip is not None:
            result['SecurityChip'] = self.security_chip
        if self.os_platform is not None:
            result['OsPlatform'] = self.os_platform
        if self.object_key is not None:
            result['ObjectKey'] = self.object_key
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InitUsageType') is not None:
            self.init_usage_type = m.get('InitUsageType')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('BrandName') is not None:
            self.brand_name = m.get('BrandName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('CanCreateDeviceId') is not None:
            self.can_create_device_id = m.get('CanCreateDeviceId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('HardwareType') is not None:
            self.hardware_type = m.get('HardwareType')
        if m.get('SecurityChip') is not None:
            self.security_chip = m.get('SecurityChip')
        if m.get('OsPlatform') is not None:
            self.os_platform = m.get('OsPlatform')
        if m.get('ObjectKey') is not None:
            self.object_key = m.get('ObjectKey')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        return self


class UpdateDeviceModelResponseBody(TeaModel):
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


class UpdateDeviceModelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateDeviceModelResponseBody = None,
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
            temp_model = UpdateDeviceModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateNamespaceDataRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        namespace: str = None,
        auth_type: str = None,
        device_id_type: str = None,
        device_id: str = None,
        account_type: str = None,
        account_id: str = None,
        path: str = None,
        old_data: str = None,
        new_data: str = None,
    ):
        self.project_id = project_id
        self.namespace = namespace
        self.auth_type = auth_type
        self.device_id_type = device_id_type
        self.device_id = device_id
        self.account_type = account_type
        self.account_id = account_id
        self.path = path
        self.old_data = old_data
        self.new_data = new_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type
        if self.device_id_type is not None:
            result['DeviceIdType'] = self.device_id_type
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.path is not None:
            result['Path'] = self.path
        if self.old_data is not None:
            result['OldData'] = self.old_data
        if self.new_data is not None:
            result['NewData'] = self.new_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')
        if m.get('DeviceIdType') is not None:
            self.device_id_type = m.get('DeviceIdType')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('OldData') is not None:
            self.old_data = m.get('OldData')
        if m.get('NewData') is not None:
            self.new_data = m.get('NewData')
        return self


class UpdateNamespaceDataResponseBody(TeaModel):
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


class UpdateNamespaceDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateNamespaceDataResponseBody = None,
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
            temp_model = UpdateNamespaceDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateOsBlackWhiteVersionsRequest(TeaModel):
    def __init__(
        self,
        white_versions: str = None,
        project_id: str = None,
        version_id: str = None,
        black_versions: str = None,
    ):
        self.white_versions = white_versions
        self.project_id = project_id
        self.version_id = version_id
        self.black_versions = black_versions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.white_versions is not None:
            result['WhiteVersions'] = self.white_versions
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.black_versions is not None:
            result['BlackVersions'] = self.black_versions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WhiteVersions') is not None:
            self.white_versions = m.get('WhiteVersions')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('BlackVersions') is not None:
            self.black_versions = m.get('BlackVersions')
        return self


class UpdateOsBlackWhiteVersionsResponseBody(TeaModel):
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


class UpdateOsBlackWhiteVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateOsBlackWhiteVersionsResponseBody = None,
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
            temp_model = UpdateOsBlackWhiteVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateOsVersionRequest(TeaModel):
    def __init__(
        self,
        is_milestone: str = None,
        is_force_night_upgrade: str = None,
        project_id: str = None,
        device_model_id: str = None,
        system_version: str = None,
        release_note: str = None,
        remark: str = None,
        is_force_upgrade: str = None,
        black_version_list: str = None,
        white_version_list: str = None,
        max_client_version: str = None,
        min_client_version: str = None,
        night_upgrade_download_type: str = None,
        night_upgrade_is_show_tip: str = None,
        night_upgrade_is_allowed_cancel: str = None,
        rom_list: str = None,
        id: str = None,
        enable_mobile_download: str = None,
        mobile_download_max_size: str = None,
    ):
        self.is_milestone = is_milestone
        self.is_force_night_upgrade = is_force_night_upgrade
        self.project_id = project_id
        self.device_model_id = device_model_id
        self.system_version = system_version
        self.release_note = release_note
        self.remark = remark
        self.is_force_upgrade = is_force_upgrade
        self.black_version_list = black_version_list
        self.white_version_list = white_version_list
        self.max_client_version = max_client_version
        self.min_client_version = min_client_version
        self.night_upgrade_download_type = night_upgrade_download_type
        self.night_upgrade_is_show_tip = night_upgrade_is_show_tip
        self.night_upgrade_is_allowed_cancel = night_upgrade_is_allowed_cancel
        self.rom_list = rom_list
        self.id = id
        self.enable_mobile_download = enable_mobile_download
        self.mobile_download_max_size = mobile_download_max_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.is_milestone is not None:
            result['IsMilestone'] = self.is_milestone
        if self.is_force_night_upgrade is not None:
            result['IsForceNightUpgrade'] = self.is_force_night_upgrade
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.device_model_id is not None:
            result['DeviceModelId'] = self.device_model_id
        if self.system_version is not None:
            result['SystemVersion'] = self.system_version
        if self.release_note is not None:
            result['ReleaseNote'] = self.release_note
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.is_force_upgrade is not None:
            result['IsForceUpgrade'] = self.is_force_upgrade
        if self.black_version_list is not None:
            result['BlackVersionList'] = self.black_version_list
        if self.white_version_list is not None:
            result['WhiteVersionList'] = self.white_version_list
        if self.max_client_version is not None:
            result['MaxClientVersion'] = self.max_client_version
        if self.min_client_version is not None:
            result['MinClientVersion'] = self.min_client_version
        if self.night_upgrade_download_type is not None:
            result['NightUpgradeDownloadType'] = self.night_upgrade_download_type
        if self.night_upgrade_is_show_tip is not None:
            result['NightUpgradeIsShowTip'] = self.night_upgrade_is_show_tip
        if self.night_upgrade_is_allowed_cancel is not None:
            result['NightUpgradeIsAllowedCancel'] = self.night_upgrade_is_allowed_cancel
        if self.rom_list is not None:
            result['RomList'] = self.rom_list
        if self.id is not None:
            result['Id'] = self.id
        if self.enable_mobile_download is not None:
            result['EnableMobileDownload'] = self.enable_mobile_download
        if self.mobile_download_max_size is not None:
            result['MobileDownloadMaxSize'] = self.mobile_download_max_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsMilestone') is not None:
            self.is_milestone = m.get('IsMilestone')
        if m.get('IsForceNightUpgrade') is not None:
            self.is_force_night_upgrade = m.get('IsForceNightUpgrade')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('DeviceModelId') is not None:
            self.device_model_id = m.get('DeviceModelId')
        if m.get('SystemVersion') is not None:
            self.system_version = m.get('SystemVersion')
        if m.get('ReleaseNote') is not None:
            self.release_note = m.get('ReleaseNote')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('IsForceUpgrade') is not None:
            self.is_force_upgrade = m.get('IsForceUpgrade')
        if m.get('BlackVersionList') is not None:
            self.black_version_list = m.get('BlackVersionList')
        if m.get('WhiteVersionList') is not None:
            self.white_version_list = m.get('WhiteVersionList')
        if m.get('MaxClientVersion') is not None:
            self.max_client_version = m.get('MaxClientVersion')
        if m.get('MinClientVersion') is not None:
            self.min_client_version = m.get('MinClientVersion')
        if m.get('NightUpgradeDownloadType') is not None:
            self.night_upgrade_download_type = m.get('NightUpgradeDownloadType')
        if m.get('NightUpgradeIsShowTip') is not None:
            self.night_upgrade_is_show_tip = m.get('NightUpgradeIsShowTip')
        if m.get('NightUpgradeIsAllowedCancel') is not None:
            self.night_upgrade_is_allowed_cancel = m.get('NightUpgradeIsAllowedCancel')
        if m.get('RomList') is not None:
            self.rom_list = m.get('RomList')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('EnableMobileDownload') is not None:
            self.enable_mobile_download = m.get('EnableMobileDownload')
        if m.get('MobileDownloadMaxSize') is not None:
            self.mobile_download_max_size = m.get('MobileDownloadMaxSize')
        return self


class UpdateOsVersionResponseBody(TeaModel):
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


class UpdateOsVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateOsVersionResponseBody = None,
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
            temp_model = UpdateOsVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateOsVersionReleaseNoteRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        version_id: str = None,
        release_note: str = None,
    ):
        self.project_id = project_id
        self.version_id = version_id
        self.release_note = release_note

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.release_note is not None:
            result['ReleaseNote'] = self.release_note
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('ReleaseNote') is not None:
            self.release_note = m.get('ReleaseNote')
        return self


class UpdateOsVersionReleaseNoteResponseBody(TeaModel):
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


class UpdateOsVersionReleaseNoteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateOsVersionReleaseNoteResponseBody = None,
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
            temp_model = UpdateOsVersionReleaseNoteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateOsVersionRemarkRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        version_id: str = None,
        remark: str = None,
    ):
        self.project_id = project_id
        self.version_id = version_id
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class UpdateOsVersionRemarkResponseBody(TeaModel):
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


class UpdateOsVersionRemarkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateOsVersionRemarkResponseBody = None,
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
            temp_model = UpdateOsVersionRemarkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateOsVersionStatusRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        id: str = None,
        status: str = None,
    ):
        self.project_id = project_id
        self.id = id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.id is not None:
            result['Id'] = self.id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateOsVersionStatusResponseBody(TeaModel):
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


class UpdateOsVersionStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateOsVersionStatusResponseBody = None,
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
            temp_model = UpdateOsVersionStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProjectRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        name: str = None,
        description: str = None,
    ):
        self.project_id = project_id
        self.name = name
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class UpdateProjectResponseBody(TeaModel):
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


class UpdateProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateProjectResponseBody = None,
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
            temp_model = UpdateProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSchemaSubscribeRequest(TeaModel):
    def __init__(
        self,
        device_model: str = None,
        subscribe_list: str = None,
        project_id: str = None,
        schema_version: str = None,
    ):
        self.device_model = device_model
        self.subscribe_list = subscribe_list
        self.project_id = project_id
        self.schema_version = schema_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.device_model is not None:
            result['DeviceModel'] = self.device_model
        if self.subscribe_list is not None:
            result['SubscribeList'] = self.subscribe_list
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceModel') is not None:
            self.device_model = m.get('DeviceModel')
        if m.get('SubscribeList') is not None:
            self.subscribe_list = m.get('SubscribeList')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        return self


class UpdateSchemaSubscribeResponseBody(TeaModel):
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


class UpdateSchemaSubscribeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateSchemaSubscribeResponseBody = None,
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
            temp_model = UpdateSchemaSubscribeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateShadowSchemaRequest(TeaModel):
    def __init__(
        self,
        device_model_id: str = None,
        auth_type: str = None,
        namespace: str = None,
        project_id: str = None,
        schema: str = None,
        id: str = None,
    ):
        self.device_model_id = device_model_id
        self.auth_type = auth_type
        self.namespace = namespace
        self.project_id = project_id
        self.schema = schema
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.device_model_id is not None:
            result['DeviceModelId'] = self.device_model_id
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.schema is not None:
            result['Schema'] = self.schema
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceModelId') is not None:
            self.device_model_id = m.get('DeviceModelId')
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Schema') is not None:
            self.schema = m.get('Schema')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class UpdateShadowSchemaResponseBody(TeaModel):
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


class UpdateShadowSchemaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateShadowSchemaResponseBody = None,
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
            temp_model = UpdateShadowSchemaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTriggerRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        id: int = None,
        sandbox: int = None,
        production: int = None,
    ):
        self.project_id = project_id
        self.id = id
        self.sandbox = sandbox
        self.production = production

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.id is not None:
            result['Id'] = self.id
        if self.sandbox is not None:
            result['Sandbox'] = self.sandbox
        if self.production is not None:
            result['Production'] = self.production
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Sandbox') is not None:
            self.sandbox = m.get('Sandbox')
        if m.get('Production') is not None:
            self.production = m.get('Production')
        return self


class UpdateTriggerResponseBody(TeaModel):
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


class UpdateTriggerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateTriggerResponseBody = None,
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
            temp_model = UpdateTriggerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUpstreamAppServerRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
        tags: str = None,
        project_id: str = None,
    ):
        self.id = id
        self.name = name
        self.tags = tags
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class UpdateUpstreamAppServerResponseBody(TeaModel):
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


class UpdateUpstreamAppServerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateUpstreamAppServerResponseBody = None,
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
            temp_model = UpdateUpstreamAppServerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateVersionDeviceGroupRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        name: str = None,
        description: str = None,
        id: str = None,
    ):
        self.project_id = project_id
        self.name = name
        self.description = description
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class UpdateVersionDeviceGroupResponseBody(TeaModel):
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


class UpdateVersionDeviceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateVersionDeviceGroupResponseBody = None,
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
            temp_model = UpdateVersionDeviceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateVersionPrepublishActiveStatusRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        prepublish_id: str = None,
        is_active: str = None,
    ):
        self.project_id = project_id
        self.prepublish_id = prepublish_id
        self.is_active = is_active

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.prepublish_id is not None:
            result['PrepublishId'] = self.prepublish_id
        if self.is_active is not None:
            result['IsActive'] = self.is_active
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('PrepublishId') is not None:
            self.prepublish_id = m.get('PrepublishId')
        if m.get('IsActive') is not None:
            self.is_active = m.get('IsActive')
        return self


class UpdateVersionPrepublishActiveStatusResponseBody(TeaModel):
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


class UpdateVersionPrepublishActiveStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateVersionPrepublishActiveStatusResponseBody = None,
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
            temp_model = UpdateVersionPrepublishActiveStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


