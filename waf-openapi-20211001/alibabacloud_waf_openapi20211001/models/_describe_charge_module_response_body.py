# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeChargeModuleResponseBody(DaraModel):
    def __init__(
        self,
        charge_modules: List[main_models.DescribeChargeModuleResponseBodyChargeModules] = None,
        request_id: str = None,
    ):
        # The list of WAF pricing module information.
        self.charge_modules = charge_modules
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.charge_modules:
            for v1 in self.charge_modules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ChargeModules'] = []
        if self.charge_modules is not None:
            for k1 in self.charge_modules:
                result['ChargeModules'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.charge_modules = []
        if m.get('ChargeModules') is not None:
            for k1 in m.get('ChargeModules'):
                temp_model = main_models.DescribeChargeModuleResponseBodyChargeModules()
                self.charge_modules.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeChargeModuleResponseBodyChargeModules(DaraModel):
    def __init__(
        self,
        charge_mode: str = None,
        charge_mode_details: List[str] = None,
        charge_unit: str = None,
        module_code: str = None,
        period_type: str = None,
        usage_type: str = None,
        usage_unit_factor: int = None,
    ):
        # The pricing mode of the pricing module. Valid values:
        # - **NORMAL_PRICE**: standard pricing.
        # - **STEP_ACCUMULATION**: tiered pricing.
        self.charge_mode = charge_mode
        # The pricing details of the pricing module.
        self.charge_mode_details = charge_mode_details
        # The pricing unit.
        self.charge_unit = charge_unit
        # The pricing module identity. Valid values:
        # - **domainCount**: the number of CNAME-connected domain names.
        # - **qps**: the peak QPS.
        # - **request**: the basic traffic fee.
        # - **ipBlacklistRuleCount**: the number of IP blacklist rules.
        # - **customAclBaseRuleCount**: the number of Basic Policies in custom rules.
        # - **customAclAdvanceRuleCount**: the number of advanced rules in custom rules.
        # - **antiScanRuleCount**: the number of scan protection rules.
        # - **customResponseRuleCount**: the number of custom response rules.
        # - **ipv6**: IPv6.
        # - **gslb**: intelligent load balancing.
        # - **exclusiveIpCount**: the number of exclusive IP addresses.
        # - **ccRuleCount**: the number of HTTP flood mitigation rules.
        # - **regionBlockRuleCount**: the number of Location Blacklist rules.
        # - **tamperproofRuleCount**: the number of web tamper proofing rules.
        # - **dlpRuleCount**: the number of information leak prevention rules.
        # - **botTraffic**: the Bot management traffic fee.
        # - **aiWhiteListTemplateCount**: the number of intelligent whitelist templates.
        # - **apisecResourceCount**: the number of protected objects with API security enabled.
        # - **apisecTraffic**: the API security traffic fee.
        # - **compliance**: the number of protocol compliance templates.
        # - **riskTraffic**: the number of risk identification hits in Bot management.
        # - **assetStatus**: the asset center.
        # - **nonPort**: non-standard ports.
        # - **customAclCaptcha**: the number of custom rule slider verification attempts.
        # - **wafBaseTemplateCount**: the number of web core protection rules.
        # - **instanceFee**: the WAF instance fee.
        # - **spikeThrottleRuleCount**: the number of peak traffic throttling rules.
        # - **botWebTemplateCount**: the number of web protection templates in Bot management.
        # - **botAppTemplateCount**: the number of app protection templates in Bot management.
        # - **customAclBotRuleCount**: the number of advanced custom rules in Bot management.
        self.module_code = module_code
        # The billing period type of the pricing module. Valid values:
        # - **Hour**: hourly billing.
        self.period_type = period_type
        # The usage type of the pricing module. Valid values:
        # - **template**: template.
        # - **qps**: QPS.
        # - **domain**: domain name.
        # - **rule**: rule.
        # - **ip**: IP address.
        # - **resource**: protected object.
        # - **reqest**: request.
        # - **function**: feature enablement.
        # - **time**: number of times.
        self.usage_type = usage_type
        # The billing unit factor of the pricing module.
        # 
        # > The billing unit factor **UsageUnitFactor** multiplied by the usage type **UsageType** forms the billing unit of the module.
        self.usage_unit_factor = usage_unit_factor

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.charge_mode is not None:
            result['ChargeMode'] = self.charge_mode

        if self.charge_mode_details is not None:
            result['ChargeModeDetails'] = self.charge_mode_details

        if self.charge_unit is not None:
            result['ChargeUnit'] = self.charge_unit

        if self.module_code is not None:
            result['ModuleCode'] = self.module_code

        if self.period_type is not None:
            result['PeriodType'] = self.period_type

        if self.usage_type is not None:
            result['UsageType'] = self.usage_type

        if self.usage_unit_factor is not None:
            result['UsageUnitFactor'] = self.usage_unit_factor

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeMode') is not None:
            self.charge_mode = m.get('ChargeMode')

        if m.get('ChargeModeDetails') is not None:
            self.charge_mode_details = m.get('ChargeModeDetails')

        if m.get('ChargeUnit') is not None:
            self.charge_unit = m.get('ChargeUnit')

        if m.get('ModuleCode') is not None:
            self.module_code = m.get('ModuleCode')

        if m.get('PeriodType') is not None:
            self.period_type = m.get('PeriodType')

        if m.get('UsageType') is not None:
            self.usage_type = m.get('UsageType')

        if m.get('UsageUnitFactor') is not None:
            self.usage_unit_factor = m.get('UsageUnitFactor')

        return self

