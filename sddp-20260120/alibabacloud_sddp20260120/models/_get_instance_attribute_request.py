# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetInstanceAttributeRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        lang: str = None,
        product_code: str = None,
        product_id: int = None,
    ):
        # The database instance identity. You can obtain this value from Items[].InstanceId in the response of the ListDataMaskingInstances operation.
        self.instance_id = instance_id
        # The language of the response description. Valid values:
        # 
        # - zh: Chinese.
        # - en: English.
        self.lang = lang
        # The cloud product code. Column encryption supports RDS, POLARDB, and PolarDBX2. If you also specify ProductId, the two values must correspond to each other.
        self.product_code = product_code
        # The cloud product type identifier. Valid values:
        # 
        # - 5: RDS.
        # - 8: POLARDB.
        # - 27: PolarDBX2.
        # 
        # If you specify both ProductId and ProductCode, the values must correspond to each other.
        self.product_id = product_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        return self

