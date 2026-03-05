# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckResourceMeasureRequest(DaraModel):
    def __init__(
        self,
        belong_id: str = None,
        belong_id_type: str = None,
        biz_type: str = None,
        esp_biz_id: str = None,
        order_component_params: str = None,
        resource_code: str = None,
        resource_value: int = None,
    ):
        self.belong_id = belong_id
        self.belong_id_type = belong_id_type
        self.biz_type = biz_type
        self.esp_biz_id = esp_biz_id
        self.order_component_params = order_component_params
        self.resource_code = resource_code
        self.resource_value = resource_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.belong_id is not None:
            result['BelongId'] = self.belong_id

        if self.belong_id_type is not None:
            result['BelongIdType'] = self.belong_id_type

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.esp_biz_id is not None:
            result['EspBizId'] = self.esp_biz_id

        if self.order_component_params is not None:
            result['OrderComponentParams'] = self.order_component_params

        if self.resource_code is not None:
            result['ResourceCode'] = self.resource_code

        if self.resource_value is not None:
            result['ResourceValue'] = self.resource_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BelongId') is not None:
            self.belong_id = m.get('BelongId')

        if m.get('BelongIdType') is not None:
            self.belong_id_type = m.get('BelongIdType')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('EspBizId') is not None:
            self.esp_biz_id = m.get('EspBizId')

        if m.get('OrderComponentParams') is not None:
            self.order_component_params = m.get('OrderComponentParams')

        if m.get('ResourceCode') is not None:
            self.resource_code = m.get('ResourceCode')

        if m.get('ResourceValue') is not None:
            self.resource_value = m.get('ResourceValue')

        return self

