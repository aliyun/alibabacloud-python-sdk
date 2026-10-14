# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeDomainCcProtectSwitchResponseBody(DaraModel):
    def __init__(
        self,
        protect_switch_list: List[main_models.DescribeDomainCcProtectSwitchResponseBodyProtectSwitchList] = None,
        request_id: str = None,
    ):
        # The status of each protection feature for the website.
        self.protect_switch_list = protect_switch_list
        # The ID of the request. This ID is unique to the request. Use the request ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.protect_switch_list:
            for v1 in self.protect_switch_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ProtectSwitchList'] = []
        if self.protect_switch_list is not None:
            for k1 in self.protect_switch_list:
                result['ProtectSwitchList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.protect_switch_list = []
        if m.get('ProtectSwitchList') is not None:
            for k1 in m.get('ProtectSwitchList'):
                temp_model = main_models.DescribeDomainCcProtectSwitchResponseBodyProtectSwitchList()
                self.protect_switch_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDomainCcProtectSwitchResponseBodyProtectSwitchList(DaraModel):
    def __init__(
        self,
        ai_mode: str = None,
        ai_rule_enable: int = None,
        ai_template: str = None,
        black_white_list_enable: int = None,
        cc_custom_rule_enable: int = None,
        cc_enable: int = None,
        cc_global_switch: str = None,
        cc_template: str = None,
        domain: str = None,
        precise_rule_enable: int = None,
        region_block_enable: int = None,
    ):
        # The mode of AI-powered protection. Valid values:
        # 
        # - **watch**: Warning mode
        # 
        # - **defense**: Defense mode
        self.ai_mode = ai_mode
        # The status of the AI-powered protection feature. Valid values:
        # 
        # - **0**: Disabled
        # 
        # - **1**: Enabled
        self.ai_rule_enable = ai_rule_enable
        # The level of AI-powered protection. Valid values:
        # 
        # - **level30**: Loose
        # 
        # - **level60**: Normal
        # 
        # - **level90**: Strict
        self.ai_template = ai_template
        # The status of the blacklists and whitelists feature. Valid values:
        # 
        # - **0**: Disabled
        # 
        # - **1**: Enabled
        self.black_white_list_enable = black_white_list_enable
        # The status of custom CC rules. Valid values:
        # 
        # - **0**: Disabled
        # 
        # - **1**: Enabled
        self.cc_custom_rule_enable = cc_custom_rule_enable
        # The status of the rate limiting (CC protection) feature. Valid values:
        # 
        # - **0**: Disabled
        # 
        # - **1**: Enabled
        self.cc_enable = cc_enable
        # The status of the global switch for custom and precise CC protection. Valid values:
        # 
        # - **open**: Enabled
        # 
        # - **close**: Disabled
        self.cc_global_switch = cc_global_switch
        # The CC protection mode. Valid values:
        # 
        # - **default**: Normal
        # 
        # - **gf_under_attack**: Emergency
        # 
        # - **gf_sos_verify**: Strict
        # 
        # - **gf_sos_enhance**: Very Strict
        self.cc_template = cc_template
        # The domain name of the website.
        self.domain = domain
        # The status of the precise access control feature. Valid values:
        # 
        # - **0**: Disabled
        # 
        # - **1**: Enabled
        self.precise_rule_enable = precise_rule_enable
        # The status of the Location Blacklist (Domain Names) feature. Valid values:
        # 
        # - **0**: Disabled
        # 
        # - **1**: Enabled
        self.region_block_enable = region_block_enable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ai_mode is not None:
            result['AiMode'] = self.ai_mode

        if self.ai_rule_enable is not None:
            result['AiRuleEnable'] = self.ai_rule_enable

        if self.ai_template is not None:
            result['AiTemplate'] = self.ai_template

        if self.black_white_list_enable is not None:
            result['BlackWhiteListEnable'] = self.black_white_list_enable

        if self.cc_custom_rule_enable is not None:
            result['CcCustomRuleEnable'] = self.cc_custom_rule_enable

        if self.cc_enable is not None:
            result['CcEnable'] = self.cc_enable

        if self.cc_global_switch is not None:
            result['CcGlobalSwitch'] = self.cc_global_switch

        if self.cc_template is not None:
            result['CcTemplate'] = self.cc_template

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.precise_rule_enable is not None:
            result['PreciseRuleEnable'] = self.precise_rule_enable

        if self.region_block_enable is not None:
            result['RegionBlockEnable'] = self.region_block_enable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AiMode') is not None:
            self.ai_mode = m.get('AiMode')

        if m.get('AiRuleEnable') is not None:
            self.ai_rule_enable = m.get('AiRuleEnable')

        if m.get('AiTemplate') is not None:
            self.ai_template = m.get('AiTemplate')

        if m.get('BlackWhiteListEnable') is not None:
            self.black_white_list_enable = m.get('BlackWhiteListEnable')

        if m.get('CcCustomRuleEnable') is not None:
            self.cc_custom_rule_enable = m.get('CcCustomRuleEnable')

        if m.get('CcEnable') is not None:
            self.cc_enable = m.get('CcEnable')

        if m.get('CcGlobalSwitch') is not None:
            self.cc_global_switch = m.get('CcGlobalSwitch')

        if m.get('CcTemplate') is not None:
            self.cc_template = m.get('CcTemplate')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('PreciseRuleEnable') is not None:
            self.precise_rule_enable = m.get('PreciseRuleEnable')

        if m.get('RegionBlockEnable') is not None:
            self.region_block_enable = m.get('RegionBlockEnable')

        return self

