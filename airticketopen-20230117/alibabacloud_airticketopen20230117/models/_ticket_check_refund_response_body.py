# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_airticketopen20230117 import models as main_models
from darabonba.model import DaraModel

class TicketCheckRefundResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.TicketCheckRefundResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.TicketCheckRefundResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class TicketCheckRefundResponseBodyData(DaraModel):
    def __init__(
        self,
        can_refund: bool = None,
        refund_amount: main_models.TicketCheckRefundResponseBodyDataRefundAmount = None,
        refund_rule: main_models.TicketCheckRefundResponseBodyDataRefundRule = None,
    ):
        self.can_refund = can_refund
        self.refund_amount = refund_amount
        self.refund_rule = refund_rule

    def validate(self):
        if self.refund_amount:
            self.refund_amount.validate()
        if self.refund_rule:
            self.refund_rule.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.can_refund is not None:
            result['CanRefund'] = self.can_refund

        if self.refund_amount is not None:
            result['RefundAmount'] = self.refund_amount.to_map()

        if self.refund_rule is not None:
            result['RefundRule'] = self.refund_rule.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanRefund') is not None:
            self.can_refund = m.get('CanRefund')

        if m.get('RefundAmount') is not None:
            temp_model = main_models.TicketCheckRefundResponseBodyDataRefundAmount()
            self.refund_amount = temp_model.from_map(m.get('RefundAmount'))

        if m.get('RefundRule') is not None:
            temp_model = main_models.TicketCheckRefundResponseBodyDataRefundRule()
            self.refund_rule = temp_model.from_map(m.get('RefundRule'))

        return self

class TicketCheckRefundResponseBodyDataRefundRule(DaraModel):
    def __init__(
        self,
        refund_stage_rules: List[main_models.TicketCheckRefundResponseBodyDataRefundRuleRefundStageRules] = None,
        refund_type: int = None,
    ):
        self.refund_stage_rules = refund_stage_rules
        self.refund_type = refund_type

    def validate(self):
        if self.refund_stage_rules:
            for v1 in self.refund_stage_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RefundStageRules'] = []
        if self.refund_stage_rules is not None:
            for k1 in self.refund_stage_rules:
                result['RefundStageRules'].append(k1.to_map() if k1 else None)

        if self.refund_type is not None:
            result['RefundType'] = self.refund_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.refund_stage_rules = []
        if m.get('RefundStageRules') is not None:
            for k1 in m.get('RefundStageRules'):
                temp_model = main_models.TicketCheckRefundResponseBodyDataRefundRuleRefundStageRules()
                self.refund_stage_rules.append(temp_model.from_map(k1))

        if m.get('RefundType') is not None:
            self.refund_type = m.get('RefundType')

        return self

class TicketCheckRefundResponseBodyDataRefundRuleRefundStageRules(DaraModel):
    def __init__(
        self,
        fee: float = None,
        fee_base: int = None,
        fee_type: int = None,
        from_: main_models.TicketCheckRefundResponseBodyDataRefundRuleRefundStageRulesFrom_ = None,
        to: main_models.TicketCheckRefundResponseBodyDataRefundRuleRefundStageRulesTo = None,
    ):
        self.fee = fee
        self.fee_base = fee_base
        self.fee_type = fee_type
        self.from_ = from_
        self.to = to

    def validate(self):
        if self.from_:
            self.from_.validate()
        if self.to:
            self.to.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fee is not None:
            result['Fee'] = self.fee

        if self.fee_base is not None:
            result['FeeBase'] = self.fee_base

        if self.fee_type is not None:
            result['FeeType'] = self.fee_type

        if self.from_ is not None:
            result['From'] = self.from_.to_map()

        if self.to is not None:
            result['To'] = self.to.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Fee') is not None:
            self.fee = m.get('Fee')

        if m.get('FeeBase') is not None:
            self.fee_base = m.get('FeeBase')

        if m.get('FeeType') is not None:
            self.fee_type = m.get('FeeType')

        if m.get('From') is not None:
            temp_model = main_models.TicketCheckRefundResponseBodyDataRefundRuleRefundStageRulesFrom_()
            self.from_ = temp_model.from_map(m.get('From'))

        if m.get('To') is not None:
            temp_model = main_models.TicketCheckRefundResponseBodyDataRefundRuleRefundStageRulesTo()
            self.to = temp_model.from_map(m.get('To'))

        return self

class TicketCheckRefundResponseBodyDataRefundRuleRefundStageRulesTo(DaraModel):
    def __init__(
        self,
        anchor: int = None,
        fixed_time: str = None,
        offset_day_of_time: str = None,
        offset_unit: int = None,
        offset_value: int = None,
    ):
        self.anchor = anchor
        self.fixed_time = fixed_time
        self.offset_day_of_time = offset_day_of_time
        self.offset_unit = offset_unit
        self.offset_value = offset_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.anchor is not None:
            result['Anchor'] = self.anchor

        if self.fixed_time is not None:
            result['FixedTime'] = self.fixed_time

        if self.offset_day_of_time is not None:
            result['OffsetDayOfTime'] = self.offset_day_of_time

        if self.offset_unit is not None:
            result['OffsetUnit'] = self.offset_unit

        if self.offset_value is not None:
            result['OffsetValue'] = self.offset_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Anchor') is not None:
            self.anchor = m.get('Anchor')

        if m.get('FixedTime') is not None:
            self.fixed_time = m.get('FixedTime')

        if m.get('OffsetDayOfTime') is not None:
            self.offset_day_of_time = m.get('OffsetDayOfTime')

        if m.get('OffsetUnit') is not None:
            self.offset_unit = m.get('OffsetUnit')

        if m.get('OffsetValue') is not None:
            self.offset_value = m.get('OffsetValue')

        return self

class TicketCheckRefundResponseBodyDataRefundRuleRefundStageRulesFrom(DaraModel):
    def __init__(
        self,
        anchor: int = None,
        fixed_time: str = None,
        offset_day_of_time: str = None,
        offset_unit: int = None,
        offset_value: int = None,
    ):
        self.anchor = anchor
        self.fixed_time = fixed_time
        self.offset_day_of_time = offset_day_of_time
        self.offset_unit = offset_unit
        self.offset_value = offset_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.anchor is not None:
            result['Anchor'] = self.anchor

        if self.fixed_time is not None:
            result['FixedTime'] = self.fixed_time

        if self.offset_day_of_time is not None:
            result['OffsetDayOfTime'] = self.offset_day_of_time

        if self.offset_unit is not None:
            result['OffsetUnit'] = self.offset_unit

        if self.offset_value is not None:
            result['OffsetValue'] = self.offset_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Anchor') is not None:
            self.anchor = m.get('Anchor')

        if m.get('FixedTime') is not None:
            self.fixed_time = m.get('FixedTime')

        if m.get('OffsetDayOfTime') is not None:
            self.offset_day_of_time = m.get('OffsetDayOfTime')

        if m.get('OffsetUnit') is not None:
            self.offset_unit = m.get('OffsetUnit')

        if m.get('OffsetValue') is not None:
            self.offset_value = m.get('OffsetValue')

        return self

class TicketCheckRefundResponseBodyDataRefundAmount(DaraModel):
    def __init__(
        self,
        amount: int = None,
        currency_code: str = None,
    ):
        self.amount = amount
        self.currency_code = currency_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.currency_code is not None:
            result['CurrencyCode'] = self.currency_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('CurrencyCode') is not None:
            self.currency_code = m.get('CurrencyCode')

        return self

