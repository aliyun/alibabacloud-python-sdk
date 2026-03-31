# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeApisecStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeApisecStatisticsResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned results.
        self.data = data
        # The request ID.
        self.request_id = request_id

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeApisecStatisticsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeApisecStatisticsResponseBodyData(DaraModel):
    def __init__(
        self,
        account: int = None,
        actioned: int = None,
        api: int = None,
        confirmed: int = None,
        domain: int = None,
        fixed: int = None,
        high: int = None,
        ignore: int = None,
        low: int = None,
        medium: int = None,
        not_fixed: int = None,
        system_fixed: int = None,
        to_be_confirmed: int = None,
        to_be_fixed: int = None,
        to_be_verified: int = None,
        today_high: str = None,
        today_low: int = None,
        today_medium: str = None,
        today_total: str = None,
        total: int = None,
    ):
        self.account = account
        # The number of handled events.
        self.actioned = actioned
        # The number of APIs.
        self.api = api
        # The number of confirmed events.
        self.confirmed = confirmed
        # The number of domain names.
        self.domain = domain
        # The number of fixed risks.
        self.fixed = fixed
        # The number of high-risk events.
        self.high = high
        # The number of ignored risks.
        self.ignore = ignore
        # The number of low-risk events.
        self.low = low
        # The number of moderate-risk events.
        self.medium = medium
        self.not_fixed = not_fixed
        self.system_fixed = system_fixed
        # The number of events to be confirmed.
        self.to_be_confirmed = to_be_confirmed
        # The number of risks to be fixed.
        self.to_be_fixed = to_be_fixed
        self.to_be_verified = to_be_verified
        # The number of new high-risk events today.
        self.today_high = today_high
        # The number of new low-risk events today.
        self.today_low = today_low
        # The number of new moderate-risk events today.
        self.today_medium = today_medium
        # The total number of new events today.
        self.today_total = today_total
        # The total number of events.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account is not None:
            result['Account'] = self.account

        if self.actioned is not None:
            result['Actioned'] = self.actioned

        if self.api is not None:
            result['Api'] = self.api

        if self.confirmed is not None:
            result['Confirmed'] = self.confirmed

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.fixed is not None:
            result['Fixed'] = self.fixed

        if self.high is not None:
            result['High'] = self.high

        if self.ignore is not None:
            result['Ignore'] = self.ignore

        if self.low is not None:
            result['Low'] = self.low

        if self.medium is not None:
            result['Medium'] = self.medium

        if self.not_fixed is not None:
            result['NotFixed'] = self.not_fixed

        if self.system_fixed is not None:
            result['SystemFixed'] = self.system_fixed

        if self.to_be_confirmed is not None:
            result['ToBeConfirmed'] = self.to_be_confirmed

        if self.to_be_fixed is not None:
            result['ToBeFixed'] = self.to_be_fixed

        if self.to_be_verified is not None:
            result['ToBeVerified'] = self.to_be_verified

        if self.today_high is not None:
            result['TodayHigh'] = self.today_high

        if self.today_low is not None:
            result['TodayLow'] = self.today_low

        if self.today_medium is not None:
            result['TodayMedium'] = self.today_medium

        if self.today_total is not None:
            result['TodayTotal'] = self.today_total

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')

        if m.get('Actioned') is not None:
            self.actioned = m.get('Actioned')

        if m.get('Api') is not None:
            self.api = m.get('Api')

        if m.get('Confirmed') is not None:
            self.confirmed = m.get('Confirmed')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Fixed') is not None:
            self.fixed = m.get('Fixed')

        if m.get('High') is not None:
            self.high = m.get('High')

        if m.get('Ignore') is not None:
            self.ignore = m.get('Ignore')

        if m.get('Low') is not None:
            self.low = m.get('Low')

        if m.get('Medium') is not None:
            self.medium = m.get('Medium')

        if m.get('NotFixed') is not None:
            self.not_fixed = m.get('NotFixed')

        if m.get('SystemFixed') is not None:
            self.system_fixed = m.get('SystemFixed')

        if m.get('ToBeConfirmed') is not None:
            self.to_be_confirmed = m.get('ToBeConfirmed')

        if m.get('ToBeFixed') is not None:
            self.to_be_fixed = m.get('ToBeFixed')

        if m.get('ToBeVerified') is not None:
            self.to_be_verified = m.get('ToBeVerified')

        if m.get('TodayHigh') is not None:
            self.today_high = m.get('TodayHigh')

        if m.get('TodayLow') is not None:
            self.today_low = m.get('TodayLow')

        if m.get('TodayMedium') is not None:
            self.today_medium = m.get('TodayMedium')

        if m.get('TodayTotal') is not None:
            self.today_total = m.get('TodayTotal')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

