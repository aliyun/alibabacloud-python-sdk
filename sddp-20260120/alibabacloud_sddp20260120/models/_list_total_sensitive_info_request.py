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
        # The statistics scenario. Valid values:
        # 
        # - 41: overview.
        # - 42: data catalog statistics by product.
        # - 43: region and template summary by product.
        self.count_type = count_type
        # The language of the response description. Valid values:
        # 
        # - zh: Chinese.
        # - en: English.
        self.lang = lang
        # The code of the cloud service. Column encryption supports RDS, POLARDB, and PolarDBX2. If you also specify ProductId, the two values must correspond to each other.
        self.product_code = product_code
        # Multiple product codes separated by commas (,). This parameter is used when CountType is set to 43 and ProductCode is not specified. The results are merged by region and template.
        self.product_code_list = product_code_list
        # The ID of the data classification template. You can obtain this value from Items[].Id in the response of the ListTemplates operation. The value must be consistent with the selected sensitivity level and detection model.
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

