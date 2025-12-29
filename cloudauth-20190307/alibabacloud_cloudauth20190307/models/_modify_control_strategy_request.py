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
        # List of security alarm rules.
        self.control_strategy_list = control_strategy_list
        # Product type, currently only supports **ANT_CLOUD_AUTH** (Financial-grade Real Person), all others are phased out.
        self.product_type = product_type
        # Region ID of the intelligent access gateway instance.
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
        # API name, same as **ProductCode**.
        self.api_name = api_name
        # Rule configuration type:
        # - **QPS**: QPS greater than
        # - **SUCCESS_RATE_5_MIN**: Success rate in the last 5 minutes less than
        # - **RESP_TIME_5_MIN**: Average response time in the last 5 minutes greater than
        # - **AMOUNT_RISE**: Call volume growth ratio greater than
        # - **AMOUNT_FALL**: Call volume decline ratio less than
        # - **PASSED_RATE_1_HOUR**: Verification consistency rate in the last hour less than
        # - **PARAM_ERROR_RATE_1_HOUR**: Parameter error rate in the last hour greater than
        self.biz_type = biz_type
        # Rule ID.
        self.id = id
        # Status:
        # - **disabled**: Disabled
        # - **normal**: Enabled
        self.status = status
        # Alarm threshold for the rule.
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

