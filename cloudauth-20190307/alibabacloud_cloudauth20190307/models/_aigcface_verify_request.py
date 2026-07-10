# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AIGCFaceVerifyRequest(DaraModel):
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
        # The Base64-encoded photo.
        # > You can use one of the following methods to pass in the image: FaceContrastPicture, FaceContrastPictureUrl, or OSS.
        self.face_contrast_picture = face_contrast_picture
        # The URL of the face image. The URL must be a publicly accessible HTTP or HTTPS link.
        # 
        # > You can use one of the following methods to pass in the image: FaceContrastPicture, FaceContrastPictureUrl, or OSS.
        self.face_contrast_picture_url = face_contrast_picture_url
        # The name of the authorized OSS bucket.
        # > You can use one of the following methods to pass in the image: FaceContrastPicture, FaceContrastPictureUrl, or OSS.
        self.oss_bucket_name = oss_bucket_name
        # The file name in the authorized OSS bucket.
        # > You can use one of the following methods to pass in the image: FaceContrastPicture, FaceContrastPictureUrl, or OSS.
        self.oss_object_name = oss_object_name
        # The custom business unique identifier on the client side, used for subsequent troubleshooting. The value can contain up to 32 characters, including letters and digits. Make sure the value is unique.
        self.outer_order_no = outer_order_no
        # The product plan.
        self.product_code = product_code
        # The ID of the verification scenario. This ID is automatically generated after you create a verification scenario in the console. For more information about how to create a verification scenario, refer to Add a verification scenario.
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

