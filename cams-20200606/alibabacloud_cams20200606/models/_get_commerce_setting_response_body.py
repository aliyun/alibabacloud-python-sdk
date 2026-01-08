# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cams20200606 import models as main_models
from darabonba.model import DaraModel

class GetCommerceSettingResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.GetCommerceSettingResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Access denied for detailed information.
        self.access_denied_detail = access_denied_detail
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other values indicate that the request failed. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetCommerceSettingResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetCommerceSettingResponseBodyData(DaraModel):
    def __init__(
        self,
        cart_enable: bool = None,
        catalog_visible: bool = None,
    ):
        # Indicates whether the shopping cart button is displayed. Valid values:
        # 
        # *   true
        # *   false
        self.cart_enable = cart_enable
        # Indicates whether the catalog button is displayed. Valid values:
        # 
        # *   true
        # *   false
        self.catalog_visible = catalog_visible

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cart_enable is not None:
            result['CartEnable'] = self.cart_enable

        if self.catalog_visible is not None:
            result['CatalogVisible'] = self.catalog_visible

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CartEnable') is not None:
            self.cart_enable = m.get('CartEnable')

        if m.get('CatalogVisible') is not None:
            self.catalog_visible = m.get('CatalogVisible')

        return self

