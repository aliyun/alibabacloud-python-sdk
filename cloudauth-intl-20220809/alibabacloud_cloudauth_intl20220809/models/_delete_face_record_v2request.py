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
        # The face group code. If this parameter is not specified, the face data of the user is deleted from all face groups.
        self.face_group_code = face_group_code
        # The unique user identifier, which must be consistent with the one used when calling AddFaceRecord. If this parameter was not specified during registration, you can use the default image name.
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

