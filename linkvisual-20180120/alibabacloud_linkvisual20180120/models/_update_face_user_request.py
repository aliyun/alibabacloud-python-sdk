# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateFaceUserRequest(DaraModel):
    def __init__(
        self,
        custom_user_id: str = None,
        face_pic_url: str = None,
        isolation_id: str = None,
        name: str = None,
        params: str = None,
        user_id: str = None,
    ):
        # The unique ID of the user in the caller\\"s business system, such as an ID card number or student ID.
        self.custom_user_id = custom_user_id
        # The image download URL. Currently, JPG and JPEG formats are supported.
        self.face_pic_url = face_pic_url
        # The isolation ID.<br>It is used for data isolation between different applications under a tenant. For example, if a user has business operations in both Zhejiang and Shaanxi, you can create two isolation IDs for the operations in Zhejiang and Xi\\"an respectively.
        # 
        # This parameter is required.
        self.isolation_id = isolation_id
        # The username.
        self.name = name
        # The user information.
        self.params = params
        # The user ID.
        # 
        # This parameter is required.
        self.user_id = user_id

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

        if self.user_id is not None:
            result['UserId'] = self.user_id

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

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

