# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class DescribeCreditPackageResponseBody(DaraModel):
    def __init__(
        self,
        credits_package_infos: List[main_models.DescribeCreditPackageResponseBodyCreditsPackageInfos] = None,
        is_first_purchase: bool = None,
        request_id: str = None,
        total_available_credits: str = None,
        total_count: int = None,
        total_exhausted_credit: str = None,
    ):
        self.credits_package_infos = credits_package_infos
        self.is_first_purchase = is_first_purchase
        self.request_id = request_id
        self.total_available_credits = total_available_credits
        self.total_count = total_count
        self.total_exhausted_credit = total_exhausted_credit

    def validate(self):
        if self.credits_package_infos:
            for v1 in self.credits_package_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CreditsPackageInfos'] = []
        if self.credits_package_infos is not None:
            for k1 in self.credits_package_infos:
                result['CreditsPackageInfos'].append(k1.to_map() if k1 else None)

        if self.is_first_purchase is not None:
            result['IsFirstPurchase'] = self.is_first_purchase

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_available_credits is not None:
            result['TotalAvailableCredits'] = self.total_available_credits

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.total_exhausted_credit is not None:
            result['TotalExhaustedCredit'] = self.total_exhausted_credit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.credits_package_infos = []
        if m.get('CreditsPackageInfos') is not None:
            for k1 in m.get('CreditsPackageInfos'):
                temp_model = main_models.DescribeCreditPackageResponseBodyCreditsPackageInfos()
                self.credits_package_infos.append(temp_model.from_map(k1))

        if m.get('IsFirstPurchase') is not None:
            self.is_first_purchase = m.get('IsFirstPurchase')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalAvailableCredits') is not None:
            self.total_available_credits = m.get('TotalAvailableCredits')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('TotalExhaustedCredit') is not None:
            self.total_exhausted_credit = m.get('TotalExhaustedCredit')

        return self

class DescribeCreditPackageResponseBodyCreditsPackageInfos(DaraModel):
    def __init__(
        self,
        available_credits: str = None,
        credit_package_id: str = None,
        credit_package_status: str = None,
        effective_time: str = None,
        exhausted_credits: str = None,
        expired_time: str = None,
        total_credits: str = None,
    ):
        self.available_credits = available_credits
        self.credit_package_id = credit_package_id
        self.credit_package_status = credit_package_status
        self.effective_time = effective_time
        self.exhausted_credits = exhausted_credits
        self.expired_time = expired_time
        self.total_credits = total_credits

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_credits is not None:
            result['AvailableCredits'] = self.available_credits

        if self.credit_package_id is not None:
            result['CreditPackageId'] = self.credit_package_id

        if self.credit_package_status is not None:
            result['CreditPackageStatus'] = self.credit_package_status

        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time

        if self.exhausted_credits is not None:
            result['ExhaustedCredits'] = self.exhausted_credits

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.total_credits is not None:
            result['TotalCredits'] = self.total_credits

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableCredits') is not None:
            self.available_credits = m.get('AvailableCredits')

        if m.get('CreditPackageId') is not None:
            self.credit_package_id = m.get('CreditPackageId')

        if m.get('CreditPackageStatus') is not None:
            self.credit_package_status = m.get('CreditPackageStatus')

        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')

        if m.get('ExhaustedCredits') is not None:
            self.exhausted_credits = m.get('ExhaustedCredits')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('TotalCredits') is not None:
            self.total_credits = m.get('TotalCredits')

        return self

