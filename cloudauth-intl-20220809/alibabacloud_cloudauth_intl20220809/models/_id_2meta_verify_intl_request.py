# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Id2MetaVerifyIntlRequest(DaraModel):
    def __init__(
        self,
        identify_num: str = None,
        param_type: str = None,
        product_code: str = None,
        user_name: str = None,
    ):
        # The ID card number.
        # 
        # > Only ID cards of residents in the Chinese mainland are supported.
        self.identify_num = identify_num
        # The parameter type.
        # 
        # **normal**: The original value in plaintext.
        # 
        # > Due to limitations of the authoritative data source, two-factor ID verification does not support MD5 encryption.
        self.param_type = param_type
        # The product plan. This is a static field. Set the value to **ID_2META**.
        self.product_code = product_code
        # The name.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.identify_num is not None:
            result['IdentifyNum'] = self.identify_num

        if self.param_type is not None:
            result['ParamType'] = self.param_type

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdentifyNum') is not None:
            self.identify_num = m.get('IdentifyNum')

        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

