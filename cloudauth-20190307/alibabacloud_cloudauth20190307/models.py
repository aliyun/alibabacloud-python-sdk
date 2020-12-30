# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, BinaryIO, List


class CompareFacesRequest(TeaModel):
    def __init__(
        self,
        target_image_type: str = None,
        source_image_type: str = None,
        source_image_value: str = None,
        target_image_value: str = None,
        biz_type: str = None,
    ):
        self.target_image_type = target_image_type
        self.source_image_type = source_image_type
        self.source_image_value = source_image_value
        self.target_image_value = target_image_value
        self.biz_type = biz_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.target_image_type is not None:
            result['TargetImageType'] = self.target_image_type
        if self.source_image_type is not None:
            result['SourceImageType'] = self.source_image_type
        if self.source_image_value is not None:
            result['SourceImageValue'] = self.source_image_value
        if self.target_image_value is not None:
            result['TargetImageValue'] = self.target_image_value
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TargetImageType') is not None:
            self.target_image_type = m.get('TargetImageType')
        if m.get('SourceImageType') is not None:
            self.source_image_type = m.get('SourceImageType')
        if m.get('SourceImageValue') is not None:
            self.source_image_value = m.get('SourceImageValue')
        if m.get('TargetImageValue') is not None:
            self.target_image_value = m.get('TargetImageValue')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        return self


class CompareFacesResponseBodyData(TeaModel):
    def __init__(
        self,
        similarity_score: float = None,
        confidence_thresholds: str = None,
    ):
        self.similarity_score = similarity_score
        self.confidence_thresholds = confidence_thresholds

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.similarity_score is not None:
            result['SimilarityScore'] = self.similarity_score
        if self.confidence_thresholds is not None:
            result['ConfidenceThresholds'] = self.confidence_thresholds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SimilarityScore') is not None:
            self.similarity_score = m.get('SimilarityScore')
        if m.get('ConfidenceThresholds') is not None:
            self.confidence_thresholds = m.get('ConfidenceThresholds')
        return self


class CompareFacesResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: CompareFacesResponseBodyData = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = CompareFacesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CompareFacesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CompareFacesResponseBody = None,
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
            temp_model = CompareFacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CompareFaceVerifyRequest(TeaModel):
    def __init__(
        self,
        scene_id: int = None,
        outer_order_no: str = None,
        product_code: str = None,
        source_face_contrast_picture: str = None,
        source_face_contrast_picture_url: str = None,
        source_certify_id: str = None,
        source_oss_bucket_name: str = None,
        source_oss_object_name: str = None,
        target_face_contrast_picture: str = None,
        target_face_contrast_picture_url: str = None,
        target_certify_id: str = None,
        target_oss_bucket_name: str = None,
        target_oss_object_name: str = None,
    ):
        self.scene_id = scene_id
        self.outer_order_no = outer_order_no
        self.product_code = product_code
        self.source_face_contrast_picture = source_face_contrast_picture
        self.source_face_contrast_picture_url = source_face_contrast_picture_url
        self.source_certify_id = source_certify_id
        self.source_oss_bucket_name = source_oss_bucket_name
        self.source_oss_object_name = source_oss_object_name
        self.target_face_contrast_picture = target_face_contrast_picture
        self.target_face_contrast_picture_url = target_face_contrast_picture_url
        self.target_certify_id = target_certify_id
        self.target_oss_bucket_name = target_oss_bucket_name
        self.target_oss_object_name = target_oss_object_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.outer_order_no is not None:
            result['OuterOrderNo'] = self.outer_order_no
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.source_face_contrast_picture is not None:
            result['SourceFaceContrastPicture'] = self.source_face_contrast_picture
        if self.source_face_contrast_picture_url is not None:
            result['SourceFaceContrastPictureUrl'] = self.source_face_contrast_picture_url
        if self.source_certify_id is not None:
            result['SourceCertifyId'] = self.source_certify_id
        if self.source_oss_bucket_name is not None:
            result['SourceOssBucketName'] = self.source_oss_bucket_name
        if self.source_oss_object_name is not None:
            result['SourceOssObjectName'] = self.source_oss_object_name
        if self.target_face_contrast_picture is not None:
            result['TargetFaceContrastPicture'] = self.target_face_contrast_picture
        if self.target_face_contrast_picture_url is not None:
            result['TargetFaceContrastPictureUrl'] = self.target_face_contrast_picture_url
        if self.target_certify_id is not None:
            result['TargetCertifyId'] = self.target_certify_id
        if self.target_oss_bucket_name is not None:
            result['TargetOssBucketName'] = self.target_oss_bucket_name
        if self.target_oss_object_name is not None:
            result['TargetOssObjectName'] = self.target_oss_object_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('OuterOrderNo') is not None:
            self.outer_order_no = m.get('OuterOrderNo')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('SourceFaceContrastPicture') is not None:
            self.source_face_contrast_picture = m.get('SourceFaceContrastPicture')
        if m.get('SourceFaceContrastPictureUrl') is not None:
            self.source_face_contrast_picture_url = m.get('SourceFaceContrastPictureUrl')
        if m.get('SourceCertifyId') is not None:
            self.source_certify_id = m.get('SourceCertifyId')
        if m.get('SourceOssBucketName') is not None:
            self.source_oss_bucket_name = m.get('SourceOssBucketName')
        if m.get('SourceOssObjectName') is not None:
            self.source_oss_object_name = m.get('SourceOssObjectName')
        if m.get('TargetFaceContrastPicture') is not None:
            self.target_face_contrast_picture = m.get('TargetFaceContrastPicture')
        if m.get('TargetFaceContrastPictureUrl') is not None:
            self.target_face_contrast_picture_url = m.get('TargetFaceContrastPictureUrl')
        if m.get('TargetCertifyId') is not None:
            self.target_certify_id = m.get('TargetCertifyId')
        if m.get('TargetOssBucketName') is not None:
            self.target_oss_bucket_name = m.get('TargetOssBucketName')
        if m.get('TargetOssObjectName') is not None:
            self.target_oss_object_name = m.get('TargetOssObjectName')
        return self


class CompareFaceVerifyResponseBodyResultObject(TeaModel):
    def __init__(
        self,
        verify_score: float = None,
        passed: str = None,
    ):
        self.verify_score = verify_score
        self.passed = passed

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.verify_score is not None:
            result['VerifyScore'] = self.verify_score
        if self.passed is not None:
            result['Passed'] = self.passed
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VerifyScore') is not None:
            self.verify_score = m.get('VerifyScore')
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
        return self


class CompareFaceVerifyResponseBody(TeaModel):
    def __init__(
        self,
        result_object: CompareFaceVerifyResponseBodyResultObject = None,
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
            temp_model = CompareFaceVerifyResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class CompareFaceVerifyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CompareFaceVerifyResponseBody = None,
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
            temp_model = CompareFaceVerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ContrastFaceVerifyRequest(TeaModel):
    def __init__(
        self,
        scene_id: int = None,
        outer_order_no: str = None,
        product_code: str = None,
        cert_type: str = None,
        cert_name: str = None,
        cert_no: str = None,
        face_contrast_picture: str = None,
        device_token: str = None,
        mobile: str = None,
        ip: str = None,
        user_id: str = None,
        face_contrast_picture_url: str = None,
        certify_id: str = None,
        oss_bucket_name: str = None,
        oss_object_name: str = None,
        model: str = None,
        face_contrast_file: str = None,
    ):
        self.scene_id = scene_id
        self.outer_order_no = outer_order_no
        self.product_code = product_code
        self.cert_type = cert_type
        self.cert_name = cert_name
        self.cert_no = cert_no
        self.face_contrast_picture = face_contrast_picture
        self.device_token = device_token
        self.mobile = mobile
        self.ip = ip
        self.user_id = user_id
        self.face_contrast_picture_url = face_contrast_picture_url
        self.certify_id = certify_id
        self.oss_bucket_name = oss_bucket_name
        self.oss_object_name = oss_object_name
        self.model = model
        self.face_contrast_file = face_contrast_file

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.outer_order_no is not None:
            result['OuterOrderNo'] = self.outer_order_no
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_no is not None:
            result['CertNo'] = self.cert_no
        if self.face_contrast_picture is not None:
            result['FaceContrastPicture'] = self.face_contrast_picture
        if self.device_token is not None:
            result['DeviceToken'] = self.device_token
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.face_contrast_picture_url is not None:
            result['FaceContrastPictureUrl'] = self.face_contrast_picture_url
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name
        if self.oss_object_name is not None:
            result['OssObjectName'] = self.oss_object_name
        if self.model is not None:
            result['Model'] = self.model
        if self.face_contrast_file is not None:
            result['FaceContrastFile'] = self.face_contrast_file
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('OuterOrderNo') is not None:
            self.outer_order_no = m.get('OuterOrderNo')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertNo') is not None:
            self.cert_no = m.get('CertNo')
        if m.get('FaceContrastPicture') is not None:
            self.face_contrast_picture = m.get('FaceContrastPicture')
        if m.get('DeviceToken') is not None:
            self.device_token = m.get('DeviceToken')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('FaceContrastPictureUrl') is not None:
            self.face_contrast_picture_url = m.get('FaceContrastPictureUrl')
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')
        if m.get('OssObjectName') is not None:
            self.oss_object_name = m.get('OssObjectName')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('FaceContrastFile') is not None:
            self.face_contrast_file = m.get('FaceContrastFile')
        return self


class ContrastFaceVerifyAdvanceRequest(TeaModel):
    def __init__(
        self,
        face_contrast_file_object: BinaryIO = None,
        scene_id: int = None,
        outer_order_no: str = None,
        product_code: str = None,
        cert_type: str = None,
        cert_name: str = None,
        cert_no: str = None,
        face_contrast_picture: str = None,
        device_token: str = None,
        mobile: str = None,
        ip: str = None,
        user_id: str = None,
        face_contrast_picture_url: str = None,
        certify_id: str = None,
        oss_bucket_name: str = None,
        oss_object_name: str = None,
        model: str = None,
    ):
        self.face_contrast_file_object = face_contrast_file_object
        self.scene_id = scene_id
        self.outer_order_no = outer_order_no
        self.product_code = product_code
        self.cert_type = cert_type
        self.cert_name = cert_name
        self.cert_no = cert_no
        self.face_contrast_picture = face_contrast_picture
        self.device_token = device_token
        self.mobile = mobile
        self.ip = ip
        self.user_id = user_id
        self.face_contrast_picture_url = face_contrast_picture_url
        self.certify_id = certify_id
        self.oss_bucket_name = oss_bucket_name
        self.oss_object_name = oss_object_name
        self.model = model

    def validate(self):
        self.validate_required(self.face_contrast_file_object, 'face_contrast_file_object')

    def to_map(self):
        result = dict()
        if self.face_contrast_file_object is not None:
            result['FaceContrastFileObject'] = self.face_contrast_file_object
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.outer_order_no is not None:
            result['OuterOrderNo'] = self.outer_order_no
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_no is not None:
            result['CertNo'] = self.cert_no
        if self.face_contrast_picture is not None:
            result['FaceContrastPicture'] = self.face_contrast_picture
        if self.device_token is not None:
            result['DeviceToken'] = self.device_token
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.face_contrast_picture_url is not None:
            result['FaceContrastPictureUrl'] = self.face_contrast_picture_url
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name
        if self.oss_object_name is not None:
            result['OssObjectName'] = self.oss_object_name
        if self.model is not None:
            result['Model'] = self.model
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceContrastFileObject') is not None:
            self.face_contrast_file_object = m.get('FaceContrastFileObject')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('OuterOrderNo') is not None:
            self.outer_order_no = m.get('OuterOrderNo')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertNo') is not None:
            self.cert_no = m.get('CertNo')
        if m.get('FaceContrastPicture') is not None:
            self.face_contrast_picture = m.get('FaceContrastPicture')
        if m.get('DeviceToken') is not None:
            self.device_token = m.get('DeviceToken')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('FaceContrastPictureUrl') is not None:
            self.face_contrast_picture_url = m.get('FaceContrastPictureUrl')
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')
        if m.get('OssObjectName') is not None:
            self.oss_object_name = m.get('OssObjectName')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        return self


class ContrastFaceVerifyResponseBodyResultObject(TeaModel):
    def __init__(
        self,
        material_info: str = None,
        sub_code: str = None,
        identity_info: str = None,
        passed: str = None,
    ):
        self.material_info = material_info
        self.sub_code = sub_code
        self.identity_info = identity_info
        self.passed = passed

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.material_info is not None:
            result['MaterialInfo'] = self.material_info
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.identity_info is not None:
            result['IdentityInfo'] = self.identity_info
        if self.passed is not None:
            result['Passed'] = self.passed
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaterialInfo') is not None:
            self.material_info = m.get('MaterialInfo')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('IdentityInfo') is not None:
            self.identity_info = m.get('IdentityInfo')
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
        return self


class ContrastFaceVerifyResponseBody(TeaModel):
    def __init__(
        self,
        result_object: ContrastFaceVerifyResponseBodyResultObject = None,
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
            temp_model = ContrastFaceVerifyResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ContrastFaceVerifyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ContrastFaceVerifyResponseBody = None,
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
            temp_model = ContrastFaceVerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAuthKeyRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        biz_type: str = None,
        user_device_id: str = None,
        test: bool = None,
        auth_years: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.biz_type = biz_type
        self.user_device_id = user_device_id
        self.test = test
        self.auth_years = auth_years

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.user_device_id is not None:
            result['UserDeviceId'] = self.user_device_id
        if self.test is not None:
            result['Test'] = self.test
        if self.auth_years is not None:
            result['AuthYears'] = self.auth_years
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('UserDeviceId') is not None:
            self.user_device_id = m.get('UserDeviceId')
        if m.get('Test') is not None:
            self.test = m.get('Test')
        if m.get('AuthYears') is not None:
            self.auth_years = m.get('AuthYears')
        return self


class CreateAuthKeyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        auth_key: str = None,
    ):
        self.request_id = request_id
        self.auth_key = auth_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')
        return self


class CreateAuthKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAuthKeyResponseBody = None,
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
            temp_model = CreateAuthKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFaceConfigRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        biz_type: str = None,
        biz_name: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.biz_type = biz_type
        self.biz_name = biz_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        return self


class CreateFaceConfigResponseBody(TeaModel):
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


class CreateFaceConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateFaceConfigResponseBody = None,
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
            temp_model = CreateFaceConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRPSDKRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        app_url: str = None,
        platform: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.app_url = app_url
        self.platform = platform

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.app_url is not None:
            result['AppUrl'] = self.app_url
        if self.platform is not None:
            result['Platform'] = self.platform
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('AppUrl') is not None:
            self.app_url = m.get('AppUrl')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        return self


class CreateRPSDKResponseBody(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        request_id: str = None,
    ):
        self.task_id = task_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateRPSDKResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateRPSDKResponseBody = None,
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
            temp_model = CreateRPSDKResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVerifySDKRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        app_url: str = None,
        platform: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.app_url = app_url
        self.platform = platform

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.app_url is not None:
            result['AppUrl'] = self.app_url
        if self.platform is not None:
            result['Platform'] = self.platform
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('AppUrl') is not None:
            self.app_url = m.get('AppUrl')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        return self


class CreateVerifySDKResponseBody(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        request_id: str = None,
    ):
        self.task_id = task_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateVerifySDKResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateVerifySDKResponseBody = None,
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
            temp_model = CreateVerifySDKResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVerifySettingRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        biz_type: str = None,
        biz_name: str = None,
        solution: str = None,
        guide_step: bool = None,
        privacy_step: bool = None,
        result_step: bool = None,
    ):
        self.source_ip = source_ip
        self.biz_type = biz_type
        self.biz_name = biz_name
        self.solution = solution
        self.guide_step = guide_step
        self.privacy_step = privacy_step
        self.result_step = result_step

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        if self.solution is not None:
            result['Solution'] = self.solution
        if self.guide_step is not None:
            result['GuideStep'] = self.guide_step
        if self.privacy_step is not None:
            result['PrivacyStep'] = self.privacy_step
        if self.result_step is not None:
            result['ResultStep'] = self.result_step
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        if m.get('Solution') is not None:
            self.solution = m.get('Solution')
        if m.get('GuideStep') is not None:
            self.guide_step = m.get('GuideStep')
        if m.get('PrivacyStep') is not None:
            self.privacy_step = m.get('PrivacyStep')
        if m.get('ResultStep') is not None:
            self.result_step = m.get('ResultStep')
        return self


class CreateVerifySettingResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        step_list: List[str] = None,
        biz_name: str = None,
        biz_type: str = None,
        solution: str = None,
    ):
        self.request_id = request_id
        self.step_list = step_list
        self.biz_name = biz_name
        self.biz_type = biz_type
        self.solution = solution

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.step_list is not None:
            result['StepList'] = self.step_list
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.solution is not None:
            result['Solution'] = self.solution
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StepList') is not None:
            self.step_list = m.get('StepList')
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('Solution') is not None:
            self.solution = m.get('Solution')
        return self


class CreateVerifySettingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateVerifySettingResponseBody = None,
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
            temp_model = CreateVerifySettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateWhitelistRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        biz_type: str = None,
        biz_id: str = None,
        id_card_num: str = None,
        valid_day: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.biz_type = biz_type
        self.biz_id = biz_id
        self.id_card_num = id_card_num
        self.valid_day = valid_day

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.id_card_num is not None:
            result['IdCardNum'] = self.id_card_num
        if self.valid_day is not None:
            result['ValidDay'] = self.valid_day
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('IdCardNum') is not None:
            self.id_card_num = m.get('IdCardNum')
        if m.get('ValidDay') is not None:
            self.valid_day = m.get('ValidDay')
        return self


class CreateWhitelistResponseBody(TeaModel):
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


class CreateWhitelistResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateWhitelistResponseBody = None,
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
            temp_model = CreateWhitelistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteWhitelistRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        ids: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.ids = ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.ids is not None:
            result['Ids'] = self.ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        return self


class DeleteWhitelistResponseBody(TeaModel):
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


class DeleteWhitelistResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteWhitelistResponseBody = None,
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
            temp_model = DeleteWhitelistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppInfoRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        page_size: int = None,
        current_page: int = None,
        platform: str = None,
    ):
        self.source_ip = source_ip
        self.page_size = page_size
        self.current_page = current_page
        self.platform = platform

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.platform is not None:
            result['Platform'] = self.platform
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        return self


class DescribeAppInfoResponseBodyAppInfoListDebugPackageInfo(TeaModel):
    def __init__(
        self,
        version: str = None,
    ):
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeAppInfoResponseBodyAppInfoListPackageInfo(TeaModel):
    def __init__(
        self,
        version: str = None,
    ):
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeAppInfoResponseBodyAppInfoList(TeaModel):
    def __init__(
        self,
        type: int = None,
        end_date: str = None,
        package_name: str = None,
        debug_package_info: DescribeAppInfoResponseBodyAppInfoListDebugPackageInfo = None,
        icon: str = None,
        start_date: str = None,
        package_info: DescribeAppInfoResponseBodyAppInfoListPackageInfo = None,
        name: str = None,
        id: int = None,
    ):
        self.type = type
        self.end_date = end_date
        self.package_name = package_name
        self.debug_package_info = debug_package_info
        self.icon = icon
        self.start_date = start_date
        self.package_info = package_info
        self.name = name
        self.id = id

    def validate(self):
        if self.debug_package_info:
            self.debug_package_info.validate()
        if self.package_info:
            self.package_info.validate()

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.package_name is not None:
            result['PackageName'] = self.package_name
        if self.debug_package_info is not None:
            result['DebugPackageInfo'] = self.debug_package_info.to_map()
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.package_info is not None:
            result['PackageInfo'] = self.package_info.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')
        if m.get('DebugPackageInfo') is not None:
            temp_model = DescribeAppInfoResponseBodyAppInfoListDebugPackageInfo()
            self.debug_package_info = temp_model.from_map(m['DebugPackageInfo'])
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('PackageInfo') is not None:
            temp_model = DescribeAppInfoResponseBodyAppInfoListPackageInfo()
            self.package_info = temp_model.from_map(m['PackageInfo'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeAppInfoResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        page_size: int = None,
        current_page: int = None,
        app_info_list: List[DescribeAppInfoResponseBodyAppInfoList] = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.page_size = page_size
        self.current_page = current_page
        self.app_info_list = app_info_list

    def validate(self):
        if self.app_info_list:
            for k in self.app_info_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['AppInfoList'] = []
        if self.app_info_list is not None:
            for k in self.app_info_list:
                result['AppInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.app_info_list = []
        if m.get('AppInfoList') is not None:
            for k in m.get('AppInfoList'):
                temp_model = DescribeAppInfoResponseBodyAppInfoList()
                self.app_info_list.append(temp_model.from_map(k))
        return self


class DescribeAppInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAppInfoResponseBody = None,
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
            temp_model = DescribeAppInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDeviceInfoRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        total_count: int = None,
        page_size: int = None,
        current_page: int = None,
        device_id: str = None,
        biz_type: str = None,
        user_device_id: str = None,
        expired_start_day: str = None,
        expired_end_day: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.total_count = total_count
        self.page_size = page_size
        self.current_page = current_page
        self.device_id = device_id
        self.biz_type = biz_type
        self.user_device_id = user_device_id
        self.expired_start_day = expired_start_day
        self.expired_end_day = expired_end_day

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.user_device_id is not None:
            result['UserDeviceId'] = self.user_device_id
        if self.expired_start_day is not None:
            result['ExpiredStartDay'] = self.expired_start_day
        if self.expired_end_day is not None:
            result['ExpiredEndDay'] = self.expired_end_day
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('UserDeviceId') is not None:
            self.user_device_id = m.get('UserDeviceId')
        if m.get('ExpiredStartDay') is not None:
            self.expired_start_day = m.get('ExpiredStartDay')
        if m.get('ExpiredEndDay') is not None:
            self.expired_end_day = m.get('ExpiredEndDay')
        return self


class DescribeDeviceInfoResponseBodyDeviceInfoListDeviceInfo(TeaModel):
    def __init__(
        self,
        user_device_id: str = None,
        device_id: str = None,
        expired_day: str = None,
        begin_day: str = None,
        biz_type: str = None,
    ):
        self.user_device_id = user_device_id
        self.device_id = device_id
        self.expired_day = expired_day
        self.begin_day = begin_day
        self.biz_type = biz_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_device_id is not None:
            result['UserDeviceId'] = self.user_device_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.expired_day is not None:
            result['ExpiredDay'] = self.expired_day
        if self.begin_day is not None:
            result['BeginDay'] = self.begin_day
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserDeviceId') is not None:
            self.user_device_id = m.get('UserDeviceId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('ExpiredDay') is not None:
            self.expired_day = m.get('ExpiredDay')
        if m.get('BeginDay') is not None:
            self.begin_day = m.get('BeginDay')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        return self


class DescribeDeviceInfoResponseBodyDeviceInfoList(TeaModel):
    def __init__(
        self,
        device_info: List[DescribeDeviceInfoResponseBodyDeviceInfoListDeviceInfo] = None,
    ):
        self.device_info = device_info

    def validate(self):
        if self.device_info:
            for k in self.device_info:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['DeviceInfo'] = []
        if self.device_info is not None:
            for k in self.device_info:
                result['DeviceInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.device_info = []
        if m.get('DeviceInfo') is not None:
            for k in m.get('DeviceInfo'):
                temp_model = DescribeDeviceInfoResponseBodyDeviceInfoListDeviceInfo()
                self.device_info.append(temp_model.from_map(k))
        return self


class DescribeDeviceInfoResponseBody(TeaModel):
    def __init__(
        self,
        device_info_list: DescribeDeviceInfoResponseBodyDeviceInfoList = None,
        total_count: int = None,
        request_id: str = None,
        page_size: int = None,
        current_page: int = None,
    ):
        self.device_info_list = device_info_list
        self.total_count = total_count
        self.request_id = request_id
        self.page_size = page_size
        self.current_page = current_page

    def validate(self):
        if self.device_info_list:
            self.device_info_list.validate()

    def to_map(self):
        result = dict()
        if self.device_info_list is not None:
            result['DeviceInfoList'] = self.device_info_list.to_map()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfoList') is not None:
            temp_model = DescribeDeviceInfoResponseBodyDeviceInfoList()
            self.device_info_list = temp_model.from_map(m['DeviceInfoList'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
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


class DescribeFaceConfigRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeFaceConfigResponseBodyItems(TeaModel):
    def __init__(
        self,
        gmt_updated: int = None,
        biz_name: str = None,
        biz_type: str = None,
    ):
        self.gmt_updated = gmt_updated
        self.biz_name = biz_name
        self.biz_type = biz_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.gmt_updated is not None:
            result['GmtUpdated'] = self.gmt_updated
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtUpdated') is not None:
            self.gmt_updated = m.get('GmtUpdated')
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        return self


class DescribeFaceConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        items: List[DescribeFaceConfigResponseBodyItems] = None,
    ):
        self.request_id = request_id
        self.items = items

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeFaceConfigResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        return self


class DescribeFaceConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeFaceConfigResponseBody = None,
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
            temp_model = DescribeFaceConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFaceUsageRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        start_date: str = None,
        end_date: str = None,
    ):
        self.source_ip = source_ip
        self.start_date = start_date
        self.end_date = end_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        return self


class DescribeFaceUsageResponseBodyFaceUsageList(TeaModel):
    def __init__(
        self,
        date: str = None,
        total_count: int = None,
    ):
        self.date = date
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.date is not None:
            result['Date'] = self.date
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeFaceUsageResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        face_usage_list: List[DescribeFaceUsageResponseBodyFaceUsageList] = None,
        request_id: str = None,
    ):
        self.total_count = total_count
        self.face_usage_list = face_usage_list
        self.request_id = request_id

    def validate(self):
        if self.face_usage_list:
            for k in self.face_usage_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['FaceUsageList'] = []
        if self.face_usage_list is not None:
            for k in self.face_usage_list:
                result['FaceUsageList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.face_usage_list = []
        if m.get('FaceUsageList') is not None:
            for k in m.get('FaceUsageList'):
                temp_model = DescribeFaceUsageResponseBodyFaceUsageList()
                self.face_usage_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeFaceUsageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeFaceUsageResponseBody = None,
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
            temp_model = DescribeFaceUsageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFaceVerifyRequest(TeaModel):
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


class DescribeFaceVerifyResponseBodyResultObject(TeaModel):
    def __init__(
        self,
        material_info: str = None,
        sub_code: str = None,
        identity_info: str = None,
        device_token: str = None,
        passed: str = None,
    ):
        self.material_info = material_info
        self.sub_code = sub_code
        self.identity_info = identity_info
        self.device_token = device_token
        self.passed = passed

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.material_info is not None:
            result['MaterialInfo'] = self.material_info
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.identity_info is not None:
            result['IdentityInfo'] = self.identity_info
        if self.device_token is not None:
            result['DeviceToken'] = self.device_token
        if self.passed is not None:
            result['Passed'] = self.passed
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaterialInfo') is not None:
            self.material_info = m.get('MaterialInfo')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('IdentityInfo') is not None:
            self.identity_info = m.get('IdentityInfo')
        if m.get('DeviceToken') is not None:
            self.device_token = m.get('DeviceToken')
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
        return self


class DescribeFaceVerifyResponseBody(TeaModel):
    def __init__(
        self,
        result_object: DescribeFaceVerifyResponseBodyResultObject = None,
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
            temp_model = DescribeFaceVerifyResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DescribeFaceVerifyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeFaceVerifyResponseBody = None,
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
            temp_model = DescribeFaceVerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOssUploadTokenRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
    ):
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeOssUploadTokenResponseBodyOssUploadToken(TeaModel):
    def __init__(
        self,
        key: str = None,
        token: str = None,
        secret: str = None,
        expired: int = None,
        path: str = None,
        end_point: str = None,
        bucket: str = None,
    ):
        self.key = key
        self.token = token
        self.secret = secret
        self.expired = expired
        self.path = path
        self.end_point = end_point
        self.bucket = bucket

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.token is not None:
            result['Token'] = self.token
        if self.secret is not None:
            result['Secret'] = self.secret
        if self.expired is not None:
            result['Expired'] = self.expired
        if self.path is not None:
            result['Path'] = self.path
        if self.end_point is not None:
            result['EndPoint'] = self.end_point
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('Secret') is not None:
            self.secret = m.get('Secret')
        if m.get('Expired') is not None:
            self.expired = m.get('Expired')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('EndPoint') is not None:
            self.end_point = m.get('EndPoint')
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        return self


class DescribeOssUploadTokenResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        oss_upload_token: DescribeOssUploadTokenResponseBodyOssUploadToken = None,
    ):
        self.request_id = request_id
        self.oss_upload_token = oss_upload_token

    def validate(self):
        if self.oss_upload_token:
            self.oss_upload_token.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.oss_upload_token is not None:
            result['OssUploadToken'] = self.oss_upload_token.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OssUploadToken') is not None:
            temp_model = DescribeOssUploadTokenResponseBodyOssUploadToken()
            self.oss_upload_token = temp_model.from_map(m['OssUploadToken'])
        return self


class DescribeOssUploadTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeOssUploadTokenResponseBody = None,
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
            temp_model = DescribeOssUploadTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRPSDKRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        task_id: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeRPSDKResponseBody(TeaModel):
    def __init__(
        self,
        sdk_url: str = None,
        request_id: str = None,
    ):
        self.sdk_url = sdk_url
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.sdk_url is not None:
            result['SdkUrl'] = self.sdk_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SdkUrl') is not None:
            self.sdk_url = m.get('SdkUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRPSDKResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRPSDKResponseBody = None,
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
            temp_model = DescribeRPSDKResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSdkUrlRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        id: int = None,
        debug: bool = None,
    ):
        self.source_ip = source_ip
        self.id = id
        self.debug = debug

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.id is not None:
            result['Id'] = self.id
        if self.debug is not None:
            result['Debug'] = self.debug
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Debug') is not None:
            self.debug = m.get('Debug')
        return self


class DescribeSdkUrlResponseBody(TeaModel):
    def __init__(
        self,
        sdk_url: str = None,
        request_id: str = None,
    ):
        self.sdk_url = sdk_url
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.sdk_url is not None:
            result['SdkUrl'] = self.sdk_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SdkUrl') is not None:
            self.sdk_url = m.get('SdkUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeSdkUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSdkUrlResponseBody = None,
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
            temp_model = DescribeSdkUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUpdatePackageResultRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        task_id: str = None,
    ):
        self.source_ip = source_ip
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeUpdatePackageResultResponseBodyAppInfoDebugPackageInfo(TeaModel):
    def __init__(
        self,
        version: str = None,
    ):
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeUpdatePackageResultResponseBodyAppInfoPackageInfo(TeaModel):
    def __init__(
        self,
        version: str = None,
    ):
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeUpdatePackageResultResponseBodyAppInfo(TeaModel):
    def __init__(
        self,
        type: int = None,
        end_date: str = None,
        package_name: str = None,
        debug_package_info: DescribeUpdatePackageResultResponseBodyAppInfoDebugPackageInfo = None,
        icon: str = None,
        start_date: str = None,
        package_info: DescribeUpdatePackageResultResponseBodyAppInfoPackageInfo = None,
        name: str = None,
        id: int = None,
    ):
        self.type = type
        self.end_date = end_date
        self.package_name = package_name
        self.debug_package_info = debug_package_info
        self.icon = icon
        self.start_date = start_date
        self.package_info = package_info
        self.name = name
        self.id = id

    def validate(self):
        if self.debug_package_info:
            self.debug_package_info.validate()
        if self.package_info:
            self.package_info.validate()

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.package_name is not None:
            result['PackageName'] = self.package_name
        if self.debug_package_info is not None:
            result['DebugPackageInfo'] = self.debug_package_info.to_map()
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.package_info is not None:
            result['PackageInfo'] = self.package_info.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')
        if m.get('DebugPackageInfo') is not None:
            temp_model = DescribeUpdatePackageResultResponseBodyAppInfoDebugPackageInfo()
            self.debug_package_info = temp_model.from_map(m['DebugPackageInfo'])
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('PackageInfo') is not None:
            temp_model = DescribeUpdatePackageResultResponseBodyAppInfoPackageInfo()
            self.package_info = temp_model.from_map(m['PackageInfo'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeUpdatePackageResultResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        app_info: DescribeUpdatePackageResultResponseBodyAppInfo = None,
    ):
        self.request_id = request_id
        self.app_info = app_info

    def validate(self):
        if self.app_info:
            self.app_info.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.app_info is not None:
            result['AppInfo'] = self.app_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AppInfo') is not None:
            temp_model = DescribeUpdatePackageResultResponseBodyAppInfo()
            self.app_info = temp_model.from_map(m['AppInfo'])
        return self


class DescribeUpdatePackageResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeUpdatePackageResultResponseBody = None,
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
            temp_model = DescribeUpdatePackageResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUploadInfoRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        biz: str = None,
    ):
        self.source_ip = source_ip
        self.biz = biz

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.biz is not None:
            result['Biz'] = self.biz
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Biz') is not None:
            self.biz = m.get('Biz')
        return self


class DescribeUploadInfoResponseBody(TeaModel):
    def __init__(
        self,
        policy: str = None,
        expire: int = None,
        request_id: str = None,
        accessid: str = None,
        signature: str = None,
        host: str = None,
        folder: str = None,
    ):
        self.policy = policy
        self.expire = expire
        self.request_id = request_id
        self.accessid = accessid
        self.signature = signature
        self.host = host
        self.folder = folder

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.accessid is not None:
            result['Accessid'] = self.accessid
        if self.signature is not None:
            result['Signature'] = self.signature
        if self.host is not None:
            result['Host'] = self.host
        if self.folder is not None:
            result['Folder'] = self.folder
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Accessid') is not None:
            self.accessid = m.get('Accessid')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Folder') is not None:
            self.folder = m.get('Folder')
        return self


class DescribeUploadInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeUploadInfoResponseBody = None,
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
            temp_model = DescribeUploadInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserStatusRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
    ):
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeUserStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        enabled: bool = None,
    ):
        self.request_id = request_id
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        return self


class DescribeUserStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeUserStatusResponseBody = None,
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
            temp_model = DescribeUserStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVerifyRecordsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        total_count: int = None,
        page_size: int = None,
        current_page: int = None,
        biz_type: str = None,
        start_date: str = None,
        end_date: str = None,
        biz_id: str = None,
        id_card_num: str = None,
        status_list: str = None,
        query_id: str = None,
    ):
        self.source_ip = source_ip
        self.total_count = total_count
        self.page_size = page_size
        self.current_page = current_page
        self.biz_type = biz_type
        self.start_date = start_date
        self.end_date = end_date
        self.biz_id = biz_id
        self.id_card_num = id_card_num
        self.status_list = status_list
        self.query_id = query_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.id_card_num is not None:
            result['IdCardNum'] = self.id_card_num
        if self.status_list is not None:
            result['StatusList'] = self.status_list
        if self.query_id is not None:
            result['QueryId'] = self.query_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('IdCardNum') is not None:
            self.id_card_num = m.get('IdCardNum')
        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')
        if m.get('QueryId') is not None:
            self.query_id = m.get('QueryId')
        return self


class DescribeVerifyRecordsResponseBodyRecordsListMaterialIdCardInfo(TeaModel):
    def __init__(
        self,
        end_date: str = None,
        sex: str = None,
        authority: str = None,
        address: str = None,
        number: str = None,
        start_date: str = None,
        nationality: str = None,
        back_image_url: str = None,
        birth: str = None,
        name: str = None,
        front_image_url: str = None,
    ):
        self.end_date = end_date
        self.sex = sex
        self.authority = authority
        self.address = address
        self.number = number
        self.start_date = start_date
        self.nationality = nationality
        self.back_image_url = back_image_url
        self.birth = birth
        self.name = name
        self.front_image_url = front_image_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.sex is not None:
            result['Sex'] = self.sex
        if self.authority is not None:
            result['Authority'] = self.authority
        if self.address is not None:
            result['Address'] = self.address
        if self.number is not None:
            result['Number'] = self.number
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.nationality is not None:
            result['Nationality'] = self.nationality
        if self.back_image_url is not None:
            result['BackImageUrl'] = self.back_image_url
        if self.birth is not None:
            result['Birth'] = self.birth
        if self.name is not None:
            result['Name'] = self.name
        if self.front_image_url is not None:
            result['FrontImageUrl'] = self.front_image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Sex') is not None:
            self.sex = m.get('Sex')
        if m.get('Authority') is not None:
            self.authority = m.get('Authority')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Nationality') is not None:
            self.nationality = m.get('Nationality')
        if m.get('BackImageUrl') is not None:
            self.back_image_url = m.get('BackImageUrl')
        if m.get('Birth') is not None:
            self.birth = m.get('Birth')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('FrontImageUrl') is not None:
            self.front_image_url = m.get('FrontImageUrl')
        return self


class DescribeVerifyRecordsResponseBodyRecordsListMaterial(TeaModel):
    def __init__(
        self,
        id_card_number: str = None,
        face_image_url: str = None,
        id_card_name: str = None,
        id_card_info: DescribeVerifyRecordsResponseBodyRecordsListMaterialIdCardInfo = None,
    ):
        self.id_card_number = id_card_number
        self.face_image_url = face_image_url
        self.id_card_name = id_card_name
        self.id_card_info = id_card_info

    def validate(self):
        if self.id_card_info:
            self.id_card_info.validate()

    def to_map(self):
        result = dict()
        if self.id_card_number is not None:
            result['IdCardNumber'] = self.id_card_number
        if self.face_image_url is not None:
            result['FaceImageUrl'] = self.face_image_url
        if self.id_card_name is not None:
            result['IdCardName'] = self.id_card_name
        if self.id_card_info is not None:
            result['IdCardInfo'] = self.id_card_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdCardNumber') is not None:
            self.id_card_number = m.get('IdCardNumber')
        if m.get('FaceImageUrl') is not None:
            self.face_image_url = m.get('FaceImageUrl')
        if m.get('IdCardName') is not None:
            self.id_card_name = m.get('IdCardName')
        if m.get('IdCardInfo') is not None:
            temp_model = DescribeVerifyRecordsResponseBodyRecordsListMaterialIdCardInfo()
            self.id_card_info = temp_model.from_map(m['IdCardInfo'])
        return self


class DescribeVerifyRecordsResponseBodyRecordsList(TeaModel):
    def __init__(
        self,
        status: int = None,
        finish_time: int = None,
        material: DescribeVerifyRecordsResponseBodyRecordsListMaterial = None,
        id_card_face_comparison_score: float = None,
        biz_id: str = None,
        verify_id: str = None,
        authority_comparison_score: float = None,
        data_stats: str = None,
        biz_type: str = None,
    ):
        self.status = status
        self.finish_time = finish_time
        self.material = material
        self.id_card_face_comparison_score = id_card_face_comparison_score
        self.biz_id = biz_id
        self.verify_id = verify_id
        self.authority_comparison_score = authority_comparison_score
        self.data_stats = data_stats
        self.biz_type = biz_type

    def validate(self):
        if self.material:
            self.material.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.material is not None:
            result['Material'] = self.material.to_map()
        if self.id_card_face_comparison_score is not None:
            result['IdCardFaceComparisonScore'] = self.id_card_face_comparison_score
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.verify_id is not None:
            result['VerifyId'] = self.verify_id
        if self.authority_comparison_score is not None:
            result['AuthorityComparisonScore'] = self.authority_comparison_score
        if self.data_stats is not None:
            result['DataStats'] = self.data_stats
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('Material') is not None:
            temp_model = DescribeVerifyRecordsResponseBodyRecordsListMaterial()
            self.material = temp_model.from_map(m['Material'])
        if m.get('IdCardFaceComparisonScore') is not None:
            self.id_card_face_comparison_score = m.get('IdCardFaceComparisonScore')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('VerifyId') is not None:
            self.verify_id = m.get('VerifyId')
        if m.get('AuthorityComparisonScore') is not None:
            self.authority_comparison_score = m.get('AuthorityComparisonScore')
        if m.get('DataStats') is not None:
            self.data_stats = m.get('DataStats')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        return self


class DescribeVerifyRecordsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        current_page: int = None,
        query_id: str = None,
        records_list: List[DescribeVerifyRecordsResponseBodyRecordsList] = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.current_page = current_page
        self.query_id = query_id
        self.records_list = records_list

    def validate(self):
        if self.records_list:
            for k in self.records_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.query_id is not None:
            result['QueryId'] = self.query_id
        result['RecordsList'] = []
        if self.records_list is not None:
            for k in self.records_list:
                result['RecordsList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('QueryId') is not None:
            self.query_id = m.get('QueryId')
        self.records_list = []
        if m.get('RecordsList') is not None:
            for k in m.get('RecordsList'):
                temp_model = DescribeVerifyRecordsResponseBodyRecordsList()
                self.records_list.append(temp_model.from_map(k))
        return self


class DescribeVerifyRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVerifyRecordsResponseBody = None,
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
            temp_model = DescribeVerifyRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVerifyResultRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_type: str = None,
    ):
        self.biz_id = biz_id
        self.biz_type = biz_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        return self


class DescribeVerifyResultResponseBodyMaterialIdCardInfo(TeaModel):
    def __init__(
        self,
        end_date: str = None,
        authority: str = None,
        address: str = None,
        number: str = None,
        start_date: str = None,
        back_image_url: str = None,
        nationality: str = None,
        birth: str = None,
        name: str = None,
        front_image_url: str = None,
    ):
        self.end_date = end_date
        self.authority = authority
        self.address = address
        self.number = number
        self.start_date = start_date
        self.back_image_url = back_image_url
        self.nationality = nationality
        self.birth = birth
        self.name = name
        self.front_image_url = front_image_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.authority is not None:
            result['Authority'] = self.authority
        if self.address is not None:
            result['Address'] = self.address
        if self.number is not None:
            result['Number'] = self.number
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.back_image_url is not None:
            result['BackImageUrl'] = self.back_image_url
        if self.nationality is not None:
            result['Nationality'] = self.nationality
        if self.birth is not None:
            result['Birth'] = self.birth
        if self.name is not None:
            result['Name'] = self.name
        if self.front_image_url is not None:
            result['FrontImageUrl'] = self.front_image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Authority') is not None:
            self.authority = m.get('Authority')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('BackImageUrl') is not None:
            self.back_image_url = m.get('BackImageUrl')
        if m.get('Nationality') is not None:
            self.nationality = m.get('Nationality')
        if m.get('Birth') is not None:
            self.birth = m.get('Birth')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('FrontImageUrl') is not None:
            self.front_image_url = m.get('FrontImageUrl')
        return self


class DescribeVerifyResultResponseBodyMaterial(TeaModel):
    def __init__(
        self,
        id_card_number: str = None,
        face_global_url: str = None,
        face_image_url: str = None,
        face_mask: bool = None,
        id_card_name: str = None,
        video_urls: List[str] = None,
        id_card_info: DescribeVerifyResultResponseBodyMaterialIdCardInfo = None,
        face_quality: str = None,
    ):
        self.id_card_number = id_card_number
        self.face_global_url = face_global_url
        self.face_image_url = face_image_url
        self.face_mask = face_mask
        self.id_card_name = id_card_name
        self.video_urls = video_urls
        self.id_card_info = id_card_info
        self.face_quality = face_quality

    def validate(self):
        if self.id_card_info:
            self.id_card_info.validate()

    def to_map(self):
        result = dict()
        if self.id_card_number is not None:
            result['IdCardNumber'] = self.id_card_number
        if self.face_global_url is not None:
            result['FaceGlobalUrl'] = self.face_global_url
        if self.face_image_url is not None:
            result['FaceImageUrl'] = self.face_image_url
        if self.face_mask is not None:
            result['FaceMask'] = self.face_mask
        if self.id_card_name is not None:
            result['IdCardName'] = self.id_card_name
        if self.video_urls is not None:
            result['VideoUrls'] = self.video_urls
        if self.id_card_info is not None:
            result['IdCardInfo'] = self.id_card_info.to_map()
        if self.face_quality is not None:
            result['FaceQuality'] = self.face_quality
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdCardNumber') is not None:
            self.id_card_number = m.get('IdCardNumber')
        if m.get('FaceGlobalUrl') is not None:
            self.face_global_url = m.get('FaceGlobalUrl')
        if m.get('FaceImageUrl') is not None:
            self.face_image_url = m.get('FaceImageUrl')
        if m.get('FaceMask') is not None:
            self.face_mask = m.get('FaceMask')
        if m.get('IdCardName') is not None:
            self.id_card_name = m.get('IdCardName')
        if m.get('VideoUrls') is not None:
            self.video_urls = m.get('VideoUrls')
        if m.get('IdCardInfo') is not None:
            temp_model = DescribeVerifyResultResponseBodyMaterialIdCardInfo()
            self.id_card_info = temp_model.from_map(m['IdCardInfo'])
        if m.get('FaceQuality') is not None:
            self.face_quality = m.get('FaceQuality')
        return self


class DescribeVerifyResultResponseBody(TeaModel):
    def __init__(
        self,
        verify_status: int = None,
        request_id: str = None,
        material: DescribeVerifyResultResponseBodyMaterial = None,
        authority_comparision_score: float = None,
        face_comparison_score: float = None,
        id_card_face_comparison_score: float = None,
    ):
        self.verify_status = verify_status
        self.request_id = request_id
        self.material = material
        self.authority_comparision_score = authority_comparision_score
        self.face_comparison_score = face_comparison_score
        self.id_card_face_comparison_score = id_card_face_comparison_score

    def validate(self):
        if self.material:
            self.material.validate()

    def to_map(self):
        result = dict()
        if self.verify_status is not None:
            result['VerifyStatus'] = self.verify_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.material is not None:
            result['Material'] = self.material.to_map()
        if self.authority_comparision_score is not None:
            result['AuthorityComparisionScore'] = self.authority_comparision_score
        if self.face_comparison_score is not None:
            result['FaceComparisonScore'] = self.face_comparison_score
        if self.id_card_face_comparison_score is not None:
            result['IdCardFaceComparisonScore'] = self.id_card_face_comparison_score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VerifyStatus') is not None:
            self.verify_status = m.get('VerifyStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Material') is not None:
            temp_model = DescribeVerifyResultResponseBodyMaterial()
            self.material = temp_model.from_map(m['Material'])
        if m.get('AuthorityComparisionScore') is not None:
            self.authority_comparision_score = m.get('AuthorityComparisionScore')
        if m.get('FaceComparisonScore') is not None:
            self.face_comparison_score = m.get('FaceComparisonScore')
        if m.get('IdCardFaceComparisonScore') is not None:
            self.id_card_face_comparison_score = m.get('IdCardFaceComparisonScore')
        return self


class DescribeVerifyResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVerifyResultResponseBody = None,
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
            temp_model = DescribeVerifyResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVerifySDKRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        task_id: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeVerifySDKResponseBody(TeaModel):
    def __init__(
        self,
        sdk_url: str = None,
        request_id: str = None,
    ):
        self.sdk_url = sdk_url
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.sdk_url is not None:
            result['SdkUrl'] = self.sdk_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SdkUrl') is not None:
            self.sdk_url = m.get('SdkUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeVerifySDKResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVerifySDKResponseBody = None,
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
            temp_model = DescribeVerifySDKResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVerifySettingRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
    ):
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeVerifySettingResponseBodyVerifySettingList(TeaModel):
    def __init__(
        self,
        step_list: List[str] = None,
        biz_name: str = None,
        solution: str = None,
        biz_type: str = None,
    ):
        self.step_list = step_list
        self.biz_name = biz_name
        self.solution = solution
        self.biz_type = biz_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.step_list is not None:
            result['StepList'] = self.step_list
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        if self.solution is not None:
            result['Solution'] = self.solution
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StepList') is not None:
            self.step_list = m.get('StepList')
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        if m.get('Solution') is not None:
            self.solution = m.get('Solution')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        return self


class DescribeVerifySettingResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        verify_setting_list: List[DescribeVerifySettingResponseBodyVerifySettingList] = None,
    ):
        self.request_id = request_id
        self.verify_setting_list = verify_setting_list

    def validate(self):
        if self.verify_setting_list:
            for k in self.verify_setting_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['VerifySettingList'] = []
        if self.verify_setting_list is not None:
            for k in self.verify_setting_list:
                result['VerifySettingList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.verify_setting_list = []
        if m.get('VerifySettingList') is not None:
            for k in m.get('VerifySettingList'):
                temp_model = DescribeVerifySettingResponseBodyVerifySettingList()
                self.verify_setting_list.append(temp_model.from_map(k))
        return self


class DescribeVerifySettingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVerifySettingResponseBody = None,
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
            temp_model = DescribeVerifySettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVerifyTokenRequest(TeaModel):
    def __init__(
        self,
        id_card_back_image_url: str = None,
        biz_type: str = None,
        failed_redirect_url: str = None,
        face_retained_image_url: str = None,
        callback_seed: str = None,
        id_card_front_image_url: str = None,
        user_id: str = None,
        biz_id: str = None,
        name: str = None,
        id_card_number: str = None,
        passed_redirect_url: str = None,
        callback_url: str = None,
        user_ip: str = None,
        user_phone_number: str = None,
        user_regist_time: int = None,
    ):
        self.id_card_back_image_url = id_card_back_image_url
        self.biz_type = biz_type
        self.failed_redirect_url = failed_redirect_url
        self.face_retained_image_url = face_retained_image_url
        self.callback_seed = callback_seed
        self.id_card_front_image_url = id_card_front_image_url
        self.user_id = user_id
        self.biz_id = biz_id
        self.name = name
        self.id_card_number = id_card_number
        self.passed_redirect_url = passed_redirect_url
        self.callback_url = callback_url
        self.user_ip = user_ip
        self.user_phone_number = user_phone_number
        self.user_regist_time = user_regist_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.id_card_back_image_url is not None:
            result['IdCardBackImageUrl'] = self.id_card_back_image_url
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.failed_redirect_url is not None:
            result['FailedRedirectUrl'] = self.failed_redirect_url
        if self.face_retained_image_url is not None:
            result['FaceRetainedImageUrl'] = self.face_retained_image_url
        if self.callback_seed is not None:
            result['CallbackSeed'] = self.callback_seed
        if self.id_card_front_image_url is not None:
            result['IdCardFrontImageUrl'] = self.id_card_front_image_url
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.name is not None:
            result['Name'] = self.name
        if self.id_card_number is not None:
            result['IdCardNumber'] = self.id_card_number
        if self.passed_redirect_url is not None:
            result['PassedRedirectUrl'] = self.passed_redirect_url
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        if self.user_ip is not None:
            result['UserIp'] = self.user_ip
        if self.user_phone_number is not None:
            result['UserPhoneNumber'] = self.user_phone_number
        if self.user_regist_time is not None:
            result['UserRegistTime'] = self.user_regist_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdCardBackImageUrl') is not None:
            self.id_card_back_image_url = m.get('IdCardBackImageUrl')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('FailedRedirectUrl') is not None:
            self.failed_redirect_url = m.get('FailedRedirectUrl')
        if m.get('FaceRetainedImageUrl') is not None:
            self.face_retained_image_url = m.get('FaceRetainedImageUrl')
        if m.get('CallbackSeed') is not None:
            self.callback_seed = m.get('CallbackSeed')
        if m.get('IdCardFrontImageUrl') is not None:
            self.id_card_front_image_url = m.get('IdCardFrontImageUrl')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('IdCardNumber') is not None:
            self.id_card_number = m.get('IdCardNumber')
        if m.get('PassedRedirectUrl') is not None:
            self.passed_redirect_url = m.get('PassedRedirectUrl')
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        if m.get('UserIp') is not None:
            self.user_ip = m.get('UserIp')
        if m.get('UserPhoneNumber') is not None:
            self.user_phone_number = m.get('UserPhoneNumber')
        if m.get('UserRegistTime') is not None:
            self.user_regist_time = m.get('UserRegistTime')
        return self


class DescribeVerifyTokenResponseBodyOssUploadToken(TeaModel):
    def __init__(
        self,
        key: str = None,
        token: str = None,
        secret: str = None,
        expired: int = None,
        path: str = None,
        end_point: str = None,
        bucket: str = None,
    ):
        self.key = key
        self.token = token
        self.secret = secret
        self.expired = expired
        self.path = path
        self.end_point = end_point
        self.bucket = bucket

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.token is not None:
            result['Token'] = self.token
        if self.secret is not None:
            result['Secret'] = self.secret
        if self.expired is not None:
            result['Expired'] = self.expired
        if self.path is not None:
            result['Path'] = self.path
        if self.end_point is not None:
            result['EndPoint'] = self.end_point
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('Secret') is not None:
            self.secret = m.get('Secret')
        if m.get('Expired') is not None:
            self.expired = m.get('Expired')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('EndPoint') is not None:
            self.end_point = m.get('EndPoint')
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        return self


class DescribeVerifyTokenResponseBody(TeaModel):
    def __init__(
        self,
        verify_page_url: str = None,
        request_id: str = None,
        oss_upload_token: DescribeVerifyTokenResponseBodyOssUploadToken = None,
        verify_token: str = None,
    ):
        self.verify_page_url = verify_page_url
        self.request_id = request_id
        self.oss_upload_token = oss_upload_token
        self.verify_token = verify_token

    def validate(self):
        if self.oss_upload_token:
            self.oss_upload_token.validate()

    def to_map(self):
        result = dict()
        if self.verify_page_url is not None:
            result['VerifyPageUrl'] = self.verify_page_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.oss_upload_token is not None:
            result['OssUploadToken'] = self.oss_upload_token.to_map()
        if self.verify_token is not None:
            result['VerifyToken'] = self.verify_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VerifyPageUrl') is not None:
            self.verify_page_url = m.get('VerifyPageUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OssUploadToken') is not None:
            temp_model = DescribeVerifyTokenResponseBodyOssUploadToken()
            self.oss_upload_token = temp_model.from_map(m['OssUploadToken'])
        if m.get('VerifyToken') is not None:
            self.verify_token = m.get('VerifyToken')
        return self


class DescribeVerifyTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVerifyTokenResponseBody = None,
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
            temp_model = DescribeVerifyTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVerifyUsageRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        biz_type: str = None,
        start_date: str = None,
        end_date: str = None,
    ):
        self.source_ip = source_ip
        self.biz_type = biz_type
        self.start_date = start_date
        self.end_date = end_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        return self


class DescribeVerifyUsageResponseBodyVerifyUsageList(TeaModel):
    def __init__(
        self,
        pass_count: int = None,
        fail_count: int = None,
        date: str = None,
        total_count: int = None,
        biz_type: str = None,
    ):
        self.pass_count = pass_count
        self.fail_count = fail_count
        self.date = date
        self.total_count = total_count
        self.biz_type = biz_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.pass_count is not None:
            result['PassCount'] = self.pass_count
        if self.fail_count is not None:
            result['FailCount'] = self.fail_count
        if self.date is not None:
            result['Date'] = self.date
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PassCount') is not None:
            self.pass_count = m.get('PassCount')
        if m.get('FailCount') is not None:
            self.fail_count = m.get('FailCount')
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        return self


class DescribeVerifyUsageResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        verify_usage_list: List[DescribeVerifyUsageResponseBodyVerifyUsageList] = None,
        request_id: str = None,
    ):
        self.total_count = total_count
        self.verify_usage_list = verify_usage_list
        self.request_id = request_id

    def validate(self):
        if self.verify_usage_list:
            for k in self.verify_usage_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['VerifyUsageList'] = []
        if self.verify_usage_list is not None:
            for k in self.verify_usage_list:
                result['VerifyUsageList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.verify_usage_list = []
        if m.get('VerifyUsageList') is not None:
            for k in m.get('VerifyUsageList'):
                temp_model = DescribeVerifyUsageResponseBodyVerifyUsageList()
                self.verify_usage_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeVerifyUsageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVerifyUsageResponseBody = None,
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
            temp_model = DescribeVerifyUsageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWhitelistRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        biz_type: str = None,
        biz_id: str = None,
        id_card_num: str = None,
        valid_start_date: str = None,
        valid_end_date: str = None,
        valid: str = None,
        page_size: int = None,
        current_page: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.biz_type = biz_type
        self.biz_id = biz_id
        self.id_card_num = id_card_num
        self.valid_start_date = valid_start_date
        self.valid_end_date = valid_end_date
        self.valid = valid
        self.page_size = page_size
        self.current_page = current_page

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.id_card_num is not None:
            result['IdCardNum'] = self.id_card_num
        if self.valid_start_date is not None:
            result['ValidStartDate'] = self.valid_start_date
        if self.valid_end_date is not None:
            result['ValidEndDate'] = self.valid_end_date
        if self.valid is not None:
            result['Valid'] = self.valid
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('IdCardNum') is not None:
            self.id_card_num = m.get('IdCardNum')
        if m.get('ValidStartDate') is not None:
            self.valid_start_date = m.get('ValidStartDate')
        if m.get('ValidEndDate') is not None:
            self.valid_end_date = m.get('ValidEndDate')
        if m.get('Valid') is not None:
            self.valid = m.get('Valid')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        return self


class DescribeWhitelistResponseBodyItems(TeaModel):
    def __init__(
        self,
        end_date: int = None,
        gmt_create: int = None,
        biz_id: str = None,
        start_date: int = None,
        id_card_num: str = None,
        gmt_modified: int = None,
        valid: int = None,
        id: int = None,
        biz_type: str = None,
        uid: int = None,
    ):
        self.end_date = end_date
        self.gmt_create = gmt_create
        self.biz_id = biz_id
        self.start_date = start_date
        self.id_card_num = id_card_num
        self.gmt_modified = gmt_modified
        self.valid = valid
        self.id = id
        self.biz_type = biz_type
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.id_card_num is not None:
            result['IdCardNum'] = self.id_card_num
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.valid is not None:
            result['Valid'] = self.valid
        if self.id is not None:
            result['Id'] = self.id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('IdCardNum') is not None:
            self.id_card_num = m.get('IdCardNum')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Valid') is not None:
            self.valid = m.get('Valid')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class DescribeWhitelistResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        current_page: int = None,
        items: List[DescribeWhitelistResponseBodyItems] = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.current_page = current_page
        self.items = items

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeWhitelistResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        return self


class DescribeWhitelistResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeWhitelistResponseBody = None,
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
            temp_model = DescribeWhitelistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectFaceAttributesRequest(TeaModel):
    def __init__(
        self,
        material_value: str = None,
        biz_type: str = None,
    ):
        self.material_value = material_value
        self.biz_type = biz_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.material_value is not None:
            result['MaterialValue'] = self.material_value
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaterialValue') is not None:
            self.material_value = m.get('MaterialValue')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        return self


class DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceAttributesSmiling(TeaModel):
    def __init__(
        self,
        value: float = None,
        threshold: float = None,
    ):
        self.value = value
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        return self


class DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceAttributesHeadpose(TeaModel):
    def __init__(
        self,
        pitch_angle: float = None,
        roll_angle: float = None,
        yaw_angle: float = None,
    ):
        self.pitch_angle = pitch_angle
        self.roll_angle = roll_angle
        self.yaw_angle = yaw_angle

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.pitch_angle is not None:
            result['PitchAngle'] = self.pitch_angle
        if self.roll_angle is not None:
            result['RollAngle'] = self.roll_angle
        if self.yaw_angle is not None:
            result['YawAngle'] = self.yaw_angle
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PitchAngle') is not None:
            self.pitch_angle = m.get('PitchAngle')
        if m.get('RollAngle') is not None:
            self.roll_angle = m.get('RollAngle')
        if m.get('YawAngle') is not None:
            self.yaw_angle = m.get('YawAngle')
        return self


class DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceAttributes(TeaModel):
    def __init__(
        self,
        glasses: str = None,
        facequal: float = None,
        integrity: int = None,
        smiling: DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceAttributesSmiling = None,
        facetype: str = None,
        respirator: str = None,
        headpose: DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceAttributesHeadpose = None,
        blur: float = None,
    ):
        self.glasses = glasses
        self.facequal = facequal
        self.integrity = integrity
        self.smiling = smiling
        self.facetype = facetype
        self.respirator = respirator
        self.headpose = headpose
        self.blur = blur

    def validate(self):
        if self.smiling:
            self.smiling.validate()
        if self.headpose:
            self.headpose.validate()

    def to_map(self):
        result = dict()
        if self.glasses is not None:
            result['Glasses'] = self.glasses
        if self.facequal is not None:
            result['Facequal'] = self.facequal
        if self.integrity is not None:
            result['Integrity'] = self.integrity
        if self.smiling is not None:
            result['Smiling'] = self.smiling.to_map()
        if self.facetype is not None:
            result['Facetype'] = self.facetype
        if self.respirator is not None:
            result['Respirator'] = self.respirator
        if self.headpose is not None:
            result['Headpose'] = self.headpose.to_map()
        if self.blur is not None:
            result['Blur'] = self.blur
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Glasses') is not None:
            self.glasses = m.get('Glasses')
        if m.get('Facequal') is not None:
            self.facequal = m.get('Facequal')
        if m.get('Integrity') is not None:
            self.integrity = m.get('Integrity')
        if m.get('Smiling') is not None:
            temp_model = DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceAttributesSmiling()
            self.smiling = temp_model.from_map(m['Smiling'])
        if m.get('Facetype') is not None:
            self.facetype = m.get('Facetype')
        if m.get('Respirator') is not None:
            self.respirator = m.get('Respirator')
        if m.get('Headpose') is not None:
            temp_model = DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceAttributesHeadpose()
            self.headpose = temp_model.from_map(m['Headpose'])
        if m.get('Blur') is not None:
            self.blur = m.get('Blur')
        return self


class DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceRect(TeaModel):
    def __init__(
        self,
        top: int = None,
        width: int = None,
        height: int = None,
        left: int = None,
    ):
        self.top = top
        self.width = width
        self.height = height
        self.left = left

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.left is not None:
            result['Left'] = self.left
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Left') is not None:
            self.left = m.get('Left')
        return self


class DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfo(TeaModel):
    def __init__(
        self,
        face_attributes: DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceAttributes = None,
        face_rect: DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceRect = None,
    ):
        self.face_attributes = face_attributes
        self.face_rect = face_rect

    def validate(self):
        if self.face_attributes:
            self.face_attributes.validate()
        if self.face_rect:
            self.face_rect.validate()

    def to_map(self):
        result = dict()
        if self.face_attributes is not None:
            result['FaceAttributes'] = self.face_attributes.to_map()
        if self.face_rect is not None:
            result['FaceRect'] = self.face_rect.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceAttributes') is not None:
            temp_model = DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceAttributes()
            self.face_attributes = temp_model.from_map(m['FaceAttributes'])
        if m.get('FaceRect') is not None:
            temp_model = DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceRect()
            self.face_rect = temp_model.from_map(m['FaceRect'])
        return self


class DetectFaceAttributesResponseBodyDataFaceInfos(TeaModel):
    def __init__(
        self,
        face_attributes_detect_info: List[DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfo] = None,
    ):
        self.face_attributes_detect_info = face_attributes_detect_info

    def validate(self):
        if self.face_attributes_detect_info:
            for k in self.face_attributes_detect_info:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['FaceAttributesDetectInfo'] = []
        if self.face_attributes_detect_info is not None:
            for k in self.face_attributes_detect_info:
                result['FaceAttributesDetectInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.face_attributes_detect_info = []
        if m.get('FaceAttributesDetectInfo') is not None:
            for k in m.get('FaceAttributesDetectInfo'):
                temp_model = DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfo()
                self.face_attributes_detect_info.append(temp_model.from_map(k))
        return self


class DetectFaceAttributesResponseBodyData(TeaModel):
    def __init__(
        self,
        img_height: int = None,
        img_width: int = None,
        face_infos: DetectFaceAttributesResponseBodyDataFaceInfos = None,
    ):
        self.img_height = img_height
        self.img_width = img_width
        self.face_infos = face_infos

    def validate(self):
        if self.face_infos:
            self.face_infos.validate()

    def to_map(self):
        result = dict()
        if self.img_height is not None:
            result['ImgHeight'] = self.img_height
        if self.img_width is not None:
            result['ImgWidth'] = self.img_width
        if self.face_infos is not None:
            result['FaceInfos'] = self.face_infos.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImgHeight') is not None:
            self.img_height = m.get('ImgHeight')
        if m.get('ImgWidth') is not None:
            self.img_width = m.get('ImgWidth')
        if m.get('FaceInfos') is not None:
            temp_model = DetectFaceAttributesResponseBodyDataFaceInfos()
            self.face_infos = temp_model.from_map(m['FaceInfos'])
        return self


class DetectFaceAttributesResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: DetectFaceAttributesResponseBodyData = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = DetectFaceAttributesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DetectFaceAttributesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DetectFaceAttributesResponseBody = None,
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
            temp_model = DetectFaceAttributesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InitDeviceRequest(TeaModel):
    def __init__(
        self,
        certify_id: str = None,
        outer_order_no: str = None,
        channel: str = None,
        merchant: str = None,
        product_name: str = None,
        produce_node: str = None,
        biz_data: str = None,
        meta_info: str = None,
        certify_principal: str = None,
        app_version: str = None,
        device_token: str = None,
        ua_token: str = None,
        web_umid_token: str = None,
    ):
        self.certify_id = certify_id
        self.outer_order_no = outer_order_no
        self.channel = channel
        self.merchant = merchant
        self.product_name = product_name
        self.produce_node = produce_node
        self.biz_data = biz_data
        self.meta_info = meta_info
        self.certify_principal = certify_principal
        self.app_version = app_version
        self.device_token = device_token
        self.ua_token = ua_token
        self.web_umid_token = web_umid_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.outer_order_no is not None:
            result['OuterOrderNo'] = self.outer_order_no
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.merchant is not None:
            result['Merchant'] = self.merchant
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.produce_node is not None:
            result['ProduceNode'] = self.produce_node
        if self.biz_data is not None:
            result['BizData'] = self.biz_data
        if self.meta_info is not None:
            result['MetaInfo'] = self.meta_info
        if self.certify_principal is not None:
            result['CertifyPrincipal'] = self.certify_principal
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.device_token is not None:
            result['DeviceToken'] = self.device_token
        if self.ua_token is not None:
            result['UaToken'] = self.ua_token
        if self.web_umid_token is not None:
            result['WebUmidToken'] = self.web_umid_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('OuterOrderNo') is not None:
            self.outer_order_no = m.get('OuterOrderNo')
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('Merchant') is not None:
            self.merchant = m.get('Merchant')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProduceNode') is not None:
            self.produce_node = m.get('ProduceNode')
        if m.get('BizData') is not None:
            self.biz_data = m.get('BizData')
        if m.get('MetaInfo') is not None:
            self.meta_info = m.get('MetaInfo')
        if m.get('CertifyPrincipal') is not None:
            self.certify_principal = m.get('CertifyPrincipal')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('DeviceToken') is not None:
            self.device_token = m.get('DeviceToken')
        if m.get('UaToken') is not None:
            self.ua_token = m.get('UaToken')
        if m.get('WebUmidToken') is not None:
            self.web_umid_token = m.get('WebUmidToken')
        return self


class InitDeviceResponseBodyResultObject(TeaModel):
    def __init__(
        self,
        oss_end_point: str = None,
        ret_code_sub: str = None,
        protocol: str = None,
        message: str = None,
        ext_params: str = None,
        certify_id: str = None,
        file_name: str = None,
        access_key_id: str = None,
        presigned_url: str = None,
        security_token: str = None,
        bucket_name: str = None,
        file_name_prefix: str = None,
        access_key_secret: str = None,
        ret_message_sub: str = None,
        ret_code: str = None,
    ):
        self.oss_end_point = oss_end_point
        self.ret_code_sub = ret_code_sub
        self.protocol = protocol
        self.message = message
        self.ext_params = ext_params
        self.certify_id = certify_id
        self.file_name = file_name
        self.access_key_id = access_key_id
        self.presigned_url = presigned_url
        self.security_token = security_token
        self.bucket_name = bucket_name
        self.file_name_prefix = file_name_prefix
        self.access_key_secret = access_key_secret
        self.ret_message_sub = ret_message_sub
        self.ret_code = ret_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.oss_end_point is not None:
            result['OssEndPoint'] = self.oss_end_point
        if self.ret_code_sub is not None:
            result['RetCodeSub'] = self.ret_code_sub
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.message is not None:
            result['Message'] = self.message
        if self.ext_params is not None:
            result['ExtParams'] = self.ext_params
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.presigned_url is not None:
            result['PresignedUrl'] = self.presigned_url
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.file_name_prefix is not None:
            result['FileNamePrefix'] = self.file_name_prefix
        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret
        if self.ret_message_sub is not None:
            result['RetMessageSub'] = self.ret_message_sub
        if self.ret_code is not None:
            result['RetCode'] = self.ret_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OssEndPoint') is not None:
            self.oss_end_point = m.get('OssEndPoint')
        if m.get('RetCodeSub') is not None:
            self.ret_code_sub = m.get('RetCodeSub')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ExtParams') is not None:
            self.ext_params = m.get('ExtParams')
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('PresignedUrl') is not None:
            self.presigned_url = m.get('PresignedUrl')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('FileNamePrefix') is not None:
            self.file_name_prefix = m.get('FileNamePrefix')
        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')
        if m.get('RetMessageSub') is not None:
            self.ret_message_sub = m.get('RetMessageSub')
        if m.get('RetCode') is not None:
            self.ret_code = m.get('RetCode')
        return self


class InitDeviceResponseBody(TeaModel):
    def __init__(
        self,
        result_object: InitDeviceResponseBodyResultObject = None,
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
            temp_model = InitDeviceResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class InitDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: InitDeviceResponseBody = None,
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
            temp_model = InitDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InitFaceVerifyRequest(TeaModel):
    def __init__(
        self,
        scene_id: int = None,
        outer_order_no: str = None,
        product_code: str = None,
        cert_type: str = None,
        cert_name: str = None,
        cert_no: str = None,
        return_url: str = None,
        face_contrast_picture: str = None,
        meta_info: str = None,
        mobile: str = None,
        ip: str = None,
        user_id: str = None,
        face_contrast_picture_url: str = None,
        certify_id: str = None,
        oss_bucket_name: str = None,
        oss_object_name: str = None,
        model: str = None,
        callback_url: str = None,
        callback_token: str = None,
    ):
        self.scene_id = scene_id
        self.outer_order_no = outer_order_no
        self.product_code = product_code
        self.cert_type = cert_type
        self.cert_name = cert_name
        self.cert_no = cert_no
        self.return_url = return_url
        self.face_contrast_picture = face_contrast_picture
        self.meta_info = meta_info
        self.mobile = mobile
        self.ip = ip
        self.user_id = user_id
        self.face_contrast_picture_url = face_contrast_picture_url
        self.certify_id = certify_id
        self.oss_bucket_name = oss_bucket_name
        self.oss_object_name = oss_object_name
        self.model = model
        self.callback_url = callback_url
        self.callback_token = callback_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.outer_order_no is not None:
            result['OuterOrderNo'] = self.outer_order_no
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_no is not None:
            result['CertNo'] = self.cert_no
        if self.return_url is not None:
            result['ReturnUrl'] = self.return_url
        if self.face_contrast_picture is not None:
            result['FaceContrastPicture'] = self.face_contrast_picture
        if self.meta_info is not None:
            result['MetaInfo'] = self.meta_info
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.face_contrast_picture_url is not None:
            result['FaceContrastPictureUrl'] = self.face_contrast_picture_url
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name
        if self.oss_object_name is not None:
            result['OssObjectName'] = self.oss_object_name
        if self.model is not None:
            result['Model'] = self.model
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        if self.callback_token is not None:
            result['CallbackToken'] = self.callback_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('OuterOrderNo') is not None:
            self.outer_order_no = m.get('OuterOrderNo')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertNo') is not None:
            self.cert_no = m.get('CertNo')
        if m.get('ReturnUrl') is not None:
            self.return_url = m.get('ReturnUrl')
        if m.get('FaceContrastPicture') is not None:
            self.face_contrast_picture = m.get('FaceContrastPicture')
        if m.get('MetaInfo') is not None:
            self.meta_info = m.get('MetaInfo')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('FaceContrastPictureUrl') is not None:
            self.face_contrast_picture_url = m.get('FaceContrastPictureUrl')
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')
        if m.get('OssObjectName') is not None:
            self.oss_object_name = m.get('OssObjectName')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        if m.get('CallbackToken') is not None:
            self.callback_token = m.get('CallbackToken')
        return self


class InitFaceVerifyResponseBodyResultObject(TeaModel):
    def __init__(
        self,
        certify_id: str = None,
        certify_url: str = None,
    ):
        self.certify_id = certify_id
        self.certify_url = certify_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.certify_url is not None:
            result['CertifyUrl'] = self.certify_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('CertifyUrl') is not None:
            self.certify_url = m.get('CertifyUrl')
        return self


class InitFaceVerifyResponseBody(TeaModel):
    def __init__(
        self,
        result_object: InitFaceVerifyResponseBodyResultObject = None,
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
            temp_model = InitFaceVerifyResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class InitFaceVerifyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: InitFaceVerifyResponseBody = None,
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
            temp_model = InitFaceVerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LivenessFaceVerifyRequest(TeaModel):
    def __init__(
        self,
        scene_id: int = None,
        outer_order_no: str = None,
        product_code: str = None,
        face_contrast_picture: str = None,
        device_token: str = None,
        mobile: str = None,
        ip: str = None,
        user_id: str = None,
        face_contrast_picture_url: str = None,
        certify_id: str = None,
        oss_bucket_name: str = None,
        oss_object_name: str = None,
        model: str = None,
    ):
        self.scene_id = scene_id
        self.outer_order_no = outer_order_no
        self.product_code = product_code
        self.face_contrast_picture = face_contrast_picture
        self.device_token = device_token
        self.mobile = mobile
        self.ip = ip
        self.user_id = user_id
        self.face_contrast_picture_url = face_contrast_picture_url
        self.certify_id = certify_id
        self.oss_bucket_name = oss_bucket_name
        self.oss_object_name = oss_object_name
        self.model = model

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.outer_order_no is not None:
            result['OuterOrderNo'] = self.outer_order_no
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.face_contrast_picture is not None:
            result['FaceContrastPicture'] = self.face_contrast_picture
        if self.device_token is not None:
            result['DeviceToken'] = self.device_token
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.face_contrast_picture_url is not None:
            result['FaceContrastPictureUrl'] = self.face_contrast_picture_url
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name
        if self.oss_object_name is not None:
            result['OssObjectName'] = self.oss_object_name
        if self.model is not None:
            result['Model'] = self.model
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('OuterOrderNo') is not None:
            self.outer_order_no = m.get('OuterOrderNo')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('FaceContrastPicture') is not None:
            self.face_contrast_picture = m.get('FaceContrastPicture')
        if m.get('DeviceToken') is not None:
            self.device_token = m.get('DeviceToken')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('FaceContrastPictureUrl') is not None:
            self.face_contrast_picture_url = m.get('FaceContrastPictureUrl')
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')
        if m.get('OssObjectName') is not None:
            self.oss_object_name = m.get('OssObjectName')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        return self


class LivenessFaceVerifyResponseBodyResultObject(TeaModel):
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


class LivenessFaceVerifyResponseBody(TeaModel):
    def __init__(
        self,
        result_object: LivenessFaceVerifyResponseBodyResultObject = None,
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
            temp_model = LivenessFaceVerifyResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class LivenessFaceVerifyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: LivenessFaceVerifyResponseBody = None,
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
            temp_model = LivenessFaceVerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDeviceInfoRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        device_id: str = None,
        user_device_id: str = None,
        biz_type: str = None,
        duration: str = None,
        expired_day: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.device_id = device_id
        self.user_device_id = user_device_id
        self.biz_type = biz_type
        self.duration = duration
        self.expired_day = expired_day

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.user_device_id is not None:
            result['UserDeviceId'] = self.user_device_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.expired_day is not None:
            result['ExpiredDay'] = self.expired_day
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('UserDeviceId') is not None:
            self.user_device_id = m.get('UserDeviceId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('ExpiredDay') is not None:
            self.expired_day = m.get('ExpiredDay')
        return self


class ModifyDeviceInfoResponseBody(TeaModel):
    def __init__(
        self,
        expired_day: str = None,
        begin_day: str = None,
        request_id: str = None,
        device_id: str = None,
        biz_type: str = None,
        user_device_id: str = None,
    ):
        self.expired_day = expired_day
        self.begin_day = begin_day
        self.request_id = request_id
        self.device_id = device_id
        self.biz_type = biz_type
        self.user_device_id = user_device_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.expired_day is not None:
            result['ExpiredDay'] = self.expired_day
        if self.begin_day is not None:
            result['BeginDay'] = self.begin_day
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.user_device_id is not None:
            result['UserDeviceId'] = self.user_device_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpiredDay') is not None:
            self.expired_day = m.get('ExpiredDay')
        if m.get('BeginDay') is not None:
            self.begin_day = m.get('BeginDay')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('UserDeviceId') is not None:
            self.user_device_id = m.get('UserDeviceId')
        return self


class ModifyDeviceInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDeviceInfoResponseBody = None,
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
            temp_model = ModifyDeviceInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAppPackageRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        id: int = None,
        package_url: str = None,
        platform: str = None,
        debug: bool = None,
    ):
        self.source_ip = source_ip
        self.id = id
        self.package_url = package_url
        self.platform = platform
        self.debug = debug

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.id is not None:
            result['Id'] = self.id
        if self.package_url is not None:
            result['PackageUrl'] = self.package_url
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.debug is not None:
            result['Debug'] = self.debug
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PackageUrl') is not None:
            self.package_url = m.get('PackageUrl')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('Debug') is not None:
            self.debug = m.get('Debug')
        return self


class UpdateAppPackageResponseBody(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        request_id: str = None,
    ):
        self.task_id = task_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAppPackageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateAppPackageResponseBody = None,
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
            temp_model = UpdateAppPackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFaceConfigRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        biz_type: str = None,
        biz_name: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.biz_type = biz_type
        self.biz_name = biz_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        return self


class UpdateFaceConfigResponseBody(TeaModel):
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


class UpdateFaceConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateFaceConfigResponseBody = None,
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
            temp_model = UpdateFaceConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateVerifySettingRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        biz_type: str = None,
        biz_name: str = None,
        solution: str = None,
        guide_step: bool = None,
        privacy_step: bool = None,
        result_step: bool = None,
    ):
        self.source_ip = source_ip
        self.biz_type = biz_type
        self.biz_name = biz_name
        self.solution = solution
        self.guide_step = guide_step
        self.privacy_step = privacy_step
        self.result_step = result_step

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        if self.solution is not None:
            result['Solution'] = self.solution
        if self.guide_step is not None:
            result['GuideStep'] = self.guide_step
        if self.privacy_step is not None:
            result['PrivacyStep'] = self.privacy_step
        if self.result_step is not None:
            result['ResultStep'] = self.result_step
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        if m.get('Solution') is not None:
            self.solution = m.get('Solution')
        if m.get('GuideStep') is not None:
            self.guide_step = m.get('GuideStep')
        if m.get('PrivacyStep') is not None:
            self.privacy_step = m.get('PrivacyStep')
        if m.get('ResultStep') is not None:
            self.result_step = m.get('ResultStep')
        return self


class UpdateVerifySettingResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        step_list: List[str] = None,
        biz_name: str = None,
        biz_type: str = None,
        solution: str = None,
    ):
        self.request_id = request_id
        self.step_list = step_list
        self.biz_name = biz_name
        self.biz_type = biz_type
        self.solution = solution

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.step_list is not None:
            result['StepList'] = self.step_list
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.solution is not None:
            result['Solution'] = self.solution
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StepList') is not None:
            self.step_list = m.get('StepList')
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('Solution') is not None:
            self.solution = m.get('Solution')
        return self


class UpdateVerifySettingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateVerifySettingResponseBody = None,
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
            temp_model = UpdateVerifySettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyDeviceRequest(TeaModel):
    def __init__(
        self,
        certify_id: str = None,
        certify_data: str = None,
        app_version: str = None,
        ext_info: str = None,
    ):
        self.certify_id = certify_id
        self.certify_data = certify_data
        self.app_version = app_version
        self.ext_info = ext_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.certify_data is not None:
            result['CertifyData'] = self.certify_data
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('CertifyData') is not None:
            self.certify_data = m.get('CertifyData')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        return self


class VerifyDeviceResponseBodyResultObject(TeaModel):
    def __init__(
        self,
        ret_code_sub: str = None,
        product_ret_code: str = None,
        has_next: str = None,
        ret_message_sub: str = None,
        ext_params: str = None,
        validation_ret_code: str = None,
    ):
        self.ret_code_sub = ret_code_sub
        self.product_ret_code = product_ret_code
        self.has_next = has_next
        self.ret_message_sub = ret_message_sub
        self.ext_params = ext_params
        self.validation_ret_code = validation_ret_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ret_code_sub is not None:
            result['RetCodeSub'] = self.ret_code_sub
        if self.product_ret_code is not None:
            result['ProductRetCode'] = self.product_ret_code
        if self.has_next is not None:
            result['HasNext'] = self.has_next
        if self.ret_message_sub is not None:
            result['RetMessageSub'] = self.ret_message_sub
        if self.ext_params is not None:
            result['ExtParams'] = self.ext_params
        if self.validation_ret_code is not None:
            result['ValidationRetCode'] = self.validation_ret_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RetCodeSub') is not None:
            self.ret_code_sub = m.get('RetCodeSub')
        if m.get('ProductRetCode') is not None:
            self.product_ret_code = m.get('ProductRetCode')
        if m.get('HasNext') is not None:
            self.has_next = m.get('HasNext')
        if m.get('RetMessageSub') is not None:
            self.ret_message_sub = m.get('RetMessageSub')
        if m.get('ExtParams') is not None:
            self.ext_params = m.get('ExtParams')
        if m.get('ValidationRetCode') is not None:
            self.validation_ret_code = m.get('ValidationRetCode')
        return self


class VerifyDeviceResponseBody(TeaModel):
    def __init__(
        self,
        result_object: VerifyDeviceResponseBodyResultObject = None,
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
            temp_model = VerifyDeviceResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class VerifyDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: VerifyDeviceResponseBody = None,
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
            temp_model = VerifyDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyMaterialRequest(TeaModel):
    def __init__(
        self,
        id_card_back_image_url: str = None,
        face_image_url: str = None,
        biz_type: str = None,
        biz_id: str = None,
        name: str = None,
        id_card_number: str = None,
        id_card_front_image_url: str = None,
        user_id: str = None,
    ):
        self.id_card_back_image_url = id_card_back_image_url
        self.face_image_url = face_image_url
        self.biz_type = biz_type
        self.biz_id = biz_id
        self.name = name
        self.id_card_number = id_card_number
        self.id_card_front_image_url = id_card_front_image_url
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.id_card_back_image_url is not None:
            result['IdCardBackImageUrl'] = self.id_card_back_image_url
        if self.face_image_url is not None:
            result['FaceImageUrl'] = self.face_image_url
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.name is not None:
            result['Name'] = self.name
        if self.id_card_number is not None:
            result['IdCardNumber'] = self.id_card_number
        if self.id_card_front_image_url is not None:
            result['IdCardFrontImageUrl'] = self.id_card_front_image_url
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdCardBackImageUrl') is not None:
            self.id_card_back_image_url = m.get('IdCardBackImageUrl')
        if m.get('FaceImageUrl') is not None:
            self.face_image_url = m.get('FaceImageUrl')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('IdCardNumber') is not None:
            self.id_card_number = m.get('IdCardNumber')
        if m.get('IdCardFrontImageUrl') is not None:
            self.id_card_front_image_url = m.get('IdCardFrontImageUrl')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class VerifyMaterialResponseBodyMaterialIdCardInfo(TeaModel):
    def __init__(
        self,
        end_date: str = None,
        authority: str = None,
        address: str = None,
        number: str = None,
        start_date: str = None,
        back_image_url: str = None,
        nationality: str = None,
        birth: str = None,
        name: str = None,
        front_image_url: str = None,
    ):
        self.end_date = end_date
        self.authority = authority
        self.address = address
        self.number = number
        self.start_date = start_date
        self.back_image_url = back_image_url
        self.nationality = nationality
        self.birth = birth
        self.name = name
        self.front_image_url = front_image_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.authority is not None:
            result['Authority'] = self.authority
        if self.address is not None:
            result['Address'] = self.address
        if self.number is not None:
            result['Number'] = self.number
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.back_image_url is not None:
            result['BackImageUrl'] = self.back_image_url
        if self.nationality is not None:
            result['Nationality'] = self.nationality
        if self.birth is not None:
            result['Birth'] = self.birth
        if self.name is not None:
            result['Name'] = self.name
        if self.front_image_url is not None:
            result['FrontImageUrl'] = self.front_image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Authority') is not None:
            self.authority = m.get('Authority')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('BackImageUrl') is not None:
            self.back_image_url = m.get('BackImageUrl')
        if m.get('Nationality') is not None:
            self.nationality = m.get('Nationality')
        if m.get('Birth') is not None:
            self.birth = m.get('Birth')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('FrontImageUrl') is not None:
            self.front_image_url = m.get('FrontImageUrl')
        return self


class VerifyMaterialResponseBodyMaterial(TeaModel):
    def __init__(
        self,
        id_card_number: str = None,
        face_global_url: str = None,
        face_image_url: str = None,
        face_mask: str = None,
        id_card_name: str = None,
        id_card_info: VerifyMaterialResponseBodyMaterialIdCardInfo = None,
        face_quality: str = None,
    ):
        self.id_card_number = id_card_number
        self.face_global_url = face_global_url
        self.face_image_url = face_image_url
        self.face_mask = face_mask
        self.id_card_name = id_card_name
        self.id_card_info = id_card_info
        self.face_quality = face_quality

    def validate(self):
        if self.id_card_info:
            self.id_card_info.validate()

    def to_map(self):
        result = dict()
        if self.id_card_number is not None:
            result['IdCardNumber'] = self.id_card_number
        if self.face_global_url is not None:
            result['FaceGlobalUrl'] = self.face_global_url
        if self.face_image_url is not None:
            result['FaceImageUrl'] = self.face_image_url
        if self.face_mask is not None:
            result['FaceMask'] = self.face_mask
        if self.id_card_name is not None:
            result['IdCardName'] = self.id_card_name
        if self.id_card_info is not None:
            result['IdCardInfo'] = self.id_card_info.to_map()
        if self.face_quality is not None:
            result['FaceQuality'] = self.face_quality
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdCardNumber') is not None:
            self.id_card_number = m.get('IdCardNumber')
        if m.get('FaceGlobalUrl') is not None:
            self.face_global_url = m.get('FaceGlobalUrl')
        if m.get('FaceImageUrl') is not None:
            self.face_image_url = m.get('FaceImageUrl')
        if m.get('FaceMask') is not None:
            self.face_mask = m.get('FaceMask')
        if m.get('IdCardName') is not None:
            self.id_card_name = m.get('IdCardName')
        if m.get('IdCardInfo') is not None:
            temp_model = VerifyMaterialResponseBodyMaterialIdCardInfo()
            self.id_card_info = temp_model.from_map(m['IdCardInfo'])
        if m.get('FaceQuality') is not None:
            self.face_quality = m.get('FaceQuality')
        return self


class VerifyMaterialResponseBody(TeaModel):
    def __init__(
        self,
        verify_status: int = None,
        request_id: str = None,
        material: VerifyMaterialResponseBodyMaterial = None,
        authority_comparision_score: float = None,
        verify_token: str = None,
        id_card_face_comparison_score: float = None,
    ):
        self.verify_status = verify_status
        self.request_id = request_id
        self.material = material
        self.authority_comparision_score = authority_comparision_score
        self.verify_token = verify_token
        self.id_card_face_comparison_score = id_card_face_comparison_score

    def validate(self):
        if self.material:
            self.material.validate()

    def to_map(self):
        result = dict()
        if self.verify_status is not None:
            result['VerifyStatus'] = self.verify_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.material is not None:
            result['Material'] = self.material.to_map()
        if self.authority_comparision_score is not None:
            result['AuthorityComparisionScore'] = self.authority_comparision_score
        if self.verify_token is not None:
            result['VerifyToken'] = self.verify_token
        if self.id_card_face_comparison_score is not None:
            result['IdCardFaceComparisonScore'] = self.id_card_face_comparison_score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VerifyStatus') is not None:
            self.verify_status = m.get('VerifyStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Material') is not None:
            temp_model = VerifyMaterialResponseBodyMaterial()
            self.material = temp_model.from_map(m['Material'])
        if m.get('AuthorityComparisionScore') is not None:
            self.authority_comparision_score = m.get('AuthorityComparisionScore')
        if m.get('VerifyToken') is not None:
            self.verify_token = m.get('VerifyToken')
        if m.get('IdCardFaceComparisonScore') is not None:
            self.id_card_face_comparison_score = m.get('IdCardFaceComparisonScore')
        return self


class VerifyMaterialResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: VerifyMaterialResponseBody = None,
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
            temp_model = VerifyMaterialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


