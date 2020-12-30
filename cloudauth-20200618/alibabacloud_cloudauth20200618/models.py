# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import BinaryIO, Dict


class ContrastSmartVerifyRequest(TeaModel):
    def __init__(
        self,
        scene_id: int = None,
        outer_order_no: str = None,
        mode: str = None,
        cert_type: str = None,
        mobile: str = None,
        ip: str = None,
        user_id: str = None,
        cert_name: str = None,
        cert_no: str = None,
        face_pic_file: str = None,
        face_pic_url: str = None,
        face_pic_string: str = None,
    ):
        self.scene_id = scene_id
        self.outer_order_no = outer_order_no
        self.mode = mode
        self.cert_type = cert_type
        self.mobile = mobile
        self.ip = ip
        self.user_id = user_id
        self.cert_name = cert_name
        self.cert_no = cert_no
        self.face_pic_file = face_pic_file
        self.face_pic_url = face_pic_url
        self.face_pic_string = face_pic_string

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.outer_order_no is not None:
            result['OuterOrderNo'] = self.outer_order_no
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_no is not None:
            result['CertNo'] = self.cert_no
        if self.face_pic_file is not None:
            result['FacePicFile'] = self.face_pic_file
        if self.face_pic_url is not None:
            result['FacePicUrl'] = self.face_pic_url
        if self.face_pic_string is not None:
            result['FacePicString'] = self.face_pic_string
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('OuterOrderNo') is not None:
            self.outer_order_no = m.get('OuterOrderNo')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertNo') is not None:
            self.cert_no = m.get('CertNo')
        if m.get('FacePicFile') is not None:
            self.face_pic_file = m.get('FacePicFile')
        if m.get('FacePicUrl') is not None:
            self.face_pic_url = m.get('FacePicUrl')
        if m.get('FacePicString') is not None:
            self.face_pic_string = m.get('FacePicString')
        return self


class ContrastSmartVerifyAdvanceRequest(TeaModel):
    def __init__(
        self,
        face_pic_file_object: BinaryIO = None,
        scene_id: int = None,
        outer_order_no: str = None,
        mode: str = None,
        cert_type: str = None,
        mobile: str = None,
        ip: str = None,
        user_id: str = None,
        cert_name: str = None,
        cert_no: str = None,
        face_pic_url: str = None,
        face_pic_string: str = None,
    ):
        self.face_pic_file_object = face_pic_file_object
        self.scene_id = scene_id
        self.outer_order_no = outer_order_no
        self.mode = mode
        self.cert_type = cert_type
        self.mobile = mobile
        self.ip = ip
        self.user_id = user_id
        self.cert_name = cert_name
        self.cert_no = cert_no
        self.face_pic_url = face_pic_url
        self.face_pic_string = face_pic_string

    def validate(self):
        self.validate_required(self.face_pic_file_object, 'face_pic_file_object')

    def to_map(self):
        result = dict()
        if self.face_pic_file_object is not None:
            result['FacePicFileObject'] = self.face_pic_file_object
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.outer_order_no is not None:
            result['OuterOrderNo'] = self.outer_order_no
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_no is not None:
            result['CertNo'] = self.cert_no
        if self.face_pic_url is not None:
            result['FacePicUrl'] = self.face_pic_url
        if self.face_pic_string is not None:
            result['FacePicString'] = self.face_pic_string
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FacePicFileObject') is not None:
            self.face_pic_file_object = m.get('FacePicFileObject')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('OuterOrderNo') is not None:
            self.outer_order_no = m.get('OuterOrderNo')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertNo') is not None:
            self.cert_no = m.get('CertNo')
        if m.get('FacePicUrl') is not None:
            self.face_pic_url = m.get('FacePicUrl')
        if m.get('FacePicString') is not None:
            self.face_pic_string = m.get('FacePicString')
        return self


class ContrastSmartVerifyResponseBodyResultObject(TeaModel):
    def __init__(
        self,
        verify_info: str = None,
        sub_code: str = None,
        certify_id: str = None,
        risk_info: str = None,
        passed: str = None,
    ):
        self.verify_info = verify_info
        self.sub_code = sub_code
        self.certify_id = certify_id
        self.risk_info = risk_info
        self.passed = passed

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.verify_info is not None:
            result['VerifyInfo'] = self.verify_info
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.risk_info is not None:
            result['RiskInfo'] = self.risk_info
        if self.passed is not None:
            result['Passed'] = self.passed
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VerifyInfo') is not None:
            self.verify_info = m.get('VerifyInfo')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('RiskInfo') is not None:
            self.risk_info = m.get('RiskInfo')
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
        return self


class ContrastSmartVerifyResponseBody(TeaModel):
    def __init__(
        self,
        result_object: ContrastSmartVerifyResponseBodyResultObject = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.result_object = result_object
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        result = dict()
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResultObject') is not None:
            temp_model = ContrastSmartVerifyResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ContrastSmartVerifyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ContrastSmartVerifyResponseBody = None,
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
            temp_model = ContrastSmartVerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSmartVerifyRequest(TeaModel):
    def __init__(
        self,
        scene_id: int = None,
        certify_id: str = None,
    ):
        self.scene_id = scene_id
        self.certify_id = certify_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        return self


class DescribeSmartVerifyResponseBodyResultObject(TeaModel):
    def __init__(
        self,
        passed_score: float = None,
        material_info: str = None,
        sub_code: str = None,
        passed: str = None,
    ):
        self.passed_score = passed_score
        self.material_info = material_info
        self.sub_code = sub_code
        self.passed = passed

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.passed_score is not None:
            result['PassedScore'] = self.passed_score
        if self.material_info is not None:
            result['MaterialInfo'] = self.material_info
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.passed is not None:
            result['Passed'] = self.passed
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PassedScore') is not None:
            self.passed_score = m.get('PassedScore')
        if m.get('MaterialInfo') is not None:
            self.material_info = m.get('MaterialInfo')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
        return self


class DescribeSmartVerifyResponseBody(TeaModel):
    def __init__(
        self,
        result_object: DescribeSmartVerifyResponseBodyResultObject = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.result_object = result_object
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        result = dict()
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResultObject') is not None:
            temp_model = DescribeSmartVerifyResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DescribeSmartVerifyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSmartVerifyResponseBody = None,
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
            temp_model = DescribeSmartVerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ElementSmartVerifyRequest(TeaModel):
    def __init__(
        self,
        scene_id: int = None,
        outer_order_no: str = None,
        mode: str = None,
        cert_type: str = None,
        cert_name: str = None,
        cert_no: str = None,
        cert_url: str = None,
        cert_file: str = None,
    ):
        self.scene_id = scene_id
        self.outer_order_no = outer_order_no
        self.mode = mode
        self.cert_type = cert_type
        self.cert_name = cert_name
        self.cert_no = cert_no
        self.cert_url = cert_url
        self.cert_file = cert_file

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.outer_order_no is not None:
            result['OuterOrderNo'] = self.outer_order_no
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_no is not None:
            result['CertNo'] = self.cert_no
        if self.cert_url is not None:
            result['CertUrl'] = self.cert_url
        if self.cert_file is not None:
            result['CertFile'] = self.cert_file
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('OuterOrderNo') is not None:
            self.outer_order_no = m.get('OuterOrderNo')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertNo') is not None:
            self.cert_no = m.get('CertNo')
        if m.get('CertUrl') is not None:
            self.cert_url = m.get('CertUrl')
        if m.get('CertFile') is not None:
            self.cert_file = m.get('CertFile')
        return self


class ElementSmartVerifyAdvanceRequest(TeaModel):
    def __init__(
        self,
        cert_file_object: BinaryIO = None,
        scene_id: int = None,
        outer_order_no: str = None,
        mode: str = None,
        cert_type: str = None,
        cert_name: str = None,
        cert_no: str = None,
        cert_url: str = None,
    ):
        self.cert_file_object = cert_file_object
        self.scene_id = scene_id
        self.outer_order_no = outer_order_no
        self.mode = mode
        self.cert_type = cert_type
        self.cert_name = cert_name
        self.cert_no = cert_no
        self.cert_url = cert_url

    def validate(self):
        self.validate_required(self.cert_file_object, 'cert_file_object')

    def to_map(self):
        result = dict()
        if self.cert_file_object is not None:
            result['CertFileObject'] = self.cert_file_object
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.outer_order_no is not None:
            result['OuterOrderNo'] = self.outer_order_no
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_no is not None:
            result['CertNo'] = self.cert_no
        if self.cert_url is not None:
            result['CertUrl'] = self.cert_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertFileObject') is not None:
            self.cert_file_object = m.get('CertFileObject')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('OuterOrderNo') is not None:
            self.outer_order_no = m.get('OuterOrderNo')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertNo') is not None:
            self.cert_no = m.get('CertNo')
        if m.get('CertUrl') is not None:
            self.cert_url = m.get('CertUrl')
        return self


class ElementSmartVerifyResponseBodyResultObject(TeaModel):
    def __init__(
        self,
        material_info: str = None,
        sub_code: str = None,
        passed: str = None,
    ):
        self.material_info = material_info
        self.sub_code = sub_code
        self.passed = passed

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.material_info is not None:
            result['MaterialInfo'] = self.material_info
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.passed is not None:
            result['Passed'] = self.passed
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaterialInfo') is not None:
            self.material_info = m.get('MaterialInfo')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
        return self


class ElementSmartVerifyResponseBody(TeaModel):
    def __init__(
        self,
        result_object: ElementSmartVerifyResponseBodyResultObject = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.result_object = result_object
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        result = dict()
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResultObject') is not None:
            temp_model = ElementSmartVerifyResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ElementSmartVerifyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ElementSmartVerifyResponseBody = None,
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
            temp_model = ElementSmartVerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InitSmartVerifyRequest(TeaModel):
    def __init__(
        self,
        scene_id: int = None,
        outer_order_no: str = None,
        mode: str = None,
        cert_type: str = None,
        meta_info: str = None,
        mobile: str = None,
        ip: str = None,
        user_id: str = None,
        cert_name: str = None,
        cert_no: str = None,
        ocr: str = None,
        callback_url: str = None,
        callback_token: str = None,
        face_picture_base_64: str = None,
        face_picture_url: str = None,
        certify_id: str = None,
        oss_bucket_name: str = None,
        oss_object_name: str = None,
    ):
        self.scene_id = scene_id
        self.outer_order_no = outer_order_no
        self.mode = mode
        self.cert_type = cert_type
        self.meta_info = meta_info
        self.mobile = mobile
        self.ip = ip
        self.user_id = user_id
        self.cert_name = cert_name
        self.cert_no = cert_no
        self.ocr = ocr
        self.callback_url = callback_url
        self.callback_token = callback_token
        self.face_picture_base_64 = face_picture_base_64
        self.face_picture_url = face_picture_url
        self.certify_id = certify_id
        self.oss_bucket_name = oss_bucket_name
        self.oss_object_name = oss_object_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.outer_order_no is not None:
            result['OuterOrderNo'] = self.outer_order_no
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.meta_info is not None:
            result['MetaInfo'] = self.meta_info
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_no is not None:
            result['CertNo'] = self.cert_no
        if self.ocr is not None:
            result['Ocr'] = self.ocr
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        if self.callback_token is not None:
            result['CallbackToken'] = self.callback_token
        if self.face_picture_base_64 is not None:
            result['FacePictureBase64'] = self.face_picture_base_64
        if self.face_picture_url is not None:
            result['FacePictureUrl'] = self.face_picture_url
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name
        if self.oss_object_name is not None:
            result['OssObjectName'] = self.oss_object_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('OuterOrderNo') is not None:
            self.outer_order_no = m.get('OuterOrderNo')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('MetaInfo') is not None:
            self.meta_info = m.get('MetaInfo')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertNo') is not None:
            self.cert_no = m.get('CertNo')
        if m.get('Ocr') is not None:
            self.ocr = m.get('Ocr')
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        if m.get('CallbackToken') is not None:
            self.callback_token = m.get('CallbackToken')
        if m.get('FacePictureBase64') is not None:
            self.face_picture_base_64 = m.get('FacePictureBase64')
        if m.get('FacePictureUrl') is not None:
            self.face_picture_url = m.get('FacePictureUrl')
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')
        if m.get('OssObjectName') is not None:
            self.oss_object_name = m.get('OssObjectName')
        return self


class InitSmartVerifyResponseBodyResultObject(TeaModel):
    def __init__(
        self,
        certify_id: str = None,
    ):
        self.certify_id = certify_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        return self


class InitSmartVerifyResponseBody(TeaModel):
    def __init__(
        self,
        result_object: InitSmartVerifyResponseBodyResultObject = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.result_object = result_object
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        result = dict()
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResultObject') is not None:
            temp_model = InitSmartVerifyResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class InitSmartVerifyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: InitSmartVerifyResponseBody = None,
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
            temp_model = InitSmartVerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


