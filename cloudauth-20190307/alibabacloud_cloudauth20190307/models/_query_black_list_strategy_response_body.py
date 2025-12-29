# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudauth20190307 import models as main_models
from darabonba.model import DaraModel

class QueryBlackListStrategyResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: List[main_models.QueryBlackListStrategyResponseBodyResultObject] = None,
    ):
        # Return code, **200** indicates successful API response.
        self.code = code
        # Error message.
        self.message = message
        # ID of the request
        self.request_id = request_id
        # Returned result information.
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            for v1 in self.result_object:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ResultObject'] = []
        if self.result_object is not None:
            for k1 in self.result_object:
                result['ResultObject'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result_object = []
        if m.get('ResultObject') is not None:
            for k1 in m.get('ResultObject'):
                temp_model = main_models.QueryBlackListStrategyResponseBodyResultObject()
                self.result_object.append(temp_model.from_map(k1))

        return self

class QueryBlackListStrategyResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        biz_content: str = None,
        biz_key: str = None,
        gmt_modified: int = None,
        id: int = None,
        product_name: str = None,
        status: str = None,
        user_id: int = None,
    ):
        # Blacklist string, separated by **commas**.
        self.biz_content = biz_content
        # List type:
        # - mobile: Phone number blacklist
        # - ip: IP blacklist
        # - identifyNum: ID number blacklist
        # - bankCard: Bank card blacklist
        self.biz_key = biz_key
        # Modification time.
        self.gmt_modified = gmt_modified
        # Rule ID.
        self.id = id
        # Product name:
        # - id2meta: ID number two-factor verification
        # - mobile3Meta: Phone number factor verification
        # - bankcardMeta: Bank card factor verification
        self.product_name = product_name
        # Status:
        # - **disabled**: Disabled
        # - **normal**: Enabled
        self.status = status
        # User ID.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_content is not None:
            result['BizContent'] = self.biz_content

        if self.biz_key is not None:
            result['BizKey'] = self.biz_key

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.product_name is not None:
            result['ProductName'] = self.product_name

        if self.status is not None:
            result['Status'] = self.status

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizContent') is not None:
            self.biz_content = m.get('BizContent')

        if m.get('BizKey') is not None:
            self.biz_key = m.get('BizKey')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

