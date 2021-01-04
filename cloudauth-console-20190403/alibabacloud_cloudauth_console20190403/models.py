# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class RetrieveFaceRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        face_64string: str = None,
        face_url: str = None,
    ):
        self.project_id = project_id
        self.face_64string = face_64string
        self.face_url = face_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.face_64string is not None:
            result['Face64String'] = self.face_64string
        if self.face_url is not None:
            result['FaceUrl'] = self.face_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Face64String') is not None:
            self.face_64string = m.get('Face64String')
        if m.get('FaceUrl') is not None:
            self.face_url = m.get('FaceUrl')
        return self


class RetrieveFaceResponseBodyDataData(TeaModel):
    def __init__(
        self,
        user_id: int = None,
        user_name: str = None,
        rate: str = None,
    ):
        self.user_id = user_id
        self.user_name = user_name
        self.rate = rate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.rate is not None:
            result['Rate'] = self.rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        return self


class RetrieveFaceResponseBodyData(TeaModel):
    def __init__(
        self,
        data: List[RetrieveFaceResponseBodyDataData] = None,
    ):
        self.data = data

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = RetrieveFaceResponseBodyDataData()
                self.data.append(temp_model.from_map(k))
        return self


class RetrieveFaceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: RetrieveFaceResponseBodyData = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = RetrieveFaceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RetrieveFaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RetrieveFaceResponseBody = None,
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
            temp_model = RetrieveFaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadIdentifyRecordRequest(TeaModel):
    def __init__(
        self,
        user_id: str = None,
        user_name: str = None,
        project_id: str = None,
        iot_id: str = None,
        identifying_image_base_64: str = None,
        identifying_time: int = None,
        identifying_image_url: str = None,
        device_name: str = None,
        product_key: str = None,
        device_secret: str = None,
        ext: str = None,
    ):
        self.user_id = user_id
        self.user_name = user_name
        self.project_id = project_id
        self.iot_id = iot_id
        self.identifying_image_base_64 = identifying_image_base_64
        self.identifying_time = identifying_time
        self.identifying_image_url = identifying_image_url
        self.device_name = device_name
        self.product_key = product_key
        self.device_secret = device_secret
        self.ext = ext

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.identifying_image_base_64 is not None:
            result['IdentifyingImageBase64'] = self.identifying_image_base_64
        if self.identifying_time is not None:
            result['IdentifyingTime'] = self.identifying_time
        if self.identifying_image_url is not None:
            result['IdentifyingImageUrl'] = self.identifying_image_url
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.device_secret is not None:
            result['DeviceSecret'] = self.device_secret
        if self.ext is not None:
            result['Ext'] = self.ext
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IdentifyingImageBase64') is not None:
            self.identifying_image_base_64 = m.get('IdentifyingImageBase64')
        if m.get('IdentifyingTime') is not None:
            self.identifying_time = m.get('IdentifyingTime')
        if m.get('IdentifyingImageUrl') is not None:
            self.identifying_image_url = m.get('IdentifyingImageUrl')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('DeviceSecret') is not None:
            self.device_secret = m.get('DeviceSecret')
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        return self


class UploadIdentifyRecordResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        http_status_code: int = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UploadIdentifyRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UploadIdentifyRecordResponseBody = None,
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
            temp_model = UploadIdentifyRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


