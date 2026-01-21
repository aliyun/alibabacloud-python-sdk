# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeActiveMetricRuleListRequest(DaraModel):
    def __init__(
        self,
        product: str = None,
    ):
        # The abbreviation of the cloud service that supports initiative alert rules.
        # 
        # For more information about how to obtain the name of a cloud service, see [DescribeProductsOfActiveMetricRule](https://help.aliyun.com/document_detail/114930.html).
        # 
        # This parameter is required.
        self.product = product

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.product is not None:
            result['Product'] = self.product

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Product') is not None:
            self.product = m.get('Product')

        return self

