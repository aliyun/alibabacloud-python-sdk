# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import BinaryIO

from darabonba.model import DaraModel

class FaceCompareV2AdvanceRequest(DaraModel):
    def __init__(
        self,
        face_picture_quality_check: str = None,
        face_quality_check: str = None,
        merchant_biz_id: str = None,
        source_face_picture: str = None,
        source_face_picture_file_object: BinaryIO = None,
        source_face_picture_url: str = None,
        target_face_picture: str = None,
        target_face_picture_file_object: BinaryIO = None,
        target_face_picture_url: str = None,
    ):
        self.face_picture_quality_check = face_picture_quality_check
        self.face_quality_check = face_quality_check
        self.merchant_biz_id = merchant_biz_id
        self.source_face_picture = source_face_picture
        self.source_face_picture_file_object = source_face_picture_file_object
        self.source_face_picture_url = source_face_picture_url
        self.target_face_picture = target_face_picture
        self.target_face_picture_file_object = target_face_picture_file_object
        self.target_face_picture_url = target_face_picture_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.face_picture_quality_check is not None:
            result['FacePictureQualityCheck'] = self.face_picture_quality_check

        if self.face_quality_check is not None:
            result['FaceQualityCheck'] = self.face_quality_check

        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FacePictureQualityCheck') is not None:
            self.face_picture_quality_check = m.get('FacePictureQualityCheck')

        if m.get('FaceQualityCheck') is not None:
            self.face_quality_check = m.get('FaceQualityCheck')

        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')

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

        return self

