# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVerifyTokenRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_type: str = None,
        callback_seed: str = None,
        callback_url: str = None,
        face_retained_image_url: str = None,
        failed_redirect_url: str = None,
        id_card_back_image_url: str = None,
        id_card_front_image_url: str = None,
        id_card_number: str = None,
        name: str = None,
        passed_redirect_url: str = None,
        user_id: str = None,
        user_ip: str = None,
        user_phone_number: str = None,
        user_regist_time: int = None,
    ):
        # Verification ID. A unique ID that identifies a verification task, not exceeding 64 characters. For a single verification task, the system supports unlimited submissions until the final verification is passed and the task is completed.
        # 
        # > Different BizIds are required for different verification tasks.
        # 
        # This parameter is required.
        self.biz_id = biz_id
        # Identifier for the business scenario using the real person authentication service. Please refer to [Business Settings](https://help.aliyun.com/document_detail/127885.html) and complete the creation in the console first.
        # 
        # This parameter is required.
        self.biz_type = biz_type
        # Callback seed.
        self.callback_seed = callback_seed
        # Callback URL.
        self.callback_url = callback_url
        # HTTP or HTTPS link to the retained portrait photo.
        self.face_retained_image_url = face_retained_image_url
        # Redirect URL for failed verification.
        self.failed_redirect_url = failed_redirect_url
        # HTTP or HTTPS link to the national emblem side of the ID card image.
        self.id_card_back_image_url = id_card_back_image_url
        # HTTP or HTTPS link to the portrait side of the ID card image.
        self.id_card_front_image_url = id_card_front_image_url
        # ID card number.
        self.id_card_number = id_card_number
        # Name.
        self.name = name
        # Redirect URL upon successful verification.
        self.passed_redirect_url = passed_redirect_url
        # ID of the end user, such as the account ID of the end user.
        self.user_id = user_id
        # User IP.
        self.user_ip = user_ip
        # User phone number.
        self.user_phone_number = user_phone_number
        # User registration time. Expressed in timestamp format, unit: milliseconds.
        self.user_regist_time = user_regist_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.callback_seed is not None:
            result['CallbackSeed'] = self.callback_seed

        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url

        if self.face_retained_image_url is not None:
            result['FaceRetainedImageUrl'] = self.face_retained_image_url

        if self.failed_redirect_url is not None:
            result['FailedRedirectUrl'] = self.failed_redirect_url

        if self.id_card_back_image_url is not None:
            result['IdCardBackImageUrl'] = self.id_card_back_image_url

        if self.id_card_front_image_url is not None:
            result['IdCardFrontImageUrl'] = self.id_card_front_image_url

        if self.id_card_number is not None:
            result['IdCardNumber'] = self.id_card_number

        if self.name is not None:
            result['Name'] = self.name

        if self.passed_redirect_url is not None:
            result['PassedRedirectUrl'] = self.passed_redirect_url

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_ip is not None:
            result['UserIp'] = self.user_ip

        if self.user_phone_number is not None:
            result['UserPhoneNumber'] = self.user_phone_number

        if self.user_regist_time is not None:
            result['UserRegistTime'] = self.user_regist_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('CallbackSeed') is not None:
            self.callback_seed = m.get('CallbackSeed')

        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')

        if m.get('FaceRetainedImageUrl') is not None:
            self.face_retained_image_url = m.get('FaceRetainedImageUrl')

        if m.get('FailedRedirectUrl') is not None:
            self.failed_redirect_url = m.get('FailedRedirectUrl')

        if m.get('IdCardBackImageUrl') is not None:
            self.id_card_back_image_url = m.get('IdCardBackImageUrl')

        if m.get('IdCardFrontImageUrl') is not None:
            self.id_card_front_image_url = m.get('IdCardFrontImageUrl')

        if m.get('IdCardNumber') is not None:
            self.id_card_number = m.get('IdCardNumber')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PassedRedirectUrl') is not None:
            self.passed_redirect_url = m.get('PassedRedirectUrl')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserIp') is not None:
            self.user_ip = m.get('UserIp')

        if m.get('UserPhoneNumber') is not None:
            self.user_phone_number = m.get('UserPhoneNumber')

        if m.get('UserRegistTime') is not None:
            self.user_regist_time = m.get('UserRegistTime')

        return self

