# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckAuthCodeBindForExtShrinkRequest(DaraModel):
    def __init__(
        self,
        auth_code: str = None,
        encode_key: str = None,
        encode_type: str = None,
        user_info_shrink: str = None,
    ):
        # The authCode obtained by specifying a user ID
        # 
        # This parameter is required.
        self.auth_code = auth_code
        # The value corresponding to the encoding type. Enter the Project ID of the project containing the ProductKey of this product in the Tmall Genie AI platform.
        # 
        # This parameter is required.
        self.encode_key = encode_key
        # Encoding type. Enter PROJECT_ID here.
        # 
        # This parameter is required.
        self.encode_type = encode_type
        # List of user identifier information.
        # 
        # This parameter is required.
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_code is not None:
            result['AuthCode'] = self.auth_code

        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key

        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type

        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthCode') is not None:
            self.auth_code = m.get('AuthCode')

        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')

        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')

        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')

        return self

