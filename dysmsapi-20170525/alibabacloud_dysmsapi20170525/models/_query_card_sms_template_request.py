# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryCardSmsTemplateRequest(DaraModel):
    def __init__(
        self,
        template_code: str = None,
    ):
        # The code of the card SMS template. Valid values:
        # 
        # - After you call the [CreateCardSmsTemplate](~~CreateCardSmsTemplate~~) operation, the value of the **TemplateCode** response parameter is the code of the newly created card SMS template.
        # 
        # - You can also log on to the [Domestic Card SMS](https://dysms.console.aliyun.com/domestic/card) page in the console and view the card SMS template code on the **Template Management** tab.
        # 
        # This parameter is required.
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

