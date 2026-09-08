# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTotalSensitiveInfoRequest(DaraModel):
    def __init__(
        self,
        count_type: int = None,
        lang: str = None,
        product_code: str = None,
        product_code_list: str = None,
        template_id: int = None,
    ):
        self.count_type = count_type
        self.lang = lang
        self.product_code = product_code
        self.product_code_list = product_code_list
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count_type is not None:
            result['CountType'] = self.count_type

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_code_list is not None:
            result['ProductCodeList'] = self.product_code_list

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CountType') is not None:
            self.count_type = m.get('CountType')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductCodeList') is not None:
            self.product_code_list = m.get('ProductCodeList')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

