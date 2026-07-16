# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAutoDisposeConfigRequest(DaraModel):
    def __init__(
        self,
        auto_decision_status: str = None,
        lang: str = None,
        product_code: str = None,
    ):
        # Specifies whether to enable auto decision. Valid values:
        # 
        # - `enabled`: Enables auto decision.
        # 
        # - `disabled`: Disables auto decision.
        # 
        # This parameter is required.
        self.auto_decision_status = auto_decision_status
        # The language of the response message. Valid values:
        # 
        # - **zh** (default): Chinese.
        # 
        # - **en**: English.
        # 
        # This parameter is required.
        self.lang = lang
        # The code for the cloud product.
        # 
        # This parameter is required.
        self.product_code = product_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_decision_status is not None:
            result['AutoDecisionStatus'] = self.auto_decision_status

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoDecisionStatus') is not None:
            self.auto_decision_status = m.get('AutoDecisionStatus')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        return self

