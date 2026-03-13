# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVendorApiListRequest(DaraModel):
    def __init__(
        self,
        api_name: str = None,
        key_word: str = None,
        page_number: int = None,
        page_size: int = None,
        product_code: str = None,
        vendor_code: str = None,
    ):
        # The name of the Alibaba Cloud product interface, supporting fuzzy search.
        self.api_name = api_name
        # Keyword.
        self.key_word = key_word
        # The current page number for pagination. The default value is 1.
        self.page_number = page_number
        # The number of items per page when displaying paginated results. The default is 10.
        self.page_size = page_size
        # Vendor\\"s product identifier:
        # - **waf**: Web Application Firewall.
        # - **cfw**: Cloud Firewall.
        self.product_code = product_code
        # Vendor code:
        # - **Tencent**: Tencent.
        # - **HUAWEICLOUD**: Huawei.
        # - **Azure**: Microsoft Azure.
        # - **AWS**: Amazon Web Services.
        # - **Chaitin**: Chaitin.
        self.vendor_code = vendor_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_name is not None:
            result['ApiName'] = self.api_name

        if self.key_word is not None:
            result['KeyWord'] = self.key_word

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.vendor_code is not None:
            result['VendorCode'] = self.vendor_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')

        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('VendorCode') is not None:
            self.vendor_code = m.get('VendorCode')

        return self

