# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FaceCompareRequest(DaraModel):
    def __init__(
        self,
        face_picture_quality_check: str = None,
        face_quality_check: str = None,
        merchant_biz_id: str = None,
        source_face_picture: str = None,
        source_face_picture_url: str = None,
        target_face_picture: str = None,
        target_face_picture_url: str = None,
    ):
        # **[Deprecated]** Specifies whether to enable the quality check for the input face image.
        self.face_picture_quality_check = face_picture_quality_check
        # The face quality check.
        self.face_quality_check = face_quality_check
        # The custom unique business identifier on the merchant side, which is used for subsequent troubleshooting. It supports a combination of letters and digits, with a maximum length of 32 characters. Make sure that the identifier is unique.
        self.merchant_biz_id = merchant_biz_id
        # The Base64-encoded portrait photo.
        # 
        # Note
        # - If you choose this method to pass the ID photo, check the photo size and do not pass oversized photos.
        # - Specify either SourceFacePicture or SourceFacePictureUrl.
        self.source_face_picture = source_face_picture
        # The HTTPS or HTTP URL of the face image.
        self.source_face_picture_url = source_face_picture_url
        # The Base64-encoded reference photo.
        # 
        # Note
        # - If you choose this method to pass the ID photo, check the photo size and do not pass oversized photos.
        # - Specify either TargetFacePicture or TargetFacePictureUrl.
        self.target_face_picture = target_face_picture
        # The HTTPS or HTTP URL of the reference face image.
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

        if self.source_face_picture_url is not None:
            result['SourceFacePictureUrl'] = self.source_face_picture_url

        if self.target_face_picture is not None:
            result['TargetFacePicture'] = self.target_face_picture

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

        if m.get('SourceFacePictureUrl') is not None:
            self.source_face_picture_url = m.get('SourceFacePictureUrl')

        if m.get('TargetFacePicture') is not None:
            self.target_face_picture = m.get('TargetFacePicture')

        if m.get('TargetFacePictureUrl') is not None:
            self.target_face_picture_url = m.get('TargetFacePictureUrl')

        return self

