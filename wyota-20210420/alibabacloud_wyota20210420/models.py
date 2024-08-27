# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class ActivateDeviceRequest(TeaModel):
    def __init__(
        self,
        uuid: str = None,
    ):
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class ActivateDeviceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ActivateDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ActivateDeviceResponseBody = None,
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
            temp_model = ActivateDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddDeviceFromSNRequest(TeaModel):
    def __init__(
        self,
        alias: str = None,
        custom_property: str = None,
        group_id: str = None,
        label_contents: str = None,
        secure_network_type: str = None,
        serial_no: str = None,
    ):
        self.alias = alias
        self.custom_property = custom_property
        self.group_id = group_id
        self.label_contents = label_contents
        self.secure_network_type = secure_network_type
        # This parameter is required.
        self.serial_no = serial_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.custom_property is not None:
            result['CustomProperty'] = self.custom_property
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.label_contents is not None:
            result['LabelContents'] = self.label_contents
        if self.secure_network_type is not None:
            result['SecureNetworkType'] = self.secure_network_type
        if self.serial_no is not None:
            result['SerialNo'] = self.serial_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('CustomProperty') is not None:
            self.custom_property = m.get('CustomProperty')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('LabelContents') is not None:
            self.label_contents = m.get('LabelContents')
        if m.get('SecureNetworkType') is not None:
            self.secure_network_type = m.get('SecureNetworkType')
        if m.get('SerialNo') is not None:
            self.serial_no = m.get('SerialNo')
        return self


class AddDeviceFromSNResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddDeviceFromSNResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddDeviceFromSNResponseBody = None,
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
            temp_model = AddDeviceFromSNResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddDeviceSeatsAndLabelsRequest(TeaModel):
    def __init__(
        self,
        is_unique: bool = None,
        label: str = None,
        label_list: List[str] = None,
        seat_name: str = None,
        serial_no: str = None,
        tenant_id: str = None,
        zone_id: str = None,
    ):
        self.is_unique = is_unique
        self.label = label
        self.label_list = label_list
        self.seat_name = seat_name
        self.serial_no = serial_no
        self.tenant_id = tenant_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_unique is not None:
            result['IsUnique'] = self.is_unique
        if self.label is not None:
            result['Label'] = self.label
        if self.label_list is not None:
            result['LabelList'] = self.label_list
        if self.seat_name is not None:
            result['SeatName'] = self.seat_name
        if self.serial_no is not None:
            result['SerialNo'] = self.serial_no
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsUnique') is not None:
            self.is_unique = m.get('IsUnique')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('LabelList') is not None:
            self.label_list = m.get('LabelList')
        if m.get('SeatName') is not None:
            self.seat_name = m.get('SeatName')
        if m.get('SerialNo') is not None:
            self.serial_no = m.get('SerialNo')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class AddDeviceSeatsAndLabelsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddDeviceSeatsAndLabelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddDeviceSeatsAndLabelsResponseBody = None,
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
            temp_model = AddDeviceSeatsAndLabelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddDevicesFromCSVRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_type: int = None,
        seat_col: int = None,
        site_id: str = None,
        site_name: str = None,
    ):
        self.file_name = file_name
        self.file_type = file_type
        self.seat_col = seat_col
        self.site_id = site_id
        self.site_name = site_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.seat_col is not None:
            result['SeatCol'] = self.seat_col
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.site_name is not None:
            result['SiteName'] = self.site_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('SeatCol') is not None:
            self.seat_col = m.get('SeatCol')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('SiteName') is not None:
            self.site_name = m.get('SiteName')
        return self


class AddDevicesFromCSVResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddDevicesFromCSVResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddDevicesFromCSVResponseBody = None,
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
            temp_model = AddDevicesFromCSVResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddLabelsRequest(TeaModel):
    def __init__(
        self,
        label_contents: str = None,
    ):
        self.label_contents = label_contents

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_contents is not None:
            result['LabelContents'] = self.label_contents
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LabelContents') is not None:
            self.label_contents = m.get('LabelContents')
        return self


class AddLabelsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddLabelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddLabelsResponseBody = None,
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
            temp_model = AddLabelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddOrUpdateDeviceSeatsRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        user_custom_id: str = None,
        zone_id: str = None,
    ):
        self.file_name = file_name
        self.user_custom_id = user_custom_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.user_custom_id is not None:
            result['UserCustomId'] = self.user_custom_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('UserCustomId') is not None:
            self.user_custom_id = m.get('UserCustomId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class AddOrUpdateDeviceSeatsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddOrUpdateDeviceSeatsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddOrUpdateDeviceSeatsResponseBody = None,
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
            temp_model = AddOrUpdateDeviceSeatsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddTerminalRequest(TeaModel):
    def __init__(
        self,
        alias: str = None,
        serial_number: str = None,
        terminal_group_id: str = None,
    ):
        self.alias = alias
        self.serial_number = serial_number
        self.terminal_group_id = terminal_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.terminal_group_id is not None:
            result['TerminalGroupId'] = self.terminal_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('TerminalGroupId') is not None:
            self.terminal_group_id = m.get('TerminalGroupId')
        return self


class AddTerminalResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddTerminalResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddTerminalResponseBody = None,
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
            temp_model = AddTerminalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachEndUsersRequest(TeaModel):
    def __init__(
        self,
        end_user_ids: str = None,
        serial_no: str = None,
    ):
        # This parameter is required.
        self.end_user_ids = end_user_ids
        # This parameter is required.
        self.serial_no = serial_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_user_ids is not None:
            result['EndUserIds'] = self.end_user_ids
        if self.serial_no is not None:
            result['SerialNo'] = self.serial_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndUserIds') is not None:
            self.end_user_ids = m.get('EndUserIds')
        if m.get('SerialNo') is not None:
            self.serial_no = m.get('SerialNo')
        return self


class AttachEndUsersResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AttachEndUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AttachEndUsersResponseBody = None,
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
            temp_model = AttachEndUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachLabelRequest(TeaModel):
    def __init__(
        self,
        label_content: str = None,
        label_id: str = None,
        serial_no: str = None,
    ):
        self.label_content = label_content
        self.label_id = label_id
        # This parameter is required.
        self.serial_no = serial_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_content is not None:
            result['LabelContent'] = self.label_content
        if self.label_id is not None:
            result['LabelId'] = self.label_id
        if self.serial_no is not None:
            result['SerialNo'] = self.serial_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LabelContent') is not None:
            self.label_content = m.get('LabelContent')
        if m.get('LabelId') is not None:
            self.label_id = m.get('LabelId')
        if m.get('SerialNo') is not None:
            self.serial_no = m.get('SerialNo')
        return self


class AttachLabelResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AttachLabelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AttachLabelResponseBody = None,
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
            temp_model = AttachLabelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachLabelsRequest(TeaModel):
    def __init__(
        self,
        label_ids: str = None,
        serial_no: str = None,
        serial_no_list: str = None,
    ):
        self.label_ids = label_ids
        self.serial_no = serial_no
        self.serial_no_list = serial_no_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_ids is not None:
            result['LabelIds'] = self.label_ids
        if self.serial_no is not None:
            result['SerialNo'] = self.serial_no
        if self.serial_no_list is not None:
            result['SerialNoList'] = self.serial_no_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LabelIds') is not None:
            self.label_ids = m.get('LabelIds')
        if m.get('SerialNo') is not None:
            self.serial_no = m.get('SerialNo')
        if m.get('SerialNoList') is not None:
            self.serial_no_list = m.get('SerialNoList')
        return self


class AttachLabelsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AttachLabelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AttachLabelsResponseBody = None,
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
            temp_model = AttachLabelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindAccountLessLoginUserRequest(TeaModel):
    def __init__(
        self,
        end_user_id: str = None,
        serial_number: str = None,
        uuid: str = None,
    ):
        self.end_user_id = end_user_id
        self.serial_number = serial_number
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class BindAccountLessLoginUserResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BindAccountLessLoginUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BindAccountLessLoginUserResponseBody = None,
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
            temp_model = BindAccountLessLoginUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckUuidValidRequest(TeaModel):
    def __init__(
        self,
        bluetooth: str = None,
        build_id: str = None,
        chip_id: str = None,
        client_id: str = None,
        custom_id: str = None,
        ether_mac: str = None,
        serial_no: str = None,
        uuid: str = None,
        wlan: str = None,
    ):
        self.bluetooth = bluetooth
        self.build_id = build_id
        # This parameter is required.
        self.chip_id = chip_id
        self.client_id = client_id
        # This parameter is required.
        self.custom_id = custom_id
        self.ether_mac = ether_mac
        # This parameter is required.
        self.serial_no = serial_no
        # This parameter is required.
        self.uuid = uuid
        self.wlan = wlan

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bluetooth is not None:
            result['Bluetooth'] = self.bluetooth
        if self.build_id is not None:
            result['BuildId'] = self.build_id
        if self.chip_id is not None:
            result['ChipId'] = self.chip_id
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.custom_id is not None:
            result['CustomId'] = self.custom_id
        if self.ether_mac is not None:
            result['EtherMac'] = self.ether_mac
        if self.serial_no is not None:
            result['SerialNo'] = self.serial_no
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.wlan is not None:
            result['Wlan'] = self.wlan
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bluetooth') is not None:
            self.bluetooth = m.get('Bluetooth')
        if m.get('BuildId') is not None:
            self.build_id = m.get('BuildId')
        if m.get('ChipId') is not None:
            self.chip_id = m.get('ChipId')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('CustomId') is not None:
            self.custom_id = m.get('CustomId')
        if m.get('EtherMac') is not None:
            self.ether_mac = m.get('EtherMac')
        if m.get('SerialNo') is not None:
            self.serial_no = m.get('SerialNo')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('Wlan') is not None:
            self.wlan = m.get('Wlan')
        return self


class CheckUuidValidResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CheckUuidValidResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckUuidValidResponseBody = None,
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
            temp_model = CheckUuidValidResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppOtaTaskRequest(TeaModel):
    def __init__(
        self,
        app_version_uid: str = None,
        channel: str = None,
        client_id_list: List[str] = None,
        client_type: int = None,
        creator: str = None,
        description: str = None,
        force_upgrade: int = None,
        label: str = None,
        name: str = None,
        project: str = None,
        regions: List[str] = None,
        status: int = None,
        task_type: int = None,
        tenant_id: str = None,
    ):
        self.app_version_uid = app_version_uid
        self.channel = channel
        self.client_id_list = client_id_list
        self.client_type = client_type
        self.creator = creator
        self.description = description
        self.force_upgrade = force_upgrade
        self.label = label
        self.name = name
        self.project = project
        self.regions = regions
        self.status = status
        self.task_type = task_type
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version_uid is not None:
            result['AppVersionUid'] = self.app_version_uid
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.client_id_list is not None:
            result['ClientIdList'] = self.client_id_list
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.description is not None:
            result['Description'] = self.description
        if self.force_upgrade is not None:
            result['ForceUpgrade'] = self.force_upgrade
        if self.label is not None:
            result['Label'] = self.label
        if self.name is not None:
            result['Name'] = self.name
        if self.project is not None:
            result['Project'] = self.project
        if self.regions is not None:
            result['Regions'] = self.regions
        if self.status is not None:
            result['Status'] = self.status
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppVersionUid') is not None:
            self.app_version_uid = m.get('AppVersionUid')
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('ClientIdList') is not None:
            self.client_id_list = m.get('ClientIdList')
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ForceUpgrade') is not None:
            self.force_upgrade = m.get('ForceUpgrade')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('Regions') is not None:
            self.regions = m.get('Regions')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class CreateAppOtaTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        task_uid: str = None,
    ):
        self.task_uid = task_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_uid is not None:
            result['TaskUid'] = self.task_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskUid') is not None:
            self.task_uid = m.get('TaskUid')
        return self


class CreateAppOtaTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateAppOtaTaskResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateAppOtaTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAppOtaTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAppOtaTaskResponseBody = None,
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
            temp_model = CreateAppOtaTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppOtaVersionRequest(TeaModel):
    def __init__(
        self,
        app_version: str = None,
        arch: str = None,
        channel: str = None,
        client_type: int = None,
        creator: str = None,
        download_url: str = None,
        md_5: str = None,
        os: str = None,
        os_type: str = None,
        ota_type: int = None,
        project: str = None,
        release_note: str = None,
        release_note_en: str = None,
        release_note_jp: str = None,
        size: int = None,
        snapshot_id: str = None,
        snapshot_region_id: str = None,
        status: int = None,
        version_type: str = None,
    ):
        self.app_version = app_version
        self.arch = arch
        self.channel = channel
        self.client_type = client_type
        self.creator = creator
        self.download_url = download_url
        self.md_5 = md_5
        self.os = os
        self.os_type = os_type
        self.ota_type = ota_type
        self.project = project
        self.release_note = release_note
        self.release_note_en = release_note_en
        self.release_note_jp = release_note_jp
        self.size = size
        self.snapshot_id = snapshot_id
        self.snapshot_region_id = snapshot_region_id
        self.status = status
        self.version_type = version_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.arch is not None:
            result['Arch'] = self.arch
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.os is not None:
            result['Os'] = self.os
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.ota_type is not None:
            result['OtaType'] = self.ota_type
        if self.project is not None:
            result['Project'] = self.project
        if self.release_note is not None:
            result['ReleaseNote'] = self.release_note
        if self.release_note_en is not None:
            result['ReleaseNoteEn'] = self.release_note_en
        if self.release_note_jp is not None:
            result['ReleaseNoteJp'] = self.release_note_jp
        if self.size is not None:
            result['Size'] = self.size
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.snapshot_region_id is not None:
            result['SnapshotRegionId'] = self.snapshot_region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.version_type is not None:
            result['VersionType'] = self.version_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('Arch') is not None:
            self.arch = m.get('Arch')
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('Os') is not None:
            self.os = m.get('Os')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('OtaType') is not None:
            self.ota_type = m.get('OtaType')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('ReleaseNote') is not None:
            self.release_note = m.get('ReleaseNote')
        if m.get('ReleaseNoteEn') is not None:
            self.release_note_en = m.get('ReleaseNoteEn')
        if m.get('ReleaseNoteJp') is not None:
            self.release_note_jp = m.get('ReleaseNoteJp')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('SnapshotRegionId') is not None:
            self.snapshot_region_id = m.get('SnapshotRegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VersionType') is not None:
            self.version_type = m.get('VersionType')
        return self


class CreateAppOtaVersionResponseBodyData(TeaModel):
    def __init__(
        self,
        version_uid: str = None,
    ):
        self.version_uid = version_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version_uid is not None:
            result['VersionUid'] = self.version_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VersionUid') is not None:
            self.version_uid = m.get('VersionUid')
        return self


class CreateAppOtaVersionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateAppOtaVersionResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateAppOtaVersionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAppOtaVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAppOtaVersionResponseBody = None,
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
            temp_model = CreateAppOtaVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAppOtaVersionsRequest(TeaModel):
    def __init__(
        self,
        version_uid_list: List[str] = None,
    ):
        self.version_uid_list = version_uid_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version_uid_list is not None:
            result['VersionUidList'] = self.version_uid_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VersionUidList') is not None:
            self.version_uid_list = m.get('VersionUidList')
        return self


class DeleteAppOtaVersionsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAppOtaVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAppOtaVersionsResponseBody = None,
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
            temp_model = DeleteAppOtaVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDevicesRequest(TeaModel):
    def __init__(
        self,
        force: str = None,
        serial_nos: str = None,
        uuids: str = None,
    ):
        # This parameter is required.
        self.force = force
        self.serial_nos = serial_nos
        self.uuids = uuids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.force is not None:
            result['Force'] = self.force
        if self.serial_nos is not None:
            result['SerialNos'] = self.serial_nos
        if self.uuids is not None:
            result['Uuids'] = self.uuids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Force') is not None:
            self.force = m.get('Force')
        if m.get('SerialNos') is not None:
            self.serial_nos = m.get('SerialNos')
        if m.get('Uuids') is not None:
            self.uuids = m.get('Uuids')
        return self


class DeleteDevicesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDevicesResponseBody = None,
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
            temp_model = DeleteDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLabelRequest(TeaModel):
    def __init__(
        self,
        force: str = None,
        label_content: str = None,
        label_id: str = None,
    ):
        # This parameter is required.
        self.force = force
        self.label_content = label_content
        self.label_id = label_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.force is not None:
            result['Force'] = self.force
        if self.label_content is not None:
            result['LabelContent'] = self.label_content
        if self.label_id is not None:
            result['LabelId'] = self.label_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Force') is not None:
            self.force = m.get('Force')
        if m.get('LabelContent') is not None:
            self.label_content = m.get('LabelContent')
        if m.get('LabelId') is not None:
            self.label_id = m.get('LabelId')
        return self


class DeleteLabelResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteLabelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteLabelResponseBody = None,
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
            temp_model = DeleteLabelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppOtaVersionRequest(TeaModel):
    def __init__(
        self,
        app_version: str = None,
        channel: str = None,
        client_type: int = None,
        creator: str = None,
        project: str = None,
        status: int = None,
        version_uid: str = None,
    ):
        self.app_version = app_version
        self.channel = channel
        self.client_type = client_type
        self.creator = creator
        self.project = project
        self.status = status
        self.version_uid = version_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.project is not None:
            result['Project'] = self.project
        if self.status is not None:
            result['Status'] = self.status
        if self.version_uid is not None:
            result['VersionUid'] = self.version_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VersionUid') is not None:
            self.version_uid = m.get('VersionUid')
        return self


class DescribeAppOtaVersionResponseBodyDataAppOtaInfoDTOList(TeaModel):
    def __init__(
        self,
        app_version: str = None,
        channel: str = None,
        download_url: str = None,
        full_download_url: str = None,
        gmt_create: str = None,
        md_5: str = None,
        os_type: str = None,
        project: str = None,
        protocol_type: str = None,
        release_note: str = None,
        release_note_en: str = None,
        session_type: str = None,
        size: int = None,
        status: int = None,
        version_code: int = None,
        version_type: str = None,
        version_uid: str = None,
    ):
        self.app_version = app_version
        self.channel = channel
        self.download_url = download_url
        self.full_download_url = full_download_url
        self.gmt_create = gmt_create
        self.md_5 = md_5
        self.os_type = os_type
        self.project = project
        self.protocol_type = protocol_type
        self.release_note = release_note
        self.release_note_en = release_note_en
        self.session_type = session_type
        self.size = size
        self.status = status
        self.version_code = version_code
        self.version_type = version_type
        self.version_uid = version_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        if self.full_download_url is not None:
            result['FullDownloadUrl'] = self.full_download_url
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.project is not None:
            result['Project'] = self.project
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.release_note is not None:
            result['ReleaseNote'] = self.release_note
        if self.release_note_en is not None:
            result['ReleaseNoteEn'] = self.release_note_en
        if self.session_type is not None:
            result['SessionType'] = self.session_type
        if self.size is not None:
            result['Size'] = self.size
        if self.status is not None:
            result['Status'] = self.status
        if self.version_code is not None:
            result['VersionCode'] = self.version_code
        if self.version_type is not None:
            result['VersionType'] = self.version_type
        if self.version_uid is not None:
            result['VersionUid'] = self.version_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        if m.get('FullDownloadUrl') is not None:
            self.full_download_url = m.get('FullDownloadUrl')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('ReleaseNote') is not None:
            self.release_note = m.get('ReleaseNote')
        if m.get('ReleaseNoteEn') is not None:
            self.release_note_en = m.get('ReleaseNoteEn')
        if m.get('SessionType') is not None:
            self.session_type = m.get('SessionType')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VersionCode') is not None:
            self.version_code = m.get('VersionCode')
        if m.get('VersionType') is not None:
            self.version_type = m.get('VersionType')
        if m.get('VersionUid') is not None:
            self.version_uid = m.get('VersionUid')
        return self


class DescribeAppOtaVersionResponseBodyData(TeaModel):
    def __init__(
        self,
        app_ota_info_dtolist: List[DescribeAppOtaVersionResponseBodyDataAppOtaInfoDTOList] = None,
    ):
        self.app_ota_info_dtolist = app_ota_info_dtolist

    def validate(self):
        if self.app_ota_info_dtolist:
            for k in self.app_ota_info_dtolist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AppOtaInfoDTOList'] = []
        if self.app_ota_info_dtolist is not None:
            for k in self.app_ota_info_dtolist:
                result['AppOtaInfoDTOList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app_ota_info_dtolist = []
        if m.get('AppOtaInfoDTOList') is not None:
            for k in m.get('AppOtaInfoDTOList'):
                temp_model = DescribeAppOtaVersionResponseBodyDataAppOtaInfoDTOList()
                self.app_ota_info_dtolist.append(temp_model.from_map(k))
        return self


class DescribeAppOtaVersionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeAppOtaVersionResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeAppOtaVersionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAppOtaVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAppOtaVersionResponseBody = None,
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
            temp_model = DescribeAppOtaVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDeviceSeatsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        serial_no: str = None,
        serial_no_list: List[str] = None,
        site_id: str = None,
        tenant_id: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.serial_no = serial_no
        self.serial_no_list = serial_no_list
        self.site_id = site_id
        self.tenant_id = tenant_id

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
        if self.serial_no is not None:
            result['SerialNo'] = self.serial_no
        if self.serial_no_list is not None:
            result['SerialNoList'] = self.serial_no_list
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SerialNo') is not None:
            self.serial_no = m.get('SerialNo')
        if m.get('SerialNoList') is not None:
            self.serial_no_list = m.get('SerialNoList')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class DescribeDeviceSeatsResponseBodyData(TeaModel):
    def __init__(
        self,
        seat_col: int = None,
        seat_name: str = None,
        seat_no: str = None,
        seat_row: int = None,
        serial_no: str = None,
        site_id: str = None,
        site_name: str = None,
    ):
        self.seat_col = seat_col
        self.seat_name = seat_name
        self.seat_no = seat_no
        self.seat_row = seat_row
        self.serial_no = serial_no
        self.site_id = site_id
        self.site_name = site_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.seat_col is not None:
            result['SeatCol'] = self.seat_col
        if self.seat_name is not None:
            result['SeatName'] = self.seat_name
        if self.seat_no is not None:
            result['SeatNo'] = self.seat_no
        if self.seat_row is not None:
            result['SeatRow'] = self.seat_row
        if self.serial_no is not None:
            result['SerialNo'] = self.serial_no
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.site_name is not None:
            result['SiteName'] = self.site_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SeatCol') is not None:
            self.seat_col = m.get('SeatCol')
        if m.get('SeatName') is not None:
            self.seat_name = m.get('SeatName')
        if m.get('SeatNo') is not None:
            self.seat_no = m.get('SeatNo')
        if m.get('SeatRow') is not None:
            self.seat_row = m.get('SeatRow')
        if m.get('SerialNo') is not None:
            self.serial_no = m.get('SerialNo')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('SiteName') is not None:
            self.site_name = m.get('SiteName')
        return self


class DescribeDeviceSeatsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[DescribeDeviceSeatsResponseBodyData] = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeDeviceSeatsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDeviceSeatsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDeviceSeatsResponseBody = None,
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
            temp_model = DescribeDeviceSeatsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDeviceVersionDetailRequest(TeaModel):
    def __init__(
        self,
        model: str = None,
        network_type: str = None,
        region: str = None,
        version_name: str = None,
    ):
        self.model = model
        self.network_type = network_type
        self.region = region
        self.version_name = version_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.model is not None:
            result['Model'] = self.model
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.region is not None:
            result['Region'] = self.region
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class DescribeDeviceVersionDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        android_horizontal_multi_cn_image_download_url: str = None,
        android_horizontal_multi_en_image_download_url: str = None,
        android_vertical_multi_cn_image_download_url: str = None,
        android_vertical_multi_en_image_download_url: str = None,
        channel: str = None,
        client_type: int = None,
        cn_image_download_url: str = None,
        creator: str = None,
        download_url: str = None,
        en_image_download_url: str = None,
        md_5: str = None,
        model: str = None,
        multi_cn_image_download_url: str = None,
        multi_en_image_download_url: str = None,
        release_note: str = None,
        release_note_en: str = None,
        size: int = None,
        version: str = None,
        version_code: str = None,
        version_type: str = None,
    ):
        self.android_horizontal_multi_cn_image_download_url = android_horizontal_multi_cn_image_download_url
        self.android_horizontal_multi_en_image_download_url = android_horizontal_multi_en_image_download_url
        self.android_vertical_multi_cn_image_download_url = android_vertical_multi_cn_image_download_url
        self.android_vertical_multi_en_image_download_url = android_vertical_multi_en_image_download_url
        self.channel = channel
        self.client_type = client_type
        self.cn_image_download_url = cn_image_download_url
        self.creator = creator
        self.download_url = download_url
        self.en_image_download_url = en_image_download_url
        self.md_5 = md_5
        self.model = model
        self.multi_cn_image_download_url = multi_cn_image_download_url
        self.multi_en_image_download_url = multi_en_image_download_url
        self.release_note = release_note
        self.release_note_en = release_note_en
        self.size = size
        self.version = version
        self.version_code = version_code
        self.version_type = version_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_horizontal_multi_cn_image_download_url is not None:
            result['AndroidHorizontalMultiCnImageDownloadUrl'] = self.android_horizontal_multi_cn_image_download_url
        if self.android_horizontal_multi_en_image_download_url is not None:
            result['AndroidHorizontalMultiEnImageDownloadUrl'] = self.android_horizontal_multi_en_image_download_url
        if self.android_vertical_multi_cn_image_download_url is not None:
            result['AndroidVerticalMultiCnImageDownloadUrl'] = self.android_vertical_multi_cn_image_download_url
        if self.android_vertical_multi_en_image_download_url is not None:
            result['AndroidVerticalMultiEnImageDownloadUrl'] = self.android_vertical_multi_en_image_download_url
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        if self.cn_image_download_url is not None:
            result['CnImageDownloadUrl'] = self.cn_image_download_url
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        if self.en_image_download_url is not None:
            result['EnImageDownloadUrl'] = self.en_image_download_url
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.model is not None:
            result['Model'] = self.model
        if self.multi_cn_image_download_url is not None:
            result['MultiCnImageDownloadUrl'] = self.multi_cn_image_download_url
        if self.multi_en_image_download_url is not None:
            result['MultiEnImageDownloadUrl'] = self.multi_en_image_download_url
        if self.release_note is not None:
            result['ReleaseNote'] = self.release_note
        if self.release_note_en is not None:
            result['ReleaseNoteEn'] = self.release_note_en
        if self.size is not None:
            result['Size'] = self.size
        if self.version is not None:
            result['Version'] = self.version
        if self.version_code is not None:
            result['VersionCode'] = self.version_code
        if self.version_type is not None:
            result['VersionType'] = self.version_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidHorizontalMultiCnImageDownloadUrl') is not None:
            self.android_horizontal_multi_cn_image_download_url = m.get('AndroidHorizontalMultiCnImageDownloadUrl')
        if m.get('AndroidHorizontalMultiEnImageDownloadUrl') is not None:
            self.android_horizontal_multi_en_image_download_url = m.get('AndroidHorizontalMultiEnImageDownloadUrl')
        if m.get('AndroidVerticalMultiCnImageDownloadUrl') is not None:
            self.android_vertical_multi_cn_image_download_url = m.get('AndroidVerticalMultiCnImageDownloadUrl')
        if m.get('AndroidVerticalMultiEnImageDownloadUrl') is not None:
            self.android_vertical_multi_en_image_download_url = m.get('AndroidVerticalMultiEnImageDownloadUrl')
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        if m.get('CnImageDownloadUrl') is not None:
            self.cn_image_download_url = m.get('CnImageDownloadUrl')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        if m.get('EnImageDownloadUrl') is not None:
            self.en_image_download_url = m.get('EnImageDownloadUrl')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('MultiCnImageDownloadUrl') is not None:
            self.multi_cn_image_download_url = m.get('MultiCnImageDownloadUrl')
        if m.get('MultiEnImageDownloadUrl') is not None:
            self.multi_en_image_download_url = m.get('MultiEnImageDownloadUrl')
        if m.get('ReleaseNote') is not None:
            self.release_note = m.get('ReleaseNote')
        if m.get('ReleaseNoteEn') is not None:
            self.release_note_en = m.get('ReleaseNoteEn')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('VersionCode') is not None:
            self.version_code = m.get('VersionCode')
        if m.get('VersionType') is not None:
            self.version_type = m.get('VersionType')
        return self


class DescribeDeviceVersionDetailResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[DescribeDeviceVersionDetailResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeDeviceVersionDetailResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDeviceVersionDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDeviceVersionDetailResponseBody = None,
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
            temp_model = DescribeDeviceVersionDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSnLabelCountsRequest(TeaModel):
    def __init__(
        self,
        label_list: List[str] = None,
        tenant_id: str = None,
        zone_id: str = None,
        zone_name: str = None,
    ):
        self.label_list = label_list
        self.tenant_id = tenant_id
        self.zone_id = zone_id
        self.zone_name = zone_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_list is not None:
            result['LabelList'] = self.label_list
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.zone_name is not None:
            result['ZoneName'] = self.zone_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LabelList') is not None:
            self.label_list = m.get('LabelList')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('ZoneName') is not None:
            self.zone_name = m.get('ZoneName')
        return self


class DescribeSnLabelCountsResponseBodyDataLabelCountDTOList(TeaModel):
    def __init__(
        self,
        count: str = None,
        label: str = None,
    ):
        self.count = count
        self.label = label

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class DescribeSnLabelCountsResponseBodyData(TeaModel):
    def __init__(
        self,
        label_count_dtolist: List[DescribeSnLabelCountsResponseBodyDataLabelCountDTOList] = None,
        total_count: int = None,
    ):
        self.label_count_dtolist = label_count_dtolist
        self.total_count = total_count

    def validate(self):
        if self.label_count_dtolist:
            for k in self.label_count_dtolist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LabelCountDTOList'] = []
        if self.label_count_dtolist is not None:
            for k in self.label_count_dtolist:
                result['LabelCountDTOList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.label_count_dtolist = []
        if m.get('LabelCountDTOList') is not None:
            for k in m.get('LabelCountDTOList'):
                temp_model = DescribeSnLabelCountsResponseBodyDataLabelCountDTOList()
                self.label_count_dtolist.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeSnLabelCountsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeSnLabelCountsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeSnLabelCountsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeSnLabelCountsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSnLabelCountsResponseBody = None,
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
            temp_model = DescribeSnLabelCountsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWorkZonesRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        tenant_id: str = None,
        zone_id_list: List[str] = None,
        zone_name_list: List[str] = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.tenant_id = tenant_id
        self.zone_id_list = zone_id_list
        self.zone_name_list = zone_name_list

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
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.zone_id_list is not None:
            result['ZoneIdList'] = self.zone_id_list
        if self.zone_name_list is not None:
            result['ZoneNameList'] = self.zone_name_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('ZoneIdList') is not None:
            self.zone_id_list = m.get('ZoneIdList')
        if m.get('ZoneNameList') is not None:
            self.zone_name_list = m.get('ZoneNameList')
        return self


class DescribeWorkZonesResponseBodyDataWorkZoneDTOList(TeaModel):
    def __init__(
        self,
        seat_col: int = None,
        seat_row: int = None,
        tenant_id: str = None,
        zone_id: str = None,
        zone_name: str = None,
    ):
        self.seat_col = seat_col
        self.seat_row = seat_row
        self.tenant_id = tenant_id
        self.zone_id = zone_id
        self.zone_name = zone_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.seat_col is not None:
            result['SeatCol'] = self.seat_col
        if self.seat_row is not None:
            result['SeatRow'] = self.seat_row
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.zone_name is not None:
            result['ZoneName'] = self.zone_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SeatCol') is not None:
            self.seat_col = m.get('SeatCol')
        if m.get('SeatRow') is not None:
            self.seat_row = m.get('SeatRow')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('ZoneName') is not None:
            self.zone_name = m.get('ZoneName')
        return self


class DescribeWorkZonesResponseBodyData(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        work_zone_dtolist: List[DescribeWorkZonesResponseBodyDataWorkZoneDTOList] = None,
    ):
        self.total_count = total_count
        self.work_zone_dtolist = work_zone_dtolist

    def validate(self):
        if self.work_zone_dtolist:
            for k in self.work_zone_dtolist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['WorkZoneDTOList'] = []
        if self.work_zone_dtolist is not None:
            for k in self.work_zone_dtolist:
                result['WorkZoneDTOList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.work_zone_dtolist = []
        if m.get('WorkZoneDTOList') is not None:
            for k in m.get('WorkZoneDTOList'):
                temp_model = DescribeWorkZonesResponseBodyDataWorkZoneDTOList()
                self.work_zone_dtolist.append(temp_model.from_map(k))
        return self


class DescribeWorkZonesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeWorkZonesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeWorkZonesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeWorkZonesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeWorkZonesResponseBody = None,
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
            temp_model = DescribeWorkZonesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachEndUsersRequest(TeaModel):
    def __init__(
        self,
        end_user_ids: str = None,
        serial_no: str = None,
    ):
        # This parameter is required.
        self.end_user_ids = end_user_ids
        # This parameter is required.
        self.serial_no = serial_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_user_ids is not None:
            result['EndUserIds'] = self.end_user_ids
        if self.serial_no is not None:
            result['SerialNo'] = self.serial_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndUserIds') is not None:
            self.end_user_ids = m.get('EndUserIds')
        if m.get('SerialNo') is not None:
            self.serial_no = m.get('SerialNo')
        return self


class DetachEndUsersResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetachEndUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetachEndUsersResponseBody = None,
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
            temp_model = DetachEndUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachLabelRequest(TeaModel):
    def __init__(
        self,
        label_content: str = None,
        label_id: str = None,
        serial_no: str = None,
    ):
        self.label_content = label_content
        self.label_id = label_id
        # This parameter is required.
        self.serial_no = serial_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_content is not None:
            result['LabelContent'] = self.label_content
        if self.label_id is not None:
            result['LabelId'] = self.label_id
        if self.serial_no is not None:
            result['SerialNo'] = self.serial_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LabelContent') is not None:
            self.label_content = m.get('LabelContent')
        if m.get('LabelId') is not None:
            self.label_id = m.get('LabelId')
        if m.get('SerialNo') is not None:
            self.serial_no = m.get('SerialNo')
        return self


class DetachLabelResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetachLabelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetachLabelResponseBody = None,
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
            temp_model = DetachLabelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachLabelsRequest(TeaModel):
    def __init__(
        self,
        label_ids: str = None,
        serial_no: str = None,
        serial_no_list: str = None,
    ):
        self.label_ids = label_ids
        self.serial_no = serial_no
        self.serial_no_list = serial_no_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_ids is not None:
            result['LabelIds'] = self.label_ids
        if self.serial_no is not None:
            result['SerialNo'] = self.serial_no
        if self.serial_no_list is not None:
            result['SerialNoList'] = self.serial_no_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LabelIds') is not None:
            self.label_ids = m.get('LabelIds')
        if m.get('SerialNo') is not None:
            self.serial_no = m.get('SerialNo')
        if m.get('SerialNoList') is not None:
            self.serial_no_list = m.get('SerialNoList')
        return self


class DetachLabelsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetachLabelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetachLabelsResponseBody = None,
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
            temp_model = DetachLabelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateOssUrlRequest(TeaModel):
    def __init__(
        self,
        object_name_list: List[str] = None,
        session_id: str = None,
    ):
        self.object_name_list = object_name_list
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.object_name_list is not None:
            result['ObjectNameList'] = self.object_name_list
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ObjectNameList') is not None:
            self.object_name_list = m.get('ObjectNameList')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class GenerateOssUrlResponseBodyData(TeaModel):
    def __init__(
        self,
        download_url: str = None,
        object_name: str = None,
    ):
        self.download_url = download_url
        self.object_name = object_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        if self.object_name is not None:
            result['ObjectName'] = self.object_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        if m.get('ObjectName') is not None:
            self.object_name = m.get('ObjectName')
        return self


class GenerateOssUrlResponseBody(TeaModel):
    def __init__(
        self,
        data: List[GenerateOssUrlResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GenerateOssUrlResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GenerateOssUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateOssUrlResponseBody = None,
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
            temp_model = GenerateOssUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAppOtaLatestVersionRequest(TeaModel):
    def __init__(
        self,
        base_version: str = None,
        client_type: int = None,
        client_uid: str = None,
        os_type: str = None,
        project: str = None,
    ):
        # This parameter is required.
        self.base_version = base_version
        self.client_type = client_type
        self.client_uid = client_uid
        # This parameter is required.
        self.os_type = os_type
        self.project = project

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_version is not None:
            result['BaseVersion'] = self.base_version
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        if self.client_uid is not None:
            result['ClientUid'] = self.client_uid
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.project is not None:
            result['Project'] = self.project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseVersion') is not None:
            self.base_version = m.get('BaseVersion')
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        if m.get('ClientUid') is not None:
            self.client_uid = m.get('ClientUid')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        return self


class GetAppOtaLatestVersionResponseBodyData(TeaModel):
    def __init__(
        self,
        app_version: str = None,
        download_url: str = None,
        force_upgrade: int = None,
        md_5: str = None,
        release_note: str = None,
        size: int = None,
        task_uid: str = None,
        version_code: str = None,
        version_type: str = None,
    ):
        self.app_version = app_version
        self.download_url = download_url
        self.force_upgrade = force_upgrade
        self.md_5 = md_5
        self.release_note = release_note
        self.size = size
        self.task_uid = task_uid
        self.version_code = version_code
        self.version_type = version_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        if self.force_upgrade is not None:
            result['ForceUpgrade'] = self.force_upgrade
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.release_note is not None:
            result['ReleaseNote'] = self.release_note
        if self.size is not None:
            result['Size'] = self.size
        if self.task_uid is not None:
            result['TaskUid'] = self.task_uid
        if self.version_code is not None:
            result['VersionCode'] = self.version_code
        if self.version_type is not None:
            result['VersionType'] = self.version_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        if m.get('ForceUpgrade') is not None:
            self.force_upgrade = m.get('ForceUpgrade')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('ReleaseNote') is not None:
            self.release_note = m.get('ReleaseNote')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('TaskUid') is not None:
            self.task_uid = m.get('TaskUid')
        if m.get('VersionCode') is not None:
            self.version_code = m.get('VersionCode')
        if m.get('VersionType') is not None:
            self.version_type = m.get('VersionType')
        return self


class GetAppOtaLatestVersionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetAppOtaLatestVersionResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetAppOtaLatestVersionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAppOtaLatestVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAppOtaLatestVersionResponseBody = None,
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
            temp_model = GetAppOtaLatestVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDeviceConfigsRequest(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        network_type: str = None,
        region: str = None,
        serial_no: str = None,
        urcl_version: str = None,
        user_custom_id: str = None,
    ):
        self.device_id = device_id
        self.network_type = network_type
        self.region = region
        self.serial_no = serial_no
        self.urcl_version = urcl_version
        self.user_custom_id = user_custom_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.region is not None:
            result['Region'] = self.region
        if self.serial_no is not None:
            result['SerialNo'] = self.serial_no
        if self.urcl_version is not None:
            result['UrclVersion'] = self.urcl_version
        if self.user_custom_id is not None:
            result['UserCustomId'] = self.user_custom_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('SerialNo') is not None:
            self.serial_no = m.get('SerialNo')
        if m.get('UrclVersion') is not None:
            self.urcl_version = m.get('UrclVersion')
        if m.get('UserCustomId') is not None:
            self.user_custom_id = m.get('UserCustomId')
        return self


class GetDeviceConfigsResponseBodyDataCustomResourcePackage(TeaModel):
    def __init__(
        self,
        config_about_logo: str = None,
        desktop_wallpaper: str = None,
        login_page_background: str = None,
        login_page_logo: str = None,
        personal_center_logo: str = None,
        start_logo: str = None,
        start_menu_logo: str = None,
        upgrade_logo: str = None,
    ):
        self.config_about_logo = config_about_logo
        self.desktop_wallpaper = desktop_wallpaper
        self.login_page_background = login_page_background
        self.login_page_logo = login_page_logo
        self.personal_center_logo = personal_center_logo
        self.start_logo = start_logo
        self.start_menu_logo = start_menu_logo
        self.upgrade_logo = upgrade_logo

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_about_logo is not None:
            result['ConfigAboutLogo'] = self.config_about_logo
        if self.desktop_wallpaper is not None:
            result['DesktopWallpaper'] = self.desktop_wallpaper
        if self.login_page_background is not None:
            result['LoginPageBackground'] = self.login_page_background
        if self.login_page_logo is not None:
            result['LoginPageLogo'] = self.login_page_logo
        if self.personal_center_logo is not None:
            result['PersonalCenterLogo'] = self.personal_center_logo
        if self.start_logo is not None:
            result['StartLogo'] = self.start_logo
        if self.start_menu_logo is not None:
            result['StartMenuLogo'] = self.start_menu_logo
        if self.upgrade_logo is not None:
            result['UpgradeLogo'] = self.upgrade_logo
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigAboutLogo') is not None:
            self.config_about_logo = m.get('ConfigAboutLogo')
        if m.get('DesktopWallpaper') is not None:
            self.desktop_wallpaper = m.get('DesktopWallpaper')
        if m.get('LoginPageBackground') is not None:
            self.login_page_background = m.get('LoginPageBackground')
        if m.get('LoginPageLogo') is not None:
            self.login_page_logo = m.get('LoginPageLogo')
        if m.get('PersonalCenterLogo') is not None:
            self.personal_center_logo = m.get('PersonalCenterLogo')
        if m.get('StartLogo') is not None:
            self.start_logo = m.get('StartLogo')
        if m.get('StartMenuLogo') is not None:
            self.start_menu_logo = m.get('StartMenuLogo')
        if m.get('UpgradeLogo') is not None:
            self.upgrade_logo = m.get('UpgradeLogo')
        return self


class GetDeviceConfigsResponseBodyData(TeaModel):
    def __init__(
        self,
        auto_lock_screen_time: int = None,
        auto_login: int = None,
        auto_update: int = None,
        custom_idle_action: int = None,
        custom_power_on: int = None,
        custom_resource_package: GetDeviceConfigsResponseBodyDataCustomResourcePackage = None,
        define_power_button: int = None,
        device_lock: int = None,
        display_layout: str = None,
        display_resolution: str = None,
        display_scale_ratio: str = None,
        enable_adb: int = None,
        enable_auto_lock_screen: int = None,
        enable_bluetooth: int = None,
        enable_lock_screen_password: int = None,
        enable_modify_password: int = None,
        enable_scheduled_power_off: int = None,
        enable_unlock_password: int = None,
        enable_wlan: int = None,
        idle_time: int = None,
        local_usb_print: int = None,
        lock_password: str = None,
        scheduled_power_off: str = None,
        secure_network_type: str = None,
        serial_no: str = None,
        sleep_time: int = None,
        urcl: str = None,
        usb_storage: int = None,
        user_custom_id: str = None,
        uuid: str = None,
    ):
        self.auto_lock_screen_time = auto_lock_screen_time
        self.auto_login = auto_login
        self.auto_update = auto_update
        self.custom_idle_action = custom_idle_action
        self.custom_power_on = custom_power_on
        self.custom_resource_package = custom_resource_package
        self.define_power_button = define_power_button
        self.device_lock = device_lock
        self.display_layout = display_layout
        self.display_resolution = display_resolution
        self.display_scale_ratio = display_scale_ratio
        self.enable_adb = enable_adb
        self.enable_auto_lock_screen = enable_auto_lock_screen
        self.enable_bluetooth = enable_bluetooth
        self.enable_lock_screen_password = enable_lock_screen_password
        self.enable_modify_password = enable_modify_password
        self.enable_scheduled_power_off = enable_scheduled_power_off
        self.enable_unlock_password = enable_unlock_password
        self.enable_wlan = enable_wlan
        self.idle_time = idle_time
        self.local_usb_print = local_usb_print
        self.lock_password = lock_password
        self.scheduled_power_off = scheduled_power_off
        self.secure_network_type = secure_network_type
        self.serial_no = serial_no
        self.sleep_time = sleep_time
        self.urcl = urcl
        self.usb_storage = usb_storage
        self.user_custom_id = user_custom_id
        self.uuid = uuid

    def validate(self):
        if self.custom_resource_package:
            self.custom_resource_package.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_lock_screen_time is not None:
            result['AutoLockScreenTime'] = self.auto_lock_screen_time
        if self.auto_login is not None:
            result['AutoLogin'] = self.auto_login
        if self.auto_update is not None:
            result['AutoUpdate'] = self.auto_update
        if self.custom_idle_action is not None:
            result['CustomIdleAction'] = self.custom_idle_action
        if self.custom_power_on is not None:
            result['CustomPowerOn'] = self.custom_power_on
        if self.custom_resource_package is not None:
            result['CustomResourcePackage'] = self.custom_resource_package.to_map()
        if self.define_power_button is not None:
            result['DefinePowerButton'] = self.define_power_button
        if self.device_lock is not None:
            result['DeviceLock'] = self.device_lock
        if self.display_layout is not None:
            result['DisplayLayout'] = self.display_layout
        if self.display_resolution is not None:
            result['DisplayResolution'] = self.display_resolution
        if self.display_scale_ratio is not None:
            result['DisplayScaleRatio'] = self.display_scale_ratio
        if self.enable_adb is not None:
            result['EnableAdb'] = self.enable_adb
        if self.enable_auto_lock_screen is not None:
            result['EnableAutoLockScreen'] = self.enable_auto_lock_screen
        if self.enable_bluetooth is not None:
            result['EnableBluetooth'] = self.enable_bluetooth
        if self.enable_lock_screen_password is not None:
            result['EnableLockScreenPassword'] = self.enable_lock_screen_password
        if self.enable_modify_password is not None:
            result['EnableModifyPassword'] = self.enable_modify_password
        if self.enable_scheduled_power_off is not None:
            result['EnableScheduledPowerOff'] = self.enable_scheduled_power_off
        if self.enable_unlock_password is not None:
            result['EnableUnlockPassword'] = self.enable_unlock_password
        if self.enable_wlan is not None:
            result['EnableWlan'] = self.enable_wlan
        if self.idle_time is not None:
            result['IdleTime'] = self.idle_time
        if self.local_usb_print is not None:
            result['LocalUsbPrint'] = self.local_usb_print
        if self.lock_password is not None:
            result['LockPassword'] = self.lock_password
        if self.scheduled_power_off is not None:
            result['ScheduledPowerOff'] = self.scheduled_power_off
        if self.secure_network_type is not None:
            result['SecureNetworkType'] = self.secure_network_type
        if self.serial_no is not None:
            result['SerialNo'] = self.serial_no
        if self.sleep_time is not None:
            result['SleepTime'] = self.sleep_time
        if self.urcl is not None:
            result['Urcl'] = self.urcl
        if self.usb_storage is not None:
            result['UsbStorage'] = self.usb_storage
        if self.user_custom_id is not None:
            result['UserCustomId'] = self.user_custom_id
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoLockScreenTime') is not None:
            self.auto_lock_screen_time = m.get('AutoLockScreenTime')
        if m.get('AutoLogin') is not None:
            self.auto_login = m.get('AutoLogin')
        if m.get('AutoUpdate') is not None:
            self.auto_update = m.get('AutoUpdate')
        if m.get('CustomIdleAction') is not None:
            self.custom_idle_action = m.get('CustomIdleAction')
        if m.get('CustomPowerOn') is not None:
            self.custom_power_on = m.get('CustomPowerOn')
        if m.get('CustomResourcePackage') is not None:
            temp_model = GetDeviceConfigsResponseBodyDataCustomResourcePackage()
            self.custom_resource_package = temp_model.from_map(m['CustomResourcePackage'])
        if m.get('DefinePowerButton') is not None:
            self.define_power_button = m.get('DefinePowerButton')
        if m.get('DeviceLock') is not None:
            self.device_lock = m.get('DeviceLock')
        if m.get('DisplayLayout') is not None:
            self.display_layout = m.get('DisplayLayout')
        if m.get('DisplayResolution') is not None:
            self.display_resolution = m.get('DisplayResolution')
        if m.get('DisplayScaleRatio') is not None:
            self.display_scale_ratio = m.get('DisplayScaleRatio')
        if m.get('EnableAdb') is not None:
            self.enable_adb = m.get('EnableAdb')
        if m.get('EnableAutoLockScreen') is not None:
            self.enable_auto_lock_screen = m.get('EnableAutoLockScreen')
        if m.get('EnableBluetooth') is not None:
            self.enable_bluetooth = m.get('EnableBluetooth')
        if m.get('EnableLockScreenPassword') is not None:
            self.enable_lock_screen_password = m.get('EnableLockScreenPassword')
        if m.get('EnableModifyPassword') is not None:
            self.enable_modify_password = m.get('EnableModifyPassword')
        if m.get('EnableScheduledPowerOff') is not None:
            self.enable_scheduled_power_off = m.get('EnableScheduledPowerOff')
        if m.get('EnableUnlockPassword') is not None:
            self.enable_unlock_password = m.get('EnableUnlockPassword')
        if m.get('EnableWlan') is not None:
            self.enable_wlan = m.get('EnableWlan')
        if m.get('IdleTime') is not None:
            self.idle_time = m.get('IdleTime')
        if m.get('LocalUsbPrint') is not None:
            self.local_usb_print = m.get('LocalUsbPrint')
        if m.get('LockPassword') is not None:
            self.lock_password = m.get('LockPassword')
        if m.get('ScheduledPowerOff') is not None:
            self.scheduled_power_off = m.get('ScheduledPowerOff')
        if m.get('SecureNetworkType') is not None:
            self.secure_network_type = m.get('SecureNetworkType')
        if m.get('SerialNo') is not None:
            self.serial_no = m.get('SerialNo')
        if m.get('SleepTime') is not None:
            self.sleep_time = m.get('SleepTime')
        if m.get('Urcl') is not None:
            self.urcl = m.get('Urcl')
        if m.get('UsbStorage') is not None:
            self.usb_storage = m.get('UsbStorage')
        if m.get('UserCustomId') is not None:
            self.user_custom_id = m.get('UserCustomId')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class GetDeviceConfigsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetDeviceConfigsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetDeviceConfigsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDeviceConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDeviceConfigsResponseBody = None,
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
            temp_model = GetDeviceConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDeviceOtaAutoStatusRequest(TeaModel):
    def __init__(
        self,
        client_type: int = None,
    ):
        self.client_type = client_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        return self


class GetDeviceOtaAutoStatusResponseBodyData(TeaModel):
    def __init__(
        self,
        auto_update: int = None,
        auto_update_time_schedule: str = None,
        force_upgrade: int = None,
        status: int = None,
    ):
        self.auto_update = auto_update
        self.auto_update_time_schedule = auto_update_time_schedule
        self.force_upgrade = force_upgrade
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_update is not None:
            result['AutoUpdate'] = self.auto_update
        if self.auto_update_time_schedule is not None:
            result['AutoUpdateTimeSchedule'] = self.auto_update_time_schedule
        if self.force_upgrade is not None:
            result['ForceUpgrade'] = self.force_upgrade
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoUpdate') is not None:
            self.auto_update = m.get('AutoUpdate')
        if m.get('AutoUpdateTimeSchedule') is not None:
            self.auto_update_time_schedule = m.get('AutoUpdateTimeSchedule')
        if m.get('ForceUpgrade') is not None:
            self.force_upgrade = m.get('ForceUpgrade')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetDeviceOtaAutoStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetDeviceOtaAutoStatusResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetDeviceOtaAutoStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDeviceOtaAutoStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDeviceOtaAutoStatusResponseBody = None,
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
            temp_model = GetDeviceOtaAutoStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDeviceOtaInfoRequest(TeaModel):
    def __init__(
        self,
        base_version: str = None,
        channel: str = None,
        device_id: str = None,
        model: str = None,
        network_type: str = None,
        os_version: str = None,
        region: str = None,
        region_id: str = None,
        target_version_type: str = None,
        tenant_id: str = None,
    ):
        # This parameter is required.
        self.base_version = base_version
        self.channel = channel
        # This parameter is required.
        self.device_id = device_id
        # This parameter is required.
        self.model = model
        self.network_type = network_type
        self.os_version = os_version
        self.region = region
        self.region_id = region_id
        self.target_version_type = target_version_type
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_version is not None:
            result['BaseVersion'] = self.base_version
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.model is not None:
            result['Model'] = self.model
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.os_version is not None:
            result['OsVersion'] = self.os_version
        if self.region is not None:
            result['Region'] = self.region
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.target_version_type is not None:
            result['TargetVersionType'] = self.target_version_type
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseVersion') is not None:
            self.base_version = m.get('BaseVersion')
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('OsVersion') is not None:
            self.os_version = m.get('OsVersion')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TargetVersionType') is not None:
            self.target_version_type = m.get('TargetVersionType')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class GetDeviceOtaInfoResponseBodyDataVersion(TeaModel):
    def __init__(
        self,
        android_horizontal_multi_cn_image_download_url: str = None,
        android_horizontal_multi_en_image_download_url: str = None,
        android_vertical_multi_cn_image_download_url: str = None,
        android_vertical_multi_en_image_download_url: str = None,
        cn_image_download_url: str = None,
        creator: str = None,
        custom_force_upgrade: bool = None,
        download_url: str = None,
        en_image_download_url: str = None,
        force_upgrade: int = None,
        is_app_download_url: bool = None,
        local_download_url: str = None,
        md_5: str = None,
        model: str = None,
        multi_cn_image_download_url: str = None,
        multi_en_image_download_url: str = None,
        release_note: str = None,
        release_note_en: str = None,
        size: int = None,
        version: str = None,
        version_code: str = None,
        version_type: str = None,
    ):
        self.android_horizontal_multi_cn_image_download_url = android_horizontal_multi_cn_image_download_url
        self.android_horizontal_multi_en_image_download_url = android_horizontal_multi_en_image_download_url
        self.android_vertical_multi_cn_image_download_url = android_vertical_multi_cn_image_download_url
        self.android_vertical_multi_en_image_download_url = android_vertical_multi_en_image_download_url
        self.cn_image_download_url = cn_image_download_url
        self.creator = creator
        self.custom_force_upgrade = custom_force_upgrade
        self.download_url = download_url
        self.en_image_download_url = en_image_download_url
        self.force_upgrade = force_upgrade
        self.is_app_download_url = is_app_download_url
        self.local_download_url = local_download_url
        self.md_5 = md_5
        self.model = model
        self.multi_cn_image_download_url = multi_cn_image_download_url
        self.multi_en_image_download_url = multi_en_image_download_url
        self.release_note = release_note
        self.release_note_en = release_note_en
        self.size = size
        self.version = version
        self.version_code = version_code
        self.version_type = version_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_horizontal_multi_cn_image_download_url is not None:
            result['AndroidHorizontalMultiCnImageDownloadUrl'] = self.android_horizontal_multi_cn_image_download_url
        if self.android_horizontal_multi_en_image_download_url is not None:
            result['AndroidHorizontalMultiEnImageDownloadUrl'] = self.android_horizontal_multi_en_image_download_url
        if self.android_vertical_multi_cn_image_download_url is not None:
            result['AndroidVerticalMultiCnImageDownloadUrl'] = self.android_vertical_multi_cn_image_download_url
        if self.android_vertical_multi_en_image_download_url is not None:
            result['AndroidVerticalMultiEnImageDownloadUrl'] = self.android_vertical_multi_en_image_download_url
        if self.cn_image_download_url is not None:
            result['CnImageDownloadUrl'] = self.cn_image_download_url
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.custom_force_upgrade is not None:
            result['CustomForceUpgrade'] = self.custom_force_upgrade
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        if self.en_image_download_url is not None:
            result['EnImageDownloadUrl'] = self.en_image_download_url
        if self.force_upgrade is not None:
            result['ForceUpgrade'] = self.force_upgrade
        if self.is_app_download_url is not None:
            result['IsAppDownloadUrl'] = self.is_app_download_url
        if self.local_download_url is not None:
            result['LocalDownloadUrl'] = self.local_download_url
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.model is not None:
            result['Model'] = self.model
        if self.multi_cn_image_download_url is not None:
            result['MultiCnImageDownloadUrl'] = self.multi_cn_image_download_url
        if self.multi_en_image_download_url is not None:
            result['MultiEnImageDownloadUrl'] = self.multi_en_image_download_url
        if self.release_note is not None:
            result['ReleaseNote'] = self.release_note
        if self.release_note_en is not None:
            result['ReleaseNoteEn'] = self.release_note_en
        if self.size is not None:
            result['Size'] = self.size
        if self.version is not None:
            result['Version'] = self.version
        if self.version_code is not None:
            result['VersionCode'] = self.version_code
        if self.version_type is not None:
            result['VersionType'] = self.version_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidHorizontalMultiCnImageDownloadUrl') is not None:
            self.android_horizontal_multi_cn_image_download_url = m.get('AndroidHorizontalMultiCnImageDownloadUrl')
        if m.get('AndroidHorizontalMultiEnImageDownloadUrl') is not None:
            self.android_horizontal_multi_en_image_download_url = m.get('AndroidHorizontalMultiEnImageDownloadUrl')
        if m.get('AndroidVerticalMultiCnImageDownloadUrl') is not None:
            self.android_vertical_multi_cn_image_download_url = m.get('AndroidVerticalMultiCnImageDownloadUrl')
        if m.get('AndroidVerticalMultiEnImageDownloadUrl') is not None:
            self.android_vertical_multi_en_image_download_url = m.get('AndroidVerticalMultiEnImageDownloadUrl')
        if m.get('CnImageDownloadUrl') is not None:
            self.cn_image_download_url = m.get('CnImageDownloadUrl')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('CustomForceUpgrade') is not None:
            self.custom_force_upgrade = m.get('CustomForceUpgrade')
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        if m.get('EnImageDownloadUrl') is not None:
            self.en_image_download_url = m.get('EnImageDownloadUrl')
        if m.get('ForceUpgrade') is not None:
            self.force_upgrade = m.get('ForceUpgrade')
        if m.get('IsAppDownloadUrl') is not None:
            self.is_app_download_url = m.get('IsAppDownloadUrl')
        if m.get('LocalDownloadUrl') is not None:
            self.local_download_url = m.get('LocalDownloadUrl')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('MultiCnImageDownloadUrl') is not None:
            self.multi_cn_image_download_url = m.get('MultiCnImageDownloadUrl')
        if m.get('MultiEnImageDownloadUrl') is not None:
            self.multi_en_image_download_url = m.get('MultiEnImageDownloadUrl')
        if m.get('ReleaseNote') is not None:
            self.release_note = m.get('ReleaseNote')
        if m.get('ReleaseNoteEn') is not None:
            self.release_note_en = m.get('ReleaseNoteEn')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('VersionCode') is not None:
            self.version_code = m.get('VersionCode')
        if m.get('VersionType') is not None:
            self.version_type = m.get('VersionType')
        return self


class GetDeviceOtaInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        version: GetDeviceOtaInfoResponseBodyDataVersion = None,
    ):
        self.version = version

    def validate(self):
        if self.version:
            self.version.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version is not None:
            result['Version'] = self.version.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            temp_model = GetDeviceOtaInfoResponseBodyDataVersion()
            self.version = temp_model.from_map(m['Version'])
        return self


class GetDeviceOtaInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetDeviceOtaInfoResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetDeviceOtaInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDeviceOtaInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDeviceOtaInfoResponseBody = None,
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
            temp_model = GetDeviceOtaInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDeviceOtaInfoTestRequest(TeaModel):
    def __init__(
        self,
        base_version: str = None,
        device_id: str = None,
        model: str = None,
        tenant_id: str = None,
    ):
        # This parameter is required.
        self.base_version = base_version
        # This parameter is required.
        self.device_id = device_id
        # This parameter is required.
        self.model = model
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_version is not None:
            result['BaseVersion'] = self.base_version
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.model is not None:
            result['Model'] = self.model
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseVersion') is not None:
            self.base_version = m.get('BaseVersion')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class GetDeviceOtaInfoTestResponseBodyDataVersion(TeaModel):
    def __init__(
        self,
        creator: str = None,
        download_url: str = None,
        force_upgrade: int = None,
        local_download_url: str = None,
        md_5: str = None,
        model: str = None,
        release_note: str = None,
        size: int = None,
        version: str = None,
        version_code: str = None,
        version_type: str = None,
    ):
        self.creator = creator
        self.download_url = download_url
        self.force_upgrade = force_upgrade
        self.local_download_url = local_download_url
        self.md_5 = md_5
        self.model = model
        self.release_note = release_note
        self.size = size
        self.version = version
        self.version_code = version_code
        self.version_type = version_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        if self.force_upgrade is not None:
            result['ForceUpgrade'] = self.force_upgrade
        if self.local_download_url is not None:
            result['LocalDownloadUrl'] = self.local_download_url
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.model is not None:
            result['Model'] = self.model
        if self.release_note is not None:
            result['ReleaseNote'] = self.release_note
        if self.size is not None:
            result['Size'] = self.size
        if self.version is not None:
            result['Version'] = self.version
        if self.version_code is not None:
            result['VersionCode'] = self.version_code
        if self.version_type is not None:
            result['VersionType'] = self.version_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        if m.get('ForceUpgrade') is not None:
            self.force_upgrade = m.get('ForceUpgrade')
        if m.get('LocalDownloadUrl') is not None:
            self.local_download_url = m.get('LocalDownloadUrl')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('ReleaseNote') is not None:
            self.release_note = m.get('ReleaseNote')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('VersionCode') is not None:
            self.version_code = m.get('VersionCode')
        if m.get('VersionType') is not None:
            self.version_type = m.get('VersionType')
        return self


class GetDeviceOtaInfoTestResponseBodyData(TeaModel):
    def __init__(
        self,
        version: GetDeviceOtaInfoTestResponseBodyDataVersion = None,
    ):
        self.version = version

    def validate(self):
        if self.version:
            self.version.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version is not None:
            result['Version'] = self.version.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            temp_model = GetDeviceOtaInfoTestResponseBodyDataVersion()
            self.version = temp_model.from_map(m['Version'])
        return self


class GetDeviceOtaInfoTestResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetDeviceOtaInfoTestResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetDeviceOtaInfoTestResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDeviceOtaInfoTestResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDeviceOtaInfoTestResponseBody = None,
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
            temp_model = GetDeviceOtaInfoTestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDeviceOtaTaskVersionInfoRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetDeviceOtaTaskVersionInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        release_note: str = None,
        size: int = None,
        version: str = None,
    ):
        self.release_note = release_note
        self.size = size
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.release_note is not None:
            result['ReleaseNote'] = self.release_note
        if self.size is not None:
            result['Size'] = self.size
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReleaseNote') is not None:
            self.release_note = m.get('ReleaseNote')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetDeviceOtaTaskVersionInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetDeviceOtaTaskVersionInfoResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetDeviceOtaTaskVersionInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDeviceOtaTaskVersionInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDeviceOtaTaskVersionInfoResponseBody = None,
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
            temp_model = GetDeviceOtaTaskVersionInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDeviceUpgradeStatusRequest(TeaModel):
    def __init__(
        self,
        app_version: str = None,
        client_uid: str = None,
        project: str = None,
        task_uid: str = None,
    ):
        self.app_version = app_version
        self.client_uid = client_uid
        self.project = project
        self.task_uid = task_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.client_uid is not None:
            result['ClientUid'] = self.client_uid
        if self.project is not None:
            result['Project'] = self.project
        if self.task_uid is not None:
            result['TaskUid'] = self.task_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('ClientUid') is not None:
            self.client_uid = m.get('ClientUid')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('TaskUid') is not None:
            self.task_uid = m.get('TaskUid')
        return self


class GetDeviceUpgradeStatusResponseBodyDataAppOtaStatusDTOList(TeaModel):
    def __init__(
        self,
        base_version: str = None,
        client_type: int = None,
        client_uid: str = None,
        note: str = None,
        os_type: str = None,
        project: str = None,
        status: int = None,
        target_version: str = None,
        task_uid: str = None,
    ):
        self.base_version = base_version
        self.client_type = client_type
        self.client_uid = client_uid
        self.note = note
        self.os_type = os_type
        self.project = project
        self.status = status
        self.target_version = target_version
        self.task_uid = task_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_version is not None:
            result['BaseVersion'] = self.base_version
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        if self.client_uid is not None:
            result['ClientUid'] = self.client_uid
        if self.note is not None:
            result['Note'] = self.note
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.project is not None:
            result['Project'] = self.project
        if self.status is not None:
            result['Status'] = self.status
        if self.target_version is not None:
            result['TargetVersion'] = self.target_version
        if self.task_uid is not None:
            result['TaskUid'] = self.task_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseVersion') is not None:
            self.base_version = m.get('BaseVersion')
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        if m.get('ClientUid') is not None:
            self.client_uid = m.get('ClientUid')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TargetVersion') is not None:
            self.target_version = m.get('TargetVersion')
        if m.get('TaskUid') is not None:
            self.task_uid = m.get('TaskUid')
        return self


class GetDeviceUpgradeStatusResponseBodyData(TeaModel):
    def __init__(
        self,
        app_ota_status_dtolist: List[GetDeviceUpgradeStatusResponseBodyDataAppOtaStatusDTOList] = None,
    ):
        self.app_ota_status_dtolist = app_ota_status_dtolist

    def validate(self):
        if self.app_ota_status_dtolist:
            for k in self.app_ota_status_dtolist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AppOtaStatusDTOList'] = []
        if self.app_ota_status_dtolist is not None:
            for k in self.app_ota_status_dtolist:
                result['AppOtaStatusDTOList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app_ota_status_dtolist = []
        if m.get('AppOtaStatusDTOList') is not None:
            for k in m.get('AppOtaStatusDTOList'):
                temp_model = GetDeviceUpgradeStatusResponseBodyDataAppOtaStatusDTOList()
                self.app_ota_status_dtolist.append(temp_model.from_map(k))
        return self


class GetDeviceUpgradeStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetDeviceUpgradeStatusResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetDeviceUpgradeStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDeviceUpgradeStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDeviceUpgradeStatusResponseBody = None,
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
            temp_model = GetDeviceUpgradeStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetExportDeviceInfoOssUrlRequest(TeaModel):
    def __init__(
        self,
        tenant_id: str = None,
        zone_id: str = None,
        zone_name: str = None,
    ):
        self.tenant_id = tenant_id
        self.zone_id = zone_id
        self.zone_name = zone_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.zone_name is not None:
            result['ZoneName'] = self.zone_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('ZoneName') is not None:
            self.zone_name = m.get('ZoneName')
        return self


class GetExportDeviceInfoOssUrlResponseBodyData(TeaModel):
    def __init__(
        self,
        url: str = None,
    ):
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetExportDeviceInfoOssUrlResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetExportDeviceInfoOssUrlResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetExportDeviceInfoOssUrlResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetExportDeviceInfoOssUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetExportDeviceInfoOssUrlResponseBody = None,
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
            temp_model = GetExportDeviceInfoOssUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFbOssConfigRequest(TeaModel):
    def __init__(
        self,
        dir_prefix: str = None,
        is_dedicated_line: int = None,
        region: str = None,
    ):
        self.dir_prefix = dir_prefix
        self.is_dedicated_line = is_dedicated_line
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dir_prefix is not None:
            result['DirPrefix'] = self.dir_prefix
        if self.is_dedicated_line is not None:
            result['IsDedicatedLine'] = self.is_dedicated_line
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirPrefix') is not None:
            self.dir_prefix = m.get('DirPrefix')
        if m.get('IsDedicatedLine') is not None:
            self.is_dedicated_line = m.get('IsDedicatedLine')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class GetFbOssConfigResponseBodyData(TeaModel):
    def __init__(
        self,
        access_key_id: str = None,
        end_point: str = None,
        oss_policy: str = None,
        oss_signature: str = None,
        session_id: str = None,
    ):
        self.access_key_id = access_key_id
        self.end_point = end_point
        self.oss_policy = oss_policy
        self.oss_signature = oss_signature
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.end_point is not None:
            result['EndPoint'] = self.end_point
        if self.oss_policy is not None:
            result['OssPolicy'] = self.oss_policy
        if self.oss_signature is not None:
            result['OssSignature'] = self.oss_signature
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('EndPoint') is not None:
            self.end_point = m.get('EndPoint')
        if m.get('OssPolicy') is not None:
            self.oss_policy = m.get('OssPolicy')
        if m.get('OssSignature') is not None:
            self.oss_signature = m.get('OssSignature')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class GetFbOssConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetFbOssConfigResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetFbOssConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetFbOssConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFbOssConfigResponseBody = None,
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
            temp_model = GetFbOssConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOssConfigRequest(TeaModel):
    def __init__(
        self,
        type: int = None,
    ):
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetOssConfigResponseBodyData(TeaModel):
    def __init__(
        self,
        access_key_id: str = None,
        end_point: str = None,
        oss_policy: str = None,
        oss_signature: str = None,
        security_token: str = None,
    ):
        self.access_key_id = access_key_id
        self.end_point = end_point
        self.oss_policy = oss_policy
        self.oss_signature = oss_signature
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.end_point is not None:
            result['EndPoint'] = self.end_point
        if self.oss_policy is not None:
            result['OssPolicy'] = self.oss_policy
        if self.oss_signature is not None:
            result['OssSignature'] = self.oss_signature
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('EndPoint') is not None:
            self.end_point = m.get('EndPoint')
        if m.get('OssPolicy') is not None:
            self.oss_policy = m.get('OssPolicy')
        if m.get('OssSignature') is not None:
            self.oss_signature = m.get('OssSignature')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class GetOssConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetOssConfigResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetOssConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetOssConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOssConfigResponseBody = None,
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
            temp_model = GetOssConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVersionDownloadUrlRequest(TeaModel):
    def __init__(
        self,
        version_name: str = None,
    ):
        self.version_name = version_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class GetVersionDownloadUrlResponseBodyData(TeaModel):
    def __init__(
        self,
        full_download_url: str = None,
    ):
        self.full_download_url = full_download_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.full_download_url is not None:
            result['FullDownloadUrl'] = self.full_download_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FullDownloadUrl') is not None:
            self.full_download_url = m.get('FullDownloadUrl')
        return self


class GetVersionDownloadUrlResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetVersionDownloadUrlResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetVersionDownloadUrlResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetVersionDownloadUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetVersionDownloadUrlResponseBody = None,
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
            temp_model = GetVersionDownloadUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeviceOtaTaskByTenantRequest(TeaModel):
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


class ListDeviceOtaTaskByTenantResponseBodyDataTenantDeviceOtaTasks(TeaModel):
    def __init__(
        self,
        model: str = None,
        operation_status: int = None,
        publish_time: str = None,
        status: int = None,
        task_id: int = None,
        upgrade_count: int = None,
        version: str = None,
    ):
        self.model = model
        self.operation_status = operation_status
        self.publish_time = publish_time
        self.status = status
        self.task_id = task_id
        self.upgrade_count = upgrade_count
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.model is not None:
            result['Model'] = self.model
        if self.operation_status is not None:
            result['OperationStatus'] = self.operation_status
        if self.publish_time is not None:
            result['PublishTime'] = self.publish_time
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.upgrade_count is not None:
            result['UpgradeCount'] = self.upgrade_count
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('OperationStatus') is not None:
            self.operation_status = m.get('OperationStatus')
        if m.get('PublishTime') is not None:
            self.publish_time = m.get('PublishTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('UpgradeCount') is not None:
            self.upgrade_count = m.get('UpgradeCount')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListDeviceOtaTaskByTenantResponseBodyData(TeaModel):
    def __init__(
        self,
        tenant_device_ota_tasks: List[ListDeviceOtaTaskByTenantResponseBodyDataTenantDeviceOtaTasks] = None,
    ):
        self.tenant_device_ota_tasks = tenant_device_ota_tasks

    def validate(self):
        if self.tenant_device_ota_tasks:
            for k in self.tenant_device_ota_tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TenantDeviceOtaTasks'] = []
        if self.tenant_device_ota_tasks is not None:
            for k in self.tenant_device_ota_tasks:
                result['TenantDeviceOtaTasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tenant_device_ota_tasks = []
        if m.get('TenantDeviceOtaTasks') is not None:
            for k in m.get('TenantDeviceOtaTasks'):
                temp_model = ListDeviceOtaTaskByTenantResponseBodyDataTenantDeviceOtaTasks()
                self.tenant_device_ota_tasks.append(temp_model.from_map(k))
        return self


class ListDeviceOtaTaskByTenantResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListDeviceOtaTaskByTenantResponseBodyData = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListDeviceOtaTaskByTenantResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDeviceOtaTaskByTenantResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDeviceOtaTaskByTenantResponseBody = None,
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
            temp_model = ListDeviceOtaTaskByTenantResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeviceSeatsRequest(TeaModel):
    def __init__(
        self,
        label: str = None,
        seat_no: str = None,
        serial_no_list: List[str] = None,
        tenant_id: str = None,
        zone_id: str = None,
    ):
        self.label = label
        self.seat_no = seat_no
        self.serial_no_list = serial_no_list
        self.tenant_id = tenant_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.seat_no is not None:
            result['SeatNo'] = self.seat_no
        if self.serial_no_list is not None:
            result['SerialNoList'] = self.serial_no_list
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('SeatNo') is not None:
            self.seat_no = m.get('SeatNo')
        if m.get('SerialNoList') is not None:
            self.serial_no_list = m.get('SerialNoList')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListDeviceSeatsResponseBodyDataDeviceSeatDTOList(TeaModel):
    def __init__(
        self,
        label: str = None,
        seat_name: str = None,
        seat_no: str = None,
        serial_no: str = None,
        site_id: str = None,
        site_name: str = None,
        zone_id: str = None,
    ):
        self.label = label
        self.seat_name = seat_name
        self.seat_no = seat_no
        self.serial_no = serial_no
        self.site_id = site_id
        self.site_name = site_name
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.seat_name is not None:
            result['SeatName'] = self.seat_name
        if self.seat_no is not None:
            result['SeatNo'] = self.seat_no
        if self.serial_no is not None:
            result['SerialNo'] = self.serial_no
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.site_name is not None:
            result['SiteName'] = self.site_name
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('SeatName') is not None:
            self.seat_name = m.get('SeatName')
        if m.get('SeatNo') is not None:
            self.seat_no = m.get('SeatNo')
        if m.get('SerialNo') is not None:
            self.serial_no = m.get('SerialNo')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('SiteName') is not None:
            self.site_name = m.get('SiteName')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListDeviceSeatsResponseBodyData(TeaModel):
    def __init__(
        self,
        device_seat_dtolist: List[ListDeviceSeatsResponseBodyDataDeviceSeatDTOList] = None,
        total_count: int = None,
    ):
        self.device_seat_dtolist = device_seat_dtolist
        self.total_count = total_count

    def validate(self):
        if self.device_seat_dtolist:
            for k in self.device_seat_dtolist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DeviceSeatDTOList'] = []
        if self.device_seat_dtolist is not None:
            for k in self.device_seat_dtolist:
                result['DeviceSeatDTOList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.device_seat_dtolist = []
        if m.get('DeviceSeatDTOList') is not None:
            for k in m.get('DeviceSeatDTOList'):
                temp_model = ListDeviceSeatsResponseBodyDataDeviceSeatDTOList()
                self.device_seat_dtolist.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDeviceSeatsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListDeviceSeatsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListDeviceSeatsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDeviceSeatsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDeviceSeatsResponseBody = None,
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
            temp_model = ListDeviceSeatsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDevicesRequest(TeaModel):
    def __init__(
        self,
        alias: str = None,
        build_id: str = None,
        client_type: int = None,
        device_group_id: str = None,
        device_ip_v4: str = None,
        device_name: str = None,
        device_os: str = None,
        device_platform: str = None,
        end_user_id: str = None,
        label_content: str = None,
        label_id: str = None,
        location_info: str = None,
        model: str = None,
        page_number: int = None,
        page_size: int = None,
        serial_no: str = None,
        user_type: str = None,
        uuid: str = None,
    ):
        self.alias = alias
        self.build_id = build_id
        self.client_type = client_type
        self.device_group_id = device_group_id
        self.device_ip_v4 = device_ip_v4
        self.device_name = device_name
        self.device_os = device_os
        self.device_platform = device_platform
        self.end_user_id = end_user_id
        self.label_content = label_content
        self.label_id = label_id
        self.location_info = location_info
        self.model = model
        self.page_number = page_number
        self.page_size = page_size
        self.serial_no = serial_no
        self.user_type = user_type
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.build_id is not None:
            result['BuildId'] = self.build_id
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id
        if self.device_ip_v4 is not None:
            result['DeviceIpV4'] = self.device_ip_v4
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.device_os is not None:
            result['DeviceOS'] = self.device_os
        if self.device_platform is not None:
            result['DevicePlatform'] = self.device_platform
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.label_content is not None:
            result['LabelContent'] = self.label_content
        if self.label_id is not None:
            result['LabelId'] = self.label_id
        if self.location_info is not None:
            result['LocationInfo'] = self.location_info
        if self.model is not None:
            result['Model'] = self.model
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.serial_no is not None:
            result['SerialNo'] = self.serial_no
        if self.user_type is not None:
            result['UserType'] = self.user_type
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('BuildId') is not None:
            self.build_id = m.get('BuildId')
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')
        if m.get('DeviceIpV4') is not None:
            self.device_ip_v4 = m.get('DeviceIpV4')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('DeviceOS') is not None:
            self.device_os = m.get('DeviceOS')
        if m.get('DevicePlatform') is not None:
            self.device_platform = m.get('DevicePlatform')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('LabelContent') is not None:
            self.label_content = m.get('LabelContent')
        if m.get('LabelId') is not None:
            self.label_id = m.get('LabelId')
        if m.get('LocationInfo') is not None:
            self.location_info = m.get('LocationInfo')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SerialNo') is not None:
            self.serial_no = m.get('SerialNo')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class ListDevicesResponseBodyDataConnectConfigs(TeaModel):
    def __init__(
        self,
        connect_script: str = None,
        peripheral_pid: str = None,
        peripheral_vid: str = None,
        redirect_policy: int = None,
    ):
        self.connect_script = connect_script
        self.peripheral_pid = peripheral_pid
        self.peripheral_vid = peripheral_vid
        self.redirect_policy = redirect_policy

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connect_script is not None:
            result['ConnectScript'] = self.connect_script
        if self.peripheral_pid is not None:
            result['PeripheralPid'] = self.peripheral_pid
        if self.peripheral_vid is not None:
            result['PeripheralVid'] = self.peripheral_vid
        if self.redirect_policy is not None:
            result['RedirectPolicy'] = self.redirect_policy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectScript') is not None:
            self.connect_script = m.get('ConnectScript')
        if m.get('PeripheralPid') is not None:
            self.peripheral_pid = m.get('PeripheralPid')
        if m.get('PeripheralVid') is not None:
            self.peripheral_vid = m.get('PeripheralVid')
        if m.get('RedirectPolicy') is not None:
            self.redirect_policy = m.get('RedirectPolicy')
        return self


class ListDevicesResponseBodyDataCustomResourcePackage(TeaModel):
    def __init__(
        self,
        config_about_logo: str = None,
        desktop_wallpaper: str = None,
        login_page_background: str = None,
        login_page_logo: str = None,
        personal_center_logo: str = None,
        start_logo: str = None,
        start_menu_logo: str = None,
        upgrade_logo: str = None,
    ):
        self.config_about_logo = config_about_logo
        self.desktop_wallpaper = desktop_wallpaper
        self.login_page_background = login_page_background
        self.login_page_logo = login_page_logo
        self.personal_center_logo = personal_center_logo
        self.start_logo = start_logo
        self.start_menu_logo = start_menu_logo
        self.upgrade_logo = upgrade_logo

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_about_logo is not None:
            result['ConfigAboutLogo'] = self.config_about_logo
        if self.desktop_wallpaper is not None:
            result['DesktopWallpaper'] = self.desktop_wallpaper
        if self.login_page_background is not None:
            result['LoginPageBackground'] = self.login_page_background
        if self.login_page_logo is not None:
            result['LoginPageLogo'] = self.login_page_logo
        if self.personal_center_logo is not None:
            result['PersonalCenterLogo'] = self.personal_center_logo
        if self.start_logo is not None:
            result['StartLogo'] = self.start_logo
        if self.start_menu_logo is not None:
            result['StartMenuLogo'] = self.start_menu_logo
        if self.upgrade_logo is not None:
            result['UpgradeLogo'] = self.upgrade_logo
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigAboutLogo') is not None:
            self.config_about_logo = m.get('ConfigAboutLogo')
        if m.get('DesktopWallpaper') is not None:
            self.desktop_wallpaper = m.get('DesktopWallpaper')
        if m.get('LoginPageBackground') is not None:
            self.login_page_background = m.get('LoginPageBackground')
        if m.get('LoginPageLogo') is not None:
            self.login_page_logo = m.get('LoginPageLogo')
        if m.get('PersonalCenterLogo') is not None:
            self.personal_center_logo = m.get('PersonalCenterLogo')
        if m.get('StartLogo') is not None:
            self.start_logo = m.get('StartLogo')
        if m.get('StartMenuLogo') is not None:
            self.start_menu_logo = m.get('StartMenuLogo')
        if m.get('UpgradeLogo') is not None:
            self.upgrade_logo = m.get('UpgradeLogo')
        return self


class ListDevicesResponseBodyDataEndUserList(TeaModel):
    def __init__(
        self,
        ad_domain: str = None,
        bind_time: str = None,
        directory_id: str = None,
        end_user_id: str = None,
        id: int = None,
        serial_no: str = None,
        tenant_id: str = None,
        user_type: str = None,
    ):
        self.ad_domain = ad_domain
        self.bind_time = bind_time
        self.directory_id = directory_id
        self.end_user_id = end_user_id
        self.id = id
        self.serial_no = serial_no
        self.tenant_id = tenant_id
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ad_domain is not None:
            result['AdDomain'] = self.ad_domain
        if self.bind_time is not None:
            result['BindTime'] = self.bind_time
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.id is not None:
            result['Id'] = self.id
        if self.serial_no is not None:
            result['SerialNo'] = self.serial_no
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdDomain') is not None:
            self.ad_domain = m.get('AdDomain')
        if m.get('BindTime') is not None:
            self.bind_time = m.get('BindTime')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('SerialNo') is not None:
            self.serial_no = m.get('SerialNo')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class ListDevicesResponseBodyDataLabelList(TeaModel):
    def __init__(
        self,
        content: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        label_id: str = None,
        tenant_id: str = None,
    ):
        self.content = content
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.label_id = label_id
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.label_id is not None:
            result['LabelId'] = self.label_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('LabelId') is not None:
            self.label_id = m.get('LabelId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class ListDevicesResponseBodyDataPeripheralConfig(TeaModel):
    def __init__(
        self,
        default_policy: int = None,
        policy_strategy: int = None,
        usb_and_internal_camera: int = None,
        usb_printer: int = None,
        usb_storage: int = None,
    ):
        self.default_policy = default_policy
        self.policy_strategy = policy_strategy
        self.usb_and_internal_camera = usb_and_internal_camera
        self.usb_printer = usb_printer
        self.usb_storage = usb_storage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_policy is not None:
            result['DefaultPolicy'] = self.default_policy
        if self.policy_strategy is not None:
            result['PolicyStrategy'] = self.policy_strategy
        if self.usb_and_internal_camera is not None:
            result['UsbAndInternalCamera'] = self.usb_and_internal_camera
        if self.usb_printer is not None:
            result['UsbPrinter'] = self.usb_printer
        if self.usb_storage is not None:
            result['UsbStorage'] = self.usb_storage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultPolicy') is not None:
            self.default_policy = m.get('DefaultPolicy')
        if m.get('PolicyStrategy') is not None:
            self.policy_strategy = m.get('PolicyStrategy')
        if m.get('UsbAndInternalCamera') is not None:
            self.usb_and_internal_camera = m.get('UsbAndInternalCamera')
        if m.get('UsbPrinter') is not None:
            self.usb_printer = m.get('UsbPrinter')
        if m.get('UsbStorage') is not None:
            self.usb_storage = m.get('UsbStorage')
        return self


class ListDevicesResponseBodyData(TeaModel):
    def __init__(
        self,
        active_time: str = None,
        alias: str = None,
        auto_lock_screen_time: int = None,
        auto_login: int = None,
        auto_type: str = None,
        bluetooth: str = None,
        build_id: str = None,
        client_id: str = None,
        client_type: str = None,
        connect_configs: List[ListDevicesResponseBodyDataConnectConfigs] = None,
        custom_idle_action: int = None,
        custom_power_on: int = None,
        custom_property: str = None,
        custom_resource_package: ListDevicesResponseBodyDataCustomResourcePackage = None,
        define_power_button: int = None,
        device_ip_v4: str = None,
        device_lock: int = None,
        device_mqtt_connection_status: int = None,
        device_name: str = None,
        device_os: str = None,
        device_platform: str = None,
        display_layout: str = None,
        display_resolution: str = None,
        display_scale_ratio: str = None,
        enable_adb: int = None,
        enable_auto_lock_screen: int = None,
        enable_bluetooth: int = None,
        enable_lock_screen_password: int = None,
        enable_modify_password: int = None,
        enable_scheduled_power_off: int = None,
        enable_unlock_password: int = None,
        enable_wlan: int = None,
        end_user_list: List[ListDevicesResponseBodyDataEndUserList] = None,
        ether_mac: str = None,
        gmt_modified: str = None,
        gmt_sync: str = None,
        id: int = None,
        idle_time: int = None,
        is_active: str = None,
        label_list: List[ListDevicesResponseBodyDataLabelList] = None,
        last_login_user: str = None,
        local_usb_print: int = None,
        location_info: str = None,
        lock_password: str = None,
        model: str = None,
        order_id: str = None,
        peripheral_config: ListDevicesResponseBodyDataPeripheralConfig = None,
        scheduled_power_off: str = None,
        secure_network_type: str = None,
        serial_no: str = None,
        sleep_time: int = None,
        source: str = None,
        tenant_id: str = None,
        usb_storage: int = None,
        uuid: str = None,
        wlan: str = None,
    ):
        self.active_time = active_time
        self.alias = alias
        self.auto_lock_screen_time = auto_lock_screen_time
        self.auto_login = auto_login
        self.auto_type = auto_type
        self.bluetooth = bluetooth
        self.build_id = build_id
        self.client_id = client_id
        self.client_type = client_type
        self.connect_configs = connect_configs
        self.custom_idle_action = custom_idle_action
        self.custom_power_on = custom_power_on
        self.custom_property = custom_property
        self.custom_resource_package = custom_resource_package
        self.define_power_button = define_power_button
        self.device_ip_v4 = device_ip_v4
        self.device_lock = device_lock
        self.device_mqtt_connection_status = device_mqtt_connection_status
        self.device_name = device_name
        self.device_os = device_os
        self.device_platform = device_platform
        self.display_layout = display_layout
        self.display_resolution = display_resolution
        self.display_scale_ratio = display_scale_ratio
        self.enable_adb = enable_adb
        self.enable_auto_lock_screen = enable_auto_lock_screen
        self.enable_bluetooth = enable_bluetooth
        self.enable_lock_screen_password = enable_lock_screen_password
        self.enable_modify_password = enable_modify_password
        self.enable_scheduled_power_off = enable_scheduled_power_off
        self.enable_unlock_password = enable_unlock_password
        self.enable_wlan = enable_wlan
        self.end_user_list = end_user_list
        self.ether_mac = ether_mac
        self.gmt_modified = gmt_modified
        self.gmt_sync = gmt_sync
        self.id = id
        self.idle_time = idle_time
        self.is_active = is_active
        self.label_list = label_list
        self.last_login_user = last_login_user
        self.local_usb_print = local_usb_print
        self.location_info = location_info
        self.lock_password = lock_password
        self.model = model
        self.order_id = order_id
        self.peripheral_config = peripheral_config
        self.scheduled_power_off = scheduled_power_off
        self.secure_network_type = secure_network_type
        self.serial_no = serial_no
        self.sleep_time = sleep_time
        self.source = source
        self.tenant_id = tenant_id
        self.usb_storage = usb_storage
        self.uuid = uuid
        self.wlan = wlan

    def validate(self):
        if self.connect_configs:
            for k in self.connect_configs:
                if k:
                    k.validate()
        if self.custom_resource_package:
            self.custom_resource_package.validate()
        if self.end_user_list:
            for k in self.end_user_list:
                if k:
                    k.validate()
        if self.label_list:
            for k in self.label_list:
                if k:
                    k.validate()
        if self.peripheral_config:
            self.peripheral_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_time is not None:
            result['ActiveTime'] = self.active_time
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.auto_lock_screen_time is not None:
            result['AutoLockScreenTime'] = self.auto_lock_screen_time
        if self.auto_login is not None:
            result['AutoLogin'] = self.auto_login
        if self.auto_type is not None:
            result['AutoType'] = self.auto_type
        if self.bluetooth is not None:
            result['Bluetooth'] = self.bluetooth
        if self.build_id is not None:
            result['BuildId'] = self.build_id
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        result['ConnectConfigs'] = []
        if self.connect_configs is not None:
            for k in self.connect_configs:
                result['ConnectConfigs'].append(k.to_map() if k else None)
        if self.custom_idle_action is not None:
            result['CustomIdleAction'] = self.custom_idle_action
        if self.custom_power_on is not None:
            result['CustomPowerOn'] = self.custom_power_on
        if self.custom_property is not None:
            result['CustomProperty'] = self.custom_property
        if self.custom_resource_package is not None:
            result['CustomResourcePackage'] = self.custom_resource_package.to_map()
        if self.define_power_button is not None:
            result['DefinePowerButton'] = self.define_power_button
        if self.device_ip_v4 is not None:
            result['DeviceIpV4'] = self.device_ip_v4
        if self.device_lock is not None:
            result['DeviceLock'] = self.device_lock
        if self.device_mqtt_connection_status is not None:
            result['DeviceMqttConnectionStatus'] = self.device_mqtt_connection_status
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.device_os is not None:
            result['DeviceOS'] = self.device_os
        if self.device_platform is not None:
            result['DevicePlatform'] = self.device_platform
        if self.display_layout is not None:
            result['DisplayLayout'] = self.display_layout
        if self.display_resolution is not None:
            result['DisplayResolution'] = self.display_resolution
        if self.display_scale_ratio is not None:
            result['DisplayScaleRatio'] = self.display_scale_ratio
        if self.enable_adb is not None:
            result['EnableAdb'] = self.enable_adb
        if self.enable_auto_lock_screen is not None:
            result['EnableAutoLockScreen'] = self.enable_auto_lock_screen
        if self.enable_bluetooth is not None:
            result['EnableBluetooth'] = self.enable_bluetooth
        if self.enable_lock_screen_password is not None:
            result['EnableLockScreenPassword'] = self.enable_lock_screen_password
        if self.enable_modify_password is not None:
            result['EnableModifyPassword'] = self.enable_modify_password
        if self.enable_scheduled_power_off is not None:
            result['EnableScheduledPowerOff'] = self.enable_scheduled_power_off
        if self.enable_unlock_password is not None:
            result['EnableUnlockPassword'] = self.enable_unlock_password
        if self.enable_wlan is not None:
            result['EnableWlan'] = self.enable_wlan
        result['EndUserList'] = []
        if self.end_user_list is not None:
            for k in self.end_user_list:
                result['EndUserList'].append(k.to_map() if k else None)
        if self.ether_mac is not None:
            result['EtherMac'] = self.ether_mac
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.gmt_sync is not None:
            result['GmtSync'] = self.gmt_sync
        if self.id is not None:
            result['Id'] = self.id
        if self.idle_time is not None:
            result['IdleTime'] = self.idle_time
        if self.is_active is not None:
            result['IsActive'] = self.is_active
        result['LabelList'] = []
        if self.label_list is not None:
            for k in self.label_list:
                result['LabelList'].append(k.to_map() if k else None)
        if self.last_login_user is not None:
            result['LastLoginUser'] = self.last_login_user
        if self.local_usb_print is not None:
            result['LocalUsbPrint'] = self.local_usb_print
        if self.location_info is not None:
            result['LocationInfo'] = self.location_info
        if self.lock_password is not None:
            result['LockPassword'] = self.lock_password
        if self.model is not None:
            result['Model'] = self.model
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.peripheral_config is not None:
            result['PeripheralConfig'] = self.peripheral_config.to_map()
        if self.scheduled_power_off is not None:
            result['ScheduledPowerOff'] = self.scheduled_power_off
        if self.secure_network_type is not None:
            result['SecureNetworkType'] = self.secure_network_type
        if self.serial_no is not None:
            result['SerialNo'] = self.serial_no
        if self.sleep_time is not None:
            result['SleepTime'] = self.sleep_time
        if self.source is not None:
            result['Source'] = self.source
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.usb_storage is not None:
            result['UsbStorage'] = self.usb_storage
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.wlan is not None:
            result['Wlan'] = self.wlan
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveTime') is not None:
            self.active_time = m.get('ActiveTime')
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('AutoLockScreenTime') is not None:
            self.auto_lock_screen_time = m.get('AutoLockScreenTime')
        if m.get('AutoLogin') is not None:
            self.auto_login = m.get('AutoLogin')
        if m.get('AutoType') is not None:
            self.auto_type = m.get('AutoType')
        if m.get('Bluetooth') is not None:
            self.bluetooth = m.get('Bluetooth')
        if m.get('BuildId') is not None:
            self.build_id = m.get('BuildId')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        self.connect_configs = []
        if m.get('ConnectConfigs') is not None:
            for k in m.get('ConnectConfigs'):
                temp_model = ListDevicesResponseBodyDataConnectConfigs()
                self.connect_configs.append(temp_model.from_map(k))
        if m.get('CustomIdleAction') is not None:
            self.custom_idle_action = m.get('CustomIdleAction')
        if m.get('CustomPowerOn') is not None:
            self.custom_power_on = m.get('CustomPowerOn')
        if m.get('CustomProperty') is not None:
            self.custom_property = m.get('CustomProperty')
        if m.get('CustomResourcePackage') is not None:
            temp_model = ListDevicesResponseBodyDataCustomResourcePackage()
            self.custom_resource_package = temp_model.from_map(m['CustomResourcePackage'])
        if m.get('DefinePowerButton') is not None:
            self.define_power_button = m.get('DefinePowerButton')
        if m.get('DeviceIpV4') is not None:
            self.device_ip_v4 = m.get('DeviceIpV4')
        if m.get('DeviceLock') is not None:
            self.device_lock = m.get('DeviceLock')
        if m.get('DeviceMqttConnectionStatus') is not None:
            self.device_mqtt_connection_status = m.get('DeviceMqttConnectionStatus')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('DeviceOS') is not None:
            self.device_os = m.get('DeviceOS')
        if m.get('DevicePlatform') is not None:
            self.device_platform = m.get('DevicePlatform')
        if m.get('DisplayLayout') is not None:
            self.display_layout = m.get('DisplayLayout')
        if m.get('DisplayResolution') is not None:
            self.display_resolution = m.get('DisplayResolution')
        if m.get('DisplayScaleRatio') is not None:
            self.display_scale_ratio = m.get('DisplayScaleRatio')
        if m.get('EnableAdb') is not None:
            self.enable_adb = m.get('EnableAdb')
        if m.get('EnableAutoLockScreen') is not None:
            self.enable_auto_lock_screen = m.get('EnableAutoLockScreen')
        if m.get('EnableBluetooth') is not None:
            self.enable_bluetooth = m.get('EnableBluetooth')
        if m.get('EnableLockScreenPassword') is not None:
            self.enable_lock_screen_password = m.get('EnableLockScreenPassword')
        if m.get('EnableModifyPassword') is not None:
            self.enable_modify_password = m.get('EnableModifyPassword')
        if m.get('EnableScheduledPowerOff') is not None:
            self.enable_scheduled_power_off = m.get('EnableScheduledPowerOff')
        if m.get('EnableUnlockPassword') is not None:
            self.enable_unlock_password = m.get('EnableUnlockPassword')
        if m.get('EnableWlan') is not None:
            self.enable_wlan = m.get('EnableWlan')
        self.end_user_list = []
        if m.get('EndUserList') is not None:
            for k in m.get('EndUserList'):
                temp_model = ListDevicesResponseBodyDataEndUserList()
                self.end_user_list.append(temp_model.from_map(k))
        if m.get('EtherMac') is not None:
            self.ether_mac = m.get('EtherMac')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('GmtSync') is not None:
            self.gmt_sync = m.get('GmtSync')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdleTime') is not None:
            self.idle_time = m.get('IdleTime')
        if m.get('IsActive') is not None:
            self.is_active = m.get('IsActive')
        self.label_list = []
        if m.get('LabelList') is not None:
            for k in m.get('LabelList'):
                temp_model = ListDevicesResponseBodyDataLabelList()
                self.label_list.append(temp_model.from_map(k))
        if m.get('LastLoginUser') is not None:
            self.last_login_user = m.get('LastLoginUser')
        if m.get('LocalUsbPrint') is not None:
            self.local_usb_print = m.get('LocalUsbPrint')
        if m.get('LocationInfo') is not None:
            self.location_info = m.get('LocationInfo')
        if m.get('LockPassword') is not None:
            self.lock_password = m.get('LockPassword')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PeripheralConfig') is not None:
            temp_model = ListDevicesResponseBodyDataPeripheralConfig()
            self.peripheral_config = temp_model.from_map(m['PeripheralConfig'])
        if m.get('ScheduledPowerOff') is not None:
            self.scheduled_power_off = m.get('ScheduledPowerOff')
        if m.get('SecureNetworkType') is not None:
            self.secure_network_type = m.get('SecureNetworkType')
        if m.get('SerialNo') is not None:
            self.serial_no = m.get('SerialNo')
        if m.get('SleepTime') is not None:
            self.sleep_time = m.get('SleepTime')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('UsbStorage') is not None:
            self.usb_storage = m.get('UsbStorage')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('Wlan') is not None:
            self.wlan = m.get('Wlan')
        return self


class ListDevicesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListDevicesResponseBodyData] = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListDevicesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDevicesResponseBody = None,
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
            temp_model = ListDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFbIssueLabelsResponseBodyData(TeaModel):
    def __init__(
        self,
        issue_label: List[str] = None,
    ):
        self.issue_label = issue_label

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.issue_label is not None:
            result['IssueLabel'] = self.issue_label
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IssueLabel') is not None:
            self.issue_label = m.get('IssueLabel')
        return self


class ListFbIssueLabelsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListFbIssueLabelsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListFbIssueLabelsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListFbIssueLabelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFbIssueLabelsResponseBody = None,
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
            temp_model = ListFbIssueLabelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFbIssueLabelsByLCRequest(TeaModel):
    def __init__(
        self,
        caller: str = None,
        language_type: str = None,
    ):
        self.caller = caller
        self.language_type = language_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.caller is not None:
            result['Caller'] = self.caller
        if self.language_type is not None:
            result['LanguageType'] = self.language_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Caller') is not None:
            self.caller = m.get('Caller')
        if m.get('LanguageType') is not None:
            self.language_type = m.get('LanguageType')
        return self


class ListFbIssueLabelsByLCResponseBodyData(TeaModel):
    def __init__(
        self,
        issue_label: List[str] = None,
    ):
        self.issue_label = issue_label

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.issue_label is not None:
            result['IssueLabel'] = self.issue_label
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IssueLabel') is not None:
            self.issue_label = m.get('IssueLabel')
        return self


class ListFbIssueLabelsByLCResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListFbIssueLabelsByLCResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListFbIssueLabelsByLCResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListFbIssueLabelsByLCResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFbIssueLabelsByLCResponseBody = None,
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
            temp_model = ListFbIssueLabelsByLCResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLabelsRequest(TeaModel):
    def __init__(
        self,
        label_content: str = None,
        label_id: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        self.label_content = label_content
        self.label_id = label_id
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_content is not None:
            result['LabelContent'] = self.label_content
        if self.label_id is not None:
            result['LabelId'] = self.label_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LabelContent') is not None:
            self.label_content = m.get('LabelContent')
        if m.get('LabelId') is not None:
            self.label_id = m.get('LabelId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListLabelsResponseBodyData(TeaModel):
    def __init__(
        self,
        content: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        id: int = None,
        label_id: str = None,
        tenant_id: str = None,
    ):
        self.content = content
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.label_id = label_id
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.label_id is not None:
            result['LabelId'] = self.label_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LabelId') is not None:
            self.label_id = m.get('LabelId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class ListLabelsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListLabelsResponseBodyData] = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.next_token = next_token
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListLabelsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListLabelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListLabelsResponseBody = None,
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
            temp_model = ListLabelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTenantDeviceOtaInfoRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        task_id: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        # This parameter is required.
        self.task_id = task_id

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
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ListTenantDeviceOtaInfoResponseBodyDataTenantDeviceOtaInfos(TeaModel):
    def __init__(
        self,
        current_version: str = None,
        device_id: str = None,
        model: str = None,
    ):
        self.current_version = current_version
        self.device_id = device_id
        self.model = model

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_version is not None:
            result['CurrentVersion'] = self.current_version
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.model is not None:
            result['Model'] = self.model
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentVersion') is not None:
            self.current_version = m.get('CurrentVersion')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        return self


class ListTenantDeviceOtaInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        tenant_device_ota_infos: List[ListTenantDeviceOtaInfoResponseBodyDataTenantDeviceOtaInfos] = None,
    ):
        self.tenant_device_ota_infos = tenant_device_ota_infos

    def validate(self):
        if self.tenant_device_ota_infos:
            for k in self.tenant_device_ota_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TenantDeviceOtaInfos'] = []
        if self.tenant_device_ota_infos is not None:
            for k in self.tenant_device_ota_infos:
                result['TenantDeviceOtaInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tenant_device_ota_infos = []
        if m.get('TenantDeviceOtaInfos') is not None:
            for k in m.get('TenantDeviceOtaInfos'):
                temp_model = ListTenantDeviceOtaInfoResponseBodyDataTenantDeviceOtaInfos()
                self.tenant_device_ota_infos.append(temp_model.from_map(k))
        return self


class ListTenantDeviceOtaInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListTenantDeviceOtaInfoResponseBodyData = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListTenantDeviceOtaInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTenantDeviceOtaInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTenantDeviceOtaInfoResponseBody = None,
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
            temp_model = ListTenantDeviceOtaInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTerminalRequest(TeaModel):
    def __init__(
        self,
        alias: str = None,
        build_id: str = None,
        client_type: int = None,
        in_manage: bool = None,
        ipv_4: str = None,
        location_info: str = None,
        max_results: int = None,
        model: str = None,
        next_token: str = None,
        search_keyword: str = None,
        serial_number: str = None,
        terminal_group_id: str = None,
        uuid: str = None,
    ):
        self.alias = alias
        self.build_id = build_id
        self.client_type = client_type
        self.in_manage = in_manage
        self.ipv_4 = ipv_4
        self.location_info = location_info
        self.max_results = max_results
        self.model = model
        self.next_token = next_token
        self.search_keyword = search_keyword
        self.serial_number = serial_number
        self.terminal_group_id = terminal_group_id
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.build_id is not None:
            result['BuildId'] = self.build_id
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        if self.in_manage is not None:
            result['InManage'] = self.in_manage
        if self.ipv_4 is not None:
            result['Ipv4'] = self.ipv_4
        if self.location_info is not None:
            result['LocationInfo'] = self.location_info
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.model is not None:
            result['Model'] = self.model
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.search_keyword is not None:
            result['SearchKeyword'] = self.search_keyword
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.terminal_group_id is not None:
            result['TerminalGroupId'] = self.terminal_group_id
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('BuildId') is not None:
            self.build_id = m.get('BuildId')
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        if m.get('InManage') is not None:
            self.in_manage = m.get('InManage')
        if m.get('Ipv4') is not None:
            self.ipv_4 = m.get('Ipv4')
        if m.get('LocationInfo') is not None:
            self.location_info = m.get('LocationInfo')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('SearchKeyword') is not None:
            self.search_keyword = m.get('SearchKeyword')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('TerminalGroupId') is not None:
            self.terminal_group_id = m.get('TerminalGroupId')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class ListTerminalResponseBodyData(TeaModel):
    def __init__(
        self,
        alias: str = None,
        bind_user_count: int = None,
        bind_user_id: str = None,
        build_id: str = None,
        client_type: int = None,
        desktop_id: str = None,
        in_manage: bool = None,
        ipv_4: str = None,
        last_login_user: str = None,
        location_info: str = None,
        lock_settings: bool = None,
        login_user: str = None,
        model: str = None,
        online_status: bool = None,
        serial_number: str = None,
        terminal_group_id: str = None,
        uuid: str = None,
    ):
        self.alias = alias
        self.bind_user_count = bind_user_count
        self.bind_user_id = bind_user_id
        self.build_id = build_id
        self.client_type = client_type
        self.desktop_id = desktop_id
        self.in_manage = in_manage
        self.ipv_4 = ipv_4
        self.last_login_user = last_login_user
        self.location_info = location_info
        self.lock_settings = lock_settings
        self.login_user = login_user
        self.model = model
        self.online_status = online_status
        self.serial_number = serial_number
        self.terminal_group_id = terminal_group_id
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.bind_user_count is not None:
            result['BindUserCount'] = self.bind_user_count
        if self.bind_user_id is not None:
            result['BindUserId'] = self.bind_user_id
        if self.build_id is not None:
            result['BuildId'] = self.build_id
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.in_manage is not None:
            result['InManage'] = self.in_manage
        if self.ipv_4 is not None:
            result['Ipv4'] = self.ipv_4
        if self.last_login_user is not None:
            result['LastLoginUser'] = self.last_login_user
        if self.location_info is not None:
            result['LocationInfo'] = self.location_info
        if self.lock_settings is not None:
            result['LockSettings'] = self.lock_settings
        if self.login_user is not None:
            result['LoginUser'] = self.login_user
        if self.model is not None:
            result['Model'] = self.model
        if self.online_status is not None:
            result['OnlineStatus'] = self.online_status
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.terminal_group_id is not None:
            result['TerminalGroupId'] = self.terminal_group_id
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('BindUserCount') is not None:
            self.bind_user_count = m.get('BindUserCount')
        if m.get('BindUserId') is not None:
            self.bind_user_id = m.get('BindUserId')
        if m.get('BuildId') is not None:
            self.build_id = m.get('BuildId')
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('InManage') is not None:
            self.in_manage = m.get('InManage')
        if m.get('Ipv4') is not None:
            self.ipv_4 = m.get('Ipv4')
        if m.get('LastLoginUser') is not None:
            self.last_login_user = m.get('LastLoginUser')
        if m.get('LocationInfo') is not None:
            self.location_info = m.get('LocationInfo')
        if m.get('LockSettings') is not None:
            self.lock_settings = m.get('LockSettings')
        if m.get('LoginUser') is not None:
            self.login_user = m.get('LoginUser')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('OnlineStatus') is not None:
            self.online_status = m.get('OnlineStatus')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('TerminalGroupId') is not None:
            self.terminal_group_id = m.get('TerminalGroupId')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class ListTerminalResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListTerminalResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.next_token = next_token
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListTerminalResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTerminalResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTerminalResponseBody = None,
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
            temp_model = ListTerminalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTerminalsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        search_keyword: str = None,
        serial_numbers: List[str] = None,
        terminal_group_id: str = None,
        uuids: List[str] = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.search_keyword = search_keyword
        self.serial_numbers = serial_numbers
        self.terminal_group_id = terminal_group_id
        self.uuids = uuids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.search_keyword is not None:
            result['SearchKeyword'] = self.search_keyword
        if self.serial_numbers is not None:
            result['SerialNumbers'] = self.serial_numbers
        if self.terminal_group_id is not None:
            result['TerminalGroupId'] = self.terminal_group_id
        if self.uuids is not None:
            result['Uuids'] = self.uuids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('SearchKeyword') is not None:
            self.search_keyword = m.get('SearchKeyword')
        if m.get('SerialNumbers') is not None:
            self.serial_numbers = m.get('SerialNumbers')
        if m.get('TerminalGroupId') is not None:
            self.terminal_group_id = m.get('TerminalGroupId')
        if m.get('Uuids') is not None:
            self.uuids = m.get('Uuids')
        return self


class ListTerminalsResponseBodyData(TeaModel):
    def __init__(
        self,
        alias: str = None,
        build_id: str = None,
        client_type: int = None,
        current_connect_desktop: str = None,
        current_login_user: str = None,
        ipv_4: str = None,
        location_info: str = None,
        manage_time: str = None,
        model: str = None,
        online: bool = None,
        password_free_login_user: str = None,
        serial_number: str = None,
        set_password_free_login_user_time: str = None,
        terminal_group_id: str = None,
        uuid: str = None,
    ):
        self.alias = alias
        self.build_id = build_id
        self.client_type = client_type
        self.current_connect_desktop = current_connect_desktop
        self.current_login_user = current_login_user
        self.ipv_4 = ipv_4
        self.location_info = location_info
        self.manage_time = manage_time
        self.model = model
        self.online = online
        self.password_free_login_user = password_free_login_user
        self.serial_number = serial_number
        self.set_password_free_login_user_time = set_password_free_login_user_time
        self.terminal_group_id = terminal_group_id
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.build_id is not None:
            result['BuildId'] = self.build_id
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        if self.current_connect_desktop is not None:
            result['CurrentConnectDesktop'] = self.current_connect_desktop
        if self.current_login_user is not None:
            result['CurrentLoginUser'] = self.current_login_user
        if self.ipv_4 is not None:
            result['Ipv4'] = self.ipv_4
        if self.location_info is not None:
            result['LocationInfo'] = self.location_info
        if self.manage_time is not None:
            result['ManageTime'] = self.manage_time
        if self.model is not None:
            result['Model'] = self.model
        if self.online is not None:
            result['Online'] = self.online
        if self.password_free_login_user is not None:
            result['PasswordFreeLoginUser'] = self.password_free_login_user
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.set_password_free_login_user_time is not None:
            result['SetPasswordFreeLoginUserTime'] = self.set_password_free_login_user_time
        if self.terminal_group_id is not None:
            result['TerminalGroupId'] = self.terminal_group_id
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('BuildId') is not None:
            self.build_id = m.get('BuildId')
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        if m.get('CurrentConnectDesktop') is not None:
            self.current_connect_desktop = m.get('CurrentConnectDesktop')
        if m.get('CurrentLoginUser') is not None:
            self.current_login_user = m.get('CurrentLoginUser')
        if m.get('Ipv4') is not None:
            self.ipv_4 = m.get('Ipv4')
        if m.get('LocationInfo') is not None:
            self.location_info = m.get('LocationInfo')
        if m.get('ManageTime') is not None:
            self.manage_time = m.get('ManageTime')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('Online') is not None:
            self.online = m.get('Online')
        if m.get('PasswordFreeLoginUser') is not None:
            self.password_free_login_user = m.get('PasswordFreeLoginUser')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('SetPasswordFreeLoginUserTime') is not None:
            self.set_password_free_login_user_time = m.get('SetPasswordFreeLoginUserTime')
        if m.get('TerminalGroupId') is not None:
            self.terminal_group_id = m.get('TerminalGroupId')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class ListTerminalsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListTerminalsResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.next_token = next_token
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListTerminalsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTerminalsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTerminalsResponseBody = None,
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
            temp_model = ListTerminalsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTrustDevicesRequest(TeaModel):
    def __init__(
        self,
        label_content: str = None,
        label_id: str = None,
        serial_no: str = None,
        user_custom_id: str = None,
    ):
        self.label_content = label_content
        self.label_id = label_id
        self.serial_no = serial_no
        self.user_custom_id = user_custom_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_content is not None:
            result['LabelContent'] = self.label_content
        if self.label_id is not None:
            result['LabelId'] = self.label_id
        if self.serial_no is not None:
            result['SerialNo'] = self.serial_no
        if self.user_custom_id is not None:
            result['UserCustomId'] = self.user_custom_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LabelContent') is not None:
            self.label_content = m.get('LabelContent')
        if m.get('LabelId') is not None:
            self.label_id = m.get('LabelId')
        if m.get('SerialNo') is not None:
            self.serial_no = m.get('SerialNo')
        if m.get('UserCustomId') is not None:
            self.user_custom_id = m.get('UserCustomId')
        return self


class ListTrustDevicesResponseBodyData(TeaModel):
    def __init__(
        self,
        model: str = None,
        serial_no: str = None,
        tenant_id: str = None,
        uuid: str = None,
    ):
        self.model = model
        self.serial_no = serial_no
        self.tenant_id = tenant_id
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.model is not None:
            result['Model'] = self.model
        if self.serial_no is not None:
            result['SerialNo'] = self.serial_no
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('SerialNo') is not None:
            self.serial_no = m.get('SerialNo')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class ListTrustDevicesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListTrustDevicesResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListTrustDevicesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListTrustDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTrustDevicesResponseBody = None,
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
            temp_model = ListTrustDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserFbAcIssuesRequest(TeaModel):
    def __init__(
        self,
        account: str = None,
        client_version: str = None,
        error_message: str = None,
        instance_id: str = None,
        issue_id: str = None,
        label: str = None,
        reserved_a: str = None,
        reserved_b: str = None,
        user_email: str = None,
    ):
        self.account = account
        self.client_version = client_version
        self.error_message = error_message
        self.instance_id = instance_id
        self.issue_id = issue_id
        self.label = label
        self.reserved_a = reserved_a
        self.reserved_b = reserved_b
        self.user_email = user_email

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.issue_id is not None:
            result['IssueId'] = self.issue_id
        if self.label is not None:
            result['Label'] = self.label
        if self.reserved_a is not None:
            result['ReservedA'] = self.reserved_a
        if self.reserved_b is not None:
            result['ReservedB'] = self.reserved_b
        if self.user_email is not None:
            result['UserEmail'] = self.user_email
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IssueId') is not None:
            self.issue_id = m.get('IssueId')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('ReservedA') is not None:
            self.reserved_a = m.get('ReservedA')
        if m.get('ReservedB') is not None:
            self.reserved_b = m.get('ReservedB')
        if m.get('UserEmail') is not None:
            self.user_email = m.get('UserEmail')
        return self


class ListUserFbAcIssuesResponseBodyDataIssueDataListFileList(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_size: int = None,
        file_type: int = None,
        session_id: str = None,
    ):
        self.file_name = file_name
        self.file_size = file_size
        self.file_type = file_type
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class ListUserFbAcIssuesResponseBodyDataIssueDataList(TeaModel):
    def __init__(
        self,
        account: str = None,
        client_version: str = None,
        error_message: str = None,
        file_list: List[ListUserFbAcIssuesResponseBodyDataIssueDataListFileList] = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        instance_id: str = None,
        issue_id: int = None,
        label: str = None,
        reserved_a: str = None,
        reserved_b: str = None,
        user_email: str = None,
    ):
        self.account = account
        self.client_version = client_version
        self.error_message = error_message
        self.file_list = file_list
        self.gmt_created = gmt_created
        self.gmt_modified = gmt_modified
        self.instance_id = instance_id
        self.issue_id = issue_id
        self.label = label
        self.reserved_a = reserved_a
        self.reserved_b = reserved_b
        self.user_email = user_email

    def validate(self):
        if self.file_list:
            for k in self.file_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        result['FileList'] = []
        if self.file_list is not None:
            for k in self.file_list:
                result['FileList'].append(k.to_map() if k else None)
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.issue_id is not None:
            result['IssueId'] = self.issue_id
        if self.label is not None:
            result['Label'] = self.label
        if self.reserved_a is not None:
            result['ReservedA'] = self.reserved_a
        if self.reserved_b is not None:
            result['ReservedB'] = self.reserved_b
        if self.user_email is not None:
            result['UserEmail'] = self.user_email
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        self.file_list = []
        if m.get('FileList') is not None:
            for k in m.get('FileList'):
                temp_model = ListUserFbAcIssuesResponseBodyDataIssueDataListFileList()
                self.file_list.append(temp_model.from_map(k))
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IssueId') is not None:
            self.issue_id = m.get('IssueId')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('ReservedA') is not None:
            self.reserved_a = m.get('ReservedA')
        if m.get('ReservedB') is not None:
            self.reserved_b = m.get('ReservedB')
        if m.get('UserEmail') is not None:
            self.user_email = m.get('UserEmail')
        return self


class ListUserFbAcIssuesResponseBodyData(TeaModel):
    def __init__(
        self,
        issue_data_list: List[ListUserFbAcIssuesResponseBodyDataIssueDataList] = None,
        total_count: int = None,
    ):
        self.issue_data_list = issue_data_list
        self.total_count = total_count

    def validate(self):
        if self.issue_data_list:
            for k in self.issue_data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['IssueDataList'] = []
        if self.issue_data_list is not None:
            for k in self.issue_data_list:
                result['IssueDataList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.issue_data_list = []
        if m.get('IssueDataList') is not None:
            for k in m.get('IssueDataList'):
                temp_model = ListUserFbAcIssuesResponseBodyDataIssueDataList()
                self.issue_data_list.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListUserFbAcIssuesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListUserFbAcIssuesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListUserFbAcIssuesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListUserFbAcIssuesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUserFbAcIssuesResponseBody = None,
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
            temp_model = ListUserFbAcIssuesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserFbIssuesRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        client_id: str = None,
        client_model: str = None,
        client_sn: str = None,
        customer_id: str = None,
        description: str = None,
        desktop_id: str = None,
        error_code: str = None,
        error_msg: str = None,
        fb_type: int = None,
        issue_id: int = None,
        issue_label: str = None,
        page_number: int = None,
        page_size: int = None,
        status: int = None,
        title: str = None,
        user_email: str = None,
        user_id: str = None,
        was_read: int = None,
    ):
        self.app_id = app_id
        self.client_id = client_id
        self.client_model = client_model
        self.client_sn = client_sn
        self.customer_id = customer_id
        self.description = description
        self.desktop_id = desktop_id
        self.error_code = error_code
        self.error_msg = error_msg
        self.fb_type = fb_type
        self.issue_id = issue_id
        self.issue_label = issue_label
        self.page_number = page_number
        self.page_size = page_size
        self.status = status
        self.title = title
        self.user_email = user_email
        self.user_id = user_id
        self.was_read = was_read

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_model is not None:
            result['ClientModel'] = self.client_model
        if self.client_sn is not None:
            result['ClientSn'] = self.client_sn
        if self.customer_id is not None:
            result['CustomerId'] = self.customer_id
        if self.description is not None:
            result['Description'] = self.description
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.fb_type is not None:
            result['FbType'] = self.fb_type
        if self.issue_id is not None:
            result['IssueId'] = self.issue_id
        if self.issue_label is not None:
            result['IssueLabel'] = self.issue_label
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        if self.user_email is not None:
            result['UserEmail'] = self.user_email
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.was_read is not None:
            result['WasRead'] = self.was_read
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientModel') is not None:
            self.client_model = m.get('ClientModel')
        if m.get('ClientSn') is not None:
            self.client_sn = m.get('ClientSn')
        if m.get('CustomerId') is not None:
            self.customer_id = m.get('CustomerId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('FbType') is not None:
            self.fb_type = m.get('FbType')
        if m.get('IssueId') is not None:
            self.issue_id = m.get('IssueId')
        if m.get('IssueLabel') is not None:
            self.issue_label = m.get('IssueLabel')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UserEmail') is not None:
            self.user_email = m.get('UserEmail')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WasRead') is not None:
            self.was_read = m.get('WasRead')
        return self


class ListUserFbIssuesResponseBodyDataFeedbackIssueDataFileList(TeaModel):
    def __init__(
        self,
        file_md_5: str = None,
        file_name: str = None,
        file_size: int = None,
        file_type: int = None,
        oss_url: str = None,
    ):
        self.file_md_5 = file_md_5
        self.file_name = file_name
        self.file_size = file_size
        self.file_type = file_type
        self.oss_url = oss_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_md_5 is not None:
            result['FileMd5'] = self.file_md_5
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.oss_url is not None:
            result['OssUrl'] = self.oss_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileMd5') is not None:
            self.file_md_5 = m.get('FileMd5')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('OssUrl') is not None:
            self.oss_url = m.get('OssUrl')
        return self


class ListUserFbIssuesResponseBodyDataFeedbackIssueData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        client_id: str = None,
        client_model: str = None,
        client_sn: str = None,
        customer_id: str = None,
        description: str = None,
        desktop_id: str = None,
        error_code: str = None,
        error_msg: str = None,
        fb_type: int = None,
        file_list: List[ListUserFbIssuesResponseBodyDataFeedbackIssueDataFileList] = None,
        gmt_created: str = None,
        issue_id: int = None,
        issue_label: str = None,
        status: int = None,
        title: str = None,
        user_email: str = None,
        user_id: str = None,
    ):
        self.app_id = app_id
        self.client_id = client_id
        self.client_model = client_model
        self.client_sn = client_sn
        self.customer_id = customer_id
        self.description = description
        self.desktop_id = desktop_id
        self.error_code = error_code
        self.error_msg = error_msg
        self.fb_type = fb_type
        self.file_list = file_list
        self.gmt_created = gmt_created
        self.issue_id = issue_id
        self.issue_label = issue_label
        self.status = status
        self.title = title
        self.user_email = user_email
        self.user_id = user_id

    def validate(self):
        if self.file_list:
            for k in self.file_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_model is not None:
            result['ClientModel'] = self.client_model
        if self.client_sn is not None:
            result['ClientSn'] = self.client_sn
        if self.customer_id is not None:
            result['CustomerId'] = self.customer_id
        if self.description is not None:
            result['Description'] = self.description
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.fb_type is not None:
            result['FbType'] = self.fb_type
        result['FileList'] = []
        if self.file_list is not None:
            for k in self.file_list:
                result['FileList'].append(k.to_map() if k else None)
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.issue_id is not None:
            result['IssueId'] = self.issue_id
        if self.issue_label is not None:
            result['IssueLabel'] = self.issue_label
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        if self.user_email is not None:
            result['UserEmail'] = self.user_email
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientModel') is not None:
            self.client_model = m.get('ClientModel')
        if m.get('ClientSn') is not None:
            self.client_sn = m.get('ClientSn')
        if m.get('CustomerId') is not None:
            self.customer_id = m.get('CustomerId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('FbType') is not None:
            self.fb_type = m.get('FbType')
        self.file_list = []
        if m.get('FileList') is not None:
            for k in m.get('FileList'):
                temp_model = ListUserFbIssuesResponseBodyDataFeedbackIssueDataFileList()
                self.file_list.append(temp_model.from_map(k))
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('IssueId') is not None:
            self.issue_id = m.get('IssueId')
        if m.get('IssueLabel') is not None:
            self.issue_label = m.get('IssueLabel')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UserEmail') is not None:
            self.user_email = m.get('UserEmail')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListUserFbIssuesResponseBodyData(TeaModel):
    def __init__(
        self,
        count: str = None,
        feedback_issue_data: List[ListUserFbIssuesResponseBodyDataFeedbackIssueData] = None,
    ):
        self.count = count
        self.feedback_issue_data = feedback_issue_data

    def validate(self):
        if self.feedback_issue_data:
            for k in self.feedback_issue_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        result['FeedbackIssueData'] = []
        if self.feedback_issue_data is not None:
            for k in self.feedback_issue_data:
                result['FeedbackIssueData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        self.feedback_issue_data = []
        if m.get('FeedbackIssueData') is not None:
            for k in m.get('FeedbackIssueData'):
                temp_model = ListUserFbIssuesResponseBodyDataFeedbackIssueData()
                self.feedback_issue_data.append(temp_model.from_map(k))
        return self


class ListUserFbIssuesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListUserFbIssuesResponseBodyData = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListUserFbIssuesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListUserFbIssuesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUserFbIssuesResponseBody = None,
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
            temp_model = ListUserFbIssuesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDevicesSecureNetworkTypeRequest(TeaModel):
    def __init__(
        self,
        all_devices: int = None,
        secure_network_type: str = None,
        serial_nos: str = None,
    ):
        self.all_devices = all_devices
        # This parameter is required.
        self.secure_network_type = secure_network_type
        self.serial_nos = serial_nos

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all_devices is not None:
            result['AllDevices'] = self.all_devices
        if self.secure_network_type is not None:
            result['SecureNetworkType'] = self.secure_network_type
        if self.serial_nos is not None:
            result['SerialNos'] = self.serial_nos
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllDevices') is not None:
            self.all_devices = m.get('AllDevices')
        if m.get('SecureNetworkType') is not None:
            self.secure_network_type = m.get('SecureNetworkType')
        if m.get('SerialNos') is not None:
            self.serial_nos = m.get('SerialNos')
        return self


class ModifyDevicesSecureNetworkTypeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDevicesSecureNetworkTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDevicesSecureNetworkTypeResponseBody = None,
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
            temp_model = ModifyDevicesSecureNetworkTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySecureNetworkTypeRequest(TeaModel):
    def __init__(
        self,
        secure_network_type: str = None,
        serial_no: str = None,
    ):
        self.secure_network_type = secure_network_type
        # This parameter is required.
        self.serial_no = serial_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.secure_network_type is not None:
            result['SecureNetworkType'] = self.secure_network_type
        if self.serial_no is not None:
            result['SerialNo'] = self.serial_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecureNetworkType') is not None:
            self.secure_network_type = m.get('SecureNetworkType')
        if m.get('SerialNo') is not None:
            self.serial_no = m.get('SerialNo')
        return self


class ModifySecureNetworkTypeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifySecureNetworkTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifySecureNetworkTypeResponseBody = None,
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
            temp_model = ModifySecureNetworkTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RegisterDeviceRequest(TeaModel):
    def __init__(
        self,
        bluetooth: str = None,
        build_id: str = None,
        chip_id: str = None,
        client_id: str = None,
        client_type: int = None,
        cpu: str = None,
        custom_id: str = None,
        ether_mac: str = None,
        memory: str = None,
        model: str = None,
        serial_no: str = None,
        storage: str = None,
        token: str = None,
        wlan: str = None,
    ):
        self.bluetooth = bluetooth
        self.build_id = build_id
        self.chip_id = chip_id
        self.client_id = client_id
        self.client_type = client_type
        self.cpu = cpu
        self.custom_id = custom_id
        self.ether_mac = ether_mac
        self.memory = memory
        self.model = model
        self.serial_no = serial_no
        self.storage = storage
        self.token = token
        self.wlan = wlan

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bluetooth is not None:
            result['Bluetooth'] = self.bluetooth
        if self.build_id is not None:
            result['BuildId'] = self.build_id
        if self.chip_id is not None:
            result['ChipId'] = self.chip_id
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.custom_id is not None:
            result['CustomId'] = self.custom_id
        if self.ether_mac is not None:
            result['EtherMac'] = self.ether_mac
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.model is not None:
            result['Model'] = self.model
        if self.serial_no is not None:
            result['SerialNo'] = self.serial_no
        if self.storage is not None:
            result['Storage'] = self.storage
        if self.token is not None:
            result['Token'] = self.token
        if self.wlan is not None:
            result['Wlan'] = self.wlan
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bluetooth') is not None:
            self.bluetooth = m.get('Bluetooth')
        if m.get('BuildId') is not None:
            self.build_id = m.get('BuildId')
        if m.get('ChipId') is not None:
            self.chip_id = m.get('ChipId')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('CustomId') is not None:
            self.custom_id = m.get('CustomId')
        if m.get('EtherMac') is not None:
            self.ether_mac = m.get('EtherMac')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('SerialNo') is not None:
            self.serial_no = m.get('SerialNo')
        if m.get('Storage') is not None:
            self.storage = m.get('Storage')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('Wlan') is not None:
            self.wlan = m.get('Wlan')
        return self


class RegisterDeviceResponseBodyData(TeaModel):
    def __init__(
        self,
        uuid: str = None,
    ):
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class RegisterDeviceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: RegisterDeviceResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = RegisterDeviceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RegisterDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RegisterDeviceResponseBody = None,
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
            temp_model = RegisterDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReportAppOtaInfoRequest(TeaModel):
    def __init__(
        self,
        base_version: str = None,
        client_type: int = None,
        client_uid: str = None,
        note: str = None,
        os_type: str = None,
        project: str = None,
        status: int = None,
        target_version: str = None,
        task_uid: str = None,
    ):
        self.base_version = base_version
        self.client_type = client_type
        self.client_uid = client_uid
        self.note = note
        self.os_type = os_type
        self.project = project
        self.status = status
        self.target_version = target_version
        self.task_uid = task_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_version is not None:
            result['BaseVersion'] = self.base_version
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        if self.client_uid is not None:
            result['ClientUid'] = self.client_uid
        if self.note is not None:
            result['Note'] = self.note
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.project is not None:
            result['Project'] = self.project
        if self.status is not None:
            result['Status'] = self.status
        if self.target_version is not None:
            result['TargetVersion'] = self.target_version
        if self.task_uid is not None:
            result['TaskUid'] = self.task_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseVersion') is not None:
            self.base_version = m.get('BaseVersion')
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        if m.get('ClientUid') is not None:
            self.client_uid = m.get('ClientUid')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TargetVersion') is not None:
            self.target_version = m.get('TargetVersion')
        if m.get('TaskUid') is not None:
            self.task_uid = m.get('TaskUid')
        return self


class ReportAppOtaInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReportAppOtaInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReportAppOtaInfoResponseBody = None,
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
            temp_model = ReportAppOtaInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReportDeviceOtaInfoRequest(TeaModel):
    def __init__(
        self,
        base_version: str = None,
        device_id: str = None,
        model: str = None,
        note: str = None,
        status: int = None,
        target_version: str = None,
    ):
        self.base_version = base_version
        self.device_id = device_id
        self.model = model
        self.note = note
        self.status = status
        self.target_version = target_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_version is not None:
            result['BaseVersion'] = self.base_version
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.model is not None:
            result['Model'] = self.model
        if self.note is not None:
            result['Note'] = self.note
        if self.status is not None:
            result['Status'] = self.status
        if self.target_version is not None:
            result['TargetVersion'] = self.target_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseVersion') is not None:
            self.base_version = m.get('BaseVersion')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TargetVersion') is not None:
            self.target_version = m.get('TargetVersion')
        return self


class ReportDeviceOtaInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReportDeviceOtaInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReportDeviceOtaInfoResponseBody = None,
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
            temp_model = ReportDeviceOtaInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReportUserFbAcIssueRequestFileList(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_size: int = None,
        file_type: int = None,
        session_id: str = None,
    ):
        # This parameter is required.
        self.file_name = file_name
        self.file_size = file_size
        self.file_type = file_type
        # This parameter is required.
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class ReportUserFbAcIssueRequest(TeaModel):
    def __init__(
        self,
        account: str = None,
        client_version: str = None,
        error_msg: str = None,
        file_list: List[ReportUserFbAcIssueRequestFileList] = None,
        instance_id: str = None,
        labels: str = None,
        reserved_a: str = None,
        reserved_b: str = None,
        user_email: str = None,
    ):
        self.account = account
        self.client_version = client_version
        self.error_msg = error_msg
        self.file_list = file_list
        self.instance_id = instance_id
        self.labels = labels
        self.reserved_a = reserved_a
        self.reserved_b = reserved_b
        self.user_email = user_email

    def validate(self):
        if self.file_list:
            for k in self.file_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        result['FileList'] = []
        if self.file_list is not None:
            for k in self.file_list:
                result['FileList'].append(k.to_map() if k else None)
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.reserved_a is not None:
            result['ReservedA'] = self.reserved_a
        if self.reserved_b is not None:
            result['ReservedB'] = self.reserved_b
        if self.user_email is not None:
            result['UserEmail'] = self.user_email
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        self.file_list = []
        if m.get('FileList') is not None:
            for k in m.get('FileList'):
                temp_model = ReportUserFbAcIssueRequestFileList()
                self.file_list.append(temp_model.from_map(k))
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('ReservedA') is not None:
            self.reserved_a = m.get('ReservedA')
        if m.get('ReservedB') is not None:
            self.reserved_b = m.get('ReservedB')
        if m.get('UserEmail') is not None:
            self.user_email = m.get('UserEmail')
        return self


class ReportUserFbAcIssueShrinkRequest(TeaModel):
    def __init__(
        self,
        account: str = None,
        client_version: str = None,
        error_msg: str = None,
        file_list_shrink: str = None,
        instance_id: str = None,
        labels: str = None,
        reserved_a: str = None,
        reserved_b: str = None,
        user_email: str = None,
    ):
        self.account = account
        self.client_version = client_version
        self.error_msg = error_msg
        self.file_list_shrink = file_list_shrink
        self.instance_id = instance_id
        self.labels = labels
        self.reserved_a = reserved_a
        self.reserved_b = reserved_b
        self.user_email = user_email

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.file_list_shrink is not None:
            result['FileList'] = self.file_list_shrink
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.reserved_a is not None:
            result['ReservedA'] = self.reserved_a
        if self.reserved_b is not None:
            result['ReservedB'] = self.reserved_b
        if self.user_email is not None:
            result['UserEmail'] = self.user_email
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('FileList') is not None:
            self.file_list_shrink = m.get('FileList')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('ReservedA') is not None:
            self.reserved_a = m.get('ReservedA')
        if m.get('ReservedB') is not None:
            self.reserved_b = m.get('ReservedB')
        if m.get('UserEmail') is not None:
            self.user_email = m.get('UserEmail')
        return self


class ReportUserFbAcIssueResponseBodyData(TeaModel):
    def __init__(
        self,
        issue_id: int = None,
    ):
        self.issue_id = issue_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.issue_id is not None:
            result['IssueId'] = self.issue_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IssueId') is not None:
            self.issue_id = m.get('IssueId')
        return self


class ReportUserFbAcIssueResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ReportUserFbAcIssueResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ReportUserFbAcIssueResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReportUserFbAcIssueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReportUserFbAcIssueResponseBody = None,
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
            temp_model = ReportUserFbAcIssueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReportUserFbIssueRequestFileList(TeaModel):
    def __init__(
        self,
        file_md_5: str = None,
        file_name: str = None,
        file_size: int = None,
        file_type: int = None,
        oss_url: str = None,
        session_id: str = None,
    ):
        self.file_md_5 = file_md_5
        # This parameter is required.
        self.file_name = file_name
        self.file_size = file_size
        self.file_type = file_type
        self.oss_url = oss_url
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_md_5 is not None:
            result['FileMd5'] = self.file_md_5
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.oss_url is not None:
            result['OssUrl'] = self.oss_url
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileMd5') is not None:
            self.file_md_5 = m.get('FileMd5')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('OssUrl') is not None:
            self.oss_url = m.get('OssUrl')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class ReportUserFbIssueRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        client_id: str = None,
        client_model: str = None,
        client_os_name: str = None,
        client_sn: str = None,
        client_version: str = None,
        customer_id: str = None,
        description: str = None,
        desktop_id: str = None,
        desktop_type: int = None,
        error_code: str = None,
        error_msg: str = None,
        fb_type: int = None,
        file_list: List[ReportUserFbIssueRequestFileList] = None,
        issue_label: str = None,
        occur_time: int = None,
        reserved_a: str = None,
        reserved_b: str = None,
        tel_no: str = None,
        title: str = None,
        user_email: str = None,
        user_id: str = None,
        user_name: str = None,
        workspace_id: str = None,
        wy_id: str = None,
    ):
        self.app_id = app_id
        self.client_id = client_id
        self.client_model = client_model
        self.client_os_name = client_os_name
        self.client_sn = client_sn
        self.client_version = client_version
        self.customer_id = customer_id
        self.description = description
        self.desktop_id = desktop_id
        self.desktop_type = desktop_type
        self.error_code = error_code
        self.error_msg = error_msg
        self.fb_type = fb_type
        self.file_list = file_list
        self.issue_label = issue_label
        self.occur_time = occur_time
        self.reserved_a = reserved_a
        self.reserved_b = reserved_b
        self.tel_no = tel_no
        self.title = title
        self.user_email = user_email
        self.user_id = user_id
        self.user_name = user_name
        self.workspace_id = workspace_id
        self.wy_id = wy_id

    def validate(self):
        if self.file_list:
            for k in self.file_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_model is not None:
            result['ClientModel'] = self.client_model
        if self.client_os_name is not None:
            result['ClientOsName'] = self.client_os_name
        if self.client_sn is not None:
            result['ClientSn'] = self.client_sn
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.customer_id is not None:
            result['CustomerId'] = self.customer_id
        if self.description is not None:
            result['Description'] = self.description
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.desktop_type is not None:
            result['DesktopType'] = self.desktop_type
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.fb_type is not None:
            result['FbType'] = self.fb_type
        result['FileList'] = []
        if self.file_list is not None:
            for k in self.file_list:
                result['FileList'].append(k.to_map() if k else None)
        if self.issue_label is not None:
            result['IssueLabel'] = self.issue_label
        if self.occur_time is not None:
            result['OccurTime'] = self.occur_time
        if self.reserved_a is not None:
            result['ReservedA'] = self.reserved_a
        if self.reserved_b is not None:
            result['ReservedB'] = self.reserved_b
        if self.tel_no is not None:
            result['TelNo'] = self.tel_no
        if self.title is not None:
            result['Title'] = self.title
        if self.user_email is not None:
            result['UserEmail'] = self.user_email
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.wy_id is not None:
            result['WyId'] = self.wy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientModel') is not None:
            self.client_model = m.get('ClientModel')
        if m.get('ClientOsName') is not None:
            self.client_os_name = m.get('ClientOsName')
        if m.get('ClientSn') is not None:
            self.client_sn = m.get('ClientSn')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('CustomerId') is not None:
            self.customer_id = m.get('CustomerId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('DesktopType') is not None:
            self.desktop_type = m.get('DesktopType')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('FbType') is not None:
            self.fb_type = m.get('FbType')
        self.file_list = []
        if m.get('FileList') is not None:
            for k in m.get('FileList'):
                temp_model = ReportUserFbIssueRequestFileList()
                self.file_list.append(temp_model.from_map(k))
        if m.get('IssueLabel') is not None:
            self.issue_label = m.get('IssueLabel')
        if m.get('OccurTime') is not None:
            self.occur_time = m.get('OccurTime')
        if m.get('ReservedA') is not None:
            self.reserved_a = m.get('ReservedA')
        if m.get('ReservedB') is not None:
            self.reserved_b = m.get('ReservedB')
        if m.get('TelNo') is not None:
            self.tel_no = m.get('TelNo')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UserEmail') is not None:
            self.user_email = m.get('UserEmail')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WyId') is not None:
            self.wy_id = m.get('WyId')
        return self


class ReportUserFbIssueShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        client_id: str = None,
        client_model: str = None,
        client_os_name: str = None,
        client_sn: str = None,
        client_version: str = None,
        customer_id: str = None,
        description: str = None,
        desktop_id: str = None,
        desktop_type: int = None,
        error_code: str = None,
        error_msg: str = None,
        fb_type: int = None,
        file_list_shrink: str = None,
        issue_label: str = None,
        occur_time: int = None,
        reserved_a: str = None,
        reserved_b: str = None,
        tel_no: str = None,
        title: str = None,
        user_email: str = None,
        user_id: str = None,
        user_name: str = None,
        workspace_id: str = None,
        wy_id: str = None,
    ):
        self.app_id = app_id
        self.client_id = client_id
        self.client_model = client_model
        self.client_os_name = client_os_name
        self.client_sn = client_sn
        self.client_version = client_version
        self.customer_id = customer_id
        self.description = description
        self.desktop_id = desktop_id
        self.desktop_type = desktop_type
        self.error_code = error_code
        self.error_msg = error_msg
        self.fb_type = fb_type
        self.file_list_shrink = file_list_shrink
        self.issue_label = issue_label
        self.occur_time = occur_time
        self.reserved_a = reserved_a
        self.reserved_b = reserved_b
        self.tel_no = tel_no
        self.title = title
        self.user_email = user_email
        self.user_id = user_id
        self.user_name = user_name
        self.workspace_id = workspace_id
        self.wy_id = wy_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_model is not None:
            result['ClientModel'] = self.client_model
        if self.client_os_name is not None:
            result['ClientOsName'] = self.client_os_name
        if self.client_sn is not None:
            result['ClientSn'] = self.client_sn
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.customer_id is not None:
            result['CustomerId'] = self.customer_id
        if self.description is not None:
            result['Description'] = self.description
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.desktop_type is not None:
            result['DesktopType'] = self.desktop_type
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.fb_type is not None:
            result['FbType'] = self.fb_type
        if self.file_list_shrink is not None:
            result['FileList'] = self.file_list_shrink
        if self.issue_label is not None:
            result['IssueLabel'] = self.issue_label
        if self.occur_time is not None:
            result['OccurTime'] = self.occur_time
        if self.reserved_a is not None:
            result['ReservedA'] = self.reserved_a
        if self.reserved_b is not None:
            result['ReservedB'] = self.reserved_b
        if self.tel_no is not None:
            result['TelNo'] = self.tel_no
        if self.title is not None:
            result['Title'] = self.title
        if self.user_email is not None:
            result['UserEmail'] = self.user_email
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.wy_id is not None:
            result['WyId'] = self.wy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientModel') is not None:
            self.client_model = m.get('ClientModel')
        if m.get('ClientOsName') is not None:
            self.client_os_name = m.get('ClientOsName')
        if m.get('ClientSn') is not None:
            self.client_sn = m.get('ClientSn')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('CustomerId') is not None:
            self.customer_id = m.get('CustomerId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('DesktopType') is not None:
            self.desktop_type = m.get('DesktopType')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('FbType') is not None:
            self.fb_type = m.get('FbType')
        if m.get('FileList') is not None:
            self.file_list_shrink = m.get('FileList')
        if m.get('IssueLabel') is not None:
            self.issue_label = m.get('IssueLabel')
        if m.get('OccurTime') is not None:
            self.occur_time = m.get('OccurTime')
        if m.get('ReservedA') is not None:
            self.reserved_a = m.get('ReservedA')
        if m.get('ReservedB') is not None:
            self.reserved_b = m.get('ReservedB')
        if m.get('TelNo') is not None:
            self.tel_no = m.get('TelNo')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UserEmail') is not None:
            self.user_email = m.get('UserEmail')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WyId') is not None:
            self.wy_id = m.get('WyId')
        return self


class ReportUserFbIssueResponseBodyData(TeaModel):
    def __init__(
        self,
        issue_id: int = None,
    ):
        self.issue_id = issue_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.issue_id is not None:
            result['IssueId'] = self.issue_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IssueId') is not None:
            self.issue_id = m.get('IssueId')
        return self


class ReportUserFbIssueResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ReportUserFbIssueResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ReportUserFbIssueResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReportUserFbIssueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReportUserFbIssueResponseBody = None,
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
            temp_model = ReportUserFbIssueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendOpsMessageToTerminalsRequest(TeaModel):
    def __init__(
        self,
        delay: bool = None,
        msg: str = None,
        ops_action: str = None,
        uuids: List[str] = None,
        wait_for_ack: bool = None,
    ):
        self.delay = delay
        self.msg = msg
        self.ops_action = ops_action
        self.uuids = uuids
        self.wait_for_ack = wait_for_ack

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delay is not None:
            result['Delay'] = self.delay
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.ops_action is not None:
            result['OpsAction'] = self.ops_action
        if self.uuids is not None:
            result['Uuids'] = self.uuids
        if self.wait_for_ack is not None:
            result['WaitForAck'] = self.wait_for_ack
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Delay') is not None:
            self.delay = m.get('Delay')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('OpsAction') is not None:
            self.ops_action = m.get('OpsAction')
        if m.get('Uuids') is not None:
            self.uuids = m.get('Uuids')
        if m.get('WaitForAck') is not None:
            self.wait_for_ack = m.get('WaitForAck')
        return self


class SendOpsMessageToTerminalsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SendOpsMessageToTerminalsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendOpsMessageToTerminalsResponseBody = None,
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
            temp_model = SendOpsMessageToTerminalsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDeviceOtaAutoStatusRequest(TeaModel):
    def __init__(
        self,
        auto_update: int = None,
        auto_update_time_schedule: str = None,
        client_type: int = None,
        force_upgrade: int = None,
        status: str = None,
    ):
        self.auto_update = auto_update
        self.auto_update_time_schedule = auto_update_time_schedule
        self.client_type = client_type
        self.force_upgrade = force_upgrade
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_update is not None:
            result['AutoUpdate'] = self.auto_update
        if self.auto_update_time_schedule is not None:
            result['AutoUpdateTimeSchedule'] = self.auto_update_time_schedule
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        if self.force_upgrade is not None:
            result['ForceUpgrade'] = self.force_upgrade
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoUpdate') is not None:
            self.auto_update = m.get('AutoUpdate')
        if m.get('AutoUpdateTimeSchedule') is not None:
            self.auto_update_time_schedule = m.get('AutoUpdateTimeSchedule')
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        if m.get('ForceUpgrade') is not None:
            self.force_upgrade = m.get('ForceUpgrade')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class SetDeviceOtaAutoStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetDeviceOtaAutoStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetDeviceOtaAutoStatusResponseBody = None,
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
            temp_model = SetDeviceOtaAutoStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDeviceOtaTaskStatusRequest(TeaModel):
    def __init__(
        self,
        operation_status: int = None,
        task_id: int = None,
    ):
        # This parameter is required.
        self.operation_status = operation_status
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation_status is not None:
            result['OperationStatus'] = self.operation_status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperationStatus') is not None:
            self.operation_status = m.get('OperationStatus')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class SetDeviceOtaTaskStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetDeviceOtaTaskStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetDeviceOtaTaskStatusResponseBody = None,
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
            temp_model = SetDeviceOtaTaskStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindAccountLessLoginUserRequest(TeaModel):
    def __init__(
        self,
        serial_number: str = None,
        uuid: str = None,
    ):
        self.serial_number = serial_number
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class UnbindAccountLessLoginUserResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UnbindAccountLessLoginUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UnbindAccountLessLoginUserResponseBody = None,
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
            temp_model = UnbindAccountLessLoginUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindDeviceSeatsRequest(TeaModel):
    def __init__(
        self,
        serial_no_list: List[str] = None,
    ):
        self.serial_no_list = serial_no_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.serial_no_list is not None:
            result['SerialNoList'] = self.serial_no_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SerialNoList') is not None:
            self.serial_no_list = m.get('SerialNoList')
        return self


class UnbindDeviceSeatsShrinkRequest(TeaModel):
    def __init__(
        self,
        serial_no_list_shrink: str = None,
    ):
        self.serial_no_list_shrink = serial_no_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.serial_no_list_shrink is not None:
            result['SerialNoList'] = self.serial_no_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SerialNoList') is not None:
            self.serial_no_list_shrink = m.get('SerialNoList')
        return self


class UnbindDeviceSeatsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UnbindDeviceSeatsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UnbindDeviceSeatsResponseBody = None,
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
            temp_model = UnbindDeviceSeatsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAliasRequest(TeaModel):
    def __init__(
        self,
        alias: str = None,
        serial_no: str = None,
        uuid: str = None,
    ):
        self.alias = alias
        self.serial_no = serial_no
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.serial_no is not None:
            result['SerialNo'] = self.serial_no
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('SerialNo') is not None:
            self.serial_no = m.get('SerialNo')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class UpdateAliasResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAliasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateAliasResponseBody = None,
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
            temp_model = UpdateAliasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDeviceBindedEndUserRequestSourceAdEndUsers(TeaModel):
    def __init__(
        self,
        ad_domain: str = None,
        directory_id: str = None,
        end_user_id: str = None,
    ):
        self.ad_domain = ad_domain
        self.directory_id = directory_id
        self.end_user_id = end_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ad_domain is not None:
            result['AdDomain'] = self.ad_domain
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdDomain') is not None:
            self.ad_domain = m.get('AdDomain')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        return self


class UpdateDeviceBindedEndUserRequestTargetAdEndUsers(TeaModel):
    def __init__(
        self,
        ad_domain: str = None,
        directory_id: str = None,
        end_user_id: str = None,
    ):
        self.ad_domain = ad_domain
        self.directory_id = directory_id
        self.end_user_id = end_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ad_domain is not None:
            result['AdDomain'] = self.ad_domain
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdDomain') is not None:
            self.ad_domain = m.get('AdDomain')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        return self


class UpdateDeviceBindedEndUserRequest(TeaModel):
    def __init__(
        self,
        serial_no: str = None,
        source_ad_end_users: List[UpdateDeviceBindedEndUserRequestSourceAdEndUsers] = None,
        source_end_user_ids: str = None,
        target_ad_end_users: List[UpdateDeviceBindedEndUserRequestTargetAdEndUsers] = None,
        target_end_user_ids: str = None,
        user_type: str = None,
    ):
        # This parameter is required.
        self.serial_no = serial_no
        self.source_ad_end_users = source_ad_end_users
        self.source_end_user_ids = source_end_user_ids
        self.target_ad_end_users = target_ad_end_users
        self.target_end_user_ids = target_end_user_ids
        self.user_type = user_type

    def validate(self):
        if self.source_ad_end_users:
            for k in self.source_ad_end_users:
                if k:
                    k.validate()
        if self.target_ad_end_users:
            for k in self.target_ad_end_users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.serial_no is not None:
            result['SerialNo'] = self.serial_no
        result['SourceAdEndUsers'] = []
        if self.source_ad_end_users is not None:
            for k in self.source_ad_end_users:
                result['SourceAdEndUsers'].append(k.to_map() if k else None)
        if self.source_end_user_ids is not None:
            result['SourceEndUserIds'] = self.source_end_user_ids
        result['TargetAdEndUsers'] = []
        if self.target_ad_end_users is not None:
            for k in self.target_ad_end_users:
                result['TargetAdEndUsers'].append(k.to_map() if k else None)
        if self.target_end_user_ids is not None:
            result['TargetEndUserIds'] = self.target_end_user_ids
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SerialNo') is not None:
            self.serial_no = m.get('SerialNo')
        self.source_ad_end_users = []
        if m.get('SourceAdEndUsers') is not None:
            for k in m.get('SourceAdEndUsers'):
                temp_model = UpdateDeviceBindedEndUserRequestSourceAdEndUsers()
                self.source_ad_end_users.append(temp_model.from_map(k))
        if m.get('SourceEndUserIds') is not None:
            self.source_end_user_ids = m.get('SourceEndUserIds')
        self.target_ad_end_users = []
        if m.get('TargetAdEndUsers') is not None:
            for k in m.get('TargetAdEndUsers'):
                temp_model = UpdateDeviceBindedEndUserRequestTargetAdEndUsers()
                self.target_ad_end_users.append(temp_model.from_map(k))
        if m.get('TargetEndUserIds') is not None:
            self.target_end_user_ids = m.get('TargetEndUserIds')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class UpdateDeviceBindedEndUserResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateDeviceBindedEndUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDeviceBindedEndUserResponseBody = None,
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
            temp_model = UpdateDeviceBindedEndUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLabelRequest(TeaModel):
    def __init__(
        self,
        label_content: str = None,
        label_id: str = None,
    ):
        self.label_content = label_content
        self.label_id = label_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_content is not None:
            result['LabelContent'] = self.label_content
        if self.label_id is not None:
            result['LabelId'] = self.label_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LabelContent') is not None:
            self.label_content = m.get('LabelContent')
        if m.get('LabelId') is not None:
            self.label_id = m.get('LabelId')
        return self


class UpdateLabelResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateLabelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateLabelResponseBody = None,
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
            temp_model = UpdateLabelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTerminalPolicyRequest(TeaModel):
    def __init__(
        self,
        display_layout: str = None,
        display_resolution: str = None,
        display_scale_ratio: str = None,
        enable_auto_lock_screen: int = None,
        enable_auto_login: int = None,
        enable_bluetooth: int = None,
        enable_modify_password: int = None,
        enable_scheduled_shutdown: int = None,
        enable_switch_personal: int = None,
        enable_wlan: int = None,
        idle_timeout: int = None,
        idle_timeout_action: int = None,
        name: str = None,
        power_button_define: int = None,
        power_button_define_for_as: int = None,
        power_button_define_for_ns: int = None,
        power_on_behavior: int = None,
        scheduled_shutdown: str = None,
        setting_lock: int = None,
        terminal_policy_id: str = None,
    ):
        self.display_layout = display_layout
        self.display_resolution = display_resolution
        self.display_scale_ratio = display_scale_ratio
        self.enable_auto_lock_screen = enable_auto_lock_screen
        self.enable_auto_login = enable_auto_login
        self.enable_bluetooth = enable_bluetooth
        self.enable_modify_password = enable_modify_password
        self.enable_scheduled_shutdown = enable_scheduled_shutdown
        self.enable_switch_personal = enable_switch_personal
        self.enable_wlan = enable_wlan
        self.idle_timeout = idle_timeout
        self.idle_timeout_action = idle_timeout_action
        self.name = name
        self.power_button_define = power_button_define
        self.power_button_define_for_as = power_button_define_for_as
        self.power_button_define_for_ns = power_button_define_for_ns
        self.power_on_behavior = power_on_behavior
        self.scheduled_shutdown = scheduled_shutdown
        self.setting_lock = setting_lock
        self.terminal_policy_id = terminal_policy_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_layout is not None:
            result['DisplayLayout'] = self.display_layout
        if self.display_resolution is not None:
            result['DisplayResolution'] = self.display_resolution
        if self.display_scale_ratio is not None:
            result['DisplayScaleRatio'] = self.display_scale_ratio
        if self.enable_auto_lock_screen is not None:
            result['EnableAutoLockScreen'] = self.enable_auto_lock_screen
        if self.enable_auto_login is not None:
            result['EnableAutoLogin'] = self.enable_auto_login
        if self.enable_bluetooth is not None:
            result['EnableBluetooth'] = self.enable_bluetooth
        if self.enable_modify_password is not None:
            result['EnableModifyPassword'] = self.enable_modify_password
        if self.enable_scheduled_shutdown is not None:
            result['EnableScheduledShutdown'] = self.enable_scheduled_shutdown
        if self.enable_switch_personal is not None:
            result['EnableSwitchPersonal'] = self.enable_switch_personal
        if self.enable_wlan is not None:
            result['EnableWlan'] = self.enable_wlan
        if self.idle_timeout is not None:
            result['IdleTimeout'] = self.idle_timeout
        if self.idle_timeout_action is not None:
            result['IdleTimeoutAction'] = self.idle_timeout_action
        if self.name is not None:
            result['Name'] = self.name
        if self.power_button_define is not None:
            result['PowerButtonDefine'] = self.power_button_define
        if self.power_button_define_for_as is not None:
            result['PowerButtonDefineForAs'] = self.power_button_define_for_as
        if self.power_button_define_for_ns is not None:
            result['PowerButtonDefineForNs'] = self.power_button_define_for_ns
        if self.power_on_behavior is not None:
            result['PowerOnBehavior'] = self.power_on_behavior
        if self.scheduled_shutdown is not None:
            result['ScheduledShutdown'] = self.scheduled_shutdown
        if self.setting_lock is not None:
            result['SettingLock'] = self.setting_lock
        if self.terminal_policy_id is not None:
            result['TerminalPolicyId'] = self.terminal_policy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayLayout') is not None:
            self.display_layout = m.get('DisplayLayout')
        if m.get('DisplayResolution') is not None:
            self.display_resolution = m.get('DisplayResolution')
        if m.get('DisplayScaleRatio') is not None:
            self.display_scale_ratio = m.get('DisplayScaleRatio')
        if m.get('EnableAutoLockScreen') is not None:
            self.enable_auto_lock_screen = m.get('EnableAutoLockScreen')
        if m.get('EnableAutoLogin') is not None:
            self.enable_auto_login = m.get('EnableAutoLogin')
        if m.get('EnableBluetooth') is not None:
            self.enable_bluetooth = m.get('EnableBluetooth')
        if m.get('EnableModifyPassword') is not None:
            self.enable_modify_password = m.get('EnableModifyPassword')
        if m.get('EnableScheduledShutdown') is not None:
            self.enable_scheduled_shutdown = m.get('EnableScheduledShutdown')
        if m.get('EnableSwitchPersonal') is not None:
            self.enable_switch_personal = m.get('EnableSwitchPersonal')
        if m.get('EnableWlan') is not None:
            self.enable_wlan = m.get('EnableWlan')
        if m.get('IdleTimeout') is not None:
            self.idle_timeout = m.get('IdleTimeout')
        if m.get('IdleTimeoutAction') is not None:
            self.idle_timeout_action = m.get('IdleTimeoutAction')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PowerButtonDefine') is not None:
            self.power_button_define = m.get('PowerButtonDefine')
        if m.get('PowerButtonDefineForAs') is not None:
            self.power_button_define_for_as = m.get('PowerButtonDefineForAs')
        if m.get('PowerButtonDefineForNs') is not None:
            self.power_button_define_for_ns = m.get('PowerButtonDefineForNs')
        if m.get('PowerOnBehavior') is not None:
            self.power_on_behavior = m.get('PowerOnBehavior')
        if m.get('ScheduledShutdown') is not None:
            self.scheduled_shutdown = m.get('ScheduledShutdown')
        if m.get('SettingLock') is not None:
            self.setting_lock = m.get('SettingLock')
        if m.get('TerminalPolicyId') is not None:
            self.terminal_policy_id = m.get('TerminalPolicyId')
        return self


class UpdateTerminalPolicyResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateTerminalPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateTerminalPolicyResponseBody = None,
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
            temp_model = UpdateTerminalPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


