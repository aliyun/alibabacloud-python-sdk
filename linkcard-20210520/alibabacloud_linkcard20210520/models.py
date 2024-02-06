# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class AddCardToDirectionalGroupRequest(TeaModel):
    def __init__(
        self,
        add_type: str = None,
        api_product: str = None,
        group_id: str = None,
        iccid_list: List[str] = None,
        msg_notify: bool = None,
        serial_no: str = None,
    ):
        self.add_type = add_type
        # Linkcard
        self.api_product = api_product
        self.group_id = group_id
        self.iccid_list = iccid_list
        self.msg_notify = msg_notify
        self.serial_no = serial_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_type is not None:
            result['AddType'] = self.add_type
        if self.api_product is not None:
            result['ApiProduct'] = self.api_product
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.iccid_list is not None:
            result['IccidList'] = self.iccid_list
        if self.msg_notify is not None:
            result['MsgNotify'] = self.msg_notify
        if self.serial_no is not None:
            result['SerialNo'] = self.serial_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddType') is not None:
            self.add_type = m.get('AddType')
        if m.get('ApiProduct') is not None:
            self.api_product = m.get('ApiProduct')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('IccidList') is not None:
            self.iccid_list = m.get('IccidList')
        if m.get('MsgNotify') is not None:
            self.msg_notify = m.get('MsgNotify')
        if m.get('SerialNo') is not None:
            self.serial_no = m.get('SerialNo')
        return self


class AddCardToDirectionalGroupShrinkRequest(TeaModel):
    def __init__(
        self,
        add_type: str = None,
        api_product: str = None,
        group_id: str = None,
        iccid_list_shrink: str = None,
        msg_notify: bool = None,
        serial_no: str = None,
    ):
        self.add_type = add_type
        # Linkcard
        self.api_product = api_product
        self.group_id = group_id
        self.iccid_list_shrink = iccid_list_shrink
        self.msg_notify = msg_notify
        self.serial_no = serial_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_type is not None:
            result['AddType'] = self.add_type
        if self.api_product is not None:
            result['ApiProduct'] = self.api_product
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.iccid_list_shrink is not None:
            result['IccidList'] = self.iccid_list_shrink
        if self.msg_notify is not None:
            result['MsgNotify'] = self.msg_notify
        if self.serial_no is not None:
            result['SerialNo'] = self.serial_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddType') is not None:
            self.add_type = m.get('AddType')
        if m.get('ApiProduct') is not None:
            self.api_product = m.get('ApiProduct')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('IccidList') is not None:
            self.iccid_list_shrink = m.get('IccidList')
        if m.get('MsgNotify') is not None:
            self.msg_notify = m.get('MsgNotify')
        if m.get('SerialNo') is not None:
            self.serial_no = m.get('SerialNo')
        return self


class AddCardToDirectionalGroupResponseBodyData(TeaModel):
    def __init__(
        self,
        result: bool = None,
        serial_no: str = None,
    ):
        self.result = result
        self.serial_no = serial_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.serial_no is not None:
            result['SerialNo'] = self.serial_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('SerialNo') is not None:
            self.serial_no = m.get('SerialNo')
        return self


class AddCardToDirectionalGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: AddCardToDirectionalGroupResponseBodyData = None,
        error_message: str = None,
        localized_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
        self.localized_message = localized_message
        self.request_id = request_id
        self.success = success

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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.localized_message is not None:
            result['LocalizedMessage'] = self.localized_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = AddCardToDirectionalGroupResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('LocalizedMessage') is not None:
            self.localized_message = m.get('LocalizedMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddCardToDirectionalGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddCardToDirectionalGroupResponseBody = None,
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
            temp_model = AddCardToDirectionalGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddDirectionalAddressRequest(TeaModel):
    def __init__(
        self,
        address: str = None,
        address_type: str = None,
        group_id: str = None,
        msg_notify: bool = None,
        serial_no: str = None,
        source: str = None,
        url_insecurity_force: bool = None,
    ):
        self.address = address
        self.address_type = address_type
        self.group_id = group_id
        self.msg_notify = msg_notify
        self.serial_no = serial_no
        self.source = source
        self.url_insecurity_force = url_insecurity_force

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.address_type is not None:
            result['AddressType'] = self.address_type
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.msg_notify is not None:
            result['MsgNotify'] = self.msg_notify
        if self.serial_no is not None:
            result['SerialNo'] = self.serial_no
        if self.source is not None:
            result['Source'] = self.source
        if self.url_insecurity_force is not None:
            result['UrlInsecurityForce'] = self.url_insecurity_force
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('MsgNotify') is not None:
            self.msg_notify = m.get('MsgNotify')
        if m.get('SerialNo') is not None:
            self.serial_no = m.get('SerialNo')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('UrlInsecurityForce') is not None:
            self.url_insecurity_force = m.get('UrlInsecurityForce')
        return self


class AddDirectionalAddressResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        error_message: str = None,
        localized_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
        self.localized_message = localized_message
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
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.localized_message is not None:
            result['LocalizedMessage'] = self.localized_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('LocalizedMessage') is not None:
            self.localized_message = m.get('LocalizedMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddDirectionalAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddDirectionalAddressResponseBody = None,
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
            temp_model = AddDirectionalAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddDirectionalCardRequest(TeaModel):
    def __init__(
        self,
        file_uri: str = None,
        group_id: str = None,
        group_name: str = None,
        order_list: List[str] = None,
        tag_list: List[str] = None,
        upload_method: str = None,
        upload_type: str = None,
    ):
        self.file_uri = file_uri
        self.group_id = group_id
        self.group_name = group_name
        self.order_list = order_list
        self.tag_list = tag_list
        self.upload_method = upload_method
        self.upload_type = upload_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_uri is not None:
            result['FileUri'] = self.file_uri
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.order_list is not None:
            result['OrderList'] = self.order_list
        if self.tag_list is not None:
            result['TagList'] = self.tag_list
        if self.upload_method is not None:
            result['UploadMethod'] = self.upload_method
        if self.upload_type is not None:
            result['UploadType'] = self.upload_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileUri') is not None:
            self.file_uri = m.get('FileUri')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('OrderList') is not None:
            self.order_list = m.get('OrderList')
        if m.get('TagList') is not None:
            self.tag_list = m.get('TagList')
        if m.get('UploadMethod') is not None:
            self.upload_method = m.get('UploadMethod')
        if m.get('UploadType') is not None:
            self.upload_type = m.get('UploadType')
        return self


class AddDirectionalCardShrinkRequest(TeaModel):
    def __init__(
        self,
        file_uri: str = None,
        group_id: str = None,
        group_name: str = None,
        order_list_shrink: str = None,
        tag_list_shrink: str = None,
        upload_method: str = None,
        upload_type: str = None,
    ):
        self.file_uri = file_uri
        self.group_id = group_id
        self.group_name = group_name
        self.order_list_shrink = order_list_shrink
        self.tag_list_shrink = tag_list_shrink
        self.upload_method = upload_method
        self.upload_type = upload_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_uri is not None:
            result['FileUri'] = self.file_uri
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.order_list_shrink is not None:
            result['OrderList'] = self.order_list_shrink
        if self.tag_list_shrink is not None:
            result['TagList'] = self.tag_list_shrink
        if self.upload_method is not None:
            result['UploadMethod'] = self.upload_method
        if self.upload_type is not None:
            result['UploadType'] = self.upload_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileUri') is not None:
            self.file_uri = m.get('FileUri')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('OrderList') is not None:
            self.order_list_shrink = m.get('OrderList')
        if m.get('TagList') is not None:
            self.tag_list_shrink = m.get('TagList')
        if m.get('UploadMethod') is not None:
            self.upload_method = m.get('UploadMethod')
        if m.get('UploadType') is not None:
            self.upload_type = m.get('UploadType')
        return self


class AddDirectionalCardResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        error_message: str = None,
        localized_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
        self.localized_message = localized_message
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
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.localized_message is not None:
            result['LocalizedMessage'] = self.localized_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('LocalizedMessage') is not None:
            self.localized_message = m.get('LocalizedMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddDirectionalCardResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddDirectionalCardResponseBody = None,
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
            temp_model = AddDirectionalCardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddDirectionalGroupRequest(TeaModel):
    def __init__(
        self,
        group_name: str = None,
    ):
        self.group_name = group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class AddDirectionalGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: int = None,
        error_message: str = None,
        localized_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
        self.localized_message = localized_message
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
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.localized_message is not None:
            result['LocalizedMessage'] = self.localized_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('LocalizedMessage') is not None:
            self.localized_message = m.get('LocalizedMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddDirectionalGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddDirectionalGroupResponseBody = None,
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
            temp_model = AddDirectionalGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddTagsToCardRequest(TeaModel):
    def __init__(
        self,
        iccid: str = None,
        tag_name_list: List[str] = None,
    ):
        self.iccid = iccid
        self.tag_name_list = tag_name_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        if self.tag_name_list is not None:
            result['TagNameList'] = self.tag_name_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        if m.get('TagNameList') is not None:
            self.tag_name_list = m.get('TagNameList')
        return self


class AddTagsToCardShrinkRequest(TeaModel):
    def __init__(
        self,
        iccid: str = None,
        tag_name_list_shrink: str = None,
    ):
        self.iccid = iccid
        self.tag_name_list_shrink = tag_name_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        if self.tag_name_list_shrink is not None:
            result['TagNameList'] = self.tag_name_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        if m.get('TagNameList') is not None:
            self.tag_name_list_shrink = m.get('TagNameList')
        return self


class AddTagsToCardResponseBodyData(TeaModel):
    def __init__(
        self,
        tag_id: str = None,
        tag_name: str = None,
    ):
        self.tag_id = tag_id
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class AddTagsToCardResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[AddTagsToCardResponseBodyData] = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = AddTagsToCardResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddTagsToCardResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddTagsToCardResponseBody = None,
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
            temp_model = AddTagsToCardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchAddDirectionalAddressRequest(TeaModel):
    def __init__(
        self,
        address_type: str = None,
        group_id: int = None,
        list_address: List[str] = None,
        source: str = None,
    ):
        self.address_type = address_type
        self.group_id = group_id
        self.list_address = list_address
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_type is not None:
            result['AddressType'] = self.address_type
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.list_address is not None:
            result['ListAddress'] = self.list_address
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('ListAddress') is not None:
            self.list_address = m.get('ListAddress')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class BatchAddDirectionalAddressResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        error_message: str = None,
        localized_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
        self.localized_message = localized_message
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
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.localized_message is not None:
            result['LocalizedMessage'] = self.localized_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('LocalizedMessage') is not None:
            self.localized_message = m.get('LocalizedMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BatchAddDirectionalAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchAddDirectionalAddressResponseBody = None,
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
            temp_model = BatchAddDirectionalAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDirectionalAddressRequest(TeaModel):
    def __init__(
        self,
        address: str = None,
        group_id: str = None,
        msg_notify: bool = None,
        serial_no: str = None,
    ):
        self.address = address
        self.group_id = group_id
        self.msg_notify = msg_notify
        self.serial_no = serial_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.msg_notify is not None:
            result['MsgNotify'] = self.msg_notify
        if self.serial_no is not None:
            result['SerialNo'] = self.serial_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('MsgNotify') is not None:
            self.msg_notify = m.get('MsgNotify')
        if m.get('SerialNo') is not None:
            self.serial_no = m.get('SerialNo')
        return self


class DeleteDirectionalAddressResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        error_message: str = None,
        localized_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
        self.localized_message = localized_message
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
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.localized_message is not None:
            result['LocalizedMessage'] = self.localized_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('LocalizedMessage') is not None:
            self.localized_message = m.get('LocalizedMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteDirectionalAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDirectionalAddressResponseBody = None,
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
            temp_model = DeleteDirectionalAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDirectionalGroupRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
    ):
        self.group_id = group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class DeleteDirectionalGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        error_message: str = None,
        localized_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
        self.localized_message = localized_message
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
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.localized_message is not None:
            result['LocalizedMessage'] = self.localized_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('LocalizedMessage') is not None:
            self.localized_message = m.get('LocalizedMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteDirectionalGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDirectionalGroupResponseBody = None,
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
            temp_model = DeleteDirectionalGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ForceActivationRequest(TeaModel):
    def __init__(
        self,
        date_type: str = None,
        iccid: str = None,
    ):
        self.date_type = date_type
        self.iccid = iccid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date_type is not None:
            result['DateType'] = self.date_type
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DateType') is not None:
            self.date_type = m.get('DateType')
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        return self


class ForceActivationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        error_message: str = None,
        localized_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
        self.localized_message = localized_message
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
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.localized_message is not None:
            result['LocalizedMessage'] = self.localized_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('LocalizedMessage') is not None:
            self.localized_message = m.get('LocalizedMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ForceActivationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ForceActivationResponseBody = None,
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
            temp_model = ForceActivationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCardDetailRequest(TeaModel):
    def __init__(
        self,
        destroy_card: bool = None,
        iccid: str = None,
        instance_id: str = None,
        show_psim: bool = None,
    ):
        self.destroy_card = destroy_card
        self.iccid = iccid
        self.instance_id = instance_id
        self.show_psim = show_psim

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destroy_card is not None:
            result['DestroyCard'] = self.destroy_card
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.show_psim is not None:
            result['ShowPsim'] = self.show_psim
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestroyCard') is not None:
            self.destroy_card = m.get('DestroyCard')
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ShowPsim') is not None:
            self.show_psim = m.get('ShowPsim')
        return self


class GetCardDetailResponseBodyDataListPsimCards(TeaModel):
    def __init__(
        self,
        apn_name: str = None,
        certify_status: str = None,
        iccid: str = None,
        imsi: List[str] = None,
        ip: List[str] = None,
        msisdn: List[str] = None,
        open_sms: bool = None,
        os_status: str = None,
        period_add_flow: str = None,
        period_sms_use: str = None,
        private_network_segment: str = None,
        status: str = None,
        vendor: str = None,
    ):
        self.apn_name = apn_name
        self.certify_status = certify_status
        self.iccid = iccid
        self.imsi = imsi
        self.ip = ip
        self.msisdn = msisdn
        self.open_sms = open_sms
        self.os_status = os_status
        self.period_add_flow = period_add_flow
        self.period_sms_use = period_sms_use
        self.private_network_segment = private_network_segment
        self.status = status
        self.vendor = vendor

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apn_name is not None:
            result['ApnName'] = self.apn_name
        if self.certify_status is not None:
            result['CertifyStatus'] = self.certify_status
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        if self.imsi is not None:
            result['Imsi'] = self.imsi
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.msisdn is not None:
            result['Msisdn'] = self.msisdn
        if self.open_sms is not None:
            result['OpenSms'] = self.open_sms
        if self.os_status is not None:
            result['OsStatus'] = self.os_status
        if self.period_add_flow is not None:
            result['PeriodAddFlow'] = self.period_add_flow
        if self.period_sms_use is not None:
            result['PeriodSmsUse'] = self.period_sms_use
        if self.private_network_segment is not None:
            result['PrivateNetworkSegment'] = self.private_network_segment
        if self.status is not None:
            result['Status'] = self.status
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApnName') is not None:
            self.apn_name = m.get('ApnName')
        if m.get('CertifyStatus') is not None:
            self.certify_status = m.get('CertifyStatus')
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        if m.get('Imsi') is not None:
            self.imsi = m.get('Imsi')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Msisdn') is not None:
            self.msisdn = m.get('Msisdn')
        if m.get('OpenSms') is not None:
            self.open_sms = m.get('OpenSms')
        if m.get('OsStatus') is not None:
            self.os_status = m.get('OsStatus')
        if m.get('PeriodAddFlow') is not None:
            self.period_add_flow = m.get('PeriodAddFlow')
        if m.get('PeriodSmsUse') is not None:
            self.period_sms_use = m.get('PeriodSmsUse')
        if m.get('PrivateNetworkSegment') is not None:
            self.private_network_segment = m.get('PrivateNetworkSegment')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        return self


class GetCardDetailResponseBodyDataVsimCardInfoTagList(TeaModel):
    def __init__(
        self,
        id: int = None,
        tag_name: str = None,
    ):
        self.id = id
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class GetCardDetailResponseBodyDataVsimCardInfo(TeaModel):
    def __init__(
        self,
        active_time: str = None,
        active_type: str = None,
        ali_fee: str = None,
        aliyun_order_id: str = None,
        apn_name: str = None,
        auto_limit_resume: bool = None,
        auto_rebind_reuse: bool = None,
        card_limit_speed_threshold: int = None,
        card_limit_stop_threshold: int = None,
        certify_status: str = None,
        certify_type: str = None,
        credential_instance_id: str = None,
        credential_limit_speed_threshold: int = None,
        credential_limit_stop_threshold: int = None,
        credential_no: str = None,
        credential_type: str = None,
        data_level: str = None,
        data_type: str = None,
        device_imei: str = None,
        directional_group_id: str = None,
        directional_group_name: str = None,
        expire_time: str = None,
        flow_threshold_unit: str = None,
        iccid: str = None,
        imsi: List[str] = None,
        ip: List[str] = None,
        is_auto_recharge: bool = None,
        msisdn: List[str] = None,
        notify_id: str = None,
        open_account_time: str = None,
        open_sms: bool = None,
        os_status: str = None,
        period: str = None,
        period_add_flow: str = None,
        period_rest_flow: str = None,
        period_sms_use: str = None,
        private_network_segment: str = None,
        sim_type: str = None,
        status: str = None,
        tag_list: List[GetCardDetailResponseBodyDataVsimCardInfoTagList] = None,
        vendor: str = None,
        vsim_instance_id: int = None,
    ):
        self.active_time = active_time
        self.active_type = active_type
        self.ali_fee = ali_fee
        self.aliyun_order_id = aliyun_order_id
        self.apn_name = apn_name
        self.auto_limit_resume = auto_limit_resume
        self.auto_rebind_reuse = auto_rebind_reuse
        self.card_limit_speed_threshold = card_limit_speed_threshold
        self.card_limit_stop_threshold = card_limit_stop_threshold
        self.certify_status = certify_status
        self.certify_type = certify_type
        self.credential_instance_id = credential_instance_id
        self.credential_limit_speed_threshold = credential_limit_speed_threshold
        self.credential_limit_stop_threshold = credential_limit_stop_threshold
        self.credential_no = credential_no
        self.credential_type = credential_type
        self.data_level = data_level
        self.data_type = data_type
        self.device_imei = device_imei
        self.directional_group_id = directional_group_id
        self.directional_group_name = directional_group_name
        self.expire_time = expire_time
        self.flow_threshold_unit = flow_threshold_unit
        self.iccid = iccid
        self.imsi = imsi
        self.ip = ip
        self.is_auto_recharge = is_auto_recharge
        self.msisdn = msisdn
        self.notify_id = notify_id
        self.open_account_time = open_account_time
        self.open_sms = open_sms
        self.os_status = os_status
        self.period = period
        self.period_add_flow = period_add_flow
        self.period_rest_flow = period_rest_flow
        self.period_sms_use = period_sms_use
        self.private_network_segment = private_network_segment
        self.sim_type = sim_type
        self.status = status
        self.tag_list = tag_list
        self.vendor = vendor
        self.vsim_instance_id = vsim_instance_id

    def validate(self):
        if self.tag_list:
            for k in self.tag_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_time is not None:
            result['ActiveTime'] = self.active_time
        if self.active_type is not None:
            result['ActiveType'] = self.active_type
        if self.ali_fee is not None:
            result['AliFee'] = self.ali_fee
        if self.aliyun_order_id is not None:
            result['AliyunOrderId'] = self.aliyun_order_id
        if self.apn_name is not None:
            result['ApnName'] = self.apn_name
        if self.auto_limit_resume is not None:
            result['AutoLimitResume'] = self.auto_limit_resume
        if self.auto_rebind_reuse is not None:
            result['AutoRebindReuse'] = self.auto_rebind_reuse
        if self.card_limit_speed_threshold is not None:
            result['CardLimitSpeedThreshold'] = self.card_limit_speed_threshold
        if self.card_limit_stop_threshold is not None:
            result['CardLimitStopThreshold'] = self.card_limit_stop_threshold
        if self.certify_status is not None:
            result['CertifyStatus'] = self.certify_status
        if self.certify_type is not None:
            result['CertifyType'] = self.certify_type
        if self.credential_instance_id is not None:
            result['CredentialInstanceId'] = self.credential_instance_id
        if self.credential_limit_speed_threshold is not None:
            result['CredentialLimitSpeedThreshold'] = self.credential_limit_speed_threshold
        if self.credential_limit_stop_threshold is not None:
            result['CredentialLimitStopThreshold'] = self.credential_limit_stop_threshold
        if self.credential_no is not None:
            result['CredentialNo'] = self.credential_no
        if self.credential_type is not None:
            result['CredentialType'] = self.credential_type
        if self.data_level is not None:
            result['DataLevel'] = self.data_level
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.device_imei is not None:
            result['DeviceImei'] = self.device_imei
        if self.directional_group_id is not None:
            result['DirectionalGroupId'] = self.directional_group_id
        if self.directional_group_name is not None:
            result['DirectionalGroupName'] = self.directional_group_name
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.flow_threshold_unit is not None:
            result['FlowThresholdUnit'] = self.flow_threshold_unit
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        if self.imsi is not None:
            result['Imsi'] = self.imsi
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.is_auto_recharge is not None:
            result['IsAutoRecharge'] = self.is_auto_recharge
        if self.msisdn is not None:
            result['Msisdn'] = self.msisdn
        if self.notify_id is not None:
            result['NotifyId'] = self.notify_id
        if self.open_account_time is not None:
            result['OpenAccountTime'] = self.open_account_time
        if self.open_sms is not None:
            result['OpenSms'] = self.open_sms
        if self.os_status is not None:
            result['OsStatus'] = self.os_status
        if self.period is not None:
            result['Period'] = self.period
        if self.period_add_flow is not None:
            result['PeriodAddFlow'] = self.period_add_flow
        if self.period_rest_flow is not None:
            result['PeriodRestFlow'] = self.period_rest_flow
        if self.period_sms_use is not None:
            result['PeriodSmsUse'] = self.period_sms_use
        if self.private_network_segment is not None:
            result['PrivateNetworkSegment'] = self.private_network_segment
        if self.sim_type is not None:
            result['SimType'] = self.sim_type
        if self.status is not None:
            result['Status'] = self.status
        result['TagList'] = []
        if self.tag_list is not None:
            for k in self.tag_list:
                result['TagList'].append(k.to_map() if k else None)
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        if self.vsim_instance_id is not None:
            result['VsimInstanceId'] = self.vsim_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveTime') is not None:
            self.active_time = m.get('ActiveTime')
        if m.get('ActiveType') is not None:
            self.active_type = m.get('ActiveType')
        if m.get('AliFee') is not None:
            self.ali_fee = m.get('AliFee')
        if m.get('AliyunOrderId') is not None:
            self.aliyun_order_id = m.get('AliyunOrderId')
        if m.get('ApnName') is not None:
            self.apn_name = m.get('ApnName')
        if m.get('AutoLimitResume') is not None:
            self.auto_limit_resume = m.get('AutoLimitResume')
        if m.get('AutoRebindReuse') is not None:
            self.auto_rebind_reuse = m.get('AutoRebindReuse')
        if m.get('CardLimitSpeedThreshold') is not None:
            self.card_limit_speed_threshold = m.get('CardLimitSpeedThreshold')
        if m.get('CardLimitStopThreshold') is not None:
            self.card_limit_stop_threshold = m.get('CardLimitStopThreshold')
        if m.get('CertifyStatus') is not None:
            self.certify_status = m.get('CertifyStatus')
        if m.get('CertifyType') is not None:
            self.certify_type = m.get('CertifyType')
        if m.get('CredentialInstanceId') is not None:
            self.credential_instance_id = m.get('CredentialInstanceId')
        if m.get('CredentialLimitSpeedThreshold') is not None:
            self.credential_limit_speed_threshold = m.get('CredentialLimitSpeedThreshold')
        if m.get('CredentialLimitStopThreshold') is not None:
            self.credential_limit_stop_threshold = m.get('CredentialLimitStopThreshold')
        if m.get('CredentialNo') is not None:
            self.credential_no = m.get('CredentialNo')
        if m.get('CredentialType') is not None:
            self.credential_type = m.get('CredentialType')
        if m.get('DataLevel') is not None:
            self.data_level = m.get('DataLevel')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DeviceImei') is not None:
            self.device_imei = m.get('DeviceImei')
        if m.get('DirectionalGroupId') is not None:
            self.directional_group_id = m.get('DirectionalGroupId')
        if m.get('DirectionalGroupName') is not None:
            self.directional_group_name = m.get('DirectionalGroupName')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('FlowThresholdUnit') is not None:
            self.flow_threshold_unit = m.get('FlowThresholdUnit')
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        if m.get('Imsi') is not None:
            self.imsi = m.get('Imsi')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('IsAutoRecharge') is not None:
            self.is_auto_recharge = m.get('IsAutoRecharge')
        if m.get('Msisdn') is not None:
            self.msisdn = m.get('Msisdn')
        if m.get('NotifyId') is not None:
            self.notify_id = m.get('NotifyId')
        if m.get('OpenAccountTime') is not None:
            self.open_account_time = m.get('OpenAccountTime')
        if m.get('OpenSms') is not None:
            self.open_sms = m.get('OpenSms')
        if m.get('OsStatus') is not None:
            self.os_status = m.get('OsStatus')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodAddFlow') is not None:
            self.period_add_flow = m.get('PeriodAddFlow')
        if m.get('PeriodRestFlow') is not None:
            self.period_rest_flow = m.get('PeriodRestFlow')
        if m.get('PeriodSmsUse') is not None:
            self.period_sms_use = m.get('PeriodSmsUse')
        if m.get('PrivateNetworkSegment') is not None:
            self.private_network_segment = m.get('PrivateNetworkSegment')
        if m.get('SimType') is not None:
            self.sim_type = m.get('SimType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tag_list = []
        if m.get('TagList') is not None:
            for k in m.get('TagList'):
                temp_model = GetCardDetailResponseBodyDataVsimCardInfoTagList()
                self.tag_list.append(temp_model.from_map(k))
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        if m.get('VsimInstanceId') is not None:
            self.vsim_instance_id = m.get('VsimInstanceId')
        return self


class GetCardDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        list_psim_cards: List[GetCardDetailResponseBodyDataListPsimCards] = None,
        vsim_card_info: GetCardDetailResponseBodyDataVsimCardInfo = None,
    ):
        self.list_psim_cards = list_psim_cards
        self.vsim_card_info = vsim_card_info

    def validate(self):
        if self.list_psim_cards:
            for k in self.list_psim_cards:
                if k:
                    k.validate()
        if self.vsim_card_info:
            self.vsim_card_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ListPsimCards'] = []
        if self.list_psim_cards is not None:
            for k in self.list_psim_cards:
                result['ListPsimCards'].append(k.to_map() if k else None)
        if self.vsim_card_info is not None:
            result['VsimCardInfo'] = self.vsim_card_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list_psim_cards = []
        if m.get('ListPsimCards') is not None:
            for k in m.get('ListPsimCards'):
                temp_model = GetCardDetailResponseBodyDataListPsimCards()
                self.list_psim_cards.append(temp_model.from_map(k))
        if m.get('VsimCardInfo') is not None:
            temp_model = GetCardDetailResponseBodyDataVsimCardInfo()
            self.vsim_card_info = temp_model.from_map(m['VsimCardInfo'])
        return self


class GetCardDetailResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetCardDetailResponseBodyData = None,
        error_message: str = None,
        localized_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
        self.localized_message = localized_message
        self.request_id = request_id
        self.success = success

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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.localized_message is not None:
            result['LocalizedMessage'] = self.localized_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetCardDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('LocalizedMessage') is not None:
            self.localized_message = m.get('LocalizedMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetCardDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCardDetailResponseBody = None,
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
            temp_model = GetCardDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCardFlowInfoRequest(TeaModel):
    def __init__(
        self,
        date_list: List[str] = None,
        iccid: str = None,
    ):
        self.date_list = date_list
        self.iccid = iccid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date_list is not None:
            result['DateList'] = self.date_list
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DateList') is not None:
            self.date_list = m.get('DateList')
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        return self


class GetCardFlowInfoResponseBodyDataListCardMonthFlowListDayFlow(TeaModel):
    def __init__(
        self,
        day: str = None,
        flow: str = None,
    ):
        self.day = day
        self.flow = flow

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day is not None:
            result['Day'] = self.day
        if self.flow is not None:
            result['Flow'] = self.flow
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Day') is not None:
            self.day = m.get('Day')
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')
        return self


class GetCardFlowInfoResponseBodyDataListCardMonthFlow(TeaModel):
    def __init__(
        self,
        flow_count: str = None,
        list_day_flow: List[GetCardFlowInfoResponseBodyDataListCardMonthFlowListDayFlow] = None,
        month: str = None,
    ):
        self.flow_count = flow_count
        self.list_day_flow = list_day_flow
        self.month = month

    def validate(self):
        if self.list_day_flow:
            for k in self.list_day_flow:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_count is not None:
            result['FlowCount'] = self.flow_count
        result['ListDayFlow'] = []
        if self.list_day_flow is not None:
            for k in self.list_day_flow:
                result['ListDayFlow'].append(k.to_map() if k else None)
        if self.month is not None:
            result['Month'] = self.month
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowCount') is not None:
            self.flow_count = m.get('FlowCount')
        self.list_day_flow = []
        if m.get('ListDayFlow') is not None:
            for k in m.get('ListDayFlow'):
                temp_model = GetCardFlowInfoResponseBodyDataListCardMonthFlowListDayFlow()
                self.list_day_flow.append(temp_model.from_map(k))
        if m.get('Month') is not None:
            self.month = m.get('Month')
        return self


class GetCardFlowInfoResponseBodyDataListPackageDTO(TeaModel):
    def __init__(
        self,
        effective_time: str = None,
        expire_time: str = None,
        package_name: str = None,
        remark: str = None,
    ):
        self.effective_time = effective_time
        self.expire_time = expire_time
        self.package_name = package_name
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.package_name is not None:
            result['PackageName'] = self.package_name
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class GetCardFlowInfoResponseBodyDataListVendorDetail(TeaModel):
    def __init__(
        self,
        net_work_delay: str = None,
        ratio: str = None,
        signal_strength: str = None,
        used_flow: str = None,
        vendor: str = None,
    ):
        self.net_work_delay = net_work_delay
        self.ratio = ratio
        self.signal_strength = signal_strength
        self.used_flow = used_flow
        self.vendor = vendor

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.net_work_delay is not None:
            result['NetWorkDelay'] = self.net_work_delay
        if self.ratio is not None:
            result['Ratio'] = self.ratio
        if self.signal_strength is not None:
            result['SignalStrength'] = self.signal_strength
        if self.used_flow is not None:
            result['UsedFlow'] = self.used_flow
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetWorkDelay') is not None:
            self.net_work_delay = m.get('NetWorkDelay')
        if m.get('Ratio') is not None:
            self.ratio = m.get('Ratio')
        if m.get('SignalStrength') is not None:
            self.signal_strength = m.get('SignalStrength')
        if m.get('UsedFlow') is not None:
            self.used_flow = m.get('UsedFlow')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        return self


class GetCardFlowInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        list_card_month_flow: List[GetCardFlowInfoResponseBodyDataListCardMonthFlow] = None,
        list_package_dto: List[GetCardFlowInfoResponseBodyDataListPackageDTO] = None,
        list_vendor_detail: List[GetCardFlowInfoResponseBodyDataListVendorDetail] = None,
    ):
        self.list_card_month_flow = list_card_month_flow
        self.list_package_dto = list_package_dto
        self.list_vendor_detail = list_vendor_detail

    def validate(self):
        if self.list_card_month_flow:
            for k in self.list_card_month_flow:
                if k:
                    k.validate()
        if self.list_package_dto:
            for k in self.list_package_dto:
                if k:
                    k.validate()
        if self.list_vendor_detail:
            for k in self.list_vendor_detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ListCardMonthFlow'] = []
        if self.list_card_month_flow is not None:
            for k in self.list_card_month_flow:
                result['ListCardMonthFlow'].append(k.to_map() if k else None)
        result['ListPackageDTO'] = []
        if self.list_package_dto is not None:
            for k in self.list_package_dto:
                result['ListPackageDTO'].append(k.to_map() if k else None)
        result['ListVendorDetail'] = []
        if self.list_vendor_detail is not None:
            for k in self.list_vendor_detail:
                result['ListVendorDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list_card_month_flow = []
        if m.get('ListCardMonthFlow') is not None:
            for k in m.get('ListCardMonthFlow'):
                temp_model = GetCardFlowInfoResponseBodyDataListCardMonthFlow()
                self.list_card_month_flow.append(temp_model.from_map(k))
        self.list_package_dto = []
        if m.get('ListPackageDTO') is not None:
            for k in m.get('ListPackageDTO'):
                temp_model = GetCardFlowInfoResponseBodyDataListPackageDTO()
                self.list_package_dto.append(temp_model.from_map(k))
        self.list_vendor_detail = []
        if m.get('ListVendorDetail') is not None:
            for k in m.get('ListVendorDetail'):
                temp_model = GetCardFlowInfoResponseBodyDataListVendorDetail()
                self.list_vendor_detail.append(temp_model.from_map(k))
        return self


class GetCardFlowInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetCardFlowInfoResponseBodyData = None,
        error_message: str = None,
        localized_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
        self.localized_message = localized_message
        self.request_id = request_id
        self.success = success

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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.localized_message is not None:
            result['LocalizedMessage'] = self.localized_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetCardFlowInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('LocalizedMessage') is not None:
            self.localized_message = m.get('LocalizedMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetCardFlowInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCardFlowInfoResponseBody = None,
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
            temp_model = GetCardFlowInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCardLatestFlowRequest(TeaModel):
    def __init__(
        self,
        iccid: str = None,
    ):
        self.iccid = iccid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        return self


class GetCardLatestFlowResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        error_message: str = None,
        localized_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
        self.localized_message = localized_message
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
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.localized_message is not None:
            result['LocalizedMessage'] = self.localized_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('LocalizedMessage') is not None:
            self.localized_message = m.get('LocalizedMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetCardLatestFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCardLatestFlowResponseBody = None,
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
            temp_model = GetCardLatestFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCardRealStatusRequest(TeaModel):
    def __init__(
        self,
        iccid: str = None,
        msisdn: str = None,
        serial_no: List[str] = None,
    ):
        self.iccid = iccid
        self.msisdn = msisdn
        self.serial_no = serial_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        if self.msisdn is not None:
            result['Msisdn'] = self.msisdn
        if self.serial_no is not None:
            result['SerialNo'] = self.serial_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        if m.get('Msisdn') is not None:
            self.msisdn = m.get('Msisdn')
        if m.get('SerialNo') is not None:
            self.serial_no = m.get('SerialNo')
        return self


class GetCardRealStatusShrinkRequest(TeaModel):
    def __init__(
        self,
        iccid: str = None,
        msisdn: str = None,
        serial_no_shrink: str = None,
    ):
        self.iccid = iccid
        self.msisdn = msisdn
        self.serial_no_shrink = serial_no_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        if self.msisdn is not None:
            result['Msisdn'] = self.msisdn
        if self.serial_no_shrink is not None:
            result['SerialNo'] = self.serial_no_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        if m.get('Msisdn') is not None:
            self.msisdn = m.get('Msisdn')
        if m.get('SerialNo') is not None:
            self.serial_no_shrink = m.get('SerialNo')
        return self


class GetCardRealStatusResponseBodyData(TeaModel):
    def __init__(
        self,
        gprs: bool = None,
        iccid: str = None,
        online: bool = None,
        serial_no: str = None,
        status: str = None,
    ):
        self.gprs = gprs
        self.iccid = iccid
        self.online = online
        self.serial_no = serial_no
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gprs is not None:
            result['Gprs'] = self.gprs
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        if self.online is not None:
            result['Online'] = self.online
        if self.serial_no is not None:
            result['SerialNo'] = self.serial_no
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Gprs') is not None:
            self.gprs = m.get('Gprs')
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        if m.get('Online') is not None:
            self.online = m.get('Online')
        if m.get('SerialNo') is not None:
            self.serial_no = m.get('SerialNo')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetCardRealStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetCardRealStatusResponseBodyData] = None,
        error_message: str = None,
        localized_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
        self.localized_message = localized_message
        self.request_id = request_id
        self.success = success

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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.localized_message is not None:
            result['LocalizedMessage'] = self.localized_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetCardRealStatusResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('LocalizedMessage') is not None:
            self.localized_message = m.get('LocalizedMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetCardRealStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCardRealStatusResponseBody = None,
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
            temp_model = GetCardRealStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCardStatusStatisticsResponseBodyDataErrorStopStatisticsDTO(TeaModel):
    def __init__(
        self,
        pool_count: int = None,
        same_flow_card_count: int = None,
        single_card_count: int = None,
        total_count: int = None,
    ):
        self.pool_count = pool_count
        self.same_flow_card_count = same_flow_card_count
        self.single_card_count = single_card_count
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pool_count is not None:
            result['PoolCount'] = self.pool_count
        if self.same_flow_card_count is not None:
            result['SameFlowCardCount'] = self.same_flow_card_count
        if self.single_card_count is not None:
            result['SingleCardCount'] = self.single_card_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PoolCount') is not None:
            self.pool_count = m.get('PoolCount')
        if m.get('SameFlowCardCount') is not None:
            self.same_flow_card_count = m.get('SameFlowCardCount')
        if m.get('SingleCardCount') is not None:
            self.single_card_count = m.get('SingleCardCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetCardStatusStatisticsResponseBodyDataExhaustStopStatisticsDTO(TeaModel):
    def __init__(
        self,
        pool_count: int = None,
        same_flow_card_count: int = None,
        single_card_count: int = None,
        total_count: int = None,
    ):
        self.pool_count = pool_count
        self.same_flow_card_count = same_flow_card_count
        self.single_card_count = single_card_count
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pool_count is not None:
            result['PoolCount'] = self.pool_count
        if self.same_flow_card_count is not None:
            result['SameFlowCardCount'] = self.same_flow_card_count
        if self.single_card_count is not None:
            result['SingleCardCount'] = self.single_card_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PoolCount') is not None:
            self.pool_count = m.get('PoolCount')
        if m.get('SameFlowCardCount') is not None:
            self.same_flow_card_count = m.get('SameFlowCardCount')
        if m.get('SingleCardCount') is not None:
            self.single_card_count = m.get('SingleCardCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetCardStatusStatisticsResponseBodyDataExpireStopStatisticsDTO(TeaModel):
    def __init__(
        self,
        pool_count: int = None,
        same_flow_card_count: int = None,
        single_card_count: int = None,
        total_count: int = None,
    ):
        self.pool_count = pool_count
        self.same_flow_card_count = same_flow_card_count
        self.single_card_count = single_card_count
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pool_count is not None:
            result['PoolCount'] = self.pool_count
        if self.same_flow_card_count is not None:
            result['SameFlowCardCount'] = self.same_flow_card_count
        if self.single_card_count is not None:
            result['SingleCardCount'] = self.single_card_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PoolCount') is not None:
            self.pool_count = m.get('PoolCount')
        if m.get('SameFlowCardCount') is not None:
            self.same_flow_card_count = m.get('SameFlowCardCount')
        if m.get('SingleCardCount') is not None:
            self.single_card_count = m.get('SingleCardCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetCardStatusStatisticsResponseBodyDataFlowOutStatisticsDTO(TeaModel):
    def __init__(
        self,
        pool_count: int = None,
        same_flow_card_count: int = None,
        single_card_count: int = None,
        total_count: int = None,
    ):
        self.pool_count = pool_count
        self.same_flow_card_count = same_flow_card_count
        self.single_card_count = single_card_count
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pool_count is not None:
            result['PoolCount'] = self.pool_count
        if self.same_flow_card_count is not None:
            result['SameFlowCardCount'] = self.same_flow_card_count
        if self.single_card_count is not None:
            result['SingleCardCount'] = self.single_card_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PoolCount') is not None:
            self.pool_count = m.get('PoolCount')
        if m.get('SameFlowCardCount') is not None:
            self.same_flow_card_count = m.get('SameFlowCardCount')
        if m.get('SingleCardCount') is not None:
            self.single_card_count = m.get('SingleCardCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetCardStatusStatisticsResponseBodyDataManageStopStatisticsDTO(TeaModel):
    def __init__(
        self,
        pool_count: int = None,
        same_flow_card_count: int = None,
        single_card_count: int = None,
        total_count: int = None,
    ):
        self.pool_count = pool_count
        self.same_flow_card_count = same_flow_card_count
        self.single_card_count = single_card_count
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pool_count is not None:
            result['PoolCount'] = self.pool_count
        if self.same_flow_card_count is not None:
            result['SameFlowCardCount'] = self.same_flow_card_count
        if self.single_card_count is not None:
            result['SingleCardCount'] = self.single_card_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PoolCount') is not None:
            self.pool_count = m.get('PoolCount')
        if m.get('SameFlowCardCount') is not None:
            self.same_flow_card_count = m.get('SameFlowCardCount')
        if m.get('SingleCardCount') is not None:
            self.single_card_count = m.get('SingleCardCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetCardStatusStatisticsResponseBodyDataRiskWaringStatisticsDTO(TeaModel):
    def __init__(
        self,
        left_flow_percentage_warn_count: int = None,
        stop_count: int = None,
        waring_total_count: int = None,
        warning_count: int = None,
    ):
        self.left_flow_percentage_warn_count = left_flow_percentage_warn_count
        self.stop_count = stop_count
        self.waring_total_count = waring_total_count
        self.warning_count = warning_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.left_flow_percentage_warn_count is not None:
            result['LeftFlowPercentageWarnCount'] = self.left_flow_percentage_warn_count
        if self.stop_count is not None:
            result['StopCount'] = self.stop_count
        if self.waring_total_count is not None:
            result['WaringTotalCount'] = self.waring_total_count
        if self.warning_count is not None:
            result['WarningCount'] = self.warning_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LeftFlowPercentageWarnCount') is not None:
            self.left_flow_percentage_warn_count = m.get('LeftFlowPercentageWarnCount')
        if m.get('StopCount') is not None:
            self.stop_count = m.get('StopCount')
        if m.get('WaringTotalCount') is not None:
            self.waring_total_count = m.get('WaringTotalCount')
        if m.get('WarningCount') is not None:
            self.warning_count = m.get('WarningCount')
        return self


class GetCardStatusStatisticsResponseBodyDataSingCardPeriodLeftFlowWarnDTO(TeaModel):
    def __init__(
        self,
        less_flow_percentage_10count: int = None,
        less_flow_percentage_30count: int = None,
    ):
        self.less_flow_percentage_10count = less_flow_percentage_10count
        self.less_flow_percentage_30count = less_flow_percentage_30count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.less_flow_percentage_10count is not None:
            result['LessFlowPercentage10Count'] = self.less_flow_percentage_10count
        if self.less_flow_percentage_30count is not None:
            result['LessFlowPercentage30Count'] = self.less_flow_percentage_30count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LessFlowPercentage10Count') is not None:
            self.less_flow_percentage_10count = m.get('LessFlowPercentage10Count')
        if m.get('LessFlowPercentage30Count') is not None:
            self.less_flow_percentage_30count = m.get('LessFlowPercentage30Count')
        return self


class GetCardStatusStatisticsResponseBodyDataUnCertifiedStopStatisticsDTO(TeaModel):
    def __init__(
        self,
        pool_count: int = None,
        same_flow_card_count: int = None,
        single_card_count: int = None,
        total_count: int = None,
    ):
        self.pool_count = pool_count
        self.same_flow_card_count = same_flow_card_count
        self.single_card_count = single_card_count
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pool_count is not None:
            result['PoolCount'] = self.pool_count
        if self.same_flow_card_count is not None:
            result['SameFlowCardCount'] = self.same_flow_card_count
        if self.single_card_count is not None:
            result['SingleCardCount'] = self.single_card_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PoolCount') is not None:
            self.pool_count = m.get('PoolCount')
        if m.get('SameFlowCardCount') is not None:
            self.same_flow_card_count = m.get('SameFlowCardCount')
        if m.get('SingleCardCount') is not None:
            self.single_card_count = m.get('SingleCardCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetCardStatusStatisticsResponseBodyDataUnbindResumeStatisticsDTO(TeaModel):
    def __init__(
        self,
        pool_count: int = None,
        same_flow_card_count: int = None,
        single_card_count: int = None,
        total_count: int = None,
    ):
        self.pool_count = pool_count
        self.same_flow_card_count = same_flow_card_count
        self.single_card_count = single_card_count
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pool_count is not None:
            result['PoolCount'] = self.pool_count
        if self.same_flow_card_count is not None:
            result['SameFlowCardCount'] = self.same_flow_card_count
        if self.single_card_count is not None:
            result['SingleCardCount'] = self.single_card_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PoolCount') is not None:
            self.pool_count = m.get('PoolCount')
        if m.get('SameFlowCardCount') is not None:
            self.same_flow_card_count = m.get('SameFlowCardCount')
        if m.get('SingleCardCount') is not None:
            self.single_card_count = m.get('SingleCardCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetCardStatusStatisticsResponseBodyDataWeekWarnStatisticsDTO(TeaModel):
    def __init__(
        self,
        pool_count: int = None,
        same_flow_card_count: int = None,
        single_card_count: int = None,
        total_count: int = None,
    ):
        self.pool_count = pool_count
        self.same_flow_card_count = same_flow_card_count
        self.single_card_count = single_card_count
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pool_count is not None:
            result['PoolCount'] = self.pool_count
        if self.same_flow_card_count is not None:
            result['SameFlowCardCount'] = self.same_flow_card_count
        if self.single_card_count is not None:
            result['SingleCardCount'] = self.single_card_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PoolCount') is not None:
            self.pool_count = m.get('PoolCount')
        if m.get('SameFlowCardCount') is not None:
            self.same_flow_card_count = m.get('SameFlowCardCount')
        if m.get('SingleCardCount') is not None:
            self.single_card_count = m.get('SingleCardCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetCardStatusStatisticsResponseBodyData(TeaModel):
    def __init__(
        self,
        error_stop_statistics_dto: GetCardStatusStatisticsResponseBodyDataErrorStopStatisticsDTO = None,
        exhaust_stop_statistics_dto: GetCardStatusStatisticsResponseBodyDataExhaustStopStatisticsDTO = None,
        expire_stop_statistics_dto: GetCardStatusStatisticsResponseBodyDataExpireStopStatisticsDTO = None,
        flow_out_statistics_dto: GetCardStatusStatisticsResponseBodyDataFlowOutStatisticsDTO = None,
        manage_stop_statistics_dto: GetCardStatusStatisticsResponseBodyDataManageStopStatisticsDTO = None,
        risk_waring_statistics_dto: GetCardStatusStatisticsResponseBodyDataRiskWaringStatisticsDTO = None,
        sing_card_period_left_flow_warn_dto: GetCardStatusStatisticsResponseBodyDataSingCardPeriodLeftFlowWarnDTO = None,
        un_certified_stop_statistics_dto: GetCardStatusStatisticsResponseBodyDataUnCertifiedStopStatisticsDTO = None,
        unbind_resume_statistics_dto: GetCardStatusStatisticsResponseBodyDataUnbindResumeStatisticsDTO = None,
        week_warn_statistics_dto: GetCardStatusStatisticsResponseBodyDataWeekWarnStatisticsDTO = None,
    ):
        self.error_stop_statistics_dto = error_stop_statistics_dto
        self.exhaust_stop_statistics_dto = exhaust_stop_statistics_dto
        self.expire_stop_statistics_dto = expire_stop_statistics_dto
        self.flow_out_statistics_dto = flow_out_statistics_dto
        self.manage_stop_statistics_dto = manage_stop_statistics_dto
        self.risk_waring_statistics_dto = risk_waring_statistics_dto
        self.sing_card_period_left_flow_warn_dto = sing_card_period_left_flow_warn_dto
        self.un_certified_stop_statistics_dto = un_certified_stop_statistics_dto
        self.unbind_resume_statistics_dto = unbind_resume_statistics_dto
        self.week_warn_statistics_dto = week_warn_statistics_dto

    def validate(self):
        if self.error_stop_statistics_dto:
            self.error_stop_statistics_dto.validate()
        if self.exhaust_stop_statistics_dto:
            self.exhaust_stop_statistics_dto.validate()
        if self.expire_stop_statistics_dto:
            self.expire_stop_statistics_dto.validate()
        if self.flow_out_statistics_dto:
            self.flow_out_statistics_dto.validate()
        if self.manage_stop_statistics_dto:
            self.manage_stop_statistics_dto.validate()
        if self.risk_waring_statistics_dto:
            self.risk_waring_statistics_dto.validate()
        if self.sing_card_period_left_flow_warn_dto:
            self.sing_card_period_left_flow_warn_dto.validate()
        if self.un_certified_stop_statistics_dto:
            self.un_certified_stop_statistics_dto.validate()
        if self.unbind_resume_statistics_dto:
            self.unbind_resume_statistics_dto.validate()
        if self.week_warn_statistics_dto:
            self.week_warn_statistics_dto.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_stop_statistics_dto is not None:
            result['ErrorStopStatisticsDTO'] = self.error_stop_statistics_dto.to_map()
        if self.exhaust_stop_statistics_dto is not None:
            result['ExhaustStopStatisticsDTO'] = self.exhaust_stop_statistics_dto.to_map()
        if self.expire_stop_statistics_dto is not None:
            result['ExpireStopStatisticsDTO'] = self.expire_stop_statistics_dto.to_map()
        if self.flow_out_statistics_dto is not None:
            result['FlowOutStatisticsDTO'] = self.flow_out_statistics_dto.to_map()
        if self.manage_stop_statistics_dto is not None:
            result['ManageStopStatisticsDTO'] = self.manage_stop_statistics_dto.to_map()
        if self.risk_waring_statistics_dto is not None:
            result['RiskWaringStatisticsDTO'] = self.risk_waring_statistics_dto.to_map()
        if self.sing_card_period_left_flow_warn_dto is not None:
            result['SingCardPeriodLeftFlowWarnDTO'] = self.sing_card_period_left_flow_warn_dto.to_map()
        if self.un_certified_stop_statistics_dto is not None:
            result['UnCertifiedStopStatisticsDTO'] = self.un_certified_stop_statistics_dto.to_map()
        if self.unbind_resume_statistics_dto is not None:
            result['UnbindResumeStatisticsDTO'] = self.unbind_resume_statistics_dto.to_map()
        if self.week_warn_statistics_dto is not None:
            result['WeekWarnStatisticsDTO'] = self.week_warn_statistics_dto.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorStopStatisticsDTO') is not None:
            temp_model = GetCardStatusStatisticsResponseBodyDataErrorStopStatisticsDTO()
            self.error_stop_statistics_dto = temp_model.from_map(m['ErrorStopStatisticsDTO'])
        if m.get('ExhaustStopStatisticsDTO') is not None:
            temp_model = GetCardStatusStatisticsResponseBodyDataExhaustStopStatisticsDTO()
            self.exhaust_stop_statistics_dto = temp_model.from_map(m['ExhaustStopStatisticsDTO'])
        if m.get('ExpireStopStatisticsDTO') is not None:
            temp_model = GetCardStatusStatisticsResponseBodyDataExpireStopStatisticsDTO()
            self.expire_stop_statistics_dto = temp_model.from_map(m['ExpireStopStatisticsDTO'])
        if m.get('FlowOutStatisticsDTO') is not None:
            temp_model = GetCardStatusStatisticsResponseBodyDataFlowOutStatisticsDTO()
            self.flow_out_statistics_dto = temp_model.from_map(m['FlowOutStatisticsDTO'])
        if m.get('ManageStopStatisticsDTO') is not None:
            temp_model = GetCardStatusStatisticsResponseBodyDataManageStopStatisticsDTO()
            self.manage_stop_statistics_dto = temp_model.from_map(m['ManageStopStatisticsDTO'])
        if m.get('RiskWaringStatisticsDTO') is not None:
            temp_model = GetCardStatusStatisticsResponseBodyDataRiskWaringStatisticsDTO()
            self.risk_waring_statistics_dto = temp_model.from_map(m['RiskWaringStatisticsDTO'])
        if m.get('SingCardPeriodLeftFlowWarnDTO') is not None:
            temp_model = GetCardStatusStatisticsResponseBodyDataSingCardPeriodLeftFlowWarnDTO()
            self.sing_card_period_left_flow_warn_dto = temp_model.from_map(m['SingCardPeriodLeftFlowWarnDTO'])
        if m.get('UnCertifiedStopStatisticsDTO') is not None:
            temp_model = GetCardStatusStatisticsResponseBodyDataUnCertifiedStopStatisticsDTO()
            self.un_certified_stop_statistics_dto = temp_model.from_map(m['UnCertifiedStopStatisticsDTO'])
        if m.get('UnbindResumeStatisticsDTO') is not None:
            temp_model = GetCardStatusStatisticsResponseBodyDataUnbindResumeStatisticsDTO()
            self.unbind_resume_statistics_dto = temp_model.from_map(m['UnbindResumeStatisticsDTO'])
        if m.get('WeekWarnStatisticsDTO') is not None:
            temp_model = GetCardStatusStatisticsResponseBodyDataWeekWarnStatisticsDTO()
            self.week_warn_statistics_dto = temp_model.from_map(m['WeekWarnStatisticsDTO'])
        return self


class GetCardStatusStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetCardStatusStatisticsResponseBodyData = None,
        error_message: str = None,
        localized_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
        self.localized_message = localized_message
        self.request_id = request_id
        self.success = success

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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.localized_message is not None:
            result['LocalizedMessage'] = self.localized_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetCardStatusStatisticsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('LocalizedMessage') is not None:
            self.localized_message = m.get('LocalizedMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetCardStatusStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCardStatusStatisticsResponseBody = None,
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
            temp_model = GetCardStatusStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCredentialPoolStatisticsRequest(TeaModel):
    def __init__(
        self,
        credential_no: str = None,
        date: str = None,
    ):
        self.credential_no = credential_no
        self.date = date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_no is not None:
            result['CredentialNO'] = self.credential_no
        if self.date is not None:
            result['Date'] = self.date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialNO') is not None:
            self.credential_no = m.get('CredentialNO')
        if m.get('Date') is not None:
            self.date = m.get('Date')
        return self


class GetCredentialPoolStatisticsResponseBodyData(TeaModel):
    def __init__(
        self,
        card_active_num: int = None,
        card_total_num: int = None,
        credential_instance_id: str = None,
        credential_no: str = None,
        credential_type: str = None,
        effective_available_flow: str = None,
        effective_total_flow: str = None,
        month_exceed_fee: int = None,
        month_feature_fee: int = None,
        month_used_amount: int = None,
        pool_avaiable: str = None,
        pool_grand_total: str = None,
        pool_grand_total_used: str = None,
        pool_out_used: str = None,
        pool_used: str = None,
        sms_used: int = None,
    ):
        self.card_active_num = card_active_num
        self.card_total_num = card_total_num
        self.credential_instance_id = credential_instance_id
        self.credential_no = credential_no
        self.credential_type = credential_type
        self.effective_available_flow = effective_available_flow
        self.effective_total_flow = effective_total_flow
        self.month_exceed_fee = month_exceed_fee
        self.month_feature_fee = month_feature_fee
        self.month_used_amount = month_used_amount
        self.pool_avaiable = pool_avaiable
        self.pool_grand_total = pool_grand_total
        self.pool_grand_total_used = pool_grand_total_used
        self.pool_out_used = pool_out_used
        self.pool_used = pool_used
        self.sms_used = sms_used

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.card_active_num is not None:
            result['CardActiveNum'] = self.card_active_num
        if self.card_total_num is not None:
            result['CardTotalNum'] = self.card_total_num
        if self.credential_instance_id is not None:
            result['CredentialInstanceId'] = self.credential_instance_id
        if self.credential_no is not None:
            result['CredentialNO'] = self.credential_no
        if self.credential_type is not None:
            result['CredentialType'] = self.credential_type
        if self.effective_available_flow is not None:
            result['EffectiveAvailableFlow'] = self.effective_available_flow
        if self.effective_total_flow is not None:
            result['EffectiveTotalFlow'] = self.effective_total_flow
        if self.month_exceed_fee is not None:
            result['MonthExceedFee'] = self.month_exceed_fee
        if self.month_feature_fee is not None:
            result['MonthFeatureFee'] = self.month_feature_fee
        if self.month_used_amount is not None:
            result['MonthUsedAmount'] = self.month_used_amount
        if self.pool_avaiable is not None:
            result['PoolAvaiable'] = self.pool_avaiable
        if self.pool_grand_total is not None:
            result['PoolGrandTotal'] = self.pool_grand_total
        if self.pool_grand_total_used is not None:
            result['PoolGrandTotalUsed'] = self.pool_grand_total_used
        if self.pool_out_used is not None:
            result['PoolOutUsed'] = self.pool_out_used
        if self.pool_used is not None:
            result['PoolUsed'] = self.pool_used
        if self.sms_used is not None:
            result['SmsUsed'] = self.sms_used
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CardActiveNum') is not None:
            self.card_active_num = m.get('CardActiveNum')
        if m.get('CardTotalNum') is not None:
            self.card_total_num = m.get('CardTotalNum')
        if m.get('CredentialInstanceId') is not None:
            self.credential_instance_id = m.get('CredentialInstanceId')
        if m.get('CredentialNO') is not None:
            self.credential_no = m.get('CredentialNO')
        if m.get('CredentialType') is not None:
            self.credential_type = m.get('CredentialType')
        if m.get('EffectiveAvailableFlow') is not None:
            self.effective_available_flow = m.get('EffectiveAvailableFlow')
        if m.get('EffectiveTotalFlow') is not None:
            self.effective_total_flow = m.get('EffectiveTotalFlow')
        if m.get('MonthExceedFee') is not None:
            self.month_exceed_fee = m.get('MonthExceedFee')
        if m.get('MonthFeatureFee') is not None:
            self.month_feature_fee = m.get('MonthFeatureFee')
        if m.get('MonthUsedAmount') is not None:
            self.month_used_amount = m.get('MonthUsedAmount')
        if m.get('PoolAvaiable') is not None:
            self.pool_avaiable = m.get('PoolAvaiable')
        if m.get('PoolGrandTotal') is not None:
            self.pool_grand_total = m.get('PoolGrandTotal')
        if m.get('PoolGrandTotalUsed') is not None:
            self.pool_grand_total_used = m.get('PoolGrandTotalUsed')
        if m.get('PoolOutUsed') is not None:
            self.pool_out_used = m.get('PoolOutUsed')
        if m.get('PoolUsed') is not None:
            self.pool_used = m.get('PoolUsed')
        if m.get('SmsUsed') is not None:
            self.sms_used = m.get('SmsUsed')
        return self


class GetCredentialPoolStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetCredentialPoolStatisticsResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetCredentialPoolStatisticsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetCredentialPoolStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCredentialPoolStatisticsResponseBody = None,
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
            temp_model = GetCredentialPoolStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOperateResultRequest(TeaModel):
    def __init__(
        self,
        api_product: str = None,
        res_id: str = None,
        serial_no: str = None,
    ):
        self.api_product = api_product
        self.res_id = res_id
        self.serial_no = serial_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_product is not None:
            result['ApiProduct'] = self.api_product
        if self.res_id is not None:
            result['ResId'] = self.res_id
        if self.serial_no is not None:
            result['SerialNo'] = self.serial_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiProduct') is not None:
            self.api_product = m.get('ApiProduct')
        if m.get('ResId') is not None:
            self.res_id = m.get('ResId')
        if m.get('SerialNo') is not None:
            self.serial_no = m.get('SerialNo')
        return self


class GetOperateResultResponseBodyData(TeaModel):
    def __init__(
        self,
        execute_result: str = None,
        operate_type: str = None,
        result: bool = None,
        status: str = None,
    ):
        self.execute_result = execute_result
        self.operate_type = operate_type
        self.result = result
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.execute_result is not None:
            result['ExecuteResult'] = self.execute_result
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        if self.result is not None:
            result['Result'] = self.result
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecuteResult') is not None:
            self.execute_result = m.get('ExecuteResult')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetOperateResultResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetOperateResultResponseBodyData = None,
        error_message: str = None,
        localized_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
        self.localized_message = localized_message
        self.request_id = request_id
        self.success = success

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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.localized_message is not None:
            result['LocalizedMessage'] = self.localized_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetOperateResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('LocalizedMessage') is not None:
            self.localized_message = m.get('LocalizedMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetOperateResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOperateResultResponseBody = None,
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
            temp_model = GetOperateResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRealNameStatusRequest(TeaModel):
    def __init__(
        self,
        iccid: str = None,
        list_msisdns: List[str] = None,
    ):
        self.iccid = iccid
        self.list_msisdns = list_msisdns

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        if self.list_msisdns is not None:
            result['ListMsisdns'] = self.list_msisdns
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        if m.get('ListMsisdns') is not None:
            self.list_msisdns = m.get('ListMsisdns')
        return self


class GetRealNameStatusShrinkRequest(TeaModel):
    def __init__(
        self,
        iccid: str = None,
        list_msisdns_shrink: str = None,
    ):
        self.iccid = iccid
        self.list_msisdns_shrink = list_msisdns_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        if self.list_msisdns_shrink is not None:
            result['ListMsisdns'] = self.list_msisdns_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        if m.get('ListMsisdns') is not None:
            self.list_msisdns_shrink = m.get('ListMsisdns')
        return self


class GetRealNameStatusResponseBodyData(TeaModel):
    def __init__(
        self,
        desc: str = None,
        real_name_status: str = None,
    ):
        self.desc = desc
        self.real_name_status = real_name_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.real_name_status is not None:
            result['RealNameStatus'] = self.real_name_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('RealNameStatus') is not None:
            self.real_name_status = m.get('RealNameStatus')
        return self


class GetRealNameStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetRealNameStatusResponseBodyData = None,
        error_message: str = None,
        localized_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
        self.localized_message = localized_message
        self.request_id = request_id
        self.success = success

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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.localized_message is not None:
            result['LocalizedMessage'] = self.localized_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetRealNameStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('LocalizedMessage') is not None:
            self.localized_message = m.get('LocalizedMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetRealNameStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRealNameStatusResponseBody = None,
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
            temp_model = GetRealNameStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSimCardStateDistributionRequest(TeaModel):
    def __init__(
        self,
        credential_no: str = None,
        date: str = None,
    ):
        self.credential_no = credential_no
        self.date = date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_no is not None:
            result['CredentialNO'] = self.credential_no
        if self.date is not None:
            result['Date'] = self.date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialNO') is not None:
            self.credential_no = m.get('CredentialNO')
        if m.get('Date') is not None:
            self.date = m.get('Date')
        return self


class GetSimCardStateDistributionResponseBodyData(TeaModel):
    def __init__(
        self,
        card_count: int = None,
        destoryed_count: int = None,
        shut_down_count: int = None,
        stop_count: int = None,
        test_count: int = None,
        unused_count: int = None,
        using_count: int = None,
    ):
        self.card_count = card_count
        self.destoryed_count = destoryed_count
        self.shut_down_count = shut_down_count
        self.stop_count = stop_count
        self.test_count = test_count
        self.unused_count = unused_count
        self.using_count = using_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.card_count is not None:
            result['CardCount'] = self.card_count
        if self.destoryed_count is not None:
            result['DestoryedCount'] = self.destoryed_count
        if self.shut_down_count is not None:
            result['ShutDownCount'] = self.shut_down_count
        if self.stop_count is not None:
            result['StopCount'] = self.stop_count
        if self.test_count is not None:
            result['TestCount'] = self.test_count
        if self.unused_count is not None:
            result['UnusedCount'] = self.unused_count
        if self.using_count is not None:
            result['UsingCount'] = self.using_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CardCount') is not None:
            self.card_count = m.get('CardCount')
        if m.get('DestoryedCount') is not None:
            self.destoryed_count = m.get('DestoryedCount')
        if m.get('ShutDownCount') is not None:
            self.shut_down_count = m.get('ShutDownCount')
        if m.get('StopCount') is not None:
            self.stop_count = m.get('StopCount')
        if m.get('TestCount') is not None:
            self.test_count = m.get('TestCount')
        if m.get('UnusedCount') is not None:
            self.unused_count = m.get('UnusedCount')
        if m.get('UsingCount') is not None:
            self.using_count = m.get('UsingCount')
        return self


class GetSimCardStateDistributionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetSimCardStateDistributionResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetSimCardStateDistributionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetSimCardStateDistributionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSimCardStateDistributionResponseBody = None,
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
            temp_model = GetSimCardStateDistributionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCardInfoRequest(TeaModel):
    def __init__(
        self,
        active_time_end: str = None,
        active_time_start: str = None,
        ali_fee: str = None,
        aliyun_order_id: str = None,
        apn_name: str = None,
        certify_type: str = None,
        credential_no: str = None,
        data_level: str = None,
        data_type: str = None,
        directional_group_id: str = None,
        expire_time_end: str = None,
        expire_time_start: str = None,
        iccid: str = None,
        imsi: str = None,
        is_auto_recharge: bool = None,
        max_flow: str = None,
        max_rest_flow_percentage: float = None,
        min_flow: str = None,
        msisdn: str = None,
        network_type: str = None,
        notify_id: str = None,
        os_status: str = None,
        page_no: int = None,
        page_size: int = None,
        period: str = None,
        pool_id: str = None,
        sim_type: str = None,
        status: str = None,
        tag_name: str = None,
        vendor: str = None,
    ):
        self.active_time_end = active_time_end
        self.active_time_start = active_time_start
        self.ali_fee = ali_fee
        self.aliyun_order_id = aliyun_order_id
        self.apn_name = apn_name
        self.certify_type = certify_type
        self.credential_no = credential_no
        self.data_level = data_level
        self.data_type = data_type
        self.directional_group_id = directional_group_id
        self.expire_time_end = expire_time_end
        self.expire_time_start = expire_time_start
        self.iccid = iccid
        self.imsi = imsi
        self.is_auto_recharge = is_auto_recharge
        self.max_flow = max_flow
        self.max_rest_flow_percentage = max_rest_flow_percentage
        self.min_flow = min_flow
        self.msisdn = msisdn
        self.network_type = network_type
        self.notify_id = notify_id
        self.os_status = os_status
        self.page_no = page_no
        self.page_size = page_size
        self.period = period
        self.pool_id = pool_id
        self.sim_type = sim_type
        self.status = status
        self.tag_name = tag_name
        self.vendor = vendor

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_time_end is not None:
            result['ActiveTimeEnd'] = self.active_time_end
        if self.active_time_start is not None:
            result['ActiveTimeStart'] = self.active_time_start
        if self.ali_fee is not None:
            result['AliFee'] = self.ali_fee
        if self.aliyun_order_id is not None:
            result['AliyunOrderId'] = self.aliyun_order_id
        if self.apn_name is not None:
            result['ApnName'] = self.apn_name
        if self.certify_type is not None:
            result['CertifyType'] = self.certify_type
        if self.credential_no is not None:
            result['CredentialNo'] = self.credential_no
        if self.data_level is not None:
            result['DataLevel'] = self.data_level
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.directional_group_id is not None:
            result['DirectionalGroupId'] = self.directional_group_id
        if self.expire_time_end is not None:
            result['ExpireTimeEnd'] = self.expire_time_end
        if self.expire_time_start is not None:
            result['ExpireTimeStart'] = self.expire_time_start
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        if self.imsi is not None:
            result['Imsi'] = self.imsi
        if self.is_auto_recharge is not None:
            result['IsAutoRecharge'] = self.is_auto_recharge
        if self.max_flow is not None:
            result['MaxFlow'] = self.max_flow
        if self.max_rest_flow_percentage is not None:
            result['MaxRestFlowPercentage'] = self.max_rest_flow_percentage
        if self.min_flow is not None:
            result['MinFlow'] = self.min_flow
        if self.msisdn is not None:
            result['Msisdn'] = self.msisdn
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.notify_id is not None:
            result['NotifyId'] = self.notify_id
        if self.os_status is not None:
            result['OsStatus'] = self.os_status
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.period is not None:
            result['Period'] = self.period
        if self.pool_id is not None:
            result['PoolId'] = self.pool_id
        if self.sim_type is not None:
            result['SimType'] = self.sim_type
        if self.status is not None:
            result['Status'] = self.status
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveTimeEnd') is not None:
            self.active_time_end = m.get('ActiveTimeEnd')
        if m.get('ActiveTimeStart') is not None:
            self.active_time_start = m.get('ActiveTimeStart')
        if m.get('AliFee') is not None:
            self.ali_fee = m.get('AliFee')
        if m.get('AliyunOrderId') is not None:
            self.aliyun_order_id = m.get('AliyunOrderId')
        if m.get('ApnName') is not None:
            self.apn_name = m.get('ApnName')
        if m.get('CertifyType') is not None:
            self.certify_type = m.get('CertifyType')
        if m.get('CredentialNo') is not None:
            self.credential_no = m.get('CredentialNo')
        if m.get('DataLevel') is not None:
            self.data_level = m.get('DataLevel')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DirectionalGroupId') is not None:
            self.directional_group_id = m.get('DirectionalGroupId')
        if m.get('ExpireTimeEnd') is not None:
            self.expire_time_end = m.get('ExpireTimeEnd')
        if m.get('ExpireTimeStart') is not None:
            self.expire_time_start = m.get('ExpireTimeStart')
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        if m.get('Imsi') is not None:
            self.imsi = m.get('Imsi')
        if m.get('IsAutoRecharge') is not None:
            self.is_auto_recharge = m.get('IsAutoRecharge')
        if m.get('MaxFlow') is not None:
            self.max_flow = m.get('MaxFlow')
        if m.get('MaxRestFlowPercentage') is not None:
            self.max_rest_flow_percentage = m.get('MaxRestFlowPercentage')
        if m.get('MinFlow') is not None:
            self.min_flow = m.get('MinFlow')
        if m.get('Msisdn') is not None:
            self.msisdn = m.get('Msisdn')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('NotifyId') is not None:
            self.notify_id = m.get('NotifyId')
        if m.get('OsStatus') is not None:
            self.os_status = m.get('OsStatus')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PoolId') is not None:
            self.pool_id = m.get('PoolId')
        if m.get('SimType') is not None:
            self.sim_type = m.get('SimType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        return self


class ListCardInfoResponseBodyDataListTagList(TeaModel):
    def __init__(
        self,
        id: int = None,
        tag_name: str = None,
    ):
        self.id = id
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class ListCardInfoResponseBodyDataList(TeaModel):
    def __init__(
        self,
        active_time: str = None,
        active_type: str = None,
        ali_fee: str = None,
        aliyun_order_id: str = None,
        apn_name: str = None,
        certify_type: str = None,
        credential_instance_id: str = None,
        credential_no: str = None,
        credential_type: str = None,
        data_level: str = None,
        data_type: str = None,
        directional_group_id: int = None,
        directional_group_name: str = None,
        expire_time: str = None,
        flow_latest_modified_time: str = None,
        iccid: str = None,
        imsi: List[str] = None,
        is_auto_recharge: bool = None,
        msisdn: List[str] = None,
        network_type: str = None,
        notify_id: str = None,
        open_account_time: str = None,
        os_status: str = None,
        period: str = None,
        period_add_flow: str = None,
        period_rest_flow: str = None,
        period_sms_use: str = None,
        private_network_segment: str = None,
        remark: str = None,
        sim_type: str = None,
        status: str = None,
        tag_list: List[ListCardInfoResponseBodyDataListTagList] = None,
        vendor: str = None,
        vsim_instance_id: int = None,
    ):
        self.active_time = active_time
        self.active_type = active_type
        self.ali_fee = ali_fee
        self.aliyun_order_id = aliyun_order_id
        self.apn_name = apn_name
        self.certify_type = certify_type
        self.credential_instance_id = credential_instance_id
        self.credential_no = credential_no
        self.credential_type = credential_type
        self.data_level = data_level
        self.data_type = data_type
        self.directional_group_id = directional_group_id
        self.directional_group_name = directional_group_name
        self.expire_time = expire_time
        self.flow_latest_modified_time = flow_latest_modified_time
        self.iccid = iccid
        self.imsi = imsi
        self.is_auto_recharge = is_auto_recharge
        self.msisdn = msisdn
        self.network_type = network_type
        self.notify_id = notify_id
        self.open_account_time = open_account_time
        self.os_status = os_status
        self.period = period
        self.period_add_flow = period_add_flow
        self.period_rest_flow = period_rest_flow
        self.period_sms_use = period_sms_use
        self.private_network_segment = private_network_segment
        self.remark = remark
        self.sim_type = sim_type
        self.status = status
        self.tag_list = tag_list
        self.vendor = vendor
        self.vsim_instance_id = vsim_instance_id

    def validate(self):
        if self.tag_list:
            for k in self.tag_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_time is not None:
            result['ActiveTime'] = self.active_time
        if self.active_type is not None:
            result['ActiveType'] = self.active_type
        if self.ali_fee is not None:
            result['AliFee'] = self.ali_fee
        if self.aliyun_order_id is not None:
            result['AliyunOrderId'] = self.aliyun_order_id
        if self.apn_name is not None:
            result['ApnName'] = self.apn_name
        if self.certify_type is not None:
            result['CertifyType'] = self.certify_type
        if self.credential_instance_id is not None:
            result['CredentialInstanceId'] = self.credential_instance_id
        if self.credential_no is not None:
            result['CredentialNo'] = self.credential_no
        if self.credential_type is not None:
            result['CredentialType'] = self.credential_type
        if self.data_level is not None:
            result['DataLevel'] = self.data_level
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.directional_group_id is not None:
            result['DirectionalGroupId'] = self.directional_group_id
        if self.directional_group_name is not None:
            result['DirectionalGroupName'] = self.directional_group_name
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.flow_latest_modified_time is not None:
            result['FlowLatestModifiedTime'] = self.flow_latest_modified_time
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        if self.imsi is not None:
            result['Imsi'] = self.imsi
        if self.is_auto_recharge is not None:
            result['IsAutoRecharge'] = self.is_auto_recharge
        if self.msisdn is not None:
            result['Msisdn'] = self.msisdn
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.notify_id is not None:
            result['NotifyId'] = self.notify_id
        if self.open_account_time is not None:
            result['OpenAccountTime'] = self.open_account_time
        if self.os_status is not None:
            result['OsStatus'] = self.os_status
        if self.period is not None:
            result['Period'] = self.period
        if self.period_add_flow is not None:
            result['PeriodAddFlow'] = self.period_add_flow
        if self.period_rest_flow is not None:
            result['PeriodRestFlow'] = self.period_rest_flow
        if self.period_sms_use is not None:
            result['PeriodSmsUse'] = self.period_sms_use
        if self.private_network_segment is not None:
            result['PrivateNetworkSegment'] = self.private_network_segment
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.sim_type is not None:
            result['SimType'] = self.sim_type
        if self.status is not None:
            result['Status'] = self.status
        result['TagList'] = []
        if self.tag_list is not None:
            for k in self.tag_list:
                result['TagList'].append(k.to_map() if k else None)
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        if self.vsim_instance_id is not None:
            result['VsimInstanceId'] = self.vsim_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveTime') is not None:
            self.active_time = m.get('ActiveTime')
        if m.get('ActiveType') is not None:
            self.active_type = m.get('ActiveType')
        if m.get('AliFee') is not None:
            self.ali_fee = m.get('AliFee')
        if m.get('AliyunOrderId') is not None:
            self.aliyun_order_id = m.get('AliyunOrderId')
        if m.get('ApnName') is not None:
            self.apn_name = m.get('ApnName')
        if m.get('CertifyType') is not None:
            self.certify_type = m.get('CertifyType')
        if m.get('CredentialInstanceId') is not None:
            self.credential_instance_id = m.get('CredentialInstanceId')
        if m.get('CredentialNo') is not None:
            self.credential_no = m.get('CredentialNo')
        if m.get('CredentialType') is not None:
            self.credential_type = m.get('CredentialType')
        if m.get('DataLevel') is not None:
            self.data_level = m.get('DataLevel')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DirectionalGroupId') is not None:
            self.directional_group_id = m.get('DirectionalGroupId')
        if m.get('DirectionalGroupName') is not None:
            self.directional_group_name = m.get('DirectionalGroupName')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('FlowLatestModifiedTime') is not None:
            self.flow_latest_modified_time = m.get('FlowLatestModifiedTime')
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        if m.get('Imsi') is not None:
            self.imsi = m.get('Imsi')
        if m.get('IsAutoRecharge') is not None:
            self.is_auto_recharge = m.get('IsAutoRecharge')
        if m.get('Msisdn') is not None:
            self.msisdn = m.get('Msisdn')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('NotifyId') is not None:
            self.notify_id = m.get('NotifyId')
        if m.get('OpenAccountTime') is not None:
            self.open_account_time = m.get('OpenAccountTime')
        if m.get('OsStatus') is not None:
            self.os_status = m.get('OsStatus')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodAddFlow') is not None:
            self.period_add_flow = m.get('PeriodAddFlow')
        if m.get('PeriodRestFlow') is not None:
            self.period_rest_flow = m.get('PeriodRestFlow')
        if m.get('PeriodSmsUse') is not None:
            self.period_sms_use = m.get('PeriodSmsUse')
        if m.get('PrivateNetworkSegment') is not None:
            self.private_network_segment = m.get('PrivateNetworkSegment')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('SimType') is not None:
            self.sim_type = m.get('SimType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tag_list = []
        if m.get('TagList') is not None:
            for k in m.get('TagList'):
                temp_model = ListCardInfoResponseBodyDataListTagList()
                self.tag_list.append(temp_model.from_map(k))
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        if m.get('VsimInstanceId') is not None:
            self.vsim_instance_id = m.get('VsimInstanceId')
        return self


class ListCardInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[ListCardInfoResponseBodyDataList] = None,
        page_count: int = None,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.list = list
        self.page_count = page_count
        self.page_no = page_no
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListCardInfoResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListCardInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListCardInfoResponseBodyData = None,
        error_message: str = None,
        localized_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
        self.localized_message = localized_message
        self.request_id = request_id
        self.success = success

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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.localized_message is not None:
            result['LocalizedMessage'] = self.localized_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListCardInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('LocalizedMessage') is not None:
            self.localized_message = m.get('LocalizedMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListCardInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCardInfoResponseBody = None,
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
            temp_model = ListCardInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDirectionalAddressRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        page_no: int = None,
        page_size: int = None,
    ):
        self.group_id = group_id
        self.page_no = page_no
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListDirectionalAddressResponseBodyDataList(TeaModel):
    def __init__(
        self,
        address: str = None,
        address_type: str = None,
        group_id: str = None,
        source: str = None,
        state: int = None,
    ):
        self.address = address
        self.address_type = address_type
        self.group_id = group_id
        self.source = source
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.address_type is not None:
            result['AddressType'] = self.address_type
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.source is not None:
            result['Source'] = self.source
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class ListDirectionalAddressResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[ListDirectionalAddressResponseBodyDataList] = None,
        page_count: int = None,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.list = list
        self.page_count = page_count
        self.page_no = page_no
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListDirectionalAddressResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListDirectionalAddressResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListDirectionalAddressResponseBodyData = None,
        error_message: str = None,
        localized_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
        self.localized_message = localized_message
        self.request_id = request_id
        self.success = success

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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.localized_message is not None:
            result['LocalizedMessage'] = self.localized_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListDirectionalAddressResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('LocalizedMessage') is not None:
            self.localized_message = m.get('LocalizedMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListDirectionalAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDirectionalAddressResponseBody = None,
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
            temp_model = ListDirectionalAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDirectionalDetailRequest(TeaModel):
    def __init__(
        self,
        iccid: str = None,
        page_no: int = None,
        page_size: int = None,
    ):
        self.iccid = iccid
        self.page_no = page_no
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListDirectionalDetailResponseBodyDataPaginationResultList(TeaModel):
    def __init__(
        self,
        address: str = None,
        address_type: str = None,
        group_id: str = None,
        source: str = None,
        state: str = None,
    ):
        self.address = address
        self.address_type = address_type
        self.group_id = group_id
        self.source = source
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.address_type is not None:
            result['AddressType'] = self.address_type
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.source is not None:
            result['Source'] = self.source
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class ListDirectionalDetailResponseBodyDataPaginationResult(TeaModel):
    def __init__(
        self,
        list: List[ListDirectionalDetailResponseBodyDataPaginationResultList] = None,
        page_count: int = None,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.list = list
        self.page_count = page_count
        self.page_no = page_no
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListDirectionalDetailResponseBodyDataPaginationResultList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListDirectionalDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        directional_group_id: int = None,
        directional_name: str = None,
        pagination_result: ListDirectionalDetailResponseBodyDataPaginationResult = None,
    ):
        self.directional_group_id = directional_group_id
        self.directional_name = directional_name
        self.pagination_result = pagination_result

    def validate(self):
        if self.pagination_result:
            self.pagination_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directional_group_id is not None:
            result['DirectionalGroupId'] = self.directional_group_id
        if self.directional_name is not None:
            result['DirectionalName'] = self.directional_name
        if self.pagination_result is not None:
            result['PaginationResult'] = self.pagination_result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectionalGroupId') is not None:
            self.directional_group_id = m.get('DirectionalGroupId')
        if m.get('DirectionalName') is not None:
            self.directional_name = m.get('DirectionalName')
        if m.get('PaginationResult') is not None:
            temp_model = ListDirectionalDetailResponseBodyDataPaginationResult()
            self.pagination_result = temp_model.from_map(m['PaginationResult'])
        return self


class ListDirectionalDetailResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListDirectionalDetailResponseBodyData = None,
        error_message: str = None,
        localized_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
        self.localized_message = localized_message
        self.request_id = request_id
        self.success = success

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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.localized_message is not None:
            result['LocalizedMessage'] = self.localized_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListDirectionalDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('LocalizedMessage') is not None:
            self.localized_message = m.get('LocalizedMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListDirectionalDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDirectionalDetailResponseBody = None,
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
            temp_model = ListDirectionalDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOrderRequest(TeaModel):
    def __init__(
        self,
        credential_no: str = None,
        end_date: str = None,
        order_id: str = None,
        order_status: str = None,
        order_type: str = None,
        page_no: int = None,
        page_size: int = None,
        start_date: str = None,
    ):
        self.credential_no = credential_no
        self.end_date = end_date
        self.order_id = order_id
        self.order_status = order_status
        self.order_type = order_type
        self.page_no = page_no
        self.page_size = page_size
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_no is not None:
            result['CredentialNo'] = self.credential_no
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.order_status is not None:
            result['OrderStatus'] = self.order_status
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialNo') is not None:
            self.credential_no = m.get('CredentialNo')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OrderStatus') is not None:
            self.order_status = m.get('OrderStatus')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class ListOrderResponseBodyDataListDeliveryInfo(TeaModel):
    def __init__(
        self,
        address: str = None,
        buyer_message: str = None,
        mail: str = None,
        receiver: str = None,
        zip_code: str = None,
    ):
        self.address = address
        self.buyer_message = buyer_message
        self.mail = mail
        self.receiver = receiver
        self.zip_code = zip_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.buyer_message is not None:
            result['BuyerMessage'] = self.buyer_message
        if self.mail is not None:
            result['Mail'] = self.mail
        if self.receiver is not None:
            result['Receiver'] = self.receiver
        if self.zip_code is not None:
            result['ZipCode'] = self.zip_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('BuyerMessage') is not None:
            self.buyer_message = m.get('BuyerMessage')
        if m.get('Mail') is not None:
            self.mail = m.get('Mail')
        if m.get('Receiver') is not None:
            self.receiver = m.get('Receiver')
        if m.get('ZipCode') is not None:
            self.zip_code = m.get('ZipCode')
        return self


class ListOrderResponseBodyDataList(TeaModel):
    def __init__(
        self,
        ali_fee: str = None,
        apn_name: str = None,
        apn_region: str = None,
        billing_cycle: str = None,
        buy_num: int = None,
        card_pay_count: int = None,
        credential_no: str = None,
        credential_package: str = None,
        data_level: str = None,
        delivery_info: ListOrderResponseBodyDataListDeliveryInfo = None,
        express_no_list: List[str] = None,
        flow_type: str = None,
        function_fee: int = None,
        network_type: str = None,
        order_detail_url: str = None,
        order_id: str = None,
        order_info: str = None,
        order_status: str = None,
        order_type: str = None,
        pay_duration: str = None,
        pay_time: str = None,
        pool_capacity: str = None,
        pool_capacity_unit: str = None,
        pool_no: str = None,
        resource_quantity: int = None,
        vendor: str = None,
    ):
        self.ali_fee = ali_fee
        self.apn_name = apn_name
        self.apn_region = apn_region
        self.billing_cycle = billing_cycle
        self.buy_num = buy_num
        self.card_pay_count = card_pay_count
        self.credential_no = credential_no
        self.credential_package = credential_package
        self.data_level = data_level
        self.delivery_info = delivery_info
        self.express_no_list = express_no_list
        self.flow_type = flow_type
        self.function_fee = function_fee
        self.network_type = network_type
        self.order_detail_url = order_detail_url
        self.order_id = order_id
        self.order_info = order_info
        self.order_status = order_status
        self.order_type = order_type
        self.pay_duration = pay_duration
        self.pay_time = pay_time
        self.pool_capacity = pool_capacity
        self.pool_capacity_unit = pool_capacity_unit
        self.pool_no = pool_no
        self.resource_quantity = resource_quantity
        self.vendor = vendor

    def validate(self):
        if self.delivery_info:
            self.delivery_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_fee is not None:
            result['AliFee'] = self.ali_fee
        if self.apn_name is not None:
            result['ApnName'] = self.apn_name
        if self.apn_region is not None:
            result['ApnRegion'] = self.apn_region
        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle
        if self.buy_num is not None:
            result['BuyNum'] = self.buy_num
        if self.card_pay_count is not None:
            result['CardPayCount'] = self.card_pay_count
        if self.credential_no is not None:
            result['CredentialNo'] = self.credential_no
        if self.credential_package is not None:
            result['CredentialPackage'] = self.credential_package
        if self.data_level is not None:
            result['DataLevel'] = self.data_level
        if self.delivery_info is not None:
            result['DeliveryInfo'] = self.delivery_info.to_map()
        if self.express_no_list is not None:
            result['ExpressNoList'] = self.express_no_list
        if self.flow_type is not None:
            result['FlowType'] = self.flow_type
        if self.function_fee is not None:
            result['FunctionFee'] = self.function_fee
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.order_detail_url is not None:
            result['OrderDetailUrl'] = self.order_detail_url
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.order_info is not None:
            result['OrderInfo'] = self.order_info
        if self.order_status is not None:
            result['OrderStatus'] = self.order_status
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.pay_duration is not None:
            result['PayDuration'] = self.pay_duration
        if self.pay_time is not None:
            result['PayTime'] = self.pay_time
        if self.pool_capacity is not None:
            result['PoolCapacity'] = self.pool_capacity
        if self.pool_capacity_unit is not None:
            result['PoolCapacityUnit'] = self.pool_capacity_unit
        if self.pool_no is not None:
            result['PoolNo'] = self.pool_no
        if self.resource_quantity is not None:
            result['ResourceQuantity'] = self.resource_quantity
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliFee') is not None:
            self.ali_fee = m.get('AliFee')
        if m.get('ApnName') is not None:
            self.apn_name = m.get('ApnName')
        if m.get('ApnRegion') is not None:
            self.apn_region = m.get('ApnRegion')
        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')
        if m.get('BuyNum') is not None:
            self.buy_num = m.get('BuyNum')
        if m.get('CardPayCount') is not None:
            self.card_pay_count = m.get('CardPayCount')
        if m.get('CredentialNo') is not None:
            self.credential_no = m.get('CredentialNo')
        if m.get('CredentialPackage') is not None:
            self.credential_package = m.get('CredentialPackage')
        if m.get('DataLevel') is not None:
            self.data_level = m.get('DataLevel')
        if m.get('DeliveryInfo') is not None:
            temp_model = ListOrderResponseBodyDataListDeliveryInfo()
            self.delivery_info = temp_model.from_map(m['DeliveryInfo'])
        if m.get('ExpressNoList') is not None:
            self.express_no_list = m.get('ExpressNoList')
        if m.get('FlowType') is not None:
            self.flow_type = m.get('FlowType')
        if m.get('FunctionFee') is not None:
            self.function_fee = m.get('FunctionFee')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('OrderDetailUrl') is not None:
            self.order_detail_url = m.get('OrderDetailUrl')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OrderInfo') is not None:
            self.order_info = m.get('OrderInfo')
        if m.get('OrderStatus') is not None:
            self.order_status = m.get('OrderStatus')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('PayDuration') is not None:
            self.pay_duration = m.get('PayDuration')
        if m.get('PayTime') is not None:
            self.pay_time = m.get('PayTime')
        if m.get('PoolCapacity') is not None:
            self.pool_capacity = m.get('PoolCapacity')
        if m.get('PoolCapacityUnit') is not None:
            self.pool_capacity_unit = m.get('PoolCapacityUnit')
        if m.get('PoolNo') is not None:
            self.pool_no = m.get('PoolNo')
        if m.get('ResourceQuantity') is not None:
            self.resource_quantity = m.get('ResourceQuantity')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        return self


class ListOrderResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[ListOrderResponseBodyDataList] = None,
        page_count: int = None,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.list = list
        self.page_count = page_count
        self.page_no = page_no
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListOrderResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListOrderResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListOrderResponseBodyData = None,
        error_message: str = None,
        localized_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
        self.localized_message = localized_message
        self.request_id = request_id
        self.success = success

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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.localized_message is not None:
            result['LocalizedMessage'] = self.localized_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListOrderResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('LocalizedMessage') is not None:
            self.localized_message = m.get('LocalizedMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListOrderResponseBody = None,
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
            temp_model = ListOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RebindResumeSingleCardRequest(TeaModel):
    def __init__(
        self,
        iccid: str = None,
        opt_msisdns: List[str] = None,
    ):
        self.iccid = iccid
        self.opt_msisdns = opt_msisdns

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        if self.opt_msisdns is not None:
            result['OptMsisdns'] = self.opt_msisdns
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        if m.get('OptMsisdns') is not None:
            self.opt_msisdns = m.get('OptMsisdns')
        return self


class RebindResumeSingleCardShrinkRequest(TeaModel):
    def __init__(
        self,
        iccid: str = None,
        opt_msisdns_shrink: str = None,
    ):
        self.iccid = iccid
        self.opt_msisdns_shrink = opt_msisdns_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        if self.opt_msisdns_shrink is not None:
            result['OptMsisdns'] = self.opt_msisdns_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        if m.get('OptMsisdns') is not None:
            self.opt_msisdns_shrink = m.get('OptMsisdns')
        return self


class RebindResumeSingleCardResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        error_message: str = None,
        localized_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
        self.localized_message = localized_message
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
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.localized_message is not None:
            result['LocalizedMessage'] = self.localized_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('LocalizedMessage') is not None:
            self.localized_message = m.get('LocalizedMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RebindResumeSingleCardResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RebindResumeSingleCardResponseBody = None,
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
            temp_model = RebindResumeSingleCardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenewRequest(TeaModel):
    def __init__(
        self,
        api_product: str = None,
        api_revision: str = None,
        buy_num: int = None,
        iccid: str = None,
        offer_code: str = None,
        recharge_type: str = None,
        serial_no: str = None,
    ):
        self.api_product = api_product
        self.api_revision = api_revision
        self.buy_num = buy_num
        self.iccid = iccid
        self.offer_code = offer_code
        self.recharge_type = recharge_type
        self.serial_no = serial_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_product is not None:
            result['ApiProduct'] = self.api_product
        if self.api_revision is not None:
            result['ApiRevision'] = self.api_revision
        if self.buy_num is not None:
            result['BuyNum'] = self.buy_num
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        if self.offer_code is not None:
            result['OfferCode'] = self.offer_code
        if self.recharge_type is not None:
            result['RechargeType'] = self.recharge_type
        if self.serial_no is not None:
            result['SerialNo'] = self.serial_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiProduct') is not None:
            self.api_product = m.get('ApiProduct')
        if m.get('ApiRevision') is not None:
            self.api_revision = m.get('ApiRevision')
        if m.get('BuyNum') is not None:
            self.buy_num = m.get('BuyNum')
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        if m.get('OfferCode') is not None:
            self.offer_code = m.get('OfferCode')
        if m.get('RechargeType') is not None:
            self.recharge_type = m.get('RechargeType')
        if m.get('SerialNo') is not None:
            self.serial_no = m.get('SerialNo')
        return self


class RenewResponseBodyData(TeaModel):
    def __init__(
        self,
        order_no: str = None,
        serial_no: str = None,
    ):
        self.order_no = order_no
        self.serial_no = serial_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_no is not None:
            result['OrderNo'] = self.order_no
        if self.serial_no is not None:
            result['SerialNo'] = self.serial_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderNo') is not None:
            self.order_no = m.get('OrderNo')
        if m.get('SerialNo') is not None:
            self.serial_no = m.get('SerialNo')
        return self


class RenewResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: RenewResponseBodyData = None,
        error_message: str = None,
        localized_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
        self.localized_message = localized_message
        self.request_id = request_id
        self.success = success

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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.localized_message is not None:
            result['LocalizedMessage'] = self.localized_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = RenewResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('LocalizedMessage') is not None:
            self.localized_message = m.get('LocalizedMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RenewResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RenewResponseBody = None,
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
            temp_model = RenewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResumeSingleCardRequest(TeaModel):
    def __init__(
        self,
        iccid: str = None,
        opt_msisdns: List[str] = None,
    ):
        self.iccid = iccid
        self.opt_msisdns = opt_msisdns

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        if self.opt_msisdns is not None:
            result['OptMsisdns'] = self.opt_msisdns
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        if m.get('OptMsisdns') is not None:
            self.opt_msisdns = m.get('OptMsisdns')
        return self


class ResumeSingleCardShrinkRequest(TeaModel):
    def __init__(
        self,
        iccid: str = None,
        opt_msisdns_shrink: str = None,
    ):
        self.iccid = iccid
        self.opt_msisdns_shrink = opt_msisdns_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        if self.opt_msisdns_shrink is not None:
            result['OptMsisdns'] = self.opt_msisdns_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        if m.get('OptMsisdns') is not None:
            self.opt_msisdns_shrink = m.get('OptMsisdns')
        return self


class ResumeSingleCardResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        error_message: str = None,
        localized_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
        self.localized_message = localized_message
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
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.localized_message is not None:
            result['LocalizedMessage'] = self.localized_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('LocalizedMessage') is not None:
            self.localized_message = m.get('LocalizedMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ResumeSingleCardResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResumeSingleCardResponseBody = None,
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
            temp_model = ResumeSingleCardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendMessageRequest(TeaModel):
    def __init__(
        self,
        api_product: str = None,
        message_send_time: int = None,
        message_template_id: int = None,
        message_variable_param: str = None,
        msisdns: List[str] = None,
        task_name: str = None,
    ):
        # Linkcard
        self.api_product = api_product
        self.message_send_time = message_send_time
        self.message_template_id = message_template_id
        self.message_variable_param = message_variable_param
        self.msisdns = msisdns
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_product is not None:
            result['ApiProduct'] = self.api_product
        if self.message_send_time is not None:
            result['MessageSendTime'] = self.message_send_time
        if self.message_template_id is not None:
            result['MessageTemplateId'] = self.message_template_id
        if self.message_variable_param is not None:
            result['MessageVariableParam'] = self.message_variable_param
        if self.msisdns is not None:
            result['Msisdns'] = self.msisdns
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiProduct') is not None:
            self.api_product = m.get('ApiProduct')
        if m.get('MessageSendTime') is not None:
            self.message_send_time = m.get('MessageSendTime')
        if m.get('MessageTemplateId') is not None:
            self.message_template_id = m.get('MessageTemplateId')
        if m.get('MessageVariableParam') is not None:
            self.message_variable_param = m.get('MessageVariableParam')
        if m.get('Msisdns') is not None:
            self.msisdns = m.get('Msisdns')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class SendMessageShrinkRequest(TeaModel):
    def __init__(
        self,
        api_product: str = None,
        message_send_time: int = None,
        message_template_id: int = None,
        message_variable_param: str = None,
        msisdns_shrink: str = None,
        task_name: str = None,
    ):
        # Linkcard
        self.api_product = api_product
        self.message_send_time = message_send_time
        self.message_template_id = message_template_id
        self.message_variable_param = message_variable_param
        self.msisdns_shrink = msisdns_shrink
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_product is not None:
            result['ApiProduct'] = self.api_product
        if self.message_send_time is not None:
            result['MessageSendTime'] = self.message_send_time
        if self.message_template_id is not None:
            result['MessageTemplateId'] = self.message_template_id
        if self.message_variable_param is not None:
            result['MessageVariableParam'] = self.message_variable_param
        if self.msisdns_shrink is not None:
            result['Msisdns'] = self.msisdns_shrink
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiProduct') is not None:
            self.api_product = m.get('ApiProduct')
        if m.get('MessageSendTime') is not None:
            self.message_send_time = m.get('MessageSendTime')
        if m.get('MessageTemplateId') is not None:
            self.message_template_id = m.get('MessageTemplateId')
        if m.get('MessageVariableParam') is not None:
            self.message_variable_param = m.get('MessageVariableParam')
        if m.get('Msisdns') is not None:
            self.msisdns_shrink = m.get('Msisdns')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class SendMessageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: int = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_message: str = None,
        localized_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_message = error_message
        self.localized_message = localized_message
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
        if self.data is not None:
            result['Data'] = self.data
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.localized_message is not None:
            result['LocalizedMessage'] = self.localized_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('LocalizedMessage') is not None:
            self.localized_message = m.get('LocalizedMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SendMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendMessageResponseBody = None,
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
            temp_model = SendMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetCardStopRuleRequest(TeaModel):
    def __init__(
        self,
        auto_restore: bool = None,
        flow_limit: int = None,
        iccid: str = None,
    ):
        self.auto_restore = auto_restore
        self.flow_limit = flow_limit
        self.iccid = iccid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_restore is not None:
            result['AutoRestore'] = self.auto_restore
        if self.flow_limit is not None:
            result['FlowLimit'] = self.flow_limit
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRestore') is not None:
            self.auto_restore = m.get('AutoRestore')
        if m.get('FlowLimit') is not None:
            self.flow_limit = m.get('FlowLimit')
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        return self


class SetCardStopRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        error_message: str = None,
        localized_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
        self.localized_message = localized_message
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
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.localized_message is not None:
            result['LocalizedMessage'] = self.localized_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('LocalizedMessage') is not None:
            self.localized_message = m.get('LocalizedMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SetCardStopRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetCardStopRuleResponseBody = None,
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
            temp_model = SetCardStopRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopSingleCardRequest(TeaModel):
    def __init__(
        self,
        iccid: str = None,
        opt_msisdns: List[str] = None,
    ):
        self.iccid = iccid
        self.opt_msisdns = opt_msisdns

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        if self.opt_msisdns is not None:
            result['OptMsisdns'] = self.opt_msisdns
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        if m.get('OptMsisdns') is not None:
            self.opt_msisdns = m.get('OptMsisdns')
        return self


class StopSingleCardShrinkRequest(TeaModel):
    def __init__(
        self,
        iccid: str = None,
        opt_msisdns_shrink: str = None,
    ):
        self.iccid = iccid
        self.opt_msisdns_shrink = opt_msisdns_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        if self.opt_msisdns_shrink is not None:
            result['OptMsisdns'] = self.opt_msisdns_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        if m.get('OptMsisdns') is not None:
            self.opt_msisdns_shrink = m.get('OptMsisdns')
        return self


class StopSingleCardResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        error_message: str = None,
        localized_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
        self.localized_message = localized_message
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
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.localized_message is not None:
            result['LocalizedMessage'] = self.localized_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('LocalizedMessage') is not None:
            self.localized_message = m.get('LocalizedMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StopSingleCardResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopSingleCardResponseBody = None,
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
            temp_model = StopSingleCardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAutoRechargeSwitchRequest(TeaModel):
    def __init__(
        self,
        iccid: str = None,
        open: bool = None,
    ):
        self.iccid = iccid
        self.open = open

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        if self.open is not None:
            result['Open'] = self.open
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        if m.get('Open') is not None:
            self.open = m.get('Open')
        return self


class UpdateAutoRechargeSwitchResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        error_message: str = None,
        localized_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
        self.localized_message = localized_message
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
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.localized_message is not None:
            result['LocalizedMessage'] = self.localized_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('LocalizedMessage') is not None:
            self.localized_message = m.get('LocalizedMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateAutoRechargeSwitchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateAutoRechargeSwitchResponseBody = None,
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
            temp_model = UpdateAutoRechargeSwitchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyIotCardRequest(TeaModel):
    def __init__(
        self,
        iccid: str = None,
    ):
        self.iccid = iccid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        return self


class VerifyIotCardResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        error_message: str = None,
        localized_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
        self.localized_message = localized_message
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
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.localized_message is not None:
            result['LocalizedMessage'] = self.localized_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('LocalizedMessage') is not None:
            self.localized_message = m.get('LocalizedMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class VerifyIotCardResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VerifyIotCardResponseBody = None,
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
            temp_model = VerifyIotCardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


