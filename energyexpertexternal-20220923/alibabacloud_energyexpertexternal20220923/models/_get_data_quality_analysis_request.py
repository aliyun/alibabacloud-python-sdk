# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDataQualityAnalysisRequest(DaraModel):
    def __init__(
        self,
        code: str = None,
        data_quality_evaluation_type: int = None,
        product_id: int = None,
        product_type: int = None,
    ):
        # The enterprise code.
        # 
        # This parameter is required.
        self.code = code
        # Data quality assessment type: 1 is DQI and 2 is DQR.
        # 
        # This parameter is required.
        self.data_quality_evaluation_type = data_quality_evaluation_type
        # The product id.
        # 
        # This parameter is required.
        self.product_id = product_id
        # Product type: 1 indicates that the carbon footprint of the product is requested, and 5 indicates that the carbon footprint of the supply chain is requested.
        # 
        # This parameter is required.
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data_quality_evaluation_type is not None:
            result['dataQualityEvaluationType'] = self.data_quality_evaluation_type

        if self.product_id is not None:
            result['productId'] = self.product_id

        if self.product_type is not None:
            result['productType'] = self.product_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('dataQualityEvaluationType') is not None:
            self.data_quality_evaluation_type = m.get('dataQualityEvaluationType')

        if m.get('productId') is not None:
            self.product_id = m.get('productId')

        if m.get('productType') is not None:
            self.product_type = m.get('productType')

        return self

