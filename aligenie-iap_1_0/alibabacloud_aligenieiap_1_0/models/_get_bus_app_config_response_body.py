# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aligenieiap_1_0 import models as main_models
from darabonba.model import DaraModel

class GetBusAppConfigResponseBody(DaraModel):
    def __init__(
        self,
        ret_code: int = None,
        ret_msg: str = None,
        ret_value: main_models.GetBusAppConfigResponseBodyRetValue = None,
    ):
        # Error code returned. 0 indicates success.
        self.ret_code = ret_code
        # Error message returned. No message is returned if the operation succeeded.
        self.ret_msg = ret_msg
        # Configuration Information (VIP label, shopping guide bar, shopping guide pop-up)
        self.ret_value = ret_value

    def validate(self):
        if self.ret_value:
            self.ret_value.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ret_code is not None:
            result['RetCode'] = self.ret_code

        if self.ret_msg is not None:
            result['RetMsg'] = self.ret_msg

        if self.ret_value is not None:
            result['RetValue'] = self.ret_value.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RetCode') is not None:
            self.ret_code = m.get('RetCode')

        if m.get('RetMsg') is not None:
            self.ret_msg = m.get('RetMsg')

        if m.get('RetValue') is not None:
            temp_model = main_models.GetBusAppConfigResponseBodyRetValue()
            self.ret_value = temp_model.from_map(m.get('RetValue'))

        return self

class GetBusAppConfigResponseBodyRetValue(DaraModel):
    def __init__(
        self,
        cashier: str = None,
        shopping_bar: str = None,
        shopping_window: str = None,
        vip_label: str = None,
    ):
        # Cashier URL
        self.cashier = cashier
        # Shopping guide bar URL
        self.shopping_bar = shopping_bar
        # Shopping guide pop-up URL
        self.shopping_window = shopping_window
        # VIP label transparency URL
        self.vip_label = vip_label

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cashier is not None:
            result['Cashier'] = self.cashier

        if self.shopping_bar is not None:
            result['ShoppingBar'] = self.shopping_bar

        if self.shopping_window is not None:
            result['ShoppingWindow'] = self.shopping_window

        if self.vip_label is not None:
            result['VipLabel'] = self.vip_label

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cashier') is not None:
            self.cashier = m.get('Cashier')

        if m.get('ShoppingBar') is not None:
            self.shopping_bar = m.get('ShoppingBar')

        if m.get('ShoppingWindow') is not None:
            self.shopping_window = m.get('ShoppingWindow')

        if m.get('VipLabel') is not None:
            self.vip_label = m.get('VipLabel')

        return self

