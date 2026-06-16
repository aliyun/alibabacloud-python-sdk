# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FaceDuplicationCheckIntlRequest(DaraModel):
    def __init__(
        self,
        auto_registration: str = None,
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
        verify_model: str = None,
    ):
        # Specifies whether to automatically register the face in the specified face database when no duplicate face is found during the search. Valid values:
        # - 0: automatic registration
        # - 1: no registration (default).
        self.auto_registration = auto_registration
        # The face database codes created in the console. A maximum of 10 face databases can be queried at a time. Separate multiple face database codes with commas (,).
        self.face_group_codes = face_group_codes
        # Specifies whether to enable face quality check.
        self.face_quality_check = face_quality_check
        # The face database for registration.
        self.face_register_group_code = face_register_group_code
        # The face matching threshold. >Warning: This is a reserved field and is not currently enabled.</warning>.
        self.face_verify_threshold = face_verify_threshold
        # Specifies whether to enable passive liveness detection. Valid values:
        # - 0: disabled
        # - 1: enabled.
        self.liveness = liveness
        # The custom unique business identifier, which is used for subsequent troubleshooting. The value is a combination of letters and digits up to 32 characters in length. Ensure that the value is unique.
        # 
        # This parameter is required.
        self.merchant_biz_id = merchant_biz_id
        # The custom user ID or another identifier that can identify a specific user, such as a phone number or email address. We strongly recommend that you desensitize the value of this field in advance, for example, by hashing the value.
        # 
        # This parameter is required.
        self.merchant_user_id = merchant_user_id
        # The product code.
        # 
        # This parameter is required.
        self.product_code = product_code
        # The number of faces to return when multiple faces above the matching threshold are found.
        # - Default value: 1.
        # - Maximum value: 5.
        self.return_faces = return_faces
        # Specifies the type of face data to save. Valid values:
        # - 0: face image (default)
        # - 1: feature
        # >Warning: This is a reserved field and is not currently enabled.</warning>.
        self.save_face_picture = save_face_picture
        # The custom verification scenario ID.
        self.scene_code = scene_code
        # The Base64-encoded facial image.
        self.source_face_picture = source_face_picture
        # The URL of the facial image. The URL must be a publicly accessible HTTP or HTTPS link.
        self.source_face_picture_url = source_face_picture_url
        # The Base64-encoded facial image.
        self.target_face_picture = target_face_picture
        # The URL of the facial image. The URL must be a publicly accessible HTTP or HTTPS link.
        self.target_face_picture_url = target_face_picture_url
        # The verification type. Valid values:
        # - 0: retrieve pattern
        # > - Feature: Submits a face database and a user facial image (sourceFacePicture). The system automatically retrieves the face database to check whether the specified facial image (sourceFacePicture) already exists. Passive liveness detection can be enabled for the facial image (sourceFacePicture).
        # > - Recommended scenario: Real-person create an account where duplicate registration is not allowed.
        # 
        # - 1 (default): authenticate pattern
        # > - Feature: Submits a specified facial image (sourceFacePicture) and a stored facial image (TargetFacePicture). The system automatically authenticates whether the two faces match. Passive liveness detection can be enabled for the specified facial image (sourceFacePicture).
        # > - Recommended scenario: Authenticating whether the operation is performed by the account owner when logon credentials or account information is modified.
        # 
        # - 2: comprehensive pattern
        # > - Feature: Submits a face database, a specified facial image (sourceFacePicture), and a stored facial image (TargetFacePicture). The system automatically retrieves the face database to check whether the specified facial image (sourceFacePicture) exists and whether it matches the stored face. Passive liveness detection can be enabled for the specified facial image (sourceFacePicture).
        # > - Recommended scenario: Authenticating that the user is new and the operation is performed by the user.
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

        if self.verify_model is not None:
            result['VerifyModel'] = self.verify_model

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRegistration') is not None:
            self.auto_registration = m.get('AutoRegistration')

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

        if m.get('VerifyModel') is not None:
            self.verify_model = m.get('VerifyModel')

        return self

