# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
try:
    from typing import BinaryIO
except ImportError:
    pass


class ElementSmartVerifyRequest(TeaModel):
    def __init__(self, scene_id=None, outer_order_no=None, mode=None, cert_type=None, cert_name=None, cert_no=None,
                 cert_url=None, cert_file=None):
        self.scene_id = scene_id        # type: int
        self.outer_order_no = outer_order_no  # type: str
        self.mode = mode                # type: str
        self.cert_type = cert_type      # type: str
        self.cert_name = cert_name      # type: str
        self.cert_no = cert_no          # type: str
        self.cert_url = cert_url        # type: str
        self.cert_file = cert_file      # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['SceneId'] = self.scene_id
        result['OuterOrderNo'] = self.outer_order_no
        result['Mode'] = self.mode
        result['CertType'] = self.cert_type
        result['CertName'] = self.cert_name
        result['CertNo'] = self.cert_no
        result['CertUrl'] = self.cert_url
        result['CertFile'] = self.cert_file
        return result

    def from_map(self, map={}):
        self.scene_id = map.get('SceneId')
        self.outer_order_no = map.get('OuterOrderNo')
        self.mode = map.get('Mode')
        self.cert_type = map.get('CertType')
        self.cert_name = map.get('CertName')
        self.cert_no = map.get('CertNo')
        self.cert_url = map.get('CertUrl')
        self.cert_file = map.get('CertFile')
        return self


class ElementSmartVerifyResponse(TeaModel):
    def __init__(self, request_id=None, message=None, code=None, result_object=None):
        self.request_id = request_id    # type: str
        self.message = message          # type: str
        self.code = code                # type: str
        self.result_object = result_object  # type: ElementSmartVerifyResponseResultObject

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.message, 'message')
        self.validate_required(self.code, 'code')
        self.validate_required(self.result_object, 'result_object')
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Message'] = self.message
        result['Code'] = self.code
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        else:
            result['ResultObject'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.message = map.get('Message')
        self.code = map.get('Code')
        if map.get('ResultObject') is not None:
            temp_model = ElementSmartVerifyResponseResultObject()
            self.result_object = temp_model.from_map(map['ResultObject'])
        else:
            self.result_object = None
        return self


class ElementSmartVerifyResponseResultObject(TeaModel):
    def __init__(self, passed=None, sub_code=None, material_info=None):
        self.passed = passed            # type: str
        self.sub_code = sub_code        # type: str
        self.material_info = material_info  # type: str

    def validate(self):
        self.validate_required(self.passed, 'passed')
        self.validate_required(self.sub_code, 'sub_code')
        self.validate_required(self.material_info, 'material_info')

    def to_map(self):
        result = {}
        result['Passed'] = self.passed
        result['SubCode'] = self.sub_code
        result['MaterialInfo'] = self.material_info
        return result

    def from_map(self, map={}):
        self.passed = map.get('Passed')
        self.sub_code = map.get('SubCode')
        self.material_info = map.get('MaterialInfo')
        return self


class ElementSmartVerifyAdvanceRequest(TeaModel):
    def __init__(self, cert_file_object=None, scene_id=None, outer_order_no=None, mode=None, cert_type=None,
                 cert_name=None, cert_no=None, cert_url=None):
        self.cert_file_object = cert_file_object  # type: BinaryIO
        self.scene_id = scene_id        # type: int
        self.outer_order_no = outer_order_no  # type: str
        self.mode = mode                # type: str
        self.cert_type = cert_type      # type: str
        self.cert_name = cert_name      # type: str
        self.cert_no = cert_no          # type: str
        self.cert_url = cert_url        # type: str

    def validate(self):
        self.validate_required(self.cert_file_object, 'cert_file_object')

    def to_map(self):
        result = {}
        result['CertFileObject'] = self.cert_file_object
        result['SceneId'] = self.scene_id
        result['OuterOrderNo'] = self.outer_order_no
        result['Mode'] = self.mode
        result['CertType'] = self.cert_type
        result['CertName'] = self.cert_name
        result['CertNo'] = self.cert_no
        result['CertUrl'] = self.cert_url
        return result

    def from_map(self, map={}):
        self.cert_file_object = map.get('CertFileObject')
        self.scene_id = map.get('SceneId')
        self.outer_order_no = map.get('OuterOrderNo')
        self.mode = map.get('Mode')
        self.cert_type = map.get('CertType')
        self.cert_name = map.get('CertName')
        self.cert_no = map.get('CertNo')
        self.cert_url = map.get('CertUrl')
        return self


class InitSmartVerifyRequest(TeaModel):
    def __init__(self, scene_id=None, outer_order_no=None, mode=None, cert_type=None, meta_info=None, mobile=None,
                 ip=None, user_id=None, cert_name=None, cert_no=None, ocr=None, callback_url=None, callback_token=None,
                 face_picture_base_64=None, face_picture_url=None, certify_id=None, oss_bucket_name=None, oss_object_name=None):
        self.scene_id = scene_id        # type: int
        self.outer_order_no = outer_order_no  # type: str
        self.mode = mode                # type: str
        self.cert_type = cert_type      # type: str
        self.meta_info = meta_info      # type: str
        self.mobile = mobile            # type: str
        self.ip = ip                    # type: str
        self.user_id = user_id          # type: str
        self.cert_name = cert_name      # type: str
        self.cert_no = cert_no          # type: str
        self.ocr = ocr                  # type: str
        self.callback_url = callback_url  # type: str
        self.callback_token = callback_token  # type: str
        self.face_picture_base_64 = face_picture_base_64  # type: str
        self.face_picture_url = face_picture_url  # type: str
        self.certify_id = certify_id    # type: str
        self.oss_bucket_name = oss_bucket_name  # type: str
        self.oss_object_name = oss_object_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['SceneId'] = self.scene_id
        result['OuterOrderNo'] = self.outer_order_no
        result['Mode'] = self.mode
        result['CertType'] = self.cert_type
        result['MetaInfo'] = self.meta_info
        result['Mobile'] = self.mobile
        result['Ip'] = self.ip
        result['UserId'] = self.user_id
        result['CertName'] = self.cert_name
        result['CertNo'] = self.cert_no
        result['Ocr'] = self.ocr
        result['CallbackUrl'] = self.callback_url
        result['CallbackToken'] = self.callback_token
        result['FacePictureBase64'] = self.face_picture_base_64
        result['FacePictureUrl'] = self.face_picture_url
        result['CertifyId'] = self.certify_id
        result['OssBucketName'] = self.oss_bucket_name
        result['OssObjectName'] = self.oss_object_name
        return result

    def from_map(self, map={}):
        self.scene_id = map.get('SceneId')
        self.outer_order_no = map.get('OuterOrderNo')
        self.mode = map.get('Mode')
        self.cert_type = map.get('CertType')
        self.meta_info = map.get('MetaInfo')
        self.mobile = map.get('Mobile')
        self.ip = map.get('Ip')
        self.user_id = map.get('UserId')
        self.cert_name = map.get('CertName')
        self.cert_no = map.get('CertNo')
        self.ocr = map.get('Ocr')
        self.callback_url = map.get('CallbackUrl')
        self.callback_token = map.get('CallbackToken')
        self.face_picture_base_64 = map.get('FacePictureBase64')
        self.face_picture_url = map.get('FacePictureUrl')
        self.certify_id = map.get('CertifyId')
        self.oss_bucket_name = map.get('OssBucketName')
        self.oss_object_name = map.get('OssObjectName')
        return self


class InitSmartVerifyResponse(TeaModel):
    def __init__(self, request_id=None, message=None, code=None, result_object=None):
        self.request_id = request_id    # type: str
        self.message = message          # type: str
        self.code = code                # type: str
        self.result_object = result_object  # type: InitSmartVerifyResponseResultObject

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.message, 'message')
        self.validate_required(self.code, 'code')
        self.validate_required(self.result_object, 'result_object')
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Message'] = self.message
        result['Code'] = self.code
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        else:
            result['ResultObject'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.message = map.get('Message')
        self.code = map.get('Code')
        if map.get('ResultObject') is not None:
            temp_model = InitSmartVerifyResponseResultObject()
            self.result_object = temp_model.from_map(map['ResultObject'])
        else:
            self.result_object = None
        return self


class InitSmartVerifyResponseResultObject(TeaModel):
    def __init__(self, certify_id=None):
        self.certify_id = certify_id    # type: str

    def validate(self):
        self.validate_required(self.certify_id, 'certify_id')

    def to_map(self):
        result = {}
        result['CertifyId'] = self.certify_id
        return result

    def from_map(self, map={}):
        self.certify_id = map.get('CertifyId')
        return self


class DescribeSmartVerifyRequest(TeaModel):
    def __init__(self, scene_id=None, certify_id=None):
        self.scene_id = scene_id        # type: int
        self.certify_id = certify_id    # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['SceneId'] = self.scene_id
        result['CertifyId'] = self.certify_id
        return result

    def from_map(self, map={}):
        self.scene_id = map.get('SceneId')
        self.certify_id = map.get('CertifyId')
        return self


class DescribeSmartVerifyResponse(TeaModel):
    def __init__(self, request_id=None, message=None, code=None, result_object=None):
        self.request_id = request_id    # type: str
        self.message = message          # type: str
        self.code = code                # type: str
        self.result_object = result_object  # type: DescribeSmartVerifyResponseResultObject

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.message, 'message')
        self.validate_required(self.code, 'code')
        self.validate_required(self.result_object, 'result_object')
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Message'] = self.message
        result['Code'] = self.code
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        else:
            result['ResultObject'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.message = map.get('Message')
        self.code = map.get('Code')
        if map.get('ResultObject') is not None:
            temp_model = DescribeSmartVerifyResponseResultObject()
            self.result_object = temp_model.from_map(map['ResultObject'])
        else:
            self.result_object = None
        return self


class DescribeSmartVerifyResponseResultObject(TeaModel):
    def __init__(self, passed=None, sub_code=None, material_info=None, passed_score=None):
        self.passed = passed            # type: str
        self.sub_code = sub_code        # type: str
        self.material_info = material_info  # type: str
        self.passed_score = passed_score  # type: float

    def validate(self):
        self.validate_required(self.passed, 'passed')
        self.validate_required(self.sub_code, 'sub_code')
        self.validate_required(self.material_info, 'material_info')
        self.validate_required(self.passed_score, 'passed_score')

    def to_map(self):
        result = {}
        result['Passed'] = self.passed
        result['SubCode'] = self.sub_code
        result['MaterialInfo'] = self.material_info
        result['PassedScore'] = self.passed_score
        return result

    def from_map(self, map={}):
        self.passed = map.get('Passed')
        self.sub_code = map.get('SubCode')
        self.material_info = map.get('MaterialInfo')
        self.passed_score = map.get('PassedScore')
        return self


