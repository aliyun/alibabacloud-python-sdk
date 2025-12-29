# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import BinaryIO

from darabonba.model import DaraModel

class ContrastFaceVerifyAdvanceRequest(DaraModel):
    def __init__(
        self,
        cert_name: str = None,
        cert_no: str = None,
        cert_type: str = None,
        certify_id: str = None,
        crop: str = None,
        device_token: str = None,
        encrypt_type: str = None,
        face_contrast_file_object: BinaryIO = None,
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
        # Real name.
        self.cert_name = cert_name
        # ID number
        self.cert_no = cert_no
        # Type of identification. Currently, only IDENTITY_CARD is supported and must be provided.
        self.cert_type = cert_type
        # The CertifyId of a previously passed real-person authentication, with the photo taken during that authentication used as the comparison photo. 
        # > Among the four ways to input images (FaceContrastPicture, FaceContrastPictureUrl, CertifyId, OSS), choose one to provide.
        self.certify_id = certify_id
        # Allow face image cropping:
        # 
        # -  **T** – Cropping is allowed.
        # -  **F** (default) – Cropping is not allowed.
        self.crop = crop
        # Risk Identification - Device Token
        self.device_token = device_token
        # Encryption type. Leave it empty if no encryption is required.
        # 
        # If you enable encrypted transmission, you must specify the encryption algorithm; currently, only the SM2 (Chinese national standard) algorithm is supported.
        # 
        # When an encryption algorithm is specified, encrypt both **CertName** and **CertNo** and submit the resulting ciphertext. For more details on parameter encryption, see the [Parameter Encryption documentation](https://help.aliyun.com/zh/id-verification/financial-grade-id-verification/description-of-parameter-encryption?spm=a2c4g.11186623.0.0.49541a8554cELI#task-2229332).
        self.encrypt_type = encrypt_type
        # Local video file.
        self.face_contrast_file_object = face_contrast_file_object
        # Base64 encoded photo
        self.face_contrast_picture = face_contrast_picture
        # OSS photo URL, currently only supports authorized OSS photo URLs.
        # > Among the four ways to input images (FaceContrastPicture, FaceContrastPictureUrl, CertifyId, OSS), choose one to input.
        self.face_contrast_picture_url = face_contrast_picture_url
        # User IP.
        self.ip = ip
        # User\\"s phone number.
        self.mobile = mobile
        # Liveness detection type. Possible values:
        # 
        # • **NO_LIVENESS** – Liveness detection is disabled.
        # 
        # • **FRONT_CAMERA_LIVENESS** (default) – Liveness detection on face images captured with the mobile device’s front camera.
        # 
        # • **REAR_CAMERA_LIVENESS** – Liveness detection on face images captured in other scenarios (e.g., via the rear camera).
        self.model = model
        # Authorized OSS space Bucket name. In the methods of passing images, including FaceContrastPicture, FaceContrastPictureUrl, CertifyId, and OSS, choose one to pass in.
        self.oss_bucket_name = oss_bucket_name
        # Filename of the authorized OSS space.
        # > Among the four ways to input images (FaceContrastPicture, FaceContrastPictureUrl, CertifyId, OSS), choose one to input.
        self.oss_object_name = oss_object_name
        # A unique identifier for the merchant\\"s request. It is a 32-character alphanumeric combination. The first few characters are a custom abbreviation defined by the merchant, followed by a period, and the latter part can be a random or incrementing sequence.
        self.outer_order_no = outer_order_no
        # Fixed value: ID_MIN.
        self.product_code = product_code
        # Authentication scenario ID.
        self.scene_id = scene_id
        # Custom user ID defined by the customer\\"s business.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_name is not None:
            result['CertName'] = self.cert_name

        if self.cert_no is not None:
            result['CertNo'] = self.cert_no

        if self.cert_type is not None:
            result['CertType'] = self.cert_type

        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id

        if self.crop is not None:
            result['Crop'] = self.crop

        if self.device_token is not None:
            result['DeviceToken'] = self.device_token

        if self.encrypt_type is not None:
            result['EncryptType'] = self.encrypt_type

        if self.face_contrast_file_object is not None:
            result['FaceContrastFile'] = self.face_contrast_file_object

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
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')

        if m.get('CertNo') is not None:
            self.cert_no = m.get('CertNo')

        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')

        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')

        if m.get('Crop') is not None:
            self.crop = m.get('Crop')

        if m.get('DeviceToken') is not None:
            self.device_token = m.get('DeviceToken')

        if m.get('EncryptType') is not None:
            self.encrypt_type = m.get('EncryptType')

        if m.get('FaceContrastFile') is not None:
            self.face_contrast_file_object = m.get('FaceContrastFile')

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

