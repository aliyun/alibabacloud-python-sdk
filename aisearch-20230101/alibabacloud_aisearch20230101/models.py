# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, BinaryIO, Dict


class Box(TeaModel):
    def __init__(
        self,
        height: int = None,
        left: int = None,
        top: int = None,
        width: int = None,
    ):
        self.height = height
        self.left = left
        self.top = top
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.height is not None:
            result['Height'] = self.height
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class AddImageRequest(TeaModel):
    def __init__(
        self,
        boxes: List[Box] = None,
        custom_content: str = None,
        detect_limit: int = None,
        int_attr: int = None,
        pic_content: str = None,
        pic_name: str = None,
        pic_url: str = None,
        str_attr: str = None,
    ):
        self.boxes = boxes
        self.custom_content = custom_content
        self.detect_limit = detect_limit
        self.int_attr = int_attr
        self.pic_content = pic_content
        self.pic_name = pic_name
        self.pic_url = pic_url
        self.str_attr = str_attr

    def validate(self):
        if self.boxes:
            for k in self.boxes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Boxes'] = []
        if self.boxes is not None:
            for k in self.boxes:
                result['Boxes'].append(k.to_map() if k else None)
        if self.custom_content is not None:
            result['CustomContent'] = self.custom_content
        if self.detect_limit is not None:
            result['DetectLimit'] = self.detect_limit
        if self.int_attr is not None:
            result['IntAttr'] = self.int_attr
        if self.pic_content is not None:
            result['PicContent'] = self.pic_content
        if self.pic_name is not None:
            result['PicName'] = self.pic_name
        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url
        if self.str_attr is not None:
            result['StrAttr'] = self.str_attr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.boxes = []
        if m.get('Boxes') is not None:
            for k in m.get('Boxes'):
                temp_model = Box()
                self.boxes.append(temp_model.from_map(k))
        if m.get('CustomContent') is not None:
            self.custom_content = m.get('CustomContent')
        if m.get('DetectLimit') is not None:
            self.detect_limit = m.get('DetectLimit')
        if m.get('IntAttr') is not None:
            self.int_attr = m.get('IntAttr')
        if m.get('PicContent') is not None:
            self.pic_content = m.get('PicContent')
        if m.get('PicName') is not None:
            self.pic_name = m.get('PicName')
        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')
        if m.get('StrAttr') is not None:
            self.str_attr = m.get('StrAttr')
        return self


class AddImageAdvanceRequest(TeaModel):
    def __init__(
        self,
        boxes: List[Box] = None,
        custom_content: str = None,
        detect_limit: int = None,
        int_attr: int = None,
        pic_content_object: BinaryIO = None,
        pic_name: str = None,
        pic_url: str = None,
        str_attr: str = None,
    ):
        self.boxes = boxes
        self.custom_content = custom_content
        self.detect_limit = detect_limit
        self.int_attr = int_attr
        self.pic_content_object = pic_content_object
        self.pic_name = pic_name
        self.pic_url = pic_url
        self.str_attr = str_attr

    def validate(self):
        if self.boxes:
            for k in self.boxes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Boxes'] = []
        if self.boxes is not None:
            for k in self.boxes:
                result['Boxes'].append(k.to_map() if k else None)
        if self.custom_content is not None:
            result['CustomContent'] = self.custom_content
        if self.detect_limit is not None:
            result['DetectLimit'] = self.detect_limit
        if self.int_attr is not None:
            result['IntAttr'] = self.int_attr
        if self.pic_content_object is not None:
            result['PicContent'] = self.pic_content_object
        if self.pic_name is not None:
            result['PicName'] = self.pic_name
        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url
        if self.str_attr is not None:
            result['StrAttr'] = self.str_attr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.boxes = []
        if m.get('Boxes') is not None:
            for k in m.get('Boxes'):
                temp_model = Box()
                self.boxes.append(temp_model.from_map(k))
        if m.get('CustomContent') is not None:
            self.custom_content = m.get('CustomContent')
        if m.get('DetectLimit') is not None:
            self.detect_limit = m.get('DetectLimit')
        if m.get('IntAttr') is not None:
            self.int_attr = m.get('IntAttr')
        if m.get('PicContent') is not None:
            self.pic_content_object = m.get('PicContent')
        if m.get('PicName') is not None:
            self.pic_name = m.get('PicName')
        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')
        if m.get('StrAttr') is not None:
            self.str_attr = m.get('StrAttr')
        return self


class AddImageShrinkRequest(TeaModel):
    def __init__(
        self,
        boxes_shrink: str = None,
        custom_content: str = None,
        detect_limit: int = None,
        int_attr: int = None,
        pic_content: str = None,
        pic_name: str = None,
        pic_url: str = None,
        str_attr: str = None,
    ):
        self.boxes_shrink = boxes_shrink
        self.custom_content = custom_content
        self.detect_limit = detect_limit
        self.int_attr = int_attr
        self.pic_content = pic_content
        self.pic_name = pic_name
        self.pic_url = pic_url
        self.str_attr = str_attr

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.boxes_shrink is not None:
            result['Boxes'] = self.boxes_shrink
        if self.custom_content is not None:
            result['CustomContent'] = self.custom_content
        if self.detect_limit is not None:
            result['DetectLimit'] = self.detect_limit
        if self.int_attr is not None:
            result['IntAttr'] = self.int_attr
        if self.pic_content is not None:
            result['PicContent'] = self.pic_content
        if self.pic_name is not None:
            result['PicName'] = self.pic_name
        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url
        if self.str_attr is not None:
            result['StrAttr'] = self.str_attr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Boxes') is not None:
            self.boxes_shrink = m.get('Boxes')
        if m.get('CustomContent') is not None:
            self.custom_content = m.get('CustomContent')
        if m.get('DetectLimit') is not None:
            self.detect_limit = m.get('DetectLimit')
        if m.get('IntAttr') is not None:
            self.int_attr = m.get('IntAttr')
        if m.get('PicContent') is not None:
            self.pic_content = m.get('PicContent')
        if m.get('PicName') is not None:
            self.pic_name = m.get('PicName')
        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')
        if m.get('StrAttr') is not None:
            self.str_attr = m.get('StrAttr')
        return self


class AddImageResponseBody(TeaModel):
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
            temp_model = AddImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceResponseBodyData(TeaModel):
    def __init__(
        self,
        capacity: int = None,
        instance_id: str = None,
        instance_name: str = None,
        qps: str = None,
        region: str = None,
        service_type: str = None,
        status: str = None,
        total_count: int = None,
        utc_create_time: int = None,
        utc_expire_time: int = None,
    ):
        self.capacity = capacity
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.qps = qps
        self.region = region
        self.service_type = service_type
        self.status = status
        self.total_count = total_count
        self.utc_create_time = utc_create_time
        self.utc_expire_time = utc_expire_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.qps is not None:
            result['Qps'] = self.qps
        if self.region is not None:
            result['Region'] = self.region
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.status is not None:
            result['Status'] = self.status
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.utc_create_time is not None:
            result['UtcCreateTime'] = self.utc_create_time
        if self.utc_expire_time is not None:
            result['UtcExpireTime'] = self.utc_expire_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Qps') is not None:
            self.qps = m.get('Qps')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('UtcCreateTime') is not None:
            self.utc_create_time = m.get('UtcCreateTime')
        if m.get('UtcExpireTime') is not None:
            self.utc_expire_time = m.get('UtcExpireTime')
        return self


class GetInstanceResponseBody(TeaModel):
    def __init__(
        self,
        data: GetInstanceResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
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
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetInstanceResponseBody = None,
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
            temp_model = GetInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateImageRequest(TeaModel):
    def __init__(
        self,
        custom_content: str = None,
        int_attr: int = None,
        pic_name: str = None,
        str_attr: str = None,
    ):
        self.custom_content = custom_content
        self.int_attr = int_attr
        self.pic_name = pic_name
        self.str_attr = str_attr

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_content is not None:
            result['CustomContent'] = self.custom_content
        if self.int_attr is not None:
            result['IntAttr'] = self.int_attr
        if self.pic_name is not None:
            result['PicName'] = self.pic_name
        if self.str_attr is not None:
            result['StrAttr'] = self.str_attr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomContent') is not None:
            self.custom_content = m.get('CustomContent')
        if m.get('IntAttr') is not None:
            self.int_attr = m.get('IntAttr')
        if m.get('PicName') is not None:
            self.pic_name = m.get('PicName')
        if m.get('StrAttr') is not None:
            self.str_attr = m.get('StrAttr')
        return self


class UpdateImageResponseBody(TeaModel):
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


class UpdateImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateImageResponseBody = None,
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
            temp_model = UpdateImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


