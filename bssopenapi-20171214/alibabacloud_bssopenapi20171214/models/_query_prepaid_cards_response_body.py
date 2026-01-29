# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class QueryPrepaidCardsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryPrepaidCardsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code returned.
        self.code = code
        # The data returned.
        self.data = data
        # The message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

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

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.QueryPrepaidCardsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryPrepaidCardsResponseBodyData(DaraModel):
    def __init__(
        self,
        prepaid_card: List[main_models.QueryPrepaidCardsResponseBodyDataPrepaidCard] = None,
    ):
        self.prepaid_card = prepaid_card

    def validate(self):
        if self.prepaid_card:
            for v1 in self.prepaid_card:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PrepaidCard'] = []
        if self.prepaid_card is not None:
            for k1 in self.prepaid_card:
                result['PrepaidCard'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.prepaid_card = []
        if m.get('PrepaidCard') is not None:
            for k1 in m.get('PrepaidCard'):
                temp_model = main_models.QueryPrepaidCardsResponseBodyDataPrepaidCard()
                self.prepaid_card.append(temp_model.from_map(k1))

        return self

class QueryPrepaidCardsResponseBodyDataPrepaidCard(DaraModel):
    def __init__(
        self,
        applicable_products: str = None,
        applicable_scenarios: str = None,
        balance: str = None,
        effective_time: str = None,
        expiry_time: str = None,
        granted_time: str = None,
        nominal_value: str = None,
        prepaid_card_id: int = None,
        prepaid_card_no: str = None,
        status: str = None,
    ):
        # The services to which the prepaid card is applicable.
        self.applicable_products = applicable_products
        # The scenario to which the prepaid card is applicable.
        self.applicable_scenarios = applicable_scenarios
        # The balance of the prepaid card.
        self.balance = balance
        # The time when the prepaid card took effect.
        self.effective_time = effective_time
        # The time when the prepaid card expired.
        self.expiry_time = expiry_time
        # The time when the prepaid card was issued.
        self.granted_time = granted_time
        # The nominal value of the prepaid card.
        self.nominal_value = nominal_value
        # The ID of the prepaid card.
        self.prepaid_card_id = prepaid_card_id
        # The number of the prepaid card.
        self.prepaid_card_no = prepaid_card_no
        # The status of the prepaid card. Valid values:
        # 
        # *   Available: The prepaid card is valid.
        # *   Expired: The prepaid card expired.
        # *   Cancelled: The prepaid card is invalid.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.applicable_products is not None:
            result['ApplicableProducts'] = self.applicable_products

        if self.applicable_scenarios is not None:
            result['ApplicableScenarios'] = self.applicable_scenarios

        if self.balance is not None:
            result['Balance'] = self.balance

        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time

        if self.expiry_time is not None:
            result['ExpiryTime'] = self.expiry_time

        if self.granted_time is not None:
            result['GrantedTime'] = self.granted_time

        if self.nominal_value is not None:
            result['NominalValue'] = self.nominal_value

        if self.prepaid_card_id is not None:
            result['PrepaidCardId'] = self.prepaid_card_id

        if self.prepaid_card_no is not None:
            result['PrepaidCardNo'] = self.prepaid_card_no

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicableProducts') is not None:
            self.applicable_products = m.get('ApplicableProducts')

        if m.get('ApplicableScenarios') is not None:
            self.applicable_scenarios = m.get('ApplicableScenarios')

        if m.get('Balance') is not None:
            self.balance = m.get('Balance')

        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')

        if m.get('ExpiryTime') is not None:
            self.expiry_time = m.get('ExpiryTime')

        if m.get('GrantedTime') is not None:
            self.granted_time = m.get('GrantedTime')

        if m.get('NominalValue') is not None:
            self.nominal_value = m.get('NominalValue')

        if m.get('PrepaidCardId') is not None:
            self.prepaid_card_id = m.get('PrepaidCardId')

        if m.get('PrepaidCardNo') is not None:
            self.prepaid_card_no = m.get('PrepaidCardNo')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

