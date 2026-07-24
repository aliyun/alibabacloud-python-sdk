# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_airticketopen20230117 import models as main_models
from darabonba.model import DaraModel

class DataSolutionListSegmentRefundChangeRuleMappingListRefundChangeRuleMapValue(DaraModel):
    def __init__(
        self,
        refund_rule_all_unused_list: List[main_models.DataSolutionListSegmentRefundChangeRuleMappingListRefundChangeRuleMapValueRefundRuleAllUnusedList] = None,
        refund_rule_part_unused_list: List[main_models.DataSolutionListSegmentRefundChangeRuleMappingListRefundChangeRuleMapValueRefundRulePartUnusedList] = None,
        change_rule_in_unused_list: List[main_models.DataSolutionListSegmentRefundChangeRuleMappingListRefundChangeRuleMapValueChangeRuleInUnusedList] = None,
        change_rule_out_unused_list: List[main_models.DataSolutionListSegmentRefundChangeRuleMappingListRefundChangeRuleMapValueChangeRuleOutUnusedList] = None,
    ):
        # Fully unused refund rules
        self.refund_rule_all_unused_list = refund_rule_all_unused_list
        # Partially unused refund rules
        self.refund_rule_part_unused_list = refund_rule_part_unused_list
        # Return/inbound unused change rules
        self.change_rule_in_unused_list = change_rule_in_unused_list
        # Outbound unused change rules
        self.change_rule_out_unused_list = change_rule_out_unused_list

    def validate(self):
        if self.refund_rule_all_unused_list:
            for v1 in self.refund_rule_all_unused_list:
                 if v1:
                    v1.validate()
        if self.refund_rule_part_unused_list:
            for v1 in self.refund_rule_part_unused_list:
                 if v1:
                    v1.validate()
        if self.change_rule_in_unused_list:
            for v1 in self.change_rule_in_unused_list:
                 if v1:
                    v1.validate()
        if self.change_rule_out_unused_list:
            for v1 in self.change_rule_out_unused_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['refund_rule_all_unused_list'] = []
        if self.refund_rule_all_unused_list is not None:
            for k1 in self.refund_rule_all_unused_list:
                result['refund_rule_all_unused_list'].append(k1.to_map() if k1 else None)

        result['refund_rule_part_unused_list'] = []
        if self.refund_rule_part_unused_list is not None:
            for k1 in self.refund_rule_part_unused_list:
                result['refund_rule_part_unused_list'].append(k1.to_map() if k1 else None)

        result['change_rule_in_unused_list'] = []
        if self.change_rule_in_unused_list is not None:
            for k1 in self.change_rule_in_unused_list:
                result['change_rule_in_unused_list'].append(k1.to_map() if k1 else None)

        result['change_rule_out_unused_list'] = []
        if self.change_rule_out_unused_list is not None:
            for k1 in self.change_rule_out_unused_list:
                result['change_rule_out_unused_list'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.refund_rule_all_unused_list = []
        if m.get('refund_rule_all_unused_list') is not None:
            for k1 in m.get('refund_rule_all_unused_list'):
                temp_model = main_models.DataSolutionListSegmentRefundChangeRuleMappingListRefundChangeRuleMapValueRefundRuleAllUnusedList()
                self.refund_rule_all_unused_list.append(temp_model.from_map(k1))

        self.refund_rule_part_unused_list = []
        if m.get('refund_rule_part_unused_list') is not None:
            for k1 in m.get('refund_rule_part_unused_list'):
                temp_model = main_models.DataSolutionListSegmentRefundChangeRuleMappingListRefundChangeRuleMapValueRefundRulePartUnusedList()
                self.refund_rule_part_unused_list.append(temp_model.from_map(k1))

        self.change_rule_in_unused_list = []
        if m.get('change_rule_in_unused_list') is not None:
            for k1 in m.get('change_rule_in_unused_list'):
                temp_model = main_models.DataSolutionListSegmentRefundChangeRuleMappingListRefundChangeRuleMapValueChangeRuleInUnusedList()
                self.change_rule_in_unused_list.append(temp_model.from_map(k1))

        self.change_rule_out_unused_list = []
        if m.get('change_rule_out_unused_list') is not None:
            for k1 in m.get('change_rule_out_unused_list'):
                temp_model = main_models.DataSolutionListSegmentRefundChangeRuleMappingListRefundChangeRuleMapValueChangeRuleOutUnusedList()
                self.change_rule_out_unused_list.append(temp_model.from_map(k1))

        return self

class DataSolutionListSegmentRefundChangeRuleMappingListRefundChangeRuleMapValueChangeRuleOutUnusedList(DaraModel):
    def __init__(
        self,
        type: int = None,
        time_unit: str = None,
        rule_start_time: int = None,
        rule_end_time: int = None,
        can_change: bool = None,
        change_fee: float = None,
    ):
        # Change rule applicable journey usage type 2: outbound unused; 3: return/inbound unused
        self.type = type
        # Time unit: day/hour
        self.time_unit = time_unit
        # Start time of the refund time interval applicable to this refund rule, unit (day/hour)
        self.rule_start_time = rule_start_time
        # End time of the refund time interval applicable to this refund rule, unit (day/hour)
        self.rule_end_time = rule_end_time
        # Whether rebooking is allowed X-Y hours (days) before departure
        self.can_change = can_change
        # Rebooking fee X-Y hours (days) before departure
        self.change_fee = change_fee

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['type'] = self.type

        if self.time_unit is not None:
            result['time_unit'] = self.time_unit

        if self.rule_start_time is not None:
            result['rule_start_time'] = self.rule_start_time

        if self.rule_end_time is not None:
            result['rule_end_time'] = self.rule_end_time

        if self.can_change is not None:
            result['can_change'] = self.can_change

        if self.change_fee is not None:
            result['change_fee'] = self.change_fee

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('time_unit') is not None:
            self.time_unit = m.get('time_unit')

        if m.get('rule_start_time') is not None:
            self.rule_start_time = m.get('rule_start_time')

        if m.get('rule_end_time') is not None:
            self.rule_end_time = m.get('rule_end_time')

        if m.get('can_change') is not None:
            self.can_change = m.get('can_change')

        if m.get('change_fee') is not None:
            self.change_fee = m.get('change_fee')

        return self

class DataSolutionListSegmentRefundChangeRuleMappingListRefundChangeRuleMapValueChangeRuleInUnusedList(DaraModel):
    def __init__(
        self,
        type: int = None,
        time_unit: str = None,
        rule_start_time: int = None,
        rule_end_time: int = None,
        can_change: bool = None,
        change_fee: float = None,
    ):
        # Change rule applicable journey usage type 2: outbound unused; 3: return/inbound unused
        self.type = type
        # Time unit: day/hour
        self.time_unit = time_unit
        # Start time of the refund time interval applicable to this refund rule, unit (day/hour)
        self.rule_start_time = rule_start_time
        # End time of the refund time interval applicable to this refund rule, unit (day/hour)
        self.rule_end_time = rule_end_time
        # Whether rebooking is allowed X-Y hours (days) before departure
        self.can_change = can_change
        # Rebooking fee X-Y hours (days) before departure
        self.change_fee = change_fee

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['type'] = self.type

        if self.time_unit is not None:
            result['time_unit'] = self.time_unit

        if self.rule_start_time is not None:
            result['rule_start_time'] = self.rule_start_time

        if self.rule_end_time is not None:
            result['rule_end_time'] = self.rule_end_time

        if self.can_change is not None:
            result['can_change'] = self.can_change

        if self.change_fee is not None:
            result['change_fee'] = self.change_fee

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('time_unit') is not None:
            self.time_unit = m.get('time_unit')

        if m.get('rule_start_time') is not None:
            self.rule_start_time = m.get('rule_start_time')

        if m.get('rule_end_time') is not None:
            self.rule_end_time = m.get('rule_end_time')

        if m.get('can_change') is not None:
            self.can_change = m.get('can_change')

        if m.get('change_fee') is not None:
            self.change_fee = m.get('change_fee')

        return self

class DataSolutionListSegmentRefundChangeRuleMappingListRefundChangeRuleMapValueRefundRulePartUnusedList(DaraModel):
    def __init__(
        self,
        type: int = None,
        time_unit: str = None,
        rule_start_time: int = None,
        rule_end_time: int = None,
        can_refund: bool = None,
        refund_fee: float = None,
        can_return_all_tax: bool = None,
        return_part_tax_fee: float = None,
    ):
        # Refund rule applicable journey usage type 0: fully unused; 1: partially unused
        self.type = type
        # Time unit: day/hour
        self.time_unit = time_unit
        # Start time of the refund time interval applicable to this refund rule, unit (day/hour)
        self.rule_start_time = rule_start_time
        # End time of the refund time interval applicable to this refund rule, unit (day/hour)
        self.rule_end_time = rule_end_time
        # Whether refund is allowed X-Y hours (days) before departure
        self.can_refund = can_refund
        # Refund fee X-Y hours (days) before departure
        self.refund_fee = refund_fee
        # Whether full tax refund is available X-Y hours (days) before departure
        self.can_return_all_tax = can_return_all_tax
        # Partial tax refund amount X-Y hours (days) before departure
        self.return_part_tax_fee = return_part_tax_fee

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['type'] = self.type

        if self.time_unit is not None:
            result['time_unit'] = self.time_unit

        if self.rule_start_time is not None:
            result['rule_start_time'] = self.rule_start_time

        if self.rule_end_time is not None:
            result['rule_end_time'] = self.rule_end_time

        if self.can_refund is not None:
            result['can_refund'] = self.can_refund

        if self.refund_fee is not None:
            result['refund_fee'] = self.refund_fee

        if self.can_return_all_tax is not None:
            result['can_return_all_tax'] = self.can_return_all_tax

        if self.return_part_tax_fee is not None:
            result['return_part_tax_fee'] = self.return_part_tax_fee

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('time_unit') is not None:
            self.time_unit = m.get('time_unit')

        if m.get('rule_start_time') is not None:
            self.rule_start_time = m.get('rule_start_time')

        if m.get('rule_end_time') is not None:
            self.rule_end_time = m.get('rule_end_time')

        if m.get('can_refund') is not None:
            self.can_refund = m.get('can_refund')

        if m.get('refund_fee') is not None:
            self.refund_fee = m.get('refund_fee')

        if m.get('can_return_all_tax') is not None:
            self.can_return_all_tax = m.get('can_return_all_tax')

        if m.get('return_part_tax_fee') is not None:
            self.return_part_tax_fee = m.get('return_part_tax_fee')

        return self



class DataSolutionListSegmentRefundChangeRuleMappingListRefundChangeRuleMapValueRefundRuleAllUnusedList(DaraModel):
    def __init__(
        self,
        type: int = None,
        time_unit: str = None,
        rule_start_time: int = None,
        rule_end_time: int = None,
        can_refund: bool = None,
        refund_fee: float = None,
        can_return_all_tax: bool = None,
        return_part_tax_fee: float = None,
    ):
        # Refund rule applicable journey usage type 0: fully unused; 1: partially unused
        self.type = type
        # Time unit: day/hour
        self.time_unit = time_unit
        # Start time of the refund time interval applicable to this refund rule, unit (day/hour)
        self.rule_start_time = rule_start_time
        # End time of the refund time interval applicable to this refund rule, unit (day/hour)
        self.rule_end_time = rule_end_time
        # Whether refund is allowed X-Y hours (days) before departure
        self.can_refund = can_refund
        # Refund fee X-Y hours (days) before departure
        self.refund_fee = refund_fee
        # Whether full tax refund is available X-Y hours (days) before departure
        self.can_return_all_tax = can_return_all_tax
        # Partial tax refund amount X-Y hours (days) before departure
        self.return_part_tax_fee = return_part_tax_fee

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['type'] = self.type

        if self.time_unit is not None:
            result['time_unit'] = self.time_unit

        if self.rule_start_time is not None:
            result['rule_start_time'] = self.rule_start_time

        if self.rule_end_time is not None:
            result['rule_end_time'] = self.rule_end_time

        if self.can_refund is not None:
            result['can_refund'] = self.can_refund

        if self.refund_fee is not None:
            result['refund_fee'] = self.refund_fee

        if self.can_return_all_tax is not None:
            result['can_return_all_tax'] = self.can_return_all_tax

        if self.return_part_tax_fee is not None:
            result['return_part_tax_fee'] = self.return_part_tax_fee

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('time_unit') is not None:
            self.time_unit = m.get('time_unit')

        if m.get('rule_start_time') is not None:
            self.rule_start_time = m.get('rule_start_time')

        if m.get('rule_end_time') is not None:
            self.rule_end_time = m.get('rule_end_time')

        if m.get('can_refund') is not None:
            self.can_refund = m.get('can_refund')

        if m.get('refund_fee') is not None:
            self.refund_fee = m.get('refund_fee')

        if m.get('can_return_all_tax') is not None:
            self.can_return_all_tax = m.get('can_return_all_tax')

        if m.get('return_part_tax_fee') is not None:
            self.return_part_tax_fee = m.get('return_part_tax_fee')

        return self

