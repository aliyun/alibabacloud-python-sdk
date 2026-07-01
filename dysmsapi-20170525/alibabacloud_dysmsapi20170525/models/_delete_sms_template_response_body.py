# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteSmsTemplateResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        template_code: str = None,
    ):
        # 请求状态码。
        # 
        # - 返回OK代表请求成功。
        # - 其他错误码，请参见[API错误码](https://help.aliyun.com/document_detail/101346.html)。
        self.code = code
        # 状态码的描述。
        self.message = message
        # 请求ID。
        self.request_id = request_id
        # 已删除的模板Code。
        self.template_code = template_code

    def validate(self):
        pass

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

        if self.template_code is not None:
            result['TemplateCode'] = self.template_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')

        return self

