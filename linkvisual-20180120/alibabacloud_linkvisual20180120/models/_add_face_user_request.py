# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddFaceUserRequest(DaraModel):
    def __init__(
        self,
        custom_user_id: str = None,
        face_pic_url: str = None,
        isolation_id: str = None,
        name: str = None,
        params: str = None,
    ):
        # The user identification ID. It supports any uppercase letter and digits. Recommended Settings: the user\\"s ID card number, student ID, or similar identifier.
        # 
        # This parameter is required.
        self.custom_user_id = custom_user_id
        # The URL for downloading the user\\"s face image. Only JPEG and JPG image formats are supported, and the image URL cannot contain Chinese characters.
        # 
        # This parameter is required.
        self.face_pic_url = face_pic_url
        # The business isolation ID. It is used for data isolation between different business applications under the same Alibaba Cloud account. It supports uppercase and lowercase English letters and digits.
        # 
        # For example, if you have face recognition businesses in Region A and Region B, you can set different business isolation IDs to distinguish the face recognition businesses in Region A and Region B.
        # 
        # >Notice: 
        # Save the business isolation ID properly for use in subsequent calls to other API operations in this business isolation zone.
        # 
        # This parameter is required.
        self.isolation_id = isolation_id
        # The username. It supports Chinese characters, uppercase and lowercase English letters, digits, underscores (_), and hyphens (-). The length cannot exceed 64 characters.
        self.name = name
        # The custom user parameters.
        self.params = params

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_user_id is not None:
            result['CustomUserId'] = self.custom_user_id

        if self.face_pic_url is not None:
            result['FacePicUrl'] = self.face_pic_url

        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id

        if self.name is not None:
            result['Name'] = self.name

        if self.params is not None:
            result['Params'] = self.params

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomUserId') is not None:
            self.custom_user_id = m.get('CustomUserId')

        if m.get('FacePicUrl') is not None:
            self.face_pic_url = m.get('FacePicUrl')

        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        return self

