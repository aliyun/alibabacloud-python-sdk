# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import BinaryIO


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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class ContrastSmartVerifyResponseResultObject(TeaModel):
    def __init__(
        self,
        certify_id: str = None,
        passed: str = None,
        sub_code: str = None,
        verify_info: str = None,
        risk_info: str = None,
    ):
        self.certify_id = certify_id
        self.passed = passed
        self.sub_code = sub_code
        self.verify_info = verify_info
        self.risk_info = risk_info

    def validate(self):
        self.validate_required(self.certify_id, 'certify_id')
        self.validate_required(self.passed, 'passed')
        self.validate_required(self.sub_code, 'sub_code')
        self.validate_required(self.verify_info, 'verify_info')
        self.validate_required(self.risk_info, 'risk_info')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.passed is not None:
            result['Passed'] = self.passed
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.verify_info is not None:
            result['VerifyInfo'] = self.verify_info
        if self.risk_info is not None:
            result['RiskInfo'] = self.risk_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('VerifyInfo') is not None:
            self.verify_info = m.get('VerifyInfo')
        if m.get('RiskInfo') is not None:
            self.risk_info = m.get('RiskInfo')
        return self


class ContrastSmartVerifyResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        code: str = None,
        result_object: ContrastSmartVerifyResponseResultObject = None,
    ):
        self.request_id = request_id
        self.message = message
        self.code = code
        self.result_object = result_object

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.message, 'message')
        self.validate_required(self.code, 'code')
        self.validate_required(self.result_object, 'result_object')
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ResultObject') is not None:
            temp_model = ContrastSmartVerifyResponseResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        cert_national_emblem_url: str = None,
    ):
        self.scene_id = scene_id
        self.outer_order_no = outer_order_no
        self.mode = mode
        self.cert_type = cert_type
        self.cert_name = cert_name
        self.cert_no = cert_no
        self.cert_url = cert_url
        self.cert_file = cert_file
        self.cert_national_emblem_url = cert_national_emblem_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        if self.cert_national_emblem_url is not None:
            result['CertNationalEmblemUrl'] = self.cert_national_emblem_url
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
        if m.get('CertNationalEmblemUrl') is not None:
            self.cert_national_emblem_url = m.get('CertNationalEmblemUrl')
        return self


class ElementSmartVerifyResponseResultObject(TeaModel):
    def __init__(
        self,
        passed: str = None,
        sub_code: str = None,
        material_info: str = None,
        certify_id: str = None,
    ):
        self.passed = passed
        self.sub_code = sub_code
        self.material_info = material_info
        self.certify_id = certify_id

    def validate(self):
        self.validate_required(self.passed, 'passed')
        self.validate_required(self.sub_code, 'sub_code')
        self.validate_required(self.material_info, 'material_info')
        self.validate_required(self.certify_id, 'certify_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.passed is not None:
            result['Passed'] = self.passed
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.material_info is not None:
            result['MaterialInfo'] = self.material_info
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('MaterialInfo') is not None:
            self.material_info = m.get('MaterialInfo')
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        return self


class ElementSmartVerifyResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        code: str = None,
        result_object: ElementSmartVerifyResponseResultObject = None,
    ):
        self.request_id = request_id
        self.message = message
        self.code = code
        self.result_object = result_object

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.message, 'message')
        self.validate_required(self.code, 'code')
        self.validate_required(self.result_object, 'result_object')
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ResultObject') is not None:
            temp_model = ElementSmartVerifyResponseResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
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
        cert_national_emblem_url: str = None,
    ):
        self.cert_file_object = cert_file_object
        self.scene_id = scene_id
        self.outer_order_no = outer_order_no
        self.mode = mode
        self.cert_type = cert_type
        self.cert_name = cert_name
        self.cert_no = cert_no
        self.cert_url = cert_url
        self.cert_national_emblem_url = cert_national_emblem_url

    def validate(self):
        self.validate_required(self.cert_file_object, 'cert_file_object')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        if self.cert_national_emblem_url is not None:
            result['CertNationalEmblemUrl'] = self.cert_national_emblem_url
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
        if m.get('CertNationalEmblemUrl') is not None:
            self.cert_national_emblem_url = m.get('CertNationalEmblemUrl')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class InitSmartVerifyResponseResultObject(TeaModel):
    def __init__(
        self,
        certify_id: str = None,
    ):
        self.certify_id = certify_id

    def validate(self):
        self.validate_required(self.certify_id, 'certify_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        return self


class InitSmartVerifyResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        code: str = None,
        result_object: InitSmartVerifyResponseResultObject = None,
    ):
        self.request_id = request_id
        self.message = message
        self.code = code
        self.result_object = result_object

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.message, 'message')
        self.validate_required(self.code, 'code')
        self.validate_required(self.result_object, 'result_object')
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ResultObject') is not None:
            temp_model = InitSmartVerifyResponseResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class DescribeSmartVerifyRequest(TeaModel):
    def __init__(
        self,
        scene_id: int = None,
        certify_id: str = None,
        picture_return_type: str = None,
    ):
        self.scene_id = scene_id
        self.certify_id = certify_id
        self.picture_return_type = picture_return_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.picture_return_type is not None:
            result['PictureReturnType'] = self.picture_return_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('PictureReturnType') is not None:
            self.picture_return_type = m.get('PictureReturnType')
        return self


class DescribeSmartVerifyResponseResultObject(TeaModel):
    def __init__(
        self,
        passed: str = None,
        sub_code: str = None,
        material_info: str = None,
        passed_score: float = None,
    ):
        self.passed = passed
        self.sub_code = sub_code
        self.material_info = material_info
        self.passed_score = passed_score

    def validate(self):
        self.validate_required(self.passed, 'passed')
        self.validate_required(self.sub_code, 'sub_code')
        self.validate_required(self.material_info, 'material_info')
        self.validate_required(self.passed_score, 'passed_score')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.passed is not None:
            result['Passed'] = self.passed
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.material_info is not None:
            result['MaterialInfo'] = self.material_info
        if self.passed_score is not None:
            result['PassedScore'] = self.passed_score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('MaterialInfo') is not None:
            self.material_info = m.get('MaterialInfo')
        if m.get('PassedScore') is not None:
            self.passed_score = m.get('PassedScore')
        return self


class DescribeSmartVerifyResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        code: str = None,
        result_object: DescribeSmartVerifyResponseResultObject = None,
    ):
        self.request_id = request_id
        self.message = message
        self.code = code
        self.result_object = result_object

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.message, 'message')
        self.validate_required(self.code, 'code')
        self.validate_required(self.result_object, 'result_object')
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ResultObject') is not None:
            temp_model = DescribeSmartVerifyResponseResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


