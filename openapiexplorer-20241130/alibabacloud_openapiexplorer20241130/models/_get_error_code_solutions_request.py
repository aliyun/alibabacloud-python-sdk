# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetErrorCodeSolutionsRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        error_code: str = None,
        error_message: str = None,
        product: str = None,
    ):
        # The language of the solution. Valid values: zh-CN and en-US. Not all of the solutions are available in English. If you set this parameter to en-US, but the corresponding solution is actually not available in English, no response is returned.
        self.accept_language = accept_language
        # The error code based on which you want to query a solution.
        # 
        # This parameter is required.
        self.error_code = error_code
        # The error message for which you want to query a solution. This parameter must be configured together with the errorCode parameter.
        self.error_message = error_message
        # The product code. You can use one of the following methods to query a product code:
        # 
        # *   Call the GetRequestLog operation to query a product code from the response.
        # *   Query the code of a product in the OpenAPI Explorer URL of the product. For example, the OpenAPI Explorer URL of Short Message Service (SMS) is https://api.alibabacloud.com/product/Dysmsapi. Therefore, the product code of SMS is Dysmsapi.
        self.product = product

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['acceptLanguage'] = self.accept_language

        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        if self.product is not None:
            result['product'] = self.product

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acceptLanguage') is not None:
            self.accept_language = m.get('acceptLanguage')

        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('product') is not None:
            self.product = m.get('product')

        return self

