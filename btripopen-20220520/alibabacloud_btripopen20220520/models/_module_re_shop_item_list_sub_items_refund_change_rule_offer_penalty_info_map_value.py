# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class ModuleReShopItemListSubItemsRefundChangeRuleOfferPenaltyInfoMapValue(DaraModel):
    def __init__(
        self,
        struct: bool = None,
        cancel_fee_ind: bool = None,
        change_fee_ind: bool = None,
        upgrade_fee_ind: bool = None,
        reissue_ind: bool = None,
        penalty_type_code: int = None,
        penalty_apply_range_code: int = None,
        penalty_charge_type_code: int = None,
        fee: float = None,
        currency: str = None,
        penalty_percent: float = None,
        start_time: int = None,
        end_time: int = None,
        time_unit_code: int = None,
        title: str = None,
        dep_time: str = None,
        segment_number: str = None,
        desc_infos: Dict[str, str] = None,
    ):
        # Indicates whether the rule is applicable.
        self.struct = struct
        # Indicates whether refund is supported.
        self.cancel_fee_ind = cancel_fee_ind
        # Indicates whether date change is supported.
        self.change_fee_ind = change_fee_ind
        # Indicates whether upgrade is supported.
        self.upgrade_fee_ind = upgrade_fee_ind
        # Indicates whether reissue is supported.
        self.reissue_ind = reissue_ind
        # The rule type. Valid values:
        # 
        # - 0: Refund fee.
        # - 1: Change fee.
        # - 2: No-show penalty.
        # - 3: Other.
        # - 4: Upgrade fee.
        # - 5: Endorsement.
        # - 6: Deduction for used segments.
        # - 100: Tax refund.
        self.penalty_type_code = penalty_type_code
        # The applicability scope of the rule. Valid values:
        #    
        # - 1: All unused.
        # - 2: Partially unused.
        # - 3: Outbound.
        # - 4: Inbound.
        self.penalty_apply_range_code = penalty_apply_range_code
        # The charge method of the rule. Valid values:
        # 
        # - 0: Charged per whole trip.
        # - 1: Charged per direction.
        # - 2: Charged per segment.
        self.penalty_charge_type_code = penalty_charge_type_code
        # The fee amount.
        self.fee = fee
        # The currency of the fee.
        self.currency = currency
        # The fee percentage.
        self.penalty_percent = penalty_percent
        # The start time of the rule time range.
        self.start_time = start_time
        # The end time of the rule time range.
        self.end_time = end_time
        # The time unit. Valid values:
        # 
        # - 0: Hours.
        # - 1: Days.
        self.time_unit_code = time_unit_code
        # The rule title.
        self.title = title
        # 起飞时间
        self.dep_time = dep_time
        # 航段序号，
        # 
        # - OUTBOUND_FIRST("去程第一段")
        # 
        # - OUTBOUND_SECOND("去程第二段")
        # 
        # - INBOUND_FIRST("回程第一段")
        # 
        # - INBOUND_SECOND("回程第二段")
        self.segment_number = segment_number
        # 各类非结构化补充说明
        self.desc_infos = desc_infos

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.struct is not None:
            result['struct'] = self.struct

        if self.cancel_fee_ind is not None:
            result['cancel_fee_ind'] = self.cancel_fee_ind

        if self.change_fee_ind is not None:
            result['change_fee_ind'] = self.change_fee_ind

        if self.upgrade_fee_ind is not None:
            result['upgrade_fee_ind'] = self.upgrade_fee_ind

        if self.reissue_ind is not None:
            result['reissue_ind'] = self.reissue_ind

        if self.penalty_type_code is not None:
            result['penalty_type_code'] = self.penalty_type_code

        if self.penalty_apply_range_code is not None:
            result['penalty_apply_range_code'] = self.penalty_apply_range_code

        if self.penalty_charge_type_code is not None:
            result['penalty_charge_type_code'] = self.penalty_charge_type_code

        if self.fee is not None:
            result['fee'] = self.fee

        if self.currency is not None:
            result['currency'] = self.currency

        if self.penalty_percent is not None:
            result['penalty_percent'] = self.penalty_percent

        if self.start_time is not None:
            result['start_time'] = self.start_time

        if self.end_time is not None:
            result['end_time'] = self.end_time

        if self.time_unit_code is not None:
            result['time_unit_code'] = self.time_unit_code

        if self.title is not None:
            result['title'] = self.title

        if self.dep_time is not None:
            result['dep_time'] = self.dep_time

        if self.segment_number is not None:
            result['segment_number'] = self.segment_number

        if self.desc_infos is not None:
            result['desc_infos'] = self.desc_infos

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('struct') is not None:
            self.struct = m.get('struct')

        if m.get('cancel_fee_ind') is not None:
            self.cancel_fee_ind = m.get('cancel_fee_ind')

        if m.get('change_fee_ind') is not None:
            self.change_fee_ind = m.get('change_fee_ind')

        if m.get('upgrade_fee_ind') is not None:
            self.upgrade_fee_ind = m.get('upgrade_fee_ind')

        if m.get('reissue_ind') is not None:
            self.reissue_ind = m.get('reissue_ind')

        if m.get('penalty_type_code') is not None:
            self.penalty_type_code = m.get('penalty_type_code')

        if m.get('penalty_apply_range_code') is not None:
            self.penalty_apply_range_code = m.get('penalty_apply_range_code')

        if m.get('penalty_charge_type_code') is not None:
            self.penalty_charge_type_code = m.get('penalty_charge_type_code')

        if m.get('fee') is not None:
            self.fee = m.get('fee')

        if m.get('currency') is not None:
            self.currency = m.get('currency')

        if m.get('penalty_percent') is not None:
            self.penalty_percent = m.get('penalty_percent')

        if m.get('start_time') is not None:
            self.start_time = m.get('start_time')

        if m.get('end_time') is not None:
            self.end_time = m.get('end_time')

        if m.get('time_unit_code') is not None:
            self.time_unit_code = m.get('time_unit_code')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('dep_time') is not None:
            self.dep_time = m.get('dep_time')

        if m.get('segment_number') is not None:
            self.segment_number = m.get('segment_number')

        if m.get('desc_infos') is not None:
            self.desc_infos = m.get('desc_infos')

        return self

