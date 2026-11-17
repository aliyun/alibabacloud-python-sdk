# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteFaceRecordV2Request(DaraModel):
    def __init__(
        self,
        face_group_code: str = None,
        merchant_user_id: str = None,
    ):
        # The code of the face group. If you do not specify this parameter, the face data of the user in all face groups is deleted.
        self.face_group_code = face_group_code
        # The unique identifier of the user. This value must be the same as the one specified when the face record was added by using AddFaceRecord. If no user identifier was specified when the record was added, you can use the default image name.
        # 
        # This parameter is required.
        self.merchant_user_id = merchant_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.face_group_code is not None:
            result['FaceGroupCode'] = self.face_group_code

        if self.merchant_user_id is not None:
            result['MerchantUserId'] = self.merchant_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceGroupCode') is not None:
            self.face_group_code = m.get('FaceGroupCode')

        if m.get('MerchantUserId') is not None:
            self.merchant_user_id = m.get('MerchantUserId')

        return self

