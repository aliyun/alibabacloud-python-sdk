# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FaceDuplicationCheckIntlRequest(DaraModel):
    def __init__(
        self,
        auto_registration: str = None,
        face_attribute_check: str = None,
        face_group_codes: str = None,
        face_quality_check: str = None,
        face_register_group_code: str = None,
        face_verify_threshold: str = None,
        liveness: str = None,
        merchant_biz_id: str = None,
        merchant_user_id: str = None,
        product_code: str = None,
        return_faces: str = None,
        save_face_picture: str = None,
        scene_code: str = None,
        source_face_picture: str = None,
        source_face_picture_url: str = None,
        target_face_picture: str = None,
        target_face_picture_url: str = None,
        update_face_if_user_exists: str = None,
        verify_model: str = None,
    ):
        # Specifies whether to automatically register the face to the specified face library if no duplicate face is found during the search. Valid values:
        # - 0: Register.
        # - 1: Do not register. This is the default value.
        self.auto_registration = auto_registration
        # Specifies whether to return additional face attribute information. Valid values:
        # - N: Do not return. This is the default value.
        # - Y: Return. The result is located in Result.ExtFaceInfo.FaceAttributeInfo.
        self.face_attribute_check = face_attribute_check
        # The codes of the face libraries created by the customer in the console. A maximum of 10 face libraries can be queried at the same time. Separate multiple face library codes with commas.
        self.face_group_codes = face_group_codes
        # The face quality check.
        self.face_quality_check = face_quality_check
        # The code of the face library for face registration.
        self.face_register_group_code = face_register_group_code
        # The face matching threshold. <warning>Reserved field. Not enabled yet.</warning>
        self.face_verify_threshold = face_verify_threshold
        # Specifies whether to enable passive liveness detection. Valid values:
        # - 0: Disable.
        # - 1: Enable.
        self.liveness = liveness
        # The custom unique business identifier used for subsequent troubleshooting. The value supports a combination of up to 32 letters and digits. Make sure that the value is unique.
        # 
        # This parameter is required.
        self.merchant_biz_id = merchant_biz_id
        # The custom user ID or other identifier that can identify a specific user, such as a mobile phone number or email address. Desensitize the value of this field in advance, such as by hashing the value.
        # 
        # This parameter is required.
        self.merchant_user_id = merchant_user_id
        # The product code.
        # 
        # This parameter is required.
        self.product_code = product_code
        # Specifies the number of faces to return when multiple faces exceed the matching threshold. Default value: 1. Maximum value: 5.
        self.return_faces = return_faces
        # Specifies the type of face data to save. Valid values:
        # - 0: Face image. This is the default value.
        # - 1: Face feature.
        # <warning>Reserved field. Not enabled yet.</warning>
        self.save_face_picture = save_face_picture
        # The custom authentication scene ID.
        self.scene_code = scene_code
        # The Base64-encoded portrait photo.
        self.source_face_picture = source_face_picture
        # The URL of the portrait image. The URL must be a publicly accessible HTTP or HTTPS link.
        self.source_face_picture_url = source_face_picture_url
        # The Base64-encoded portrait photo.
        self.target_face_picture = target_face_picture
        # The URL of the portrait image. The URL must be a publicly accessible HTTP or HTTPS link.
        self.target_face_picture_url = target_face_picture_url
        # Specifies whether to overwrite the original face with the current face if the MerchantUserId already exists during automatic registration. Valid values:
        # - Y: Overwrite.
        # - N: Do not overwrite and return that the UserId already exists.
        self.update_face_if_user_exists = update_face_if_user_exists
        # The authentication type. Valid values:
        # - 0: Retrieve pattern
        #   - Feature: The system receives a face library and a user face image (sourceFacePicture), and automatically retrieves from the face library to check whether the specified face image (sourceFacePicture) already exists. Passive liveness detection can be enabled for the face image (sourceFacePicture).
        #   - Recommended scenario: Scenarios where a real person needs to create an account and duplicate registration is not allowed.
        # - 1 (default): Authenticate pattern
        #   - Feature: The system receives a specified face image (sourceFacePicture) and a retained face image (TargetFacePicture), and automatically authenticates whether the faces match. Passive liveness detection can be enabled for the specified face image (sourceFacePicture).
        #   - Recommended scenario: Scenarios where it is required to authenticate whether the operation is performed by the user when modifying logon or account information.
        # - 2: Comprehensive pattern
        #   - Feature: The system receives a face library, a specified face image (sourceFacePicture), and a retained face image (TargetFacePicture) at the same time, and automatically retrieves from the face library to check whether the specified face image (sourceFacePicture) exists and authenticates whether it matches the retained face. Passive liveness detection can be enabled for the specified face image (sourceFacePicture).
        #   - Recommended scenario: Scenarios where it is required to authenticate that the user is a new user and the operation is performed by the user.
        # 
        # This parameter is required.
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

        if self.face_verify_threshold is not None:
            result['FaceVerifyThreshold'] = self.face_verify_threshold

        if self.liveness is not None:
            result['Liveness'] = self.liveness

        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id

        if self.merchant_user_id is not None:
            result['MerchantUserId'] = self.merchant_user_id

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.return_faces is not None:
            result['ReturnFaces'] = self.return_faces

        if self.save_face_picture is not None:
            result['SaveFacePicture'] = self.save_face_picture

        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code

        if self.source_face_picture is not None:
            result['SourceFacePicture'] = self.source_face_picture

        if self.source_face_picture_url is not None:
            result['SourceFacePictureUrl'] = self.source_face_picture_url

        if self.target_face_picture is not None:
            result['TargetFacePicture'] = self.target_face_picture

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

        if m.get('FaceVerifyThreshold') is not None:
            self.face_verify_threshold = m.get('FaceVerifyThreshold')

        if m.get('Liveness') is not None:
            self.liveness = m.get('Liveness')

        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')

        if m.get('MerchantUserId') is not None:
            self.merchant_user_id = m.get('MerchantUserId')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ReturnFaces') is not None:
            self.return_faces = m.get('ReturnFaces')

        if m.get('SaveFacePicture') is not None:
            self.save_face_picture = m.get('SaveFacePicture')

        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')

        if m.get('SourceFacePicture') is not None:
            self.source_face_picture = m.get('SourceFacePicture')

        if m.get('SourceFacePictureUrl') is not None:
            self.source_face_picture_url = m.get('SourceFacePictureUrl')

        if m.get('TargetFacePicture') is not None:
            self.target_face_picture = m.get('TargetFacePicture')

        if m.get('TargetFacePictureUrl') is not None:
            self.target_face_picture_url = m.get('TargetFacePictureUrl')

        if m.get('UpdateFaceIfUserExists') is not None:
            self.update_face_if_user_exists = m.get('UpdateFaceIfUserExists')

        if m.get('VerifyModel') is not None:
            self.verify_model = m.get('VerifyModel')

        return self

