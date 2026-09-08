# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDataMaskingColumnCountRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        product_ids: str = None,
        template_id: int = None,
    ):
        self.lang = lang
        self.product_ids = product_ids
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.product_ids is not None:
            result['ProductIds'] = self.product_ids

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('ProductIds') is not None:
            self.product_ids = m.get('ProductIds')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

