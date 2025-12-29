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

