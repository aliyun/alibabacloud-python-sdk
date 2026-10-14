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
        # The language of the response description. Valid values:
        # 
        # - zh: Chinese.
        # - en: English.
        self.lang = lang
        # The list of cloud product type identifiers. Separate multiple values with commas (,). Valid values for column encryption scenarios: 5 (ApsaraDB RDS), 8 (PolarDB), and 27 (PolarDB-X 2.0).
        self.product_ids = product_ids
        # The ID of the data classification template. You can obtain this value from Items[].Id returned by the ListTemplates operation. This value must be consistent with the selected sensitivity level and detection model.
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

