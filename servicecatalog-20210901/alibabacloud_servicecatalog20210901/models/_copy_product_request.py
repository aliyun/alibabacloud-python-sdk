# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CopyProductRequest(DaraModel):
    def __init__(
        self,
        source_product_arn: str = None,
        target_product_name: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the source product.
        # 
        # > The source product can belong to the current account or belong to a product portfolio that is shared by another account.
        # 
        # This parameter is required.
        self.source_product_arn = source_product_arn
        # The name of the destination product.
        self.target_product_name = target_product_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.source_product_arn is not None:
            result['SourceProductArn'] = self.source_product_arn

        if self.target_product_name is not None:
            result['TargetProductName'] = self.target_product_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceProductArn') is not None:
            self.source_product_arn = m.get('SourceProductArn')

        if m.get('TargetProductName') is not None:
            self.target_product_name = m.get('TargetProductName')

        return self

