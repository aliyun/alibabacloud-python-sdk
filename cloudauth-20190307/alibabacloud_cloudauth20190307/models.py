# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, BinaryIO, List


class AIGCFaceVerifyRequest(TeaModel):
    def __init__(
        self,
        face_contrast_picture: str = None,
        face_contrast_picture_url: str = None,
        oss_bucket_name: str = None,
        oss_object_name: str = None,
        outer_order_no: str = None,
        product_code: str = None,
        scene_id: int = None,
    ):
        # Base64 encoded photo.
        # > Choose one of the three ways to input images: FaceContrastPicture, FaceContrastPictureUrl, or OSS.
        self.face_contrast_picture = face_contrast_picture
        # Portrait address, accessible via public HTTP or HTTPS link.
        # 
        # > Choose one of the three ways to input images: FaceContrastPicture, FaceContrastPictureUrl, or OSS.
        self.face_contrast_picture_url = face_contrast_picture_url
        # Authorized OSS bucket name.
        # > Choose one of the three ways to input images: FaceContrastPicture, FaceContrastPictureUrl, or OSS.
        self.oss_bucket_name = oss_bucket_name
        # Authorized OSS file name.
        # > Choose one of the three ways to input images: FaceContrastPicture, FaceContrastPictureUrl, or OSS.
        self.oss_object_name = oss_object_name
        # A unique business identifier defined by the client side, used for subsequent troubleshooting. The value should be a combination of letters and numbers with a maximum length of 32 characters, please ensure its uniqueness.
        self.outer_order_no = outer_order_no
        # Product solution
        self.product_code = product_code
        # Authentication scene ID. This ID is automatically generated after creating an authentication scene in the console. For how to create an authentication scene, see Adding an Authentication Scene.
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_contrast_picture is not None:
            result['FaceContrastPicture'] = self.face_contrast_picture
        if self.face_contrast_picture_url is not None:
            result['FaceContrastPictureUrl'] = self.face_contrast_picture_url
        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name
        if self.oss_object_name is not None:
            result['OssObjectName'] = self.oss_object_name
        if self.outer_order_no is not None:
            result['OuterOrderNo'] = self.outer_order_no
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceContrastPicture') is not None:
            self.face_contrast_picture = m.get('FaceContrastPicture')
        if m.get('FaceContrastPictureUrl') is not None:
            self.face_contrast_picture_url = m.get('FaceContrastPictureUrl')
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')
        if m.get('OssObjectName') is not None:
            self.oss_object_name = m.get('OssObjectName')
        if m.get('OuterOrderNo') is not None:
            self.outer_order_no = m.get('OuterOrderNo')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class AIGCFaceVerifyResponseBodyResultObject(TeaModel):
    def __init__(
        self,
        certify_id: str = None,
        result: str = None,
        score: str = None,
    ):
        # Unique real-person authentication identifier.
        self.certify_id = certify_id
        # Authentication result. Values:
        # 
        # ● Y: AIGC-generated face.
        # 
        # ● N: Not detected
        self.result = result
        # Detection score
        self.score = score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.result is not None:
            result['Result'] = self.result
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class AIGCFaceVerifyResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: AIGCFaceVerifyResponseBodyResultObject = None,
    ):
        # Return code: 200 for success, others for failure.
        self.code = code
        # Message.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Returned result
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

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
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultObject') is not None:
            temp_model = AIGCFaceVerifyResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class AIGCFaceVerifyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AIGCFaceVerifyResponseBody = None,
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
            temp_model = AIGCFaceVerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BankMetaVerifyRequest(TeaModel):
    def __init__(
        self,
        bank_card: str = None,
        identify_num: str = None,
        identity_type: str = None,
        mobile: str = None,
        param_type: str = None,
        product_type: str = None,
        user_name: str = None,
        verify_mode: str = None,
    ):
        # Bank card number.
        # 
        # - When `paramType` is `normal`, enter the plain text bank card number.
        # - When `paramType` is `md5`, enter the part of the card number except the last 6 digits in plain text + the last 6 digits encrypted with MD5 (32 lowercase).
        self.bank_card = bank_card
        # ID number.
        # 
        # - When `ProductType` is `BANK_CARD_3_META`, this field is required.
        # - When `paramType` is `normal`, enter the plain text ID number.
        # - When `paramType` is `md5`, enter the first 6 digits of the ID number in plain text + the birth date encrypted with MD5 (32 lowercase MD5) + the last 4 digits of the ID number.
        self.identify_num = identify_num
        # Identity type.
        self.identity_type = identity_type
        # Mobile phone number.
        # 
        # - When `ProductType` is `BANK_CARD_4_META`, this field is required.
        # - When `paramType` is `normal`, enter the plain text mobile phone number.
        # - When `paramType` is `md5`, enter the mobile phone number (32 lowercase MD5).
        self.mobile = mobile
        # Parameter type:
        # 
        # - normal: Unencrypted.
        # - md5: MD5 encrypted.
        self.param_type = param_type
        # Product type to call:
        # 
        # - BANK_CARD_2_META: Bank card number + name verification.
        # - BANK_CARD_3_META: Bank card number + name + ID number verification.
        # - BANK_CARD_4_META: Bank card number + name + ID number + mobile phone number verification.
        self.product_type = product_type
        # Name.
        # 
        # - When `paramType` is `normal`, enter the plain text name.
        # - When `paramType` is `md5`, encrypt the first character of the name with MD5 (32 lowercase MD5) + the rest of the name in plain text.
        self.user_name = user_name
        # VERIFY_BANK_CARD: Bank card authentication mode. It indicates whether the provided bank card number matches the user\\"s real name, ID number, and mobile phone number.
        self.verify_mode = verify_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bank_card is not None:
            result['BankCard'] = self.bank_card
        if self.identify_num is not None:
            result['IdentifyNum'] = self.identify_num
        if self.identity_type is not None:
            result['IdentityType'] = self.identity_type
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.param_type is not None:
            result['ParamType'] = self.param_type
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.verify_mode is not None:
            result['VerifyMode'] = self.verify_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BankCard') is not None:
            self.bank_card = m.get('BankCard')
        if m.get('IdentifyNum') is not None:
            self.identify_num = m.get('IdentifyNum')
        if m.get('IdentityType') is not None:
            self.identity_type = m.get('IdentityType')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('VerifyMode') is not None:
            self.verify_mode = m.get('VerifyMode')
        return self


class BankMetaVerifyResponseBodyResultObject(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        sub_code: str = None,
    ):
        # Verification result.
        # 
        # - 1: Consistent (billable)
        # - 2: Inconsistent (billable)
        # - 3: No record found (non-billable)
        self.biz_code = biz_code
        # Verification details:
        # 
        # - **101**: Verification passed.
        # - **201**: Authentication information does not match, cardholder information is incorrect.
        # - **202**: Authentication information does not match, bank card has not enabled authentication payment.
        # - **203**: Authentication information does not match, bank card has expired.
        # - **204**: Authentication information does not match, bank card is a restricted card.
        # - **205**: Authentication information does not match, this card has been confiscated.
        # - **206**: Authentication information does not match, bank card is invalid.
        # - **207**: Authentication information does not match, this card has no corresponding issuing bank.
        # - **208**: Authentication information does not match, the card is uninitialized or a dormant card.
        # - **209**: Authentication information does not match, this card is a cheating card or swallowed card.
        # - **210**: Authentication information does not match, this card has been reported lost.
        # - **211**: Authentication information does not match, the number of password errors exceeds the limit.
        # - **212**: Authentication information does not match, the issuing bank does not support this transaction.
        # - **213**: Authentication information does not match, the card status is abnormal or the card is invalid.
        # - **214**: Authentication information does not match, no mobile phone number reserved.
        # - **215**: Authentication information does not match, the entered password, expiration date, or CVN2 is incorrect.
        # - **216**: Authentication information does not match, other card anomalies.
        # - **301**: Unable to verify, the bank card does not support this service.
        # - **302**: Unable to verify, verification failed or the bank refused to verify, please contact the issuing bank.
        # - **303**: Unable to verify, the bank card does not currently support mobile phone number verification.
        # - **304**: Unable to verify, the bank card number is incorrect.
        # - **305**: Unable to verify, other reasons.
        # - **306**: Unable to verify, the number of verifications exceeds the limit.
        self.sub_code = sub_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        return self


class BankMetaVerifyResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: BankMetaVerifyResponseBodyResultObject = None,
    ):
        # Return code: 200 for success, others for failure.
        self.code = code
        # Return message.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Returned result information
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

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
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultObject') is not None:
            temp_model = BankMetaVerifyResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class BankMetaVerifyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BankMetaVerifyResponseBody = None,
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
            temp_model = BankMetaVerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CompareFaceVerifyRequest(TeaModel):
    def __init__(
        self,
        crop: str = None,
        outer_order_no: str = None,
        product_code: str = None,
        scene_id: int = None,
        source_certify_id: str = None,
        source_face_contrast_picture: str = None,
        source_face_contrast_picture_url: str = None,
        source_oss_bucket_name: str = None,
        source_oss_object_name: str = None,
        target_certify_id: str = None,
        target_face_contrast_picture: str = None,
        target_face_contrast_picture_url: str = None,
        target_oss_bucket_name: str = None,
        target_oss_object_name: str = None,
    ):
        # Whether cropping is allowed. Default is not allowed, T/F.
        # 
        # - T: Indicates that cropping is required
        # - F: Indicates that cropping is not required (default F)
        self.crop = crop
        # A unique identifier for the merchant\\"s request. The value is a 32-character alphanumeric combination, where the first few characters are a custom abbreviation defined by the merchant, followed by a period, and the latter part can be a random or incrementing sequence.
        self.outer_order_no = outer_order_no
        # Fixed value: PV_FC.
        self.product_code = product_code
        # Authentication scenario ID.
        self.scene_id = scene_id
        # The CertifyId of a previously successful real-person verification, where the photo taken during that verification is used as the face comparison photo.
        # > Among the four ways to input facial photos (FaceContrastPicture, FaceContrastPictureUrl, CertifyId, OSS), choose one to provide.
        self.source_certify_id = source_certify_id
        # Base64 encoding of the photo.
        # > Choose one of the four ways to input a face photo: FaceContrastPicture, FaceContrastPictureUrl, CertifyId, or OSS.
        self.source_face_contrast_picture = source_face_contrast_picture
        # OSS photo URL, currently only supports authorized OSS photo URLs.
        # > Four ways to input face photos: FaceContrastPicture, FaceContrastPictureUrl, CertifyId, and OSS. Choose one of them to input.
        self.source_face_contrast_picture_url = source_face_contrast_picture_url
        # Name of the authorized OSS bucket.
        # > Choose one of the four ways to input face photos: FaceContrastPicture, FaceContrastPictureUrl, CertifyId, or OSS.
        self.source_oss_bucket_name = source_oss_bucket_name
        # Filename of the authorized OSS space.
        # > Choose one of the four ways to input face photos: FaceContrastPicture, FaceContrastPictureUrl, CertifyId, or OSS.
        self.source_oss_object_name = source_oss_object_name
        # CertifyId from a previously successful real-person authentication, where the photo taken during the authentication is used for face comparison.
        # 
        # > Choose one of the four methods to provide the reference face photo: FaceContrastPicture, FaceContrastPictureUrl, CertifyId, or OSS.
        self.target_certify_id = target_certify_id
        # Base64 encoding of the reference photo.
        # 
        # > Choose one of the four methods to provide the reference face photo: FaceContrastPicture, FaceContrastPictureUrl, CertifyId, or OSS.
        self.target_face_contrast_picture = target_face_contrast_picture
        # OSS address of the reference photo. Currently, only authorized OSS addresses are supported.
        # 
        # > Choose one of the four methods to provide the reference face photo: FaceContrastPicture, FaceContrastPictureUrl, CertifyId, or OSS.
        self.target_face_contrast_picture_url = target_face_contrast_picture_url
        # Name of the authorized OSS bucket.
        # 
        # > Choose one of the four methods to provide the reference face photo: FaceContrastPicture, FaceContrastPictureUrl, CertifyId, or OSS.
        self.target_oss_bucket_name = target_oss_bucket_name
        # File name in the authorized OSS space.
        # 
        # > Choose one of the four methods to provide the reference face photo: FaceContrastPicture, FaceContrastPictureUrl, CertifyId, or OSS.
        self.target_oss_object_name = target_oss_object_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.crop is not None:
            result['Crop'] = self.crop
        if self.outer_order_no is not None:
            result['OuterOrderNo'] = self.outer_order_no
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.source_certify_id is not None:
            result['SourceCertifyId'] = self.source_certify_id
        if self.source_face_contrast_picture is not None:
            result['SourceFaceContrastPicture'] = self.source_face_contrast_picture
        if self.source_face_contrast_picture_url is not None:
            result['SourceFaceContrastPictureUrl'] = self.source_face_contrast_picture_url
        if self.source_oss_bucket_name is not None:
            result['SourceOssBucketName'] = self.source_oss_bucket_name
        if self.source_oss_object_name is not None:
            result['SourceOssObjectName'] = self.source_oss_object_name
        if self.target_certify_id is not None:
            result['TargetCertifyId'] = self.target_certify_id
        if self.target_face_contrast_picture is not None:
            result['TargetFaceContrastPicture'] = self.target_face_contrast_picture
        if self.target_face_contrast_picture_url is not None:
            result['TargetFaceContrastPictureUrl'] = self.target_face_contrast_picture_url
        if self.target_oss_bucket_name is not None:
            result['TargetOssBucketName'] = self.target_oss_bucket_name
        if self.target_oss_object_name is not None:
            result['TargetOssObjectName'] = self.target_oss_object_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Crop') is not None:
            self.crop = m.get('Crop')
        if m.get('OuterOrderNo') is not None:
            self.outer_order_no = m.get('OuterOrderNo')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('SourceCertifyId') is not None:
            self.source_certify_id = m.get('SourceCertifyId')
        if m.get('SourceFaceContrastPicture') is not None:
            self.source_face_contrast_picture = m.get('SourceFaceContrastPicture')
        if m.get('SourceFaceContrastPictureUrl') is not None:
            self.source_face_contrast_picture_url = m.get('SourceFaceContrastPictureUrl')
        if m.get('SourceOssBucketName') is not None:
            self.source_oss_bucket_name = m.get('SourceOssBucketName')
        if m.get('SourceOssObjectName') is not None:
            self.source_oss_object_name = m.get('SourceOssObjectName')
        if m.get('TargetCertifyId') is not None:
            self.target_certify_id = m.get('TargetCertifyId')
        if m.get('TargetFaceContrastPicture') is not None:
            self.target_face_contrast_picture = m.get('TargetFaceContrastPicture')
        if m.get('TargetFaceContrastPictureUrl') is not None:
            self.target_face_contrast_picture_url = m.get('TargetFaceContrastPictureUrl')
        if m.get('TargetOssBucketName') is not None:
            self.target_oss_bucket_name = m.get('TargetOssBucketName')
        if m.get('TargetOssObjectName') is not None:
            self.target_oss_object_name = m.get('TargetOssObjectName')
        return self


class CompareFaceVerifyResponseBodyResultObject(TeaModel):
    def __init__(
        self,
        certify_id: str = None,
        passed: str = None,
        verify_score: float = None,
    ):
        # Unique identifier for the real-person authentication request.
        self.certify_id = certify_id
        # Whether the verification passed, T for pass, F for fail.
        self.passed = passed
        # Face comparison score.
        self.verify_score = verify_score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.passed is not None:
            result['Passed'] = self.passed
        if self.verify_score is not None:
            result['VerifyScore'] = self.verify_score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
        if m.get('VerifyScore') is not None:
            self.verify_score = m.get('VerifyScore')
        return self


class CompareFaceVerifyResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: CompareFaceVerifyResponseBodyResultObject = None,
    ):
        # Return code: 200 for success, other values indicate failure.
        self.code = code
        # Error message.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Face comparison result information.
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

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
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultObject') is not None:
            temp_model = CompareFaceVerifyResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class CompareFaceVerifyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CompareFaceVerifyResponseBody = None,
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
            temp_model = CompareFaceVerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CompareFacesRequest(TeaModel):
    def __init__(
        self,
        source_image_type: str = None,
        source_image_value: str = None,
        target_image_type: str = None,
        target_image_value: str = None,
    ):
        # Type of Image 1, with values:
        # 
        # - **FacePic**: User\\"s face photo
        # - **IDPic**: Headshot from the user\\"s second-generation ID card chip (typically obtained and decoded by a second-generation ID card reader)
        self.source_image_type = source_image_type
        # Address of Image 1. Please refer to the instructions on uploading image addresses.
        self.source_image_value = source_image_value
        # Type of Image 2, with values:
        # 
        # - **FacePic**: User\\"s face photo
        # - **IDPic**: Headshot from the user\\"s second-generation ID card chip (typically obtained and decoded by a second-generation ID card reader)
        self.target_image_type = target_image_type
        # Address of Image 2. Please refer to the instructions on uploading image addresses.
        self.target_image_value = target_image_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_image_type is not None:
            result['SourceImageType'] = self.source_image_type
        if self.source_image_value is not None:
            result['SourceImageValue'] = self.source_image_value
        if self.target_image_type is not None:
            result['TargetImageType'] = self.target_image_type
        if self.target_image_value is not None:
            result['TargetImageValue'] = self.target_image_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceImageType') is not None:
            self.source_image_type = m.get('SourceImageType')
        if m.get('SourceImageValue') is not None:
            self.source_image_value = m.get('SourceImageValue')
        if m.get('TargetImageType') is not None:
            self.target_image_type = m.get('TargetImageType')
        if m.get('TargetImageValue') is not None:
            self.target_image_value = m.get('TargetImageValue')
        return self


class CompareFacesResponseBodyData(TeaModel):
    def __init__(
        self,
        confidence_thresholds: str = None,
        similarity_score: float = None,
    ):
        # Confidence thresholds for face comparison. The returned content is a JSON Object, with the specific structure being `"key":"value"`.
        # 
        # - `key` represents the false acceptance rate, which is the probability of misidentifying someone else as the specified person.
        # - `value` is the corresponding threshold.
        # 
        # 
        # > Regarding the confidence thresholds (confidenceThresholds) in the example:
        # - `"0.0001": "90.07"` indicates that the threshold is 90.07 when the false acceptance rate is 0.01%.
        # - `"0.001": "80.01"` indicates that the threshold is 80.01 when the false acceptance rate is 0.1%.
        # - `"0.01": "70.02"` indicates that the threshold is 70.02 when the false acceptance rate is 1%.
        # 
        # Confidence thresholds are dynamically provided based on different images and algorithms, so do not persist these thresholds.
        self.confidence_thresholds = confidence_thresholds
        # The degree of similarity between the faces in the two images. The value range is [0, 100], with higher values indicating greater similarity.
        self.similarity_score = similarity_score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confidence_thresholds is not None:
            result['ConfidenceThresholds'] = self.confidence_thresholds
        if self.similarity_score is not None:
            result['SimilarityScore'] = self.similarity_score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfidenceThresholds') is not None:
            self.confidence_thresholds = m.get('ConfidenceThresholds')
        if m.get('SimilarityScore') is not None:
            self.similarity_score = m.get('SimilarityScore')
        return self


class CompareFacesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CompareFacesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # HTTP status code.
        self.code = code
        # Result of the face comparison.
        self.data = data
        # Error code.
        self.message = message
        # ID of the current request.
        self.request_id = request_id
        # Indicates whether the response was successful.
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
        if m.get('Data') is not None:
            temp_model = CompareFacesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CompareFacesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CompareFacesResponseBody = None,
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
            temp_model = CompareFacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ContrastFaceVerifyRequest(TeaModel):
    def __init__(
        self,
        cert_name: str = None,
        cert_no: str = None,
        cert_type: str = None,
        certify_id: str = None,
        crop: str = None,
        device_token: str = None,
        encrypt_type: str = None,
        face_contrast_file: str = None,
        face_contrast_picture: str = None,
        face_contrast_picture_url: str = None,
        ip: str = None,
        mobile: str = None,
        model: str = None,
        oss_bucket_name: str = None,
        oss_object_name: str = None,
        outer_order_no: str = None,
        product_code: str = None,
        scene_id: int = None,
        user_id: str = None,
    ):
        # Real name.
        self.cert_name = cert_name
        # ID number
        self.cert_no = cert_no
        # Type of identification. Currently, only IDENTITY_CARD is supported and must be provided.
        self.cert_type = cert_type
        # The CertifyId of a previously passed real-person authentication, with the photo taken during that authentication used as the comparison photo. 
        # > Among the four ways to input images (FaceContrastPicture, FaceContrastPictureUrl, CertifyId, OSS), choose one to provide.
        self.certify_id = certify_id
        # Allow face image cropping:
        # 
        # -  **T** – Cropping is allowed.
        # -  **F** (default) – Cropping is not allowed.
        self.crop = crop
        # Risk Identification - Device Token
        self.device_token = device_token
        # Encryption type. Leave it empty if no encryption is required.
        # 
        # If you enable encrypted transmission, you must specify the encryption algorithm; currently, only the SM2 (Chinese national standard) algorithm is supported.
        # 
        # When an encryption algorithm is specified, encrypt both **CertName** and **CertNo** and submit the resulting ciphertext. For more details on parameter encryption, see the [Parameter Encryption documentation](https://help.aliyun.com/zh/id-verification/financial-grade-id-verification/description-of-parameter-encryption?spm=a2c4g.11186623.0.0.49541a8554cELI#task-2229332).
        self.encrypt_type = encrypt_type
        # Local video file.
        self.face_contrast_file = face_contrast_file
        # Base64 encoded photo
        self.face_contrast_picture = face_contrast_picture
        # OSS photo URL, currently only supports authorized OSS photo URLs.
        # > Among the four ways to input images (FaceContrastPicture, FaceContrastPictureUrl, CertifyId, OSS), choose one to input.
        self.face_contrast_picture_url = face_contrast_picture_url
        # User IP.
        self.ip = ip
        # User\\"s phone number.
        self.mobile = mobile
        # Liveness detection type. Possible values:
        # 
        # • **NO_LIVENESS** – Liveness detection is disabled.
        # 
        # • **FRONT_CAMERA_LIVENESS** (default) – Liveness detection on face images captured with the mobile device’s front camera.
        # 
        # • **REAR_CAMERA_LIVENESS** – Liveness detection on face images captured in other scenarios (e.g., via the rear camera).
        self.model = model
        # Authorized OSS space Bucket name. In the methods of passing images, including FaceContrastPicture, FaceContrastPictureUrl, CertifyId, and OSS, choose one to pass in.
        self.oss_bucket_name = oss_bucket_name
        # Filename of the authorized OSS space.
        # > Among the four ways to input images (FaceContrastPicture, FaceContrastPictureUrl, CertifyId, OSS), choose one to input.
        self.oss_object_name = oss_object_name
        # A unique identifier for the merchant\\"s request. It is a 32-character alphanumeric combination. The first few characters are a custom abbreviation defined by the merchant, followed by a period, and the latter part can be a random or incrementing sequence.
        self.outer_order_no = outer_order_no
        # Fixed value: ID_MIN.
        self.product_code = product_code
        # Authentication scenario ID.
        self.scene_id = scene_id
        # Custom user ID defined by the customer\\"s business.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_no is not None:
            result['CertNo'] = self.cert_no
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.crop is not None:
            result['Crop'] = self.crop
        if self.device_token is not None:
            result['DeviceToken'] = self.device_token
        if self.encrypt_type is not None:
            result['EncryptType'] = self.encrypt_type
        if self.face_contrast_file is not None:
            result['FaceContrastFile'] = self.face_contrast_file
        if self.face_contrast_picture is not None:
            result['FaceContrastPicture'] = self.face_contrast_picture
        if self.face_contrast_picture_url is not None:
            result['FaceContrastPictureUrl'] = self.face_contrast_picture_url
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.model is not None:
            result['Model'] = self.model
        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name
        if self.oss_object_name is not None:
            result['OssObjectName'] = self.oss_object_name
        if self.outer_order_no is not None:
            result['OuterOrderNo'] = self.outer_order_no
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertNo') is not None:
            self.cert_no = m.get('CertNo')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('Crop') is not None:
            self.crop = m.get('Crop')
        if m.get('DeviceToken') is not None:
            self.device_token = m.get('DeviceToken')
        if m.get('EncryptType') is not None:
            self.encrypt_type = m.get('EncryptType')
        if m.get('FaceContrastFile') is not None:
            self.face_contrast_file = m.get('FaceContrastFile')
        if m.get('FaceContrastPicture') is not None:
            self.face_contrast_picture = m.get('FaceContrastPicture')
        if m.get('FaceContrastPictureUrl') is not None:
            self.face_contrast_picture_url = m.get('FaceContrastPictureUrl')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')
        if m.get('OssObjectName') is not None:
            self.oss_object_name = m.get('OssObjectName')
        if m.get('OuterOrderNo') is not None:
            self.outer_order_no = m.get('OuterOrderNo')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ContrastFaceVerifyAdvanceRequest(TeaModel):
    def __init__(
        self,
        cert_name: str = None,
        cert_no: str = None,
        cert_type: str = None,
        certify_id: str = None,
        crop: str = None,
        device_token: str = None,
        encrypt_type: str = None,
        face_contrast_file_object: BinaryIO = None,
        face_contrast_picture: str = None,
        face_contrast_picture_url: str = None,
        ip: str = None,
        mobile: str = None,
        model: str = None,
        oss_bucket_name: str = None,
        oss_object_name: str = None,
        outer_order_no: str = None,
        product_code: str = None,
        scene_id: int = None,
        user_id: str = None,
    ):
        # Real name.
        self.cert_name = cert_name
        # ID number
        self.cert_no = cert_no
        # Type of identification. Currently, only IDENTITY_CARD is supported and must be provided.
        self.cert_type = cert_type
        # The CertifyId of a previously passed real-person authentication, with the photo taken during that authentication used as the comparison photo. 
        # > Among the four ways to input images (FaceContrastPicture, FaceContrastPictureUrl, CertifyId, OSS), choose one to provide.
        self.certify_id = certify_id
        # Allow face image cropping:
        # 
        # -  **T** – Cropping is allowed.
        # -  **F** (default) – Cropping is not allowed.
        self.crop = crop
        # Risk Identification - Device Token
        self.device_token = device_token
        # Encryption type. Leave it empty if no encryption is required.
        # 
        # If you enable encrypted transmission, you must specify the encryption algorithm; currently, only the SM2 (Chinese national standard) algorithm is supported.
        # 
        # When an encryption algorithm is specified, encrypt both **CertName** and **CertNo** and submit the resulting ciphertext. For more details on parameter encryption, see the [Parameter Encryption documentation](https://help.aliyun.com/zh/id-verification/financial-grade-id-verification/description-of-parameter-encryption?spm=a2c4g.11186623.0.0.49541a8554cELI#task-2229332).
        self.encrypt_type = encrypt_type
        # Local video file.
        self.face_contrast_file_object = face_contrast_file_object
        # Base64 encoded photo
        self.face_contrast_picture = face_contrast_picture
        # OSS photo URL, currently only supports authorized OSS photo URLs.
        # > Among the four ways to input images (FaceContrastPicture, FaceContrastPictureUrl, CertifyId, OSS), choose one to input.
        self.face_contrast_picture_url = face_contrast_picture_url
        # User IP.
        self.ip = ip
        # User\\"s phone number.
        self.mobile = mobile
        # Liveness detection type. Possible values:
        # 
        # • **NO_LIVENESS** – Liveness detection is disabled.
        # 
        # • **FRONT_CAMERA_LIVENESS** (default) – Liveness detection on face images captured with the mobile device’s front camera.
        # 
        # • **REAR_CAMERA_LIVENESS** – Liveness detection on face images captured in other scenarios (e.g., via the rear camera).
        self.model = model
        # Authorized OSS space Bucket name. In the methods of passing images, including FaceContrastPicture, FaceContrastPictureUrl, CertifyId, and OSS, choose one to pass in.
        self.oss_bucket_name = oss_bucket_name
        # Filename of the authorized OSS space.
        # > Among the four ways to input images (FaceContrastPicture, FaceContrastPictureUrl, CertifyId, OSS), choose one to input.
        self.oss_object_name = oss_object_name
        # A unique identifier for the merchant\\"s request. It is a 32-character alphanumeric combination. The first few characters are a custom abbreviation defined by the merchant, followed by a period, and the latter part can be a random or incrementing sequence.
        self.outer_order_no = outer_order_no
        # Fixed value: ID_MIN.
        self.product_code = product_code
        # Authentication scenario ID.
        self.scene_id = scene_id
        # Custom user ID defined by the customer\\"s business.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_no is not None:
            result['CertNo'] = self.cert_no
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.crop is not None:
            result['Crop'] = self.crop
        if self.device_token is not None:
            result['DeviceToken'] = self.device_token
        if self.encrypt_type is not None:
            result['EncryptType'] = self.encrypt_type
        if self.face_contrast_file_object is not None:
            result['FaceContrastFile'] = self.face_contrast_file_object
        if self.face_contrast_picture is not None:
            result['FaceContrastPicture'] = self.face_contrast_picture
        if self.face_contrast_picture_url is not None:
            result['FaceContrastPictureUrl'] = self.face_contrast_picture_url
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.model is not None:
            result['Model'] = self.model
        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name
        if self.oss_object_name is not None:
            result['OssObjectName'] = self.oss_object_name
        if self.outer_order_no is not None:
            result['OuterOrderNo'] = self.outer_order_no
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertNo') is not None:
            self.cert_no = m.get('CertNo')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('Crop') is not None:
            self.crop = m.get('Crop')
        if m.get('DeviceToken') is not None:
            self.device_token = m.get('DeviceToken')
        if m.get('EncryptType') is not None:
            self.encrypt_type = m.get('EncryptType')
        if m.get('FaceContrastFile') is not None:
            self.face_contrast_file_object = m.get('FaceContrastFile')
        if m.get('FaceContrastPicture') is not None:
            self.face_contrast_picture = m.get('FaceContrastPicture')
        if m.get('FaceContrastPictureUrl') is not None:
            self.face_contrast_picture_url = m.get('FaceContrastPictureUrl')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')
        if m.get('OssObjectName') is not None:
            self.oss_object_name = m.get('OssObjectName')
        if m.get('OuterOrderNo') is not None:
            self.outer_order_no = m.get('OuterOrderNo')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ContrastFaceVerifyResponseBodyResultObject(TeaModel):
    def __init__(
        self,
        certify_id: str = None,
        identity_info: str = None,
        material_info: str = None,
        passed: str = None,
        sub_code: str = None,
    ):
        # Unique identifier for the real-person verification request.
        self.certify_id = certify_id
        # Information about the authenticated entity, which is usually empty in general authentication scenarios.
        self.identity_info = identity_info
        # Attachment information of the authenticated entity, mainly image materials, in JSON format, as follows.
        self.material_info = material_info
        # Whether it passed, T for pass, F for fail.
        self.passed = passed
        # Description of the authentication result. For details, see the SubCode explanation below.
        self.sub_code = sub_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.identity_info is not None:
            result['IdentityInfo'] = self.identity_info
        if self.material_info is not None:
            result['MaterialInfo'] = self.material_info
        if self.passed is not None:
            result['Passed'] = self.passed
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('IdentityInfo') is not None:
            self.identity_info = m.get('IdentityInfo')
        if m.get('MaterialInfo') is not None:
            self.material_info = m.get('MaterialInfo')
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        return self


class ContrastFaceVerifyResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: ContrastFaceVerifyResponseBodyResultObject = None,
    ):
        # Return code: 200 for success, others for failure.
        self.code = code
        # Error message.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Request result
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

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
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultObject') is not None:
            temp_model = ContrastFaceVerifyResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class ContrastFaceVerifyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ContrastFaceVerifyResponseBody = None,
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
            temp_model = ContrastFaceVerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAuthKeyRequest(TeaModel):
    def __init__(
        self,
        auth_years: int = None,
        biz_type: str = None,
        test: bool = None,
        user_device_id: str = None,
    ):
        # When the Test flag is false or empty, AuthYears is required, in years, with a range of [1,100]. A value of 100 indicates permanent authorization.
        self.auth_years = auth_years
        # Business type. No more than 64 characters. Can be used to note specific business, such as different face usage scenarios of the access party or the customer identifier to be delivered. It is recommended to pass this parameter.
        self.biz_type = biz_type
        # Test flag. If true, it indicates using test authorization with a default duration of 30 days; if false, the authorization duration will be based on AuthYears.
        self.test = test
        # User device ID. No more than 64 characters. Can be used to identify a specific device, and it is suggested to use the physical number of the device. It is recommended to pass this parameter.
        self.user_device_id = user_device_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_years is not None:
            result['AuthYears'] = self.auth_years
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.test is not None:
            result['Test'] = self.test
        if self.user_device_id is not None:
            result['UserDeviceId'] = self.user_device_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthYears') is not None:
            self.auth_years = m.get('AuthYears')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('Test') is not None:
            self.test = m.get('Test')
        if m.get('UserDeviceId') is not None:
            self.user_device_id = m.get('UserDeviceId')
        return self


class CreateAuthKeyResponseBody(TeaModel):
    def __init__(
        self,
        auth_key: str = None,
        request_id: str = None,
    ):
        # The key that can be used for authorization activation. The authorization key is valid for 30 minutes and cannot be reused. It is recommended to re-obtain it before each activation.
        self.auth_key = auth_key
        # The ID of this request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAuthKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAuthKeyResponseBody = None,
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
            temp_model = CreateAuthKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVerifySettingRequest(TeaModel):
    def __init__(
        self,
        biz_name: str = None,
        biz_type: str = None,
        guide_step: bool = None,
        privacy_step: bool = None,
        result_step: bool = None,
        solution: str = None,
    ):
        # Verification scenario name, supporting Chinese, English, numbers, and hyphens (-), with a maximum of 20 characters.
        # 
        # This parameter is required.
        self.biz_name = biz_name
        # Verification scenario identifier, supporting English letters, numbers, and hyphens (-), with a maximum of 20 characters.
        # 
        # This parameter is required.
        self.biz_type = biz_type
        # Whether to use the system\\"s default guide page.
        self.guide_step = guide_step
        # Whether to use the system\\"s default authorization page.
        self.privacy_step = privacy_step
        # Whether to use the system\\"s default result page.
        self.result_step = result_step
        # The name of the authentication solution to use, such as **RPBasic**, **RPBioOnly**, etc. For all supported authentication solutions, see [Authentication Solutions](https://help.aliyun.com/document_detail/127521.html).
        # 
        # This parameter is required.
        self.solution = solution

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.guide_step is not None:
            result['GuideStep'] = self.guide_step
        if self.privacy_step is not None:
            result['PrivacyStep'] = self.privacy_step
        if self.result_step is not None:
            result['ResultStep'] = self.result_step
        if self.solution is not None:
            result['Solution'] = self.solution
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('GuideStep') is not None:
            self.guide_step = m.get('GuideStep')
        if m.get('PrivacyStep') is not None:
            self.privacy_step = m.get('PrivacyStep')
        if m.get('ResultStep') is not None:
            self.result_step = m.get('ResultStep')
        if m.get('Solution') is not None:
            self.solution = m.get('Solution')
        return self


class CreateVerifySettingResponseBody(TeaModel):
    def __init__(
        self,
        biz_name: str = None,
        biz_type: str = None,
        request_id: str = None,
        solution: str = None,
        step_list: List[str] = None,
    ):
        # Verification scenario name.
        self.biz_name = biz_name
        # Verification scenario identifier.
        self.biz_type = biz_type
        # ID of this request.
        self.request_id = request_id
        # Authentication solution name.
        self.solution = solution
        # Authentication steps
        self.step_list = step_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.solution is not None:
            result['Solution'] = self.solution
        if self.step_list is not None:
            result['StepList'] = self.step_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Solution') is not None:
            self.solution = m.get('Solution')
        if m.get('StepList') is not None:
            self.step_list = m.get('StepList')
        return self


class CreateVerifySettingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateVerifySettingResponseBody = None,
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
            temp_model = CreateVerifySettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CredentialProductVerifyV2Request(TeaModel):
    def __init__(
        self,
        cred_name: str = None,
        cred_type: str = None,
        image_file: str = None,
        image_url: str = None,
        merchant_id: str = None,
        product_code: str = None,
    ):
        # Credential name: Only supports value 0501 (product image).
        # 
        # This parameter is required.
        self.cred_name = cred_name
        # Credential type: Only supports value 05 (product image).
        # 
        # This parameter is required.
        self.cred_type = cred_type
        # InputStream object of the image.
        self.image_file = image_file
        # URL of the image.
        self.image_url = image_url
        # Merchant ID.
        self.merchant_id = merchant_id
        # Invocation mode:
        # Only supports value ANTI_FAKE_CHECK.
        # 
        # This parameter is required.
        self.product_code = product_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cred_name is not None:
            result['CredName'] = self.cred_name
        if self.cred_type is not None:
            result['CredType'] = self.cred_type
        if self.image_file is not None:
            result['ImageFile'] = self.image_file
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.merchant_id is not None:
            result['MerchantId'] = self.merchant_id
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredName') is not None:
            self.cred_name = m.get('CredName')
        if m.get('CredType') is not None:
            self.cred_type = m.get('CredType')
        if m.get('ImageFile') is not None:
            self.image_file = m.get('ImageFile')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('MerchantId') is not None:
            self.merchant_id = m.get('MerchantId')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        return self


class CredentialProductVerifyV2AdvanceRequest(TeaModel):
    def __init__(
        self,
        cred_name: str = None,
        cred_type: str = None,
        image_file_object: BinaryIO = None,
        image_url: str = None,
        merchant_id: str = None,
        product_code: str = None,
    ):
        # Credential name: Only supports value 0501 (product image).
        # 
        # This parameter is required.
        self.cred_name = cred_name
        # Credential type: Only supports value 05 (product image).
        # 
        # This parameter is required.
        self.cred_type = cred_type
        # InputStream object of the image.
        self.image_file_object = image_file_object
        # URL of the image.
        self.image_url = image_url
        # Merchant ID.
        self.merchant_id = merchant_id
        # Invocation mode:
        # Only supports value ANTI_FAKE_CHECK.
        # 
        # This parameter is required.
        self.product_code = product_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cred_name is not None:
            result['CredName'] = self.cred_name
        if self.cred_type is not None:
            result['CredType'] = self.cred_type
        if self.image_file_object is not None:
            result['ImageFile'] = self.image_file_object
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.merchant_id is not None:
            result['MerchantId'] = self.merchant_id
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredName') is not None:
            self.cred_name = m.get('CredName')
        if m.get('CredType') is not None:
            self.cred_type = m.get('CredType')
        if m.get('ImageFile') is not None:
            self.image_file_object = m.get('ImageFile')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('MerchantId') is not None:
            self.merchant_id = m.get('MerchantId')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        return self


class CredentialProductVerifyV2ResponseBodyResultObject(TeaModel):
    def __init__(
        self,
        material_info: str = None,
        result: str = None,
        risk_score: Dict[str, str] = None,
        risk_tag: str = None,
    ):
        # Additional information in JSON format.
        self.material_info = material_info
        # - 0: Low risk
        # - 1: High risk
        # - 2: Suspicious
        self.result = result
        # Map of risk scores.
        self.risk_score = risk_score
        # Risk tags, separated by commas, including:
        # - PS: Image has been photoshopped
        # - LOW_QUALITY_PRODUCT: Low quality (low clarity)
        # - SAME_BACKGROUND: Similar background
        self.risk_tag = risk_tag

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.material_info is not None:
            result['MaterialInfo'] = self.material_info
        if self.result is not None:
            result['Result'] = self.result
        if self.risk_score is not None:
            result['RiskScore'] = self.risk_score
        if self.risk_tag is not None:
            result['RiskTag'] = self.risk_tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaterialInfo') is not None:
            self.material_info = m.get('MaterialInfo')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RiskScore') is not None:
            self.risk_score = m.get('RiskScore')
        if m.get('RiskTag') is not None:
            self.risk_tag = m.get('RiskTag')
        return self


class CredentialProductVerifyV2ResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: CredentialProductVerifyV2ResponseBodyResultObject = None,
    ):
        # Return code: 200 for success, others for failure.
        self.code = code
        # Return message.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Result object.
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

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
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultObject') is not None:
            temp_model = CredentialProductVerifyV2ResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class CredentialProductVerifyV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CredentialProductVerifyV2ResponseBody = None,
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
            temp_model = CredentialProductVerifyV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CredentialVerifyRequestMerchantDetail(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The private key of the certificate.
        # 
        # >  If this parameter is specified, you must also specify **CertName** and **Cert**. If **CertName**, **Cert**, and **Key** are specified, you do not need to specify **CertId**.
        self.key = key
        # Keyword value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CredentialVerifyRequest(TeaModel):
    def __init__(
        self,
        cert_num: str = None,
        cred_name: str = None,
        cred_type: str = None,
        identify_num: str = None,
        image_context: str = None,
        image_url: str = None,
        is_check: str = None,
        is_ocr: str = None,
        merchant_detail: List[CredentialVerifyRequestMerchantDetail] = None,
        merchant_id: str = None,
        product_code: str = None,
        prompt: str = None,
        prompt_model: str = None,
        user_name: str = None,
    ):
        # Relevant certificate number.
        self.cert_num = cert_num
        # - 01: Personal ID cards
        #   - **0101**: ID card
        #   - **0102**: Bank card
        #   - **0104**: Teacher qualification certificate
        #   - **0107**: Student ID card
        # - 02: Business scenario
        #   - **0201**: Storefront photo
        #   - **0202**: Counter photo
        #   - **0203**: Scene photo
        # - 03: Corporate qualifications
        #   - **0301**: Business license
        self.cred_name = cred_name
        # Credential type:
        # 
        # - 01: Personal ID cards
        # - 02: Business scenario
        # - 03: Corporate qualifications
        self.cred_type = cred_type
        # ID number:
        # 
        # Note
        # Only supports the ID numbers of second-generation resident IDs and Hong Kong, Macao, and Taiwan residence permits.
        # 
        # - When paramType is normal: enter the plaintext ID number.
        # 
        # - When paramType is md5: first 6 digits of the ID number (plaintext) + date of birth (ciphertext) + last 4 digits of the ID number (plaintext).
        self.identify_num = identify_num
        # Base64 encoded image, choose one from `imageUrl`, `imageFile`, or `imageContext`.
        self.image_context = image_context
        # Image URL, choose one from `imageUrl`, `imageFile`, or `imageContext`.
        self.image_url = image_url
        # Whether to enable authoritative authentication
        # 
        # - ****0****: No
        # - **1**: Yes
        self.is_check = is_check
        # Whether to enable OCR recognition.
        # 
        # - **0**: No
        # - **1**: Yes
        # 
        # > IsOCR can be set to 1 only when **CredType** is 01.
        self.is_ocr = is_ocr
        # Merchant details:
        # 
        # 
        # > This field is required when PromptModel is set to DEFAULT.
        self.merchant_detail = merchant_detail
        # Merchant ID. 
        # 
        # > This field is required when ****CredName**** is set to **02**.
        self.merchant_id = merchant_id
        # Invocation mode:
        # 
        # - **ANTI_FAKE_CHECK**: Image anti-forgery check
        # 
        # - **ANTI_FAKE_VL**: Image anti-forgery check and semantic understanding
        # 
        # - **IMAGE_VL_COG**: Image semantic understanding
        # 
        # Default value: ANTI_FAKE_CHECK
        # 
        # > When **CredType** is set to 02, **ProductCode** can only be ANTI_FAKE_VL or IMAGE_VL_COG.
        self.product_code = product_code
        # Customer-defined prompt content for image semantic understanding.
        # 
        # 
        # > This field is required when PromptModel is set to CUSTOM.
        self.prompt = prompt
        # Prompt acquisition method for image semantic understanding:
        # 
        # - **DEFAULT**: System default
        # 
        # - **CUSTOM**: Customer-defined
        # 
        # > When **ProductCode** is set to **ANTI_FAKE_VL** or **IMAGE_VL_COG**, this parameter must be provided.
        self.prompt_model = prompt_model
        # UserName
        self.user_name = user_name

    def validate(self):
        if self.merchant_detail:
            for k in self.merchant_detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_num is not None:
            result['CertNum'] = self.cert_num
        if self.cred_name is not None:
            result['CredName'] = self.cred_name
        if self.cred_type is not None:
            result['CredType'] = self.cred_type
        if self.identify_num is not None:
            result['IdentifyNum'] = self.identify_num
        if self.image_context is not None:
            result['ImageContext'] = self.image_context
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.is_check is not None:
            result['IsCheck'] = self.is_check
        if self.is_ocr is not None:
            result['IsOCR'] = self.is_ocr
        result['MerchantDetail'] = []
        if self.merchant_detail is not None:
            for k in self.merchant_detail:
                result['MerchantDetail'].append(k.to_map() if k else None)
        if self.merchant_id is not None:
            result['MerchantId'] = self.merchant_id
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        if self.prompt_model is not None:
            result['PromptModel'] = self.prompt_model
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertNum') is not None:
            self.cert_num = m.get('CertNum')
        if m.get('CredName') is not None:
            self.cred_name = m.get('CredName')
        if m.get('CredType') is not None:
            self.cred_type = m.get('CredType')
        if m.get('IdentifyNum') is not None:
            self.identify_num = m.get('IdentifyNum')
        if m.get('ImageContext') is not None:
            self.image_context = m.get('ImageContext')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('IsCheck') is not None:
            self.is_check = m.get('IsCheck')
        if m.get('IsOCR') is not None:
            self.is_ocr = m.get('IsOCR')
        self.merchant_detail = []
        if m.get('MerchantDetail') is not None:
            for k in m.get('MerchantDetail'):
                temp_model = CredentialVerifyRequestMerchantDetail()
                self.merchant_detail.append(temp_model.from_map(k))
        if m.get('MerchantId') is not None:
            self.merchant_id = m.get('MerchantId')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        if m.get('PromptModel') is not None:
            self.prompt_model = m.get('PromptModel')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class CredentialVerifyShrinkRequest(TeaModel):
    def __init__(
        self,
        cert_num: str = None,
        cred_name: str = None,
        cred_type: str = None,
        identify_num: str = None,
        image_context: str = None,
        image_url: str = None,
        is_check: str = None,
        is_ocr: str = None,
        merchant_detail_shrink: str = None,
        merchant_id: str = None,
        product_code: str = None,
        prompt: str = None,
        prompt_model: str = None,
        user_name: str = None,
    ):
        # Relevant certificate number.
        self.cert_num = cert_num
        # - 01: Personal ID cards
        #   - **0101**: ID card
        #   - **0102**: Bank card
        #   - **0104**: Teacher qualification certificate
        #   - **0107**: Student ID card
        # - 02: Business scenario
        #   - **0201**: Storefront photo
        #   - **0202**: Counter photo
        #   - **0203**: Scene photo
        # - 03: Corporate qualifications
        #   - **0301**: Business license
        self.cred_name = cred_name
        # Credential type:
        # 
        # - 01: Personal ID cards
        # - 02: Business scenario
        # - 03: Corporate qualifications
        self.cred_type = cred_type
        # ID number:
        # 
        # Note
        # Only supports the ID numbers of second-generation resident IDs and Hong Kong, Macao, and Taiwan residence permits.
        # 
        # - When paramType is normal: enter the plaintext ID number.
        # 
        # - When paramType is md5: first 6 digits of the ID number (plaintext) + date of birth (ciphertext) + last 4 digits of the ID number (plaintext).
        self.identify_num = identify_num
        # Base64 encoded image, choose one from `imageUrl`, `imageFile`, or `imageContext`.
        self.image_context = image_context
        # Image URL, choose one from `imageUrl`, `imageFile`, or `imageContext`.
        self.image_url = image_url
        # Whether to enable authoritative authentication
        # 
        # - ****0****: No
        # - **1**: Yes
        self.is_check = is_check
        # Whether to enable OCR recognition.
        # 
        # - **0**: No
        # - **1**: Yes
        # 
        # > IsOCR can be set to 1 only when **CredType** is 01.
        self.is_ocr = is_ocr
        # Merchant details:
        # 
        # 
        # > This field is required when PromptModel is set to DEFAULT.
        self.merchant_detail_shrink = merchant_detail_shrink
        # Merchant ID. 
        # 
        # > This field is required when ****CredName**** is set to **02**.
        self.merchant_id = merchant_id
        # Invocation mode:
        # 
        # - **ANTI_FAKE_CHECK**: Image anti-forgery check
        # 
        # - **ANTI_FAKE_VL**: Image anti-forgery check and semantic understanding
        # 
        # - **IMAGE_VL_COG**: Image semantic understanding
        # 
        # Default value: ANTI_FAKE_CHECK
        # 
        # > When **CredType** is set to 02, **ProductCode** can only be ANTI_FAKE_VL or IMAGE_VL_COG.
        self.product_code = product_code
        # Customer-defined prompt content for image semantic understanding.
        # 
        # 
        # > This field is required when PromptModel is set to CUSTOM.
        self.prompt = prompt
        # Prompt acquisition method for image semantic understanding:
        # 
        # - **DEFAULT**: System default
        # 
        # - **CUSTOM**: Customer-defined
        # 
        # > When **ProductCode** is set to **ANTI_FAKE_VL** or **IMAGE_VL_COG**, this parameter must be provided.
        self.prompt_model = prompt_model
        # UserName
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_num is not None:
            result['CertNum'] = self.cert_num
        if self.cred_name is not None:
            result['CredName'] = self.cred_name
        if self.cred_type is not None:
            result['CredType'] = self.cred_type
        if self.identify_num is not None:
            result['IdentifyNum'] = self.identify_num
        if self.image_context is not None:
            result['ImageContext'] = self.image_context
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.is_check is not None:
            result['IsCheck'] = self.is_check
        if self.is_ocr is not None:
            result['IsOCR'] = self.is_ocr
        if self.merchant_detail_shrink is not None:
            result['MerchantDetail'] = self.merchant_detail_shrink
        if self.merchant_id is not None:
            result['MerchantId'] = self.merchant_id
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        if self.prompt_model is not None:
            result['PromptModel'] = self.prompt_model
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertNum') is not None:
            self.cert_num = m.get('CertNum')
        if m.get('CredName') is not None:
            self.cred_name = m.get('CredName')
        if m.get('CredType') is not None:
            self.cred_type = m.get('CredType')
        if m.get('IdentifyNum') is not None:
            self.identify_num = m.get('IdentifyNum')
        if m.get('ImageContext') is not None:
            self.image_context = m.get('ImageContext')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('IsCheck') is not None:
            self.is_check = m.get('IsCheck')
        if m.get('IsOCR') is not None:
            self.is_ocr = m.get('IsOCR')
        if m.get('MerchantDetail') is not None:
            self.merchant_detail_shrink = m.get('MerchantDetail')
        if m.get('MerchantId') is not None:
            self.merchant_id = m.get('MerchantId')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        if m.get('PromptModel') is not None:
            self.prompt_model = m.get('PromptModel')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class CredentialVerifyResponseBodyResultObjectVlResult(TeaModel):
    def __init__(
        self,
        success: bool = None,
        vl_content: str = None,
    ):
        # Indicates whether the call was successful. Valid values:
        # 
        # - **true**: The call was successful.
        # - **false**: The call failed.
        self.success = success
        # Image understanding result:
        # 
        # - When PromptModel is DEFAULT, the output format refers to the example on the right.
        # 
        # - When PromptModel is CUSTOM, the output format follows the agreed format of the Prompt.
        self.vl_content = vl_content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        if self.vl_content is not None:
            result['VlContent'] = self.vl_content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('VlContent') is not None:
            self.vl_content = m.get('VlContent')
        return self


class CredentialVerifyResponseBodyResultObject(TeaModel):
    def __init__(
        self,
        material_info: str = None,
        ocr_info: str = None,
        result: str = None,
        risk_score: Dict[str, str] = None,
        risk_tag: str = None,
        verify_detail: str = None,
        verify_result: str = None,
        vl_result: CredentialVerifyResponseBodyResultObjectVlResult = None,
    ):
        # Additional information in JSON format.
        self.material_info = material_info
        # OCR recognition result.
        self.ocr_info = ocr_info
        # Risk result
        # 
        # - **0**: Low risk
        # - **1**: High risk
        # - **2**: Suspicious
        self.result = result
        # Risk score map.
        self.risk_score = risk_score
        # Risk tags, separated by commas (,), including:
        # 
        # - **PS**: Image manipulation.
        # - **SCREEN_PHOTO**: Screen recapture.
        # - **SCREENSHOT**: Screenshot.
        # - **WATERMARK**: Watermark.
        # - **SAME_BACKGROUND**: Similar background.
        # - **ORIGINAL_PHOTO**: Not the original image
        self.risk_tag = risk_tag
        # Authority verification details.
        self.verify_detail = verify_detail
        # The verification result.
        self.verify_result = verify_result
        # Qwen interpretation.
        self.vl_result = vl_result

    def validate(self):
        if self.vl_result:
            self.vl_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.material_info is not None:
            result['MaterialInfo'] = self.material_info
        if self.ocr_info is not None:
            result['OcrInfo'] = self.ocr_info
        if self.result is not None:
            result['Result'] = self.result
        if self.risk_score is not None:
            result['RiskScore'] = self.risk_score
        if self.risk_tag is not None:
            result['RiskTag'] = self.risk_tag
        if self.verify_detail is not None:
            result['VerifyDetail'] = self.verify_detail
        if self.verify_result is not None:
            result['VerifyResult'] = self.verify_result
        if self.vl_result is not None:
            result['VlResult'] = self.vl_result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaterialInfo') is not None:
            self.material_info = m.get('MaterialInfo')
        if m.get('OcrInfo') is not None:
            self.ocr_info = m.get('OcrInfo')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RiskScore') is not None:
            self.risk_score = m.get('RiskScore')
        if m.get('RiskTag') is not None:
            self.risk_tag = m.get('RiskTag')
        if m.get('VerifyDetail') is not None:
            self.verify_detail = m.get('VerifyDetail')
        if m.get('VerifyResult') is not None:
            self.verify_result = m.get('VerifyResult')
        if m.get('VlResult') is not None:
            temp_model = CredentialVerifyResponseBodyResultObjectVlResult()
            self.vl_result = temp_model.from_map(m['VlResult'])
        return self


class CredentialVerifyResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: CredentialVerifyResponseBodyResultObject = None,
    ):
        # Return code: 200 for success, others for failure.
        self.code = code
        # Return message.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Returned result
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

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
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultObject') is not None:
            temp_model = CredentialVerifyResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class CredentialVerifyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CredentialVerifyResponseBody = None,
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
            temp_model = CredentialVerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CredentialVerifyV2RequestMerchantDetail(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # Keyword key.
        self.key = key
        # Keyword value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CredentialVerifyV2Request(TeaModel):
    def __init__(
        self,
        cert_num: str = None,
        cred_name: str = None,
        cred_type: str = None,
        identify_num: str = None,
        image_context: str = None,
        image_file: str = None,
        image_url: str = None,
        is_check: str = None,
        is_ocr: str = None,
        merchant_detail: List[CredentialVerifyV2RequestMerchantDetail] = None,
        merchant_id: str = None,
        product_code: str = None,
        prompt: str = None,
        prompt_model: str = None,
        user_name: str = None,
    ):
        # Relevant certificate number.
        self.cert_num = cert_num
        # - 01: Personal ID cards
        #   - 0101: ID card
        #   - 0102: Bank card
        #   - 0104: Teacher qualification certificate
        #   - 0107: Student ID card
        # - 02: Business scenario
        #   - 0201: Storefront photo
        #   - 0202: Counter photo
        #   - 0203: Scene photo
        # - 03: Corporate qualifications
        #   - 0301: Business license
        self.cred_name = cred_name
        # Credential type:
        # 
        # - 01: Personal ID cards
        # - 02: Business scenario
        # - 03: Corporate qualifications
        self.cred_type = cred_type
        # ID number.
        self.identify_num = identify_num
        # Base64 encoded image, choose one from `imageUrl`, `imageFile`, or `imageContext`.
        self.image_context = image_context
        # Image input stream, choose one from `imageUrl`, `imageFile`, or `imageContext`.
        self.image_file = image_file
        # Image URL, choose one from `imageUrl`, `imageFile`, or `imageContext`.
        self.image_url = image_url
        # Whether to enable authoritative authentication
        # 
        # - ****0****: No
        # - **1**: Yes
        self.is_check = is_check
        # Whether to use OCR
        self.is_ocr = is_ocr
        # Merchant details:
        # 
        # MerchantName: Merchant name
        # 
        # BusinessType: Industry information
        # 
        # BusinessContent: Business content
        # 
        # This field is required when PromptModel is set to DEFAULT.
        self.merchant_detail = merchant_detail
        # Merchant ID. This field is required when ****CredName**** is set to **02**.
        self.merchant_id = merchant_id
        # Invocation mode:
        # 
        # - ANTI_FAKE_CHECK: Image anti-forgery check
        # 
        # - ANTI_FAKE_VL: Image anti-forgery check and semantic understanding
        # 
        # - IMAGE_VL_COG: Image semantic understanding
        # 
        # Default value: ANTI_FAKE_CHECK
        # 
        # When CredType is set to 02, ProductCode can only be ANTI_FAKE_VL or IMAGE_VL_COG.
        self.product_code = product_code
        # Customer-defined prompt content for image semantic understanding.
        # 
        # This field is required when PromptModel is set to CUSTOM.
        self.prompt = prompt
        # Prompt acquisition method for image semantic understanding:
        # 
        # - DEFAULT: System default
        # 
        # - CUSTOM: Customer-defined
        # 
        # Note: When ProductCode is set to ANTI_FAKE_VL or IMAGE_VL_COG, this parameter must be provided.
        self.prompt_model = prompt_model
        # Name.
        self.user_name = user_name

    def validate(self):
        if self.merchant_detail:
            for k in self.merchant_detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_num is not None:
            result['CertNum'] = self.cert_num
        if self.cred_name is not None:
            result['CredName'] = self.cred_name
        if self.cred_type is not None:
            result['CredType'] = self.cred_type
        if self.identify_num is not None:
            result['IdentifyNum'] = self.identify_num
        if self.image_context is not None:
            result['ImageContext'] = self.image_context
        if self.image_file is not None:
            result['ImageFile'] = self.image_file
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.is_check is not None:
            result['IsCheck'] = self.is_check
        if self.is_ocr is not None:
            result['IsOcr'] = self.is_ocr
        result['MerchantDetail'] = []
        if self.merchant_detail is not None:
            for k in self.merchant_detail:
                result['MerchantDetail'].append(k.to_map() if k else None)
        if self.merchant_id is not None:
            result['MerchantId'] = self.merchant_id
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        if self.prompt_model is not None:
            result['PromptModel'] = self.prompt_model
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertNum') is not None:
            self.cert_num = m.get('CertNum')
        if m.get('CredName') is not None:
            self.cred_name = m.get('CredName')
        if m.get('CredType') is not None:
            self.cred_type = m.get('CredType')
        if m.get('IdentifyNum') is not None:
            self.identify_num = m.get('IdentifyNum')
        if m.get('ImageContext') is not None:
            self.image_context = m.get('ImageContext')
        if m.get('ImageFile') is not None:
            self.image_file = m.get('ImageFile')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('IsCheck') is not None:
            self.is_check = m.get('IsCheck')
        if m.get('IsOcr') is not None:
            self.is_ocr = m.get('IsOcr')
        self.merchant_detail = []
        if m.get('MerchantDetail') is not None:
            for k in m.get('MerchantDetail'):
                temp_model = CredentialVerifyV2RequestMerchantDetail()
                self.merchant_detail.append(temp_model.from_map(k))
        if m.get('MerchantId') is not None:
            self.merchant_id = m.get('MerchantId')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        if m.get('PromptModel') is not None:
            self.prompt_model = m.get('PromptModel')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class CredentialVerifyV2AdvanceRequestMerchantDetail(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # Keyword key.
        self.key = key
        # Keyword value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CredentialVerifyV2AdvanceRequest(TeaModel):
    def __init__(
        self,
        cert_num: str = None,
        cred_name: str = None,
        cred_type: str = None,
        identify_num: str = None,
        image_context: str = None,
        image_file_object: BinaryIO = None,
        image_url: str = None,
        is_check: str = None,
        is_ocr: str = None,
        merchant_detail: List[CredentialVerifyV2AdvanceRequestMerchantDetail] = None,
        merchant_id: str = None,
        product_code: str = None,
        prompt: str = None,
        prompt_model: str = None,
        user_name: str = None,
    ):
        # Relevant certificate number.
        self.cert_num = cert_num
        # - 01: Personal ID cards
        #   - 0101: ID card
        #   - 0102: Bank card
        #   - 0104: Teacher qualification certificate
        #   - 0107: Student ID card
        # - 02: Business scenario
        #   - 0201: Storefront photo
        #   - 0202: Counter photo
        #   - 0203: Scene photo
        # - 03: Corporate qualifications
        #   - 0301: Business license
        self.cred_name = cred_name
        # Credential type:
        # 
        # - 01: Personal ID cards
        # - 02: Business scenario
        # - 03: Corporate qualifications
        self.cred_type = cred_type
        # ID number.
        self.identify_num = identify_num
        # Base64 encoded image, choose one from `imageUrl`, `imageFile`, or `imageContext`.
        self.image_context = image_context
        # Image input stream, choose one from `imageUrl`, `imageFile`, or `imageContext`.
        self.image_file_object = image_file_object
        # Image URL, choose one from `imageUrl`, `imageFile`, or `imageContext`.
        self.image_url = image_url
        # Whether to enable authoritative authentication
        # 
        # - ****0****: No
        # - **1**: Yes
        self.is_check = is_check
        # Whether to use OCR
        self.is_ocr = is_ocr
        # Merchant details:
        # 
        # MerchantName: Merchant name
        # 
        # BusinessType: Industry information
        # 
        # BusinessContent: Business content
        # 
        # This field is required when PromptModel is set to DEFAULT.
        self.merchant_detail = merchant_detail
        # Merchant ID. This field is required when ****CredName**** is set to **02**.
        self.merchant_id = merchant_id
        # Invocation mode:
        # 
        # - ANTI_FAKE_CHECK: Image anti-forgery check
        # 
        # - ANTI_FAKE_VL: Image anti-forgery check and semantic understanding
        # 
        # - IMAGE_VL_COG: Image semantic understanding
        # 
        # Default value: ANTI_FAKE_CHECK
        # 
        # When CredType is set to 02, ProductCode can only be ANTI_FAKE_VL or IMAGE_VL_COG.
        self.product_code = product_code
        # Customer-defined prompt content for image semantic understanding.
        # 
        # This field is required when PromptModel is set to CUSTOM.
        self.prompt = prompt
        # Prompt acquisition method for image semantic understanding:
        # 
        # - DEFAULT: System default
        # 
        # - CUSTOM: Customer-defined
        # 
        # Note: When ProductCode is set to ANTI_FAKE_VL or IMAGE_VL_COG, this parameter must be provided.
        self.prompt_model = prompt_model
        # Name.
        self.user_name = user_name

    def validate(self):
        if self.merchant_detail:
            for k in self.merchant_detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_num is not None:
            result['CertNum'] = self.cert_num
        if self.cred_name is not None:
            result['CredName'] = self.cred_name
        if self.cred_type is not None:
            result['CredType'] = self.cred_type
        if self.identify_num is not None:
            result['IdentifyNum'] = self.identify_num
        if self.image_context is not None:
            result['ImageContext'] = self.image_context
        if self.image_file_object is not None:
            result['ImageFile'] = self.image_file_object
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.is_check is not None:
            result['IsCheck'] = self.is_check
        if self.is_ocr is not None:
            result['IsOcr'] = self.is_ocr
        result['MerchantDetail'] = []
        if self.merchant_detail is not None:
            for k in self.merchant_detail:
                result['MerchantDetail'].append(k.to_map() if k else None)
        if self.merchant_id is not None:
            result['MerchantId'] = self.merchant_id
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        if self.prompt_model is not None:
            result['PromptModel'] = self.prompt_model
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertNum') is not None:
            self.cert_num = m.get('CertNum')
        if m.get('CredName') is not None:
            self.cred_name = m.get('CredName')
        if m.get('CredType') is not None:
            self.cred_type = m.get('CredType')
        if m.get('IdentifyNum') is not None:
            self.identify_num = m.get('IdentifyNum')
        if m.get('ImageContext') is not None:
            self.image_context = m.get('ImageContext')
        if m.get('ImageFile') is not None:
            self.image_file_object = m.get('ImageFile')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('IsCheck') is not None:
            self.is_check = m.get('IsCheck')
        if m.get('IsOcr') is not None:
            self.is_ocr = m.get('IsOcr')
        self.merchant_detail = []
        if m.get('MerchantDetail') is not None:
            for k in m.get('MerchantDetail'):
                temp_model = CredentialVerifyV2AdvanceRequestMerchantDetail()
                self.merchant_detail.append(temp_model.from_map(k))
        if m.get('MerchantId') is not None:
            self.merchant_id = m.get('MerchantId')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        if m.get('PromptModel') is not None:
            self.prompt_model = m.get('PromptModel')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class CredentialVerifyV2ShrinkRequest(TeaModel):
    def __init__(
        self,
        cert_num: str = None,
        cred_name: str = None,
        cred_type: str = None,
        identify_num: str = None,
        image_context: str = None,
        image_file: str = None,
        image_url: str = None,
        is_check: str = None,
        is_ocr: str = None,
        merchant_detail_shrink: str = None,
        merchant_id: str = None,
        product_code: str = None,
        prompt: str = None,
        prompt_model: str = None,
        user_name: str = None,
    ):
        # Relevant certificate number.
        self.cert_num = cert_num
        # - 01: Personal ID cards
        #   - 0101: ID card
        #   - 0102: Bank card
        #   - 0104: Teacher qualification certificate
        #   - 0107: Student ID card
        # - 02: Business scenario
        #   - 0201: Storefront photo
        #   - 0202: Counter photo
        #   - 0203: Scene photo
        # - 03: Corporate qualifications
        #   - 0301: Business license
        self.cred_name = cred_name
        # Credential type:
        # 
        # - 01: Personal ID cards
        # - 02: Business scenario
        # - 03: Corporate qualifications
        self.cred_type = cred_type
        # ID number.
        self.identify_num = identify_num
        # Base64 encoded image, choose one from `imageUrl`, `imageFile`, or `imageContext`.
        self.image_context = image_context
        # Image input stream, choose one from `imageUrl`, `imageFile`, or `imageContext`.
        self.image_file = image_file
        # Image URL, choose one from `imageUrl`, `imageFile`, or `imageContext`.
        self.image_url = image_url
        # Whether to enable authoritative authentication
        # 
        # - ****0****: No
        # - **1**: Yes
        self.is_check = is_check
        # Whether to use OCR
        self.is_ocr = is_ocr
        # Merchant details:
        # 
        # MerchantName: Merchant name
        # 
        # BusinessType: Industry information
        # 
        # BusinessContent: Business content
        # 
        # This field is required when PromptModel is set to DEFAULT.
        self.merchant_detail_shrink = merchant_detail_shrink
        # Merchant ID. This field is required when ****CredName**** is set to **02**.
        self.merchant_id = merchant_id
        # Invocation mode:
        # 
        # - ANTI_FAKE_CHECK: Image anti-forgery check
        # 
        # - ANTI_FAKE_VL: Image anti-forgery check and semantic understanding
        # 
        # - IMAGE_VL_COG: Image semantic understanding
        # 
        # Default value: ANTI_FAKE_CHECK
        # 
        # When CredType is set to 02, ProductCode can only be ANTI_FAKE_VL or IMAGE_VL_COG.
        self.product_code = product_code
        # Customer-defined prompt content for image semantic understanding.
        # 
        # This field is required when PromptModel is set to CUSTOM.
        self.prompt = prompt
        # Prompt acquisition method for image semantic understanding:
        # 
        # - DEFAULT: System default
        # 
        # - CUSTOM: Customer-defined
        # 
        # Note: When ProductCode is set to ANTI_FAKE_VL or IMAGE_VL_COG, this parameter must be provided.
        self.prompt_model = prompt_model
        # Name.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_num is not None:
            result['CertNum'] = self.cert_num
        if self.cred_name is not None:
            result['CredName'] = self.cred_name
        if self.cred_type is not None:
            result['CredType'] = self.cred_type
        if self.identify_num is not None:
            result['IdentifyNum'] = self.identify_num
        if self.image_context is not None:
            result['ImageContext'] = self.image_context
        if self.image_file is not None:
            result['ImageFile'] = self.image_file
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.is_check is not None:
            result['IsCheck'] = self.is_check
        if self.is_ocr is not None:
            result['IsOcr'] = self.is_ocr
        if self.merchant_detail_shrink is not None:
            result['MerchantDetail'] = self.merchant_detail_shrink
        if self.merchant_id is not None:
            result['MerchantId'] = self.merchant_id
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        if self.prompt_model is not None:
            result['PromptModel'] = self.prompt_model
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertNum') is not None:
            self.cert_num = m.get('CertNum')
        if m.get('CredName') is not None:
            self.cred_name = m.get('CredName')
        if m.get('CredType') is not None:
            self.cred_type = m.get('CredType')
        if m.get('IdentifyNum') is not None:
            self.identify_num = m.get('IdentifyNum')
        if m.get('ImageContext') is not None:
            self.image_context = m.get('ImageContext')
        if m.get('ImageFile') is not None:
            self.image_file = m.get('ImageFile')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('IsCheck') is not None:
            self.is_check = m.get('IsCheck')
        if m.get('IsOcr') is not None:
            self.is_ocr = m.get('IsOcr')
        if m.get('MerchantDetail') is not None:
            self.merchant_detail_shrink = m.get('MerchantDetail')
        if m.get('MerchantId') is not None:
            self.merchant_id = m.get('MerchantId')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        if m.get('PromptModel') is not None:
            self.prompt_model = m.get('PromptModel')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class CredentialVerifyV2ResponseBodyResultObjectVlResult(TeaModel):
    def __init__(
        self,
        success: bool = None,
        vl_content: str = None,
    ):
        # Qwen interpretation success indicator
        # 
        # true: Success
        # 
        # false: Failure
        self.success = success
        # Image understanding result:
        # 
        # - When PromptModel is DEFAULT, the output format refers to the example on the right.
        # 
        # - When PromptModel is CUSTOM, the output format follows the agreed format of the Prompt.
        self.vl_content = vl_content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        if self.vl_content is not None:
            result['VlContent'] = self.vl_content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('VlContent') is not None:
            self.vl_content = m.get('VlContent')
        return self


class CredentialVerifyV2ResponseBodyResultObject(TeaModel):
    def __init__(
        self,
        material_info: str = None,
        ocr_info: str = None,
        result: str = None,
        risk_score: Dict[str, str] = None,
        risk_tag: str = None,
        verify_detail: str = None,
        verify_result: str = None,
        vl_result: CredentialVerifyV2ResponseBodyResultObjectVlResult = None,
    ):
        # Additional information in JSON format.
        self.material_info = material_info
        # OCR recognition result.
        self.ocr_info = ocr_info
        # Risk result
        # 
        # - 0: Low risk
        # - 1: High risk
        # - 2: Suspicious
        self.result = result
        # Risk score map.
        self.risk_score = risk_score
        # Risk tags, separated by commas (,), including:
        # 
        # - PS: Image manipulation.
        # - SCREEN_PHOTO: Screen recapture.
        # - SCREENSHOT: Screenshot.
        # - WATERMARK: Watermark.
        # - SAME_BACKGROUND: Similar background.
        # - ORIGINAL_PHOTO: Not the original image
        self.risk_tag = risk_tag
        # Authority verification details.
        self.verify_detail = verify_detail
        # Authority verification result
        self.verify_result = verify_result
        # Qwen interpretation.
        self.vl_result = vl_result

    def validate(self):
        if self.vl_result:
            self.vl_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.material_info is not None:
            result['MaterialInfo'] = self.material_info
        if self.ocr_info is not None:
            result['OcrInfo'] = self.ocr_info
        if self.result is not None:
            result['Result'] = self.result
        if self.risk_score is not None:
            result['RiskScore'] = self.risk_score
        if self.risk_tag is not None:
            result['RiskTag'] = self.risk_tag
        if self.verify_detail is not None:
            result['VerifyDetail'] = self.verify_detail
        if self.verify_result is not None:
            result['VerifyResult'] = self.verify_result
        if self.vl_result is not None:
            result['VlResult'] = self.vl_result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaterialInfo') is not None:
            self.material_info = m.get('MaterialInfo')
        if m.get('OcrInfo') is not None:
            self.ocr_info = m.get('OcrInfo')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RiskScore') is not None:
            self.risk_score = m.get('RiskScore')
        if m.get('RiskTag') is not None:
            self.risk_tag = m.get('RiskTag')
        if m.get('VerifyDetail') is not None:
            self.verify_detail = m.get('VerifyDetail')
        if m.get('VerifyResult') is not None:
            self.verify_result = m.get('VerifyResult')
        if m.get('VlResult') is not None:
            temp_model = CredentialVerifyV2ResponseBodyResultObjectVlResult()
            self.vl_result = temp_model.from_map(m['VlResult'])
        return self


class CredentialVerifyV2ResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: CredentialVerifyV2ResponseBodyResultObject = None,
    ):
        # Return code: 200 for success, others for failure.
        self.code = code
        # Return message.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Returned result information.
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

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
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultObject') is not None:
            temp_model = CredentialVerifyV2ResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class CredentialVerifyV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CredentialVerifyV2ResponseBody = None,
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
            temp_model = CredentialVerifyV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeepfakeDetectRequest(TeaModel):
    def __init__(
        self,
        face_base_64: str = None,
        face_input_type: str = None,
        face_url: str = None,
        outer_order_no: str = None,
    ):
        # Enter the Base64 encoded string of the face image.
        # > Either FaceUrl or FaceBase64 must be provided.
        self.face_base_64 = face_base_64
        # Input **IMAGE** to indicate an image type.
        self.face_input_type = face_input_type
        # Enter the URL of the face image.
        # > Either FaceUrl or FaceBase64 must be provided.
        self.face_url = face_url
        # A unique identifier for the merchant\\"s request, consisting of a 32-character alphanumeric combination. The first few characters can be a custom abbreviation defined by the merchant, the middle part may include a timestamp, and the latter part can use a random or incrementing sequence.
        self.outer_order_no = outer_order_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_base_64 is not None:
            result['FaceBase64'] = self.face_base_64
        if self.face_input_type is not None:
            result['FaceInputType'] = self.face_input_type
        if self.face_url is not None:
            result['FaceUrl'] = self.face_url
        if self.outer_order_no is not None:
            result['OuterOrderNo'] = self.outer_order_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceBase64') is not None:
            self.face_base_64 = m.get('FaceBase64')
        if m.get('FaceInputType') is not None:
            self.face_input_type = m.get('FaceInputType')
        if m.get('FaceUrl') is not None:
            self.face_url = m.get('FaceUrl')
        if m.get('OuterOrderNo') is not None:
            self.outer_order_no = m.get('OuterOrderNo')
        return self


class DeepfakeDetectResponseBodyResultObject(TeaModel):
    def __init__(
        self,
        result: str = None,
        risk_score: Dict[str, str] = None,
        risk_tag: str = None,
    ):
        # Risk result:
        # 
        # - **0**: Low risk
        # - **1**: High risk
        # - **2**: Suspicious
        self.result = result
        # Risk score map.
        self.risk_score = risk_score
        # Risk tags. Multiple tags are separated by commas (,). Includes:
        # 
        # - Suspected deep forgery  SuspectDeepForgery
        # - Suspected synthetic attack  SuspectPSFace
        # - Suspected watermark  SuspectWarterMark
        # - Suspected black industry attack  SuspectTemple
        # - Suspected generated face  SuspectAIGC Face
        # - Suspected rephotographed face  SuspectRemake
        self.risk_tag = risk_tag

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.risk_score is not None:
            result['RiskScore'] = self.risk_score
        if self.risk_tag is not None:
            result['RiskTag'] = self.risk_tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RiskScore') is not None:
            self.risk_score = m.get('RiskScore')
        if m.get('RiskTag') is not None:
            self.risk_tag = m.get('RiskTag')
        return self


class DeepfakeDetectResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: DeepfakeDetectResponseBodyResultObject = None,
    ):
        # Return code: 200 indicates success, others indicate failure.
        self.code = code
        # Return message.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Returned result information.
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

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
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultObject') is not None:
            temp_model = DeepfakeDetectResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class DeepfakeDetectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeepfakeDetectResponseBody = None,
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
            temp_model = DeepfakeDetectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFaceVerifyResultRequest(TeaModel):
    def __init__(
        self,
        certify_id: str = None,
        delete_after_query: str = None,
    ):
        # Unique identifier for real-person authentication.
        self.certify_id = certify_id
        # Whether deletion depends on having already obtained relevant data from the corresponding authentication process.
        # 
        # - Y: Required. To successfully delete the related data, you must have obtained the processing result through the DescribeFaceVerify interface.
        # - N: Not required (default). For pure server-side API integration, you can directly pass N.
        self.delete_after_query = delete_after_query

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.delete_after_query is not None:
            result['DeleteAfterQuery'] = self.delete_after_query
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('DeleteAfterQuery') is not None:
            self.delete_after_query = m.get('DeleteAfterQuery')
        return self


class DeleteFaceVerifyResultResponseBodyResultObject(TeaModel):
    def __init__(
        self,
        certify_id: str = None,
        delete_result: str = None,
        fail_reason: str = None,
    ):
        # Unique identifier for real-person authentication.
        self.certify_id = certify_id
        # Deletion result. Possible values are as follows:
        # 
        # - Y: Deletion successful.
        # - N: Deletion failed.
        self.delete_result = delete_result
        # Reason for deletion failure
        # 
        # - NOT_DELETE_REPEATEDLY: Cannot be deleted repeatedly
        # - NEED_QUERY_VERIFY_RESULT: Need to query the verification result first, then delete
        self.fail_reason = fail_reason

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.delete_result is not None:
            result['DeleteResult'] = self.delete_result
        if self.fail_reason is not None:
            result['FailReason'] = self.fail_reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('DeleteResult') is not None:
            self.delete_result = m.get('DeleteResult')
        if m.get('FailReason') is not None:
            self.fail_reason = m.get('FailReason')
        return self


class DeleteFaceVerifyResultResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: DeleteFaceVerifyResultResponseBodyResultObject = None,
    ):
        # Return code: 200 for success, others for failure.
        self.code = code
        # Return message.
        self.message = message
        # ID of the request
        self.request_id = request_id
        # Returned result information.
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

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
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultObject') is not None:
            temp_model = DeleteFaceVerifyResultResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class DeleteFaceVerifyResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteFaceVerifyResultResponseBody = None,
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
            temp_model = DeleteFaceVerifyResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCardVerifyRequest(TeaModel):
    def __init__(
        self,
        certify_id: str = None,
    ):
        # Authentication request ID.
        # You must first call the initialization interface InitCardVerify to submit an authentication request in order to get the authentication request ID.
        # 
        # This parameter is required.
        self.certify_id = certify_id

    def validate(self):
        pass

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


class DescribeCardVerifyResponseBodyResultObject(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        card_info: str = None,
        face_detail: str = None,
        ocr_card_info: str = None,
        picture_info: str = None,
    ):
        # Identity verification result:
        # - 1: Consistent
        # - 2: Inconsistent
        # - 3: No Record Found
        self.biz_code = biz_code
        # Submitted ID card information for verification.
        self.card_info = card_info
        # Image comparison score.
        self.face_detail = face_detail
        # ID card information read by OCR.
        self.ocr_card_info = ocr_card_info
        # Returned photo URLs.
        # - certUrl  Front side
        # - certNationalUrl  National emblem side
        self.picture_info = picture_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.card_info is not None:
            result['CardInfo'] = self.card_info
        if self.face_detail is not None:
            result['FaceDetail'] = self.face_detail
        if self.ocr_card_info is not None:
            result['OcrCardInfo'] = self.ocr_card_info
        if self.picture_info is not None:
            result['PictureInfo'] = self.picture_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('CardInfo') is not None:
            self.card_info = m.get('CardInfo')
        if m.get('FaceDetail') is not None:
            self.face_detail = m.get('FaceDetail')
        if m.get('OcrCardInfo') is not None:
            self.ocr_card_info = m.get('OcrCardInfo')
        if m.get('PictureInfo') is not None:
            self.picture_info = m.get('PictureInfo')
        return self


class DescribeCardVerifyResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: DescribeCardVerifyResponseBodyResultObject = None,
    ):
        # Return code: 200 indicates success, all others indicate failure.
        # Important
        # - This parameter indicates whether the interface was called correctly. For detailed return code explanations, please refer to the error codes.
        # - Please check the business verification results through the fields in ResultObject.
        self.code = code
        # Interface call return message.
        # Important
        # - This parameter only indicates whether there was an exception with the interface.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Result object.
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

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
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultObject') is not None:
            temp_model = DescribeCardVerifyResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class DescribeCardVerifyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCardVerifyResponseBody = None,
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
            temp_model = DescribeCardVerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDeviceInfoRequest(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        current_page: int = None,
        device_id: str = None,
        expired_end_day: str = None,
        expired_start_day: str = None,
        page_size: int = None,
        user_device_id: str = None,
    ):
        # Business type. No more than 64 characters.
        self.biz_type = biz_type
        # The current page number being queried.
        self.current_page = current_page
        # A unique ID generated by the real-person authentication server for the access party\\"s device. This ID is only generated after the device has been successfully activated and can be obtained through the getLicenseExtraInfo function in the offline facial recognition SDK.
        self.device_id = device_id
        # The end time of the query, i.e., querying authorizations that will expire between ExpiredStartDay and ExpiredEndDay.
        self.expired_end_day = expired_end_day
        # The start time of the query, i.e., querying authorizations that will expire between ExpiredStartDay and ExpiredEndDay.
        self.expired_start_day = expired_start_day
        # Number of items per page in the query.
        self.page_size = page_size
        # No more than 64 characters, defined by the access party, which can be used to identify a specific device.
        self.user_device_id = user_device_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.expired_end_day is not None:
            result['ExpiredEndDay'] = self.expired_end_day
        if self.expired_start_day is not None:
            result['ExpiredStartDay'] = self.expired_start_day
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.user_device_id is not None:
            result['UserDeviceId'] = self.user_device_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('ExpiredEndDay') is not None:
            self.expired_end_day = m.get('ExpiredEndDay')
        if m.get('ExpiredStartDay') is not None:
            self.expired_start_day = m.get('ExpiredStartDay')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('UserDeviceId') is not None:
            self.user_device_id = m.get('UserDeviceId')
        return self


class DescribeDeviceInfoResponseBodyDeviceInfoListDeviceInfo(TeaModel):
    def __init__(
        self,
        begin_day: str = None,
        biz_type: str = None,
        device_id: str = None,
        expired_day: str = None,
        user_device_id: str = None,
    ):
        # Authorization start date.
        self.begin_day = begin_day
        # Corresponds to the BizType in the request.
        self.biz_type = biz_type
        # Corresponds to the DeviceId in the request.
        self.device_id = device_id
        # Authorization expiration date.
        self.expired_day = expired_day
        # Corresponds to the UserDeviceId in the request.
        self.user_device_id = user_device_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_day is not None:
            result['BeginDay'] = self.begin_day
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.expired_day is not None:
            result['ExpiredDay'] = self.expired_day
        if self.user_device_id is not None:
            result['UserDeviceId'] = self.user_device_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginDay') is not None:
            self.begin_day = m.get('BeginDay')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('ExpiredDay') is not None:
            self.expired_day = m.get('ExpiredDay')
        if m.get('UserDeviceId') is not None:
            self.user_device_id = m.get('UserDeviceId')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        current_page: int = None,
        device_info_list: DescribeDeviceInfoResponseBodyDeviceInfoList = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The current page number being queried.
        self.current_page = current_page
        # Array of device information.
        self.device_info_list = device_info_list
        # Number of items per page.
        self.page_size = page_size
        # The ID of this request.
        self.request_id = request_id
        # Total count.
        self.total_count = total_count

    def validate(self):
        if self.device_info_list:
            self.device_info_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.device_info_list is not None:
            result['DeviceInfoList'] = self.device_info_list.to_map()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DeviceInfoList') is not None:
            temp_model = DescribeDeviceInfoResponseBodyDeviceInfoList()
            self.device_info_list = temp_model.from_map(m['DeviceInfoList'])
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDeviceInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDeviceInfoResponseBody = None,
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
            temp_model = DescribeDeviceInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFaceGuardRiskRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        device_token: str = None,
        outer_order_no: str = None,
        product_code: str = None,
    ):
        # Authentication ID
        self.biz_id = biz_id
        # Risk identification - device token.
        self.device_token = device_token
        # This identifier is used for subsequent troubleshooting, and you need to ensure that this value is unique in your business.
        # 
        # Supports the use of English letters (including uppercase and lowercase) and numbers, with a maximum length of 32 characters.
        self.outer_order_no = outer_order_no
        # Product code, fixed value: FACE_GUARD
        self.product_code = product_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.device_token is not None:
            result['DeviceToken'] = self.device_token
        if self.outer_order_no is not None:
            result['OuterOrderNo'] = self.outer_order_no
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('DeviceToken') is not None:
            self.device_token = m.get('DeviceToken')
        if m.get('OuterOrderNo') is not None:
            self.outer_order_no = m.get('OuterOrderNo')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        return self


class DescribeFaceGuardRiskResponseBodyResultObject(TeaModel):
    def __init__(
        self,
        certify_id: str = None,
        risk_extends: str = None,
        risk_tags: str = None,
    ):
        # Unique real-person authentication identifier.
        self.certify_id = certify_id
        # Extended information, in JSON format. (Customized return based on tenant requirements)
        self.risk_extends = risk_extends
        # Device risk tags.
        # 
        # - Multiple device risk tags are separated by commas (,). For example, “ROOT,VPN,HOOK”,
        # 
        # - For more information about device risk tags and their meanings, please refer to the official documentation on Face Guard Tag Descriptions.
        self.risk_tags = risk_tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.risk_extends is not None:
            result['RiskExtends'] = self.risk_extends
        if self.risk_tags is not None:
            result['RiskTags'] = self.risk_tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('RiskExtends') is not None:
            self.risk_extends = m.get('RiskExtends')
        if m.get('RiskTags') is not None:
            self.risk_tags = m.get('RiskTags')
        return self


class DescribeFaceGuardRiskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: DescribeFaceGuardRiskResponseBodyResultObject = None,
    ):
        # Return code, **200** indicates successful response from the interface.
        self.code = code
        # Return message.
        self.message = message
        # ID of the request
        self.request_id = request_id
        # Returned result information.
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

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
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultObject') is not None:
            temp_model = DescribeFaceGuardRiskResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class DescribeFaceGuardRiskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFaceGuardRiskResponseBody = None,
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
            temp_model = DescribeFaceGuardRiskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFaceVerifyRequest(TeaModel):
    def __init__(
        self,
        certify_id: str = None,
        picture_return_type: str = None,
        scene_id: int = None,
    ):
        # Unique identifier for real-person authentication.
        self.certify_id = certify_id
        # Image return type.
        self.picture_return_type = picture_return_type
        # Authentication scene ID.
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.picture_return_type is not None:
            result['PictureReturnType'] = self.picture_return_type
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('PictureReturnType') is not None:
            self.picture_return_type = m.get('PictureReturnType')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class DescribeFaceVerifyResponseBodyResultObject(TeaModel):
    def __init__(
        self,
        device_risk: str = None,
        device_token: str = None,
        identity_info: str = None,
        material_info: str = None,
        passed: str = None,
        sub_code: str = None,
        success: str = None,
        user_info: str = None,
    ):
        # Device risk label.
        self.device_risk = device_risk
        # Device token.
        self.device_token = device_token
        # Information about the authenticated subject, usually empty in general authentication scenarios.
        self.identity_info = identity_info
        # Attachment information of the authenticated subject, mainly image materials. JSON format, see example below.
        self.material_info = material_info
        # Whether it passed, T for pass, F for fail.
        self.passed = passed
        # Description of the authentication result. For details, see the SubCode explanation below.
        self.sub_code = sub_code
        # Whether the response was successful.
        self.success = success
        # Records the identity information and corresponding encoding entered by the user under the rare character mode. The returned data is a JSON formatted string, which will be an empty string if there are no rare characters in the name.
        # 
        # - name: Refers to the name entered by the user.
        # 
        # - verifyName: Refers to the final name encoding after verification. For example, if a rare character is verified through transcoding: “Mr. Wang”, the actual verified name is “Wang Xiansheng”.
        # 
        # - number: Refers to the identification number entered by the user.
        self.user_info = user_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_risk is not None:
            result['DeviceRisk'] = self.device_risk
        if self.device_token is not None:
            result['DeviceToken'] = self.device_token
        if self.identity_info is not None:
            result['IdentityInfo'] = self.identity_info
        if self.material_info is not None:
            result['MaterialInfo'] = self.material_info
        if self.passed is not None:
            result['Passed'] = self.passed
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.success is not None:
            result['Success'] = self.success
        if self.user_info is not None:
            result['UserInfo'] = self.user_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceRisk') is not None:
            self.device_risk = m.get('DeviceRisk')
        if m.get('DeviceToken') is not None:
            self.device_token = m.get('DeviceToken')
        if m.get('IdentityInfo') is not None:
            self.identity_info = m.get('IdentityInfo')
        if m.get('MaterialInfo') is not None:
            self.material_info = m.get('MaterialInfo')
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('UserInfo') is not None:
            self.user_info = m.get('UserInfo')
        return self


class DescribeFaceVerifyResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: DescribeFaceVerifyResponseBodyResultObject = None,
    ):
        # Return code: 200 indicates success, other values indicate failure.
        self.code = code
        # Error message
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Returned result information
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

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
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultObject') is not None:
            temp_model = DescribeFaceVerifyResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class DescribeFaceVerifyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFaceVerifyResponseBody = None,
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
            temp_model = DescribeFaceVerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOssUploadTokenResponseBodyOssUploadToken(TeaModel):
    def __init__(
        self,
        bucket: str = None,
        end_point: str = None,
        expired: int = None,
        key: str = None,
        path: str = None,
        secret: str = None,
        token: str = None,
    ):
        # OSS bucket for file storage.
        self.bucket = bucket
        # Access endpoint.
        self.end_point = end_point
        # Expiration time.
        self.expired = expired
        # The Key required for file upload.
        self.key = key
        # File storage path.
        self.path = path
        # The Secret required for file upload.
        self.secret = secret
        # The Token required for file upload.
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.end_point is not None:
            result['EndPoint'] = self.end_point
        if self.expired is not None:
            result['Expired'] = self.expired
        if self.key is not None:
            result['Key'] = self.key
        if self.path is not None:
            result['Path'] = self.path
        if self.secret is not None:
            result['Secret'] = self.secret
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('EndPoint') is not None:
            self.end_point = m.get('EndPoint')
        if m.get('Expired') is not None:
            self.expired = m.get('Expired')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Secret') is not None:
            self.secret = m.get('Secret')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class DescribeOssUploadTokenResponseBody(TeaModel):
    def __init__(
        self,
        oss_upload_token: DescribeOssUploadTokenResponseBodyOssUploadToken = None,
        request_id: str = None,
    ):
        # Information about the OSS upload Token.
        self.oss_upload_token = oss_upload_token
        # The ID of this request.
        self.request_id = request_id

    def validate(self):
        if self.oss_upload_token:
            self.oss_upload_token.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss_upload_token is not None:
            result['OssUploadToken'] = self.oss_upload_token.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OssUploadToken') is not None:
            temp_model = DescribeOssUploadTokenResponseBodyOssUploadToken()
            self.oss_upload_token = temp_model.from_map(m['OssUploadToken'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeOssUploadTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeOssUploadTokenResponseBody = None,
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
            temp_model = DescribeOssUploadTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePageFaceVerifyDataRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        end_date: str = None,
        page_size: int = None,
        product_code: str = None,
        scene_id: int = None,
        start_date: str = None,
    ):
        # Current page number, default is 1.
        self.current_page = current_page
        # Required, end time, format is yyyy-MM-dd, default is yyyy-MM-dd 00:00:00, the query interval cannot exceed 90 days.
        self.end_date = end_date
        # Number of items per page, default is 10.
        self.page_size = page_size
        # Product code.
        self.product_code = product_code
        # Scene ID.
        self.scene_id = scene_id
        # Required, start time, format is yyyy-MM-dd, default is yyyy-MM-dd 00:00:00, the query interval cannot exceed 90 days.
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class DescribePageFaceVerifyDataResponseBodyItems(TeaModel):
    def __init__(
        self,
        date: str = None,
        product_code: str = None,
        scene_id: str = None,
        scene_name: str = None,
        success_count: str = None,
        total_count: str = None,
    ):
        # Date.
        self.date = date
        # Product scheme code, please refer to the financial-grade real-person help documentation.
        self.product_code = product_code
        # Scene ID.
        self.scene_id = scene_id
        # Scene name.
        self.scene_name = scene_name
        # Number of successful calls.
        self.success_count = success_count
        # Total count.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['Date'] = self.date
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name
        if self.success_count is not None:
            result['SuccessCount'] = self.success_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribePageFaceVerifyDataResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        current_page: str = None,
        items: List[DescribePageFaceVerifyDataResponseBodyItems] = None,
        message: str = None,
        page_size: str = None,
        request_id: str = None,
        success: str = None,
        total_count: str = None,
        total_page: str = None,
    ):
        # Return code
        self.code = code
        # Current page number.
        self.current_page = current_page
        # List of returned data.
        self.items = items
        # Return message.
        self.message = message
        # Number of items per page.
        self.page_size = page_size
        # ID of this request.
        self.request_id = request_id
        # Whether the response was successful.
        self.success = success
        # Total count.
        self.total_count = total_count
        # Total number of pages.
        self.total_page = total_page

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribePageFaceVerifyDataResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class DescribePageFaceVerifyDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribePageFaceVerifyDataResponseBody = None,
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
            temp_model = DescribePageFaceVerifyDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSmartStatisticsPageListRequest(TeaModel):
    def __init__(
        self,
        current_page: str = None,
        end_date: str = None,
        page_size: str = None,
        scene_id: str = None,
        service_code: str = None,
        start_date: str = None,
    ):
        # Current page number.
        # 
        # This parameter is required.
        self.current_page = current_page
        # End time, using UTC format, in the form of yyyy-MM-ddTHH:mm:ssZ.
        # 
        # This parameter is required.
        self.end_date = end_date
        # Number of items per page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # Scene ID.
        # 
        # This parameter is required.
        self.scene_id = scene_id
        # ServiceCode for the real person cloud product, only value: **cloudauthst**.
        self.service_code = service_code
        # Start time, using UTC format, in the form of yyyy-MM-ddTHH:mm:ssZ.
        # 
        # This parameter is required.
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class DescribeSmartStatisticsPageListResponseBodyItems(TeaModel):
    def __init__(
        self,
        date: str = None,
        pass_rate: str = None,
        product_code: str = None,
        scene_id: int = None,
        scene_name: str = None,
        success_count: int = None,
        total_count: int = None,
    ):
        # Date. Format: <i>month/day</i>
        self.date = date
        # Pass rate.
        self.pass_rate = pass_rate
        # Product solution Code, please refer to the Enhanced Real Person Help Documentation.
        self.product_code = product_code
        # Scene ID.
        self.scene_id = scene_id
        # Scene name.
        self.scene_name = scene_name
        # Number of successful calls.
        self.success_count = success_count
        # Total count.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['Date'] = self.date
        if self.pass_rate is not None:
            result['PassRate'] = self.pass_rate
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name
        if self.success_count is not None:
            result['SuccessCount'] = self.success_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('PassRate') is not None:
            self.pass_rate = m.get('PassRate')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeSmartStatisticsPageListResponseBody(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        items: List[DescribeSmartStatisticsPageListResponseBodyItems] = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        total_page: int = None,
    ):
        # Current page number.
        self.current_page = current_page
        # Returned data list.
        self.items = items
        # Number of items displayed per page.
        self.page_size = page_size
        # ID of this request.
        self.request_id = request_id
        # Total count.
        self.total_count = total_count
        # Total number of pages.
        self.total_page = total_page

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeSmartStatisticsPageListResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class DescribeSmartStatisticsPageListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSmartStatisticsPageListResponseBody = None,
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
            temp_model = DescribeSmartStatisticsPageListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVerifyResultRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_type: str = None,
    ):
        # Authentication ID. A unique ID that identifies an authentication task, not exceeding 64 characters. For a single authentication task, the system supports an unlimited number of submissions until the final authentication is successful and the task is completed. > You need to use a different BizId for each new authentication task.
        # 
        # This parameter is required.
        self.biz_id = biz_id
        # Business scenario identifier for real-person authentication service
        # 
        # This parameter is required.
        self.biz_type = biz_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        address: str = None,
        authority: str = None,
        back_image_url: str = None,
        birth: str = None,
        end_date: str = None,
        front_image_url: str = None,
        name: str = None,
        nationality: str = None,
        number: str = None,
        start_date: str = None,
    ):
        # Address.
        self.address = address
        # Issuing authority.
        self.authority = authority
        # HTTP/HTTPS link to the image of the back side (national emblem side) of the ID card. The link is valid for 5 minutes, and it is recommended to store it for business use to avoid any impact.
        # > If the HTTP/HTTPS link to the front-facing portrait image expires, you can call DescribeVerifyResult again to get the link.
        self.back_image_url = back_image_url
        # Date of birth.
        self.birth = birth
        # The end date of the document\\"s validity period. Format: yyyymmdd.
        self.end_date = end_date
        # HTTP/HTTPS link to the image of the front side (portrait side) of the ID card. The link is valid for 5 minutes, and it is recommended to store it for business use to avoid any impact.
        # > If the HTTP/HTTPS link to the front-facing portrait image expires, you can call DescribeVerifyResult again to get the link.
        self.front_image_url = front_image_url
        # Name.
        self.name = name
        # Nationality.
        self.nationality = nationality
        # ID card number.
        self.number = number
        # Start date of the document\\"s validity. Format: yyyymmdd.
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.authority is not None:
            result['Authority'] = self.authority
        if self.back_image_url is not None:
            result['BackImageUrl'] = self.back_image_url
        if self.birth is not None:
            result['Birth'] = self.birth
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.front_image_url is not None:
            result['FrontImageUrl'] = self.front_image_url
        if self.name is not None:
            result['Name'] = self.name
        if self.nationality is not None:
            result['Nationality'] = self.nationality
        if self.number is not None:
            result['Number'] = self.number
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Authority') is not None:
            self.authority = m.get('Authority')
        if m.get('BackImageUrl') is not None:
            self.back_image_url = m.get('BackImageUrl')
        if m.get('Birth') is not None:
            self.birth = m.get('Birth')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('FrontImageUrl') is not None:
            self.front_image_url = m.get('FrontImageUrl')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Nationality') is not None:
            self.nationality = m.get('Nationality')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class DescribeVerifyResultResponseBodyMaterial(TeaModel):
    def __init__(
        self,
        face_global_url: str = None,
        face_image_url: str = None,
        face_mask: bool = None,
        face_quality: str = None,
        id_card_info: DescribeVerifyResultResponseBodyMaterialIdCardInfo = None,
        id_card_name: str = None,
        id_card_number: str = None,
        video_urls: List[str] = None,
    ):
        # The global camera image captured by the real-person authentication SDK.
        # 
        # > This parameter will only take effect after configuration. If you need to use this parameter, please submit a [ticket](https://selfservice.console.aliyun.com/ticket/category/cloudauth/today) to contact us.
        self.face_global_url = face_global_url
        # The HTTP or HTTPS link to the frontal face image. The link is valid for 5 minutes, and it is recommended to store it elsewhere to avoid any impact on usage.
        # > If the HTTP or HTTPS link to the frontal face image expires, you can call [DescribeVerifyResult](https://help.aliyun.com/document_detail/154606.html) again to get the link.
        self.face_image_url = face_image_url
        # Whether the face is wearing a mask. Values:
        # - **true**: Wearing a mask
        # - **false**: Not wearing a mask
        self.face_mask = face_mask
        # The quality of the frontal face image. Values:
        # - **UNQUALIFIED**: Poor quality
        # - **LOW**: Low
        # - **NORMAL**: Normal
        # - **HIGH**: High
        self.face_quality = face_quality
        # OCR results of the ID card information.
        # > If there is no front and back information of the ID card during the authentication process, the real-person authentication service will not return the OCR results of the ID card. Even if there is front and back information of the ID card during the authentication process, the real-person authentication service does not guarantee to return all the information on the ID card. Due to issues with ID card photography, the OCR may fail to recognize some information, resulting in incomplete OCR information. It is recommended that your business does not strongly rely on the ID card OCR information.
        self.id_card_info = id_card_info
        # Name.
        self.id_card_name = id_card_name
        # ID number.
        self.id_card_number = id_card_number
        # The URL addresses of the recorded videos returned by the historical RPH5BioOnly solution.
        self.video_urls = video_urls

    def validate(self):
        if self.id_card_info:
            self.id_card_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_global_url is not None:
            result['FaceGlobalUrl'] = self.face_global_url
        if self.face_image_url is not None:
            result['FaceImageUrl'] = self.face_image_url
        if self.face_mask is not None:
            result['FaceMask'] = self.face_mask
        if self.face_quality is not None:
            result['FaceQuality'] = self.face_quality
        if self.id_card_info is not None:
            result['IdCardInfo'] = self.id_card_info.to_map()
        if self.id_card_name is not None:
            result['IdCardName'] = self.id_card_name
        if self.id_card_number is not None:
            result['IdCardNumber'] = self.id_card_number
        if self.video_urls is not None:
            result['VideoUrls'] = self.video_urls
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceGlobalUrl') is not None:
            self.face_global_url = m.get('FaceGlobalUrl')
        if m.get('FaceImageUrl') is not None:
            self.face_image_url = m.get('FaceImageUrl')
        if m.get('FaceMask') is not None:
            self.face_mask = m.get('FaceMask')
        if m.get('FaceQuality') is not None:
            self.face_quality = m.get('FaceQuality')
        if m.get('IdCardInfo') is not None:
            temp_model = DescribeVerifyResultResponseBodyMaterialIdCardInfo()
            self.id_card_info = temp_model.from_map(m['IdCardInfo'])
        if m.get('IdCardName') is not None:
            self.id_card_name = m.get('IdCardName')
        if m.get('IdCardNumber') is not None:
            self.id_card_number = m.get('IdCardNumber')
        if m.get('VideoUrls') is not None:
            self.video_urls = m.get('VideoUrls')
        return self


class DescribeVerifyResultResponseBody(TeaModel):
    def __init__(
        self,
        authority_comparision_score: float = None,
        face_comparison_score: float = None,
        id_card_face_comparison_score: float = None,
        material: DescribeVerifyResultResponseBodyMaterial = None,
        request_id: str = None,
        verify_status: int = None,
    ):
        # The comparison score between the face photo submitted during the authentication process and the authoritative data, with a value range of **0** to **100**.
        # Confidence threshold references:
        # - When the false acceptance rate is 0.001%, the corresponding threshold is 95. - When the false acceptance rate is 0.01%, the corresponding threshold is 90. - When the false acceptance rate is 0.1%, the corresponding threshold is 80. - When the false acceptance rate is 1%, the corresponding threshold is 60.
        # > This field only indicates the comparison result between the face and the authoritative data, for your reference only. It is generally not recommended to use this value alone as the standard for whether the authentication passes. For a comprehensive authentication result, please refer to the **VerifyStatus** field. The **VerifyStatus** result integrates the comparison of the face with the authoritative data and various other strategies, which can enhance security levels.
        self.authority_comparision_score = authority_comparision_score
        # The comparison score between the face photo submitted during the authentication process and the face in the retained face image. The value range is **0**~**100**.
        # 
        # Confidence threshold reference:
        # 
        # - When the false recognition rate is 0.001%, the corresponding threshold is 95.
        # - When the false recognition rate is 0.01%, the corresponding threshold is 90.
        # - When the false recognition rate is 0.1%, the corresponding threshold is 80.
        # - When the false recognition rate is 1%, the corresponding threshold is 60.
        self.face_comparison_score = face_comparison_score
        # The comparison score between the face photo submitted during the authentication process and the face on the ID card\\"s face side. The value range is **0**~**100**.
        # 
        # Confidence threshold reference:
        # 
        # - When the false recognition rate is 0.001%, the corresponding threshold is 95.
        # - When the false recognition rate is 0.01%, the corresponding threshold is 90.
        # - When the false recognition rate is 0.1%, the corresponding threshold is 80.
        # - When the false recognition rate is 1%, the corresponding threshold is 60.
        self.id_card_face_comparison_score = id_card_face_comparison_score
        # Authentication materials.
        self.material = material
        # The ID of this request.
        self.request_id = request_id
        # Authentication status, values:
        # - **-1**: Not authenticated - **1**: Authentication passed - **2** to **n**: Authentication failed for various reasons. For detailed descriptions, see the authentication status explanation.
        self.verify_status = verify_status

    def validate(self):
        if self.material:
            self.material.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authority_comparision_score is not None:
            result['AuthorityComparisionScore'] = self.authority_comparision_score
        if self.face_comparison_score is not None:
            result['FaceComparisonScore'] = self.face_comparison_score
        if self.id_card_face_comparison_score is not None:
            result['IdCardFaceComparisonScore'] = self.id_card_face_comparison_score
        if self.material is not None:
            result['Material'] = self.material.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.verify_status is not None:
            result['VerifyStatus'] = self.verify_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorityComparisionScore') is not None:
            self.authority_comparision_score = m.get('AuthorityComparisionScore')
        if m.get('FaceComparisonScore') is not None:
            self.face_comparison_score = m.get('FaceComparisonScore')
        if m.get('IdCardFaceComparisonScore') is not None:
            self.id_card_face_comparison_score = m.get('IdCardFaceComparisonScore')
        if m.get('Material') is not None:
            temp_model = DescribeVerifyResultResponseBodyMaterial()
            self.material = temp_model.from_map(m['Material'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VerifyStatus') is not None:
            self.verify_status = m.get('VerifyStatus')
        return self


class DescribeVerifyResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeVerifyResultResponseBody = None,
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
            temp_model = DescribeVerifyResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVerifySDKRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        # The task ID for generating the SDK.
        # 
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


class DescribeVerifySDKResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        sdk_url: str = None,
    ):
        # The ID of this request.
        self.request_id = request_id
        # The SDK download URL. When not empty, it indicates that the generation is complete.
        self.sdk_url = sdk_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sdk_url is not None:
            result['SdkUrl'] = self.sdk_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SdkUrl') is not None:
            self.sdk_url = m.get('SdkUrl')
        return self


class DescribeVerifySDKResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeVerifySDKResponseBody = None,
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
            temp_model = DescribeVerifySDKResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVerifyTokenRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_type: str = None,
        callback_seed: str = None,
        callback_url: str = None,
        face_retained_image_url: str = None,
        failed_redirect_url: str = None,
        id_card_back_image_url: str = None,
        id_card_front_image_url: str = None,
        id_card_number: str = None,
        name: str = None,
        passed_redirect_url: str = None,
        user_id: str = None,
        user_ip: str = None,
        user_phone_number: str = None,
        user_regist_time: int = None,
    ):
        # Verification ID. A unique ID that identifies a verification task, not exceeding 64 characters. For a single verification task, the system supports unlimited submissions until the final verification is passed and the task is completed.
        # 
        # > Different BizIds are required for different verification tasks.
        # 
        # This parameter is required.
        self.biz_id = biz_id
        # Identifier for the business scenario using the real person authentication service. Please refer to [Business Settings](https://help.aliyun.com/document_detail/127885.html) and complete the creation in the console first.
        # 
        # This parameter is required.
        self.biz_type = biz_type
        # Callback seed.
        self.callback_seed = callback_seed
        # Callback URL.
        self.callback_url = callback_url
        # HTTP or HTTPS link to the retained portrait photo.
        self.face_retained_image_url = face_retained_image_url
        # Redirect URL for failed verification.
        self.failed_redirect_url = failed_redirect_url
        # HTTP or HTTPS link to the national emblem side of the ID card image.
        self.id_card_back_image_url = id_card_back_image_url
        # HTTP or HTTPS link to the portrait side of the ID card image.
        self.id_card_front_image_url = id_card_front_image_url
        # ID card number.
        self.id_card_number = id_card_number
        # Name.
        self.name = name
        # Redirect URL upon successful verification.
        self.passed_redirect_url = passed_redirect_url
        # ID of the end user, such as the account ID of the end user.
        self.user_id = user_id
        # User IP.
        self.user_ip = user_ip
        # User phone number.
        self.user_phone_number = user_phone_number
        # User registration time. Expressed in timestamp format, unit: milliseconds.
        self.user_regist_time = user_regist_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.callback_seed is not None:
            result['CallbackSeed'] = self.callback_seed
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        if self.face_retained_image_url is not None:
            result['FaceRetainedImageUrl'] = self.face_retained_image_url
        if self.failed_redirect_url is not None:
            result['FailedRedirectUrl'] = self.failed_redirect_url
        if self.id_card_back_image_url is not None:
            result['IdCardBackImageUrl'] = self.id_card_back_image_url
        if self.id_card_front_image_url is not None:
            result['IdCardFrontImageUrl'] = self.id_card_front_image_url
        if self.id_card_number is not None:
            result['IdCardNumber'] = self.id_card_number
        if self.name is not None:
            result['Name'] = self.name
        if self.passed_redirect_url is not None:
            result['PassedRedirectUrl'] = self.passed_redirect_url
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_ip is not None:
            result['UserIp'] = self.user_ip
        if self.user_phone_number is not None:
            result['UserPhoneNumber'] = self.user_phone_number
        if self.user_regist_time is not None:
            result['UserRegistTime'] = self.user_regist_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('CallbackSeed') is not None:
            self.callback_seed = m.get('CallbackSeed')
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        if m.get('FaceRetainedImageUrl') is not None:
            self.face_retained_image_url = m.get('FaceRetainedImageUrl')
        if m.get('FailedRedirectUrl') is not None:
            self.failed_redirect_url = m.get('FailedRedirectUrl')
        if m.get('IdCardBackImageUrl') is not None:
            self.id_card_back_image_url = m.get('IdCardBackImageUrl')
        if m.get('IdCardFrontImageUrl') is not None:
            self.id_card_front_image_url = m.get('IdCardFrontImageUrl')
        if m.get('IdCardNumber') is not None:
            self.id_card_number = m.get('IdCardNumber')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PassedRedirectUrl') is not None:
            self.passed_redirect_url = m.get('PassedRedirectUrl')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
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
        bucket: str = None,
        end_point: str = None,
        expired: int = None,
        key: str = None,
        path: str = None,
        secret: str = None,
        token: str = None,
    ):
        # OSS file storage bucket.
        self.bucket = bucket
        # Access endpoint.
        self.end_point = end_point
        # Expiration time. Expressed in timestamp format, unit: milliseconds.
        self.expired = expired
        # The key required for file upload.
        self.key = key
        # File storage path.
        self.path = path
        # The secret required for file upload.
        self.secret = secret
        # The token required for file upload.
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.end_point is not None:
            result['EndPoint'] = self.end_point
        if self.expired is not None:
            result['Expired'] = self.expired
        if self.key is not None:
            result['Key'] = self.key
        if self.path is not None:
            result['Path'] = self.path
        if self.secret is not None:
            result['Secret'] = self.secret
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('EndPoint') is not None:
            self.end_point = m.get('EndPoint')
        if m.get('Expired') is not None:
            self.expired = m.get('Expired')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Secret') is not None:
            self.secret = m.get('Secret')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class DescribeVerifyTokenResponseBody(TeaModel):
    def __init__(
        self,
        oss_upload_token: DescribeVerifyTokenResponseBodyOssUploadToken = None,
        request_id: str = None,
        verify_page_url: str = None,
        verify_token: str = None,
    ):
        # OSS upload token information.
        self.oss_upload_token = oss_upload_token
        # The ID of this request.
        self.request_id = request_id
        # The entry link for the original H5 verification scheme, which has been discontinued and no longer supports new integrations. If you need to integrate an H5 verification scheme, it is recommended to use the [PC or mobile H5 web integration solution](https://help.aliyun.com/document_detail/173779.html) of financial-grade real-person authentication.
        self.verify_page_url = verify_page_url
        # The token for this verification, used to link various interfaces in the verification request, valid for 30 minutes.
        self.verify_token = verify_token

    def validate(self):
        if self.oss_upload_token:
            self.oss_upload_token.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss_upload_token is not None:
            result['OssUploadToken'] = self.oss_upload_token.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.verify_page_url is not None:
            result['VerifyPageUrl'] = self.verify_page_url
        if self.verify_token is not None:
            result['VerifyToken'] = self.verify_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OssUploadToken') is not None:
            temp_model = DescribeVerifyTokenResponseBodyOssUploadToken()
            self.oss_upload_token = temp_model.from_map(m['OssUploadToken'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VerifyPageUrl') is not None:
            self.verify_page_url = m.get('VerifyPageUrl')
        if m.get('VerifyToken') is not None:
            self.verify_token = m.get('VerifyToken')
        return self


class DescribeVerifyTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeVerifyTokenResponseBody = None,
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
            temp_model = DescribeVerifyTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectFaceAttributesRequest(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        material_value: str = None,
    ):
        # Identifier for the business scenario using real-person authentication services.
        self.biz_type = biz_type
        # The photo to be detected, see the instructions for uploading image addresses for format description. A maximum of 5 faces can be detected in a single image.
        # 
        # This parameter is required.
        self.material_value = material_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.material_value is not None:
            result['MaterialValue'] = self.material_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('MaterialValue') is not None:
            self.material_value = m.get('MaterialValue')
        return self


class DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceAttributesHeadpose(TeaModel):
    def __init__(
        self,
        pitch_angle: float = None,
        roll_angle: float = None,
        yaw_angle: float = None,
    ):
        # Pitch angle, in degrees.
        self.pitch_angle = pitch_angle
        # Roll angle, in degrees.
        self.roll_angle = roll_angle
        # Yaw angle, in degrees.
        self.yaw_angle = yaw_angle

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceAttributesSmiling(TeaModel):
    def __init__(
        self,
        threshold: float = None,
        value: float = None,
    ):
        # Smile threshold.
        self.threshold = threshold
        # Smile score.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceAttributes(TeaModel):
    def __init__(
        self,
        blur: float = None,
        facequal: float = None,
        facetype: str = None,
        glasses: str = None,
        headpose: DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceAttributesHeadpose = None,
        integrity: int = None,
        respirator: str = None,
        smiling: DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceAttributesSmiling = None,
    ):
        # Face blur level, with higher values indicating more blurriness. Typically, a value ≥2.0 is considered quite blurry. It is recommended to adjust based on actual business data testing.
        self.blur = blur
        # A score ranging from 0 to 100. The higher the score, the better the quality. It is recommended to consider a score of 50 or above as acceptable quality.
        self.facequal = facequal
        # Whether it is a human face. Values:
        # 
        # - **None**: Not a human face
        # - **Face**: Human face
        # - **Profile**: Profile (head turned left or right by more than 30°)
        # 
        # > If no face is detected, the `faceInfos` in the response will be empty; here, `None` means that a face was detected but is considered to be a cartoon, pet, etc.
        self.facetype = facetype
        # Whether wearing glasses. Values:
        # 
        # - **None**: Not wearing glasses
        # - **Wear**: Wearing regular glasses
        # - **Sunglass**: Wearing sunglasses
        self.glasses = glasses
        # Face pose.
        self.headpose = headpose
        # A score ranging from 0 to 100. The higher the score, the more complete the face. It is recommended to consider a score of 70 or above as acceptable completeness.
        self.integrity = integrity
        # Whether wearing a mask. Values:
        # 
        # - Wear: Wearing a mask.
        # - None: Not wearing a mask.
        self.respirator = respirator
        # Whether smiling.
        self.smiling = smiling

    def validate(self):
        if self.headpose:
            self.headpose.validate()
        if self.smiling:
            self.smiling.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.blur is not None:
            result['Blur'] = self.blur
        if self.facequal is not None:
            result['Facequal'] = self.facequal
        if self.facetype is not None:
            result['Facetype'] = self.facetype
        if self.glasses is not None:
            result['Glasses'] = self.glasses
        if self.headpose is not None:
            result['Headpose'] = self.headpose.to_map()
        if self.integrity is not None:
            result['Integrity'] = self.integrity
        if self.respirator is not None:
            result['Respirator'] = self.respirator
        if self.smiling is not None:
            result['Smiling'] = self.smiling.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Blur') is not None:
            self.blur = m.get('Blur')
        if m.get('Facequal') is not None:
            self.facequal = m.get('Facequal')
        if m.get('Facetype') is not None:
            self.facetype = m.get('Facetype')
        if m.get('Glasses') is not None:
            self.glasses = m.get('Glasses')
        if m.get('Headpose') is not None:
            temp_model = DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceAttributesHeadpose()
            self.headpose = temp_model.from_map(m['Headpose'])
        if m.get('Integrity') is not None:
            self.integrity = m.get('Integrity')
        if m.get('Respirator') is not None:
            self.respirator = m.get('Respirator')
        if m.get('Smiling') is not None:
            temp_model = DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceAttributesSmiling()
            self.smiling = temp_model.from_map(m['Smiling'])
        return self


class DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceRect(TeaModel):
    def __init__(
        self,
        height: int = None,
        left: int = None,
        top: int = None,
        width: int = None,
    ):
        # Height of the face rectangle.
        self.height = height
        # Distance from the top-left corner of the face rectangle to the left edge of the original image, in pixels.
        self.left = left
        # Distance from the top-left corner of the face rectangle to the top edge of the original image, in pixels.
        self.top = top
        # Width of the face rectangle.
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


class DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfo(TeaModel):
    def __init__(
        self,
        face_attributes: DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceAttributes = None,
        face_rect: DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceRect = None,
    ):
        # Face attributes.
        self.face_attributes = face_attributes
        # Position of the face in the original image.
        self.face_rect = face_rect

    def validate(self):
        if self.face_attributes:
            self.face_attributes.validate()
        if self.face_rect:
            self.face_rect.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        face_infos: DetectFaceAttributesResponseBodyDataFaceInfos = None,
        img_height: int = None,
        img_width: int = None,
    ):
        # Face detection results.
        self.face_infos = face_infos
        # Original image height, in pixels.
        self.img_height = img_height
        # Original image width, in pixels.
        self.img_width = img_width

    def validate(self):
        if self.face_infos:
            self.face_infos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_infos is not None:
            result['FaceInfos'] = self.face_infos.to_map()
        if self.img_height is not None:
            result['ImgHeight'] = self.img_height
        if self.img_width is not None:
            result['ImgWidth'] = self.img_width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceInfos') is not None:
            temp_model = DetectFaceAttributesResponseBodyDataFaceInfos()
            self.face_infos = temp_model.from_map(m['FaceInfos'])
        if m.get('ImgHeight') is not None:
            self.img_height = m.get('ImgHeight')
        if m.get('ImgWidth') is not None:
            self.img_width = m.get('ImgWidth')
        return self


class DetectFaceAttributesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DetectFaceAttributesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # HTTP status code.
        self.code = code
        # Returned data.
        self.data = data
        # Error code.
        self.message = message
        # ID of this request.
        self.request_id = request_id
        # Whether the response was successful.
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
        if m.get('Data') is not None:
            temp_model = DetectFaceAttributesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DetectFaceAttributesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetectFaceAttributesResponseBody = None,
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
            temp_model = DetectFaceAttributesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class Id2MetaPeriodVerifyRequest(TeaModel):
    def __init__(
        self,
        identify_num: str = None,
        param_type: str = None,
        user_name: str = None,
        validity_end_date: str = None,
        validity_start_date: str = None,
    ):
        # ID number:
        # 
        # - When `paramType` is `normal`: Enter the plain text of the ID number.
        # - When `paramType` is `md5`:
        # The first 6 digits (plain text) + date of birth (encrypted) + last 4 digits (plain text).
        self.identify_num = identify_num
        # Parameter type:
        # 
        # - normal: Unencrypted.
        # - md5: MD5 encrypted.
        self.param_type = param_type
        # Name.
        # 
        # - When `paramType` = `normal`: Enter the plain text of the name.
        # - When `paramType` = `md5`: The first character of the name MD5 encrypted (32 lowercase MD5) + the rest of the name in plain text.
        self.user_name = user_name
        # End date of ID validity, format: YYYYMMDD
        self.validity_end_date = validity_end_date
        # Start date of ID validity, format: YYYYMMDD
        self.validity_start_date = validity_start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identify_num is not None:
            result['IdentifyNum'] = self.identify_num
        if self.param_type is not None:
            result['ParamType'] = self.param_type
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.validity_end_date is not None:
            result['ValidityEndDate'] = self.validity_end_date
        if self.validity_start_date is not None:
            result['ValidityStartDate'] = self.validity_start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdentifyNum') is not None:
            self.identify_num = m.get('IdentifyNum')
        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('ValidityEndDate') is not None:
            self.validity_end_date = m.get('ValidityEndDate')
        if m.get('ValidityStartDate') is not None:
            self.validity_start_date = m.get('ValidityStartDate')
        return self


class Id2MetaPeriodVerifyResponseBodyResultObject(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
    ):
        # Verification result code:
        # - **1**: Verification consistent.
        # - **2**: Verification inconsistent.
        # - **3**: No record found.
        self.biz_code = biz_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        return self


class Id2MetaPeriodVerifyResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: Id2MetaPeriodVerifyResponseBodyResultObject = None,
    ):
        # Return code: 200 for success, others for failure.
        self.code = code
        # Return message.
        self.message = message
        # ID of the request
        self.request_id = request_id
        # Returned result information.
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

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
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultObject') is not None:
            temp_model = Id2MetaPeriodVerifyResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class Id2MetaPeriodVerifyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Id2MetaPeriodVerifyResponseBody = None,
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
            temp_model = Id2MetaPeriodVerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class Id2MetaStandardVerifyRequest(TeaModel):
    def __init__(
        self,
        identify_num: str = None,
        param_type: str = None,
        user_name: str = None,
    ):
        # ID number:
        # 
        # - When `paramType` is normal: enter the plain text of the ID number.
        # - When `paramType` is md5:
        # The first 6 digits (plain text) + date of birth (encrypted) + last 4 digits (plain text).
        self.identify_num = identify_num
        # Parameter type:
        # 
        # - normal: unencrypted.
        # - md5: md5 encrypted.
        self.param_type = param_type
        # Name:
        # 
        # - When `paramType` is normal: enter the plain text of the name.
        # - When `paramType` is md5: the first character of the name (encrypted) + the rest of the name (plain text).
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identify_num is not None:
            result['IdentifyNum'] = self.identify_num
        if self.param_type is not None:
            result['ParamType'] = self.param_type
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdentifyNum') is not None:
            self.identify_num = m.get('IdentifyNum')
        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class Id2MetaStandardVerifyResponseBodyResultObject(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
    ):
        # Verification result code:
        # - **1**: verification matches.
        # - **2**: verification does not match.
        # - **3**: no record found.
        self.biz_code = biz_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        return self


class Id2MetaStandardVerifyResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: Id2MetaStandardVerifyResponseBodyResultObject = None,
    ):
        # Return code: 200 for success, others for failure.
        self.code = code
        # Return message.
        self.message = message
        # ID of the request
        self.request_id = request_id
        # Returned result information.
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

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
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultObject') is not None:
            temp_model = Id2MetaStandardVerifyResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class Id2MetaStandardVerifyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Id2MetaStandardVerifyResponseBody = None,
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
            temp_model = Id2MetaStandardVerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class Id2MetaVerifyRequest(TeaModel):
    def __init__(
        self,
        identify_num: str = None,
        param_type: str = None,
        user_name: str = None,
    ):
        # ID number:
        # 
        # Note
        # Only supports the ID numbers of second-generation resident IDs and Hong Kong, Macao, and Taiwan residence permits.
        # 
        # - When paramType is normal: enter the plaintext ID number.
        # 
        # - When paramType is md5: first 6 digits of the ID number (plaintext) + date of birth (ciphertext) + last 4 digits of the ID number (plaintext).
        self.identify_num = identify_num
        # Encryption method:
        # 
        # - normal: plaintext, no encryption
        # 
        # - md5: MD5 encryption
        self.param_type = param_type
        # Name:
        # 
        # - When paramType is normal: enter the plaintext name.
        # 
        # - When paramType is md5: first character of the name in ciphertext + rest of the name in plaintext.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identify_num is not None:
            result['IdentifyNum'] = self.identify_num
        if self.param_type is not None:
            result['ParamType'] = self.param_type
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdentifyNum') is not None:
            self.identify_num = m.get('IdentifyNum')
        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class Id2MetaVerifyResponseBodyResultObject(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
    ):
        # Verification result code:
        # - **1**: Verification consistent.
        # - **2**: Verification inconsistent.
        # - **3**: No record found.
        self.biz_code = biz_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        return self


class Id2MetaVerifyResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: Id2MetaVerifyResponseBodyResultObject = None,
    ):
        # Return code, **200** indicates successful API response.
        self.code = code
        # Return message.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Returned result information.
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

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
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultObject') is not None:
            temp_model = Id2MetaVerifyResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class Id2MetaVerifyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Id2MetaVerifyResponseBody = None,
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
            temp_model = Id2MetaVerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class Id2MetaVerifyWithOCRRequest(TeaModel):
    def __init__(
        self,
        cert_file: str = None,
        cert_national_file: str = None,
        cert_national_url: str = None,
        cert_url: str = None,
    ):
        # Input stream for the portrait side of the ID card image.
        # Choose one between CertUrl and CertFile.
        self.cert_file = cert_file
        # National emblem side of the ID card image address.
        # Choose one between CertNationalUrl and CertNationalFile, or omit both.
        self.cert_national_file = cert_national_file
        # National emblem side of the ID card image URL. National emblem side
        # A publicly accessible HTTP or HTTPS link.
        # Choose one between CertNationalUrl and CertNationalFile, or omit both.
        self.cert_national_url = cert_national_url
        # Portrait side of the ID card image.
        # A publicly accessible HTTP or HTTPS link.
        # Choose one between CertUrl and CertFile.
        self.cert_url = cert_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_file is not None:
            result['CertFile'] = self.cert_file
        if self.cert_national_file is not None:
            result['CertNationalFile'] = self.cert_national_file
        if self.cert_national_url is not None:
            result['CertNationalUrl'] = self.cert_national_url
        if self.cert_url is not None:
            result['CertUrl'] = self.cert_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertFile') is not None:
            self.cert_file = m.get('CertFile')
        if m.get('CertNationalFile') is not None:
            self.cert_national_file = m.get('CertNationalFile')
        if m.get('CertNationalUrl') is not None:
            self.cert_national_url = m.get('CertNationalUrl')
        if m.get('CertUrl') is not None:
            self.cert_url = m.get('CertUrl')
        return self


class Id2MetaVerifyWithOCRAdvanceRequest(TeaModel):
    def __init__(
        self,
        cert_file_object: BinaryIO = None,
        cert_national_file_object: BinaryIO = None,
        cert_national_url: str = None,
        cert_url: str = None,
    ):
        # Input stream for the portrait side of the ID card image.
        # Choose one between CertUrl and CertFile.
        self.cert_file_object = cert_file_object
        # National emblem side of the ID card image address.
        # Choose one between CertNationalUrl and CertNationalFile, or omit both.
        self.cert_national_file_object = cert_national_file_object
        # National emblem side of the ID card image URL. National emblem side
        # A publicly accessible HTTP or HTTPS link.
        # Choose one between CertNationalUrl and CertNationalFile, or omit both.
        self.cert_national_url = cert_national_url
        # Portrait side of the ID card image.
        # A publicly accessible HTTP or HTTPS link.
        # Choose one between CertUrl and CertFile.
        self.cert_url = cert_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_file_object is not None:
            result['CertFile'] = self.cert_file_object
        if self.cert_national_file_object is not None:
            result['CertNationalFile'] = self.cert_national_file_object
        if self.cert_national_url is not None:
            result['CertNationalUrl'] = self.cert_national_url
        if self.cert_url is not None:
            result['CertUrl'] = self.cert_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertFile') is not None:
            self.cert_file_object = m.get('CertFile')
        if m.get('CertNationalFile') is not None:
            self.cert_national_file_object = m.get('CertNationalFile')
        if m.get('CertNationalUrl') is not None:
            self.cert_national_url = m.get('CertNationalUrl')
        if m.get('CertUrl') is not None:
            self.cert_url = m.get('CertUrl')
        return self


class Id2MetaVerifyWithOCRResponseBodyResultObject(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        card_info: str = None,
    ):
        # Identity verification result:
        # - 1: Consistent
        # - 2: Inconsistent
        # - 3: No record found
        self.biz_code = biz_code
        # {"address":"Zhejiang Province, Hangzhou City, Yu*****","birthDate":"19901226","certName":"Zhang San","certNo":"1234561990122*****","nationality":"Han","authority":"xxx Public Security Bureau","startDate":"20201130","endDate":"20301130"}
        self.card_info = card_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.card_info is not None:
            result['CardInfo'] = self.card_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('CardInfo') is not None:
            self.card_info = m.get('CardInfo')
        return self


class Id2MetaVerifyWithOCRResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: Id2MetaVerifyWithOCRResponseBodyResultObject = None,
    ):
        # Return code: 200 indicates success, any other value indicates failure.
        # **Important**\
        # - This parameter indicates whether the API was called correctly. For detailed return code explanations, please refer to the error codes.
        # - Check the business verification results through the fields in ResultObject.
        self.code = code
        # API call return message.
        # **Important**\
        # This parameter only indicates if there was an exception with the API call.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Result object
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

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
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultObject') is not None:
            temp_model = Id2MetaVerifyWithOCRResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class Id2MetaVerifyWithOCRResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Id2MetaVerifyWithOCRResponseBody = None,
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
            temp_model = Id2MetaVerifyWithOCRResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class Id3MetaVerifyRequest(TeaModel):
    def __init__(
        self,
        crop: str = None,
        face_file: str = None,
        face_url: str = None,
        identify_num: str = None,
        param_type: str = None,
        user_name: str = None,
    ):
        # Whether to allow cropping of the face image, default is not allowed.
        # - T: Allow cropping.
        # - F: Do not allow cropping.
        # 
        # **Note**\
        # 
        # If the image you request is not collected from a standard liveness detection SDK, it is recommended to allow cropping of the face image. After enabling this feature, the system will first crop and correct the requested image, then initiate the service request.
        self.crop = crop
        # Portrait side of the ID card image input stream.
        # Choose one between `CertUrl` and `CertFile`.
        self.face_file = face_file
        # Portrait side of the ID card image.
        # Accessible HTTP or HTTPS link on the public network.
        # Choose one between `CertUrl` and `CertFile`.
        self.face_url = face_url
        # ID number:
        # - When `paramType` is `normal`: enter the plaintext ID number.
        # - When `paramType` is `md5`:
        # The first 6 digits (plaintext) + date of birth (ciphertext) + last 4 digits (plaintext).
        self.identify_num = identify_num
        # Encryption method:
        # - normal: plaintext without encryption
        # - md5: MD5 encryption
        # 
        # **Important**\
        # 
        # - All encrypted parameters should be in the form of a 32-character lowercase MD5 string.
        # - The ciphertext generated by different MD5 tools may vary. If the interface works before encryption but not after, try changing the MD5 tool.
        self.param_type = param_type
        # Name:
        # - When `paramType` is `normal`: enter the plaintext name.
        # - When `paramType` is `md5`: the first character of the name (ciphertext) + the rest of the name (plaintext).
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.crop is not None:
            result['Crop'] = self.crop
        if self.face_file is not None:
            result['FaceFile'] = self.face_file
        if self.face_url is not None:
            result['FaceUrl'] = self.face_url
        if self.identify_num is not None:
            result['IdentifyNum'] = self.identify_num
        if self.param_type is not None:
            result['ParamType'] = self.param_type
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Crop') is not None:
            self.crop = m.get('Crop')
        if m.get('FaceFile') is not None:
            self.face_file = m.get('FaceFile')
        if m.get('FaceUrl') is not None:
            self.face_url = m.get('FaceUrl')
        if m.get('IdentifyNum') is not None:
            self.identify_num = m.get('IdentifyNum')
        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class Id3MetaVerifyAdvanceRequest(TeaModel):
    def __init__(
        self,
        crop: str = None,
        face_file_object: BinaryIO = None,
        face_url: str = None,
        identify_num: str = None,
        param_type: str = None,
        user_name: str = None,
    ):
        # Whether to allow cropping of the face image, default is not allowed.
        # - T: Allow cropping.
        # - F: Do not allow cropping.
        # 
        # **Note**\
        # 
        # If the image you request is not collected from a standard liveness detection SDK, it is recommended to allow cropping of the face image. After enabling this feature, the system will first crop and correct the requested image, then initiate the service request.
        self.crop = crop
        # Portrait side of the ID card image input stream.
        # Choose one between `CertUrl` and `CertFile`.
        self.face_file_object = face_file_object
        # Portrait side of the ID card image.
        # Accessible HTTP or HTTPS link on the public network.
        # Choose one between `CertUrl` and `CertFile`.
        self.face_url = face_url
        # ID number:
        # - When `paramType` is `normal`: enter the plaintext ID number.
        # - When `paramType` is `md5`:
        # The first 6 digits (plaintext) + date of birth (ciphertext) + last 4 digits (plaintext).
        self.identify_num = identify_num
        # Encryption method:
        # - normal: plaintext without encryption
        # - md5: MD5 encryption
        # 
        # **Important**\
        # 
        # - All encrypted parameters should be in the form of a 32-character lowercase MD5 string.
        # - The ciphertext generated by different MD5 tools may vary. If the interface works before encryption but not after, try changing the MD5 tool.
        self.param_type = param_type
        # Name:
        # - When `paramType` is `normal`: enter the plaintext name.
        # - When `paramType` is `md5`: the first character of the name (ciphertext) + the rest of the name (plaintext).
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.crop is not None:
            result['Crop'] = self.crop
        if self.face_file_object is not None:
            result['FaceFile'] = self.face_file_object
        if self.face_url is not None:
            result['FaceUrl'] = self.face_url
        if self.identify_num is not None:
            result['IdentifyNum'] = self.identify_num
        if self.param_type is not None:
            result['ParamType'] = self.param_type
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Crop') is not None:
            self.crop = m.get('Crop')
        if m.get('FaceFile') is not None:
            self.face_file_object = m.get('FaceFile')
        if m.get('FaceUrl') is not None:
            self.face_url = m.get('FaceUrl')
        if m.get('IdentifyNum') is not None:
            self.identify_num = m.get('IdentifyNum')
        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class Id3MetaVerifyResponseBodyResultObject(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        face_detail: str = None,
    ):
        # Identity verification result:
        # 
        # - 1: Consistent
        # - 2: Inconsistent
        # - 3: No record found
        self.biz_code = biz_code
        # Image comparison score.
        self.face_detail = face_detail

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.face_detail is not None:
            result['FaceDetail'] = self.face_detail
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('FaceDetail') is not None:
            self.face_detail = m.get('FaceDetail')
        return self


class Id3MetaVerifyResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: Id3MetaVerifyResponseBodyResultObject = None,
    ):
        # Return code: 200 indicates success, others indicate failure.
        # **Important**\
        # - This parameter indicates whether the interface was called correctly. For detailed return code explanations, please refer to the error codes.
        # - Check the business verification result through the fields in `ResultObject`.
        self.code = code
        # Interface call return message.
        # 
        # **Important**\
        # 
        # This parameter only indicates whether there was an exception with the interface.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Result object.
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

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
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultObject') is not None:
            temp_model = Id3MetaVerifyResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class Id3MetaVerifyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Id3MetaVerifyResponseBody = None,
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
            temp_model = Id3MetaVerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InitCardVerifyRequest(TeaModel):
    def __init__(
        self,
        callback_token: str = None,
        callback_url: str = None,
        card_page_number: str = None,
        card_type: str = None,
        doc_scan_mode: str = None,
        merchant_biz_id: str = None,
        meta_info: str = None,
        model: str = None,
        picture_save: str = None,
        verify_meta: str = None,
    ):
        # Security Token, used for anti-replay and anti-tampering checks. If this parameter is passed, the CallbackToken field will be displayed in the callback address.
        self.callback_token = callback_token
        # - The callback notification address for the authentication result, which must start with https.
        # - The platform will call back this address after completing the authentication and automatically add the certifyId and passed fields, example: https://www.aliyun.com?certifyId=xxxx&passed=T
        # - Warning
        # The callback is triggered only when the authentication is completed. If the authentication is abandoned, interrupted abnormally, or not performed, no notification will be sent. It is recommended that when you receive the callback notification, if necessary, you can obtain detailed authentication information through the query interface.
        self.callback_url = callback_url
        # Number of card pages collected by the SDK
        # - You can input 1 or 2; input 1 to collect the front side, input 2 to collect both the front and back sides.
        # 
        # - If the verification type is ID period (VerifyMeta value is ID_PERIOD), you must input 2.
        # 
        # This parameter is required.
        self.card_page_number = card_page_number
        # Type of identification
        # - Resident Second Generation ID Card: IDENTITY_CARD
        # 
        # This parameter is required.
        self.card_type = card_type
        # Enumeration of photo-taking methods (manual/auto)
        # - Take a photo: shoot
        # - Scan: scan 
        # - Auto switch: auto
        self.doc_scan_mode = doc_scan_mode
        # A unique business identifier you define, used for subsequent troubleshooting.
        # Supports a combination of 32 alphanumeric characters, please ensure uniqueness.
        # 
        # This parameter is required.
        self.merchant_biz_id = merchant_biz_id
        # MetaInfo environment parameter, which needs to be obtained through the client SDK.
        # 
        # This parameter is required.
        self.meta_info = meta_info
        # Verification method, value:
        # - OCR_VERIFY: OCR recognition and verification mode.
        # 
        # This parameter is required.
        self.model = model
        # Whether to temporarily store the images collected by the app.
        # - Y: Yes
        # - N: No
        # - If \\"Yes\\" is selected here, the query interface will support returning the card image information.
        # 
        # This parameter is required.
        self.picture_save = picture_save
        # Verification type, value:
        # - Identity two elements (name + ID number): ID_2_META
        # 
        # This parameter is required.
        self.verify_meta = verify_meta

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.callback_token is not None:
            result['CallbackToken'] = self.callback_token
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        if self.card_page_number is not None:
            result['CardPageNumber'] = self.card_page_number
        if self.card_type is not None:
            result['CardType'] = self.card_type
        if self.doc_scan_mode is not None:
            result['DocScanMode'] = self.doc_scan_mode
        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id
        if self.meta_info is not None:
            result['MetaInfo'] = self.meta_info
        if self.model is not None:
            result['Model'] = self.model
        if self.picture_save is not None:
            result['PictureSave'] = self.picture_save
        if self.verify_meta is not None:
            result['VerifyMeta'] = self.verify_meta
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallbackToken') is not None:
            self.callback_token = m.get('CallbackToken')
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        if m.get('CardPageNumber') is not None:
            self.card_page_number = m.get('CardPageNumber')
        if m.get('CardType') is not None:
            self.card_type = m.get('CardType')
        if m.get('DocScanMode') is not None:
            self.doc_scan_mode = m.get('DocScanMode')
        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')
        if m.get('MetaInfo') is not None:
            self.meta_info = m.get('MetaInfo')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('PictureSave') is not None:
            self.picture_save = m.get('PictureSave')
        if m.get('VerifyMeta') is not None:
            self.verify_meta = m.get('VerifyMeta')
        return self


class InitCardVerifyResponseBodyResultObject(TeaModel):
    def __init__(
        self,
        certify_id: str = None,
    ):
        # Verification request ID, a unique identifier for the verification service\\"s authentication request.
        # - When querying the authentication result, the authentication request ID must be provided.
        # 
        # - The CertifyId field is a billing statistics field. To facilitate subsequent bill reconciliation, please retain this field information locally. The CertifyId returned by the initialization interface is valid for 30 minutes and can only be submitted once for authentication. Please apply it within the validity period to avoid reuse.
        self.certify_id = certify_id

    def validate(self):
        pass

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


class InitCardVerifyResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: InitCardVerifyResponseBodyResultObject = None,
    ):
        # Return code: 200 for success, others for failure.
        # Important
        # - This parameter indicates whether the interface was called correctly. For detailed return code descriptions, see the error codes.
        # - Business results should be viewed through the fields in ResultObject.
        self.code = code
        # Return message.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Return result.
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

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
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultObject') is not None:
            temp_model = InitCardVerifyResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class InitCardVerifyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InitCardVerifyResponseBody = None,
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
            temp_model = InitCardVerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InitFaceVerifyRequest(TeaModel):
    def __init__(
        self,
        app_quality_check: str = None,
        auth_id: str = None,
        birthday: str = None,
        callback_token: str = None,
        callback_url: str = None,
        camera_selection: str = None,
        cert_name: str = None,
        cert_no: str = None,
        cert_type: str = None,
        certify_id: str = None,
        certify_url_style: str = None,
        certify_url_type: str = None,
        crop: str = None,
        encrypt_type: str = None,
        face_contrast_picture: str = None,
        face_contrast_picture_url: str = None,
        face_guard_output: str = None,
        ip: str = None,
        meta_info: str = None,
        mobile: str = None,
        mode: str = None,
        model: str = None,
        need_multi_face_check: str = None,
        oss_bucket_name: str = None,
        oss_object_name: str = None,
        outer_order_no: str = None,
        procedure_priority: str = None,
        product_code: str = None,
        rarely_characters: str = None,
        read_img: str = None,
        return_url: str = None,
        scene_id: int = None,
        suitable_type: str = None,
        ui_custom_url: str = None,
        user_id: str = None,
        validity_date: str = None,
        video_evidence: str = None,
        voluntary_customized_content: str = None,
    ):
        # Whether the SDK enables strict face quality detection:
        # 
        # - **Y**: Enable
        # 
        # - **N** (default): Disable
        # 
        # 
        # > 
        # > - If this parameter is enabled, the SDK needs to integrate the [strict face quality detection module](https://help.aliyun.com/zh/id-verification/financial-grade-id-verification/description-of-sdk-package-clipping?spm=a2c4g.11186623.0.0.1a9d35c6ySFUPW). Enabling strict quality detection may decrease the success rate of user face recognition.
        # > - Only supported in Android SDK version 2.3.24 and above.
        self.app_quality_check = app_quality_check
        # User authorization ID, with a maximum length of 64 characters.
        self.auth_id = auth_id
        # Date of birth on the document.
        # 
        # This field is required when the document type **CertType** is **PASSPORT** and **Mode** is **3**.
        self.birthday = birthday
        # Security token, generated by you, used for preventing duplication and tampering.
        # 
        # If this value is set, the **CallbackToken** field will be displayed in the callback address.
        self.callback_token = callback_token
        # Callback notification address for the authentication result, with the default callback request method being GET. The callback address must start with `https`. After completing the authentication, the platform will call back this address and automatically add the `certifyId` and `passed` fields, where the value of the `passed` field is the subcode, for example: `https://www.aliyun.com?callbackToken=1000004826&certifyId=shaxxxx&passed=200`.
        # 
        # <notice>
        # 
        # - Callbacks are triggered only when the authentication is completed (including both successful and unsuccessful authentications). If the authentication is abandoned, interrupted abnormally, or not performed, no notification will be sent. It is recommended that you retrieve detailed authentication information through a query interface if needed after receiving the callback notification.
        # - The accessibility of the provided address will be verified before the API call. If the address cannot be accessed over the public network, a 401 error will be returned.
        # - The callback interface must return an HTTP status code of 200; otherwise, it will trigger a retry, with two callbacks within 3 seconds.
        # 
        # </notice>
        self.callback_url = callback_url
        # Whether to enable the camera selection feature:
        # 
        # - **Y**: Enable
        # 
        # - **N** (default): Disable
        # 
        # > This feature only takes effect in PC integration mode. When enabled, it allows users to select the camera for authentication.
        self.camera_selection = camera_selection
        # Real name.
        self.cert_name = cert_name
        # Document number.
        self.cert_no = cert_no
        # Document type.
        # Currently, only IDENTITY_CARD (ID card) is supported.
        self.cert_type = cert_type
        # >Warning: To be deprecated
        # 
        # Previously passed CertifyId for real-person authentication, where the photo taken during authentication is used as the comparison photo.
        # 
        # > Among the four image input methods (FaceContrastPicture, FaceContrastPictureUrl, CertifyId, OSS), choose one to input.
        self.certify_id = certify_id
        # Types of **CertifyUrl** returned, including:
        # 
        # - **L**: Original long link
        # 
        # - **S** (default): Short link
        self.certify_url_style = certify_url_style
        # Web SDK device type, with values **WEB** or **H5**.
        # 
        # > Only Web SDK device types are supported.
        self.certify_url_type = certify_url_type
        # Whether to allow cropping of the face image, with the default being not allowed.
        # 
        # - T: Indicates allowing cropping.
        # 
        # - F: Indicates not allowing cropping.
        # 
        # > If the image you are requesting is not from a standard liveness detection SDK, it is recommended to allow face image cropping. When this feature is enabled, the requested image will first undergo face cropping and alignment, and then the service request will be initiated.
        self.crop = crop
        # Encryption algorithm to be used, currently supporting only the SM2 national encryption algorithm.
        # 
        # After enabling encrypted transmission, you need to pass in the encrypted CertName and CertNo. For how to encrypt, please refer to [Parameter Encryption Instructions](https://help.aliyun.com/zh/id-verification/financial-grade-id-verification/description-of-parameter-encryption?spm=a2c4g.11186623.0.0.1a9d566eWdqwy8#task-2229332).
        self.encrypt_type = encrypt_type
        # Base64 encoded photo.
        # 
        # > Choose one of the following methods to upload the image: FaceContrastPicture, FaceContrastPictureUrl, CertifyId, or OSS.
        self.face_contrast_picture = face_contrast_picture
        # OSS photo address, currently only supports authorized OSS photo addresses.
        # 
        # > Among the four image input methods (FaceContrastPicture, FaceContrastPictureUrl, CertifyId, OSS), choose one to input.
        self.face_contrast_picture_url = face_contrast_picture_url
        # Device assistant label type, with the value: **DeviceRisk**.
        # 
        # >
        # > - Choosing to output the device assistant will incur additional costs. For details, see [Paid Value-Added Services](https://help.aliyun.com/zh/id-verification/financial-grade-id-verification/face-guard?spm=a2c4g.11186623.0.0.443e5522rbHsR4).
        # > - If you do not need to output the device assistant label, you can either not pass the parameter or pass an empty value.
        self.face_guard_output = face_guard_output
        # User\\"s IP address.
        self.ip = ip
        # Metainfo environment parameter, which needs to be obtained through the client SDK.
        self.meta_info = meta_info
        # User\\"s phone number.
        self.mobile = mobile
        # Method to obtain passport NFC verification elements:
        # 
        # - **1**: User input, where the end-user manually inputs the document information using the UI interface provided by the Alibaba Cloud SDK.
        # 
        # - **3**: External parameter input, where the document information is passed through external parameters.
        # 
        # > When decoding the encrypted information from the passport chip using NFC, three elements of the passport need to be obtained, including name, date of birth, and document expiration date.
        self.mode = mode
        # Liveness detection type, with values:
        # > Only the following liveness detection types are supported; custom actions or combinations are not supported at this time.
        # 
        # Note
        # Only the following liveness detection types are supported; custom actions or combinations are not supported at this time.
        # 
        # - **LIVENESS** (default): Blinking
        # 
        # - **PHOTINUS_LIVENESS**: Blinking + Colorful Light
        # 
        # - **MULTI_ACTION**: Blinking + Head Shaking (the order of blinking and head shaking is random)
        # 
        # - **MOVE_ACTION** (recommended): Moving Closer and Farther + Blinking
        # 
        # - **MOVE_PHOTINUS**: Moving Closer and Farther + Colorful Light
        # 
        # > 
        # >- The **default liveness detection type** is supported in the following versions:
        # >   - Android SDK 1.2.6 and above
        # >   - iOS SDK 1.2.4 and above
        # >   - Harmony SDK 1.0.0 and above
        # >- Other types are supported in the latest SDK versions for Android/iOS/Harmony. It is recommended to integrate the latest version.
        self.model = model
        # Whether to intercept when multiple faces are detected, with the following values:
        # 
        # - **Y**: Intercept, and the client prompts the user to re-scan their face.
        # 
        # - **N** (default): Do not intercept, and send the largest face in the scanned image to the server for security checks.
        self.need_multi_face_check = need_multi_face_check
        # Authorized OSS bucket name.
        # 
        # > Among the four image input methods (FaceContrastPicture, FaceContrastPictureUrl, CertifyId, OSS), choose one to input.
        self.oss_bucket_name = oss_bucket_name
        # Authorized OSS object name.
        # 
        # > Among the four image input methods (FaceContrastPicture, FaceContrastPictureUrl, CertifyId, OSS), choose one to input.
        self.oss_object_name = oss_object_name
        # Unique identifier for the merchant\\"s request.
        # 
        # The value is a 32-character alphanumeric combination. The first few characters are a custom abbreviation defined by the merchant, followed by a period, and the latter part can be a random or incremental sequence.
        self.outer_order_no = outer_order_no
        # Degradation configuration for mobile H5 authentication when WebRTC or Webassembly is incompatible.
        # 
        # - **keep**: Does not support degradation, returns directly.
        # 
        # - **url** (default): Supports degradation, returns an authentication URL. Users can use this URL to open or switch browsers for authentication.
        # 
        # - **video**: Supports degradation, uses the system camera to record a 3~5 second blinking video for authentication.
        # 
        # 
        # > 
        # > When the degradation mode is Video, the following functions will be disabled, and the product security will decrease. It is recommended to configure it only for secure scenarios.
        # > - Liveness detection type settings will not take effect.
        # > - The VideoEvidence function is not supported.
        self.procedure_priority = procedure_priority
        # Fixed value. The parameter value differs based on the product solution:
        # - APP Authentication Scheme: Fixed value is ID_PRO
        # - Live Face Verification Scheme: Fixed value is PV_FV
        # - Liveness Detection Scheme: Fixed value is LR_FR
        self.product_code = product_code
        # Whether to enable rare character mode:
        # 
        # - **Y**: Enable. A message input box will pop up before the user authenticates, requiring the input of the rare character name and ID number. The user must agree to the terms before starting the authentication process.
        # 
        # - **N**: Not enabled (default)
        self.rarely_characters = rarely_characters
        # Whether to read the document photo:
        # 
        # - **Y**: Read
        # 
        # - **N**: Do not read
        # 
        # > If the document face photo is needed in subsequent authentication steps, it is recommended to set this parameter to Y.
        self.read_img = read_img
        # Target URL for the merchant\\"s business page to redirect to.
        self.return_url = return_url
        # Authentication Scene ID.
        self.scene_id = scene_id
        # Aging-friendly configuration parameters that take effect for each authentication request. You can choose different parameters based on your app\\"s business attributes, customer distribution, operational characteristics, etc., for each authentication request. The options include the following, with the default being 0.
        # 
        # - **0**: Not enabled, indicating that the current authentication request does not enable aging-friendly mode.
        # 
        # - **1**: Enabled, indicating that the current authentication request enables aging-friendly mode.
        # 
        # - **2**: User choice.
        # 
        # 
        # Supports end-users in choosing the authentication mode. The product guide page provides two authentication entry points: \\"Enable Authentication\\" and \\"Elderly Authentication Mode\\". When the user selects \\"Elderly Authentication Mode\\", the system enters aging-friendly mode.
        # > 
        # > - Aging-friendly parameters are only effective when the liveness detection type **Model** is set to **LIVENESS** or **MULTI_ACTION**.
        self.suitable_type = suitable_type
        # UI configuration file URL.
        # 
        # You can view the complete configuration in the [Web SDK UI Customization Description](https://help.aliyun.com/zh/id-verification/financial-grade-id-verification/web-sdk-ui-custom-configuration-description?spm=a2c4g.11186623.0.0.4c683f5c8K3I9p).
        self.ui_custom_url = ui_custom_url
        # Custom user ID for the customer\\"s business, please ensure it is unique.
        self.user_id = user_id
        # Document expiration date.
        # 
        # This field is required when the document type **CertType** is **PASSPORT** and **Mode** is **3**.
        self.validity_date = validity_date
        # Whether to enable video evidence:
        # 
        # - **true**: Enable
        # 
        # - **false** (default): Disable
        # 
        # > Due to the large size of video files, when the network is unstable, the system will discard the video file to prioritize the transmission of necessary images for authentication. It is recommended that your business set a weak dependency on the video.
        self.video_evidence = video_evidence
        # Customized content. Required when personalized settings are enabled. The format is a JSON String of a String List.
        # 
        # - For the follow-reading scenario: It should not exceed 60 Chinese characters (excluding punctuation), and the List contains only one element.
        # 
        # - For the Q&A scenario: Up to 3 questions can be set, with each question not exceeding 30 Chinese characters, and each question being an element in the List.
        self.voluntary_customized_content = voluntary_customized_content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_quality_check is not None:
            result['AppQualityCheck'] = self.app_quality_check
        if self.auth_id is not None:
            result['AuthId'] = self.auth_id
        if self.birthday is not None:
            result['Birthday'] = self.birthday
        if self.callback_token is not None:
            result['CallbackToken'] = self.callback_token
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        if self.camera_selection is not None:
            result['CameraSelection'] = self.camera_selection
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_no is not None:
            result['CertNo'] = self.cert_no
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.certify_url_style is not None:
            result['CertifyUrlStyle'] = self.certify_url_style
        if self.certify_url_type is not None:
            result['CertifyUrlType'] = self.certify_url_type
        if self.crop is not None:
            result['Crop'] = self.crop
        if self.encrypt_type is not None:
            result['EncryptType'] = self.encrypt_type
        if self.face_contrast_picture is not None:
            result['FaceContrastPicture'] = self.face_contrast_picture
        if self.face_contrast_picture_url is not None:
            result['FaceContrastPictureUrl'] = self.face_contrast_picture_url
        if self.face_guard_output is not None:
            result['FaceGuardOutput'] = self.face_guard_output
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.meta_info is not None:
            result['MetaInfo'] = self.meta_info
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.model is not None:
            result['Model'] = self.model
        if self.need_multi_face_check is not None:
            result['NeedMultiFaceCheck'] = self.need_multi_face_check
        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name
        if self.oss_object_name is not None:
            result['OssObjectName'] = self.oss_object_name
        if self.outer_order_no is not None:
            result['OuterOrderNo'] = self.outer_order_no
        if self.procedure_priority is not None:
            result['ProcedurePriority'] = self.procedure_priority
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.rarely_characters is not None:
            result['RarelyCharacters'] = self.rarely_characters
        if self.read_img is not None:
            result['ReadImg'] = self.read_img
        if self.return_url is not None:
            result['ReturnUrl'] = self.return_url
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.suitable_type is not None:
            result['SuitableType'] = self.suitable_type
        if self.ui_custom_url is not None:
            result['UiCustomUrl'] = self.ui_custom_url
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.validity_date is not None:
            result['ValidityDate'] = self.validity_date
        if self.video_evidence is not None:
            result['VideoEvidence'] = self.video_evidence
        if self.voluntary_customized_content is not None:
            result['VoluntaryCustomizedContent'] = self.voluntary_customized_content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppQualityCheck') is not None:
            self.app_quality_check = m.get('AppQualityCheck')
        if m.get('AuthId') is not None:
            self.auth_id = m.get('AuthId')
        if m.get('Birthday') is not None:
            self.birthday = m.get('Birthday')
        if m.get('CallbackToken') is not None:
            self.callback_token = m.get('CallbackToken')
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        if m.get('CameraSelection') is not None:
            self.camera_selection = m.get('CameraSelection')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertNo') is not None:
            self.cert_no = m.get('CertNo')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('CertifyUrlStyle') is not None:
            self.certify_url_style = m.get('CertifyUrlStyle')
        if m.get('CertifyUrlType') is not None:
            self.certify_url_type = m.get('CertifyUrlType')
        if m.get('Crop') is not None:
            self.crop = m.get('Crop')
        if m.get('EncryptType') is not None:
            self.encrypt_type = m.get('EncryptType')
        if m.get('FaceContrastPicture') is not None:
            self.face_contrast_picture = m.get('FaceContrastPicture')
        if m.get('FaceContrastPictureUrl') is not None:
            self.face_contrast_picture_url = m.get('FaceContrastPictureUrl')
        if m.get('FaceGuardOutput') is not None:
            self.face_guard_output = m.get('FaceGuardOutput')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('MetaInfo') is not None:
            self.meta_info = m.get('MetaInfo')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('NeedMultiFaceCheck') is not None:
            self.need_multi_face_check = m.get('NeedMultiFaceCheck')
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')
        if m.get('OssObjectName') is not None:
            self.oss_object_name = m.get('OssObjectName')
        if m.get('OuterOrderNo') is not None:
            self.outer_order_no = m.get('OuterOrderNo')
        if m.get('ProcedurePriority') is not None:
            self.procedure_priority = m.get('ProcedurePriority')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('RarelyCharacters') is not None:
            self.rarely_characters = m.get('RarelyCharacters')
        if m.get('ReadImg') is not None:
            self.read_img = m.get('ReadImg')
        if m.get('ReturnUrl') is not None:
            self.return_url = m.get('ReturnUrl')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('SuitableType') is not None:
            self.suitable_type = m.get('SuitableType')
        if m.get('UiCustomUrl') is not None:
            self.ui_custom_url = m.get('UiCustomUrl')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('ValidityDate') is not None:
            self.validity_date = m.get('ValidityDate')
        if m.get('VideoEvidence') is not None:
            self.video_evidence = m.get('VideoEvidence')
        if m.get('VoluntaryCustomizedContent') is not None:
            self.voluntary_customized_content = m.get('VoluntaryCustomizedContent')
        return self


class InitFaceVerifyResponseBodyResultObject(TeaModel):
    def __init__(
        self,
        certify_id: str = None,
        certify_url: str = None,
    ):
        # Unique identifier for real-person authentication.
        self.certify_id = certify_id
        # URL for real-person authentication in a Web browser, which will redirect according to the ReturnUrl parameter after authentication.
        # 
        # >Notice: 
        # 
        # - The CertifyUrl returned by the initialization interface is valid for **30 minutes and can only be used once**. Please use it within the validity period to avoid reuse.
        # - This parameter requires the correct input of **MetaInfo** to return a CertifyUrl that matches the client. If you cannot obtain it, please check whether **MetaInfo** and other input parameters are correct.
        # 
        # - The domain name of this URL may change with service updates. To ensure normal service availability, it is recommended not to apply access control to this domain name.
        # 
        # - When redirecting in the browser, try not to use incognito mode or modify the URL, as this may result in a **signature error**.
        self.certify_url = certify_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: InitFaceVerifyResponseBodyResultObject = None,
    ):
        # Return code: 200 indicates success, other values indicate failure.
        self.code = code
        # Error message.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Result object.
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

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
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultObject') is not None:
            temp_model = InitFaceVerifyResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class InitFaceVerifyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InitFaceVerifyResponseBody = None,
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
            temp_model = InitFaceVerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InsertWhiteListSettingRequest(TeaModel):
    def __init__(
        self,
        cert_no: str = None,
        certify_id: str = None,
        remark: str = None,
        scene_id: int = None,
        service_code: str = None,
        valid_day: int = None,
    ):
        # ID number.
        self.cert_no = cert_no
        # Unique identifier for real person authentication.
        self.certify_id = certify_id
        # Remark, with a length less than 32 characters.
        self.remark = remark
        # Authentication scene ID. This ID is automatically generated after creating an authentication scene in the console. For instructions on how to create an authentication scene, see Adding an Authentication Scene.
        self.scene_id = scene_id
        # ServiceCode for the real person cloud product, value: **antcloudauth**.
        self.service_code = service_code
        # Whitelist validity period in days (only supports 3, 7, 30).
        self.valid_day = valid_day

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_no is not None:
            result['CertNo'] = self.cert_no
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.valid_day is not None:
            result['ValidDay'] = self.valid_day
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertNo') is not None:
            self.cert_no = m.get('CertNo')
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('ValidDay') is not None:
            self.valid_day = m.get('ValidDay')
        return self


class InsertWhiteListSettingResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: bool = None,
        success: bool = None,
    ):
        # Return code: 200 for success, others for failure.
        self.code = code
        # Return message.
        self.message = message
        # Request ID
        self.request_id = request_id
        # Returned result
        self.result_object = result_object
        # Indicates whether the response was successful.
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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_object is not None:
            result['ResultObject'] = self.result_object
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultObject') is not None:
            self.result_object = m.get('ResultObject')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class InsertWhiteListSettingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InsertWhiteListSettingResponseBody = None,
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
            temp_model = InsertWhiteListSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LivenessFaceVerifyRequest(TeaModel):
    def __init__(
        self,
        certify_id: str = None,
        crop: str = None,
        device_token: str = None,
        face_contrast_picture: str = None,
        face_contrast_picture_url: str = None,
        ip: str = None,
        mobile: str = None,
        model: str = None,
        oss_bucket_name: str = None,
        oss_object_name: str = None,
        outer_order_no: str = None,
        product_code: str = None,
        scene_id: int = None,
        user_id: str = None,
    ):
        # Unique identifier for real-person authentication.
        self.certify_id = certify_id
        # Whether to allow cropping of the face image:
        # 
        # - T: Allow cropping
        # 
        # - F (default): Do not allow cropping.
        self.crop = crop
        # Device token, used for risk identification.
        self.device_token = device_token
        # Base64 encoded photo.
        self.face_contrast_picture = face_contrast_picture
        # Image URL.
        self.face_contrast_picture_url = face_contrast_picture_url
        # User\\"s network IP address.
        self.ip = ip
        # User\\"s mobile phone number.
        self.mobile = mobile
        # Liveness detection parameters.
        self.model = model
        # Authorized OSS bucket name.
        self.oss_bucket_name = oss_bucket_name
        # Authorized OSS file name.
        self.oss_object_name = oss_object_name
        # A unique business identifier defined by the client side, used for subsequent troubleshooting. The value should be a combination of letters and numbers up to 32 characters long, ensuring uniqueness.
        self.outer_order_no = outer_order_no
        # Fixed value: LR_FR_MIN.
        self.product_code = product_code
        # Authentication scenario ID. This ID is automatically generated after creating an authentication scenario in the console.
        self.scene_id = scene_id
        # Your custom user ID (up to 100 characters), please ensure it is unique.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.crop is not None:
            result['Crop'] = self.crop
        if self.device_token is not None:
            result['DeviceToken'] = self.device_token
        if self.face_contrast_picture is not None:
            result['FaceContrastPicture'] = self.face_contrast_picture
        if self.face_contrast_picture_url is not None:
            result['FaceContrastPictureUrl'] = self.face_contrast_picture_url
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.model is not None:
            result['Model'] = self.model
        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name
        if self.oss_object_name is not None:
            result['OssObjectName'] = self.oss_object_name
        if self.outer_order_no is not None:
            result['OuterOrderNo'] = self.outer_order_no
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('Crop') is not None:
            self.crop = m.get('Crop')
        if m.get('DeviceToken') is not None:
            self.device_token = m.get('DeviceToken')
        if m.get('FaceContrastPicture') is not None:
            self.face_contrast_picture = m.get('FaceContrastPicture')
        if m.get('FaceContrastPictureUrl') is not None:
            self.face_contrast_picture_url = m.get('FaceContrastPictureUrl')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')
        if m.get('OssObjectName') is not None:
            self.oss_object_name = m.get('OssObjectName')
        if m.get('OuterOrderNo') is not None:
            self.outer_order_no = m.get('OuterOrderNo')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class LivenessFaceVerifyResponseBodyResultObject(TeaModel):
    def __init__(
        self,
        certify_id: str = None,
        material_info: str = None,
        passed: str = None,
        sub_code: str = None,
    ):
        # Unique identifier for the real-person authentication request.
        self.certify_id = certify_id
        # Attachment information of the face authentication subject, including data such as face quality, face attack, face or OCR image, and intent verification.
        self.material_info = material_info
        # Authentication result, values:
        # 
        # - T: Passed
        # 
        # - F: Not passed
        self.passed = passed
        # Authentication result code.
        self.sub_code = sub_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.material_info is not None:
            result['MaterialInfo'] = self.material_info
        if self.passed is not None:
            result['Passed'] = self.passed
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('MaterialInfo') is not None:
            self.material_info = m.get('MaterialInfo')
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        return self


class LivenessFaceVerifyResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: LivenessFaceVerifyResponseBodyResultObject = None,
    ):
        # Return code, **200** indicates successful API response.
        self.code = code
        # Return message.
        self.message = message
        # ID of this request.
        self.request_id = request_id
        # Return result.
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

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
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultObject') is not None:
            temp_model = LivenessFaceVerifyResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class LivenessFaceVerifyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: LivenessFaceVerifyResponseBody = None,
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
            temp_model = LivenessFaceVerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class Mobile2MetaVerifyRequest(TeaModel):
    def __init__(
        self,
        mobile: str = None,
        param_type: str = None,
        user_name: str = None,
    ):
        # Phone number:
        # - When paramType is normal: input the plaintext phone number.
        # - When paramType is md5: input the encrypted phone number.
        # 
        # This parameter is required.
        self.mobile = mobile
        # Encryption method:
        # - normal: plaintext without encryption
        # - md5: MD5 encryption
        # 
        # This parameter is required.
        self.param_type = param_type
        # Name:
        # - When paramType is normal: input the plaintext name.
        # - When paramType is md5: input the encrypted name.
        # 
        # This parameter is required.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.param_type is not None:
            result['ParamType'] = self.param_type
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class Mobile2MetaVerifyResponseBodyResultObject(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        isp_name: str = None,
    ):
        # Verification result:
        # - 1: Consistent verification
        # - 2: Inconsistent verification
        # - 3: No record found
        self.biz_code = biz_code
        # Operator name:
        # - CMCC: China Mobile
        # - CUCC: China Unicom
        # - CTCC: China Telecom
        self.isp_name = isp_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.isp_name is not None:
            result['IspName'] = self.isp_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('IspName') is not None:
            self.isp_name = m.get('IspName')
        return self


class Mobile2MetaVerifyResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: Mobile2MetaVerifyResponseBodyResultObject = None,
    ):
        # Return code: 200 for success, others for failure.
        self.code = code
        # Return message.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Result object.
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

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
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultObject') is not None:
            temp_model = Mobile2MetaVerifyResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class Mobile2MetaVerifyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Mobile2MetaVerifyResponseBody = None,
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
            temp_model = Mobile2MetaVerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class Mobile3MetaDetailStandardVerifyRequest(TeaModel):
    def __init__(
        self,
        identify_num: str = None,
        mobile: str = None,
        param_type: str = None,
        user_name: str = None,
    ):
        # ID number:
        # 
        # - When `paramType` is `normal`: Input the plain text of the ID number.
        # - When `paramType` is `md5`: Input the encrypted text of the ID number.
        self.identify_num = identify_num
        # Phone number:
        # 
        # - When `paramType` is `normal`: Input the plain text of the phone number.
        # - When `paramType` is `md5`: Input the encrypted text of the phone number.
        self.mobile = mobile
        # Parameter type:
        # 
        # - normal: Unencrypted.
        # - md5: Encrypted with MD5.
        self.param_type = param_type
        # Name:
        # 
        # - When `paramType` is `normal`: Input the plain text of the name.
        # - When `paramType` is `md5`: Input the encrypted text of the name.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identify_num is not None:
            result['IdentifyNum'] = self.identify_num
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.param_type is not None:
            result['ParamType'] = self.param_type
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdentifyNum') is not None:
            self.identify_num = m.get('IdentifyNum')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class Mobile3MetaDetailStandardVerifyResponseBodyResultObject(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        isp_name: str = None,
        sub_code: str = None,
    ):
        # Verification result code:
        # - **1**: Verification matches.
        # - **2**: Verification does not match.
        # - **3**: No record found.
        self.biz_code = biz_code
        # ISP name:
        # 
        # - **CMCC**: China Mobile.
        # - **CUCC**: China Unicom.
        # - **CTCC**: China Telecom.
        # - **CBCC**: China Broadcasting Network.
        self.isp_name = isp_name
        # Detailed verification results:
        # 
        # - 101: Passed, three elements are consistent.
        # - 201: The phone number does not match the name and ID number.
        # - 202: The phone number matches the name but does not match the ID number.
        # - 203: The phone number does not match the name but matches the ID number.
        # - 204: Other inconsistencies.
        # - 301: No record found.
        self.sub_code = sub_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.isp_name is not None:
            result['IspName'] = self.isp_name
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('IspName') is not None:
            self.isp_name = m.get('IspName')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        return self


class Mobile3MetaDetailStandardVerifyResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: Mobile3MetaDetailStandardVerifyResponseBodyResultObject = None,
    ):
        # Return code, **200** indicates a successful API response.
        self.code = code
        # Return message.
        self.message = message
        # Request ID
        self.request_id = request_id
        # Returned result information
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

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
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultObject') is not None:
            temp_model = Mobile3MetaDetailStandardVerifyResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class Mobile3MetaDetailStandardVerifyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Mobile3MetaDetailStandardVerifyResponseBody = None,
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
            temp_model = Mobile3MetaDetailStandardVerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class Mobile3MetaDetailVerifyRequest(TeaModel):
    def __init__(
        self,
        identify_num: str = None,
        mobile: str = None,
        param_type: str = None,
        user_name: str = None,
    ):
        # ID number:
        # 
        # Note
        # Only supports the ID numbers of second-generation resident IDs and Hong Kong, Macao, and Taiwan residence permits.
        # 
        # - When paramType is normal: enter the plaintext ID number.
        # 
        # - When paramType is md5: enter the encrypted ID number.
        self.identify_num = identify_num
        # Mobile phone number:
        # 
        # - When paramType is normal: enter the plaintext mobile phone number.
        # 
        # - When paramType is md5: enter the encrypted mobile phone number.
        self.mobile = mobile
        # Encryption method:
        # 
        # - normal: plaintext, unencrypted
        # 
        # - md5: MD5 encryption
        self.param_type = param_type
        # Name:
        # 
        # - When paramType is normal: enter the plaintext name.
        # 
        # - When paramType is md5: enter the encrypted name.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identify_num is not None:
            result['IdentifyNum'] = self.identify_num
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.param_type is not None:
            result['ParamType'] = self.param_type
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdentifyNum') is not None:
            self.identify_num = m.get('IdentifyNum')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class Mobile3MetaDetailVerifyResponseBodyResultObject(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        isp_name: str = None,
        sub_code: str = None,
    ):
        # Verification result code:
        # - **1**: Verification consistent.
        # - **2**: Verification inconsistent.
        # - **3**: No record found.
        self.biz_code = biz_code
        # Operator name:
        # 
        # - **CMCC**: China Mobile.
        # - **CUCC**: China Unicom.
        # - **CTCC**: China Telecom.
        self.isp_name = isp_name
        # Detailed verification results:
        # 
        # - **101**: Verification passed.
        # - **201**: Mobile number and name do not match, mobile number and ID number do not match.
        # - **202**: Mobile number and name match, but mobile number and ID number do not match.
        # - **203**: Mobile number and ID number match, but mobile number and name do not match.
        # - **204**: Other inconsistencies.
        # - **301**: No record found.
        self.sub_code = sub_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.isp_name is not None:
            result['IspName'] = self.isp_name
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('IspName') is not None:
            self.isp_name = m.get('IspName')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        return self


class Mobile3MetaDetailVerifyResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: Mobile3MetaDetailVerifyResponseBodyResultObject = None,
    ):
        # Return code, **200** indicates a successful API response.
        self.code = code
        # Return message.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Returned result information.
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

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
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultObject') is not None:
            temp_model = Mobile3MetaDetailVerifyResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class Mobile3MetaDetailVerifyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Mobile3MetaDetailVerifyResponseBody = None,
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
            temp_model = Mobile3MetaDetailVerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class Mobile3MetaSimpleStandardVerifyRequest(TeaModel):
    def __init__(
        self,
        identify_num: str = None,
        mobile: str = None,
        param_type: str = None,
        user_name: str = None,
    ):
        # ID number:
        # 
        # - When `paramType` is `normal`: Input the plain text of the ID number.
        # - When `paramType` is `md5`: Input the encrypted ID number.
        self.identify_num = identify_num
        # Phone number:
        # 
        # - When `paramType` is `normal`: Input the plain text of the phone number.
        # - When `paramType` is `md5`: Input the encrypted phone number.
        self.mobile = mobile
        # Parameter type:
        # 
        # - normal: Unencrypted.
        # - md5: MD5 encrypted.
        self.param_type = param_type
        # Name:
        # 
        # - When `paramType` is `normal`: Input the plain text of the name.
        # - When `paramType` is `md5`: Input the encrypted name.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identify_num is not None:
            result['IdentifyNum'] = self.identify_num
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.param_type is not None:
            result['ParamType'] = self.param_type
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdentifyNum') is not None:
            self.identify_num = m.get('IdentifyNum')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class Mobile3MetaSimpleStandardVerifyResponseBodyResultObject(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        isp_name: str = None,
    ):
        # Verification result:
        # 
        # - 1: Consistent (billable)
        # - 2: Inconsistent (billable)
        # - 3: No record found (non-billable)
        self.biz_code = biz_code
        # Operator name:
        # 
        # - **CMCC**: China Mobile.
        # - **CUCC**: China Unicom.
        # - **CTCC**: China Telecom.
        # - **CBCC**: China Broadcasting Network.
        self.isp_name = isp_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.isp_name is not None:
            result['IspName'] = self.isp_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('IspName') is not None:
            self.isp_name = m.get('IspName')
        return self


class Mobile3MetaSimpleStandardVerifyResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: Mobile3MetaSimpleStandardVerifyResponseBodyResultObject = None,
    ):
        # Return code: 200 for success, others for failure
        self.code = code
        # Return message.
        self.message = message
        # ID of the request
        self.request_id = request_id
        # Returned result information
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

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
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultObject') is not None:
            temp_model = Mobile3MetaSimpleStandardVerifyResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class Mobile3MetaSimpleStandardVerifyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Mobile3MetaSimpleStandardVerifyResponseBody = None,
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
            temp_model = Mobile3MetaSimpleStandardVerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class Mobile3MetaSimpleVerifyRequest(TeaModel):
    def __init__(
        self,
        identify_num: str = None,
        mobile: str = None,
        param_type: str = None,
        user_name: str = None,
    ):
        # ID number:
        # 
        # Note
        # Only supports the ID numbers of second-generation resident IDs and Hong Kong, Macao, and Taiwan residence permits.
        # 
        # - When paramType is normal: enter the plaintext ID number.
        # 
        # - When paramType is md5: enter the encrypted ID number.
        self.identify_num = identify_num
        # Mobile phone number:
        # 
        # - When paramType is normal: enter the plaintext mobile phone number.
        # 
        # - When paramType is md5: enter the encrypted mobile phone number.
        self.mobile = mobile
        # Encryption method:
        # 
        # - normal: plaintext, not encrypted
        # 
        # - md5: MD5 encryption
        self.param_type = param_type
        # Name:
        # 
        # - When paramType is normal: enter the plaintext name.
        # 
        # - When paramType is md5: enter the encrypted name.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identify_num is not None:
            result['IdentifyNum'] = self.identify_num
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.param_type is not None:
            result['ParamType'] = self.param_type
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdentifyNum') is not None:
            self.identify_num = m.get('IdentifyNum')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class Mobile3MetaSimpleVerifyResponseBodyResultObject(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        isp_name: str = None,
    ):
        # Verification result code:
        # - **1**: Verification consistent.
        # - **2**: Verification inconsistent.
        # - **3**: No record found.
        self.biz_code = biz_code
        # ISP name:
        # 
        # - **CMCC**: China Mobile.
        # - **CUCC**: China Unicom.
        # - **CTCC**: China Telecom.
        self.isp_name = isp_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.isp_name is not None:
            result['IspName'] = self.isp_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('IspName') is not None:
            self.isp_name = m.get('IspName')
        return self


class Mobile3MetaSimpleVerifyResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: Mobile3MetaSimpleVerifyResponseBodyResultObject = None,
    ):
        # Return code: 200 for success, others for failure.
        self.code = code
        # Return message.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Returned result.
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

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
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultObject') is not None:
            temp_model = Mobile3MetaSimpleVerifyResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class Mobile3MetaSimpleVerifyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Mobile3MetaSimpleVerifyResponseBody = None,
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
            temp_model = Mobile3MetaSimpleVerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MobileDetectRequest(TeaModel):
    def __init__(
        self,
        mobiles: str = None,
        param_type: str = None,
    ):
        # List of phone numbers.
        self.mobiles = mobiles
        # Encryption method:
        # - normal: plaintext, no encryption
        # - md5: MD5 encryption
        self.param_type = param_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mobiles is not None:
            result['Mobiles'] = self.mobiles
        if self.param_type is not None:
            result['ParamType'] = self.param_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mobiles') is not None:
            self.mobiles = m.get('Mobiles')
        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')
        return self


class MobileDetectResponseBodyResultObjectItems(TeaModel):
    def __init__(
        self,
        area: str = None,
        biz_code: str = None,
        isp_name: str = None,
        mobile: str = None,
        sub_code: str = None,
    ):
        # Phone number\\"s area (only for plaintext phone numbers)
        self.area = area
        # Verification result
        # 
        # - 1: Available online 
        # - 2: Not available online
        # - 3: No query result
        self.biz_code = biz_code
        # Operator name
        # 
        # - CMCC: China Mobile 
        # - CUCC: China Unicom 
        # - CTCC: China Telecom
        self.isp_name = isp_name
        # Phone number
        self.mobile = mobile
        # Verification details
        # 
        # - 101: Available number
        # - 102: Empty number
        # - 103: Suspended 
        # - 104: Silent number (inactive small number, new number, non-smartphone user within the last six months) 
        # - 105: Risky number (long-term shutdown or no voice service activated and prone to complaints)
        # - 301: No record found
        self.sub_code = sub_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area is not None:
            result['Area'] = self.area
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.isp_name is not None:
            result['IspName'] = self.isp_name
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('IspName') is not None:
            self.isp_name = m.get('IspName')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        return self


class MobileDetectResponseBodyResultObject(TeaModel):
    def __init__(
        self,
        charge_count: str = None,
        items: List[MobileDetectResponseBodyResultObjectItems] = None,
    ):
        # Billing count, the total billing count in one request
        self.charge_count = charge_count
        # Verification results set
        self.items = items

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_count is not None:
            result['ChargeCount'] = self.charge_count
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeCount') is not None:
            self.charge_count = m.get('ChargeCount')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = MobileDetectResponseBodyResultObjectItems()
                self.items.append(temp_model.from_map(k))
        return self


class MobileDetectResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: MobileDetectResponseBodyResultObject = None,
    ):
        # Return code: 200 for success, others for failure.
        self.code = code
        # Return message.
        self.message = message
        # Request ID
        self.request_id = request_id
        # Returned result information
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

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
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultObject') is not None:
            temp_model = MobileDetectResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class MobileDetectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: MobileDetectResponseBody = None,
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
            temp_model = MobileDetectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MobileOnlineStatusRequest(TeaModel):
    def __init__(
        self,
        mobile: str = None,
        param_type: str = None,
    ):
        # Mobile number:
        # 
        # - When `paramType` is `normal`: provide the plaintext mobile number.
        # - When `paramType` is `md5`: provide the encrypted mobile number.
        self.mobile = mobile
        # Parameter type:
        # 
        # - normal: unencrypted.
        # - md5: md5 encrypted.
        self.param_type = param_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.param_type is not None:
            result['ParamType'] = self.param_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')
        return self


class MobileOnlineStatusResponseBodyResultObject(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        isp_name: str = None,
        sub_code: str = None,
    ):
        # Verification result
        # 
        # - 1: Available online 
        # - 2: Not available online (see subCode for details)
        # - 3: No query result
        self.biz_code = biz_code
        # ISP name
        # 
        # - CMCC: China Mobile 
        # - CUCC: China Unicom 
        # - CTCC: China Telecom
        self.isp_name = isp_name
        # Verification details
        # 
        # - 101: Available online 
        # - 201: Suspended 
        # - 202: Disconnected 
        # - 203: Online but not available 
        # - 204: Not online 
        # - 301: No record found
        self.sub_code = sub_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.isp_name is not None:
            result['IspName'] = self.isp_name
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('IspName') is not None:
            self.isp_name = m.get('IspName')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        return self


class MobileOnlineStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: MobileOnlineStatusResponseBodyResultObject = None,
    ):
        # Return code: 200 for success, others for failure.
        self.code = code
        # Return message.
        self.message = message
        # Request ID
        self.request_id = request_id
        # Returned result information
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

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
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultObject') is not None:
            temp_model = MobileOnlineStatusResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class MobileOnlineStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: MobileOnlineStatusResponseBody = None,
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
            temp_model = MobileOnlineStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MobileOnlineTimeRequest(TeaModel):
    def __init__(
        self,
        mobile: str = None,
        param_type: str = None,
    ):
        # Mobile number:
        # - When `paramType` is `normal`: provide the plaintext mobile number.
        # - When `paramType` is `md5`: provide the encrypted mobile number.
        self.mobile = mobile
        # Parameter type:
        # 
        # - normal: unencrypted.
        # - md5: md5 encrypted.
        self.param_type = param_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.param_type is not None:
            result['ParamType'] = self.param_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')
        return self


class MobileOnlineTimeResponseBodyResultObject(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        isp_name: str = None,
        time_code: str = None,
    ):
        # Verification result code.
        # - 1: Verification consistent
        # - 2: Verification inconsistent
        # - 3: No record found
        self.biz_code = biz_code
        # Operator name
        # 
        # - CMCC: China Mobile 
        # - CUCC: China Unicom 
        # - CTCC: China Telecom
        self.isp_name = isp_name
        # - 1: [0,3) indicates the online duration is 0~3 months 
        # - 2: [3,6) indicates the online duration is 3~6 months 
        # - 3: [6,12) indicates the online duration is 6~12 months 
        # - 4: [12,24) indicates the online duration is 12~24 months 
        # - 5: [24,+) indicates the online duration is more than 24 months
        self.time_code = time_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.isp_name is not None:
            result['IspName'] = self.isp_name
        if self.time_code is not None:
            result['TimeCode'] = self.time_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('IspName') is not None:
            self.isp_name = m.get('IspName')
        if m.get('TimeCode') is not None:
            self.time_code = m.get('TimeCode')
        return self


class MobileOnlineTimeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: MobileOnlineTimeResponseBodyResultObject = None,
    ):
        # Return code: 200 for success, others for failure.
        self.code = code
        # Return message.
        self.message = message
        # Request ID
        self.request_id = request_id
        # Returned result information
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

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
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultObject') is not None:
            temp_model = MobileOnlineTimeResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class MobileOnlineTimeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: MobileOnlineTimeResponseBody = None,
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
            temp_model = MobileOnlineTimeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDeviceInfoRequest(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        device_id: str = None,
        duration: str = None,
        expired_day: str = None,
        user_device_id: str = None,
    ):
        # The updated business type. It should not exceed 64 characters and is defined by the connected party. It can be used to annotate specific businesses, for example, different face usage scenarios or the customer identifiers to be delivered.
        self.biz_type = biz_type
        # A unique ID generated by the real-person authentication server for the connected device, which is only generated after the device is successfully activated. This ID can be obtained through the getLicenseExtraInfo function in the offline facial recognition SDK.
        # 
        # This parameter is required.
        self.device_id = device_id
        # The extended duration of the device expiration. Unit: years, with a range of [1,100]. A value of 100 indicates permanent use. One year is calculated as 365 days.
        self.duration = duration
        # The current expiration time of the device. If the expiration date is incorrect (differing from the real-person authentication server\\"s recorded expiration time by more than one week), an error will be reported.
        # > The expiration time can be queried through the DescribeDeviceInfo interface. An incorrect expiration date will result in an error. This check ensures that the business party does not accidentally re-activate a device due to some misoperation, thus consuming the authorization unnecessarily.
        self.expired_day = expired_day
        # The updated user device ID. It should not exceed 64 characters and is defined by the connected party. It can be used to identify specific devices, and it is recommended to use the physical number of the device.
        self.user_device_id = user_device_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.expired_day is not None:
            result['ExpiredDay'] = self.expired_day
        if self.user_device_id is not None:
            result['UserDeviceId'] = self.user_device_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('ExpiredDay') is not None:
            self.expired_day = m.get('ExpiredDay')
        if m.get('UserDeviceId') is not None:
            self.user_device_id = m.get('UserDeviceId')
        return self


class ModifyDeviceInfoResponseBody(TeaModel):
    def __init__(
        self,
        begin_day: str = None,
        biz_type: str = None,
        device_id: str = None,
        expired_day: str = None,
        request_id: str = None,
        user_device_id: str = None,
    ):
        # If the Duration in the request parameters is not empty, this field represents the start time of the authorization after the device validity period has been extended. One year of Duration is calculated as 365 days. Example: 20180101.
        self.begin_day = begin_day
        # Corresponds to the BizType in the request parameters.
        self.biz_type = biz_type
        # Corresponds to the DeviceId in the request parameters.
        self.device_id = device_id
        # If the Duration in the request parameters is not empty, this field represents the expiration time of the authorization after the device validity period has been extended. One year of Duration is calculated as 365 days. Example: 20180101.
        self.expired_day = expired_day
        # The ID of this request.
        self.request_id = request_id
        # Corresponds to the UserDeviceId in the request parameters.
        self.user_device_id = user_device_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_day is not None:
            result['BeginDay'] = self.begin_day
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.expired_day is not None:
            result['ExpiredDay'] = self.expired_day
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_device_id is not None:
            result['UserDeviceId'] = self.user_device_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginDay') is not None:
            self.begin_day = m.get('BeginDay')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('ExpiredDay') is not None:
            self.expired_day = m.get('ExpiredDay')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserDeviceId') is not None:
            self.user_device_id = m.get('UserDeviceId')
        return self


class ModifyDeviceInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDeviceInfoResponseBody = None,
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
            temp_model = ModifyDeviceInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PageQueryWhiteListSettingRequest(TeaModel):
    def __init__(
        self,
        cert_no: str = None,
        certify_id: str = None,
        current_page: int = None,
        page_size: int = None,
        scene_id: int = None,
        service_code: str = None,
        status: str = None,
        valid_end_date: str = None,
        valid_start_date: str = None,
    ):
        # ID number.
        self.cert_no = cert_no
        # Unique identifier for real person authentication.
        self.certify_id = certify_id
        # Current page number, default is 1.
        self.current_page = current_page
        # Number of items per page, default is 10
        self.page_size = page_size
        # Authentication scene ID. This ID is automatically generated after creating an authentication scene in the console. For how to create an authentication scene, see Adding an Authentication Scene.
        self.scene_id = scene_id
        # ServiceCode of the real person cloud product, value: **antcloudauth**.
        self.service_code = service_code
        # Status:
        # 
        # - DELETE: Deleted
        # - VALID: Not deleted and within the validity period, valid
        # - INVALID: Not deleted but outside the validity period, invalid
        self.status = status
        # End date of validity (timestamp in milliseconds)
        self.valid_end_date = valid_end_date
        # Start date of validity (timestamp in milliseconds)
        self.valid_start_date = valid_start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_no is not None:
            result['CertNo'] = self.cert_no
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.status is not None:
            result['Status'] = self.status
        if self.valid_end_date is not None:
            result['ValidEndDate'] = self.valid_end_date
        if self.valid_start_date is not None:
            result['ValidStartDate'] = self.valid_start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertNo') is not None:
            self.cert_no = m.get('CertNo')
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ValidEndDate') is not None:
            self.valid_end_date = m.get('ValidEndDate')
        if m.get('ValidStartDate') is not None:
            self.valid_start_date = m.get('ValidStartDate')
        return self


class PageQueryWhiteListSettingResponseBodyResultObject(TeaModel):
    def __init__(
        self,
        cert_no: str = None,
        certify_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        remark: str = None,
        scene_id: int = None,
        service_code: str = None,
        status: str = None,
        valid_end_date: str = None,
        valid_start_date: str = None,
    ):
        # ID number.
        self.cert_no = cert_no
        # Unique identifier for real person authentication.
        self.certify_id = certify_id
        # Creation time.
        self.gmt_create = gmt_create
        # Modification time.
        self.gmt_modified = gmt_modified
        # Whitelist ID.
        self.id = id
        # Remark information.
        self.remark = remark
        # Authentication scene ID.
        self.scene_id = scene_id
        # ServiceCode of the real person cloud product
        self.service_code = service_code
        # Status:
        # 
        # - DELETE: Deleted
        # - VALID: Not deleted and within the validity period, valid
        # - INVALID: Not deleted but outside the validity period, invalid
        self.status = status
        # End date of validity
        self.valid_end_date = valid_end_date
        # Start date of validity
        self.valid_start_date = valid_start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_no is not None:
            result['CertNo'] = self.cert_no
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.status is not None:
            result['Status'] = self.status
        if self.valid_end_date is not None:
            result['ValidEndDate'] = self.valid_end_date
        if self.valid_start_date is not None:
            result['ValidStartDate'] = self.valid_start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertNo') is not None:
            self.cert_no = m.get('CertNo')
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ValidEndDate') is not None:
            self.valid_end_date = m.get('ValidEndDate')
        if m.get('ValidStartDate') is not None:
            self.valid_start_date = m.get('ValidStartDate')
        return self


class PageQueryWhiteListSettingResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        current_page: int = None,
        message: str = None,
        page_size: int = None,
        request_id: str = None,
        result_object: List[PageQueryWhiteListSettingResponseBodyResultObject] = None,
        success: bool = None,
        total_item: int = None,
        total_page: int = None,
    ):
        # Return code, **200** indicates a successful API response.
        self.code = code
        # Current page number.
        self.current_page = current_page
        # Return message.
        self.message = message
        # Number of items per page.
        self.page_size = page_size
        # ID of the request
        self.request_id = request_id
        # Request result
        self.result_object = result_object
        # Whether the response was successful.
        self.success = success
        # Total number of items.
        self.total_item = total_item
        # Total number of pages.
        self.total_page = total_page

    def validate(self):
        if self.result_object:
            for k in self.result_object:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ResultObject'] = []
        if self.result_object is not None:
            for k in self.result_object:
                result['ResultObject'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        if self.total_item is not None:
            result['TotalItem'] = self.total_item
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result_object = []
        if m.get('ResultObject') is not None:
            for k in m.get('ResultObject'):
                temp_model = PageQueryWhiteListSettingResponseBodyResultObject()
                self.result_object.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalItem') is not None:
            self.total_item = m.get('TotalItem')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class PageQueryWhiteListSettingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PageQueryWhiteListSettingResponseBody = None,
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
            temp_model = PageQueryWhiteListSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveWhiteListSettingRequest(TeaModel):
    def __init__(
        self,
        ids: List[int] = None,
        service_code: str = None,
    ):
        # IDs of the whitelist to be deleted in bulk.
        self.ids = ids
        # ServiceCode for the real person cloud product, only value: **antcloudauth**.
        self.service_code = service_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ids is not None:
            result['Ids'] = self.ids
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        return self


class RemoveWhiteListSettingShrinkRequest(TeaModel):
    def __init__(
        self,
        ids_shrink: str = None,
        service_code: str = None,
    ):
        # IDs of the whitelist to be deleted in bulk.
        self.ids_shrink = ids_shrink
        # ServiceCode for the real person cloud product, only value: **antcloudauth**.
        self.service_code = service_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ids_shrink is not None:
            result['Ids'] = self.ids_shrink
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids_shrink = m.get('Ids')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        return self


class RemoveWhiteListSettingResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: bool = None,
        success: bool = None,
    ):
        # Return code: 200 for success, others for failure
        self.code = code
        # Return message.
        self.message = message
        # ID of the request
        self.request_id = request_id
        # Returned result information.
        self.result_object = result_object
        # Whether the response was successful.
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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_object is not None:
            result['ResultObject'] = self.result_object
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultObject') is not None:
            self.result_object = m.get('ResultObject')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RemoveWhiteListSettingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveWhiteListSettingResponseBody = None,
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
            temp_model = RemoveWhiteListSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class Vehicle5ItemQueryRequest(TeaModel):
    def __init__(
        self,
        param_type: str = None,
        vehicle_num: str = None,
        vehicle_type: str = None,
    ):
        # Parameter type:
        # 
        # - **normal**: Unencrypted.
        # - **md5**: MD5 encrypted.
        self.param_type = param_type
        # License plate number
        # 
        # > 
        # > - When paramType is set to normal, enter the plain text.
        # > - When paramType is set to md5, enter the plain text of all but the last two characters of the license plate + MD5 encryption (32-bit lowercase MD5) of the last two characters.
        self.vehicle_num = vehicle_num
        # Vehicle type
        # 
        # > 
        # > - 02: Ordinary passenger car
        # > - 52: New energy passenger car
        self.vehicle_type = vehicle_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.param_type is not None:
            result['ParamType'] = self.param_type
        if self.vehicle_num is not None:
            result['VehicleNum'] = self.vehicle_num
        if self.vehicle_type is not None:
            result['VehicleType'] = self.vehicle_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')
        if m.get('VehicleNum') is not None:
            self.vehicle_num = m.get('VehicleNum')
        if m.get('VehicleType') is not None:
            self.vehicle_type = m.get('VehicleType')
        return self


class Vehicle5ItemQueryResponseBodyResultObject(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        vehicle_info: str = None,
    ):
        # Verification result code:
        # - **1**: Found (charged)
        # - **3**: No record found (not charged)
        self.biz_code = biz_code
        # Vehicle information
        self.vehicle_info = vehicle_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.vehicle_info is not None:
            result['VehicleInfo'] = self.vehicle_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('VehicleInfo') is not None:
            self.vehicle_info = m.get('VehicleInfo')
        return self


class Vehicle5ItemQueryResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: Vehicle5ItemQueryResponseBodyResultObject = None,
    ):
        # Return code
        self.code = code
        # Return message.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Returned result information.
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

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
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultObject') is not None:
            temp_model = Vehicle5ItemQueryResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class Vehicle5ItemQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Vehicle5ItemQueryResponseBody = None,
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
            temp_model = Vehicle5ItemQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VehicleInsureQueryRequest(TeaModel):
    def __init__(
        self,
        param_type: str = None,
        vehicle_num: str = None,
        vehicle_type: str = None,
        vin: str = None,
    ):
        # Parameter type:
        # 
        # - **normal**: Unencrypted.
        # - **md5**: MD5 encrypted.
        self.param_type = param_type
        # License plate number
        # > 
        # > - When `paramType` is set to `normal`, enter the plain text.
        # > - When `paramType` is set to `md5`, enter the plain text of all but the last two characters of the license plate + the MD5 encryption (32 lowercase characters) of the last two characters of the license plate.
        self.vehicle_num = vehicle_num
        # Driver\\"s license vehicle type.
        self.vehicle_type = vehicle_type
        # Vehicle identification code, i.e., the vehicle VIN
        # 
        # 
        # > 
        # > - When `paramType` is set to `normal`, enter the plain text.
        # > - When `paramType` is set to `md5`, enter the plain text of all but the last four characters of the VIN + the MD5 encryption (32 lowercase characters) of the last four characters of the VIN.
        self.vin = vin

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.param_type is not None:
            result['ParamType'] = self.param_type
        if self.vehicle_num is not None:
            result['VehicleNum'] = self.vehicle_num
        if self.vehicle_type is not None:
            result['VehicleType'] = self.vehicle_type
        if self.vin is not None:
            result['Vin'] = self.vin
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')
        if m.get('VehicleNum') is not None:
            self.vehicle_num = m.get('VehicleNum')
        if m.get('VehicleType') is not None:
            self.vehicle_type = m.get('VehicleType')
        if m.get('Vin') is not None:
            self.vin = m.get('Vin')
        return self


class VehicleInsureQueryResponseBodyResultObject(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        vehicle_info: str = None,
    ):
        # Verification result code:
        # 
        # > 
        # > - 1: Found (charged)
        # > - 3: No record found (not charged)
        self.biz_code = biz_code
        # Insurance date information
        self.vehicle_info = vehicle_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.vehicle_info is not None:
            result['VehicleInfo'] = self.vehicle_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('VehicleInfo') is not None:
            self.vehicle_info = m.get('VehicleInfo')
        return self


class VehicleInsureQueryResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: VehicleInsureQueryResponseBodyResultObject = None,
    ):
        # Return code: 200 indicates success, others indicate failure.
        self.code = code
        # Response message for the request information.
        self.message = message
        # Request ID
        self.request_id = request_id
        # Returned result information.
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

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
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultObject') is not None:
            temp_model = VehicleInsureQueryResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class VehicleInsureQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VehicleInsureQueryResponseBody = None,
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
            temp_model = VehicleInsureQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VehicleMetaVerifyRequest(TeaModel):
    def __init__(
        self,
        identify_num: str = None,
        param_type: str = None,
        user_name: str = None,
        vehicle_num: str = None,
        vehicle_type: str = None,
        verify_meta_type: str = None,
    ):
        # ID number.
        # 
        # This is a required field when VerifyMetaType is set to VEHICLE_3_META.
        # > 
        # > - When paramType is set to normal, enter the plain text.
        # > - When paramType is set to md5, enter the first 6 digits in plain text + the birth date encrypted with MD5 (32 lowercase characters) + the last 4 digits in plain text.
        self.identify_num = identify_num
        # Parameter type:
        # 
        # - normal: Unencrypted.
        # - md5: Encrypted with MD5.
        self.param_type = param_type
        # Name
        # 
        # > This is an explanation
        # > - When paramType is set to normal, enter the plain text.
        # > - When paramType is set to md5, encrypt the first character of the name with MD5 (32 lowercase characters) + the rest of the name in plain text.
        self.user_name = user_name
        # Vehicle license plate
        # 
        # > 
        # > - When paramType is set to normal, enter the plain text.
        # > - When paramType is set to md5, enter the part of the license plate except for the last two characters in plain text + the last two characters of the license plate encrypted with MD5 (32 lowercase characters).
        self.vehicle_num = vehicle_num
        # Vehicle type
        self.vehicle_type = vehicle_type
        # Verification type
        # 
        # > 
        # > - VEHICLE_2_META: Two-element verification, name + vehicle license plate verification;
        # > - VEHICLE_3_META: Three-element verification, name + vehicle license plate + ID number verification;
        self.verify_meta_type = verify_meta_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identify_num is not None:
            result['IdentifyNum'] = self.identify_num
        if self.param_type is not None:
            result['ParamType'] = self.param_type
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.vehicle_num is not None:
            result['VehicleNum'] = self.vehicle_num
        if self.vehicle_type is not None:
            result['VehicleType'] = self.vehicle_type
        if self.verify_meta_type is not None:
            result['VerifyMetaType'] = self.verify_meta_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdentifyNum') is not None:
            self.identify_num = m.get('IdentifyNum')
        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('VehicleNum') is not None:
            self.vehicle_num = m.get('VehicleNum')
        if m.get('VehicleType') is not None:
            self.vehicle_type = m.get('VehicleType')
        if m.get('VerifyMetaType') is not None:
            self.verify_meta_type = m.get('VerifyMetaType')
        return self


class VehicleMetaVerifyResponseBodyResultObject(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
    ):
        # Verification result.
        # 
        # - 1: Consistent (billable)
        # - 2: Inconsistent (billable)
        # - 3: No record found (non-billable)
        self.biz_code = biz_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        return self


class VehicleMetaVerifyResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: VehicleMetaVerifyResponseBodyResultObject = None,
    ):
        # Response code, **200** indicates that the API response was successful.
        self.code = code
        # Response message.
        self.message = message
        # ID of the request
        self.request_id = request_id
        # Returned result information.
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

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
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultObject') is not None:
            temp_model = VehicleMetaVerifyResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class VehicleMetaVerifyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VehicleMetaVerifyResponseBody = None,
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
            temp_model = VehicleMetaVerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VehicleMetaVerifyV2Request(TeaModel):
    def __init__(
        self,
        identify_num: str = None,
        param_type: str = None,
        user_name: str = None,
        vehicle_num: str = None,
        vehicle_type: str = None,
        verify_meta_type: str = None,
    ):
        # ID number.
        # 
        # This is a required field when VerifyMetaType is VEHICLE_3_META.
        # 
        # > 
        # > - When paramType is normal, enter plain text.
        # > - When paramType is md5, enter the first 6 digits in plain text + MD5 (32 lowercase) of the birth date + the last 4 digits in plain text.
        self.identify_num = identify_num
        # Parameter type:
        # 
        # - normal: Unencrypted.
        # - md5: Md5 encrypted.
        self.param_type = param_type
        # Name
        # > 
        # > - When paramType is normal, enter plain text.
        # > - When paramType is md5, enter the first character of the name as MD5 (32 lowercase) + the rest of the name in plain text.
        self.user_name = user_name
        # License plate number
        # 
        # > 
        # > - When paramType is normal, enter plain text.
        # > - When paramType is md5, enter all but the last two characters in plain text + the last two characters as MD5 (32 lowercase).
        self.vehicle_num = vehicle_num
        # Vehicle type
        self.vehicle_type = vehicle_type
        # Verification type
        # 
        # > 
        # > - VEHICLE_2_META: Two-element verification, name + license plate number verification;
        # > - VEHICLE_3_META: Three-element verification, name + license plate number + ID number verification;
        self.verify_meta_type = verify_meta_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identify_num is not None:
            result['IdentifyNum'] = self.identify_num
        if self.param_type is not None:
            result['ParamType'] = self.param_type
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.vehicle_num is not None:
            result['VehicleNum'] = self.vehicle_num
        if self.vehicle_type is not None:
            result['VehicleType'] = self.vehicle_type
        if self.verify_meta_type is not None:
            result['VerifyMetaType'] = self.verify_meta_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdentifyNum') is not None:
            self.identify_num = m.get('IdentifyNum')
        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('VehicleNum') is not None:
            self.vehicle_num = m.get('VehicleNum')
        if m.get('VehicleType') is not None:
            self.vehicle_type = m.get('VehicleType')
        if m.get('VerifyMetaType') is not None:
            self.verify_meta_type = m.get('VerifyMetaType')
        return self


class VehicleMetaVerifyV2ResponseBodyResultObject(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        vehicle_info: str = None,
    ):
        # Verification result code:
        # - **1**: Verification consistent.
        # - **2**: Verification inconsistent.
        # - **3**: No record found.
        self.biz_code = biz_code
        # Detailed vehicle information.
        self.vehicle_info = vehicle_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.vehicle_info is not None:
            result['VehicleInfo'] = self.vehicle_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('VehicleInfo') is not None:
            self.vehicle_info = m.get('VehicleInfo')
        return self


class VehicleMetaVerifyV2ResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: VehicleMetaVerifyV2ResponseBodyResultObject = None,
    ):
        # Return code, **200** indicates successful API response.
        self.code = code
        # Return message.
        self.message = message
        # Request ID
        self.request_id = request_id
        # Returned result
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

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
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultObject') is not None:
            temp_model = VehicleMetaVerifyV2ResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class VehicleMetaVerifyV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VehicleMetaVerifyV2ResponseBody = None,
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
            temp_model = VehicleMetaVerifyV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VehicleQueryRequest(TeaModel):
    def __init__(
        self,
        param_type: str = None,
        vehicle_num: str = None,
        vehicle_type: str = None,
    ):
        # Parameter type:
        # 
        # - **normal**: Unencrypted.
        # - **md5**: MD5 encrypted.
        self.param_type = param_type
        # License plate number
        # 
        # > 
        # > - When paramType is set to normal, enter the plain text.
        # > - When paramType is set to md5, enter the unencrypted part of the license plate number except for the last two characters + the MD5 (32 lowercase) encryption of the last two characters of the license plate.
        self.vehicle_num = vehicle_num
        # Vehicle type
        self.vehicle_type = vehicle_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.param_type is not None:
            result['ParamType'] = self.param_type
        if self.vehicle_num is not None:
            result['VehicleNum'] = self.vehicle_num
        if self.vehicle_type is not None:
            result['VehicleType'] = self.vehicle_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')
        if m.get('VehicleNum') is not None:
            self.vehicle_num = m.get('VehicleNum')
        if m.get('VehicleType') is not None:
            self.vehicle_type = m.get('VehicleType')
        return self


class VehicleQueryResponseBodyResultObject(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        vehicle_info: str = None,
    ):
        # Verification result code:
        # 
        # > 
        # > - 1: Found (charged)
        # > - 3: No record found (not charged)
        self.biz_code = biz_code
        # Vehicle information.
        self.vehicle_info = vehicle_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.vehicle_info is not None:
            result['VehicleInfo'] = self.vehicle_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('VehicleInfo') is not None:
            self.vehicle_info = m.get('VehicleInfo')
        return self


class VehicleQueryResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: VehicleQueryResponseBodyResultObject = None,
    ):
        # Return code: 200 for success, others for failure
        self.code = code
        # Return message.
        self.message = message
        # Request ID
        self.request_id = request_id
        # Request result
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

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
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultObject') is not None:
            temp_model = VehicleQueryResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class VehicleQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VehicleQueryResponseBody = None,
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
            temp_model = VehicleQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyMaterialRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_type: str = None,
        face_image_url: str = None,
        id_card_back_image_url: str = None,
        id_card_front_image_url: str = None,
        id_card_number: str = None,
        name: str = None,
        user_id: str = None,
    ):
        # A unique ID that identifies a single authentication task, not exceeding 64 characters. For a single authentication task, the system supports unlimited submissions until the final authentication is passed and the task is completed.
        # 
        # > Different BizIds are required for different authentication tasks.
        # 
        # This parameter is required.
        self.biz_id = biz_id
        # Identifier for the business scenario using the real-person authentication service. Please refer to [Business Setup](https://help.aliyun.com/document_detail/127885.html) and complete the creation in the console first.
        # 
        # This parameter is required.
        self.biz_type = biz_type
        # HTTP or HTTPS link to the frontal face image.
        # 
        # This parameter is required.
        self.face_image_url = face_image_url
        # HTTP or HTTPS link to the national emblem side of the ID card.
        self.id_card_back_image_url = id_card_back_image_url
        # HTTP or HTTPS link to the portrait side of the ID card image.
        self.id_card_front_image_url = id_card_front_image_url
        # ID number.
        # 
        # This parameter is required.
        self.id_card_number = id_card_number
        # Name.
        # 
        # This parameter is required.
        self.name = name
        # The ID of the end user, such as the account ID of the end user.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.face_image_url is not None:
            result['FaceImageUrl'] = self.face_image_url
        if self.id_card_back_image_url is not None:
            result['IdCardBackImageUrl'] = self.id_card_back_image_url
        if self.id_card_front_image_url is not None:
            result['IdCardFrontImageUrl'] = self.id_card_front_image_url
        if self.id_card_number is not None:
            result['IdCardNumber'] = self.id_card_number
        if self.name is not None:
            result['Name'] = self.name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('FaceImageUrl') is not None:
            self.face_image_url = m.get('FaceImageUrl')
        if m.get('IdCardBackImageUrl') is not None:
            self.id_card_back_image_url = m.get('IdCardBackImageUrl')
        if m.get('IdCardFrontImageUrl') is not None:
            self.id_card_front_image_url = m.get('IdCardFrontImageUrl')
        if m.get('IdCardNumber') is not None:
            self.id_card_number = m.get('IdCardNumber')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class VerifyMaterialResponseBodyMaterialIdCardInfo(TeaModel):
    def __init__(
        self,
        address: str = None,
        authority: str = None,
        back_image_url: str = None,
        birth: str = None,
        end_date: str = None,
        front_image_url: str = None,
        name: str = None,
        nationality: str = None,
        number: str = None,
        start_date: str = None,
    ):
        # Address.
        self.address = address
        # Issuing authority.
        self.authority = authority
        # HTTP or HTTPS link to the national emblem side of the ID card. The link is valid for 5 minutes. It is recommended to store it in your business system to avoid any impact on usage.
        self.back_image_url = back_image_url
        # Date of birth.
        self.birth = birth
        # End date of the document\\"s validity period. Format: yyyymmdd.
        self.end_date = end_date
        # HTTP or HTTPS link to the portrait side of the ID card. The link is valid for 5 minutes. It is recommended to store it in your business system to avoid any impact on usage.
        self.front_image_url = front_image_url
        # Name.
        self.name = name
        # Nationality.
        self.nationality = nationality
        # ID number.
        self.number = number
        # Start date of the document\\"s validity period. Format: yyyymmdd.
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.authority is not None:
            result['Authority'] = self.authority
        if self.back_image_url is not None:
            result['BackImageUrl'] = self.back_image_url
        if self.birth is not None:
            result['Birth'] = self.birth
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.front_image_url is not None:
            result['FrontImageUrl'] = self.front_image_url
        if self.name is not None:
            result['Name'] = self.name
        if self.nationality is not None:
            result['Nationality'] = self.nationality
        if self.number is not None:
            result['Number'] = self.number
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Authority') is not None:
            self.authority = m.get('Authority')
        if m.get('BackImageUrl') is not None:
            self.back_image_url = m.get('BackImageUrl')
        if m.get('Birth') is not None:
            self.birth = m.get('Birth')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('FrontImageUrl') is not None:
            self.front_image_url = m.get('FrontImageUrl')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Nationality') is not None:
            self.nationality = m.get('Nationality')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class VerifyMaterialResponseBodyMaterial(TeaModel):
    def __init__(
        self,
        face_global_url: str = None,
        face_image_url: str = None,
        face_mask: str = None,
        face_quality: str = None,
        id_card_info: VerifyMaterialResponseBodyMaterialIdCardInfo = None,
        id_card_name: str = None,
        id_card_number: str = None,
    ):
        # Global camera image captured by the real-person authentication SDK.
        # 
        # > This parameter will take effect after configuration. If you need to use this parameter, please submit a [ticket](https://selfservice.console.aliyun.com/ticket/category/cloudauth/today) to contact us.
        self.face_global_url = face_global_url
        # HTTP or HTTPS link to the frontal face image, corresponding to the request parameter **FaceImageUrl**. The link is valid for 5 minutes, and it is recommended to store it in your business to avoid affecting usage.
        self.face_image_url = face_image_url
        # Whether the face is wearing a mask. Values:
        # - **true**: Wearing a mask
        # - **false**: Not wearing a mask
        self.face_mask = face_mask
        # The quality of the frontal face image. Possible values:
        # - **UNQUALIFIED**: Poor quality
        # - **LOW**: Low
        # - **NORMAL**: Average
        # - **HIGH**: High
        self.face_quality = face_quality
        # OCR result of the ID card information.
        # 
        # > If there is no front or back of the ID card during the verification process, the OCR result of the ID card information will not be returned. Even if the front and back of the ID card are present during the verification process, it does not guarantee that all the information on the ID card will be returned. Due to issues such as poor ID card photography, the OCR may fail to recognize some information, leading to incomplete OCR results. It is recommended that the business side does not heavily rely on the ID card OCR information.
        self.id_card_info = id_card_info
        # Name, corresponding to the request parameter **Name**.
        self.id_card_name = id_card_name
        # ID number, corresponding to the request parameter **IdCardNumber**.
        self.id_card_number = id_card_number

    def validate(self):
        if self.id_card_info:
            self.id_card_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_global_url is not None:
            result['FaceGlobalUrl'] = self.face_global_url
        if self.face_image_url is not None:
            result['FaceImageUrl'] = self.face_image_url
        if self.face_mask is not None:
            result['FaceMask'] = self.face_mask
        if self.face_quality is not None:
            result['FaceQuality'] = self.face_quality
        if self.id_card_info is not None:
            result['IdCardInfo'] = self.id_card_info.to_map()
        if self.id_card_name is not None:
            result['IdCardName'] = self.id_card_name
        if self.id_card_number is not None:
            result['IdCardNumber'] = self.id_card_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceGlobalUrl') is not None:
            self.face_global_url = m.get('FaceGlobalUrl')
        if m.get('FaceImageUrl') is not None:
            self.face_image_url = m.get('FaceImageUrl')
        if m.get('FaceMask') is not None:
            self.face_mask = m.get('FaceMask')
        if m.get('FaceQuality') is not None:
            self.face_quality = m.get('FaceQuality')
        if m.get('IdCardInfo') is not None:
            temp_model = VerifyMaterialResponseBodyMaterialIdCardInfo()
            self.id_card_info = temp_model.from_map(m['IdCardInfo'])
        if m.get('IdCardName') is not None:
            self.id_card_name = m.get('IdCardName')
        if m.get('IdCardNumber') is not None:
            self.id_card_number = m.get('IdCardNumber')
        return self


class VerifyMaterialResponseBody(TeaModel):
    def __init__(
        self,
        authority_comparision_score: float = None,
        id_card_face_comparison_score: float = None,
        material: VerifyMaterialResponseBodyMaterial = None,
        request_id: str = None,
        verify_status: int = None,
        verify_token: str = None,
    ):
        # Comparison score between the facial photo submitted during the authentication process and authoritative data, with a range of **0**~**100**.
        # 
        # Confidence threshold references:
        # - False recognition rate 0.001% corresponds to a threshold of 95.
        # - False recognition rate 0.01% corresponds to a threshold of 90.
        # - False recognition rate 0.1% corresponds to a threshold of 80.
        # - False recognition rate 1% corresponds to a threshold of 60.
        # 
        # > This field only indicates the comparison result between the face and authoritative data, serving as a reference score. It is generally not recommended to use this score alone as the pass/fail criterion. For the comprehensive authentication result, please refer to the **VerifyStatus** field. The **VerifyStatus** result integrates the face-to-authoritative data comparison and other various strategies, enhancing security levels.
        self.authority_comparision_score = authority_comparision_score
        # Comparison score between the facial photo submitted during the authentication process and the face on the portrait side of the ID card image, with a range of **0**~**100**.
        # 
        # Confidence threshold references:
        # - False recognition rate 0.001% corresponds to a threshold of 95.
        # - False recognition rate 0.01% corresponds to a threshold of 90.
        # - False recognition rate 0.1% corresponds to a threshold of 80.
        # - False recognition rate 1% corresponds to a threshold of 60.
        self.id_card_face_comparison_score = id_card_face_comparison_score
        # Authentication materials.
        self.material = material
        # Request ID.
        self.request_id = request_id
        # Authentication status. Values:
        # 
        # - **1**: Authentication passed.
        # - **2**~**n**: Authentication failed due to various reasons. For detailed descriptions, see the **Authentication Status Explanation** below.
        self.verify_status = verify_status
        # Token for this authentication, used to link various interfaces in the authentication request, valid for 30 minutes.
        self.verify_token = verify_token

    def validate(self):
        if self.material:
            self.material.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authority_comparision_score is not None:
            result['AuthorityComparisionScore'] = self.authority_comparision_score
        if self.id_card_face_comparison_score is not None:
            result['IdCardFaceComparisonScore'] = self.id_card_face_comparison_score
        if self.material is not None:
            result['Material'] = self.material.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.verify_status is not None:
            result['VerifyStatus'] = self.verify_status
        if self.verify_token is not None:
            result['VerifyToken'] = self.verify_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorityComparisionScore') is not None:
            self.authority_comparision_score = m.get('AuthorityComparisionScore')
        if m.get('IdCardFaceComparisonScore') is not None:
            self.id_card_face_comparison_score = m.get('IdCardFaceComparisonScore')
        if m.get('Material') is not None:
            temp_model = VerifyMaterialResponseBodyMaterial()
            self.material = temp_model.from_map(m['Material'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VerifyStatus') is not None:
            self.verify_status = m.get('VerifyStatus')
        if m.get('VerifyToken') is not None:
            self.verify_token = m.get('VerifyToken')
        return self


class VerifyMaterialResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VerifyMaterialResponseBody = None,
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
            temp_model = VerifyMaterialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


