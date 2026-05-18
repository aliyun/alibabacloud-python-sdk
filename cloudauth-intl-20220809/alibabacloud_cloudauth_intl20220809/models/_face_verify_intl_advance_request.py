# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import BinaryIO

from darabonba.model import DaraModel

class FaceVerifyIntlAdvanceRequest(DaraModel):
    def __init__(
        self,
        auto_registration: str = None,
        face_group_codes: str = None,
        face_quality_check: str = None,
        face_register_group_code: str = None,
        merchant_biz_id: str = None,
        merchant_user_id: str = None,
        product_code: str = None,
        return_faces: str = None,
        source_face_picture: str = None,
        source_face_picture_file_object: BinaryIO = None,
        source_face_picture_url: str = None,
        target_face_picture: str = None,
        target_face_picture_file_object: BinaryIO = None,
        target_face_picture_url: str = None,
        verify_model: str = None,
    ):
        self.auto_registration = auto_registration
        self.face_group_codes = face_group_codes
        self.face_quality_check = face_quality_check
        self.face_register_group_code = face_register_group_code
        self.merchant_biz_id = merchant_biz_id
        self.merchant_user_id = merchant_user_id
        # This parameter is required.
        self.product_code = product_code
        self.return_faces = return_faces
        self.source_face_picture = source_face_picture
        self.source_face_picture_file_object = source_face_picture_file_object
        self.source_face_picture_url = source_face_picture_url
        self.target_face_picture = target_face_picture
        self.target_face_picture_file_object = target_face_picture_file_object
        self.target_face_picture_url = target_face_picture_url
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

        if self.source_face_picture_file_object is not None:
            result['SourceFacePictureFile'] = self.source_face_picture_file_object

        if self.source_face_picture_url is not None:
            result['SourceFacePictureUrl'] = self.source_face_picture_url

        if self.target_face_picture is not None:
            result['TargetFacePicture'] = self.target_face_picture

        if self.target_face_picture_file_object is not None:
            result['TargetFacePictureFile'] = self.target_face_picture_file_object

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
            self.source_face_picture_file_object = m.get('SourceFacePictureFile')

        if m.get('SourceFacePictureUrl') is not None:
            self.source_face_picture_url = m.get('SourceFacePictureUrl')

        if m.get('TargetFacePicture') is not None:
            self.target_face_picture = m.get('TargetFacePicture')

        if m.get('TargetFacePictureFile') is not None:
            self.target_face_picture_file_object = m.get('TargetFacePictureFile')

        if m.get('TargetFacePictureUrl') is not None:
            self.target_face_picture_url = m.get('TargetFacePictureUrl')

        if m.get('VerifyModel') is not None:
            self.verify_model = m.get('VerifyModel')

        return self

