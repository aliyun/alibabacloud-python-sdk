# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class VerifyMaterialRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_type: str = None,
        face_image_url: str = None,
        id_card_back_image_url: str = None,
        id_card_front_image_url: str = None,
        id_card_number: str = None,
        name: str = None,
        user_id: str = None,
    ):
        # The unique ID that identifies a verification task. The value can be up to 64 characters in length. For a single verification task, the system supports unlimited submissions until the verification is passed and the task is completed.
        # 
        # > Use a different BizId for each new verification task.
        # 
        # This parameter is required.
        self.biz_id = biz_id
        # The business scenario identifier for the ID Verification service. Create one in the console first. For more information, see [Business settings](https://help.aliyun.com/document_detail/127885.html).
        # 
        # This parameter is required.
        self.biz_type = biz_type
        # The HTTP or HTTPS URL of the front-facing facial photo.
        # 
        # This parameter is required.
        self.face_image_url = face_image_url
        # The HTTP or HTTPS URL of the national emblem side of the ID card.
        self.id_card_back_image_url = id_card_back_image_url
        # The HTTP or HTTPS URL of the portrait side of the ID card.
        self.id_card_front_image_url = id_card_front_image_url
        # The ID card number.
        # 
        # This parameter is required.
        self.id_card_number = id_card_number
        # The name.
        # 
        # This parameter is required.
        self.name = name
        # The ID of the end user, such as the account ID of the end user.
        self.user_id = user_id

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

        if self.face_image_url is not None:
            result['FaceImageUrl'] = self.face_image_url

        if self.id_card_back_image_url is not None:
            result['IdCardBackImageUrl'] = self.id_card_back_image_url

        if self.id_card_front_image_url is not None:
            result['IdCardFrontImageUrl'] = self.id_card_front_image_url

        if self.id_card_number is not None:
            result['IdCardNumber'] = self.id_card_number

        if self.name is not None:
            result['Name'] = self.name

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('FaceImageUrl') is not None:
            self.face_image_url = m.get('FaceImageUrl')

        if m.get('IdCardBackImageUrl') is not None:
            self.id_card_back_image_url = m.get('IdCardBackImageUrl')

        if m.get('IdCardFrontImageUrl') is not None:
            self.id_card_front_image_url = m.get('IdCardFrontImageUrl')

        if m.get('IdCardNumber') is not None:
            self.id_card_number = m.get('IdCardNumber')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

