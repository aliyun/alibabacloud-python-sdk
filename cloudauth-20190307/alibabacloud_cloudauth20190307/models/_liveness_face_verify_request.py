# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class LivenessFaceVerifyRequest(DaraModel):
    def __init__(
        self,
        certify_id: str = None,
        crop: str = None,
        device_token: str = None,
        face_contrast_picture: str = None,
        face_contrast_picture_url: str = None,
        ip: str = None,
        mobile: str = None,
        model: str = None,
        oss_bucket_name: str = None,
        oss_object_name: str = None,
        outer_order_no: str = None,
        product_code: str = None,
        scene_id: int = None,
        user_id: str = None,
    ):
        # Unique identifier for real-person authentication.
        self.certify_id = certify_id
        # Whether to allow cropping of the face image:
        # 
        # - T: Allow cropping
        # 
        # - F (default): Do not allow cropping.
        self.crop = crop
        # Device token, used for risk identification.
        self.device_token = device_token
        # Base64 encoded photo.
        self.face_contrast_picture = face_contrast_picture
        # Image URL.
        self.face_contrast_picture_url = face_contrast_picture_url
        # User\\"s network IP address.
        self.ip = ip
        # User\\"s mobile phone number.
        self.mobile = mobile
        # Liveness detection parameters.
        self.model = model
        # Authorized OSS bucket name.
        self.oss_bucket_name = oss_bucket_name
        # Authorized OSS file name.
        self.oss_object_name = oss_object_name
        # A unique business identifier defined by the client side, used for subsequent troubleshooting. The value should be a combination of letters and numbers up to 32 characters long, ensuring uniqueness.
        self.outer_order_no = outer_order_no
        # Fixed value: LR_FR_MIN.
        self.product_code = product_code
        # Authentication scenario ID. This ID is automatically generated after creating an authentication scenario in the console.
        self.scene_id = scene_id
        # Your custom user ID (up to 100 characters), please ensure it is unique.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id

        if self.crop is not None:
            result['Crop'] = self.crop

        if self.device_token is not None:
            result['DeviceToken'] = self.device_token

        if self.face_contrast_picture is not None:
            result['FaceContrastPicture'] = self.face_contrast_picture

        if self.face_contrast_picture_url is not None:
            result['FaceContrastPictureUrl'] = self.face_contrast_picture_url

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.mobile is not None:
            result['Mobile'] = self.mobile

        if self.model is not None:
            result['Model'] = self.model

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

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')

        if m.get('Crop') is not None:
            self.crop = m.get('Crop')

        if m.get('DeviceToken') is not None:
            self.device_token = m.get('DeviceToken')

        if m.get('FaceContrastPicture') is not None:
            self.face_contrast_picture = m.get('FaceContrastPicture')

        if m.get('FaceContrastPictureUrl') is not None:
            self.face_contrast_picture_url = m.get('FaceContrastPictureUrl')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')

        if m.get('Model') is not None:
            self.model = m.get('Model')

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

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

