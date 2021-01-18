# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class DetectIPCPedestrianOptimizedRequest(TeaModel):
    def __init__(
        self,
        image_data: bytes = None,
        width: int = None,
        height: int = None,
    ):
        # image data
        self.image_data = image_data
        # image width
        self.width = width
        # image height
        self.height = height

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_data is not None:
            result['imageData'] = self.image_data
        if self.width is not None:
            result['width'] = self.width
        if self.height is not None:
            result['height'] = self.height
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('imageData') is not None:
            self.image_data = m.get('imageData')
        if m.get('width') is not None:
            self.width = m.get('width')
        if m.get('height') is not None:
            self.height = m.get('height')
        return self


class DetectIPCPedestrianOptimizedResponseBodyDataImageInfoListElements(TeaModel):
    def __init__(
        self,
        boxes: List[int] = None,
        score: float = None,
    ):
        # box array
        self.boxes = boxes
        # score
        self.score = score

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.boxes is not None:
            result['Boxes'] = self.boxes
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Boxes') is not None:
            self.boxes = m.get('Boxes')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class DetectIPCPedestrianOptimizedResponseBodyDataImageInfoList(TeaModel):
    def __init__(
        self,
        elements: List[DetectIPCPedestrianOptimizedResponseBodyDataImageInfoListElements] = None,
    ):
        # Elements
        self.elements = elements

    def validate(self):
        if self.elements:
            for k in self.elements:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Elements'] = []
        if self.elements is not None:
            for k in self.elements:
                result['Elements'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.elements = []
        if m.get('Elements') is not None:
            for k in m.get('Elements'):
                temp_model = DetectIPCPedestrianOptimizedResponseBodyDataImageInfoListElements()
                self.elements.append(temp_model.from_map(k))
        return self


class DetectIPCPedestrianOptimizedResponseBodyData(TeaModel):
    def __init__(
        self,
        image_info_list: List[DetectIPCPedestrianOptimizedResponseBodyDataImageInfoList] = None,
    ):
        # imageInfoList
        self.image_info_list = image_info_list

    def validate(self):
        if self.image_info_list:
            for k in self.image_info_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ImageInfoList'] = []
        if self.image_info_list is not None:
            for k in self.image_info_list:
                result['ImageInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.image_info_list = []
        if m.get('ImageInfoList') is not None:
            for k in m.get('ImageInfoList'):
                temp_model = DetectIPCPedestrianOptimizedResponseBodyDataImageInfoList()
                self.image_info_list.append(temp_model.from_map(k))
        return self


class DetectIPCPedestrianOptimizedResponseBody(TeaModel):
    def __init__(
        self,
        data: DetectIPCPedestrianOptimizedResponseBodyData = None,
        request_id: str = None,
    ):
        # data
        self.data = data
        # requestId
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DetectIPCPedestrianOptimizedResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetectIPCPedestrianOptimizedResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DetectIPCPedestrianOptimizedResponseBody = None,
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
            temp_model = DetectIPCPedestrianOptimizedResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteServerSideVerificationRequest(TeaModel):
    def __init__(
        self,
        certificate_name: str = None,
        certificate_number: str = None,
        facial_picture_data: bytes = None,
        facial_picture_url: str = None,
        scene_type: str = None,
    ):
        self.certificate_name = certificate_name
        self.certificate_number = certificate_number
        self.facial_picture_data = facial_picture_data
        self.facial_picture_url = facial_picture_url
        self.scene_type = scene_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.certificate_name is not None:
            result['certificateName'] = self.certificate_name
        if self.certificate_number is not None:
            result['certificateNumber'] = self.certificate_number
        if self.facial_picture_data is not None:
            result['facialPictureData'] = self.facial_picture_data
        if self.facial_picture_url is not None:
            result['facialPictureUrl'] = self.facial_picture_url
        if self.scene_type is not None:
            result['sceneType'] = self.scene_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('certificateName') is not None:
            self.certificate_name = m.get('certificateName')
        if m.get('certificateNumber') is not None:
            self.certificate_number = m.get('certificateNumber')
        if m.get('facialPictureData') is not None:
            self.facial_picture_data = m.get('facialPictureData')
        if m.get('facialPictureUrl') is not None:
            self.facial_picture_url = m.get('facialPictureUrl')
        if m.get('sceneType') is not None:
            self.scene_type = m.get('sceneType')
        return self


class ExecuteServerSideVerificationResponseBodyData(TeaModel):
    def __init__(
        self,
        pass_: bool = None,
        verification_token: str = None,
        reason: str = None,
    ):
        self.pass_ = pass_
        self.verification_token = verification_token
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.pass_ is not None:
            result['Pass'] = self.pass_
        if self.verification_token is not None:
            result['VerificationToken'] = self.verification_token
        if self.reason is not None:
            result['Reason'] = self.reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pass') is not None:
            self.pass_ = m.get('Pass')
        if m.get('VerificationToken') is not None:
            self.verification_token = m.get('VerificationToken')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        return self


class ExecuteServerSideVerificationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: ExecuteServerSideVerificationResponseBodyData = None,
        code: str = None,
        message: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.data = data
        self.code = code
        self.message = message

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ExecuteServerSideVerificationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class ExecuteServerSideVerificationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ExecuteServerSideVerificationResponseBody = None,
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
            temp_model = ExecuteServerSideVerificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


