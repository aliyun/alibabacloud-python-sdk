# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class DescribeConfigurationPriceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeConfigurationPriceResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        # The HTTP status code. Valid values:
        # 
        # *   **2xx**: The request was successful.
        # *   **3xx**: The request was redirected.
        # *   **4xx**: The request failed.
        # *   **5xx**: A server error occurred.
        self.code = code
        # The price.
        self.data = data
        # The error code. Valid values:
        # 
        # *   If the request was successful, **ErrorCode** is not returned.
        # *   If the request failed, **ErrorCode** is returned. For more information, see **Error codes** in this topic.
        self.error_code = error_code
        # The message returned. Valid values:
        # 
        # *   If the request was successful, **success** is returned.
        # *   If the request failed, an error code is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the configuration price was obtained.
        # 
        # *   **true**: The price was obtained.
        # *   **false**: The price failed to be queried.
        self.success = success
        # The ID of the trace.
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.DescribeConfigurationPriceResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        return self

class DescribeConfigurationPriceResponseBodyData(DaraModel):
    def __init__(
        self,
        bag_usage: main_models.DescribeConfigurationPriceResponseBodyDataBagUsage = None,
        cpu_mem_price: main_models.DescribeConfigurationPriceResponseBodyDataCpuMemPrice = None,
        order: main_models.DescribeConfigurationPriceResponseBodyDataOrder = None,
        request_price: main_models.DescribeConfigurationPriceResponseBodyDataRequestPrice = None,
        rules: List[main_models.DescribeConfigurationPriceResponseBodyDataRules] = None,
        traffic_price: main_models.DescribeConfigurationPriceResponseBodyDataTrafficPrice = None,
    ):
        # The remaining capacity of the resource plan.
        self.bag_usage = bag_usage
        # The price of CPU and memory.
        self.cpu_mem_price = cpu_mem_price
        # The information about pricing.
        self.order = order
        # The price based on the number of requests.
        self.request_price = request_price
        # The promotion rules.
        self.rules = rules
        # The traffic price.
        self.traffic_price = traffic_price

    def validate(self):
        if self.bag_usage:
            self.bag_usage.validate()
        if self.cpu_mem_price:
            self.cpu_mem_price.validate()
        if self.order:
            self.order.validate()
        if self.request_price:
            self.request_price.validate()
        if self.rules:
            for v1 in self.rules:
                 if v1:
                    v1.validate()
        if self.traffic_price:
            self.traffic_price.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bag_usage is not None:
            result['BagUsage'] = self.bag_usage.to_map()

        if self.cpu_mem_price is not None:
            result['CpuMemPrice'] = self.cpu_mem_price.to_map()

        if self.order is not None:
            result['Order'] = self.order.to_map()

        if self.request_price is not None:
            result['RequestPrice'] = self.request_price.to_map()

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        if self.traffic_price is not None:
            result['TrafficPrice'] = self.traffic_price.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BagUsage') is not None:
            temp_model = main_models.DescribeConfigurationPriceResponseBodyDataBagUsage()
            self.bag_usage = temp_model.from_map(m.get('BagUsage'))

        if m.get('CpuMemPrice') is not None:
            temp_model = main_models.DescribeConfigurationPriceResponseBodyDataCpuMemPrice()
            self.cpu_mem_price = temp_model.from_map(m.get('CpuMemPrice'))

        if m.get('Order') is not None:
            temp_model = main_models.DescribeConfigurationPriceResponseBodyDataOrder()
            self.order = temp_model.from_map(m.get('Order'))

        if m.get('RequestPrice') is not None:
            temp_model = main_models.DescribeConfigurationPriceResponseBodyDataRequestPrice()
            self.request_price = temp_model.from_map(m.get('RequestPrice'))

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.DescribeConfigurationPriceResponseBodyDataRules()
                self.rules.append(temp_model.from_map(k1))

        if m.get('TrafficPrice') is not None:
            temp_model = main_models.DescribeConfigurationPriceResponseBodyDataTrafficPrice()
            self.traffic_price = temp_model.from_map(m.get('TrafficPrice'))

        return self

class DescribeConfigurationPriceResponseBodyDataTrafficPrice(DaraModel):
    def __init__(
        self,
        order: main_models.DescribeConfigurationPriceResponseBodyDataTrafficPriceOrder = None,
        rules: List[main_models.DescribeConfigurationPriceResponseBodyDataTrafficPriceRules] = None,
    ):
        # The information about pricing.
        self.order = order
        # The discount rule.
        self.rules = rules

    def validate(self):
        if self.order:
            self.order.validate()
        if self.rules:
            for v1 in self.rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order is not None:
            result['Order'] = self.order.to_map()

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Order') is not None:
            temp_model = main_models.DescribeConfigurationPriceResponseBodyDataTrafficPriceOrder()
            self.order = temp_model.from_map(m.get('Order'))

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.DescribeConfigurationPriceResponseBodyDataTrafficPriceRules()
                self.rules.append(temp_model.from_map(k1))

        return self

class DescribeConfigurationPriceResponseBodyDataTrafficPriceRules(DaraModel):
    def __init__(
        self,
        name: str = None,
        rule_desc_id: float = None,
    ):
        # The name of the discount rule.
        self.name = name
        # The ID of the discount rule.
        self.rule_desc_id = rule_desc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.rule_desc_id is not None:
            result['RuleDescId'] = self.rule_desc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RuleDescId') is not None:
            self.rule_desc_id = m.get('RuleDescId')

        return self

class DescribeConfigurationPriceResponseBodyDataTrafficPriceOrder(DaraModel):
    def __init__(
        self,
        discount_amount: float = None,
        original_amount: float = None,
        rule_ids: List[str] = None,
        trade_amount: float = None,
    ):
        # The discount amount.
        self.discount_amount = discount_amount
        # The original price of the order.
        self.original_amount = original_amount
        # The ID of the discount rule.
        self.rule_ids = rule_ids
        # The final price of the order.
        self.trade_amount = trade_amount

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.discount_amount is not None:
            result['DiscountAmount'] = self.discount_amount

        if self.original_amount is not None:
            result['OriginalAmount'] = self.original_amount

        if self.rule_ids is not None:
            result['RuleIds'] = self.rule_ids

        if self.trade_amount is not None:
            result['TradeAmount'] = self.trade_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiscountAmount') is not None:
            self.discount_amount = m.get('DiscountAmount')

        if m.get('OriginalAmount') is not None:
            self.original_amount = m.get('OriginalAmount')

        if m.get('RuleIds') is not None:
            self.rule_ids = m.get('RuleIds')

        if m.get('TradeAmount') is not None:
            self.trade_amount = m.get('TradeAmount')

        return self

class DescribeConfigurationPriceResponseBodyDataRules(DaraModel):
    def __init__(
        self,
        name: str = None,
        rule_desc_id: int = None,
    ):
        # The name of the promotion rule.
        self.name = name
        # The ID of the promotion rule.
        self.rule_desc_id = rule_desc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.rule_desc_id is not None:
            result['RuleDescId'] = self.rule_desc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RuleDescId') is not None:
            self.rule_desc_id = m.get('RuleDescId')

        return self

class DescribeConfigurationPriceResponseBodyDataRequestPrice(DaraModel):
    def __init__(
        self,
        order: main_models.DescribeConfigurationPriceResponseBodyDataRequestPriceOrder = None,
        rules: List[main_models.DescribeConfigurationPriceResponseBodyDataRequestPriceRules] = None,
    ):
        # The information about pricing.
        self.order = order
        # The discount rule.
        self.rules = rules

    def validate(self):
        if self.order:
            self.order.validate()
        if self.rules:
            for v1 in self.rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order is not None:
            result['Order'] = self.order.to_map()

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Order') is not None:
            temp_model = main_models.DescribeConfigurationPriceResponseBodyDataRequestPriceOrder()
            self.order = temp_model.from_map(m.get('Order'))

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.DescribeConfigurationPriceResponseBodyDataRequestPriceRules()
                self.rules.append(temp_model.from_map(k1))

        return self

class DescribeConfigurationPriceResponseBodyDataRequestPriceRules(DaraModel):
    def __init__(
        self,
        name: str = None,
        rule_desc_id: int = None,
    ):
        # The name of the discount rule.
        self.name = name
        # The ID of the discount policy.
        self.rule_desc_id = rule_desc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.rule_desc_id is not None:
            result['RuleDescId'] = self.rule_desc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RuleDescId') is not None:
            self.rule_desc_id = m.get('RuleDescId')

        return self

class DescribeConfigurationPriceResponseBodyDataRequestPriceOrder(DaraModel):
    def __init__(
        self,
        discount_amount: float = None,
        original_amount: float = None,
        rule_ids: List[str] = None,
        trade_amount: float = None,
    ):
        # The discount amount.
        self.discount_amount = discount_amount
        # The original price of the order.
        self.original_amount = original_amount
        # The ID of the discount rule.
        self.rule_ids = rule_ids
        # The actual price of the order.
        self.trade_amount = trade_amount

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.discount_amount is not None:
            result['DiscountAmount'] = self.discount_amount

        if self.original_amount is not None:
            result['OriginalAmount'] = self.original_amount

        if self.rule_ids is not None:
            result['RuleIds'] = self.rule_ids

        if self.trade_amount is not None:
            result['TradeAmount'] = self.trade_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiscountAmount') is not None:
            self.discount_amount = m.get('DiscountAmount')

        if m.get('OriginalAmount') is not None:
            self.original_amount = m.get('OriginalAmount')

        if m.get('RuleIds') is not None:
            self.rule_ids = m.get('RuleIds')

        if m.get('TradeAmount') is not None:
            self.trade_amount = m.get('TradeAmount')

        return self

class DescribeConfigurationPriceResponseBodyDataOrder(DaraModel):
    def __init__(
        self,
        discount_amount: float = None,
        original_amount: float = None,
        rule_ids: List[str] = None,
        trade_amount: float = None,
    ):
        # The discount amount.
        self.discount_amount = discount_amount
        # The original price of the order.
        self.original_amount = original_amount
        # The ID of the promotion rule.
        self.rule_ids = rule_ids
        # The transaction price.
        self.trade_amount = trade_amount

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.discount_amount is not None:
            result['DiscountAmount'] = self.discount_amount

        if self.original_amount is not None:
            result['OriginalAmount'] = self.original_amount

        if self.rule_ids is not None:
            result['RuleIds'] = self.rule_ids

        if self.trade_amount is not None:
            result['TradeAmount'] = self.trade_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiscountAmount') is not None:
            self.discount_amount = m.get('DiscountAmount')

        if m.get('OriginalAmount') is not None:
            self.original_amount = m.get('OriginalAmount')

        if m.get('RuleIds') is not None:
            self.rule_ids = m.get('RuleIds')

        if m.get('TradeAmount') is not None:
            self.trade_amount = m.get('TradeAmount')

        return self

class DescribeConfigurationPriceResponseBodyDataCpuMemPrice(DaraModel):
    def __init__(
        self,
        order: main_models.DescribeConfigurationPriceResponseBodyDataCpuMemPriceOrder = None,
        rules: List[main_models.DescribeConfigurationPriceResponseBodyDataCpuMemPriceRules] = None,
    ):
        # The information about pricing.
        self.order = order
        # The discount rules.
        self.rules = rules

    def validate(self):
        if self.order:
            self.order.validate()
        if self.rules:
            for v1 in self.rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order is not None:
            result['Order'] = self.order.to_map()

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Order') is not None:
            temp_model = main_models.DescribeConfigurationPriceResponseBodyDataCpuMemPriceOrder()
            self.order = temp_model.from_map(m.get('Order'))

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.DescribeConfigurationPriceResponseBodyDataCpuMemPriceRules()
                self.rules.append(temp_model.from_map(k1))

        return self

class DescribeConfigurationPriceResponseBodyDataCpuMemPriceRules(DaraModel):
    def __init__(
        self,
        name: str = None,
        rule_desc_id: float = None,
    ):
        # The name of discount rule.
        self.name = name
        # The ID of the discount rule.
        self.rule_desc_id = rule_desc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.rule_desc_id is not None:
            result['RuleDescId'] = self.rule_desc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RuleDescId') is not None:
            self.rule_desc_id = m.get('RuleDescId')

        return self

class DescribeConfigurationPriceResponseBodyDataCpuMemPriceOrder(DaraModel):
    def __init__(
        self,
        discount_amount: float = None,
        original_amount: float = None,
        rule_ids: List[str] = None,
        trade_amount: float = None,
    ):
        # The discount amount.
        self.discount_amount = discount_amount
        # The original price.
        self.original_amount = original_amount
        # The ID of the discount rule.
        self.rule_ids = rule_ids
        # The final price of the order.
        self.trade_amount = trade_amount

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.discount_amount is not None:
            result['DiscountAmount'] = self.discount_amount

        if self.original_amount is not None:
            result['OriginalAmount'] = self.original_amount

        if self.rule_ids is not None:
            result['RuleIds'] = self.rule_ids

        if self.trade_amount is not None:
            result['TradeAmount'] = self.trade_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiscountAmount') is not None:
            self.discount_amount = m.get('DiscountAmount')

        if m.get('OriginalAmount') is not None:
            self.original_amount = m.get('OriginalAmount')

        if m.get('RuleIds') is not None:
            self.rule_ids = m.get('RuleIds')

        if m.get('TradeAmount') is not None:
            self.trade_amount = m.get('TradeAmount')

        return self

class DescribeConfigurationPriceResponseBodyDataBagUsage(DaraModel):
    def __init__(
        self,
        cpu: float = None,
        cu: float = None,
        mem: float = None,
    ):
        # The available CPU capacity. Unit: cores \\*.
        self.cpu = cpu
        self.cu = cu
        # The available memory size. Unit: GiB ×.
        self.mem = mem

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.cu is not None:
            result['Cu'] = self.cu

        if self.mem is not None:
            result['Mem'] = self.mem

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('Cu') is not None:
            self.cu = m.get('Cu')

        if m.get('Mem') is not None:
            self.mem = m.get('Mem')

        return self

