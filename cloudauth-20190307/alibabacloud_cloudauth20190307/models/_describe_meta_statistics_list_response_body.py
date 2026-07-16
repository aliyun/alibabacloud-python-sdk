# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudauth20190307 import models as main_models
from darabonba.model import DaraModel

class DescribeMetaStatisticsListResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeMetaStatisticsListResponseBodyItems] = None,
        request_id: str = None,
    ):
        # The list of statistics information.
        self.items = items
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeMetaStatisticsListResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeMetaStatisticsListResponseBodyItems(DaraModel):
    def __init__(
        self,
        api: str = None,
        api_name: str = None,
        bill_count: int = None,
        bill_rate: str = None,
        charge_count: int = None,
        date: str = None,
        isp_name: str = None,
        no_record_count: int = None,
        passed_count: int = None,
        passed_rate: str = None,
        success_count: int = None,
        success_rate: str = None,
        total_count: int = None,
        unpassed_count: int = None,
    ):
        # The commodity (product) code.
        self.api = api
        # The name corresponding to the API. Valid values:
        # - **ID_CARD_2_META**: ID card two-element verification
        # - **ID_PERIOD**: ID card validity period verification
        # - **MOBILE_ONLINE_LENGTH**: mobile number online duration
        # - **MOBILE_ONLINE_STATUS**: mobile number online status
        # - **MOBILE_3_META_SIMPLE**: mobile number three-element verification (simple edition)
        # - **MOBILE_3_META**: mobile number three-element verification (detailed edition)
        # - **MOBILE_2_META**: mobile number two-element verification
        # - **BANK_CARD_N_META**: bank card verification (detailed edition)
        # - **MOBILE_DETECT**: phone number detection
        # - **VEHICLE_N_META**: vehicle element verification (enhanced edition)
        # - **VEHICLE_PENTA_INFO**: vehicle five-element information recognition
        # - **VEHICLE_LICENSE_INFO**: vehicle information recognition
        # - **VEHICLE_INSURE_DATE**: vehicle insurance date query
        # - **VEHICLE_CHECK**: vehicle element verification.
        self.api_name = api_name
        # The number of successful queries (billable).
        self.bill_count = bill_count
        # The query hit rate (%).
        self.bill_rate = bill_rate
        # The number of successful phone number queries (exclusive to phone number detection).
        self.charge_count = charge_count
        # The date.
        self.date = date
        # The name of the telecommunications service provider. Valid values:
        # - **CMCC**: China Mobile
        # - **CUCC**: China Unicom
        # - **CTCC**: China Telecom.
        self.isp_name = isp_name
        # The number of calls with no education information found.
        self.no_record_count = no_record_count
        # The number of authentication-passed transactions.
        self.passed_count = passed_count
        # The authentication pass rate (%).
        self.passed_rate = passed_rate
        # The number of successful calls.
        self.success_count = success_count
        # The call success rate (%).
        self.success_rate = success_rate
        # The total number of calls.
        self.total_count = total_count
        # The number of authentication-failed transactions.
        self.unpassed_count = unpassed_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api is not None:
            result['Api'] = self.api

        if self.api_name is not None:
            result['ApiName'] = self.api_name

        if self.bill_count is not None:
            result['BillCount'] = self.bill_count

        if self.bill_rate is not None:
            result['BillRate'] = self.bill_rate

        if self.charge_count is not None:
            result['ChargeCount'] = self.charge_count

        if self.date is not None:
            result['Date'] = self.date

        if self.isp_name is not None:
            result['IspName'] = self.isp_name

        if self.no_record_count is not None:
            result['NoRecordCount'] = self.no_record_count

        if self.passed_count is not None:
            result['PassedCount'] = self.passed_count

        if self.passed_rate is not None:
            result['PassedRate'] = self.passed_rate

        if self.success_count is not None:
            result['SuccessCount'] = self.success_count

        if self.success_rate is not None:
            result['SuccessRate'] = self.success_rate

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.unpassed_count is not None:
            result['UnpassedCount'] = self.unpassed_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Api') is not None:
            self.api = m.get('Api')

        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')

        if m.get('BillCount') is not None:
            self.bill_count = m.get('BillCount')

        if m.get('BillRate') is not None:
            self.bill_rate = m.get('BillRate')

        if m.get('ChargeCount') is not None:
            self.charge_count = m.get('ChargeCount')

        if m.get('Date') is not None:
            self.date = m.get('Date')

        if m.get('IspName') is not None:
            self.isp_name = m.get('IspName')

        if m.get('NoRecordCount') is not None:
            self.no_record_count = m.get('NoRecordCount')

        if m.get('PassedCount') is not None:
            self.passed_count = m.get('PassedCount')

        if m.get('PassedRate') is not None:
            self.passed_rate = m.get('PassedRate')

        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')

        if m.get('SuccessRate') is not None:
            self.success_rate = m.get('SuccessRate')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('UnpassedCount') is not None:
            self.unpassed_count = m.get('UnpassedCount')

        return self

