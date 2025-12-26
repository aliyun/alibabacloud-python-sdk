# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FaceCrossCompareIntlRequest(DaraModel):
    def __init__(
        self,
        compare_model: str = None,
        face_verify_threshold: str = None,
        merchant_biz_id: str = None,
        product_code: str = None,
        scene_code: str = None,
        source_aface_picture: str = None,
        source_aface_picture_url: str = None,
        source_bface_picture: str = None,
        source_bface_picture_url: str = None,
        source_cface_picture: str = None,
        source_cface_picture_url: str = None,
    ):
        # Comparison mode
        # - 0-Chain comparison (default): A:B and B:C
        # - 1-Circular comparison: A:B and B:C and C:A
        self.compare_model = compare_model
        # Face matching threshold.
        self.face_verify_threshold = face_verify_threshold
        # A unique business identifier for subsequent troubleshooting. It supports a combination of 32 alphanumeric characters, please ensure its uniqueness.
        # 
        # This parameter is required.
        self.merchant_biz_id = merchant_biz_id
        # Product solution to be integrated. Value: 
        # FACE_CROSS_COMPARE
        # 
        # This parameter is required.
        self.product_code = product_code
        # Custom business scenario ID
        self.scene_code = scene_code
        self.source_aface_picture = source_aface_picture
        # Portrait image URL, accessible via HTTP or HTTPS on the public network.
        self.source_aface_picture_url = source_aface_picture_url
        self.source_bface_picture = source_bface_picture
        # Portrait image URL, accessible via HTTP or HTTPS on the public network.
        self.source_bface_picture_url = source_bface_picture_url
        self.source_cface_picture = source_cface_picture
        # Portrait image URL, accessible via HTTP or HTTPS on the public network.
        self.source_cface_picture_url = source_cface_picture_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compare_model is not None:
            result['CompareModel'] = self.compare_model

        if self.face_verify_threshold is not None:
            result['FaceVerifyThreshold'] = self.face_verify_threshold

        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code

        if self.source_aface_picture is not None:
            result['SourceAFacePicture'] = self.source_aface_picture

        if self.source_aface_picture_url is not None:
            result['SourceAFacePictureUrl'] = self.source_aface_picture_url

        if self.source_bface_picture is not None:
            result['SourceBFacePicture'] = self.source_bface_picture

        if self.source_bface_picture_url is not None:
            result['SourceBFacePictureUrl'] = self.source_bface_picture_url

        if self.source_cface_picture is not None:
            result['SourceCFacePicture'] = self.source_cface_picture

        if self.source_cface_picture_url is not None:
            result['SourceCFacePictureUrl'] = self.source_cface_picture_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompareModel') is not None:
            self.compare_model = m.get('CompareModel')

        if m.get('FaceVerifyThreshold') is not None:
            self.face_verify_threshold = m.get('FaceVerifyThreshold')

        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')

        if m.get('SourceAFacePicture') is not None:
            self.source_aface_picture = m.get('SourceAFacePicture')

        if m.get('SourceAFacePictureUrl') is not None:
            self.source_aface_picture_url = m.get('SourceAFacePictureUrl')

        if m.get('SourceBFacePicture') is not None:
            self.source_bface_picture = m.get('SourceBFacePicture')

        if m.get('SourceBFacePictureUrl') is not None:
            self.source_bface_picture_url = m.get('SourceBFacePictureUrl')

        if m.get('SourceCFacePicture') is not None:
            self.source_cface_picture = m.get('SourceCFacePicture')

        if m.get('SourceCFacePictureUrl') is not None:
            self.source_cface_picture_url = m.get('SourceCFacePictureUrl')

        return self

