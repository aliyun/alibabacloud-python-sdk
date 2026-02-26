# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ShopCreateRequest(DaraModel):
    def __init__(
        self,
        after_sale_ding_talk_id: str = None,
        description: str = None,
        operator_ding_talk_id: str = None,
        pre_sale_ding_talk_id: str = None,
        shop_name: str = None,
    ):
        self.after_sale_ding_talk_id = after_sale_ding_talk_id
        # This parameter is required.
        self.description = description
        # This parameter is required.
        self.operator_ding_talk_id = operator_ding_talk_id
        self.pre_sale_ding_talk_id = pre_sale_ding_talk_id
        # This parameter is required.
        self.shop_name = shop_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.after_sale_ding_talk_id is not None:
            result['afterSaleDingTalkId'] = self.after_sale_ding_talk_id

        if self.description is not None:
            result['description'] = self.description

        if self.operator_ding_talk_id is not None:
            result['operatorDingTalkId'] = self.operator_ding_talk_id

        if self.pre_sale_ding_talk_id is not None:
            result['preSaleDingTalkId'] = self.pre_sale_ding_talk_id

        if self.shop_name is not None:
            result['shopName'] = self.shop_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('afterSaleDingTalkId') is not None:
            self.after_sale_ding_talk_id = m.get('afterSaleDingTalkId')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('operatorDingTalkId') is not None:
            self.operator_ding_talk_id = m.get('operatorDingTalkId')

        if m.get('preSaleDingTalkId') is not None:
            self.pre_sale_ding_talk_id = m.get('preSaleDingTalkId')

        if m.get('shopName') is not None:
            self.shop_name = m.get('shopName')

        return self

