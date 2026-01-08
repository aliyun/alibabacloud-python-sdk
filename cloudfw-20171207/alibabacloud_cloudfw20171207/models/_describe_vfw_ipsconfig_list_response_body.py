# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeVfwIPSConfigListResponseBody(DaraModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        vfw_ips_switch_config_list: List[main_models.DescribeVfwIPSConfigListResponseBodyVfwIpsSwitchConfigList] = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count
        self.vfw_ips_switch_config_list = vfw_ips_switch_config_list

    def validate(self):
        if self.vfw_ips_switch_config_list:
            for v1 in self.vfw_ips_switch_config_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['VfwIpsSwitchConfigList'] = []
        if self.vfw_ips_switch_config_list is not None:
            for k1 in self.vfw_ips_switch_config_list:
                result['VfwIpsSwitchConfigList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.vfw_ips_switch_config_list = []
        if m.get('VfwIpsSwitchConfigList') is not None:
            for k1 in m.get('VfwIpsSwitchConfigList'):
                temp_model = main_models.DescribeVfwIPSConfigListResponseBodyVfwIpsSwitchConfigList()
                self.vfw_ips_switch_config_list.append(temp_model.from_map(k1))

        return self

class DescribeVfwIPSConfigListResponseBodyVfwIpsSwitchConfigList(DaraModel):
    def __init__(
        self,
        basic_rules: int = None,
        member_uid: str = None,
        patch_rules: int = None,
        rule_class: int = None,
        run_mode: int = None,
        vpc_firewall_id: str = None,
        vpc_firewall_id_list: List[str] = None,
        vpc_firewall_name: str = None,
    ):
        self.basic_rules = basic_rules
        self.member_uid = member_uid
        self.patch_rules = patch_rules
        self.rule_class = rule_class
        self.run_mode = run_mode
        self.vpc_firewall_id = vpc_firewall_id
        self.vpc_firewall_id_list = vpc_firewall_id_list
        self.vpc_firewall_name = vpc_firewall_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.basic_rules is not None:
            result['BasicRules'] = self.basic_rules

        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid

        if self.patch_rules is not None:
            result['PatchRules'] = self.patch_rules

        if self.rule_class is not None:
            result['RuleClass'] = self.rule_class

        if self.run_mode is not None:
            result['RunMode'] = self.run_mode

        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id

        if self.vpc_firewall_id_list is not None:
            result['VpcFirewallIdList'] = self.vpc_firewall_id_list

        if self.vpc_firewall_name is not None:
            result['VpcFirewallName'] = self.vpc_firewall_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BasicRules') is not None:
            self.basic_rules = m.get('BasicRules')

        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')

        if m.get('PatchRules') is not None:
            self.patch_rules = m.get('PatchRules')

        if m.get('RuleClass') is not None:
            self.rule_class = m.get('RuleClass')

        if m.get('RunMode') is not None:
            self.run_mode = m.get('RunMode')

        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')

        if m.get('VpcFirewallIdList') is not None:
            self.vpc_firewall_id_list = m.get('VpcFirewallIdList')

        if m.get('VpcFirewallName') is not None:
            self.vpc_firewall_name = m.get('VpcFirewallName')

        return self

