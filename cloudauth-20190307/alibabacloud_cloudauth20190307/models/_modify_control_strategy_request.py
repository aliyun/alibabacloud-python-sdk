# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudauth20190307 import models as main_models
from darabonba.model import DaraModel

class ModifyControlStrategyRequest(DaraModel):
    def __init__(
        self,
        control_strategy_list: List[main_models.ModifyControlStrategyRequestControlStrategyList] = None,
        product_type: str = None,
        region_id: str = None,
    ):
        # The list of security alert rules.
        self.control_strategy_list = control_strategy_list
        # The product type. Currently, only **ANT_CLOUD_AUTH** (Financial-grade ID Verification) is supported. All other types are retired.
        self.product_type = product_type
        # The region ID of the Smart Access Gateway instance.
        self.region_id = region_id

    def validate(self):
        if self.control_strategy_list:
            for v1 in self.control_strategy_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ControlStrategyList'] = []
        if self.control_strategy_list is not None:
            for k1 in self.control_strategy_list:
                result['ControlStrategyList'].append(k1.to_map() if k1 else None)

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.control_strategy_list = []
        if m.get('ControlStrategyList') is not None:
            for k1 in m.get('ControlStrategyList'):
                temp_model = main_models.ModifyControlStrategyRequestControlStrategyList()
                self.control_strategy_list.append(temp_model.from_map(k1))

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class ModifyControlStrategyRequestControlStrategyList(DaraModel):
    def __init__(
        self,
        api_name: str = None,
        biz_type: str = None,
        id: int = None,
        status: str = None,
        threshold: float = None,
    ):
        # The name of the API operation, which is the same as **ProductCode**.
        self.api_name = api_name
        # The rule configuration type. Valid values:
        # - **QPS**: The QPS is greater than the threshold.
        # - **SUCCESS_RATE_5_MIN**: The success rate in the last 5 minutes is less than the threshold.
        # - **RESP_TIME_5_MIN**: The average response time in the last 5 minutes is greater than the threshold.
        # - **AMOUNT_RISE**: The period-over-period increase in call volume is greater than the threshold.
        # - **AMOUNT_FALL**: The period-over-period decrease in call volume is less than the threshold.
        # - **PASSED_RATE_1_HOUR**: The verification consistency rate in the last hour is less than the threshold.
        # - **PARAM_ERROR_RATE_1_HOUR**: The parameter error rate in the last hour is greater than the threshold.
        self.biz_type = biz_type
        # The ID of the rule.
        self.id = id
        # The status. Valid values:
        # - **disabled**: Disabled.
        # - **normal**: Enabled.
        self.status = status
        # The alert threshold of the rule.
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_name is not None:
            result['ApiName'] = self.api_name

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.id is not None:
            result['Id'] = self.id

        if self.status is not None:
            result['Status'] = self.status

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        return self

