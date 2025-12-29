# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CompareFaceVerifyRequest(DaraModel):
    def __init__(
        self,
        crop: str = None,
        outer_order_no: str = None,
        product_code: str = None,
        scene_id: int = None,
        source_certify_id: str = None,
        source_face_contrast_picture: str = None,
        source_face_contrast_picture_url: str = None,
        source_oss_bucket_name: str = None,
        source_oss_object_name: str = None,
        target_certify_id: str = None,
        target_face_contrast_picture: str = None,
        target_face_contrast_picture_url: str = None,
        target_oss_bucket_name: str = None,
        target_oss_object_name: str = None,
    ):
        # Whether cropping is allowed. Default is not allowed, T/F.
        # 
        # - T: Indicates that cropping is required
        # - F: Indicates that cropping is not required (default F)
        self.crop = crop
        # A unique identifier for the merchant\\"s request. The value is a 32-character alphanumeric combination, where the first few characters are a custom abbreviation defined by the merchant, followed by a period, and the latter part can be a random or incrementing sequence.
        self.outer_order_no = outer_order_no
        # Fixed value: PV_FC.
        self.product_code = product_code
        # Authentication scenario ID.
        self.scene_id = scene_id
        # The CertifyId of a previously successful real-person verification, where the photo taken during that verification is used as the face comparison photo.
        # > Among the four ways to input facial photos (FaceContrastPicture, FaceContrastPictureUrl, CertifyId, OSS), choose one to provide.
        self.source_certify_id = source_certify_id
        # Base64 encoding of the photo.
        # > Choose one of the four ways to input a face photo: FaceContrastPicture, FaceContrastPictureUrl, CertifyId, or OSS.
        self.source_face_contrast_picture = source_face_contrast_picture
        # OSS photo URL, currently only supports authorized OSS photo URLs.
        # > Four ways to input face photos: FaceContrastPicture, FaceContrastPictureUrl, CertifyId, and OSS. Choose one of them to input.
        self.source_face_contrast_picture_url = source_face_contrast_picture_url
        # Name of the authorized OSS bucket.
        # > Choose one of the four ways to input face photos: FaceContrastPicture, FaceContrastPictureUrl, CertifyId, or OSS.
        self.source_oss_bucket_name = source_oss_bucket_name
        # Filename of the authorized OSS space.
        # > Choose one of the four ways to input face photos: FaceContrastPicture, FaceContrastPictureUrl, CertifyId, or OSS.
        self.source_oss_object_name = source_oss_object_name
        # CertifyId from a previously successful real-person authentication, where the photo taken during the authentication is used for face comparison.
        # 
        # > Choose one of the four methods to provide the reference face photo: FaceContrastPicture, FaceContrastPictureUrl, CertifyId, or OSS.
        self.target_certify_id = target_certify_id
        # Base64 encoding of the reference photo.
        # 
        # > Choose one of the four methods to provide the reference face photo: FaceContrastPicture, FaceContrastPictureUrl, CertifyId, or OSS.
        self.target_face_contrast_picture = target_face_contrast_picture
        # OSS address of the reference photo. Currently, only authorized OSS addresses are supported.
        # 
        # > Choose one of the four methods to provide the reference face photo: FaceContrastPicture, FaceContrastPictureUrl, CertifyId, or OSS.
        self.target_face_contrast_picture_url = target_face_contrast_picture_url
        # Name of the authorized OSS bucket.
        # 
        # > Choose one of the four methods to provide the reference face photo: FaceContrastPicture, FaceContrastPictureUrl, CertifyId, or OSS.
        self.target_oss_bucket_name = target_oss_bucket_name
        # File name in the authorized OSS space.
        # 
        # > Choose one of the four methods to provide the reference face photo: FaceContrastPicture, FaceContrastPictureUrl, CertifyId, or OSS.
        self.target_oss_object_name = target_oss_object_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.crop is not None:
            result['Crop'] = self.crop

        if self.outer_order_no is not None:
            result['OuterOrderNo'] = self.outer_order_no

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        if self.source_certify_id is not None:
            result['SourceCertifyId'] = self.source_certify_id

        if self.source_face_contrast_picture is not None:
            result['SourceFaceContrastPicture'] = self.source_face_contrast_picture

        if self.source_face_contrast_picture_url is not None:
            result['SourceFaceContrastPictureUrl'] = self.source_face_contrast_picture_url

        if self.source_oss_bucket_name is not None:
            result['SourceOssBucketName'] = self.source_oss_bucket_name

        if self.source_oss_object_name is not None:
            result['SourceOssObjectName'] = self.source_oss_object_name

        if self.target_certify_id is not None:
            result['TargetCertifyId'] = self.target_certify_id

        if self.target_face_contrast_picture is not None:
            result['TargetFaceContrastPicture'] = self.target_face_contrast_picture

        if self.target_face_contrast_picture_url is not None:
            result['TargetFaceContrastPictureUrl'] = self.target_face_contrast_picture_url

        if self.target_oss_bucket_name is not None:
            result['TargetOssBucketName'] = self.target_oss_bucket_name

        if self.target_oss_object_name is not None:
            result['TargetOssObjectName'] = self.target_oss_object_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Crop') is not None:
            self.crop = m.get('Crop')

        if m.get('OuterOrderNo') is not None:
            self.outer_order_no = m.get('OuterOrderNo')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        if m.get('SourceCertifyId') is not None:
            self.source_certify_id = m.get('SourceCertifyId')

        if m.get('SourceFaceContrastPicture') is not None:
            self.source_face_contrast_picture = m.get('SourceFaceContrastPicture')

        if m.get('SourceFaceContrastPictureUrl') is not None:
            self.source_face_contrast_picture_url = m.get('SourceFaceContrastPictureUrl')

        if m.get('SourceOssBucketName') is not None:
            self.source_oss_bucket_name = m.get('SourceOssBucketName')

        if m.get('SourceOssObjectName') is not None:
            self.source_oss_object_name = m.get('SourceOssObjectName')

        if m.get('TargetCertifyId') is not None:
            self.target_certify_id = m.get('TargetCertifyId')

        if m.get('TargetFaceContrastPicture') is not None:
            self.target_face_contrast_picture = m.get('TargetFaceContrastPicture')

        if m.get('TargetFaceContrastPictureUrl') is not None:
            self.target_face_contrast_picture_url = m.get('TargetFaceContrastPictureUrl')

        if m.get('TargetOssBucketName') is not None:
            self.target_oss_bucket_name = m.get('TargetOssBucketName')

        if m.get('TargetOssObjectName') is not None:
            self.target_oss_object_name = m.get('TargetOssObjectName')

        return self

