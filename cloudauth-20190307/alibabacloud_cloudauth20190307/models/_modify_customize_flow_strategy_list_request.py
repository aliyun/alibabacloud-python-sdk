# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudauth20190307 import models as main_models
from darabonba.model import DaraModel

class ModifyCustomizeFlowStrategyListRequest(DaraModel):
    def __init__(
        self,
        product_type: str = None,
        strategy_object: List[main_models.ModifyCustomizeFlowStrategyListRequestStrategyObject] = None,
    ):
        # Product type, currently only supports **ANT_CLOUD_AUTH** (Financial-grade real person), all others have been phased out.
        self.product_type = product_type
        # Strategy list.
        self.strategy_object = strategy_object

    def validate(self):
        if self.strategy_object:
            for v1 in self.strategy_object:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.product_type is not None:
            result['ProductType'] = self.product_type

        result['StrategyObject'] = []
        if self.strategy_object is not None:
            for k1 in self.strategy_object:
                result['StrategyObject'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        self.strategy_object = []
        if m.get('StrategyObject') is not None:
            for k1 in m.get('StrategyObject'):
                temp_model = main_models.ModifyCustomizeFlowStrategyListRequestStrategyObject()
                self.strategy_object.append(temp_model.from_map(k1))

        return self

class ModifyCustomizeFlowStrategyListRequestStrategyObject(DaraModel):
    def __init__(
        self,
        accumulate_key: str = None,
        accumulate_window: int = None,
        api_name: str = None,
        flow_type: str = None,
        id: int = None,
        operation: str = None,
        status: str = None,
        threshold: int = None,
        user_id: int = None,
    ):
        # AccumulateKey
        self.accumulate_key = accumulate_key
        # Flow control statistical window size, in minutes.
        self.accumulate_window = accumulate_window
        # API name, same as **ProductCode**.
        # 
        # This parameter is required.
        self.api_name = api_name
        # Flow type:
        # - **ACCUMULATE**: Repeated appearance of ID card
        # - **PASSED_RATE**: Pass rate less than
        # - **SUB_CODE_205**: Authentication failed and liveness attack 205 ratio greater than
        # - **SUB_CODE_206**: Authentication failed and liveness attack 206 ratio greater than
        self.flow_type = flow_type
        # Rule ID.
        self.id = id
        # Operation.
        self.operation = operation
        # Status:
        # - **disabled**: Disabled
        # - **normal**: Enabled
        # 
        # This parameter is required.
        self.status = status
        # Flow control threshold.
        # 
        # This parameter is required.
        self.threshold = threshold
        # User ID.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accumulate_key is not None:
            result['AccumulateKey'] = self.accumulate_key

        if self.accumulate_window is not None:
            result['AccumulateWindow'] = self.accumulate_window

        if self.api_name is not None:
            result['ApiName'] = self.api_name

        if self.flow_type is not None:
            result['FlowType'] = self.flow_type

        if self.id is not None:
            result['Id'] = self.id

        if self.operation is not None:
            result['Operation'] = self.operation

        if self.status is not None:
            result['Status'] = self.status

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccumulateKey') is not None:
            self.accumulate_key = m.get('AccumulateKey')

        if m.get('AccumulateWindow') is not None:
            self.accumulate_window = m.get('AccumulateWindow')

        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')

        if m.get('FlowType') is not None:
            self.flow_type = m.get('FlowType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Operation') is not None:
            self.operation = m.get('Operation')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

