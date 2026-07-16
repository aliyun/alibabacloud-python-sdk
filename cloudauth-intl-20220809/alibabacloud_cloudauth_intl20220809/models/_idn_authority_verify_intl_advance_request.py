# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import BinaryIO

from darabonba.model import DaraModel

class IdnAuthorityVerifyIntlAdvanceRequest(DaraModel):
    def __init__(
        self,
        birth_date: str = None,
        email: str = None,
        full_name: str = None,
        id_number: str = None,
        merchant_biz_id: str = None,
        merchant_user_id: str = None,
        mobile: str = None,
        product_code: str = None,
        scene_code: str = None,
        source_face_picture: str = None,
        source_face_picture_file_object: BinaryIO = None,
        source_face_picture_url: str = None,
        timestamp: str = None,
    ):
        # The date of birth.
        # 
        # This parameter is required.
        self.birth_date = birth_date
        # The email address of the user.
        # 
        # This parameter is required.
        self.email = email
        # The full name.
        # 
        # This parameter is required.
        self.full_name = full_name
        # The ID card number.
        # 
        # This parameter is required.
        self.id_number = id_number
        # The merchant-side custom business unique identifier, which is used for subsequent troubleshooting. The value can be a combination of letters and digits with a maximum length of 32 characters. Ensure that the value is unique.
        # 
        # This parameter is required.
        self.merchant_biz_id = merchant_biz_id
        # The custom user ID, or another identifier that can identify a specific user, such as a phone number or email address. We strongly recommend that you desensitize the value of this field in advance, for example, by hashing the value.
        # 
        # This parameter is required.
        self.merchant_user_id = merchant_user_id
        # The Indonesian mobile phone number. The number must start with +62, followed by 9 to 11 digits.
        # 
        # This parameter is required.
        self.mobile = mobile
        # The product solution to use. Set the value to IDN_META.
        # 
        # This parameter is required.
        self.product_code = product_code
        # The custom authentication scenario ID. You can use this scenario ID to query related records in the console. The value can be a combination of letters, digits, or underscores with a maximum length of 10 characters.
        self.scene_code = scene_code
        # The Base64-encoded facial photo.
        # 
        # > **Note**
        # 
        # - If you use this method to pass the ID photo, check the photo size and do not pass an excessively large photo.
        # - Specify one of the following parameters: SourceFacePicture, SourceFacePictureUrl, or SourceFacePictureFile.
        self.source_face_picture = source_face_picture
        # The file stream of the facial photo.
        self.source_face_picture_file_object = source_face_picture_file_object
        # The URL of the facial photo. The URL must be a publicly accessible HTTP or HTTPS link.
        self.source_face_picture_url = source_face_picture_url
        # This parameter is required.
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.birth_date is not None:
            result['BirthDate'] = self.birth_date

        if self.email is not None:
            result['Email'] = self.email

        if self.full_name is not None:
            result['FullName'] = self.full_name

        if self.id_number is not None:
            result['IdNumber'] = self.id_number

        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id

        if self.merchant_user_id is not None:
            result['MerchantUserId'] = self.merchant_user_id

        if self.mobile is not None:
            result['Mobile'] = self.mobile

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code

        if self.source_face_picture is not None:
            result['SourceFacePicture'] = self.source_face_picture

        if self.source_face_picture_file_object is not None:
            result['SourceFacePictureFile'] = self.source_face_picture_file_object

        if self.source_face_picture_url is not None:
            result['SourceFacePictureUrl'] = self.source_face_picture_url

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BirthDate') is not None:
            self.birth_date = m.get('BirthDate')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('FullName') is not None:
            self.full_name = m.get('FullName')

        if m.get('IdNumber') is not None:
            self.id_number = m.get('IdNumber')

        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')

        if m.get('MerchantUserId') is not None:
            self.merchant_user_id = m.get('MerchantUserId')

        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')

        if m.get('SourceFacePicture') is not None:
            self.source_face_picture = m.get('SourceFacePicture')

        if m.get('SourceFacePictureFile') is not None:
            self.source_face_picture_file_object = m.get('SourceFacePictureFile')

        if m.get('SourceFacePictureUrl') is not None:
            self.source_face_picture_url = m.get('SourceFacePictureUrl')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

