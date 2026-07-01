# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dysmsapi20170525 import models as main_models
from darabonba.model import DaraModel

class CreateCardSmsTemplateResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.CreateCardSmsTemplateResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The request status code. Valid values:
        # 
        # - OK: The request was successful.
        # 
        # - For a list of other error codes, see [Error codes](https://help.aliyun.com/document_detail/101346.html).
        self.code = code
        # The data returned by the operation.
        self.data = data
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # - **true**: The call was successful.
        # 
        # - **false**: The call failed.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.CreateCardSmsTemplateResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class CreateCardSmsTemplateResponseBodyData(DaraModel):
    def __init__(
        self,
        template_code: str = None,
    ):
        # The code for the card SMS template. You can view the **Template Code** on the **Card SMS** > [template management](https://dysms.console.aliyun.com/domestic/card) page in the console.
        # 
        # > The card SMS template must be approved before it can be used.
        self.template_code = template_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')

        return self

