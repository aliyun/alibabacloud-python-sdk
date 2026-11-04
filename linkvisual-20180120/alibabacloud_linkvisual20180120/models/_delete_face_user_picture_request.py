# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteFaceUserPictureRequest(DaraModel):
    def __init__(
        self,
        face_pic_md_5: str = None,
        isolation_id: str = None,
        user_id: str = None,
    ):
        # The unique identifier of the user\\"s face image. Set this parameter to the **Data** value that you obtained and saved locally after you called the [AddFaceUserPicutre](https://help.aliyun.com/document_detail/312040.html) operation to add the face image for the user.
        # 
        # This parameter is required.
        self.face_pic_md_5 = face_pic_md_5
        # The business isolation ID. It is used to isolate data between different business applications under the same Alibaba Cloud account. Set this parameter to the same value as the **IsolationId** that you specified when you called the [AddFaceUser](https://help.aliyun.com/document_detail/288338.html) operation to add the user.
        # 
        # This parameter is required.
        self.isolation_id = isolation_id
        # The user ID. Set this parameter to the **UserId** value that you obtained and saved locally after you called the [AddFaceUser](https://help.aliyun.com/document_detail/288338.html) operation to add the user.
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
        if self.face_pic_md_5 is not None:
            result['FacePicMd5'] = self.face_pic_md_5

        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FacePicMd5') is not None:
            self.face_pic_md_5 = m.get('FacePicMd5')

        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

