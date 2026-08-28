# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class GetGatewayElasticPolicyResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetGatewayElasticPolicyResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetGatewayElasticPolicyResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetGatewayElasticPolicyResponseBodyData(DaraModel):
    def __init__(
        self,
        elastic_policy: main_models.GetGatewayElasticPolicyResponseBodyDataElasticPolicy = None,
        elastic_strategy_id: str = None,
        elastic_type: str = None,
        gateway_id: str = None,
    ):
        self.elastic_policy = elastic_policy
        self.elastic_strategy_id = elastic_strategy_id
        self.elastic_type = elastic_type
        self.gateway_id = gateway_id

    def validate(self):
        if self.elastic_policy:
            self.elastic_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.elastic_policy is not None:
            result['elasticPolicy'] = self.elastic_policy.to_map()

        if self.elastic_strategy_id is not None:
            result['elasticStrategyId'] = self.elastic_strategy_id

        if self.elastic_type is not None:
            result['elasticType'] = self.elastic_type

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('elasticPolicy') is not None:
            temp_model = main_models.GetGatewayElasticPolicyResponseBodyDataElasticPolicy()
            self.elastic_policy = temp_model.from_map(m.get('elasticPolicy'))

        if m.get('elasticStrategyId') is not None:
            self.elastic_strategy_id = m.get('elasticStrategyId')

        if m.get('elasticType') is not None:
            self.elastic_type = m.get('elasticType')

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        return self

class GetGatewayElasticPolicyResponseBodyDataElasticPolicy(DaraModel):
    def __init__(
        self,
        disable_scale_time_policy_list: List[main_models.GetGatewayElasticPolicyResponseBodyDataElasticPolicyDisableScaleTimePolicyList] = None,
        elastic_enabled: bool = None,
        elastic_type: str = None,
        enable_scale_time_policy_list: List[main_models.GetGatewayElasticPolicyResponseBodyDataElasticPolicyEnableScaleTimePolicyList] = None,
        load_warning_threshold: bool = None,
        max_units: int = None,
        time_policy_list: List[main_models.GetGatewayElasticPolicyResponseBodyDataElasticPolicyTimePolicyList] = None,
    ):
        self.disable_scale_time_policy_list = disable_scale_time_policy_list
        self.elastic_enabled = elastic_enabled
        self.elastic_type = elastic_type
        self.enable_scale_time_policy_list = enable_scale_time_policy_list
        self.load_warning_threshold = load_warning_threshold
        self.max_units = max_units
        self.time_policy_list = time_policy_list

    def validate(self):
        if self.disable_scale_time_policy_list:
            for v1 in self.disable_scale_time_policy_list:
                 if v1:
                    v1.validate()
        if self.enable_scale_time_policy_list:
            for v1 in self.enable_scale_time_policy_list:
                 if v1:
                    v1.validate()
        if self.time_policy_list:
            for v1 in self.time_policy_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['disableScaleTimePolicyList'] = []
        if self.disable_scale_time_policy_list is not None:
            for k1 in self.disable_scale_time_policy_list:
                result['disableScaleTimePolicyList'].append(k1.to_map() if k1 else None)

        if self.elastic_enabled is not None:
            result['elasticEnabled'] = self.elastic_enabled

        if self.elastic_type is not None:
            result['elasticType'] = self.elastic_type

        result['enableScaleTimePolicyList'] = []
        if self.enable_scale_time_policy_list is not None:
            for k1 in self.enable_scale_time_policy_list:
                result['enableScaleTimePolicyList'].append(k1.to_map() if k1 else None)

        if self.load_warning_threshold is not None:
            result['loadWarningThreshold'] = self.load_warning_threshold

        if self.max_units is not None:
            result['maxUnits'] = self.max_units

        result['timePolicyList'] = []
        if self.time_policy_list is not None:
            for k1 in self.time_policy_list:
                result['timePolicyList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.disable_scale_time_policy_list = []
        if m.get('disableScaleTimePolicyList') is not None:
            for k1 in m.get('disableScaleTimePolicyList'):
                temp_model = main_models.GetGatewayElasticPolicyResponseBodyDataElasticPolicyDisableScaleTimePolicyList()
                self.disable_scale_time_policy_list.append(temp_model.from_map(k1))

        if m.get('elasticEnabled') is not None:
            self.elastic_enabled = m.get('elasticEnabled')

        if m.get('elasticType') is not None:
            self.elastic_type = m.get('elasticType')

        self.enable_scale_time_policy_list = []
        if m.get('enableScaleTimePolicyList') is not None:
            for k1 in m.get('enableScaleTimePolicyList'):
                temp_model = main_models.GetGatewayElasticPolicyResponseBodyDataElasticPolicyEnableScaleTimePolicyList()
                self.enable_scale_time_policy_list.append(temp_model.from_map(k1))

        if m.get('loadWarningThreshold') is not None:
            self.load_warning_threshold = m.get('loadWarningThreshold')

        if m.get('maxUnits') is not None:
            self.max_units = m.get('maxUnits')

        self.time_policy_list = []
        if m.get('timePolicyList') is not None:
            for k1 in m.get('timePolicyList'):
                temp_model = main_models.GetGatewayElasticPolicyResponseBodyDataElasticPolicyTimePolicyList()
                self.time_policy_list.append(temp_model.from_map(k1))

        return self

class GetGatewayElasticPolicyResponseBodyDataElasticPolicyTimePolicyList(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
        units: int = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.units = units

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.units is not None:
            result['units'] = self.units

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('units') is not None:
            self.units = m.get('units')

        return self

class GetGatewayElasticPolicyResponseBodyDataElasticPolicyEnableScaleTimePolicyList(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.start_time is not None:
            result['startTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        return self

class GetGatewayElasticPolicyResponseBodyDataElasticPolicyDisableScaleTimePolicyList(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.start_time is not None:
            result['startTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        return self

