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


class CheckOssIncrementMetaExistRequest(TeaModel):
    def __init__(
        self,
        bucket_name: str = None,
        key: str = None,
        oss_path: str = None,
    ):
        # oss bucket
        self.bucket_name = bucket_name
        self.key = key
        # oss path
        self.oss_path = oss_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.key is not None:
            result['Key'] = self.key
        if self.oss_path is not None:
            result['OssPath'] = self.oss_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('OssPath') is not None:
            self.oss_path = m.get('OssPath')
        return self


class CheckOssIncrementMetaExistResponseBodyData(TeaModel):
    def __init__(
        self,
        exist: bool = None,
    ):
        self.exist = exist

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exist is not None:
            result['Exist'] = self.exist
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Exist') is not None:
            self.exist = m.get('Exist')
        return self


class CheckOssIncrementMetaExistResponseBody(TeaModel):
    def __init__(
        self,
        data: CheckOssIncrementMetaExistResponseBodyData = None,
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
            temp_model = CheckOssIncrementMetaExistResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckOssIncrementMetaExistResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckOssIncrementMetaExistResponseBody = None,
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
            temp_model = CheckOssIncrementMetaExistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBatchTasksRequest(TeaModel):
    def __init__(
        self,
        bucket_name: str = None,
        callback_address: str = None,
        oss_path: str = None,
    ):
        # oss bucket
        self.bucket_name = bucket_name
        self.callback_address = callback_address
        # oss path
        self.oss_path = oss_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.callback_address is not None:
            result['CallbackAddress'] = self.callback_address
        if self.oss_path is not None:
            result['OssPath'] = self.oss_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('CallbackAddress') is not None:
            self.callback_address = m.get('CallbackAddress')
        if m.get('OssPath') is not None:
            self.oss_path = m.get('OssPath')
        return self


class CreateBatchTasksResponseBodyData(TeaModel):
    def __init__(
        self,
        id: int = None,
        status: str = None,
    ):
        self.id = id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateBatchTasksResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateBatchTasksResponseBodyData = None,
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
            temp_model = CreateBatchTasksResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateBatchTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateBatchTasksResponseBody = None,
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
            temp_model = CreateBatchTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDumpMetaResponseBodyData(TeaModel):
    def __init__(
        self,
        id: int = None,
        status: str = None,
    ):
        self.id = id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateDumpMetaResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateDumpMetaResponseBodyData = None,
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
            temp_model = CreateDumpMetaResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateDumpMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDumpMetaResponseBody = None,
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
            temp_model = CreateDumpMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteImageRequest(TeaModel):
    def __init__(
        self,
        pic_name: str = None,
    ):
        self.pic_name = pic_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pic_name is not None:
            result['PicName'] = self.pic_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PicName') is not None:
            self.pic_name = m.get('PicName')
        return self


class DeleteImageResponseBodyData(TeaModel):
    def __init__(
        self,
        pic_names: List[str] = None,
    ):
        self.pic_names = pic_names

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pic_names is not None:
            result['PicNames'] = self.pic_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PicNames') is not None:
            self.pic_names = m.get('PicNames')
        return self


class DeleteImageResponseBody(TeaModel):
    def __init__(
        self,
        data: DeleteImageResponseBodyData = None,
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
            temp_model = DeleteImageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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


class GetImageRequest(TeaModel):
    def __init__(
        self,
        pic_name: str = None,
    ):
        self.pic_name = pic_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pic_name is not None:
            result['PicName'] = self.pic_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PicName') is not None:
            self.pic_name = m.get('PicName')
        return self


class GetImageResponseBodyDataBoxes(TeaModel):
    def __init__(
        self,
        bbox: List[int] = None,
        confidence: float = None,
    ):
        self.bbox = bbox
        self.confidence = confidence

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bbox is not None:
            result['Bbox'] = self.bbox
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bbox') is not None:
            self.bbox = m.get('Bbox')
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        return self


class GetImageResponseBodyData(TeaModel):
    def __init__(
        self,
        boxes: List[GetImageResponseBodyDataBoxes] = None,
        custom_content: str = None,
        int_attr: int = None,
        pic_name: str = None,
        product_id: str = None,
        str_attr: str = None,
    ):
        self.boxes = boxes
        self.custom_content = custom_content
        self.int_attr = int_attr
        self.pic_name = pic_name
        self.product_id = product_id
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
        if self.int_attr is not None:
            result['IntAttr'] = self.int_attr
        if self.pic_name is not None:
            result['PicName'] = self.pic_name
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.str_attr is not None:
            result['StrAttr'] = self.str_attr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.boxes = []
        if m.get('Boxes') is not None:
            for k in m.get('Boxes'):
                temp_model = GetImageResponseBodyDataBoxes()
                self.boxes.append(temp_model.from_map(k))
        if m.get('CustomContent') is not None:
            self.custom_content = m.get('CustomContent')
        if m.get('IntAttr') is not None:
            self.int_attr = m.get('IntAttr')
        if m.get('PicName') is not None:
            self.pic_name = m.get('PicName')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('StrAttr') is not None:
            self.str_attr = m.get('StrAttr')
        return self


class GetImageResponseBody(TeaModel):
    def __init__(
        self,
        data: GetImageResponseBodyData = None,
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
            temp_model = GetImageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetImageResponseBody = None,
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
            temp_model = GetImageResponseBody()
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


class ListBatchTasksRequest(TeaModel):
    def __init__(
        self,
        bucket_name: str = None,
        id: int = None,
        oss_path: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # oss bucket
        self.bucket_name = bucket_name
        self.id = id
        # oss path
        self.oss_path = oss_path
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.id is not None:
            result['Id'] = self.id
        if self.oss_path is not None:
            result['OssPath'] = self.oss_path
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OssPath') is not None:
            self.oss_path = m.get('OssPath')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListBatchTasksResponseBodyDataIncrements(TeaModel):
    def __init__(
        self,
        bucket_name: str = None,
        callback_address: str = None,
        callback_task_status: str = None,
        error_url: str = None,
        id: int = None,
        msg: str = None,
        oss_path: str = None,
        status: str = None,
        utc_create_time: str = None,
        utc_update_time: str = None,
    ):
        self.bucket_name = bucket_name
        self.callback_address = callback_address
        self.callback_task_status = callback_task_status
        self.error_url = error_url
        self.id = id
        self.msg = msg
        self.oss_path = oss_path
        self.status = status
        self.utc_create_time = utc_create_time
        self.utc_update_time = utc_update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.callback_address is not None:
            result['CallbackAddress'] = self.callback_address
        if self.callback_task_status is not None:
            result['CallbackTaskStatus'] = self.callback_task_status
        if self.error_url is not None:
            result['ErrorUrl'] = self.error_url
        if self.id is not None:
            result['Id'] = self.id
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.oss_path is not None:
            result['OssPath'] = self.oss_path
        if self.status is not None:
            result['Status'] = self.status
        if self.utc_create_time is not None:
            result['UtcCreateTime'] = self.utc_create_time
        if self.utc_update_time is not None:
            result['UtcUpdateTime'] = self.utc_update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('CallbackAddress') is not None:
            self.callback_address = m.get('CallbackAddress')
        if m.get('CallbackTaskStatus') is not None:
            self.callback_task_status = m.get('CallbackTaskStatus')
        if m.get('ErrorUrl') is not None:
            self.error_url = m.get('ErrorUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('OssPath') is not None:
            self.oss_path = m.get('OssPath')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UtcCreateTime') is not None:
            self.utc_create_time = m.get('UtcCreateTime')
        if m.get('UtcUpdateTime') is not None:
            self.utc_update_time = m.get('UtcUpdateTime')
        return self


class ListBatchTasksResponseBodyData(TeaModel):
    def __init__(
        self,
        increments: List[ListBatchTasksResponseBodyDataIncrements] = None,
        page_number: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.increments = increments
        self.page_number = page_number
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.increments:
            for k in self.increments:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Increments'] = []
        if self.increments is not None:
            for k in self.increments:
                result['Increments'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.increments = []
        if m.get('Increments') is not None:
            for k in m.get('Increments'):
                temp_model = ListBatchTasksResponseBodyDataIncrements()
                self.increments.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListBatchTasksResponseBody(TeaModel):
    def __init__(
        self,
        data: ListBatchTasksResponseBodyData = None,
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
            temp_model = ListBatchTasksResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListBatchTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListBatchTasksResponseBody = None,
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
            temp_model = ListBatchTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDumpMetaRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.id = id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListDumpMetaResponseBodyDataDumpMetaList(TeaModel):
    def __init__(
        self,
        id: int = None,
        meta_url: str = None,
        msg: str = None,
        status: str = None,
        utc_create_time: str = None,
        utc_update_time: str = None,
    ):
        self.id = id
        self.meta_url = meta_url
        self.msg = msg
        self.status = status
        self.utc_create_time = utc_create_time
        self.utc_update_time = utc_update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.meta_url is not None:
            result['MetaUrl'] = self.meta_url
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.status is not None:
            result['Status'] = self.status
        if self.utc_create_time is not None:
            result['UtcCreateTime'] = self.utc_create_time
        if self.utc_update_time is not None:
            result['UtcUpdateTime'] = self.utc_update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MetaUrl') is not None:
            self.meta_url = m.get('MetaUrl')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UtcCreateTime') is not None:
            self.utc_create_time = m.get('UtcCreateTime')
        if m.get('UtcUpdateTime') is not None:
            self.utc_update_time = m.get('UtcUpdateTime')
        return self


class ListDumpMetaResponseBodyData(TeaModel):
    def __init__(
        self,
        dump_meta_list: List[ListDumpMetaResponseBodyDataDumpMetaList] = None,
        page_number: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.dump_meta_list = dump_meta_list
        self.page_number = page_number
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.dump_meta_list:
            for k in self.dump_meta_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DumpMetaList'] = []
        if self.dump_meta_list is not None:
            for k in self.dump_meta_list:
                result['DumpMetaList'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dump_meta_list = []
        if m.get('DumpMetaList') is not None:
            for k in m.get('DumpMetaList'):
                temp_model = ListDumpMetaResponseBodyDataDumpMetaList()
                self.dump_meta_list.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListDumpMetaResponseBody(TeaModel):
    def __init__(
        self,
        data: ListDumpMetaResponseBodyData = None,
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
            temp_model = ListDumpMetaResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListDumpMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDumpMetaResponseBody = None,
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
            temp_model = ListDumpMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        page_number: int = None,
        page_size: int = None,
        service_type: str = None,
    ):
        self.instance_name = instance_name
        self.page_number = page_number
        self.page_size = page_size
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        return self


class ListInstanceResponseBodyDataInstances(TeaModel):
    def __init__(
        self,
        capacity: int = None,
        instance_id: str = None,
        instance_name: str = None,
        qps: str = None,
        region: str = None,
        service_type: str = None,
        status: str = None,
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
        if m.get('UtcCreateTime') is not None:
            self.utc_create_time = m.get('UtcCreateTime')
        if m.get('UtcExpireTime') is not None:
            self.utc_expire_time = m.get('UtcExpireTime')
        return self


class ListInstanceResponseBodyData(TeaModel):
    def __init__(
        self,
        instances: List[ListInstanceResponseBodyDataInstances] = None,
        page_number: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.instances = instances
        self.page_number = page_number
        self.page_size = page_size
        self.total = total

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
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = ListInstanceResponseBodyDataInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListInstanceResponseBody(TeaModel):
    def __init__(
        self,
        data: ListInstanceResponseBodyData = None,
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
            temp_model = ListInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInstanceResponseBody = None,
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
            temp_model = ListInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOssBucketAndPathRequest(TeaModel):
    def __init__(
        self,
        bucket_name: str = None,
        oss_path: str = None,
    ):
        self.bucket_name = bucket_name
        self.oss_path = oss_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.oss_path is not None:
            result['OssPath'] = self.oss_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('OssPath') is not None:
            self.oss_path = m.get('OssPath')
        return self


class ListOssBucketAndPathResponseBodyData(TeaModel):
    def __init__(
        self,
        bucket_list: List[str] = None,
        path_list: List[str] = None,
    ):
        self.bucket_list = bucket_list
        self.path_list = path_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_list is not None:
            result['BucketList'] = self.bucket_list
        if self.path_list is not None:
            result['PathList'] = self.path_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketList') is not None:
            self.bucket_list = m.get('BucketList')
        if m.get('PathList') is not None:
            self.path_list = m.get('PathList')
        return self


class ListOssBucketAndPathResponseBody(TeaModel):
    def __init__(
        self,
        data: ListOssBucketAndPathResponseBodyData = None,
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
            temp_model = ListOssBucketAndPathResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListOssBucketAndPathResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListOssBucketAndPathResponseBody = None,
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
            temp_model = ListOssBucketAndPathResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetInstanceResponseBodyData(TeaModel):
    def __init__(
        self,
        capacity: int = None,
        instance_id: str = None,
        instance_name: str = None,
        service_type: str = None,
        status: str = None,
        utc_create_time: int = None,
        utc_expire_time: int = None,
    ):
        self.capacity = capacity
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.service_type = service_type
        self.status = status
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
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.status is not None:
            result['Status'] = self.status
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
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UtcCreateTime') is not None:
            self.utc_create_time = m.get('UtcCreateTime')
        if m.get('UtcExpireTime') is not None:
            self.utc_expire_time = m.get('UtcExpireTime')
        return self


class ResetInstanceResponseBody(TeaModel):
    def __init__(
        self,
        data: ResetInstanceResponseBodyData = None,
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
            temp_model = ResetInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ResetInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResetInstanceResponseBody = None,
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
            temp_model = ResetInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchImageByNameRequest(TeaModel):
    def __init__(
        self,
        filter: str = None,
        num: int = None,
        pic_name: str = None,
        product_id: str = None,
        start: int = None,
        text: str = None,
    ):
        self.filter = filter
        self.num = num
        self.pic_name = pic_name
        self.product_id = product_id
        self.start = start
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.num is not None:
            result['Num'] = self.num
        if self.pic_name is not None:
            result['PicName'] = self.pic_name
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.start is not None:
            result['Start'] = self.start
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('Num') is not None:
            self.num = m.get('Num')
        if m.get('PicName') is not None:
            self.pic_name = m.get('PicName')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class SearchImageByNameResponseBodyDataPicInfos(TeaModel):
    def __init__(
        self,
        bbox: List[int] = None,
        confidence: float = None,
    ):
        self.bbox = bbox
        self.confidence = confidence

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bbox is not None:
            result['Bbox'] = self.bbox
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bbox') is not None:
            self.bbox = m.get('Bbox')
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        return self


class SearchImageByNameResponseBodyDataPicListOtherBoxes(TeaModel):
    def __init__(
        self,
        bbox: List[int] = None,
        confidence: float = None,
    ):
        self.bbox = bbox
        self.confidence = confidence

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bbox is not None:
            result['Bbox'] = self.bbox
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bbox') is not None:
            self.bbox = m.get('Bbox')
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        return self


class SearchImageByNameResponseBodyDataPicListSimilarBoxes(TeaModel):
    def __init__(
        self,
        bbox: List[int] = None,
        confidence: float = None,
        score: float = None,
    ):
        self.bbox = bbox
        self.confidence = confidence
        self.score = score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bbox is not None:
            result['Bbox'] = self.bbox
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bbox') is not None:
            self.bbox = m.get('Bbox')
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class SearchImageByNameResponseBodyDataPicList(TeaModel):
    def __init__(
        self,
        custom_content: str = None,
        int_attr: int = None,
        other_boxes: List[SearchImageByNameResponseBodyDataPicListOtherBoxes] = None,
        pic_name: str = None,
        product_id: str = None,
        score: float = None,
        similar_boxes: List[SearchImageByNameResponseBodyDataPicListSimilarBoxes] = None,
        str_attr: str = None,
    ):
        self.custom_content = custom_content
        self.int_attr = int_attr
        self.other_boxes = other_boxes
        self.pic_name = pic_name
        self.product_id = product_id
        self.score = score
        self.similar_boxes = similar_boxes
        self.str_attr = str_attr

    def validate(self):
        if self.other_boxes:
            for k in self.other_boxes:
                if k:
                    k.validate()
        if self.similar_boxes:
            for k in self.similar_boxes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_content is not None:
            result['CustomContent'] = self.custom_content
        if self.int_attr is not None:
            result['IntAttr'] = self.int_attr
        result['OtherBoxes'] = []
        if self.other_boxes is not None:
            for k in self.other_boxes:
                result['OtherBoxes'].append(k.to_map() if k else None)
        if self.pic_name is not None:
            result['PicName'] = self.pic_name
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.score is not None:
            result['Score'] = self.score
        result['SimilarBoxes'] = []
        if self.similar_boxes is not None:
            for k in self.similar_boxes:
                result['SimilarBoxes'].append(k.to_map() if k else None)
        if self.str_attr is not None:
            result['StrAttr'] = self.str_attr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomContent') is not None:
            self.custom_content = m.get('CustomContent')
        if m.get('IntAttr') is not None:
            self.int_attr = m.get('IntAttr')
        self.other_boxes = []
        if m.get('OtherBoxes') is not None:
            for k in m.get('OtherBoxes'):
                temp_model = SearchImageByNameResponseBodyDataPicListOtherBoxes()
                self.other_boxes.append(temp_model.from_map(k))
        if m.get('PicName') is not None:
            self.pic_name = m.get('PicName')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        self.similar_boxes = []
        if m.get('SimilarBoxes') is not None:
            for k in m.get('SimilarBoxes'):
                temp_model = SearchImageByNameResponseBodyDataPicListSimilarBoxes()
                self.similar_boxes.append(temp_model.from_map(k))
        if m.get('StrAttr') is not None:
            self.str_attr = m.get('StrAttr')
        return self


class SearchImageByNameResponseBodyData(TeaModel):
    def __init__(
        self,
        pic_infos: List[SearchImageByNameResponseBodyDataPicInfos] = None,
        pic_list: List[SearchImageByNameResponseBodyDataPicList] = None,
    ):
        self.pic_infos = pic_infos
        self.pic_list = pic_list

    def validate(self):
        if self.pic_infos:
            for k in self.pic_infos:
                if k:
                    k.validate()
        if self.pic_list:
            for k in self.pic_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PicInfos'] = []
        if self.pic_infos is not None:
            for k in self.pic_infos:
                result['PicInfos'].append(k.to_map() if k else None)
        result['PicList'] = []
        if self.pic_list is not None:
            for k in self.pic_list:
                result['PicList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.pic_infos = []
        if m.get('PicInfos') is not None:
            for k in m.get('PicInfos'):
                temp_model = SearchImageByNameResponseBodyDataPicInfos()
                self.pic_infos.append(temp_model.from_map(k))
        self.pic_list = []
        if m.get('PicList') is not None:
            for k in m.get('PicList'):
                temp_model = SearchImageByNameResponseBodyDataPicList()
                self.pic_list.append(temp_model.from_map(k))
        return self


class SearchImageByNameResponseBody(TeaModel):
    def __init__(
        self,
        data: SearchImageByNameResponseBodyData = None,
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
            temp_model = SearchImageByNameResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SearchImageByNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SearchImageByNameResponseBody = None,
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
            temp_model = SearchImageByNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchImageByPicRequest(TeaModel):
    def __init__(
        self,
        box: Box = None,
        detect_limit: int = None,
        filter: str = None,
        num: int = None,
        pic_content: str = None,
        pic_url: str = None,
        start: int = None,
        text: str = None,
    ):
        self.box = box
        self.detect_limit = detect_limit
        self.filter = filter
        self.num = num
        self.pic_content = pic_content
        self.pic_url = pic_url
        self.start = start
        self.text = text

    def validate(self):
        if self.box:
            self.box.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.box is not None:
            result['Box'] = self.box.to_map()
        if self.detect_limit is not None:
            result['DetectLimit'] = self.detect_limit
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.num is not None:
            result['Num'] = self.num
        if self.pic_content is not None:
            result['PicContent'] = self.pic_content
        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url
        if self.start is not None:
            result['Start'] = self.start
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Box') is not None:
            temp_model = Box()
            self.box = temp_model.from_map(m['Box'])
        if m.get('DetectLimit') is not None:
            self.detect_limit = m.get('DetectLimit')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('Num') is not None:
            self.num = m.get('Num')
        if m.get('PicContent') is not None:
            self.pic_content = m.get('PicContent')
        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class SearchImageByPicAdvanceRequest(TeaModel):
    def __init__(
        self,
        box: Box = None,
        detect_limit: int = None,
        filter: str = None,
        num: int = None,
        pic_content_object: BinaryIO = None,
        pic_url: str = None,
        start: int = None,
        text: str = None,
    ):
        self.box = box
        self.detect_limit = detect_limit
        self.filter = filter
        self.num = num
        self.pic_content_object = pic_content_object
        self.pic_url = pic_url
        self.start = start
        self.text = text

    def validate(self):
        if self.box:
            self.box.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.box is not None:
            result['Box'] = self.box.to_map()
        if self.detect_limit is not None:
            result['DetectLimit'] = self.detect_limit
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.num is not None:
            result['Num'] = self.num
        if self.pic_content_object is not None:
            result['PicContent'] = self.pic_content_object
        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url
        if self.start is not None:
            result['Start'] = self.start
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Box') is not None:
            temp_model = Box()
            self.box = temp_model.from_map(m['Box'])
        if m.get('DetectLimit') is not None:
            self.detect_limit = m.get('DetectLimit')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('Num') is not None:
            self.num = m.get('Num')
        if m.get('PicContent') is not None:
            self.pic_content_object = m.get('PicContent')
        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class SearchImageByPicShrinkRequest(TeaModel):
    def __init__(
        self,
        box_shrink: str = None,
        detect_limit: int = None,
        filter: str = None,
        num: int = None,
        pic_content: str = None,
        pic_url: str = None,
        start: int = None,
        text: str = None,
    ):
        self.box_shrink = box_shrink
        self.detect_limit = detect_limit
        self.filter = filter
        self.num = num
        self.pic_content = pic_content
        self.pic_url = pic_url
        self.start = start
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.box_shrink is not None:
            result['Box'] = self.box_shrink
        if self.detect_limit is not None:
            result['DetectLimit'] = self.detect_limit
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.num is not None:
            result['Num'] = self.num
        if self.pic_content is not None:
            result['PicContent'] = self.pic_content
        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url
        if self.start is not None:
            result['Start'] = self.start
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Box') is not None:
            self.box_shrink = m.get('Box')
        if m.get('DetectLimit') is not None:
            self.detect_limit = m.get('DetectLimit')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('Num') is not None:
            self.num = m.get('Num')
        if m.get('PicContent') is not None:
            self.pic_content = m.get('PicContent')
        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class SearchImageByPicResponseBodyDataPicInfos(TeaModel):
    def __init__(
        self,
        bbox: List[int] = None,
        confidence: float = None,
    ):
        self.bbox = bbox
        self.confidence = confidence

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bbox is not None:
            result['Bbox'] = self.bbox
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bbox') is not None:
            self.bbox = m.get('Bbox')
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        return self


class SearchImageByPicResponseBodyDataPicListOtherBoxes(TeaModel):
    def __init__(
        self,
        bbox: List[int] = None,
        confidence: float = None,
    ):
        self.bbox = bbox
        self.confidence = confidence

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bbox is not None:
            result['Bbox'] = self.bbox
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bbox') is not None:
            self.bbox = m.get('Bbox')
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        return self


class SearchImageByPicResponseBodyDataPicListSimilarBoxes(TeaModel):
    def __init__(
        self,
        bbox: List[int] = None,
        confidence: float = None,
        score: float = None,
    ):
        self.bbox = bbox
        self.confidence = confidence
        self.score = score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bbox is not None:
            result['Bbox'] = self.bbox
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bbox') is not None:
            self.bbox = m.get('Bbox')
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class SearchImageByPicResponseBodyDataPicList(TeaModel):
    def __init__(
        self,
        custom_content: str = None,
        int_attr: int = None,
        other_boxes: List[SearchImageByPicResponseBodyDataPicListOtherBoxes] = None,
        pic_name: str = None,
        product_id: str = None,
        score: float = None,
        similar_boxes: List[SearchImageByPicResponseBodyDataPicListSimilarBoxes] = None,
        str_attr: str = None,
    ):
        self.custom_content = custom_content
        self.int_attr = int_attr
        self.other_boxes = other_boxes
        self.pic_name = pic_name
        self.product_id = product_id
        self.score = score
        self.similar_boxes = similar_boxes
        self.str_attr = str_attr

    def validate(self):
        if self.other_boxes:
            for k in self.other_boxes:
                if k:
                    k.validate()
        if self.similar_boxes:
            for k in self.similar_boxes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_content is not None:
            result['CustomContent'] = self.custom_content
        if self.int_attr is not None:
            result['IntAttr'] = self.int_attr
        result['OtherBoxes'] = []
        if self.other_boxes is not None:
            for k in self.other_boxes:
                result['OtherBoxes'].append(k.to_map() if k else None)
        if self.pic_name is not None:
            result['PicName'] = self.pic_name
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.score is not None:
            result['Score'] = self.score
        result['SimilarBoxes'] = []
        if self.similar_boxes is not None:
            for k in self.similar_boxes:
                result['SimilarBoxes'].append(k.to_map() if k else None)
        if self.str_attr is not None:
            result['StrAttr'] = self.str_attr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomContent') is not None:
            self.custom_content = m.get('CustomContent')
        if m.get('IntAttr') is not None:
            self.int_attr = m.get('IntAttr')
        self.other_boxes = []
        if m.get('OtherBoxes') is not None:
            for k in m.get('OtherBoxes'):
                temp_model = SearchImageByPicResponseBodyDataPicListOtherBoxes()
                self.other_boxes.append(temp_model.from_map(k))
        if m.get('PicName') is not None:
            self.pic_name = m.get('PicName')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        self.similar_boxes = []
        if m.get('SimilarBoxes') is not None:
            for k in m.get('SimilarBoxes'):
                temp_model = SearchImageByPicResponseBodyDataPicListSimilarBoxes()
                self.similar_boxes.append(temp_model.from_map(k))
        if m.get('StrAttr') is not None:
            self.str_attr = m.get('StrAttr')
        return self


class SearchImageByPicResponseBodyData(TeaModel):
    def __init__(
        self,
        pic_infos: List[SearchImageByPicResponseBodyDataPicInfos] = None,
        pic_list: List[SearchImageByPicResponseBodyDataPicList] = None,
    ):
        self.pic_infos = pic_infos
        self.pic_list = pic_list

    def validate(self):
        if self.pic_infos:
            for k in self.pic_infos:
                if k:
                    k.validate()
        if self.pic_list:
            for k in self.pic_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PicInfos'] = []
        if self.pic_infos is not None:
            for k in self.pic_infos:
                result['PicInfos'].append(k.to_map() if k else None)
        result['PicList'] = []
        if self.pic_list is not None:
            for k in self.pic_list:
                result['PicList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.pic_infos = []
        if m.get('PicInfos') is not None:
            for k in m.get('PicInfos'):
                temp_model = SearchImageByPicResponseBodyDataPicInfos()
                self.pic_infos.append(temp_model.from_map(k))
        self.pic_list = []
        if m.get('PicList') is not None:
            for k in m.get('PicList'):
                temp_model = SearchImageByPicResponseBodyDataPicList()
                self.pic_list.append(temp_model.from_map(k))
        return self


class SearchImageByPicResponseBody(TeaModel):
    def __init__(
        self,
        data: SearchImageByPicResponseBodyData = None,
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
            temp_model = SearchImageByPicResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SearchImageByPicResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SearchImageByPicResponseBody = None,
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
            temp_model = SearchImageByPicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopBatchTasksResponseBody(TeaModel):
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


class StopBatchTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopBatchTasksResponseBody = None,
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
            temp_model = StopBatchTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopDumpMetaResponseBody(TeaModel):
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


class StopDumpMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopDumpMetaResponseBody = None,
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
            temp_model = StopDumpMetaResponseBody()
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


