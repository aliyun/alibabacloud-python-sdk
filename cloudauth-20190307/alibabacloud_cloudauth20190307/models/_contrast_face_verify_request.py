# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ContrastFaceVerifyRequest(DaraModel):
    def __init__(
        self,
        cert_name: str = None,
        cert_no: str = None,
        cert_type: str = None,
        certify_id: str = None,
        crop: str = None,
        device_token: str = None,
        encrypt_type: str = None,
        face_contrast_file: str = None,
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
        # The real name.
        self.cert_name = cert_name
        # The certificate number.
        self.cert_no = cert_no
        # The certificate type.
        # Currently only ID cards are supported. You must set this parameter to IDENTITY_CARD.
        self.cert_type = cert_type
        # The CertifyId from a previous successful ID Verification. The photo from that verification is used as the comparison photo.
        # 
        # > Among the four methods of passing in images (FaceContrastPicture, FaceContrastPictureUrl, CertifyId, and OSS), select only one.
        self.certify_id = certify_id
        # Specifies whether to allow cropping of the face image. Valid values:
        # 
        # - T: Allowed.
        # 
        # - F (default): Not allowed.
        self.crop = crop
        # The device token for risk identification.
        self.device_token = device_token
        # The encryption type. An empty value indicates no encryption.
        self.encrypt_type = encrypt_type
        # The local video file.
        self.face_contrast_file = face_contrast_file
        # The Base64-encoded photo.
        self.face_contrast_picture = face_contrast_picture
        # The OSS photo URL. Currently only authorized OSS photo URLs are supported.
        # 
        # > Among the four methods of passing in images (FaceContrastPicture, FaceContrastPictureUrl, CertifyId, and OSS), select only one.
        self.face_contrast_picture_url = face_contrast_picture_url
        # The IP address of the user.
        self.ip = ip
        # The mobile phone number of the user.
        self.mobile = mobile
        # The liveness detection type.
        self.model = model
        # The bucket name of the authorized OSS space.
        # 
        # > Among the four methods of passing in images (FaceContrastPicture, FaceContrastPictureUrl, CertifyId, and OSS), select only one.
        self.oss_bucket_name = oss_bucket_name
        # The file name in the authorized OSS space.
        # 
        # > Among the four methods of passing in images (FaceContrastPicture, FaceContrastPictureUrl, CertifyId, and OSS), select only one.
        self.oss_object_name = oss_object_name
        # The unique identifier of the merchant request.
        # The value is a 32-character alphanumeric string. The first few characters are a custom abbreviation defined by the merchant, the middle part can be a time segment, and the last part can be a random or incremental sequence.
        self.outer_order_no = outer_order_no
        # Fixed value: ID_MIN.
        self.product_code = product_code
        # The verification scenario ID.
        self.scene_id = scene_id
        # The custom user ID defined by the business.
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

        if self.face_contrast_file is not None:
            result['FaceContrastFile'] = self.face_contrast_file

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
            self.face_contrast_file = m.get('FaceContrastFile')

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

