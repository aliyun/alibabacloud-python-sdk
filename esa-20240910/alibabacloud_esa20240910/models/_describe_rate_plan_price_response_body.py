# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class DescribeRatePlanPriceResponseBody(DaraModel):
    def __init__(
        self,
        price_model: main_models.DescribeRatePlanPriceResponseBodyPriceModel = None,
        request_id: str = None,
    ):
        self.price_model = price_model
        self.request_id = request_id

    def validate(self):
        if self.price_model:
            self.price_model.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.price_model is not None:
            result['PriceModel'] = self.price_model.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PriceModel') is not None:
            temp_model = main_models.DescribeRatePlanPriceResponseBodyPriceModel()
            self.price_model = temp_model.from_map(m.get('PriceModel'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeRatePlanPriceResponseBodyPriceModel(DaraModel):
    def __init__(
        self,
        rate_plan: main_models.DescribeRatePlanPriceResponseBodyPriceModelRatePlan = None,
        rule: main_models.DescribeRatePlanPriceResponseBodyPriceModelRule = None,
    ):
        self.rate_plan = rate_plan
        self.rule = rule

    def validate(self):
        if self.rate_plan:
            self.rate_plan.validate()
        if self.rule:
            self.rule.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rate_plan is not None:
            result['RatePlan'] = self.rate_plan.to_map()

        if self.rule is not None:
            result['Rule'] = self.rule.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RatePlan') is not None:
            temp_model = main_models.DescribeRatePlanPriceResponseBodyPriceModelRatePlan()
            self.rate_plan = temp_model.from_map(m.get('RatePlan'))

        if m.get('Rule') is not None:
            temp_model = main_models.DescribeRatePlanPriceResponseBodyPriceModelRule()
            self.rule = temp_model.from_map(m.get('Rule'))

        return self

class DescribeRatePlanPriceResponseBodyPriceModelRule(DaraModel):
    def __init__(
        self,
        rule_list: List[main_models.DescribeRatePlanPriceResponseBodyPriceModelRuleRuleList] = None,
    ):
        self.rule_list = rule_list

    def validate(self):
        if self.rule_list:
            for v1 in self.rule_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RuleList'] = []
        if self.rule_list is not None:
            for k1 in self.rule_list:
                result['RuleList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rule_list = []
        if m.get('RuleList') is not None:
            for k1 in m.get('RuleList'):
                temp_model = main_models.DescribeRatePlanPriceResponseBodyPriceModelRuleRuleList()
                self.rule_list.append(temp_model.from_map(k1))

        return self

class DescribeRatePlanPriceResponseBodyPriceModelRuleRuleList(DaraModel):
    def __init__(
        self,
        name: str = None,
        rule_desc_id: int = None,
    ):
        self.name = name
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

class DescribeRatePlanPriceResponseBodyPriceModelRatePlan(DaraModel):
    def __init__(
        self,
        plan_price_list: List[main_models.DescribeRatePlanPriceResponseBodyPriceModelRatePlanPlanPriceList] = None,
    ):
        self.plan_price_list = plan_price_list

    def validate(self):
        if self.plan_price_list:
            for v1 in self.plan_price_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PlanPriceList'] = []
        if self.plan_price_list is not None:
            for k1 in self.plan_price_list:
                result['PlanPriceList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.plan_price_list = []
        if m.get('PlanPriceList') is not None:
            for k1 in m.get('PlanPriceList'):
                temp_model = main_models.DescribeRatePlanPriceResponseBodyPriceModelRatePlanPlanPriceList()
                self.plan_price_list.append(temp_model.from_map(k1))

        return self

class DescribeRatePlanPriceResponseBodyPriceModelRatePlanPlanPriceList(DaraModel):
    def __init__(
        self,
        accelerate_type: str = None,
        charge_type: str = None,
        coverages: str = None,
        crossborder_traffic: str = None,
        currency: str = None,
        dcdn_plan: str = None,
        discount_price: float = None,
        edge_compute: str = None,
        edge_ddos_4layer: str = None,
        edge_ddos_4layer_intl: str = None,
        edge_ddos_7layer: str = None,
        edge_ddos_instance_cn: str = None,
        edge_ddos_instance_intl: str = None,
        edge_lb_4layer: str = None,
        edge_lb_4layer_intl: str = None,
        edge_lb_7layer: str = None,
        edge_waf: str = None,
        edge_waf_instance: str = None,
        layer_4traffic: str = None,
        layer_4traffic_intl: str = None,
        plan_name: str = None,
        plan_status: str = None,
        plan_traffic: str = None,
        plan_type: str = None,
        position: int = None,
        price: float = None,
        total_price: float = None,
    ):
        self.accelerate_type = accelerate_type
        self.charge_type = charge_type
        self.coverages = coverages
        self.crossborder_traffic = crossborder_traffic
        self.currency = currency
        self.dcdn_plan = dcdn_plan
        self.discount_price = discount_price
        self.edge_compute = edge_compute
        self.edge_ddos_4layer = edge_ddos_4layer
        self.edge_ddos_4layer_intl = edge_ddos_4layer_intl
        self.edge_ddos_7layer = edge_ddos_7layer
        self.edge_ddos_instance_cn = edge_ddos_instance_cn
        self.edge_ddos_instance_intl = edge_ddos_instance_intl
        self.edge_lb_4layer = edge_lb_4layer
        self.edge_lb_4layer_intl = edge_lb_4layer_intl
        self.edge_lb_7layer = edge_lb_7layer
        self.edge_waf = edge_waf
        self.edge_waf_instance = edge_waf_instance
        self.layer_4traffic = layer_4traffic
        self.layer_4traffic_intl = layer_4traffic_intl
        self.plan_name = plan_name
        self.plan_status = plan_status
        self.plan_traffic = plan_traffic
        self.plan_type = plan_type
        self.position = position
        self.price = price
        self.total_price = total_price

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerate_type is not None:
            result['AccelerateType'] = self.accelerate_type

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.coverages is not None:
            result['Coverages'] = self.coverages

        if self.crossborder_traffic is not None:
            result['CrossborderTraffic'] = self.crossborder_traffic

        if self.currency is not None:
            result['Currency'] = self.currency

        if self.dcdn_plan is not None:
            result['DcdnPlan'] = self.dcdn_plan

        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price

        if self.edge_compute is not None:
            result['EdgeCompute'] = self.edge_compute

        if self.edge_ddos_4layer is not None:
            result['EdgeDdos4Layer'] = self.edge_ddos_4layer

        if self.edge_ddos_4layer_intl is not None:
            result['EdgeDdos4LayerIntl'] = self.edge_ddos_4layer_intl

        if self.edge_ddos_7layer is not None:
            result['EdgeDdos7Layer'] = self.edge_ddos_7layer

        if self.edge_ddos_instance_cn is not None:
            result['EdgeDdosInstanceCn'] = self.edge_ddos_instance_cn

        if self.edge_ddos_instance_intl is not None:
            result['EdgeDdosInstanceIntl'] = self.edge_ddos_instance_intl

        if self.edge_lb_4layer is not None:
            result['EdgeLb4Layer'] = self.edge_lb_4layer

        if self.edge_lb_4layer_intl is not None:
            result['EdgeLb4LayerIntl'] = self.edge_lb_4layer_intl

        if self.edge_lb_7layer is not None:
            result['EdgeLb7Layer'] = self.edge_lb_7layer

        if self.edge_waf is not None:
            result['EdgeWaf'] = self.edge_waf

        if self.edge_waf_instance is not None:
            result['EdgeWafInstance'] = self.edge_waf_instance

        if self.layer_4traffic is not None:
            result['Layer4Traffic'] = self.layer_4traffic

        if self.layer_4traffic_intl is not None:
            result['Layer4TrafficIntl'] = self.layer_4traffic_intl

        if self.plan_name is not None:
            result['PlanName'] = self.plan_name

        if self.plan_status is not None:
            result['PlanStatus'] = self.plan_status

        if self.plan_traffic is not None:
            result['PlanTraffic'] = self.plan_traffic

        if self.plan_type is not None:
            result['PlanType'] = self.plan_type

        if self.position is not None:
            result['Position'] = self.position

        if self.price is not None:
            result['Price'] = self.price

        if self.total_price is not None:
            result['TotalPrice'] = self.total_price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccelerateType') is not None:
            self.accelerate_type = m.get('AccelerateType')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('Coverages') is not None:
            self.coverages = m.get('Coverages')

        if m.get('CrossborderTraffic') is not None:
            self.crossborder_traffic = m.get('CrossborderTraffic')

        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('DcdnPlan') is not None:
            self.dcdn_plan = m.get('DcdnPlan')

        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')

        if m.get('EdgeCompute') is not None:
            self.edge_compute = m.get('EdgeCompute')

        if m.get('EdgeDdos4Layer') is not None:
            self.edge_ddos_4layer = m.get('EdgeDdos4Layer')

        if m.get('EdgeDdos4LayerIntl') is not None:
            self.edge_ddos_4layer_intl = m.get('EdgeDdos4LayerIntl')

        if m.get('EdgeDdos7Layer') is not None:
            self.edge_ddos_7layer = m.get('EdgeDdos7Layer')

        if m.get('EdgeDdosInstanceCn') is not None:
            self.edge_ddos_instance_cn = m.get('EdgeDdosInstanceCn')

        if m.get('EdgeDdosInstanceIntl') is not None:
            self.edge_ddos_instance_intl = m.get('EdgeDdosInstanceIntl')

        if m.get('EdgeLb4Layer') is not None:
            self.edge_lb_4layer = m.get('EdgeLb4Layer')

        if m.get('EdgeLb4LayerIntl') is not None:
            self.edge_lb_4layer_intl = m.get('EdgeLb4LayerIntl')

        if m.get('EdgeLb7Layer') is not None:
            self.edge_lb_7layer = m.get('EdgeLb7Layer')

        if m.get('EdgeWaf') is not None:
            self.edge_waf = m.get('EdgeWaf')

        if m.get('EdgeWafInstance') is not None:
            self.edge_waf_instance = m.get('EdgeWafInstance')

        if m.get('Layer4Traffic') is not None:
            self.layer_4traffic = m.get('Layer4Traffic')

        if m.get('Layer4TrafficIntl') is not None:
            self.layer_4traffic_intl = m.get('Layer4TrafficIntl')

        if m.get('PlanName') is not None:
            self.plan_name = m.get('PlanName')

        if m.get('PlanStatus') is not None:
            self.plan_status = m.get('PlanStatus')

        if m.get('PlanTraffic') is not None:
            self.plan_traffic = m.get('PlanTraffic')

        if m.get('PlanType') is not None:
            self.plan_type = m.get('PlanType')

        if m.get('Position') is not None:
            self.position = m.get('Position')

        if m.get('Price') is not None:
            self.price = m.get('Price')

        if m.get('TotalPrice') is not None:
            self.total_price = m.get('TotalPrice')

        return self

