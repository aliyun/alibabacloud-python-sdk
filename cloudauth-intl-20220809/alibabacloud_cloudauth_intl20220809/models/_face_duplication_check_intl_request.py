# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FaceDuplicationCheckIntlRequest(DaraModel):
    def __init__(
        self,
        auto_registration: str = None,
        face_group_codes: str = None,
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
        # Indicates whether to automatically register the face to the specified face library if no duplicate face is found.
        # - 0- Auto-register (default)
        # - 1- Do not register
        self.auto_registration = auto_registration
        # The face library code created through the console, supporting up to 10 face libraries simultaneously. When multiple face library codes are passed, they should be separated by commas.
        self.face_group_codes = face_group_codes
        # Face registration library.
        self.face_register_group_code = face_register_group_code
        # Face matching threshold.
        self.face_verify_threshold = face_verify_threshold
        # Whether to enable silent liveness detection
        # - 0- Disabled
        # - 1- Enabled
        self.liveness = liveness
        # A unique business identifier for troubleshooting purposes. It supports a combination of 32 alphanumeric characters, please ensure its uniqueness.
        # 
        # This parameter is required.
        self.merchant_biz_id = merchant_biz_id
        # Your custom user ID or other identifiers that can uniquely identify a specific user, such as a phone number or email address. It is strongly recommended to pre-desensitize the value of this field, for example, by hashing it.
        # 
        # This parameter is required.
        self.merchant_user_id = merchant_user_id
        # Product code
        # 
        # This parameter is required.
        self.product_code = product_code
        # When there are multiple faces above the matching threshold, you can use this parameter to customize the number of returned faces
        # - Default returns 1
        # - Maximum support 5
        self.return_faces = return_faces
        # Distinguishes between saving the face image and features
        # - 0- Face (default)
        # - 1- Features
        self.save_face_picture = save_face_picture
        # Your custom authentication scenario ID.
        self.scene_code = scene_code
        # Base64 encoded portrait photo.
        self.source_face_picture = source_face_picture
        # Portrait image URL, accessible via public HTTP or HTTPS link.
        self.source_face_picture_url = source_face_picture_url
        # Base64 encoded portrait photo.
        self.target_face_picture = target_face_picture
        # Portrait image URL, accessible via public HTTP or HTTPS link.
        self.target_face_picture_url = target_face_picture_url
        # Verification type
        # - 0- 1:N (default)
        # - 1- 1:1
        # - 2- 1:N + 1:1
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

