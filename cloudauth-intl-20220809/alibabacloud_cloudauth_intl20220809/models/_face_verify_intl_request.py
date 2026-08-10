# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FaceVerifyIntlRequest(DaraModel):
    def __init__(
        self,
        auto_registration: str = None,
        face_attribute_check: str = None,
        face_group_codes: str = None,
        face_quality_check: str = None,
        face_register_group_code: str = None,
        merchant_biz_id: str = None,
        merchant_user_id: str = None,
        product_code: str = None,
        return_faces: str = None,
        source_face_picture: str = None,
        source_face_picture_file: str = None,
        source_face_picture_url: str = None,
        target_face_picture: str = None,
        target_face_picture_file: str = None,
        target_face_picture_url: str = None,
        update_face_if_user_exists: str = None,
        verify_model: str = None,
    ):
        # Required when ProductCode=FACE_IDU_MIN.
        # 
        # Specifies whether to automatically register the face to the specified face library when no duplicate face is found during retrieval. Valid values:
        # - 0: automatic registration.
        # - 1: no registration (default).
        self.auto_registration = auto_registration
        self.face_attribute_check = face_attribute_check
        # Required when ProductCode=FACE_IDU_MIN.
        # 
        # The face library codes created by the customer through the console. A maximum of 10 face libraries can be queried simultaneously. Separate multiple face library codes with commas.
        self.face_group_codes = face_group_codes
        # Specifies whether to check the quality of the face image. Valid values:
        # - Y: enabled.
        # - N: disabled (default).
        self.face_quality_check = face_quality_check
        # Required when ProductCode=FACE_IDU_MIN.
        # 
        # The face library for registration.
        self.face_register_group_code = face_register_group_code
        # A custom unique business identifier used for subsequent troubleshooting. The value supports a combination of letters and numbers up to 32 characters in length. Ensure that the value is unique.
        self.merchant_biz_id = merchant_biz_id
        # A custom user ID or other identifier that can identify a specific user, such as a phone number or email address. We strongly recommend that you desensitize the value of this field in advance, for example, by hashing the value.
        self.merchant_user_id = merchant_user_id
        # The product code. Valid values: FACE_VERIFY_MIN and FACE_IDU_MIN.
        # 
        # This parameter is required.
        self.product_code = product_code
        # Required when ProductCode=FACE_IDU_MIN.
        # 
        # Specifies the number of faces to return when multiple faces exist above the matching threshold. You can customize the return quantity through this parameter.
        # - Default value: 1.
        # - Maximum value: 5.
        self.return_faces = return_faces
        # The Base64-encoded portrait image.
        # 
        # Note
        # 
        # - If you choose this method to pass in the image, check the image size and do not pass in an excessively large image.
        # - Specify one of the following parameters: SourceFacePicture, SourceFacePictureUrl, or SourceFacePictureFile.
        self.source_face_picture = source_face_picture
        # The file stream of the face image.
        self.source_face_picture_file = source_face_picture_file
        # The publicly accessible HTTPS URL of the portrait image.
        self.source_face_picture_url = source_face_picture_url
        # The Base64-encoded reference face image.
        # 
        # Note
        # 
        # - If you choose this method to pass in the image, check the image size and do not pass in an excessively large image.
        # - Specify one of the following parameters: TargetFacePicture, TargetFacePictureUrl, or TargetFacePictureFile.
        self.target_face_picture = target_face_picture
        # The file stream of the reference face image.
        self.target_face_picture_file = target_face_picture_file
        # The HTTPS URL of the reference face image.
        self.target_face_picture_url = target_face_picture_url
        # Specifies whether to overwrite the existing face with the current face during automatic registration if MerchantUserId already exists. Valid values:
        # - Y: overwrite.
        # - N: do not overwrite and return that the UserId already exists.
        self.update_face_if_user_exists = update_face_if_user_exists
        # Required when ProductCode=FACE_IDU_MIN.
        # The verification type. Valid values:
        # - 0: retrieval pattern.
        # > - Feature: Pass in a face library and a user face image (sourceFacePicture). The system automatically retrieves whether the specified face image (sourceFacePicture) already exists in the face library. Passive liveness detection can be enabled for the face image (sourceFacePicture).
        # > - Recommended scenario: Real-person create an account where duplicate registration is not allowed.
        # 
        # - 1 (default): authentication pattern.
        # > - Feature: Pass in a specified face image (sourceFacePicture) and a reference face image (TargetFacePicture). The system automatically authenticates whether the faces match. Passive liveness detection can be enabled for the specified face image (sourceFacePicture).
        # > - Recommended scenario: Authenticating the identity of the user when modifying logon credentials or account information.
        # 
        # - 2: comprehensive pattern.
        # > - Feature: Pass in a face library, a specified face image (sourceFacePicture), and a reference face image (TargetFacePicture). The system automatically retrieves whether the specified face image (sourceFacePicture) exists in the face library, authenticates whether it matches the reference face, and supports enabling passive liveness detection for the specified face image (sourceFacePicture).
        # > - Recommended scenario: Authenticating that the user is new and is performing the operation in person.
        self.verify_model = verify_model

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_registration is not None:
            result['AutoRegistration'] = self.auto_registration

        if self.face_attribute_check is not None:
            result['FaceAttributeCheck'] = self.face_attribute_check

        if self.face_group_codes is not None:
            result['FaceGroupCodes'] = self.face_group_codes

        if self.face_quality_check is not None:
            result['FaceQualityCheck'] = self.face_quality_check

        if self.face_register_group_code is not None:
            result['FaceRegisterGroupCode'] = self.face_register_group_code

        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id

        if self.merchant_user_id is not None:
            result['MerchantUserId'] = self.merchant_user_id

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.return_faces is not None:
            result['ReturnFaces'] = self.return_faces

        if self.source_face_picture is not None:
            result['SourceFacePicture'] = self.source_face_picture

        if self.source_face_picture_file is not None:
            result['SourceFacePictureFile'] = self.source_face_picture_file

        if self.source_face_picture_url is not None:
            result['SourceFacePictureUrl'] = self.source_face_picture_url

        if self.target_face_picture is not None:
            result['TargetFacePicture'] = self.target_face_picture

        if self.target_face_picture_file is not None:
            result['TargetFacePictureFile'] = self.target_face_picture_file

        if self.target_face_picture_url is not None:
            result['TargetFacePictureUrl'] = self.target_face_picture_url

        if self.update_face_if_user_exists is not None:
            result['UpdateFaceIfUserExists'] = self.update_face_if_user_exists

        if self.verify_model is not None:
            result['VerifyModel'] = self.verify_model

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRegistration') is not None:
            self.auto_registration = m.get('AutoRegistration')

        if m.get('FaceAttributeCheck') is not None:
            self.face_attribute_check = m.get('FaceAttributeCheck')

        if m.get('FaceGroupCodes') is not None:
            self.face_group_codes = m.get('FaceGroupCodes')

        if m.get('FaceQualityCheck') is not None:
            self.face_quality_check = m.get('FaceQualityCheck')

        if m.get('FaceRegisterGroupCode') is not None:
            self.face_register_group_code = m.get('FaceRegisterGroupCode')

        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')

        if m.get('MerchantUserId') is not None:
            self.merchant_user_id = m.get('MerchantUserId')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ReturnFaces') is not None:
            self.return_faces = m.get('ReturnFaces')

        if m.get('SourceFacePicture') is not None:
            self.source_face_picture = m.get('SourceFacePicture')

        if m.get('SourceFacePictureFile') is not None:
            self.source_face_picture_file = m.get('SourceFacePictureFile')

        if m.get('SourceFacePictureUrl') is not None:
            self.source_face_picture_url = m.get('SourceFacePictureUrl')

        if m.get('TargetFacePicture') is not None:
            self.target_face_picture = m.get('TargetFacePicture')

        if m.get('TargetFacePictureFile') is not None:
            self.target_face_picture_file = m.get('TargetFacePictureFile')

        if m.get('TargetFacePictureUrl') is not None:
            self.target_face_picture_url = m.get('TargetFacePictureUrl')

        if m.get('UpdateFaceIfUserExists') is not None:
            self.update_face_if_user_exists = m.get('UpdateFaceIfUserExists')

        if m.get('VerifyModel') is not None:
            self.verify_model = m.get('VerifyModel')

        return self

