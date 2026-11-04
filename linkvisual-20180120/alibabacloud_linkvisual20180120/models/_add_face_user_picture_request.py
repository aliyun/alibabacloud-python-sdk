# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddFaceUserPictureRequest(DaraModel):
    def __init__(
        self,
        face_pic_url: str = None,
        isolation_id: str = None,
        user_id: str = None,
    ):
        # The download URL of the user\\"s face image. Only JPEG and JPG images are supported, and the image URL cannot contain Chinese characters.
        # 
        # This parameter is required.
        self.face_pic_url = face_pic_url
        # The business isolation ID, which is used to isolate data between different business applications under the same Alibaba Cloud account. Keep this value consistent with the **IsolationId** set when calling the [AddFaceUser](https://help.aliyun.com/document_detail/288338.html) API operation to add a user.
        # 
        # This parameter is required.
        self.isolation_id = isolation_id
        # The user ID. Pass in the **UserId** value that was obtained and saved locally after calling the [AddFaceUser](https://help.aliyun.com/document_detail/288338.html) API operation to add a user.
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
        if self.face_pic_url is not None:
            result['FacePicUrl'] = self.face_pic_url

        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FacePicUrl') is not None:
            self.face_pic_url = m.get('FacePicUrl')

        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

